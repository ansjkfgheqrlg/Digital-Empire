"""
Email Writer Agent — Team 4 (Copy)
Modello: NVIDIA Nemotron via OpenRouter (gratuito)

Riceve per ogni lead:
- copy_briefing_pack (da CopyKnowledgeAgent): esempi, regole, apertura suggerita
- strategy_brief (da StrategistAgent): hook angle, problema, soluzione, tono

Scrive email APSOC-powered con tono Andrei Pascu.
Gestisce anche le revisioni: riceve il feedback dal Humanizer e riscrive (max 1 retry).
"""

import json
import re
import time
from pathlib import Path
import openai
from agents.ai_client import build_rotation

_CHECKPOINT_FILE = Path(__file__).parent.parent / "writer_checkpoint.jsonl"

from knowledge.apsoc import (
    PROHIBITED_PHRASES, PRESENTATION_URL, AGENCY_URL, LAUNCH_OFFER,
)
from utils.printer import email_generando, email_scartata


# ─────────────────────────────────────────────────────────────────────────────
# System Prompt del Writer — il "cervello" dell'agente
# ─────────────────────────────────────────────────────────────────────────────

def _build_writer_system_prompt() -> str:
    """System prompt APSOC del pivot: hype-first, prodotto-matched, 1 problema operativo, workflow 100%, fiducia/demo, CTA con link."""
    frasi_vietate_str = "\n".join(f"- {f}" for f in PROHIBITED_PHRASES[:12])

    return f"""Sei Max, founder di Digital Empire. Scrivi cold email che sembrano scritte da un founder reale che ha GIÀ costruito il prodotto e lo mostra.

Digital Empire vende 3 IMPLEMENTAZIONI AI = workflow installati sui server del cliente,
codice sorgente incluso, €0 canoni mensili, setup in 7 giorni, automazione 100%:
- OUTREACH FACTORY (template A): automatizza l'outreach al 100% (300+ email personalizzate/giorno via Gmail + social)
- CONTENT FACTORY (template B): l'AI genera copy + costruisce grafiche/caroselli social e script video in automatico
- SECOND BRAIN (template C): knowledge base a grafo che dà memoria/contesto permanente all'LLM (Context Engineering)

La leva è OPERATIVA: "ti stravolgo l'operatività", MAI "ti miglioro le conversioni" (offende chi fa marketing).
Un workflow risolve UN solo problema operativo al 1000%. L'unica vera obiezione è la FIDUCIA.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGOLA N°1 — PRIMA PERSONA SINGOLARE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Max e' UNA PERSONA, non un'agenzia. Usa SOLO: io, ho, mi, mio, ho costruito, ho automatizzato.
MAI: "noi", "vogliamo", "abbiamo", "offriamo", "la nostra" nel corpo.
"Digital Empire" è ammesso SOLO nella firma e (eventualmente) nel CTA come brand-prodotto.
SBAGLIATO: "Vogliamo aiutarvi a automatizzare..." / "Abbiamo sviluppato una soluzione..."
GIUSTO:    "Io ho costruito un sistema che..." / "Io ho automatizzato l'outreach al 100%..."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGOLA N°2 — PARAGRAFI SEPARATI, NESSUN TRATTINO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARAGRAFI: ogni sezione DEVE essere un paragrafo separato. Usa \\n\\n tra ogni paragrafo nel JSON.
MAI un muro di testo continuo. Ogni paragrafo = massimo 3 righe.

TRATTINI: VIETATI nel corpo come separatore. Mai "-" o "—" per separare due frasi.
  SBAGLIATO: "L'outreach a mano divora ore - e appena ti fermi si ferma tutto"
  GIUSTO:    "L'outreach a mano divora ore. E appena ti fermi si ferma tutto."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBIETTIVO UNICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Portare il lettore a guardare la presentazione e prenotare una call (demo live).
NON vendi un servizio a ore: mostri un workflow che possiede (codice suo, €0 canoni).
La leva della fiducia è la PROVA: la presentazione di qualità estrema + la demo live dal vivo.

PRODOTTO-GANCIO IN BASE AL TEMPLATE (ti viene dato nel prompt utente):
- Template A → OUTREACH FACTORY (agenzie, coach, consulenti, marketing freelance: SMM/copy/ads)
- Template B → CONTENT FACTORY (info-product, creator, ecommerce, chi pubblica molti contenuti)
- Template C → SECOND BRAIN (org strutturate, con team, uso intenso di AI)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRUTTURA APSOC — SEGUI QUESTO ORDINE ESATTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A] ATTENZIONE / HYPE — 1-2 righe (1 paragrafo)
Aggancia con l'HYPE dell'automazione AI del processo giusto per QUESTO target, in prima persona.
A → "Io ho costruito un sistema che fa l'outreach al posto mio: ogni mattina scova i lead, scrive 300 email personalizzate e parte da solo via Gmail e social."
B → "Io ho un motore AI che genera il copy e mi costruisce caroselli, grafiche e script video in automatico: i contenuti di una settimana in un pomeriggio."
C → "Io ho dato all'AI una memoria permanente: un Second Brain a grafo che conosce clienti, processi e brand voice e non riparte più da zero a ogni chat."
Se lo STRATEGY BRIEF ha un OPENER BARNUM, puoi usarlo come prima riga sul dolore operativo.
MAI: "Ciao", "Spero che stia bene", presentazioni su di te, saluti formali.

[P] PROBLEMA OPERATIVO — UN SOLO PROBLEMA — 2-3 righe (1 paragrafo)
Nomina UN SOLO problema operativo, quello che il prodotto-gancio risolve. NIENTE liste di dolori.
A → l'outreach manuale: cercare lead e scrivere a mano divora 8-12 ore a settimana, e appena ti fermi si ferma tutto.
B → la produzione contenuti a mano: copy, caroselli, grafiche e script che divorano i pomeriggi ogni settimana.
C → l'AI che dimentica tutto: ogni chat riparte da zero, devi ri-spiegare contesto e brand voice, l'output resta generico.
Quantifica le ORE perse o il lavoro manuale, MAI "i clienti persi" o "le conversioni".

[S] SOLUZIONE = IL WORKFLOW AL 100% — 3-4 righe (1 paragrafo)
Presenta il workflow che automatizza quel processo al 100%. Collegalo al problema appena nominato.
I 4 GARANTI sono SEMPRE presenti: codice sorgente TUO, €0 canoni mensili, setup in 7 giorni, sui TUOI server.
"Questo workflow lo fa girare al 100%: [cosa fa]. Te lo installo sui tuoi server in 7 giorni, il codice è tuo, zero canoni mensili. Non noleggi un tool: possiedi un motore."

[O] OBIEZIONE = SOLO FIDUCIA + DEMO LIVE — 2 righe (1 paragrafo)
Il prodotto è chiaro: l'unica obiezione vera è la fiducia ("funziona davvero per me?").
Sciogli con la prova, non con le promesse: "Non ti chiedo di crederci sulla parola: te lo mostro dal vivo mentre gira, in 20 minuti."
MAI promesse garantite, MAI percentuali inventate, MAI urgenza falsa.

[C] CTA — PRESENTAZIONE + CALL — 2-3 righe (1 paragrafo) + RIGA AGENCY + FIRMA
UNA sola CTA logica: guarda la presentazione, e se ha senso, prenotiamo una call breve (demo live).
DEVI inserire il link presentazione: {PRESENTATION_URL}
DEVI citare lo sconto lancio: {LAUNCH_OFFER}
Esempio CTA: "Ti lascio la presentazione qui: {PRESENTATION_URL} — se ti parla, prenota una call ({LAUNCH_OFFER})."
Poi, su una riga separata, metti SOLO il link agency: {AGENCY_URL}
Ultima riga, la firma esatta: Max | Digital Empire

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMATO E LUNGHEZZA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LUNGHEZZA CORPO: 160-260 parole. MAI meno di 140.
PARAGRAFI: 2-3 righe ciascuno, separati da riga vuota. MAI muri di testo.
TRATTINI: VIETATI come separatore nel corpo. Sostituiscili con punto, due punti o virgola.
TONO: da founder a founder / collega a collega. Entusiasta sull'automazione ma concreto. Non venditore.
NUMERI CONCRETI sull'operatività: 300 email/giorno, 8-12 ore/settimana, 7 giorni di setup, €0 canoni.
CHIUSURA OBBLIGATORIA del corpo, in quest'ordine:
  riga CTA con {PRESENTATION_URL} e lo sconto lancio
  riga con {AGENCY_URL}
  riga firma: Max | Digital Empire

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VIETATO ASSOLUTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{frasi_vietate_str}
- Trattini "-" o "—" come separatori nel testo del corpo: MAI
- Superlativi vuoti: eccellente, straordinario, rivoluzionario, innovativo, all'avanguardia
- "la nostra agenzia", "i nostri servizi", "offriamo", "siamo specializzati" — parla in prima persona singolare
- "Vogliamo aiutarvi", "possiamo aiutarvi", "siamo qui per", "saremo felici"
- "Noi possiamo", "Noi abbiamo" — mai iniziare frase con "Noi"
- Promesse garantite, percentuali inventate, urgenza falsa
- Parlare di CONVERSIONI o di risultati di marketing del lettore (offende il marketer)
- Più di una CTA "forte" (il link agency in firma NON conta come CTA)
- Annotazioni di training come "Perche' funziona:", "Segnale reale:", "ESEMPIO:" nell'email finale
NOTA: "AI", "automazione", "workflow", "scalare", "operatività" sono ora APPROVATI e attesi.

OUTPUT — SOLO JSON valido, nient'altro:
{{
  "oggetto": "<hype operativo del prodotto-gancio — max 9 parole>",
  "oggetto_b": "<angolo alternativo — max 9 parole>",
  "oggetto_c": "<terzo angolo completamente diverso — max 9 parole>",
  "corpo": "<email APSOC del pivot, 160-260 parole — finisce con CTA + riga {AGENCY_URL} + riga: Max | Digital Empire>"
}}"""


