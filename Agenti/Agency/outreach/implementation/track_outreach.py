"""
WF-E — Tracciamento Pipeline Outreach

Aggiorna lo stato di un lead nel Google Sheets e genera report settimanale.
Gestisce le transizioni di stato della pipeline e i reminder follow-up.

Uso:
    python implementation/track_outreach.py --id NS-MI-xxx --stato risposto
    python implementation/track_outreach.py --id AF-RM-xxx --stato call_fissata --note "Call lunedì alle 15"
    python implementation/track_outreach.py --report           (genera report settimanale)
    python implementation/track_outreach.py --followup         (mostra follow-up scaduti)

Input:
    --id: ID del lead
    --stato: Nuovo stato (vedi stati validi)
    --note: Note libere da aggiungere
    --data-followup: Data per reminder (formato YYYY-MM-DD)
    --report: Genera report settimanale pipeline
    --followup: Mostra lead con follow-up scaduti

Stati validi:
    nuovo, bozza_pronta, inviato, followup_1, followup_2,
    risposto, call_fissata, proposta_inviata, cliente,
    non_interessato, nessuna_risposta, archiviato
"""

import os
import sys
import argparse
from datetime import datetime, date
from pathlib import Path
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.utils.logger import get_logger
from implementation.utils.sheets_client import crea_client_da_env, INTESTAZIONI_NO_SITO, INTESTAZIONI_FUNNEL_SCARSO

load_dotenv()

# Transizioni valide (da → a)
TRANSIZIONI_VALIDE = {
    "nuovo": {"bozza_pronta", "archiviato"},
    "bozza_pronta": {"inviato", "archiviato"},
    "inviato": {"risposto", "followup_1", "non_interessato", "archiviato"},
    "followup_1": {"risposto", "followup_2", "non_interessato", "archiviato"},
    "followup_2": {"risposto", "nessuna_risposta", "non_interessato", "archiviato"},
    "risposto": {"call_fissata", "non_interessato", "archiviato"},
    "call_fissata": {"proposta_inviata", "non_interessato", "archiviato"},
    "proposta_inviata": {"cliente", "non_interessato", "archiviato"},
    "cliente": {"archiviato"},
    "non_interessato": {"archiviato"},
    "nessuna_risposta": {"archiviato", "inviato"},  # Può rientrare dopo un po'
    "archiviato": set()
}

STATI_CON_DATA_CONTATTO = {"inviato", "followup_1", "followup_2"}
STATI_TERMINALI = {"cliente", "non_interessato", "nessuna_risposta", "archiviato"}
STATI_POSITIVI = {"risposto", "call_fissata", "proposta_inviata", "cliente"}


def trova_riga_lead(sheets, id_lead: str) -> tuple:
    """Cerca il lead in tutti i tab."""
    for tab_nome, intestazioni in [("Lead_NoSito", INTESTAZIONI_NO_SITO), ("Lead_FunnelScarso", INTESTAZIONI_FUNNEL_SCARSO)]:
        riga, num_riga = sheets.trova_riga_per_id(tab_nome, id_lead)
        if riga:
            return tab_nome, intestazioni, num_riga, riga
    return None, None, -1, None


