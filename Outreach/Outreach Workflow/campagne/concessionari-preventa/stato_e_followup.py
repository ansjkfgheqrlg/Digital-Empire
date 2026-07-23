"""
stato_e_followup.py — Campagna "concessionari-preventa" (G-A3)

Tiene lo stato di ogni lead (da_contattare / contattato / risposto / interessato / no_grazie) in
un CSV locale e genera in automatico i follow-up dovuti (G+2 -> MSG2, G+5 -> MSG3, da
05_FOLLOW_UP_G2_G5.md), senza inviare nulla: produce un report giornaliero di cosa è pronto da
mandare. L'invio reale resta un passo separato, gated (G-A4). Non tocca empire_auto_v3.py
(ADR-003).

Uso:
  # 1. Inizializza/aggiorna il DB da un output di personalizza_messaggi.py (idempotente)
  python stato_e_followup.py --init output_run.json --db stato_lead.csv

  # 2. Simula l'invio del primo contatto (finché G-A4 non è live, va segnato a mano/da import)
  python stato_e_followup.py --segna-contattato "+390212345" --data 2026-07-23 --db stato_lead.csv

  # 3. Segna una risposta arrivata (ferma la sequenza automatica)
  python stato_e_followup.py --segna-risposta "+390212345" --esito interessato --db stato_lead.csv

  # 4. Genera il batch di follow-up dovuti "oggi" + report
  python stato_e_followup.py --followup-oggi --data 2026-07-25 --db stato_lead.csv --output report.json
"""

import argparse
import csv
import json
import sys
from datetime import date, datetime
from pathlib import Path

from personalizza_messaggi import (
    normalizza_telefono,
    whatsapp_msg2,
    whatsapp_msg3,
    email2,
    email3,
)

CAMPI = [
    "id", "nome_attivita", "citta", "telefono", "canale_primario",
    "stato", "data_primo_contatto", "ultimo_step_inviato", "data_ultimo_invio",
]

STATI_ATTIVI = {"da_contattare", "contattato"}  # solo questi ricevono follow-up automatici


def lead_id(telefono: str, nome_attivita: str) -> str:
    tel = normalizza_telefono(telefono)
    return tel if tel else nome_attivita.strip().lower()


def carica_db(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, newline="", encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def salva_db(path: Path, righe: dict):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPI)
        writer.writeheader()
        for r in righe.values():
            writer.writerow(r)


def cmd_init(args):
    db_path = Path(args.db)
    db = carica_db(db_path)

    with open(args.init, encoding="utf-8") as f:
        lead = json.load(f)

    nuovi = 0
    for l in lead:
        lid = lead_id(l.get("telefono", ""), l.get("nome_attivita", ""))
        if lid in db:
            continue  # idempotente: non tocca lead già tracciati
        db[lid] = {
            "id": lid,
            "nome_attivita": l.get("nome_attivita", ""),
            "citta": l.get("citta", ""),
            "telefono": l.get("telefono", ""),
            "canale_primario": l.get("canale_primario", "email"),
            "stato": "da_contattare",
            "data_primo_contatto": "",
            "ultimo_step_inviato": "",
            "data_ultimo_invio": "",
        }
        nuovi += 1

    salva_db(db_path, db)
    print(f"DB: {len(db)} lead totali ({nuovi} nuovi aggiunti, {len(db) - nuovi} già presenti)")


def cmd_segna_contattato(args):
    db_path = Path(args.db)
    db = carica_db(db_path)
    lid = normalizza_telefono(args.segna_contattato) or args.segna_contattato
    if lid not in db:
        print(f"Errore: lead '{lid}' non trovato nel DB")
        sys.exit(1)
    db[lid]["stato"] = "contattato"
    db[lid]["data_primo_contatto"] = args.data
    db[lid]["ultimo_step_inviato"] = "msg1"
    db[lid]["data_ultimo_invio"] = args.data
    salva_db(db_path, db)
    print(f"Segnato contattato: {db[lid]['nome_attivita']} ({args.data})")


