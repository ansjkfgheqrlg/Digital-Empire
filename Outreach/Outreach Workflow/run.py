"""
Digital Empire — Outreach Automatico 300/giorno v2.0
=====================================================
Sistema multi-agente a 6 team. Costo: $0/giorno.

WORKFLOW CONSIGLIATO (2 fasi separate):
  Notte  02:00  →  python run.py --mode genera          # Genera 300 email, le salva nel DB
  Mattina 09:00  →  python run.py --mode invia           # Invia dal DB in orario business

ALTRI USI:
  python run.py --mode genera --target 50    # Genera solo 50 email
  python run.py --anteprima                  # Genera e mostra senza inviare (test)
  python run.py --target 10 --anteprima      # Test rapido su 10 email
  python run.py                              # Genera + invia subito (modalità legacy)

SCHEDULING WINDOWS (Task Scheduler):
  Attività 1: ogni giorno 02:00  →  python run.py --mode genera
  Attività 2: lun-ven    09:00  →  python run.py --mode invia
"""

import argparse
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from dotenv import load_dotenv

# ────────────────────────────────────────────────────────────────────────────
# Carica .env dalla cartella Outreach/
# ────────────────────────────────────────────────────────────────────────────
load_dotenv(Path(__file__).parent / ".env")


VARIABILI_RICHIESTE = {
    "OPENROUTER_API_KEY": "API key OpenRouter per NVIDIA Nemotron (openrouter.ai)",
    "GMAIL_USER":         "Il tuo Gmail (es. max.infoproducer@gmail.com)",
    "GMAIL_APP_PASSWORD": "App Password Gmail 16 caratteri (SETUP.md sezione 3)",
}

# Almeno una di queste deve essere presente
VARIABILI_SCRAPER = {
    "APIFY_API_TOKEN":       "API token Apify (consigliato, free tier) — apify.com → Settings → Integrations → API Token",
    "OUTSCRAPER_API_KEY":    "API key Outscraper — outscraper.com → Dashboard → API Key",
    "GOOGLE_PLACES_API_KEY": "API key Google Places — console.cloud.google.com → Enable Places API",
    "FB_ACCESS_TOKEN":       "Token Facebook Ad Library — developers.facebook.com/tools/explorer",
}


def verifica_configurazione() -> dict:
    """
    Verifica che le variabili d'ambiente obbligatorie siano presenti.
    Per lo scraper basta avere GOOGLE_PLACES_API_KEY OPPURE FB_ACCESS_TOKEN.
    """
    config = {k: os.getenv(k, "") for k in {**VARIABILI_RICHIESTE, **VARIABILI_SCRAPER}}
    mancanti = {k: v for k, v in VARIABILI_RICHIESTE.items() if not config.get(k)}

    if mancanti:
        print("\n" + "=" * 60)
        print("  CONFIGURAZIONE INCOMPLETA — leggi SETUP.md")
        print("=" * 60)
        print("\nVariabili mancanti nel file .env:\n")
        for var, desc in mancanti.items():
            print(f"  {var}\n    → {desc}\n")
        print("Copia .env.example in .env e compila i valori mancanti.\n")
        sys.exit(1)

    # Verifica scraper: almeno uno tra Apify, Outscraper, Google Places, Facebook
    ha_apify      = bool(config.get("APIFY_API_TOKEN", "").strip())
    ha_outscraper = bool(config.get("OUTSCRAPER_API_KEY", "").strip())
    ha_google     = bool(config.get("GOOGLE_PLACES_API_KEY", "").strip())
    ha_fb         = bool(config.get("FB_ACCESS_TOKEN", "").strip())
    if not ha_apify and not ha_outscraper and not ha_google and not ha_fb:
        print("\n" + "=" * 60)
        print("  SCRAPER NON CONFIGURATO")
        print("=" * 60)
        print("\nServe almeno uno dei seguenti nel .env:\n")
        for var, desc in VARIABILI_SCRAPER.items():
            print(f"  {var}\n    → {desc}\n")
        print("Consigliato: APIFY_API_TOKEN (free tier, zero billing setup)\n")
        sys.exit(1)

    # Mostra scraper primario (Maps Browser se sessione presente) + fallback disponibili
    from agents.maps_browser_scraper import SESSION_DIR
    if SESSION_DIR.exists():
        print("[CONFIG] Scraper primario: Google Maps Browser (sessione attiva)")
        fallbacks = []
        if ha_apify:      fallbacks.append("Apify")
        if ha_outscraper: fallbacks.append("Outscraper")
        if ha_google:     fallbacks.append("Google Places")
        if fallbacks:
            print(f"[CONFIG] Fallback: {' → '.join(fallbacks)}")
    elif ha_apify:
        print("[CONFIG] Scraper: Apify ✓")
    elif ha_outscraper:
        print("[CONFIG] Scraper: Outscraper ✓")
    elif ha_google:
        print("[CONFIG] Scraper: Google Places API ✓")
    else:
        print("[CONFIG] Scraper: Facebook Ads Library ✓")

    # Avviso se App Password sembra troppo corta
    app_pwd = config.get("GMAIL_APP_PASSWORD", "")
    if app_pwd and len(app_pwd.replace(" ", "")) < 16:
        print(
            "\n⚠  ATTENZIONE: GMAIL_APP_PASSWORD sembra troppo corta.\n"
            "   Una vera App Password Gmail ha esattamente 16 caratteri.\n"
            "   Leggi SETUP.md sezione 3 per crearla correttamente.\n"
        )

    return config


