"""
scrape_only.py — Raccolta lead per domani (SOLO scraping + email)
=================================================================
TARGET: N EMAIL NUOVE (non N business).
FILTRI: nome + sito web + email — tripla deduplicazione.
COMPENSAZIONE automatica: se trova email duplicate, continua a cercare altri.

Uso:
  python scrape_only.py --target 300
  python scrape_only.py --target 300 --fresh   # ignora checkpoint, riparte da zero
"""

import argparse
import csv
import json
import os
import sys
from pathlib import Path

_SESSION_CP  = Path(__file__).parent / "scrape_only_session.json"
_RAW_CP      = Path(__file__).parent / "scrape_only_raw.json"     # business grezzi pre-extractor

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")


def _carica_memoria(output_path: Path, db_path: Path):
    """Carica nomi, siti e email già noti da CSV e DB."""
    nomi_noti, siti_noti, email_note = set(), set(), set()
    if output_path.exists():
        with open(output_path, newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                if row.get("page_name"): nomi_noti.add(row["page_name"].strip().lower())
                if row.get("website"):   siti_noti.add(row["website"].strip().lower().rstrip("/"))
                if row.get("email"):     email_note.add(row["email"].strip().lower())

    if db_path.exists():
        import sqlite3
        with sqlite3.connect(db_path) as conn:
            try:
                for (nome, sito, email) in conn.execute(
                    "SELECT page_name, website, email FROM leads_contattati"
                ).fetchall():
                    if nome:  nomi_noti.add(nome.strip().lower())
                    if sito:  siti_noti.add(sito.strip().lower().rstrip("/"))
                    if email: email_note.add(email.strip().lower())
            except Exception:
                pass
    return nomi_noti, siti_noti, email_note


def main():
    parser = argparse.ArgumentParser(description="Scraper-only — raccolta email nuove per domani")
    parser.add_argument("--target",   type=int, default=300,
                        help="Email NUOVE da trovare (default: 300). Compensa automaticamente i duplicati.")
    parser.add_argument("--output",   type=str, default="leads_verificati.csv",
                        help="File CSV output (default: leads_verificati.csv)")
    parser.add_argument("--use-maps", action="store_true", help="Forza Maps Browser")
    parser.add_argument("--no-maps",  action="store_true", help="Salta Maps Browser")
    parser.add_argument("--fresh",    action="store_true", help="Ignora checkpoint, riparte da zero")
    args = parser.parse_args()

    apify_token    = os.getenv("APIFY_API_TOKEN",       "").strip()
    outscraper_key = os.getenv("OUTSCRAPER_API_KEY",    "").strip()
    google_key     = os.getenv("GOOGLE_PLACES_API_KEY", "").strip()

    from agents.maps_browser_scraper import MapsBrowserScraper, SESSION_DIR, SCRAPE_CHECKPOINT
    from agents.extractor import EmailExtractorAgent, EXTRACTOR_CHECKPOINT

    scrapers = []
    if apify_token:
        from agents.apify_scraper import ApifyScraper
        scrapers.append(("Apify Google Maps", ApifyScraper(apify_token)))
    if outscraper_key:
        from agents.outscraper_scraper import OutscraperScraper
        scrapers.append(("Outscraper", OutscraperScraper(outscraper_key)))
    if google_key:
        from agents.google_scraper import GooglePlacesScraper
        scrapers.append(("Google Places API", GooglePlacesScraper(google_key)))
    if SESSION_DIR.exists() and not args.no_maps:
        scrapers.append(("Maps Browser", MapsBrowserScraper()))

    if not scrapers:
        print("\n✗  Nessuno scraper disponibile.")
        print("   Configura APIFY_API_TOKEN o avvia Maps Browser almeno una volta.")
        sys.exit(1)

    print(f"\n{'='*64}")
    print(f"  SCRAPE-ONLY — raccolta {args.target} email NUOVE per domani")
    print(f"  Output: {args.output}")
    print(f"  Scrapers: {', '.join(s[0] for s in scrapers)}")
    print(f"  Filtri: nome + sito + email (compensazione automatica duplicati)")
    print(f"{'='*64}\n")

    output_path = Path(__file__).parent / args.output
    db_path     = Path(__file__).parent / "leads.db"

    # ── Pulizia checkpoint se --fresh ────────────────────────────────────────
    if args.fresh:
        for cp in [SCRAPE_CHECKPOINT, EXTRACTOR_CHECKPOINT, _SESSION_CP, _RAW_CP]:
            if cp.exists():
                cp.unlink()
        print("[FRESH] Checkpoint rimossi — parto da zero\n")

    # ── Carica memoria: nomi, siti, email già noti ───────────────────────────
    nomi_noti, siti_noti, email_note = _carica_memoria(output_path, db_path)
    print(f"[MEMORIA] {len(email_note)} email già note | {len(nomi_noti)} nomi | {len(siti_noti)} siti\n")

    # ── Funzioni dedup ────────────────────────────────────────────────────────

    def _e_nuovo_business(b: dict) -> bool:
        """
        FILTRO 1+2: business nuovo per nome, sito e (se disponibile) email diretta.
        Blocca PRIMA di andare sul sito — risparmia tempo extractor.
        """
        nome  = (b.get("page_name") or "").strip().lower()
        sito  = (b.get("website") or "").strip().lower().rstrip("/")
        email = (b.get("email_diretta") or "").strip().lower()
        if nome and nome in nomi_noti:   return False
        if sito and sito in siti_noti:   return False
        if email and email in email_note: return False
        return True

    def _aggiorna_memoria_business(b: dict):
        """Segna il business come 'già visto' per evitare duplicati tra batch."""
        if b.get("page_name"): nomi_noti.add(b["page_name"].strip().lower())
        if b.get("website"):   siti_noti.add(b["website"].strip().lower().rstrip("/"))

    # ── Istanza extractor (unica per tutto il run) ────────────────────────────
    extractor = EmailExtractorAgent()

    # ── Risultato finale — carica checkpoint se disponibile ──────────────────
    leads_finali = []
    email_finali = set()

    if _SESSION_CP.exists() and not args.fresh:
        try:
            saved = json.loads(_SESSION_CP.read_text(encoding="utf-8"))
            leads_finali = saved.get("leads", [])
            email_finali = set(saved.get("emails", []))
            print(f"[CHECKPOINT] Ripreso: {len(leads_finali)}/{args.target} email già trovate — continuo da qui\n")
            # Aggiorna memoria in-memory coi lead già trovati
            for lead in leads_finali:
                if lead.get("page_name"): nomi_noti.add(lead["page_name"].strip().lower())
                if lead.get("website"):   siti_noti.add(lead["website"].strip().lower().rstrip("/"))
                if lead.get("email"):     email_note.add(lead["email"].strip().lower())
        except Exception as e:
            print(f"[CHECKPOINT] Errore nel caricamento ({e}) — parto da zero")
            leads_finali, email_finali = [], set()

    BATCH_FACTOR = 4.0  # scrapa 4x per compensare: ~3x nome/sito + ~1x email

    # ── Recovery raw businesses (stop durante extractor) ────────────────────────
    _raw_recovery_batch = None
    _raw_recovery_scraper = None
    if _RAW_CP.exists() and not args.fresh:
        try:
            _raw_saved = json.loads(_RAW_CP.read_text(encoding="utf-8"))
            _raw_recovery_batch   = _raw_saved.get("business", [])
            _raw_recovery_scraper = _raw_saved.get("scraper", "")
            print(f"[RAW-CP] Recovery: {len(_raw_recovery_batch)} business pronti per EXTRACTOR "
                  f"(scraper: {_raw_recovery_scraper}) — salto scraping\n")
        except Exception as e:
            print(f"[RAW-CP] Errore caricamento ({e}) — riscraping")
            _raw_recovery_batch = None

    # ── Loop principale: scrapa → estrai → filtra email → se sotto target ripeti
    for scraper_nome, scraper_obj in scrapers:
        giro = 0

        while len(leads_finali) < args.target:
            giro += 1
            mancanti     = args.target - len(leads_finali)
            target_giro  = int(mancanti * BATCH_FACTOR)

            # Recovery: usa business già trovati pre-crash invece di riscraping
            if _raw_recovery_batch and (not _raw_recovery_scraper or _raw_recovery_scraper == scraper_nome):
                raw_nuovi = _raw_recovery_batch
                _raw_recovery_batch = None  # usa solo al primo giro
                print(f"\n[{scraper_nome}] Giro {giro}: RECOVERY {len(raw_nuovi)} business da checkpoint raw "
                      f"(mancano {mancanti} email | trovate {len(leads_finali)}/{args.target})...")
                for b in raw_nuovi:
                    _aggiorna_memoria_business(b)
            else:
                print(f"\n[{scraper_nome}] Giro {giro}: cerco {target_giro} business "
                      f"(mancano {mancanti} email nuove | trovate {len(leads_finali)}/{args.target})...")

                try:
                    raw = scraper_obj.run(target=target_giro)
                except Exception as e:
                    print(f"[{scraper_nome}] ✗ Errore: {e}")
                    break

                if not raw:
                    print(f"[{scraper_nome}] 0 risultati → scraper esaurito")
                    break

                # FILTRO 1+2: per nome, sito, email diretta — PRIMA dell'extractor
                raw_nuovi = [b for b in raw if _e_nuovo_business(b)]
                saltati   = len(raw) - len(raw_nuovi)
                print(f"[{scraper_nome}] ✓ {len(raw)} trovati | {saltati} già noti (nome/sito/email) "
                      f"| {len(raw_nuovi)} nuovi da estrarre")

                # Aggiorna memoria in-memory per il prossimo batch
                for b in raw_nuovi:
                    _aggiorna_memoria_business(b)

                if not raw_nuovi:
                    # Tutti i risultati già noti → scraper esaurito, non ha senso riprovare
                    print(f"[{scraper_nome}] 0 nuovi su {len(raw)} trovati — scraper esaurito, passo al prossimo")
                    break

            # Salva business grezzi PRIMA dell'extractor (recovery crash durante estrazione)
            _RAW_CP.write_text(
                json.dumps({"business": raw_nuovi, "scraper": scraper_nome}, ensure_ascii=False),
                encoding="utf-8"
            )

            # Estrazione email
            con_diretta = [b for b in raw_nuovi if b.get("email_diretta")]
            senza       = [b for b in raw_nuovi if not b.get("email_diretta")]

            batch_leads = []
            for b in con_diretta:
                b["email"] = b.pop("email_diretta")
                batch_leads.append(b)
            if senza:
                print(f"[EXTRACTOR] Estraggo email da {len(senza)} siti nuovi...")
                batch_leads.extend(extractor.run(senza))

            # FILTRO 3: per email — il vero test di unicità
            nuovi_giro      = 0
            duplicati_email = 0
            for lead in batch_leads:
                email = lead.get("email", "").strip().lower()
                if not email:
                    continue
                if email in email_note or email in email_finali:
                    duplicati_email += 1
                    continue  # email già nota → scarta E COMPENSA (il while continua)
                leads_finali.append(lead)
                email_finali.add(email)
                nuovi_giro += 1

            print(f"[FILTRO EMAIL] +{nuovi_giro} email nuove | {duplicati_email} duplicate scartate "
                  f"→ Totale: {len(leads_finali)}/{args.target}")

            if duplicati_email > 0:
                print(f"[COMPENSA] {duplicati_email} duplicati → continuo a cercare per raggiungere il target")

            # ── Salva checkpoint dopo ogni batch (ripristino automatico su crash) ──
            if leads_finali:
                _SESSION_CP.write_text(
                    json.dumps({"leads": leads_finali, "emails": list(email_finali)},
                               ensure_ascii=False),
                    encoding="utf-8"
                )
                print(f"[CP] Checkpoint salvato: {len(leads_finali)} lead")

            # Scraper esaurito (trovato meno del 30% di quanto chiesto)
            if len(raw) < target_giro * 0.3 and len(leads_finali) < args.target:
                print(f"[{scraper_nome}] Scraper esaurito — passo al prossimo")
                break

        if len(leads_finali) >= args.target:
            break

        print(f"[{scraper_nome}] Fine — {len(leads_finali)}/{args.target} email nuove → prossimo scraper")

    if not leads_finali:
        print("\n✗ Nessuna email nuova trovata. Tutti gli scraper esauriti.")
        sys.exit(1)

    # ── Salva CSV ─────────────────────────────────────────────────────────────
    fields    = ["page_name", "email", "settore", "citta", "website"]
    da_salvare = leads_finali[:args.target]

    file_esiste = output_path.exists()
    with open(output_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if not file_esiste:
            writer.writeheader()
        for lead in da_salvare:
            writer.writerow({k: lead.get(k, "") for k in fields})

    # Rimuovi checkpoint residui (solo dopo salvataggio CSV riuscito)
    for cp in [SCRAPE_CHECKPOINT, EXTRACTOR_CHECKPOINT, _SESSION_CP, _RAW_CP]:
        if cp.exists():
            cp.unlink()

    print(f"\n{'='*64}")
    print(f"  ✓ {len(da_salvare)} email NUOVE salvate → {args.output}")
    print(f"{'='*64}")
    print(f"\nDomani mattina esegui:")
    print(f"  python run.py --csv {args.output} --target {len(da_salvare)} --mode completo\n")


if __name__ == "__main__":
    main()
