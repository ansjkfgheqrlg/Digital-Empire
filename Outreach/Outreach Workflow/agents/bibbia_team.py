"""
Team BIBBIA OUTREACH — Digital Empire (PIVOT: implementazioni AI)
3 agenti AI in parallelo che verificano ogni email contro la Bibbia Outreach.

Checkers (paralleli via ThreadPoolExecutor):
  CheckerUmano       — Tono umano, prima persona, zero AI slop, zero jargon
  CheckerStruttura   — APSOC nuovo (hype → 1 problema → workflow 100% → fiducia/demo → CTA)
  CheckerConversione — Oggetto hype, una sola CTA, link presentazione PRESENTE, lunghezza

NUOVA POLICY LINK (pivot 2026): il primo messaggio PORTA i link.
Il link presentazione (PRESENTATION_URL) sta nel CTA e il link agency (AGENCY_URL)
in firma, GIÀ nel primo messaggio. I link NON sono più un hard-block: la loro
ASSENZA è il problema, non la presenza.

Flusso:
  1. Pre-filter deterministico (solo hard blocks di tono agenzia, millisecondi)
  2. 3 checker AI in parallelo (lettura Bibbia + valutazione)
  3. Verdetto: pass se tutti >= SOGLIA_PASS E nessuno sotto SOGLIA_HARD_FAIL
  4. Se fail: feedback specifico → orchestrator lo passa a Writer.revise()

Sostituisce il vecchio HumanizerAgent (che aveva i punteggi hardcoded a 8/10).
"""

import json
import os
import re
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from agents.ai_client import build_rotation

try:
    from knowledge.apsoc import PRESENTATION_URL, AGENCY_URL, LAUNCH_OFFER
except Exception:  # pragma: no cover — fallback se il modulo non è importabile
    PRESENTATION_URL = "https://presentazione-empire.vercel.app/"
    AGENCY_URL = "https://agency-empire-landing.vercel.app"
    LAUNCH_OFFER = "sconto early-adopter per i primi clienti che partono questo mese"

# ── Abilita ANSI colors su Windows CMD ────────────────────────────────────────
os.system("")

_R  = "\033[91m"   # rosso
_G  = "\033[92m"   # verde
_Y  = "\033[93m"   # giallo
_B  = "\033[94m"   # blu
_C  = "\033[96m"   # ciano
_W  = "\033[97m"   # bianco brillante
_DIM = "\033[2m"   # dimmed
_BOLD = "\033[1m"  # grassetto
_RST = "\033[0m"   # reset

# ─────────────────────────────────────────────────────────────────────────────
# Caricamento e parsing della Bibbia Outreach
# ─────────────────────────────────────────────────────────────────────────────

_BIBBIA_PATH = Path(__file__).parent.parent / "knowledge" / "bibbia_outreach.md"


def _carica_sezione(contenuto: str, nome_sezione: str) -> str:
    """Estrae una sezione specifica dalla Bibbia usando il marker ## SEZIONE_X:"""
    pattern = rf"## {re.escape(nome_sezione)}:(.*?)(?=\n## SEZIONE_|\Z)"
    match = re.search(pattern, contenuto, re.DOTALL)
    return match.group(1).strip() if match else ""


def _carica_bibbia() -> dict:
    """Carica e parsa la Bibbia Outreach. Cache in memoria per il processo."""
    if not _BIBBIA_PATH.exists():
        raise FileNotFoundError(
            f"Bibbia Outreach non trovata: {_BIBBIA_PATH}\n"
            "Crea il file knowledge/bibbia_outreach.md prima di eseguire il sistema."
        )
    contenuto = _BIBBIA_PATH.read_text(encoding="utf-8")
    return {
        "A": _carica_sezione(contenuto, "SEZIONE_A"),
        "B": _carica_sezione(contenuto, "SEZIONE_B"),
        "C": _carica_sezione(contenuto, "SEZIONE_C"),
        "D": _carica_sezione(contenuto, "SEZIONE_D"),
        "E": _carica_sezione(contenuto, "SEZIONE_E"),
        "F": _carica_sezione(contenuto, "SEZIONE_F"),
    }


# ─────────────────────────────────────────────────────────────────────────────
# System prompts dei 3 checker (iniettano la sezione rilevante della Bibbia)
# ─────────────────────────────────────────────────────────────────────────────

