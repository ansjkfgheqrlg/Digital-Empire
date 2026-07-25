"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE (Gael)
Governo: MANDATO Art.8 + ADR-008

personalizza_messaggi.py — Campagna "concessionari-preventa" (G-A2)

Legge il CSV prodotto da Outreach/preventa-maps-scraper/ e genera, per ogni lead, il gancio
scelto + WhatsApp MSG1 + Email 1 personalizzati, pronti per l'invio (che resta un passo
successivo, gated). Non invia nulla. Non tocca empire_auto_v3.py né alcun file esistente
(ADR-003: wrap, mai riscrittura).

Uso:
  python personalizza_messaggi.py --input <csv-lead> --output <json-output>
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

MITTENTE = "Max"
BRAND = "Preventa"


def scegli_gancio(note_qualifica: str, priorita: str, ha_sito: str) -> dict:
    """Logica da preventa-maps-scraper/LEGGIMI.md §8: ALTA no sito/sito scarso -> Gancio 3,
    ALTA poche recensioni -> Gancio 2, altrimenti Gancio 1 (control).
    Nota: scraper.py marca ALTA sia "Senza sito web" sia "Sito vecchio/scarso" (ha_sito=True
    ma punteggio basso) — entrambi i casi vanno sul Gancio 3 (leva immagine/brand)."""
    note = (note_qualifica or "").lower()
    ha_sito_str = str(ha_sito).strip().lower()
    sito_assente = ha_sito_str in ("false", "no", "0", "", "none")
    sito_scarso = "senza sito" in note or "sito vecchio" in note or "sito scarso" in note

    if priorita == "ALTA" and (sito_scarso or sito_assente):
        return {"numero": 3, "nome": "PDF brutto / brand", "motivo": "nessun sito o sito vecchio/scarso"}
    if priorita == "ALTA" and "poche recensioni" in note:
        return {"numero": 2, "nome": "Cliente perso su WhatsApp", "motivo": "poche recensioni, attività poco digitalizzata"}
    return {"numero": 1, "nome": "Tempo perso", "motivo": "gancio control, dolore universale"}


def whatsapp_msg1(nome_attivita: str, citta: str, gancio: dict) -> str:
    nome_attivita = nome_attivita.strip()
    if gancio["numero"] == 3:
        corpo = (
            f"Ciao, sono {MITTENTE} di {BRAND} 👋\n"
            f"Ho visto {nome_attivita} su Maps - immagine curata online.\n"
            f"Chiamo diversi saloni premium in zona {citta} e mi dicono tutti: poi però i preventivi "
            f"escono su Excel o PDF del gestionale tutti storti.\n"
            f"Come li mandate voi oggi?"
        )
    elif gancio["numero"] == 2:
        corpo = (
            f"Ciao, sono {MITTENTE} di {BRAND} 👋\n"
            f"Ho visto {nome_attivita} su Maps - siete presenti in zona {citta}, immagino vi scrivano "
            f"tanti su WhatsApp per preventivi.\n"
            f"Mi dicono molti titolari: se non rispondi con un PDF bello in 5 minuti, il cliente ha già "
            f"scritto ad altri 3. Vi capita?"
        )
    else:
        corpo = (
            f"Ciao, sono {MITTENTE} di {BRAND} 👋\n"
            f"Ho visto {nome_attivita} su Maps.\n"
            f"Chiamo diversi titolari in zona {citta} e mi dicono tutti: perdere 20-30 min a preventivo "
            f"e vedere il cliente scappare su WhatsApp.\n"
            f"Anche da voi succede?"
        )
    return corpo


def email1(nome_attivita: str, citta: str, gancio: dict) -> dict:
    oggetti = [
        f"Preventivi {nome_attivita}: 2 minuti, non 30?",
        "Domanda veloce sui vostri PDF preventivi",
        f"{nome_attivita}, anche voi su Excel per i preventivi?",
    ]
    corpo = (
        f"Buongiorno,\n"
        f"vi scrivo perché sto sentendo diversi concessionari nella zona di {citta}.\n"
        f"Problema comune: 20-30 min per fare un preventivo decente e clienti che nel frattempo "
        f"chiedono altrove.\n"
        f"Voi come li state gestendo ora? Ancora su Excel/gestionale o avete già velocizzato?\n"
        f"{MITTENTE} - {BRAND}"
    )
    return {"oggetto_a": oggetti[0], "oggetto_b": oggetti[1], "oggetto_c": oggetti[2], "corpo": corpo}


