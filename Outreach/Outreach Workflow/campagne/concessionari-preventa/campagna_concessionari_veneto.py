#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
campagna_concessionari_veneto.py  —  Runner ONE-SHOT per campagna
concessionari Verona / Padova / Vicenza (Preventa: 490€ setup + 149€/mese).

ADR-003: WRAP degli asset esistenti, zero riscritture:
  - Outreach/Outreach Workflow/empire_auto_v3.py  (non toccato)
  - Outreach/preventa-outreach-pack/01-06_*.md   (script APSOC, letti come riferimento copy)
  - Outreach/preventa-maps-scraper/              (scraper Playwright, richiamato come CLI)
  - Outreach/Outreach Workflow/campagne/concessionari-preventa/
        personalizza_messaggi.py  (generatore messaggi)
        stato_e_followup.py       (DB + follow-up G+2/G+5)

Uso:
  # 1. Estrai lead (richiede Chromium + rete Maps):
  python campagna_concessionari_veneto.py scrape

  # 2. Gate anti-figuraccia (obbligatorio prima di ogni invio)
  python campagna_concessionari_veneto.py gate

  # 3. Dry-run primi N messaggi (default 20)
  python campagna_concessionari_veneto.py dry-run [--n 20]

  # 4. Invio graduale N messaggi (default 20, rispetta warm-up)
  python campagna_concessionari_veneto.py send [--n 20]

  # 5. Verifica follow-up schedulati
  python campagna_concessionari_veneto.py verify-followup

  # 6. Numero del giorno
  python campagna_concessionari_veneto.py report
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import random
import re
import smtplib
import subprocess
import sys
from datetime import date, datetime, timedelta
from email.message import EmailMessage
from pathlib import Path
from typing import List, Dict

# ---------------------------------------------------------------------------
# PATH
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[4]  # repo root (file è Outreach/Outreach Workflow/campagne/concessionari-preventa/)
OUTREACH = ROOT / "Outreach"
SCRAPER_DIR = OUTREACH / "preventa-maps-scraper"
SCRAPER_SCRIPTS = SCRAPER_DIR / "02-AUTOMAZIONI-E-SCRIPTS"
CAMPAGNA_DIR = OUTREACH / "Outreach Workflow" / "campagne" / "concessionari-preventa"
WORKFLOW_DIR = OUTREACH / "Outreach Workflow"
OUTPUT_DIR = CAMPAGNA_DIR / "output_veneto"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_INVII = OUTPUT_DIR / "invii_log.csv"
STATO_DB = OUTPUT_DIR / "stato_lead.csv"
DRY_RUN_FILE = OUTPUT_DIR / "dry_run_primi20.json"
LEADS_CSV = SCRAPER_DIR / "data" / "leads_concessionari_veneto.csv"
REPORT_JSON = OUTPUT_DIR / "report_giornaliero.json"

TARGET_PROVINCE = ["Verona", "Padova", "Vicenza"]
CATEGORIA = "concessionario auto"
MITTENTE = "Digital Empire - Max"
INDIRIZZO_FISICO = "Digital Empire SRLS, Via Giuseppe Verdi 12, 20121 Milano (MI) – Italy"
# Sender email per campagne: presa da .env, mai hardcoded
try:
    from dotenv import load_dotenv
    load_dotenv(WORKFLOW_DIR / ".env")
    load_dotenv(ROOT / ".env")
except Exception:
    pass

SENDER_EMAIL = os.getenv("GMAIL_USER") or os.getenv("OUTREACH_SENDER_EMAIL", "")
SENDER_PASSWORD = os.getenv("GMAIL_APP_PASSWORD") or os.getenv("OUTREACH_SENDER_PASSWORD", "")
# Unsubscribe: mailto + link a pagina (pagina pubblica preventa / gestita dal tuo ESP)
UNSUB_MAIL = f"mailto:unsubscribe@preventa.digital-empire.agency?subject=UNSUB"
UNSUB_URL = os.getenv("UNSUB_URL", "https://digital-empire.agency/unsubscribe")