def aggiorna_stato(id_lead: str, nuovo_stato: str, note: str, data_followup: str,
                   sheets, logger) -> bool:
    """
    Aggiorna lo stato di un lead nella pipeline.

    Args:
        id_lead: ID del lead
        nuovo_stato: Nuovo stato
        note: Note aggiuntive
        data_followup: Data follow-up schedulato (YYYY-MM-DD)
        sheets: SheetsClient
        logger: Logger

    Returns:
        True se successo
    """
    # Cerca lead
    tab_nome, intestazioni, num_riga, riga = trova_riga_lead(sheets, id_lead)
    if not riga:
        logger.error(f"Lead non trovato: {id_lead}")
        return False

    nome = riga.get("NOME_BUSINESS") or riga.get("NOME_PAGINA", "?")
    stato_corrente = riga.get("STATO_OUTREACH", "nuovo")

    logger.info(f"Lead: {nome} ({id_lead})")
    logger.info(f"Transizione: {stato_corrente} → {nuovo_stato}")

    # Valida transizione
    transizioni_ok = TRANSIZIONI_VALIDE.get(stato_corrente, set())
    if nuovo_stato not in transizioni_ok:
        logger.warning(
            f"Transizione non standard: {stato_corrente} → {nuovo_stato}. "
            f"Transizioni valide da '{stato_corrente}': {', '.join(transizioni_ok) or 'nessuna'}"
        )
        conferma = input(f"Procedere comunque con la transizione {stato_corrente} → {nuovo_stato}? (s/N): ").strip().lower()
        if conferma != "s":
            logger.info("Aggiornamento annullato")
            return False

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Aggiorna stato
    sheets.aggiorna_cella(tab_nome, num_riga, "STATO_OUTREACH", nuovo_stato, intestazioni)

    # Aggiorna data contatto
    if nuovo_stato in STATI_CON_DATA_CONTATTO:
        sheets.aggiorna_cella(tab_nome, num_riga, "DATA_ULTIMO_CONTATTO", timestamp, intestazioni)

    # Aggiorna data risposta
    if nuovo_stato == "risposto":
        sheets.aggiorna_cella(tab_nome, num_riga, "DATA_RISPOSTA", timestamp, intestazioni)

    # Aggiorna follow-up schedulato
    if data_followup:
        sheets.aggiorna_cella(tab_nome, num_riga, "DATA_FOLLOWUP_SCHEDULATO", data_followup, intestazioni)
    elif nuovo_stato in STATI_CON_DATA_CONTATTO:
        # Auto-calcola: oggi + 7 giorni
        from datetime import timedelta
        auto_followup = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        sheets.aggiorna_cella(tab_nome, num_riga, "DATA_FOLLOWUP_SCHEDULATO", auto_followup, intestazioni)
        logger.info(f"Follow-up auto-schedulato: {auto_followup}")

    # Aggiorna storico stati
    storico_attuale = riga.get("STORICO_STATI", "")
    nuova_entry = f"{timestamp}: {stato_corrente} → {nuovo_stato}"
    storico_aggiornato = f"{storico_attuale}\n{nuova_entry}".strip() if storico_attuale else nuova_entry
    sheets.aggiorna_cella(tab_nome, num_riga, "STORICO_STATI", storico_aggiornato, intestazioni)

    # Aggiorna note
    if note:
        note_attuali = riga.get("NOTE", "")
        note_aggiornate = f"{note_attuali}\n[{timestamp}] {note}".strip() if note_attuali else f"[{timestamp}] {note}"
        sheets.aggiorna_cella(tab_nome, num_riga, "NOTE", note_aggiornate, intestazioni)

    # Log speciale per eventi importanti
    if nuovo_stato in STATI_POSITIVI:
        logger.info(f"RISPOSTA/AVANZAMENTO: {nome} → {nuovo_stato}")
        if nuovo_stato == "risposto":
            print(f"\n{'='*50}")
            print(f"RISPOSTA RICEVUTA!")
            print(f"Business: {nome}")
            print(f"ID Lead: {id_lead}")
            print(f"{'='*50}\n")
    elif nuovo_stato == "cliente":
        print(f"\n{'*'*50}")
        print(f"NUOVO CLIENTE: {nome}")
        print(f"{'*'*50}\n")

    logger.info(f"Stato aggiornato con successo: {nome} → {nuovo_stato}")
    return True


def mostra_followup_scaduti(sheets, logger) -> None:
    """Mostra i lead con follow-up scaduti."""
    oggi = date.today()
    lead_scaduti = []

    for tab_nome, _ in [("Lead_NoSito", None), ("Lead_FunnelScarso", None)]:
        righe = sheets.leggi_tab(tab_nome)
        for riga in righe:
            data_fu = riga.get("DATA_FOLLOWUP_SCHEDULATO", "")
            stato = riga.get("STATO_OUTREACH", "")

            if not data_fu or stato in STATI_TERMINALI:
                continue

            try:
                data_followup = datetime.strptime(data_fu, "%Y-%m-%d").date()
                if data_followup <= oggi:
                    nome = riga.get("NOME_BUSINESS") or riga.get("NOME_PAGINA", "?")
                    giorni_ritardo = (oggi - data_followup).days
                    lead_scaduti.append({
                        "id": riga.get("ID_LEAD"),
                        "nome": nome,
                        "stato": stato,
                        "data_followup": data_fu,
                        "ritardo_giorni": giorni_ritardo,
                        "tab": tab_nome
                    })
            except ValueError:
                continue

    if not lead_scaduti:
        print("Nessun follow-up scaduto.")
        return

    lead_scaduti.sort(key=lambda x: x["ritardo_giorni"], reverse=True)

    print(f"\n{'='*60}")
    print(f"FOLLOW-UP SCADUTI ({len(lead_scaduti)} lead)")
    print(f"{'='*60}")
    for lead in lead_scaduti:
        print(f"\n[{lead['id']}] {lead['nome']}")
        print(f"  Stato: {lead['stato']}")
        print(f"  Follow-up previsto: {lead['data_followup']} ({lead['ritardo_giorni']} giorni fa)")
    print(f"\n{'='*60}\n")


