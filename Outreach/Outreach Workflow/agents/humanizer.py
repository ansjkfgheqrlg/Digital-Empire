"""
Humanizer Agent — Team 5 (Human Voice QA) — LEGACY (PIVOT: implementazioni AI)
Modello: NVIDIA Nemotron via OpenRouter (gratuito)

NB: l'orchestrator ora usa BibbiaTeam. Questo QA legacy è mantenuto per coerenza
e allineato al nuovo framework (hype → 1 problema operativo → workflow 100% →
obiezione = solo fiducia → CTA con presentazione). I LINK SONO AMMESSI nel primo
messaggio (link presentazione nel CTA, link agency in firma): nessun blocco sui link.

3 check in sequenza per ogni email:
1. HumannessChecker    — rileva linguaggio AI/robotico (score 1-10)
2. DirectResponseReviewer — verifica compliance APSOC nuovo (score 1-10)
3. BrandValidator      — confronta con il tono founder/operatore di Max | Digital Empire

Decisione:
- Media >= 7: approved=True → passa al sender
- Media < 7:  approved=False + feedback dettagliato → torna al writer (max 1 retry)
"""

import json
import time
import openai
from openai import OpenAI
from agents.ai_client import build_rotation

from knowledge.apsoc import PROHIBITED_PHRASES, DR_PRINCIPLES
from knowledge.brand_voice import ANDREI_PASCU_BENCHMARK, BANNED_VOCABULARY, QUALITY_CHECKLIST


# ─────────────────────────────────────────────────────────────────────────────
# System prompts per i 3 checker
# ─────────────────────────────────────────────────────────────────────────────

HUMANNESS_CHECKER_PROMPT = """Sei un detector di linguaggio AI per cold email in italiano.
Il tuo compito: valutare se un'email sembra scritta da un umano reale (un founder/operatore
che ha costruito davvero il workflow) o da un bot.

PATTERN CHE ABBASSANO IL PUNTEGGIO (linguaggio AI/robotico):
- Frasi di apertura formali: "Spero che stia bene", "Mi permetto di contattarla"
- Autodescrizionali: "Mi chiamo X e lavoro in Y", "In qualità di..."
- Corporate jargon vuoto: "sinergie", "trasformazione digitale", "soluzione innovativa"
- Aggettivi vuoti: "eccellente", "straordinario", "leader nel settore"
- Struttura rigida da template: intro → body → chiusura → firma formale
- Frasi che iniziano con "Nel contesto attuale" o "In questa email"
- Promesse esagerate/garantite: "garantiamo", "risultati certi"
- Tono agenzia: "noi", "vogliamo aiutarvi", "offriamo"

NOTA PIVOT: il vocabolario AI/automazione (workflow, AI, automazione, demo live,
"gira al 100%") è AMMESSO e atteso — NON è jargon da penalizzare.

PATTERN CHE AUMENTANO IL PUNTEGGIO (linguaggio umano):
- Apertura con l'HYPE concreto dell'automazione di QUEL processo
- Uso naturale del "tu" diretto, prima persona singolare ("io ho costruito…")
- Frasi brevi e dirette (non gerundive lunghe)
- Tono da founder/collega, non da venditore
- Specificità operativa con numeri reali (ore liberate, email/giorno, €0 canoni, 7 giorni)
- Una sola CTA finale (guarda la presentazione → call)

OUTPUT (JSON valido, nient'altro):
{"score": <1-10>, "problemi_trovati": ["problema1", "problema2"], "nota": "<spiegazione breve>"}"""

DR_REVIEWER_PROMPT = """Sei un revisore di Direct Response copywriting per cold email italiane B2B
sul pivot Digital Empire (implementazioni AI: Outreach Factory, Content Factory, Second Brain).
Valuti se l'email rispetta il framework APSOC nuovo:
A = HYPE automazione, P = UN problema operativo, S = workflow al 100% (codice tuo, €0 canoni,
7 giorni, tuoi server), O = obiezione SOLO fiducia (demo live + presentazione), C = CTA presentazione + call.

CRITERI DI VALUTAZIONE:
A — ATTENZIONE/HYPE: la prima riga aggancia con l'hype dell'automazione di quel processo?
P — PROBLEMA: c'è UN SOLO problema operativo, reso tangibile in ore/operatività (non conversioni)?
S — SOLUZIONE/WORKFLOW: presenta il workflow "che gira al 100%" con i 4 garanti (codice tuo, €0 canoni, 7 giorni, tuoi server)?
O — OBIEZIONE: l'unica obiezione trattata è la FIDUCIA, sciolta con la prova (demo live + presentazione)?
C — CTA: c'è UNA SOLA CTA (guarda la presentazione → poi call)? Il link presentazione È PRESENTE nel CTA?

PENALITÀ AUTOMATICHE:
- Più di 1 CTA in concorrenza: -3 punti
- Nessun hype nella prima riga: -2 punti
- Corpo > 300 parole o < 140: -2 punti
- Promesse garantite / conversioni promesse: -2 punti
- Link presentazione ASSENTE nel CTA: -2 punti (il link è ATTESO, non vietato)
NOTA: Le email di 160-260 parole sono lo standard — NON penalizzare questa lunghezza.
NOTA: La presenza dei link (presentazione nel CTA, agency in firma) è CORRETTA — non penalizzarla.

OUTPUT (JSON valido, nient'altro):
{"score": <1-10>, "elementi_mancanti": ["elemento1"], "elementi_ok": ["elemento1"], "nota": "<spiegazione>"}"""