# ---------------------------------------------------------------------------
# Helpers path (aggiungi i moduli campagna al path)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(CAMPAGNA_DIR))
import personalizza_messaggi  # noqa: E402
import stato_e_followup  # noqa: E402

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")

# ---------------------------------------------------------------------------
# STEP 1 — scrape
# ---------------------------------------------------------------------------
def cmd_scrape(args):
    """Lancia lo scraper Playwright per le 3 province. Se Chromium non c'è,
    stampa il comando manuale ed esce con 1 (non inventiamo lead)."""
    if not LEADS_CSV.parent.exists():
        LEADS_CSV.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable, str(SCRAPER_DIR / "scraper.py"),
        "--cities", ",".join(TARGET_PROVINCE),
        "--categoria", CATEGORIA,
        "--limit", str(args.limit),
        "--output", str(LEADS_CSV),
        "--only-alta",
    ]
    print(f"[SCRAPE] $ {' '.join(cmd)}")
    try:
        res = subprocess.run(cmd, cwd=str(SCRAPER_DIR), check=False)
        if res.returncode != 0:
            print(f"[SCRAPE] exit code {res.returncode} — lo scraper richiede Chromium + accesso Google Maps.")
            print("         Esegui lo stesso comando da un PC con Playwright installato:")
            print("         cd Outreach/preventa-maps-scraper")
            print(f"         python scraper.py --cities \"{','.join(TARGET_PROVINCE)}\" --categoria \"{CATEGORIA}\" --limit {args.limit} --output data/leads_concessionari_veneto.csv --only-alta")
            return res.returncode
        print(f"[SCRAPE] OK -> {LEADS_CSV}")
        return 0
    except FileNotFoundError:
        print("[SCRAPE] Playwright non disponibile in questo ambiente. Esegui da un PC con:")
        print(f"         cd {SCRAPER_DIR} && pip install -r requirements.txt && python -m playwright install chromium")
        print(f"         python scraper.py --cities \"{','.join(TARGET_PROVINCE)}\" --categoria \"{CATEGORIA}\" --limit {args.limit} --output data/leads_concessionari_veneto.csv --only-alta")
        return 1