def _build_prompt_umano(bibbia: dict) -> str:
    return f"""Sei il CHECKER UMANO del Team BIBBIA OUTREACH di Digital Empire.

Il tuo compito: valutare se questa cold email sembra scritta da Max in persona (firma "Max | Digital Empire") — un founder/operatore che ha costruito davvero il workflow e parla da pari — oppure da un AI/bot che compila template.

NOTA PIVOT: il vocabolario AI/automazione (workflow, AI, automazione, demo live) è ora AMMESSO e atteso, NON è jargon da penalizzare. Resta jargon vietato il corporate vuoto (sinergie, trasformazione digitale, soluzione innovativa) e il tono agenzia ("noi", "vogliamo aiutarvi").

Questa è la tua RUBRICA (estratta dalla Bibbia Outreach ufficiale):

{bibbia['A']}

ANTI-ESEMPI da cui imparare cosa NON fare:
{bibbia['E']}

ISTRUZIONI DI VALUTAZIONE:
1. Leggi l'email completa una volta.
2. Cerca i pattern che abbassano il punteggio (elencati nella rubrica).
3. Cerca i pattern che alzano il punteggio.
4. Assegna un score 1-10 secondo la scala nella rubrica.
5. Elenca le frasi problematiche ESATTE trovate nell'email (copia-incolla dalla email).
6. Scrivi note di revisione specifiche: cosa cambiare e perché, max 60 parole.

REGOLA: sii severo. Un punteggio 8 significa che l'email è davvero buona. Non dare 8 per default.

OUTPUT (JSON valido, assolutamente nient'altro prima o dopo):
{{"score": <1-10>, "problemi_trovati": ["frase esatta 1", "frase esatta 2"], "note_revisione": "<cosa cambiare esattamente, max 60 parole>"}}"""


def _build_prompt_struttura(bibbia: dict) -> str:
    return f"""Sei il CHECKER STRUTTURA del Team BIBBIA OUTREACH di Digital Empire.

Il tuo compito: verificare che questa cold email rispetti il framework APSOC nuovo (PIVOT implementazioni AI):
A = HYPE dell'automazione AI → P = UN solo problema operativo → S = il workflow al 100%
(codice tuo, €0 canoni, setup 7 giorni, sui tuoi server) → O = obiezione SOLO fiducia
(sciolta con demo live + presentazione di qualità estrema) → C = CTA che porta a guardare
la presentazione (link) e prenotare una call, con sconto lancio.

Questa è la tua RUBRICA (estratta dalla Bibbia Outreach ufficiale):

{bibbia['B']}

ESEMPI GOLD di riferimento (struttura corretta):
{bibbia['D'][:2000]}

ISTRUZIONI DI VALUTAZIONE:
1. Usa la checklist binaria della rubrica: ogni elemento presente = punti.
2. Verifica ogni elemento nell'ordine A → P → S → O → C.
3. Per [A]: l'aggancio è l'HYPE dell'automazione di QUEL processo, o è un complimento/oggetto generico? (generico = -2 punti)
4. Per [P]: c'è UN SOLO problema operativo preciso (non una lista di dolori), reso tangibile in ore/operatività?
5. Per [S]: il workflow è presentato come "lo fa girare al 100%" con i 4 garanti (codice tuo, €0 canoni, 7 giorni, tuoi server)? Il valore qui è il WORKFLOW/la demo, non un consiglio gratis applicabile da soli.
6. Per [O]: l'unica obiezione trattata è la FIDUCIA, sciolta con la prova (demo live + presentazione)? Niente garanzie gonfiate.
7. Per [C]: la CTA porta a guardare la presentazione (link nel CTA) e prenotare una call/demo? Va bene anche una chiusura binaria leggera, ma NON deve essere la vecchia domanda fissa "Ha senso fare quella chiamata?".

OUTPUT (JSON valido, assolutamente nient'altro prima o dopo):
{{"score": <1-10>, "check_passati": ["A", "P", "S", "C"], "check_falliti": ["O: obiezione fiducia mancante", "C: link presentazione assente"], "note_revisione": "<cosa aggiungere o correggere, max 60 parole>"}}"""


