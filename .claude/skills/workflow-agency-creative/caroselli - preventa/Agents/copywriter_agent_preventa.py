import json
import os
import re
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENCY_DIR = os.path.join(os.path.dirname(PROJECT_DIR), "caroselli - agency")
if AGENCY_DIR not in sys.path:
    sys.path.append(AGENCY_DIR)

from Agents.ai_client import call_ai  # noqa: E402 - riuso client Agency (stesse API key)


def extract_json(text):
    match = re.search(r'```(?:json)?(.*?)```', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()


def generate_carousel_copy_preventa(topic=None):
    """Come Agents/copywriter_agent.py del progetto Agency, ma per Preventa:
    CTA diversa (Preventa vende via WhatsApp outreach diretto, non via DM
    Instagram — il carosello è social proof/brand awareness, non funnel di
    vendita) e contesto reale del prodotto (vedi REGOLE.md e
    wiki/projects/Preventa/Preventa_Logica_Completa_Metodo.md)."""

    prompt = f"""
    Sei il CRO Copy Architect di Preventa, prodotto per concessionari auto.
    Preventa: incolli il link di un annuncio auto (anche estero, es. tedesco) e ottieni
    un PDF preventivo brandizzato con prezzi bloccati dal titolare, pronto da mandare su
    WhatsApp — invece di 20-30 minuti su Excel/gestionale mentre il cliente scrive già
    ad altri 3 concessionari. Prezzo: 2.000 euro una tantum, nessun canone mensile.
    Target: concessionari che fanno import (il dolore specifico è tradurre annunci
    esteri e ricalcolare il prezzo a mano).

    Devi scrivere il copy per un carosello Instagram di ESATTAMENTE 3 slide, più la
    descrizione del post (caption). Frasi compatte, potenti, corte - niente muri di testo.
    Il carosello è social proof/brand awareness (Preventa vende via outreach WhatsApp
    diretto, NON tramite DM Instagram) - la CTA finale NON deve chiedere di scrivere in DM
    per una call di vendita, deve invitare a seguire/informarsi o a visitare il sito.

    Argomento (se 'None', usa il pain point del tempo perso sui preventivi manuali): {topic}

    Regole di Output:
    - Restituisci ESCLUSIVAMENTE un oggetto JSON valido con le chiavi "slides" (array di
      3 oggetti) e "descrizione" (stringa), senza altro testo prima o dopo.
    - Ogni oggetto in "slides" ha queste chiavi:
        "slide_numero": intero (1, 2, o 3)
        "titolo_nascosto": stringa (scopo della slide: "Hook", "Soluzione", "CTA")
        "testo_esatto": stringa, max 12 parole, tutto minuscolo, testo FISICO sulla slide.
    - "descrizione": caption Instagram con emoji e hashtag rilevanti (concessionari,
      auto, import, gestionale).

    Specifiche delle 3 slide:
    - Slide 1 (Hook): pain point concreto e riconoscibile per un concessionario
      (tempo perso sui preventivi, o annunci esteri da tradurre a mano).
    - Slide 2 (Soluzione): come funziona Preventa in una frase (link annuncio -> PDF
      pronto in italiano con prezzo bloccato).
    - Slide 3 (CTA): invito a seguire/scoprire di più, MAI "scrivimi X in DM per una call
      di vendita" (quello è il pattern Agency, non Preventa).

    ESEMPIO DI OUTPUT ATTESO:
    {{
      "slides": [
        {{
          "slide_numero": 1,
          "titolo_nascosto": "Hook",
          "testo_esatto": "20 minuti su excel mentre il cliente scrive gia ad altri 3"
        }},
        {{
          "slide_numero": 2,
          "titolo_nascosto": "Soluzione",
          "testo_esatto": "incolli il link dell'annuncio, esce il pdf pronto in italiano"
        }},
        {{
          "slide_numero": 3,
          "titolo_nascosto": "CTA",
          "testo_esatto": "preventa. il preventivo pronto prima che il cliente cambi idea"
        }}
      ],
      "descrizione": "Il cliente scrive gia' ad altri 3 concessionari mentre tu sei ancora su Excel. 🚗 Preventa trasforma un link (anche di un annuncio tedesco) in un PDF preventivo pronto, brandizzato, con i tuoi prezzi. #concessionari #autoimport #preventivi #gestionale"
    }}
    """

    messages = [
        {"role": "system", "content": "Sei un agente che produce solo e rigorosamente JSON valido come richiesto."},
        {"role": "user", "content": prompt},
    ]

    response = call_ai(messages, label="Copywriter-Preventa")

    if not response:
        return None

    try:
        clean_json_str = extract_json(response)
        return json.loads(clean_json_str)
    except Exception as e:
        print(f"[Copywriter-Preventa] Errore nel parsing del JSON restituito: {e}")
        print(f"Risposta raw:\n{response}")
        return None
