# -*- coding: utf-8 -*-
"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE (content-forge, 2026-07-30)

Rule Keeper — versione DETERMINISTICA (no chiamata LLM) del checklist a 5 Pilastri
descritto in agents/rule-keeper/system_prompt.md, per applicare la Bibbia dei Messaggi
(../../knowledge/bibbia-messaggi-outreach.md) nel flusso di invio reale (outreach_giornaliero.py),
dove un invio LLM per ogni messaggio non è praticabile a 50 msg/giorno (costo/latenza).

Il rule-keeper LLM (agents/rule-keeper/) resta la versione di riferimento, piu' sfumata,
usabile per revisione manuale o batch offline. Questo modulo copre solo le violazioni
oggettive/strutturali — non sostituisce il giudizio umano o LLM su casi ambigui.
"""
from __future__ import annotations

import re
from typing import Dict, List

MAX_PAROLE_WHATSAPP = 90
PAROLE_PREZZO = ["€", "prezzo", "costo", "canone", "tantum", "pagamento", "euro"]
VERBI_DEMAND_ALTO_ATTRITO = [
    "chiamami", "prenota una call", "prenota un appuntamento", "compra",
    "acquista ora", "paga", "firma", "iscriviti",
]


def _conta_parole(testo: str) -> int:
    return len(testo.split())


def lint_messaggio(testo: str, nome_attivita: str, citta: str, tentativo_numero: int = 1,
                    testi_precedenti: List[str] | None = None) -> Dict:
    """
    Verifica deterministica dei 5 Pilastri su un messaggio WhatsApp/LinkedIn (msg1).
    Ritorna {"esito": "APPROVATO"|"RESPINTO", "violazioni": [...]}.
    Non sostituisce il rule-keeper LLM per giudizi sfumati (es. qualita' della frase
    Barnum) — cattura solo violazioni strutturali oggettive.
    """
    violazioni = []

    # Le parole "vietate" (prezzo, verbi ad alto impegno) vanno cercate SOLO nella prosa
    # scritta dall'agente, non nel nome dell'attivita' che viene ripetuto verbatim nel
    # messaggio ("Ho visto {nome_attivita} su Maps..."). Senza questa esclusione, nomi
    # come "Auto Europa" o "Compravendita Automobili" fanno scattare falsi positivi
    # (euro dentro "Europa", compra dentro "Compravendita") — bug reale trovato in test.
    testo_senza_nome = testo.replace(nome_attivita, "") if nome_attivita else testo
    testo_l = testo.lower()
    testo_senza_nome_l = testo_senza_nome.lower()
    prime_150 = testo[:150].lower()

    def _match_parola_intera(parola: str, testo_target: str) -> bool:
        return re.search(r"\b" + re.escape(parola.lower()) + r"\b", testo_target) is not None

    # Pilastro 1 — Personalizzazione reale: nome attivita' deve comparire
    if nome_attivita and nome_attivita.lower() not in testo_l:
        violazioni.append({
            "pilastro": 1, "nome": "Personalizzazione reale",
            "motivo": f"'{nome_attivita}' non compare nel messaggio — nessuna personalizzazione verificabile.",
        })

    # Pilastro 2 — Chiarezza 3 secondi: mittente/brand devono comparire nelle prime 150 char
    if "max" not in prime_150 and "preventa" not in prime_150:
        violazioni.append({
            "pilastro": 2, "nome": "Chiarezza 3 secondi",
            "motivo": "Non e' chiaro chi scrive entro i primi ~150 caratteri (manca mittente/brand).",
        })

    # Pilastro 3 — Valore anticipato: niente prezzo/soldi nel primo messaggio
    if tentativo_numero == 1:
        for parola in PAROLE_PREZZO:
            if parola in ("€",) and parola in testo_senza_nome:
                match = True
            else:
                match = _match_parola_intera(parola, testo_senza_nome_l)
            if match:
                violazioni.append({
                    "pilastro": 3, "nome": "Valore anticipato",
                    "motivo": f"Il primo messaggio menziona '{parola}' — si chiede prima di dare valore (vedi caso Video Editor v1, bocciato).",
                })
                break

    # Pilastro 4 — Micro-commitment: CTA deve essere una domanda, non un comando ad alto impegno
    ultima_frase = testo.strip().split("\n")[-1] if testo.strip() else ""
    for verbo in VERBI_DEMAND_ALTO_ATTRITO:
        if _match_parola_intera(verbo, testo_senza_nome_l) if " " not in verbo else verbo in testo_senza_nome_l:
            violazioni.append({
                "pilastro": 4, "nome": "Micro-commitment",
                "motivo": f"Richiesta ad alto impegno rilevata ('{verbo}') — il primo messaggio deve chiedere un micro-commitment, non un impegno grande.",
            })
            break
    if not ultima_frase.strip().endswith("?"):
        violazioni.append({
            "pilastro": 4, "nome": "Micro-commitment",
            "motivo": "Il messaggio non si chiude con una domanda — un CTA aperto senza domanda e' piu' facile da ignorare.",
        })

    # Pilastro 5 — Basso attrito: lunghezza sotto soglia canale
    n_parole = _conta_parole(testo)
    if n_parole > MAX_PAROLE_WHATSAPP:
        violazioni.append({
            "pilastro": 5, "nome": "Basso attrito",
            "motivo": f"Messaggio di {n_parole} parole, sopra la soglia di {MAX_PAROLE_WHATSAPP} per WhatsApp — troppo lungo da leggere in pochi secondi.",
        })

    # Follow-up: angolo diverso dal tentativo precedente (check di similarita' grezzo)
    if tentativo_numero > 1 and testi_precedenti:
        for prec in testi_precedenti:
            parole_comuni = set(testo_l.split()) & set(prec.lower().split())
            if len(parole_comuni) / max(1, len(set(testo_l.split()))) > 0.6:
                violazioni.append({
                    "pilastro": 6, "nome": "Angolo follow-up diverso",
                    "motivo": "Il messaggio ripete troppe parole del tentativo precedente — serve un angolo psicologico diverso.",
                })
                break

    return {
        "esito": "RESPINTO" if violazioni else "APPROVATO",
        "violazioni": violazioni,
    }