WRITER_SYSTEM_PROMPT = _build_writer_system_prompt()


class EmailWriterAgent:
    """
    Team 4 — Copy: scrive email APSOC-powered con NVIDIA Nemotron.
    Utilizza il copy_briefing_pack + strategy_brief per ogni email.
    Gestisce revisioni su feedback del Humanizer.
    """

    # Sostituzioni deterministiche applicate DOPO la generazione del modello.
    # Non importa cosa produce il modello — l'output è sempre pulito.
    _SOSTITUZIONI = [
        # Agency "noi" → "io" (ordine: più lungo prima per evitare match parziali)
        ("Vogliamo aiutarvi a", "Posso mostrarti come"),
        ("Vogliamo aiutarti a", "Posso mostrarti come"),
        ("vogliamo aiutarvi a", "posso mostrarti come"),
        ("vogliamo aiutarti a", "posso mostrarti come"),
        ("Vogliamo aiutarvi", "Posso aiutarti"),
        ("Vogliamo aiutarti", "Posso aiutarti"),
        ("vogliamo aiutarvi", "posso aiutarti"),
        ("vogliamo aiutarti", "posso aiutarti"),
        ("Possiamo aiutarvi", "Posso aiutarti"),
        ("Possiamo aiutarti", "Posso aiutarti"),
        ("possiamo aiutarvi", "posso aiutarti"),
        ("possiamo aiutarti", "posso aiutarti"),
        ("Voglio aiutarvi", "Posso mostrarti come"),
        ("Voglio aiutarti", "Posso mostrarti come"),
        ("voglio aiutarvi", "posso mostrarti come"),
        ("voglio aiutarti", "posso mostrarti come"),
        ("Abbiamo sviluppato", "Ho sviluppato"),
        ("abbiamo sviluppato", "ho sviluppato"),
        ("Abbiamo aiutato", "Ho aiutato"),
        ("abbiamo aiutato", "ho aiutato"),
        ("Abbiamo creato", "Ho creato"),
        ("abbiamo creato", "ho creato"),
        ("Abbiamo lavorato", "Ho lavorato"),
        ("abbiamo lavorato", "ho lavorato"),
        ("Offriamo soluzioni", "Offro una soluzione"),
        ("offriamo soluzioni", "offro una soluzione"),
        ("Il nostro team", "Io"),
        ("il nostro team", "io"),
        ("La nostra agenzia", "Digital Empire"),
        ("la nostra agenzia", "Digital Empire"),
        ("La nostra consulenza", "La mia analisi"),
        ("la nostra consulenza", "la mia analisi"),
        ("Siamo specializzati", "Mi sono specializzato"),
        ("siamo specializzati", "mi sono specializzato"),
        ("Siamo qui per", "Sono qui per"),
        ("siamo qui per", "sono qui per"),
        ("Saremo felici", "Sarò felice"),
        ("saremo felici", "sarò felice"),
        ("Saremo lieti", "Sarò disponibile"),
        ("saremo lieti", "sarò disponibile"),
        ("Sono lieto di aiutarvi", "Posso mostrarti come"),
        ("sono lieto di aiutarvi", "posso mostrarti come"),
        ("Sono lieto di aiutarti", "Posso mostrarti come"),
        ("sono lieto di aiutarti", "posso mostrarti come"),
        ("Sono lieto", "Sono disponibile"),
        ("sono lieto", "sono disponibile"),
        # Superlativi vuoti residui (restano corretti — non cancellano AI/automazione)
        ("reputazione eccellente", "ottima reputazione"),
        ("Reputazione eccellente", "Ottima reputazione"),
        ("qualità eccellente", "buon livello di qualità"),
        ("Qualità eccellente", "Buon livello di qualità"),
        # "noi" in forma indiretta
        ("Siamo in grado di aiutarvi", "Sono in grado di aiutarti"),
        ("siamo in grado di aiutarvi", "sono in grado di aiutarti"),
        ("Siamo in grado di aiutarti", "Sono in grado di aiutarti"),
        ("siamo in grado di aiutarti", "sono in grado di aiutarti"),
        ("La nostra esperienza ha dimostrato", "La mia esperienza mostra"),
        ("la nostra esperienza ha dimostrato", "la mia esperienza mostra"),
        ("La nostra esperienza", "La mia esperienza"),
        ("la nostra esperienza", "la mia esperienza"),
        # Fix grammaticale frequente del modello
        ("Hai senso fare quella chiamata?", "Ha senso fare quella chiamata?"),
        ("hai senso fare quella chiamata?", "ha senso fare quella chiamata?"),
    ]

    def _sanitize_corpo(self, testo: str) -> str:
        """Applica sostituzioni deterministiche per eliminare frasi vietate dal corpo."""
        for vecchio, nuovo in self._SOSTITUZIONI:
            testo = testo.replace(vecchio, nuovo)
        # Rimuove backslash spuri che il modello a volte inserisce prima dei newline
        testo = testo.replace('\\\n', '\n').replace('\\n', '\n')
        # Rimuovi em-dash e en-dash usati come separatori di frase (mai nel corpo)
        testo = testo.replace(' — ', '. ').replace(' – ', '. ')
        # Rimuovi spazio-trattino-spazio usato come separatore (non tocca bullet "- item" a inizio riga)
        # Eccezione: non toccare gli URL (es. agency-empire-kohl) che contengono "-"
        testo = re.sub(r'(?<=[^\n]) - (?=[A-Za-zÀ-ÿ])(?![^\s]*\.(?:app|vercel|com|it))',
                       '. ', testo)
        # Normalizza eventuali doppi punti generati dalle sostituzioni
        testo = re.sub(r'\.\s*\.', '.', testo)
        return testo

    def _enforce_links(self, corpo: str) -> str:
        """
        Garantisce che il corpo finisca con:
          riga CTA contenente PRESENTATION_URL
          firma: Maximilian - Agency | Digital Empire
                 link sito web: https://agency-empire-landing.vercel.app
        Se PRESENTATION_URL manca, lo inietta nel CTA.
        Post-processing di sicurezza: il modello a volte dimentica i link richiesti.
        """
        if not corpo:
            return corpo
        testo = corpo.rstrip()

        ha_pres = PRESENTATION_URL in testo
        if ha_pres:
            # Se ha il link presentazione, solo assicurati che la firma sia presente
            if "Maximilian - Agency | Digital Empire" in testo and AGENCY_URL in testo:
                return testo  # già conforme

        # Rimuovi eventuali righe di firma/agency residue per ricostruire pulito
        firma_vecchia = "Max | Digital Empire"
        firma_nuova = "Maximilian - Agency | Digital Empire"
        righe = testo.split("\n")
        while righe and (
            righe[-1].strip() == ""
            or firma_vecchia in righe[-1]
            or firma_nuova in righe[-1]
            or "link sito web:" in righe[-1]
            or righe[-1].strip().rstrip("/") == AGENCY_URL.rstrip("/")
        ):
            righe.pop()
        corpo_base = "\n".join(righe).rstrip()

        # Blocco finale: CTA con presentazione + firma
        blocco = []
        if not ha_pres:
            blocco.append(
                f"Ho preparato questa presentazione: {PRESENTATION_URL} — "
                f"se ti parla, prenota una call ({LAUNCH_OFFER})."
            )
        blocco.append("")
        blocco.append(firma_nuova)
        blocco.append(f"link sito web: {AGENCY_URL}")

        return corpo_base + "\n\n" + "\n".join(blocco)

    def __init__(self, openrouter_api_key: str):
        self.rotation = build_rotation(openrouter_api_key)
        self._model_rl_until: dict[str, float] = {}  # model → timestamp disponibile

    def _formatta_briefing_pack(self, pack: dict) -> str:
        """Formatta il briefing pack in testo leggibile per il prompt."""
        if not pack:
            return "Nessun briefing disponibile."

        esempi = pack.get("esempi_approvati", [])
        esempi_str = ""
        for i, ex in enumerate(esempi[:2], 1):
            esempi_str += f"\nESEMPIO DI STILE {i} (settore: {ex.get('settore', '')}) — leggi per capire il tono, NON copiare:\n"
            esempi_str += f"Oggetto: {ex.get('oggetto', '')}\n"
            corpo_preview = ex.get("corpo", "")[:300]
            esempi_str += f"Corpo:\n{corpo_preview}...\n"
            # NOTA: "perche_funziona" rimosso — era copiato letteralmente nell'email dal LLM

        anti = pack.get("anti_esempio", {})
        anti_str = ""
        if anti:
            anti_str = f"\nANTI-ESEMPIO (cosa NON fare — tipo: {anti.get('tipo', '')}):\n"
            anti_str += f"{anti.get('email_sbagliata', '')[:200]}...\n"
            anti_str += f"Perché sbagliata: {anti.get('perche_sbagliata', '')}\n"

        regole = pack.get("regole_settore", [])
        regole_str = "\n".join(f"  • {r}" for r in regole[:5])

        stats = pack.get("statistiche", [])
        stats_str = "\n".join(f"  • {s}" for s in stats)

        apertura = pack.get("apertura_suggerita", {})
        apertura_str = ""
        if apertura:
            apertura_str = f"\nAPERTURA SUGGERITA (usa come base, puoi personalizzare):\n"
            apertura_str += f"Oggetto proposto: {apertura.get('oggetto', '')}\n"
            apertura_str += f"Prima riga proposta: {apertura.get('prima_riga', '')}\n"

        tono = pack.get("tono_settore", {})
        tono_str = ""
        if tono:
            tono_str = f"\nCALIBRAZIONE TONO SETTORE:\n"
            tono_str += f"  Pain point principale: {tono.get('pain_point_principale', '')}\n"
            tono_str += f"  Benefit chiave: {tono.get('benefit_chiave', '')}\n"
            tono_str += f"  Tono suggerito: {tono.get('tono_suggerito', '')}\n"

        return f"""
MATERIALE DI RIFERIMENTO:
{esempi_str}
{anti_str}
REGOLE SPECIFICHE PER QUESTO SETTORE:
{regole_str}

STATISTICHE DA USARE SE RILEVANTI:
{stats_str}
{apertura_str}
{tono_str}"""

    def _formatta_website_intel(self, intel: dict) -> str:
        """Formatta i dati reali del sito per il prompt del Writer.

        NB: nel nuovo posizionamento NON vendiamo CRO/landing page, quindi NON
        elenchiamo "problemi del sito". I dati del sito servono solo a capire
        ESATTAMENTE cosa fa il business e a confermare il prodotto-gancio giusto
        (Outreach Factory / Content Factory / Second Brain) e personalizzare l'hype [A].
        """
        if not intel or not intel.get("available"):
            return ""

        meta     = intel.get("meta", {})
        headings = intel.get("headings", {})
        ctas     = intel.get("ctas", [])
        sp       = intel.get("social_proof", {})

        h1_str  = " | ".join(headings.get("h1", []))[:120] or "nessuno"
        h2_str  = " | ".join(headings.get("h2", []))[:150] or "nessuno"
        cta_str = ", ".join(ctas[:4]) or "nessuna"
        sp_kw   = ", ".join(sp.get("keywords", [])[:4]) or "nessuna"

        return f"""
DATI REALI DAL SITO (usali SOLO per capire cosa fa il business e personalizzare l'apertura [A]):
  Titolo pagina: {meta.get('title', '')[:100]}
  Meta description: {meta.get('description', '')[:150] or 'assente'}
  H1: {h1_str}
  H2 principali: {h2_str}
  Cosa offre / temi del sito: {cta_str}
  Segnali (vendono corsi/servizi, pubblicano contenuti, hanno team): {sp_kw}
ISTRUZIONE: usa Titolo/H1/H2 per capire ESATTAMENTE cosa fa il business e confermare il prodotto-gancio corretto. NON elencare problemi del sito, NON parlare di conversioni/landing page. Mostra solo, nell'apertura [A], di aver capito cosa fanno."""

    def _formatta_strategy_brief(self, brief: dict, insight_brief: dict = None) -> str:
        """Formatta il strategy brief in testo leggibile. Inietta insight_brief se disponibile."""
        if not brief:
            return ""
        barnum = brief.get('barnum_opener', '')
        niche  = brief.get('niche_term', '')

        # Se abbiamo insight_brief con dati reali, sostituisce il Barnum generico
        insight_block = ""
        if insight_brief and insight_brief.get("available"):
            apertura = insight_brief.get("apertura_email", "")
            p1 = insight_brief.get("problema_principale", {})
            p2 = insight_brief.get("problema_2", {})
            p3 = insight_brief.get("problema_3", {})
            if apertura:
                insight_block = f"""
  ━━ DATI REALI DAL SITO (PRIORITÀ ASSOLUTA) ━━
  APERTURA [A] — usa questa INVECE del Barnum generico:
  "{apertura}"
  PROBLEMA 1 (con dato reale): {p1.get("testo", "")} [{p1.get("dato_reale", "")}]
  PROBLEMA 2 (con dato reale): {p2.get("testo", "")} [{p2.get("dato_reale", "")}]
  PROBLEMA 3 (con dato reale): {p3.get("testo", "")} [{p3.get("dato_reale", "")}]
  REGOLA: cita i dati reali nel paragrafo [P] PROBLEMA — "Ho visto che..." / "Sul tuo sito..."
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

        barnum_line = f"\n  OPENER BARNUM/RAINBOW — usa come prima riga ESATTA: {barnum}" if barnum and not insight_block else ""
        niche_line  = f"\n  TERMINE TECNICO nicchia — usa nel paragrafo PROBLEMA: {niche}" if niche else ""

        return f"""