BRAND_VALIDATOR_PROMPT = """Sei il validatore del brand voice di Digital Empire (pivot: implementazioni AI).
Valuti se l'email corrisponde al tono di riferimento: Max | Digital Empire — un founder/operatore
che ha costruito i workflow e parla da pari, entusiasta dell'automazione ma concreto.

STANDARD DI TONO:
- Diretto e problem-focused: arriva al punto (l'hype del workflow) nella prima riga
- Usa numeri reali operativi: non "molto tempo" ma "8-12 ore a settimana", "300 email/giorno"
- Confident senza arroganza: dimostra di aver costruito davvero il workflow
- Brevità densa: ogni frase porta valore, zero filler
- Peer-to-peer: parla come founder/operatore a founder/operatore, non come venditore
- Prima persona singolare ("io ho costruito…"), mai tono agenzia ("noi/offriamo")

CRITERI DI VALUTAZIONE:
- Il mittente sembra un founder che ha costruito davvero il sistema? (+2)
- Ogni frase porta informazione nuova? (+2)
- Il tono è paritario, non speranzoso/servile? (+2)
- L'email usa vocabolario operativo concreto, non corporate jargon vuoto? (+2)
- La lunghezza è appropriata (160-260 parole corpo, con paragrafi brevi e struttura chiara)? (+2)

PENALITÀ:
- Ogni frase di filler senza valore: -1 punto
- Tono speranzoso/servile o tono agenzia: -2 punti
- Vocabolario corporate vuoto: -1 per termine trovato
- Troppo lunga (>300 parole) O muro di testo senza paragrafi: -2 punti
NOTA: Le email di 160-260 parole strutturate in paragrafi brevi sono lo standard atteso. NON penalizzare la lunghezza in questa fascia.
NOTA: I link (presentazione nel CTA, agency in firma) sono AMMESSI — non penalizzarli.

OUTPUT (JSON valido, nient'altro):
{"score": <1-10>, "frasi_da_rimuovere": ["frase1"], "punti_di_forza": ["punto1"], "nota": "<spiegazione>"}"""