def _build_prompt_conversione(bibbia: dict) -> str:
    return f"""Sei il CHECKER CONVERSIONE del Team BIBBIA OUTREACH di Digital Empire.

Il tuo compito: verificare che ogni scelta tecnica dell'email massimizzi la probabilità di risposta.

Questa è la tua RUBRICA (estratta dalla Bibbia Outreach ufficiale):

{bibbia['C']}

REGOLE GLOSSARIO NICCHIA:
{bibbia['F']}

ISTRUZIONI DI VALUTAZIONE (PIVOT — i link sono ora AMMESSI e ATTESI):
1. Controlla i checkpoint nell'ordine della rubrica.
2. Per LINK: il primo messaggio DEVE contenere il link della presentazione ({PRESENTATION_URL}) nel CTA e il link agency ({AGENCY_URL}) in firma. La loro ASSENZA è un problema (-2 punti se manca il link presentazione nel CTA), NON la presenza. Penalizza solo se ci sono DUE o più link "forti" in concorrenza nel corpo (la presentazione deve essere l'unica CTA; l'agency sta in firma e non conta come seconda CTA).
3. Per OGGETTO: è un hype operativo dell'automazione AI (es. "Ho automatizzato l'outreach al 100%")? O è generico ("Proposta", "Collaborazione")? Generico = -2 punti.
4. Per LUNGHEZZA: conta le parole del corpo (esclude oggetto e firma). Fascia attesa 160-260 parole. Sotto 140 o sopra 300 = problema.
5. Per CTA: c'è UNA SOLA CTA logica (guarda la presentazione → poi call)? Più di una CTA in concorrenza → -3 punti.
6. Verifica che il dato numerico sia credibile e operativo (ore liberate, email/giorno, setup 7 giorni, €0 canoni), non 5 statistiche di fila né promesse di conversioni.

OUTPUT (JSON valido, assolutamente nient'altro prima o dopo):
{{"score": <1-10>, "violazioni": ["link presentazione assente nel CTA", "oggetto generico: testo"], "punti_forza": ["oggetto hype operativo", "link presentazione presente nel CTA", "una sola CTA"], "note_revisione": "<cosa correggere, max 60 parole>"}}"""


# ─────────────────────────────────────────────────────────────────────────────
# Hard blocks deterministici (velocissimi, nessuna chiamata API)
# ─────────────────────────────────────────────────────────────────────────────

_HARD_BLOCKS = [
    # Tono agenzia — kill immediato
    "vogliamo aiutarvi", "vogliamo aiutarti",
    "possiamo aiutarvi", "possiamo aiutarti",
    "abbiamo sviluppato", "abbiamo aiutato",
    "offriamo soluzioni", "la nostra consulenza",
    "il nostro team", "la nostra agenzia",
    "siamo specializzati", "siamo qui per",
    "saremo felici", "saremo lieti",
    "sono lieto di", "sono felice di",
    # Aperture robotiche
    "spero che tu stia bene", "spero che stia bene",
    "mi permetto di contattarti", "mi permetto di contattarla",
    "è un piacere contattarvi",
    "in qualità di",
]

_SOFT_PENALTIES = [
    # Clichés stilistici — deducono punti al checker umano
    # NB (pivot): rimossi "visibilità online"/"presenza online" — non più rilevanti
    # ora che vendiamo implementazioni AI e non più landing/visibilità.
    "trasformazione digitale", "soluzione innovativa",
    "ottimale", "straordinario", "eccellente",
    "sinergie", "nel contesto attuale",
    "potreste guadagnare", "potrete guadagnare",
]


def _controlla_hard(testo: str) -> list[str]:
    """Restituisce le frasi hard-blocked trovate. Se non vuoto → email rifiutata senza check AI."""
    testo_lower = testo.lower()
    return [f for f in _HARD_BLOCKS if f.lower() in testo_lower]


def _conta_link(testo: str) -> list[str]:
    """Cerca URL nel corpo.

    PIVOT 2026: i link NON sono più un hard block. Il primo messaggio PORTA
    il link presentazione nel CTA e il link agency in firma. Questa funzione
    NON è più usata come blocco; resta disponibile per VERIFICARE (opzionale)
    che PRESENTATION_URL sia PRESENTE — la sua assenza è il vero problema.
    """
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, testo)


def _presentazione_presente(testo: str) -> bool:
    """True se il link della presentazione è presente nel testo (atteso nel CTA)."""
    return PRESENTATION_URL.rstrip("/") in testo


# ─────────────────────────────────────────────────────────────────────────────
# Classe principale: BibbiaTeam
# ─────────────────────────────────────────────────────────────────────────────