def whatsapp_msg2(nome_attivita: str) -> str:
    """Da 02_SCRIPT_WHATSAPP_EMAIL_3MSG.md — invia SOLO se msg1 ha avuto risposta, o G+1/+2 se silenzio."""
    return (
        f"Capito.\n"
        f"Noi abbiamo fatto {BRAND} proprio per questo: non è un gestionale.\n"
        f"Incollate il link dell'annuncio ed esce un PDF brandizzato {nome_attivita} con prezzi "
        f"bloccati dal titolare. Pulito, inviabile su WA al volo.\n"
        f"Vuoi che ti mando un esempio fatto con un vostro annuncio?"
    )


def whatsapp_msg3(nome_attivita: str) -> str:
    """Da 02_SCRIPT_WHATSAPP_EMAIL_3MSG.md — dopo sì a msg2, o G+5 di silenzio dopo msg1."""
    return (
        f"Fatto. Ti preparo io il demo con un vostro annuncio in 15 min su schermo, senza impegno.\n"
        f"Licenza a canone, disdetta libera con kill-switch se non lo usate più.\n"
        f"Domani alle 11:00 o giovedì alle 16:30 ti va meglio per vederlo?"
    )


def email2(nome_attivita: str) -> dict:
    return {
        "oggetto": f"Esempio PDF {nome_attivita} (2 min)",
        "corpo": (
            f"Ti lascio un esempio pratico:\n"
            f"{BRAND} non sostituisce il vostro gestionale. Lo affianca.\n"
            f"Incollate il link dell'annuncio, esce PDF brandizzato con vostro logo, foto, "
            f"listino bloccato dal titolare.\n"
            f"Niente fogli Excel brutti da mandare su WhatsApp.\n"
            f"Ti va se te lo preparo con un vostro annuncio?\n"
            f"{MITTENTE}"
        ),
    }


def email3(nome_attivita: str, citta: str) -> dict:
    return {
        "oggetto": f"Chiudo il file {nome_attivita}?",
        "corpo": (
            f"Chiudo il giro contatti nella zona di {citta} questa settimana.\n"
            f"Se non è prioritario per voi velocizzare i preventivi ora, nessun problema.\n"
            f"Se invece vuoi dare un'occhiata, ti faccio vedere tutto in 15 min su un vostro annuncio. "
            f"Canone mensile, disdetta libera con kill-switch.\n"
            f"Altrimenti archivio.\n"
            f"Va bene così?\n"
            f"{MITTENTE} - {BRAND}"
        ),
    }


def normalizza_telefono(telefono: str) -> str:
    return re.sub(r"[^\d+]", "", telefono or "")


def genera_messaggi(riga: dict) -> dict:
    nome_attivita = riga.get("nome_attivita", "").strip()
    citta = riga.get("citta_ricerca", "").strip() or "zona"
    telefono = riga.get("telefono", "").strip()
    priorita = riga.get("priorita_lead", "MEDIA").strip().upper()
    note = riga.get("note_qualifica", "")
    ha_sito = riga.get("ha_sito", "")

    gancio = scegli_gancio(note, priorita, ha_sito)
    canale_primario = "whatsapp" if normalizza_telefono(telefono) else "email"

    return {
        "nome_attivita": nome_attivita,
        "citta": citta,
        "telefono": telefono,
        "priorita_lead": priorita,
        "gancio_scelto": gancio,
        "canale_primario": canale_primario,
        "whatsapp_msg1": whatsapp_msg1(nome_attivita, citta, gancio),
        "email1": email1(nome_attivita, citta, gancio),
        "stato": "da_contattare",
    }


def main():
    parser = argparse.ArgumentParser(description="Personalizza messaggi outreach concessionari (G-A2)")
    parser.add_argument("--input", required=True, help="CSV lead (output preventa-maps-scraper)")
    parser.add_argument("--output", required=True, help="Path JSON output messaggi generati")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Errore: file non trovato -> {input_path}")
        sys.exit(1)

    with open(input_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        righe = list(reader)

    risultati = [genera_messaggi(r) for r in righe]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(risultati, f, ensure_ascii=False, indent=2)

    distribuzione = {}
    for r in risultati:
        g = r["gancio_scelto"]["numero"]
        distribuzione[g] = distribuzione.get(g, 0) + 1

    print(f"Lead processati: {len(risultati)}")
    print(f"Distribuzione ganci: {distribuzione}")
    print(f"Output: {output_path}")
    print("0 messaggi inviati (solo generazione — invio reale è task separato, gated).")


if __name__ == "__main__":
    main()