def genera_report(sheets, logger) -> None:
    """Genera report settimanale della pipeline."""
    stats = {
        "totale": 0,
        "per_stato": {},
        "fascia_A": 0,
        "fascia_B": 0,
        "fascia_C": 0,
        "pronti": 0,
        "tasso_risposta": 0
    }

    n_inviati = 0
    n_risposte = 0

    for tab_nome, _ in [("Lead_NoSito", None), ("Lead_FunnelScarso", None)]:
        righe = sheets.leggi_tab(tab_nome)
        for riga in righe:
            stato = riga.get("STATO_OUTREACH", "")
            fascia = riga.get("FASCIA", "")
            pronto = riga.get("PRONTO_OUTREACH", "")

            stats["totale"] += 1
            stats["per_stato"][stato] = stats["per_stato"].get(stato, 0) + 1

            if fascia == "A":
                stats["fascia_A"] += 1
            elif fascia == "B":
                stats["fascia_B"] += 1
            elif fascia == "C":
                stats["fascia_C"] += 1

            if pronto == "Sì":
                stats["pronti"] += 1

            if stato in ("inviato", "followup_1", "followup_2"):
                n_inviati += 1
            if stato in STATI_POSITIVI or stato == "risposto":
                n_risposte += 1

    tasso = round((n_risposte / n_inviati * 100), 1) if n_inviati > 0 else 0

    print(f"\n{'='*60}")
    print(f"REPORT PIPELINE — {datetime.now().strftime('%d/%m/%Y')}")
    print(f"{'='*60}")
    print(f"\nTOTALE LEAD: {stats['totale']}")
    print(f"Fascia A (caldi):  {stats['fascia_A']}")
    print(f"Fascia B (medi):   {stats['fascia_B']}")
    print(f"Fascia C (freddi): {stats['fascia_C']}")
    print(f"\nPRONTI PER OUTREACH: {stats['pronti']}")
    print(f"\nSTATO PIPELINE:")
    for stato, n in sorted(stats["per_stato"].items(), key=lambda x: x[1], reverse=True):
        print(f"  {stato:25s}: {n}")
    print(f"\nTASSO DI RISPOSTA: {tasso}% ({n_risposte}/{n_inviati} email)")
    print(f"{'='*60}\n")

    logger.info(
        f"Report: {stats['totale']} lead totali | "
        f"A={stats['fascia_A']}, B={stats['fascia_B']}, C={stats['fascia_C']} | "
        f"Tasso risposta: {tasso}%"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Gestione pipeline e tracking outreach"
    )
    parser.add_argument("--id", help="ID del lead da aggiornare")
    parser.add_argument(
        "--stato",
        choices=list(TRANSIZIONI_VALIDE.keys()),
        help="Nuovo stato del lead"
    )
    parser.add_argument("--note", default="", help="Note libere da aggiungere")
    parser.add_argument("--data-followup", help="Data follow-up (YYYY-MM-DD)")
    parser.add_argument("--report", action="store_true", help="Genera report settimanale")
    parser.add_argument("--followup", action="store_true", help="Mostra follow-up scaduti")
    args = parser.parse_args()

    # Validazione
    if not args.report and not args.followup and (not args.id or not args.stato):
        print("Specifica --id e --stato per aggiornare un lead, oppure --report o --followup")
        sys.exit(1)

    logger = get_logger("WF-E", "tracking")

    sheets = crea_client_da_env()
    if not sheets:
        logger.error("Google Sheets non configurato")
        sys.exit(1)

    if args.report:
        genera_report(sheets, logger)
        return

    if args.followup:
        mostra_followup_scaduti(sheets, logger)
        return

    # Aggiornamento stato
    logger.info(f"START — Aggiornamento stato: {args.id} → {args.stato}")
    successo = aggiorna_stato(
        id_lead=args.id,
        nuovo_stato=args.stato,
        note=args.note,
        data_followup=args.data_followup,
        sheets=sheets,
        logger=logger
    )

    if successo:
        logger.info("END — Aggiornamento completato")
    else:
        logger.error("END — Aggiornamento fallito")
        sys.exit(1)


if __name__ == "__main__":
    main()