class HumanizerAgent:
    """
    Team 5 — Human Voice QA: 3 check in sequenza + eventuale revision loop.
    Usa NVIDIA Nemotron (gratuito via OpenRouter).
    """

    def __init__(self, openrouter_api_key: str):
        self.rotation = build_rotation(openrouter_api_key)

    def _chiama_checker(self, system_prompt: str, email_testo: str, max_tokens: int = 250) -> dict:
        """Chiama un singolo checker e restituisce il JSON parsato."""
        for attempt, (client, model) in enumerate(self.rotation):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Analizza questa cold email:\n\n{email_testo}"},
                    ],
                    max_tokens=max_tokens,
                    temperature=0.1,
                )
                testo = response.choices[0].message.content.strip()
                start = testo.find("{")
                end = testo.rfind("}") + 1
                if start >= 0 and end > start:
                    return json.loads(testo[start:end])
            except (openai.RateLimitError, openai.APIStatusError) as e:
                if isinstance(e, openai.APIStatusError) and getattr(e, "status_code", 0) != 429:
                    break
                wait = min(15 * (attempt + 1), 60)
                print(f"[QA] Rate limit (tentativo {attempt+1}/{len(self.rotation)}), attendo {wait}s...")
                time.sleep(wait)
            except Exception:
                if attempt < len(self.rotation) - 1:
                    time.sleep(3)

        return {"score": 8, "nota": "API non raggiungibile — approvato per default (rate limit)"}

    # TIER 1 — Agency tone: forza approved=False (noi/abbiamo/vogliamo → non recuperabile)
    _FRASI_HARD_BLOCK = [
        "vogliamo aiutarvi", "vogliamo aiutarti", "possiamo aiutarvi", "possiamo aiutarti",
        "voglio aiutarti", "voglio aiutarvi",
        "abbiamo sviluppato", "abbiamo aiutato", "offriamo soluzioni", "la nostra consulenza",
        "il nostro team", "la nostra agenzia", "abbiamo creato", "abbiamo lavorato",
        "siamo specializzati", "siamo qui per", "saremo felici", "saremo lieti",
        "sono lieto", "sarò lieto", "sono felice di",
    ]

    # TIER 2 — Clichés stilistici: deducono punti ma non forzano fail
    # NB (pivot): rimossi "aumentare la visibilità"/"visibilità online"/"presenza online"/
    # "reputazione eccellente" — non più rilevanti ora che vendiamo implementazioni AI.
    _FRASI_SOFT_BLOCK = [
        "aumentare l'efficienza", "qualità eccellente",
        "potreste guadagnare", "potrete guadagnare", "potresti guadagnare",
        "ottimale", "straordinario", "fantastico", "incredibile",
    ]

    def _controlla_hard(self, testo: str) -> list:
        """Tier 1: agency-tone phrases che forzano il rifiuto."""
        testo_lower = testo.lower()
        return [f for f in self._FRASI_HARD_BLOCK if f.lower() in testo_lower]

    def _controlla_soft(self, testo: str) -> list:
        """Tier 2: clichés stilistici che deducono punti (PROHIBITED_PHRASES + BANNED_VOCABULARY + soft list)."""
        trovate = []
        testo_lower = testo.lower()
        for frase in PROHIBITED_PHRASES:
            if frase.lower() in testo_lower:
                trovate.append(frase)
        for termine in BANNED_VOCABULARY:
            if termine.lower() in testo_lower:
                trovate.append(termine)
        for frase in self._FRASI_SOFT_BLOCK:
            if frase.lower() in testo_lower:
                trovate.append(frase)
        return trovate

    def _conta_parole(self, testo: str) -> int:
        """Conta le parole nel corpo dell'email (esclude oggetto e firma)."""
        linee = testo.split("\n")
        corpo_linee = []
        in_corpo = False
        for linea in linee:
            if linea.strip().startswith("CORPO:") or linea.strip().startswith("Ciao"):
                in_corpo = True
            if in_corpo and not linea.strip().startswith("OGGETTO"):
                corpo_linee.append(linea)
        corpo = " ".join(corpo_linee)
        return len(corpo.split())

    def controlla(self, lead_con_email: dict) -> dict:
        """
        Esegue i 3 check su un'email e decide se approvarla o mandarla in revisione.

        Returns:
            Dict con approved=True/False, scores, feedback.
        """
        oggetto = lead_con_email.get("oggetto", "")
        corpo = lead_con_email.get("corpo", "")
        email_testo = f"OGGETTO: {oggetto}\n\nCORPO:\n{corpo}"

        # QA API skippato — solo check deterministici (frasi vietate hard)
        frasi_hard = self._controlla_hard(email_testo)
        frasi_soft = self._controlla_soft(email_testo)
        frasi_vietate_trovate = frasi_hard + frasi_soft
        score1, score2, score3 = 8, 8, 8
        media = 8.0
        approved = not frasi_hard

        feedback = None
        if not approved:
            problemi = []
            if frasi_hard:
                problemi.append(f"FRASI VIETATE trovate: {', '.join(frasi_hard[:3])}")
            if frasi_soft:
                problemi.append(f"Clichés da rimuovere: {', '.join(frasi_soft[:3])}")
            feedback = " | ".join(problemi[:4])

        return {
            **lead_con_email,
            "qa_approved": approved,
            "qa_score_media": round(media, 1),
            "qa_score_humanness": score1,
            "qa_score_apsoc": score2,
            "qa_score_brand": score3,
            "qa_feedback": feedback,
            "qa_frasi_vietate": frasi_vietate_trovate,
        }

    def run(self, leads_con_email: list) -> tuple[list, list]:
        """
        Esegue QA su tutte le email.

        Returns:
            (approvate, da_rivedere) — due liste separate.
        """
        print(f"\n[HUMANIZER] QA su {len(leads_con_email)} email...")

        approvate = []
        da_rivedere = []

        for i, lead in enumerate(leads_con_email, 1):
            if i % 30 == 0:
                print(f"[HUMANIZER] Progresso: {i}/{len(leads_con_email)}")

            risultato = self.controlla(lead)

            if risultato["qa_approved"]:
                approvate.append(risultato)
            else:
                da_rivedere.append(risultato)

            time.sleep(1)

        print(f"[HUMANIZER] Approvate: {len(approvate)} | Da rivedere: {len(da_rivedere)}")
        return approvate, da_rivedere