STRATEGY BRIEF (segui queste indicazioni):{insight_block}{barnum_line}{niche_line}
  Hook angle: {brief.get('hook_angle', '')}
  Problema da amplificare: {brief.get('problema_da_amplificare', '')}
  Angolo soluzione: {brief.get('angolo_soluzione', '')}
  Nota tono: {brief.get('nota_tono', '')}"""

    def _sanitize_json(self, raw: str) -> str:
        """Escape all bare control characters inside JSON string values (Groq quirk)."""
        out = []
        in_str = False
        skip = False
        for ch in raw:
            if skip:
                out.append(ch)
                skip = False
            elif ch == '\\' and in_str:
                out.append(ch)
                skip = True
            elif ch == '"':
                in_str = not in_str
                out.append(ch)
            elif in_str and ord(ch) < 0x20:
                out.append(f'\\u{ord(ch):04x}')
            else:
                out.append(ch)
        return ''.join(out)

    _FIELD_RE = {
        k: re.compile(rf'"{k}"\s*:\s*"((?:[^"\\]|\\.)*)"', re.DOTALL)
        for k in ("oggetto", "oggetto_b", "oggetto_c", "corpo")
    }

    def _extract_fields_regex(self, testo: str) -> dict:
        """Fallback: estrae i campi direttamente via regex quando JSON è corrotto."""
        result = {}
        for key, pat in self._FIELD_RE.items():
            m = pat.search(testo)
            if m:
                val = m.group(1).replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"')
                result[key] = val
        return result

    def _scrivi_email(self, lead: dict, feedback_revisione: str = None) -> dict:
        """Scrive un'email per un singolo lead."""
        nome = lead.get("page_name", "Business")
        settore = lead.get("settore_calibrato", lead.get("settore", ""))
        citta = lead.get("citta", "")
        template = lead.get("template", "A")
        website = lead.get("website", "")
        email = lead.get("email", "")

        briefing_pack     = lead.get("copy_briefing_pack", {})
        strategy_brief    = lead.get("strategy_brief", {})
        website_intel     = lead.get("website_intelligence", {})

        briefing_str  = self._formatta_briefing_pack(briefing_pack)
        strategy_str  = self._formatta_strategy_brief(strategy_brief)
        intel_str     = self._formatta_website_intel(website_intel)

        template_context = {
            "A": "Outreach Factory (automazione outreach 100%)",
            "B": "Content Factory (produzione contenuti AI)",
            "C": "Second Brain (memoria/contesto permanente per l'AI)",
        }.get(template, "Outreach Factory (automazione outreach 100%)")

        revisione_str = ""
        if feedback_revisione:
            revisione_str = f"""
═══════════════════════════════════════
ATTENZIONE — STAI RISCRIVENDO UN'EMAIL RIFIUTATA
Il QA team ha trovato questi problemi (correggi tutti):
{feedback_revisione}
═══════════════════════════════════════
"""

        prompt = f"""{revisione_str}
Scrivi la cold email per questo lead:

Business: {nome}
Settore: {settore}
Città: {citta}
Template: {template} ({template_context})
Ha sito web: {"Sì — " + website if website else "No"}
Email destinatario: {email}
{intel_str}
{strategy_str}

{briefing_str}

ISTRUZIONI OBBLIGATORIE:
1. Segui la struttura APSOC del pivot: [A] hype automazione → [P] 1 solo problema operativo → [S] workflow al 100% (codice tuo, €0 canoni, 7 giorni, tuoi server) → [O] obiezione = solo fiducia + "te lo mostro in demo live" → [C] CTA con presentazione + call
2. Aggancia con il PRODOTTO-GANCIO del template ({template_context}) — non mischiare i 3 prodotti
3. UN SOLO problema operativo, mai una lista di dolori. Parla di OPERATIVITÀ e ORE liberate, MAI di conversioni
4. Paragrafi brevi (2-3 righe), riga vuota tra ogni sezione — MAI muri di testo — usa \\n\\n tra paragrafi
5. TARGET: 160-260 parole nel corpo (il limite di 130 nel briefing è IGNORATO)
6. USA SOLO "io/ho/mi" — MAI "noi/vogliamo/abbiamo/offriamo". "Digital Empire" solo in firma/CTA
7. CHIUSURA OBBLIGATORIA del corpo, in quest'ordine esatto:
   - riga CTA con il link presentazione {PRESENTATION_URL} e lo sconto lancio ({LAUNCH_OFFER})
   - riga separata con SOLO il link agency: {AGENCY_URL}
   - ultima riga, firma esatta: Max | Digital Empire
8. OGGETTO: hype operativo del prodotto-gancio (max 9 parole), NON copiare gli esempi alla lettera:
   A → "Ho automatizzato l'outreach al 100% — gira da solo ogni mattina"
   B → "I contenuti di una settimana in un pomeriggio"
   C → "La tua AI dimentica tutto: ho risolto con un Second Brain"
   STRUTTURE SBAGLIATE: oggetti generici di 3 parole, "Soluzioni AI per il tuo business", promesse vuote

Restituisci SOLO il JSON con oggetto e corpo."""

        for _cycle in range(4):  # max 4 cicli interi prima di arrendersi
            _tried_any = False

            for attempt, (client, model) in enumerate(self.rotation):
                # Salta modelli ancora in cooldown rate-limit
                _now = time.time()
                _rl_until = self._model_rl_until.get(model, 0)
                if _rl_until > _now:
                    continue  # cooldown attivo, skip silenzioso

                _tried_any = True
                provider = "Groq" if "groq" in str(client.base_url) else "OR"
                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": WRITER_SYSTEM_PROMPT},
                            {"role": "user", "content": prompt},
                        ],
                        max_tokens=1100,
                        temperature=0.65,
                    )
                    msg = response.choices[0].message
                    content = msg.content
                    # Reasoning models (DeepSeek, Nemotron) mettono l'output in reasoning invece di content
                    if not content:
                        content = getattr(msg, "reasoning", None) or getattr(msg, "reasoning_content", None)
                    if not content:
                        print(f"[WRITER] Risposta vuota (None) dal modello, tentativo {attempt+1}")
                        continue
                    testo = content.strip()
                    start = testo.find("{")
                    if start < 0:
                        print(f"[WRITER] {provider} no JSON (attempt {attempt+1}): {testo[:120]!r}")
                        continue
                    try:
                        risultato, _ = json.JSONDecoder().raw_decode(
                            self._sanitize_json(testo[start:])
                        )
                    except json.JSONDecodeError:
                        risultato = self._extract_fields_regex(testo)
                        if not risultato.get("oggetto") or not risultato.get("corpo"):
                            print(f"[WRITER] {provider} JSON irrecuperabile (attempt {attempt+1}): {testo[start:start+80]!r}")
                            continue
                    oggetto = risultato.get("oggetto", "")
                    corpo = risultato.get("corpo", "")
                    if corpo:
                        corpo = self._sanitize_corpo(corpo)
                        # Forza link presentazione + agency + firma in chiusura (post-processing di sicurezza)
                        corpo = self._enforce_links(corpo)
                    parole = len(corpo.split()) if corpo else 0
                    if oggetto and corpo and parole >= 130:
                        return {
                            **lead,
                            "oggetto": oggetto,
                            "oggetto_b": risultato.get("oggetto_b", ""),
                            "oggetto_c": risultato.get("oggetto_c", ""),
                            "corpo": corpo,
                        }
                    print(f"[WRITER] {provider} email troppo corta: oggetto={bool(oggetto)}, parole={parole} (min 130)")

                except (openai.RateLimitError, openai.APIStatusError) as e:
                    if isinstance(e, openai.APIStatusError):
                        sc = getattr(e, "status_code", 0)
                        if sc == 413:
                            continue
                        if sc == 402:
                            self._model_rl_until[model] = time.time() + 300  # spend limit: 5 min
                            print(f"[WRITER] Spend limit {provider}/{model.split('/')[-1][:20]} — cooldown 5min")
                            continue
                        if sc == 400:
                            print(f"[WRITER] Errore API fatale (400) per '{nome}': {e}")
                            break
                        if sc not in (429, 500, 502, 503, 504):
                            print(f"[WRITER] Errore API {sc} {provider}/{model.split('/')[-1][:20]} — passo al prossimo")
                            continue
                    # Rate limit 429: cooldown differenziato — Groq TPM esaurisce in fretta
                    _cd = 120 if "groq" in str(client.base_url) else 60
                    self._model_rl_until[model] = time.time() + _cd
                    print(f"[WRITER] Rate limit {provider}/{model.split('/')[-1][:20]} — cooldown {_cd}s")
                    continue

                except Exception as e:
                    print(f"[WRITER] {provider}/{model.split('/')[-1][:20]} attempt {attempt+1}: {type(e).__name__}: {str(e)[:200]}")
                    if attempt < len(self.rotation) - 1:
                        time.sleep(1)

            if not _tried_any:
                # Tutti i modelli in cooldown — aspetta il primo a liberarsi
                _earliest = min(
                    (self._model_rl_until.get(m, 0) for _, m in self.rotation),
                    default=0,
                )
                _wait = max(1.0, _earliest - time.time())
                print(f"[WRITER] Tutti i modelli in cooldown — attendo {_wait:.0f}s...")
                time.sleep(_wait)

        return None

    def revise(self, lead_con_feedback: dict) -> dict:
        """
        Riscrive un'email rifiutata dal QA incorporando il feedback.

        Returns:
            Lead con email riscritta, o None se anche la revisione fallisce.
        """
        feedback = lead_con_feedback.get("qa_feedback", "")
        nome = lead_con_feedback.get("page_name", "?")
        print(f"[WRITER] Revisione per '{nome[:40]}' — Feedback: {feedback[:80]}...")

        return self._scrivi_email(lead_con_feedback, feedback_revisione=feedback)

    def run(self, leads: list) -> list:
        """
        Scrive email personalizzate per tutti i lead.
        Salva checkpoint JSONL dopo ogni email — riprende automaticamente se interrotto.

        Returns:
            Lista di lead con 'oggetto', 'oggetto_b', 'oggetto_c', 'corpo' aggiunti.
        """
        # ── Carica checkpoint (resume da interruzione) ─────────────────────────
        # Matching per EMAIL (chiave univoca) — non page_name che può differire
        email_lead_correnti = {l.get("email", "").strip().lower() for l in leads}
        emails_pronte = []
        email_completate = set()
        if _CHECKPOINT_FILE.exists():
            with open(_CHECKPOINT_FILE, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        saved = json.loads(line)
                        email_saved = saved.get("email", "").strip().lower()
                        if email_saved and email_saved in email_lead_correnti:
                            emails_pronte.append(saved)
                            email_completate.add(email_saved)
                    except json.JSONDecodeError:
                        pass
            if emails_pronte:
                print(f"\n[WRITER] Checkpoint trovato: {len(emails_pronte)} email già scritte — riprendo da dove ero...")
            elif _CHECKPOINT_FILE.exists():
                _CHECKPOINT_FILE.unlink()

        leads_da_fare = [l for l in leads if l.get("email", "").strip().lower() not in email_completate]
        errori = 0
        totale = len(leads)
        offset = len(emails_pronte)

        print(f"\n[WRITER] Scrivo {len(leads_da_fare)} email (di {totale} totali)...")

        for i, lead in enumerate(leads_da_fare, offset + 1):
            nome    = lead.get("page_name", "?")
            settore = lead.get("settore", "")
            citta   = lead.get("citta", "")
            email_generando(i, totale, nome, settore, citta)

            risultato = self._scrivi_email(lead)

            if risultato:
                emails_pronte.append(risultato)
                # Salva checkpoint immediatamente
                with open(_CHECKPOINT_FILE, "a", encoding="utf-8") as f:
                    f.write(json.dumps(risultato, ensure_ascii=False) + "\n")
            else:
                errori += 1
                email_scartata(nome, "errore generazione")

            time.sleep(0.5)

        # Rimuovi checkpoint a completamento avvenuto
        if _CHECKPOINT_FILE.exists():
            _CHECKPOINT_FILE.unlink()

        print(f"[WRITER] Email scritte: {len(emails_pronte)}/{totale} ({errori} errori)")
        return emails_pronte