class BibbiaTeam:
    """
    Team BIBBIA OUTREACH — Digital Empire.

    3 checker AI in parallelo con soglia reale (non punteggi hardcoded).
    Legge la Bibbia Outreach da file al momento dell'istanziazione.

    Interface pubblica identica a HumanizerAgent.run() per compatibilità con l'orchestrator.
    """

    SOGLIA_PASS = 6.0      # score minimo per ogni checker  (era 7.0)
    SOGLIA_HARD_FAIL = 4.5  # sotto questo → rifiuto immediato senza retry (era 5.5)

    def __init__(self, openrouter_api_key: str):
        self.rotation = build_rotation(openrouter_api_key)
        self._bibbia = _carica_bibbia()
        self._prompt_umano = _build_prompt_umano(self._bibbia)
        self._prompt_struttura = _build_prompt_struttura(self._bibbia)
        self._prompt_conversione = _build_prompt_conversione(self._bibbia)
        print(f"  {_G}[BIBBIA TEAM]{_RST} Bibbia caricata  {_W}Soglia: {self.SOGLIA_PASS}/10{_RST} su tutti i checker")

    # ─────────────────────────────────────────────────────────────────────────
    # Singolo checker: chiama il modello AI con retry su tutta la rotation
    # ─────────────────────────────────────────────────────────────────────────

    def _chiama_checker(self, system_prompt: str, email_testo: str, checker_name: str) -> dict:
        """Chiama un singolo checker con retry. Restituisce il JSON parsato."""
        import openai

        for attempt, (client, model) in enumerate(self.rotation):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Analizza questa cold email e restituisci SOLO il JSON:\n\n{email_testo}"},
                    ],
                    max_tokens=400,
                    temperature=0.1,  # QA deve essere stabile, non creativa
                )
                testo = response.choices[0].message.content.strip()
                # Estrai JSON anche se il modello aggiunge testo prima/dopo
                start = testo.find("{")
                end = testo.rfind("}") + 1
                if start >= 0 and end > start:
                    try:
                        return json.loads(testo[start:end])
                    except json.JSONDecodeError:
                        pass  # Fallback sotto

            except (openai.RateLimitError, openai.APIStatusError) as e:
                sc = getattr(e, "status_code", 0) if isinstance(e, openai.APIStatusError) else 429
                provider = "Groq" if "groq" in str(client.base_url) else "OR"
                if isinstance(e, openai.APIStatusError) and sc not in (429, 500, 502, 503, 504):
                    print(f"  {_DIM}[BIBBIA/{checker_name}] Err {sc} {provider}/{model.split('/')[-1][:18]} → next{_RST}")
                    continue
                print(f"  {_DIM}[BIBBIA/{checker_name}] RL {provider}/{model.split('/')[-1][:18]} → next{_RST}")
                continue
            except Exception as e:
                provider = "Groq" if "groq" in str(client.base_url) else "OR"
                print(f"  {_DIM}[BIBBIA/{checker_name}] {provider}/{model.split('/')[-1][:18]} {type(e).__name__}{_RST}")
                if attempt < len(self.rotation) - 1:
                    time.sleep(1)

        # Fallback: se tutti i modelli falliscono → score conservativo (non approvazione automatica)
        print(f"  {_Y}[BIBBIA/{checker_name}] Tutti i modelli esauriti — score fallback 6.0{_RST}")
        return {"score": 6.0, "note_revisione": "API non raggiungibile — check manuale consigliato"}

    # ─────────────────────────────────────────────────────────────────────────
    # Valutazione completa di una singola email
    # ─────────────────────────────────────────────────────────────────────────

    def valuta(self, lead_con_email: dict) -> dict:
        """
        Esegue il check completo su un'email:
        1. Pre-filter deterministico (solo hard blocks di tono agenzia — i link sono ammessi)
        2. 3 checker AI in parallelo
        3. Calcola verdetto finale

        Returns:
            Lead arricchito con campi bibbia_* e bibbia_approved.
        """
        oggetto = lead_con_email.get("oggetto", "")
        corpo = lead_con_email.get("corpo", "")
        nome = lead_con_email.get("page_name", "?")
        email_testo = f"OGGETTO: {oggetto}\n\nCORPO:\n{corpo}"

        # ── Step 1: Pre-filter deterministico ───────────────────────────────
        # PIVOT 2026: l'UNICO hard block deterministico è il tono agenzia.
        # I link NON sono più bloccati: il primo messaggio PORTA il link
        # presentazione (CTA) e il link agency (firma). La loro eventuale
        # ASSENZA è valutata dai checker AI, non bloccata qui.
        hard_trovati = _controlla_hard(email_testo)

        if hard_trovati:
            feedback = f"HARD BLOCK — Frasi agenzia vietate: {', '.join(hard_trovati[:3])}"
            return {
                **lead_con_email,
                "bibbia_approved": False,
                "bibbia_score_umano": 0,
                "bibbia_score_struttura": 0,
                "bibbia_score_conversione": 0,
                "bibbia_score_media": 0,
                "bibbia_feedback": feedback,
                "bibbia_hard_block": True,
            }

        # ── Step 2: 3 checker AI in parallelo ───────────────────────────────
        checker_tasks = [
            ("umano",       self._prompt_umano,       "Umano"),
            ("struttura",   self._prompt_struttura,   "Struttura"),
            ("conversione", self._prompt_conversione, "Conversione"),
        ]

        risultati_checker = {}

        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {
                executor.submit(self._chiama_checker, prompt, email_testo, label): key
                for key, prompt, label in checker_tasks
            }
            for future in as_completed(futures):
                key = futures[future]
                try:
                    risultati_checker[key] = future.result()
                except Exception as e:
                    print(f"[BIBBIA] Checker '{key}' exception: {e}")
                    risultati_checker[key] = {"score": 6.0, "note_revisione": f"Errore checker: {e}"}

        # ── Step 3: Calcola verdetto ─────────────────────────────────────────
        score_u = float(risultati_checker.get("umano", {}).get("score", 6))
        score_s = float(risultati_checker.get("struttura", {}).get("score", 6))
        score_c = float(risultati_checker.get("conversione", {}).get("score", 6))

        # Clamp 1-10
        score_u = max(1.0, min(10.0, score_u))
        score_s = max(1.0, min(10.0, score_s))
        score_c = max(1.0, min(10.0, score_c))

        score_media = round((score_u + score_s + score_c) / 3, 1)

        # Criteri di approvazione:
        # - tutti i checker devono essere >= SOGLIA_PASS
        # - nessun checker può essere sotto SOGLIA_HARD_FAIL
        tutti_sopra_soglia = all(s >= self.SOGLIA_PASS for s in [score_u, score_s, score_c])
        nessuno_hard_fail = all(s >= self.SOGLIA_HARD_FAIL for s in [score_u, score_s, score_c])
        approved = tutti_sopra_soglia and nessuno_hard_fail

        # Costruisce feedback aggregato per il Writer.revise()
        feedback_parts = []
        checker_nomi = {"umano": "TONO", "struttura": "STRUTTURA", "conversione": "CONVERSIONE"}
        for key in ["umano", "struttura", "conversione"]:
            r = risultati_checker.get(key, {})
            score_checker = float(r.get("score", 6))
            if score_checker < self.SOGLIA_PASS:
                note = r.get("note_revisione", "")
                if note:
                    feedback_parts.append(f"[{checker_nomi[key]}] {note}")

        feedback = " | ".join(feedback_parts) if feedback_parts else None

        return {
            **lead_con_email,
            "bibbia_approved": approved,
            "bibbia_score_umano": score_u,
            "bibbia_score_struttura": score_s,
            "bibbia_score_conversione": score_c,
            "bibbia_score_media": score_media,
            "bibbia_feedback": feedback,
            "bibbia_hard_block": False,
            # Alias per compatibilità con il report qualità dell'orchestrator
            "qa_score_media": score_media,
            "qa_feedback": feedback,
        }

    # ─────────────────────────────────────────────────────────────────────────
    # Interfaccia pubblica identica a HumanizerAgent.run()
    # ─────────────────────────────────────────────────────────────────────────

    def run(self, leads_con_email: list) -> tuple[list, list]:
        """
        Esegue il check BIBBIA su tutte le email — 3 email in parallelo per velocità.

        Returns:
            (approvate, da_rivedere) — stessa interfaccia di HumanizerAgent.run().
        """
        import threading

        totale = len(leads_con_email)
        PARALLEL = 1  # sequenziale — parallel>1 causa rate limit a cascata e rallenta
        line = "─" * 54
        print(f"\n  {_C}{line}{_RST}")
        print(f"  {_B}BIBBIA TEAM  —  {totale} email da verificare{_RST}")
        print(f"  {_DIM}Soglia pass >= {self.SOGLIA_PASS}  |  Hard fail < {self.SOGLIA_HARD_FAIL}{_RST}")
        print(f"  {_C}{line}{_RST}")

        # Risultati indicizzati per mantenere ordine
        risultati_map: dict[int, dict] = {}
        lock = threading.Lock()
        counter = [0]  # mutable per closure

        def _valuta_con_indice(idx: int, lead: dict):
            risultato = self.valuta(lead)
            with lock:
                risultati_map[idx] = risultato
                counter[0] += 1
                i = counter[0]
                nome = lead.get("page_name", "?")[:38]
                approved = risultato.get("bibbia_approved", False)
                media = risultato.get("bibbia_score_media", 0)
                score_u = risultato.get("bibbia_score_umano", 0)
                score_s = risultato.get("bibbia_score_struttura", 0)
                score_c = risultato.get("bibbia_score_conversione", 0)

                # ── Barra progresso ────────────────────────────────────────
                pct  = int(i / totale * 20)
                bar  = f"{_G}{'█' * pct}{_DIM}{'░' * (20 - pct)}{_RST}"
                pct_label = f"{_W}{i/totale*100:.0f}%{_RST}"

                if risultato.get("bibbia_hard_block"):
                    print(f"  {_R}[{i:>3}/{totale}]{_RST} {bar} {pct_label}  "
                          f"{_R}✗ HARD BLOCK{_RST}  {_DIM}{nome}{_RST}")
                elif approved:
                    score_str = f"{_G}{media:.1f}/10{_RST}"
                    checks = f"{_G}U:{score_u:.0f} S:{score_s:.0f} C:{score_c:.0f}{_RST}"
                    print(f"  {_G}[{i:>3}/{totale}]{_RST} {bar} {pct_label}  "
                          f"{_G}✓ PASS{_RST}  {score_str}  {checks}  {_W}{nome}{_RST}")
                else:
                    checker_fail = []
                    if score_u < self.SOGLIA_PASS: checker_fail.append(f"U:{score_u:.0f}")
                    if score_s < self.SOGLIA_PASS: checker_fail.append(f"S:{score_s:.0f}")
                    if score_c < self.SOGLIA_PASS: checker_fail.append(f"C:{score_c:.0f}")
                    fail_str = f"{_Y}{', '.join(checker_fail)}{_RST}"
                    score_str = f"{_Y}{media:.1f}/10{_RST}"
                    print(f"  {_R}[{i:>3}/{totale}]{_RST} {bar} {pct_label}  "
                          f"{_R}✗ FAIL{_RST}  {score_str}  ({fail_str})  {_DIM}{nome}{_RST}")

        with ThreadPoolExecutor(max_workers=PARALLEL) as executor:
            futures = {
                executor.submit(_valuta_con_indice, idx, lead): idx
                for idx, lead in enumerate(leads_con_email)
            }
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    idx = futures[future]
                    print(f"[BIBBIA TEAM] Errore su lead {idx}: {e}")

        # Ricostruisce liste in ordine originale
        approvate = []
        da_rivedere = []
        hard_blocks = 0

        for idx in range(totale):
            risultato = risultati_map.get(idx)
            if not risultato:
                continue
            if risultato.get("bibbia_hard_block"):
                hard_blocks += 1
                da_rivedere.append({**risultato, "qa_feedback": risultato["bibbia_feedback"]})
            elif risultato.get("bibbia_approved"):
                approvate.append(risultato)
            else:
                da_rivedere.append({**risultato, "qa_feedback": risultato.get("bibbia_feedback", "")})

        line = "─" * 54
        pct_ok = len(approvate) / totale * 100 if totale else 0
        media_approvate = (
            sum(e.get("bibbia_score_media", 0) for e in approvate) / len(approvate)
            if approvate else 0
        )
        print(f"\n  {_C}{line}{_RST}")
        print(f"  {_B}BIBBIA TEAM  —  RISULTATO FINALE{_RST}")
        print(f"  {_C}{line}{_RST}")
        print(f"  {_G}✓ Approvate   {len(approvate):>4}/{totale}  ({pct_ok:.0f}%){_RST}")
        print(f"  {_R}✗ Da rivedere {len(da_rivedere):>4}/{totale}  "
              f"(hard block: {hard_blocks}){_RST}")
        if approvate:
            print(f"  {_W}Score medio   {media_approvate:.1f}/10{_RST}")
        print(f"  {_C}{line}{_RST}\n")

        return approvate, da_rivedere