def cmd_segna_risposta(args):
    db_path = Path(args.db)
    db = carica_db(db_path)
    lid = normalizza_telefono(args.segna_risposta) or args.segna_risposta
    if lid not in db:
        print(f"Errore: lead '{lid}' non trovato nel DB")
        sys.exit(1)
    db[lid]["stato"] = args.esito
    salva_db(db_path, db)
    print(f"Segnato '{args.esito}': {db[lid]['nome_attivita']} — esce dalla sequenza automatica")


def genera_followup_per_lead(riga: dict, oggi: date) -> dict | None:
    if riga["stato"] not in STATI_ATTIVI or not riga["data_primo_contatto"]:
        return None

    data_primo = datetime.strptime(riga["data_primo_contatto"], "%Y-%m-%d").date()
    giorni_passati = (oggi - data_primo).days
    ultimo_step = riga["ultimo_step_inviato"]
    nome = riga["nome_attivita"]
    citta = riga["citta"]
    canale = riga["canale_primario"]

    step_dovuto = None
    if giorni_passati >= 5 and ultimo_step in ("msg1", "msg2"):
        step_dovuto = "msg3"
    elif giorni_passati >= 2 and ultimo_step == "msg1":
        step_dovuto = "msg2"

    if not step_dovuto:
        return None

    if canale == "whatsapp":
        testo = whatsapp_msg3(nome) if step_dovuto == "msg3" else whatsapp_msg2(nome)
        contenuto = {"canale": "whatsapp", "testo": testo}
    else:
        contenuto = {"canale": "email", **(email3(nome, citta) if step_dovuto == "msg3" else email2(nome))}

    return {
        "id": riga["id"],
        "nome_attivita": nome,
        "step": step_dovuto,
        "giorni_da_primo_contatto": giorni_passati,
        **contenuto,
    }


def cmd_followup_oggi(args):
    db_path = Path(args.db)
    db = carica_db(db_path)
    oggi = datetime.strptime(args.data, "%Y-%m-%d").date()

    dovuti = []
    for lid, riga in db.items():
        fu = genera_followup_per_lead(riga, oggi)
        if fu:
            dovuti.append(fu)
            riga["ultimo_step_inviato"] = fu["step"]
            riga["data_ultimo_invio"] = args.data

    salva_db(db_path, db)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dovuti, f, ensure_ascii=False, indent=2)

    per_stato = {}
    for r in db.values():
        per_stato[r["stato"]] = per_stato.get(r["stato"], 0) + 1

    print(f"Data: {args.data}")
    print(f"Follow-up generati (pronti, 0 inviati): {len(dovuti)}")
    print(f"Distribuzione stato DB ({len(db)} lead totali): {per_stato}")
    print(f"Report: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Tracking + follow-up automatico G-A3")
    parser.add_argument("--db", required=True, help="Path CSV stato lead")
    parser.add_argument("--init", help="Path JSON output di personalizza_messaggi.py da caricare nel DB")
    parser.add_argument("--segna-contattato", help="Telefono/id lead: msg1 inviato")
    parser.add_argument("--segna-risposta", help="Telefono/id lead: risposta arrivata")
    parser.add_argument("--esito", choices=["risposto", "interessato", "no_grazie"], help="Esito della risposta")
    parser.add_argument("--followup-oggi", action="store_true", help="Genera i follow-up dovuti oggi")
    parser.add_argument("--data", help="Data di riferimento YYYY-MM-DD")
    parser.add_argument("--output", help="Path JSON report follow-up (con --followup-oggi)")
    args = parser.parse_args()

    if args.init:
        cmd_init(args)
    elif args.segna_contattato:
        if not args.data:
            print("Errore: --data richiesta con --segna-contattato")
            sys.exit(1)
        cmd_segna_contattato(args)
    elif args.segna_risposta:
        if not args.esito:
            print("Errore: --esito richiesto con --segna-risposta")
            sys.exit(1)
        cmd_segna_risposta(args)
    elif args.followup_oggi:
        if not args.data or not args.output:
            print("Errore: --data e --output richiesti con --followup-oggi")
            sys.exit(1)
        cmd_followup_oggi(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