def main():
    parser = argparse.ArgumentParser(
        description="Digital Empire — Outreach Automatico",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi:
  python run.py                    → 300 email (produzione)
  python run.py --anteprima        → Vedi le email senza inviarle
  python run.py --target 10        → Testa con 10 email
  python run.py --target 10 --anteprima  → Test completo senza invio
        """,
    )
    parser.add_argument(
        "--target", type=int, default=150,
        help="Numero di email da generare (default: 150). Solo con --mode genera.",
    )
    parser.add_argument(
        "--anteprima", action="store_true",
        help="Genera le email e mostra senza inviarle (test)",
    )
    parser.add_argument(
        "--mode", choices=["genera", "invia", "completo"], default="completo",
        help=(
            "genera: scraping+QA+salva nel DB (esegui di notte) | "
            "invia: legge DB e invia in orario business (esegui la mattina) | "
            "completo: genera+invia subito (default, per test)"
        ),
    )
    parser.add_argument(
        "--mock", action="store_true",
        help="Salta scraping FB, usa lead di test (utile se token FB non funziona)",
    )
    parser.add_argument(
        "--csv", type=str, default=None, metavar="FILE",
        help="Carica lead da un file CSV invece di scrapare FB. "
             "Colonne attese: page_name,email,settore,citta,website(opzionale). "
             "Esempio: python run.py --csv leads.csv --mode genera",
    )
    args = parser.parse_args()

    # Verifica configurazione
    config = verifica_configurazione()

    # Import agenti (dopo dotenv)
    from agents.orchestrator import OutreachOrchestrator

    orchestrator = OutreachOrchestrator(
        config=config,
        output_dir=str(Path(__file__).parent / "output"),
    )

    mock_leads = None

    # ── Carica lead da CSV (bypass scraping FB) ───────────────────────────────
    if args.csv:
        import csv as _csv
        csv_path = Path(args.csv) if Path(args.csv).is_absolute() else Path(__file__).parent / args.csv
        if not csv_path.exists():
            print(f"\nERRORE: file CSV non trovato: {csv_path}")
            print("Crea un file CSV con colonne: page_name,email,settore,citta,website")
            sys.exit(1)
        with open(csv_path, newline="", encoding="utf-8-sig") as f:
            reader = _csv.DictReader(f)
            mock_leads = []
            for i, row in enumerate(reader):
                if i >= args.target:
                    break
                email = row.get("email", "").strip()
                if not email or "@" not in email:
                    continue
                settore = row.get("settore", "").strip()
                mock_leads.append({
                    "page_name":  row.get("page_name", row.get("nome", f"Business {i+1}")).strip(),
                    "email":      email,
                    "settore":    settore,
                    "citta":      row.get("citta", row.get("città", "")).strip(),
                    "website":    row.get("website", row.get("sito", "")).strip(),
                    "score":      int(row.get("score", 70)),
                    "template":   row.get("template", "A").strip().upper(),
                    "settore_calibrato": row.get("settore_calibrato", settore),
                    "pain_point": row.get("pain_point", ""),
                    "key_observation": row.get("key_observation", row.get("osservazione", "")),
                })
        print(f"\n[CSV] Caricati {len(mock_leads)} lead da {csv_path.name}")

    # ── Fallback mock (5 lead di test) ────────────────────────────────────────
    elif args.mock:
        mock_leads = [
            {"page_name": "Fisioterapia Bianchi", "website": "https://fisioterapiabianchi.it",
             "email": "info@fisioterapiabianchi.it", "settore": "fisioterapista", "citta": "Milano",
             "score": 85, "template": "A", "settore_calibrato": "salute",
             "pain_point": "Nessuna presenza online efficace", "key_observation": "Pagina FB attiva, nessun sito"},
            {"page_name": "Ristorante Da Marco", "website": "https://ristorantedamarco.it",
             "email": "prenotazioni@ristorantedamarco.it", "settore": "ristorante", "citta": "Roma",
             "score": 72, "template": "B", "settore_calibrato": "ristorante",
             "pain_point": "Ads Facebook ma landing page lenta", "key_observation": "Ads attivi, nessuna prenotazione online"},
            {"page_name": "Studio Legale Verdi", "website": "https://studiolegale-verdi.it",
             "email": "info@studiolegale-verdi.it", "settore": "avvocato", "citta": "Torino",
             "score": 78, "template": "C", "settore_calibrato": "consulente",
             "pain_point": "15+ ore/settimana processi manuali", "key_observation": "5 avvocati, gestione su Excel"},
            {"page_name": "Centro Estetico Luna", "website": "https://centroestetilcoluna.it",
             "email": "info@centroestetilcoluna.it", "settore": "estetista", "citta": "Firenze",
             "score": 68, "template": "A", "settore_calibrato": "benessere",
             "pain_point": "Non trovabile su Google", "key_observation": "Solo Instagram, nessun sito"},
            {"page_name": "Idraulico Rossi", "website": "", "email": "rossi.idraulico@gmail.com",
             "settore": "idraulico", "citta": "Napoli", "score": 55, "template": "A",
             "settore_calibrato": "artigiano", "pain_point": "Zero presenza online",
             "key_observation": "Solo Facebook personale"},
        ][:args.target]

    if args.mode == "invia":
        stats = orchestrator.run_invia()
    elif args.mode == "genera":
        stats = orchestrator.run(target=args.target, anteprima=False, solo_genera=True, mock_leads=mock_leads)
    else:
        stats = orchestrator.run(target=args.target, anteprima=args.anteprima, mock_leads=mock_leads)

    # Exit code basato sul risultato
    if stats.get("errore") and stats["errore"] not in ("weekend", "fuori orario"):
        sys.exit(1)
    elif args.anteprima:
        print("Anteprima completata. Usa --mode genera per la produzione.")
    elif args.mode in ("genera", "completo") and stats.get("email_inviate", 0) == 0 and not args.anteprima and args.mode == "completo":
        print("Nessuna email inviata. Controlla i log sopra per capire perche'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