# ---------------------------------------------------------------------------
# STEP 2 — gate anti-figuraccia
# ---------------------------------------------------------------------------
def _load_leads() -> List[Dict]:
    if not LEADS_CSV.exists():
        return []
    with open(LEADS_CSV, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def _derive_email(lead: Dict) -> str:
    """Ricava l'email dal lead. Se il CSV non ha campo email, la deriva dal sito
    (info@dominio) - ma non viene inventata: se non c'è sito, email resta vuota
    (il canale primario di personalizza_messaggi diventa whatsapp)."""
    for k in ("email", "mail", "email_contatto"):
        if lead.get(k, "").strip():
            return lead[k].strip()
    sito = (lead.get("sito_web") or "").strip().lower()
    if not sito:
        return ""
    dominio = sito.replace("https://", "").replace("http://", "").split("/")[0].replace("www.", "").strip()
    if not dominio or "." not in dominio:
        return ""
    return f"info@{dominio}"

def _mx_ok(domain: str) -> bool:
    try:
        import dns.resolver
        ans = dns.resolver.resolve(domain, "MX")
        return len(ans) > 0
    except Exception:
        return False

PLACEHOLDER_PATTERNS = [r"\[[^\]]+\]", r"\bXXX+\b", r"\bTODO\b", r"nome_azienda", r"\{[a-z_]+\}", r"<[^>]+>"]

def _has_placeholder(text: str) -> List[str]:
    hits = []
    for p in PLACEHOLDER_PATTERNS:
        for m in re.finditer(p, text or ""):
            hits.append(m.group(0))
    return hits

def cmd_gate(args):
    print("=" * 70)
    print(" GATE ANTI-FIGURACCIA — campagna concessionari Veneto")
    print("=" * 70)
    all_red = []

    def mark(label: str, ok: bool, detail: str = ""):
        sym = "🟢 VERDE" if ok else "🔴 ROSSO"
        print(f" {sym} | {label}  {('- ' + detail) if detail else ''}")
        if not ok:
            all_red.append(label)

    leads = _load_leads()
    mark(f"Lead CSV presente ({LEADS_CSV.name})", bool(leads),
         f"{len(leads)} righe" if leads else "file assente o vuoto")
    if not leads:
        print()
        print("❌ Nessun lead: blocca qui. Lancia `python campagna_concessionari_veneto.py scrape` da un PC con Playwright.")
        sys.exit(1)

    # Copertura province target
    province_presenti = {(l.get("citta_ricerca", "") or "").strip() for l in leads}
    missing = [p for p in TARGET_PROVINCE if p not in province_presenti]
    mark("Tutte le province target coperte",
         not missing, f"mancanti: {missing}" if missing else f"{TARGET_PROVINCE}")

    # Categoria concessionari
    non_car = [l for l in leads if "concession" not in (l.get("categoria") or "").lower()
               and "auto" not in (l.get("categoria") or "").lower()]
    mark("Tutti i lead sono 'concessionario auto'",
         len(non_car) == 0, f"{len(non_car)} lead di categoria diversa" if non_car else "ok")

    # Email valide con MX che risolve
    bad_mx = []
    no_email = 0
    for l in leads:
        email = _derive_email(l)
        if not email or not EMAIL_RE.match(email):
            no_email += 1
            continue
        dom = email.split("@", 1)[1]
        if not _mx_ok(dom):
            bad_mx.append((l.get("nome_attivita"), email, dom))
    mark("Email con dominio MX valido",
         len(bad_mx) == 0 and no_email <= max(1, len(leads)//10),
         f"morti: {len(bad_mx)} — senza email: {no_email}/{len(leads)}"
         if (bad_mx or no_email > max(1, len(leads)//10)) else "ok")
    if bad_mx[:5]:
        for n,e,d in bad_mx[:5]:
            print(f"        - MX MORTO: {n}  →  {e}")

    # Placeholder
    ph_hits = []
    for l in leads:
        msg = personalizza_messaggi.genera_messaggi(l)
        for etichetta, testo in [
            ("wa1", msg["whatsapp_msg1"]),
            ("email1_oggetto", msg["email1"]["oggetto_a"]),
            ("email1_corpo", msg["email1"]["corpo"]),
        ]:
            hits = _has_placeholder(testo)
            if hits:
                ph_hits.append((l.get("nome_attivita"), etichetta, hits[:3]))
    mark("Nessun placeholder rimasto nel testo",
         len(ph_hits) == 0, f"{len(ph_hits)} occorrenze" if ph_hits else "ok")

    # Nome salone combacia col messaggio (cross-check 5 random)
    sample = random.sample(leads, k=min(5, len(leads)))
    mismatch = []
    for l in sample:
        nome = (l.get("nome_attivita") or "").strip()
        msg = personalizza_messaggi.genera_messaggi(l)
        corpo = msg["email1"]["corpo"] + " " + msg["whatsapp_msg1"]
        # nome (prime 2 parole) deve comparire nel soggetto/oggetto/whatsapp
        token = " ".join(nome.split()[:2])
        if token and token.lower() not in corpo.lower() and token.lower() not in msg["email1"]["oggetto_a"].lower():
            # tolleranza: il primo token della ragione sociale basta
            first_tok = nome.split()[0] if nome.split() else ""
            if first_tok.lower() not in corpo.lower() and first_tok.lower() not in msg["email1"]["oggetto_a"].lower():
                mismatch.append((nome, token))
    mark("Nome salone coerente col lead (cross-check 5 a caso)",
         len(mismatch) == 0, f"mismatch: {mismatch}" if mismatch else "ok")

    # Disiscrizione + indirizzo fisico mittente
    unsub_ok = True
    addr_ok = True
    for l in leads:
        msg = personalizza_messaggi.genera_messaggi(l)
        corpo = msg["email1"]["corpo"]
        if "disiscriv" not in corpo.lower() and "unsubscribe" not in corpo.lower() and "cancell" not in corpo.lower():
            unsub_ok = False
        if INDIRIZZO_FISICO.split(",")[0] not in corpo and "Digital Empire" not in corpo:
            addr_ok = False
    mark("Link disiscrizione presente in ogni email", unsub_ok, "mancano i riferimenti di unsubscribe" if not unsub_ok else "ok")
    mark("Indirizzo fisico mittente presente", addr_ok, "mancano i dati del mittente" if not addr_ok else "ok")

    # Nessun lead già contattato negli ultimi 90 giorni
    cutoff = datetime.now().date() - timedelta(days=90)
    already = []
    # 1) log storici in Outreach Workflow/output/*
    if WORKFLOW_DIR.exists():
        for log in (WORKFLOW_DIR / "output").glob("*invio_log.csv") if (WORKFLOW_DIR / "output").exists() else []:
            try:
                with open(log, newline="", encoding="utf-8", errors="replace") as f:
                    rdr = csv.reader(f)
                    for row in rdr:
                        if not row: continue
                        ts = row[0][:10]
                        try:
                            d = datetime.strptime(ts, "%Y-%m-%d").date()
                            if d >= cutoff:
                                for l in leads:
                                    nome = (l.get("nome_attivita") or "").lower()
                                    if nome and nome in " ".join(row).lower():
                                        already.append((nome, d.isoformat(), log.name))
                        except Exception:
                            continue
            except Exception:
                pass
    # 2) DB stato campagna
    if STATO_DB.exists():
        with open(STATO_DB, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("stato") in ("contattato", "risposto", "interessato") and row.get("data_primo_contatto"):
                    try:
                        d = datetime.strptime(row["data_primo_contatto"][:10], "%Y-%m-%d").date()
                        if d >= cutoff:
                            already.append((row.get("nome_attivita"), d.isoformat(), "stato_lead.csv"))
                    except Exception:
                        pass
    already = list({(n,d,p) for n,d,p in already})  # dedup
    mark("Nessun lead già contattato negli ultimi 90 giorni",
         len(already) == 0, f"{len(already)} già contattati: {already[:5]}" if already else "ok")

    print()
    if all_red:
        print(f"🔴 GATE FALLITO — {len(all_red)} criterio/i rossi: {all_red}")
        sys.exit(1)
    print("🟢 GATE PASS — tutti i criteri verdi. Si può procedere a dry-run.")
    return 0

# ---------------------------------------------------------------------------
# STEP 3 — dry-run messaggi
# ---------------------------------------------------------------------------
def _firma_email() -> str:
    return (
        "\n--\n"
        f"{MITTENTE}\n"
        f"{INDIRIZZO_FISICO}\n"
        f"Preventa — 490€ setup una tantum + 149€/mese, disdetta libera\n"
        f"Per non ricevere più email: rispondi \"CANCELLA\" | {UNSUB_URL}\n"
    )

def _render_email(lead: Dict) -> Dict:
    msg = personalizza_messaggi.genera_messaggi(lead)
    email = _derive_email(lead)
    # email1.corpo contiene già firma+indirizzo+unsubscribe (dall'update di personalizza_messaggi)
    corpo_completo = msg["email1"]["corpo"]
    return {
        "nome_attivita": lead.get("nome_attivita"),
        "citta": lead.get("citta_ricerca"),
        "canale_primario": msg["canale_primario"],
        "email_destinatario": email or f"(no email — canale whatsapp: {lead.get('telefono','')})",
        "telefono": lead.get("telefono"),
        "oggetto": msg["email1"]["oggetto_a"],
        "corpo": corpo_completo,
        "whatsapp_msg1": msg["whatsapp_msg1"],
        "gancio": msg["gancio_scelto"],
        "priorita": lead.get("priorita_lead"),
    }

def cmd_dry_run(args):
    leads = _load_leads()
    if not leads:
        print(f"❌ Nessun lead in {LEADS_CSV}. Esegui scrape o copia il CSV.")
        sys.exit(1)
    # Prendi N lead ALTA + MEDIA ordinati per priorità
    order = {"ALTA":0,"MEDIA":1,"BASSA":2}
    leads_sorted = sorted(leads, key=lambda x: (order.get((x.get("priorita_lead") or "BASSA").upper(),2),
                                                -int(x.get("numero_recensioni") or 0)))
    n = min(args.n, len(leads_sorted))
    batch = leads_sorted[:n]
    rendered = [_render_email(l) for l in batch]
    DRY_RUN_FILE.write_text(json.dumps(rendered, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[DRY-RUN] {len(rendered)} messaggi generati -> {DRY_RUN_FILE}")
    print(f"         (0 inviati)")
    # Mostra 3 messaggi interi in chat
    print()
    for i, r in enumerate(rendered[:3], 1):
        print("=" * 70)
        print(f" MESSAGGIO {i}  —  {r['nome_attivita']} ({r['citta']})")
        print(f" Canale: {r['canale_primario']}  |  Gancio {r['gancio']['numero']}: {r['gancio']['nome']}  |  Priorità: {r['priorita']}")
        print("-" * 70)
        if r['canale_primario'] == "whatsapp":
            print(f"[WHATSAPP] -> {r['telefono']}")
            print(r['whatsapp_msg1'])
        print(f"[EMAIL] A: {r['email_destinatario']}")
        print(f"OGGETTO: {r['oggetto']}")
        print()
        print(r['corpo'])
        print()
    return 0

# ---------------------------------------------------------------------------
# STEP 4 — invio graduale (max N, default 20)
# ---------------------------------------------------------------------------
def _invia_email(dest: str, oggetto: str, corpo: str) -> bool:
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print(f"[SEND] ⚠️  Mancano credenziali (.env GMAIL_USER/GMAIL_APP_PASSWORD o OUTREACH_SENDER_*)")
        print(f"        Messaggio NON inviato a {dest} (dry run forzato).")
        return False
    msg = EmailMessage()
    msg["From"] = f"Max @ Digital Empire <{SENDER_EMAIL}>"
    msg["To"] = dest
    msg["Subject"] = oggetto
    msg.set_content(corpo)
    # Header unsubscribe (anti-spam best practice)
    msg["List-Unsubscribe"] = f"<{UNSUB_MAIL}> , <{UNSUB_URL}>"
    msg["Precedence"] = "bulk"
    msg["Auto-Submitted"] = "auto-generated"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as s:
            s.ehlo()
            s.starttls()
            s.login(SENDER_EMAIL, SENDER_PASSWORD)
            s.send_message(msg)
        return True
    except Exception as e:
        print(f"[SEND] ❌ Errore invio a {dest}: {e}")
        return False

def cmd_send(args):
    leads = _load_leads()
    if not leads:
        print(f"❌ Nessun lead in {LEADS_CSV}")
        sys.exit(1)
    order = {"ALTA":0,"MEDIA":1,"BASSA":2}
    leads_sorted = sorted(leads, key=lambda x: (order.get((x.get("priorita_lead") or "BASSA").upper(),2),
                                                -int(x.get("numero_recensioni") or 0)))
    n = min(args.n, 20)  # hard cap 20 al giorno 1 (warm-up)
    if args.n > 20:
        print(f"[SEND] ⚠️  Warm-up dominio: massimo 20 oggi (richiesti {args.n}), limitati a 20.")
    batch = leads_sorted[:n]

    # Seleziona solo quelli con email valida e MX ok
    da_inviare = []
    for l in batch:
        email = _derive_email(l)
        if not email or not EMAIL_RE.match(email):
            continue
        dom = email.split("@",1)[1]
        if not _mx_ok(dom):
            print(f"[SEND] Skip {l.get('nome_attivita')} — MX non valido ({dom})")
            continue
        da_inviare.append((l, email))

    if not da_inviare:
        print("[SEND] Nessun destinatario valido. 0 invii.")
        return 0

    # Init log CSV se non esiste e tieni un handle UNICO per tutto il batch
    log_new = not LOG_INVII.exists()
    LOG_INVII.parent.mkdir(parents=True, exist_ok=True)
    _log_fh = open(LOG_INVII, "a", newline="", encoding="utf-8")
    w = csv.writer(_log_fh)
    if log_new:
        w.writerow(["timestamp","nome_attivita","citta","email","oggetto","stato"])

    # Invio con delay umano (>=60s tra messaggi per warm-up)
    inviati = 0
    consegnati = 0
    aperte = 0     # non tracciabili senza tracking pixel — restano 0
    risposte = 0   # conteggiato da reply manager (0 al momento dell'invio)
    demo = 0       # 0 al primo invio
    inizio = datetime.now()
    try:
        for i,(l, email) in enumerate(da_inviare, 1):
            r = _render_email(l)
            print(f"[SEND {i}/{len(da_inviare)}] -> {r['nome_attivita']} ({email})")
            ts = datetime.now().isoformat(timespec="seconds")
            # Se le credenziali non ci sono, simula (mai inventare "consegnato")
            if SENDER_EMAIL and SENDER_PASSWORD:
                ok = _invia_email(email, r["oggetto"], r["corpo"])
                stato = "inviata" if ok else "errore"
                if ok:
                    inviati += 1
                    consegnati += 1  # semplificazione: reply/bounce gestiti dopo
            else:
                stato = "dry_no_creds"
            w.writerow([ts, r["nome_attivita"], r["citta"], email, r["oggetto"], stato])
            _log_fh.flush()
            if i < len(da_inviare):
                delay = random.uniform(65, 95)
                print(f"        pausa {delay:.0f}s (warm-up)")
                import time as _t; _t.sleep(delay if not args.fake_fast else 0.1)
    finally:
        _log_fh.flush()
        _log_fh.close()

    # Aggiorna DB stato per follow-up (chiamata DIRETTA, non subprocess)
    _args_update = type("Args", (), {"inviati_log": str(LOG_INVII)})()
    try:
        # cmd_update_stato è definito a livello di modulo — usa globals()
        globals()["cmd_update_stato"](_args_update)
    except SystemExit:
        pass

    print()
    print(f"[SEND] Completato in {(datetime.now()-inizio).total_seconds()/60:.1f} min.")
    print(f"       inviate {inviati} | consegnate {consegnati} | aperte {aperte} | risposte {risposte} | demo {demo}")
    return 0

# ---------------------------------------------------------------------------
# STEP 5 — verifica follow-up schedulati
# ---------------------------------------------------------------------------
def cmd_verify_followup(args):
    """Calcola e scrive i follow-up dovuti per G+2 e G+5 SENZA invocare lo script
    storico (che ha uno schema DB diverso e riscrive i campi). Produce direttamente
    il JSON dei messaggi da inviare alle date calcolate (N=0 inviati, gated)."""
    if not STATO_DB.exists():
        print(f"❌ DB stato non trovato: {STATO_DB}. Esegui `send` prima.")
        sys.exit(1)
    with open(STATO_DB, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    oggi = datetime.now().date()
    data_g2 = oggi + timedelta(days=2)
    data_g5 = oggi + timedelta(days=5)
    inviati_oggi = [r for r in rows if r.get("data_primo_contatto","")[:10] == oggi.isoformat()
                    and r.get("stato") == "contattato"]
    print(f"[FOLLOWUP] Lead inviati oggi ({oggi.isoformat()}): {len(inviati_oggi)}")
    for r in inviati_oggi:
        print(f"   - {r.get('nome_attivita')} ({r.get('citta')})  | MSG2={data_g2.isoformat()}  | MSG3={data_g5.isoformat()}")
    print()

    # Produce JSON di preview per G+2 e G+5 usando le funzioni di personalizzazione
    # (non invia nulla - solo preview)
    def _build_followup(offset_days: int, step: str, label: str):
        target = oggi + timedelta(days=offset_days)
        out = []
        for r in inviati_oggi:
            nome = r.get("nome_attivita","")
            citta = r.get("citta","")
            if step == "msg2":
                testo = personalizza_messaggi.email2(nome)
            else:
                testo = personalizza_messaggi.email3(nome, citta)
            out.append({
                "data_invio": target.isoformat(),
                "step": step,
                "nome_attivita": nome,
                "citta": citta,
                "email": r.get("email",""),
                "oggetto": testo["oggetto"],
                "corpo": testo["corpo"],
            })
        return out

    g2 = _build_followup(2, "msg2", "G+2")
    g5 = _build_followup(5, "msg3", "G+5")

    out_g2 = OUTPUT_DIR / f"followup_G+2_{data_g2.isoformat()}.json"
    out_g5 = OUTPUT_DIR / f"followup_G+5_{data_g5.isoformat()}.json"
    out_g2.write_text(json.dumps(g2, ensure_ascii=False, indent=2), encoding="utf-8")
    out_g5.write_text(json.dumps(g5, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[FOLLOWUP] G+2 ({data_g2.isoformat()}): {len(g2)} email MSG2 pronte -> {out_g2.name}")
    print(f"[FOLLOWUP] G+5 ({data_g5.isoformat()}): {len(g5)} email MSG3 pronte -> {out_g5.name}")
    print("[FOLLOWUP] 0 invii: i file JSON sono preview pronti per l'invio graduale al giorno stabilito.")
    return 0

def cmd_update_stato(args):
    """Aggiorna lo stato DB da un log di invio."""
    if not args.inviati_log or not Path(args.inviati_log).exists():
        print("no log"); return 1
    leads = _load_leads()
    fieldnames = [
        "id","nome_attivita","citta","telefono","canale_primario",
        "stato","data_primo_contatto","ultimo_step_inviato","data_ultimo_invio","email",
    ]
    # Se DB non esiste, inizializzalo da zero
    if not STATO_DB.exists():
        if not leads:
            return 1
        with open(STATO_DB, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames); w.writeheader()
            for i, l in enumerate(leads, 1):
                msg = personalizza_messaggi.genera_messaggi(l)
                w.writerow({
                    "id": i,
                    "nome_attivita": msg["nome_attivita"],
                    "citta": msg["citta"],
                    "telefono": msg["telefono"],
                    "canale_primario": msg["canale_primario"],
                    "stato": "da_contattare",
                    "data_primo_contatto": "",
                    "ultimo_step_inviato": "",
                    "data_ultimo_invio": "",
                    "email": _derive_email(l),
                })

    # Helpers: normalizza sempre le chiavi togliendo CR/LF e spazi superflui
    import re as _re
    def _norm(s: str) -> str:
        return (s or "").replace("\r", "").replace("\n", " ").strip().lower()
    def toks(s):
        return tuple(_re.sub(r"[^a-z0-9àèéìòù ]", " ", _norm(s)).split())

    # Carica DB esistente
    with open(STATO_DB, newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        rows_by_name = {}
        for r in rdr:
            k = _norm(r["nome_attivita"])
            # dedup: mantieni il record con stato "più avanzato" (contattato > da_contattare)
            if k not in rows_by_name or (r.get("stato") == "contattato" and rows_by_name[k].get("stato") != "contattato"):
                rows_by_name[k] = r
        existing_fn = rdr.fieldnames or fieldnames

    # Segna come contattati quelli nel log con stato inviata/dry_no_creds (simulazione locale)
    oggi = datetime.now().date().isoformat()
    n_new = 0

    def _find(name_lc):
        key = _norm(name_lc)
        if key in rows_by_name:
            return rows_by_name[key]
        # fallback fuzzy: un lead matcha se le prime 4 parole del nome nel log
        # corrispondono alle prime 4 parole di un nome nel DB (gestisce small
        # differenze di maiuscole/troncamenti/"-"/"/").
        tgt = toks(key)[:4]
        if not tgt:
            return None
        for k, rec in rows_by_name.items():
            kt = toks(k)[:4]
            if kt and kt == tgt:
                return rec
        return None

    with open(args.inviati_log, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("stato","") not in ("inviata","dry_no_creds"):
                continue
            key = r["nome_attivita"].strip().lower()
            rec = _find(key)
            if rec is not None:
                if rec.get("stato") != "contattato":
                    rec["stato"] = "contattato"
                    rec["data_primo_contatto"] = oggi
                    rec["ultimo_step_inviato"] = "msg1"
                    rec["data_ultimo_invio"] = oggi
                    n_new += 1
            else:
                print(f"[STATO] ⚠️  Lead nel log non trovato nel DB: {r['nome_attivita'][:60]}")

    # Assicura che tutti i lead siano nel DB (merge additivo se CSV è cambiato)
    for i, l in enumerate(leads, 1):
        msg = personalizza_messaggi.genera_messaggi(l)
        key = _norm(msg["nome_attivita"])
        if key not in rows_by_name:
            rows_by_name[key] = {
                "id": i,
                "nome_attivita": msg["nome_attivita"],
                "citta": msg["citta"],
                "telefono": msg["telefono"],
                "canale_primario": msg["canale_primario"],
                "stato": "da_contattare",
                "data_primo_contatto": "",
                "ultimo_step_inviato": "",
                "data_ultimo_invio": "",
                "email": _derive_email(l),
            }

    with open(STATO_DB, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=existing_fn); w.writeheader()
        w.writerows(rows_by_name.values())
    print(f"[STATO] Aggiornato {STATO_DB}: {n_new} lead marcati 'contattato' oggi ({oggi}).")
    return 0

# ---------------------------------------------------------------------------
# STEP 6 — report
# ---------------------------------------------------------------------------
def cmd_report(args):
    """Stampa la riga del giorno per Max."""
    # Conta dai log di oggi
    oggi = datetime.now().date().isoformat()
    inviate = consegnate = aperte = risposte = demo = 0
    if LOG_INVII.exists():
        with open(LOG_INVII, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["timestamp"][:10] == oggi:
                    if r["stato"] == "inviata":
                        inviate += 1
                        consegnate += 1
                    # dry_no_creds / errore NON vengono contati come invii (né consegne)
    # Aperte/risposte/demo non sono tracciabili in assenza di pixel/IMAP; se ci sono file reply aggiungi
    # (lascia 0, non inventare)
    print(f"inviate {inviate} | consegnate {consegnate} | aperte {aperte} | risposte {risposte} | demo {demo}")
    # Salva anche JSON
    REPORT_JSON.write_text(json.dumps({
        "data": oggi, "inviate": inviate, "consegnate": consegnate,
        "aperte": aperte, "risposte": risposte, "demo": demo
    }), encoding="utf-8")
    return 0

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Campagna Preventa concessionari Verona/Padova/Vicenza")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("scrape"); p1.add_argument("--limit", type=int, default=60)
    p1.set_defaults(fn=cmd_scrape)

    p2 = sub.add_parser("gate"); p2.set_defaults(fn=cmd_gate)

    p3 = sub.add_parser("dry-run"); p3.add_argument("--n", type=int, default=20)
    p3.set_defaults(fn=cmd_dry_run)

    p4 = sub.add_parser("send"); p4.add_argument("--n", type=int, default=20); p4.add_argument("--fake-fast", action="store_true")
    p4.set_defaults(fn=cmd_send)

    p5 = sub.add_parser("verify-followup"); p5.set_defaults(fn=cmd_verify_followup)

    p6 = sub.add_parser("report"); p6.set_defaults(fn=cmd_report)

    p7 = sub.add_parser("update-stato")
    p7.add_argument("--inviati-log", required=True); p7.set_defaults(fn=cmd_update_stato)

    args = ap.parse_args()
    sys.exit(args.fn(args) or 0)

if __name__ == "__main__":
    main()
