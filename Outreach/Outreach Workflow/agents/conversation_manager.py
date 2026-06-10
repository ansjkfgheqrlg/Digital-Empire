"""
Conversation Manager Agent — Digital Empire Outreach (PIVOT: implementazioni AI)
================================================================================
Quando un lead risponde, analizza la risposta e genera il messaggio giusto per
continuare la conversazione verso una CALL / DEMO LIVE del workflow, con la
presentazione come materiale di supporto.

Digital Empire vende 3 implementazioni AI (workflow sui server del cliente, codice
incluso, €0 canoni, setup 7 giorni, automazione 100%):
  - Outreach Factory  → automatizza l'outreach al 100%
  - Content Factory   → genera copy, grafiche, caroselli e script video
  - Second Brain      → memoria/contesto permanente per l'LLM (Context Engineering)

Classifica la risposta in 4 tipologie:
  POSITIVO     → propone slot per call/demo live del workflow
  OBIEZIONE    → (l'unica vera obiezione è la fiducia) riframe con demo live + presentazione + sconto
  NON_INTERESS → uscita rispettosa, porta aperta, link presentazione
  DOMANDA      → risponde alla domanda, poi guida verso call/demo

Stesse regole di qualità della prima email:
  - Prima persona singolare (Max | Digital Empire, non agenzia)
  - Zero trattini nel corpo
  - Paragrafi separati
  - Link presentazione nel CTA + link agency in firma (ammessi dalla policy pivot)
  - Max 100 parole (la brevità mantiene il ritmo della conversazione)
"""

import json
import time
import openai
from agents.ai_client import build_rotation

try:
    from knowledge.apsoc import PRESENTATION_URL, AGENCY_URL, LAUNCH_OFFER
except Exception:  # pragma: no cover — fallback se il modulo non è importabile
    PRESENTATION_URL = "https://presentazione-empire.vercel.app/"
    AGENCY_URL = "https://agency-empire-landing.vercel.app"
    LAUNCH_OFFER = "sconto early-adopter per i primi clienti che partono questo mese"

# Alias storico mantenuto per compatibilità a valle (firma)
CTA_LINK = AGENCY_URL

# ── PROMPT CLASSIFICAZIONE ────────────────────────────────────────────────────

_CLASSIFICAZIONE_PROMPT = """Analizza questa risposta a una cold email di Digital Empire,
che vende implementazioni AI (workflow installati sui server del cliente: Outreach Factory,
Content Factory, Second Brain — codice incluso, €0 canoni, setup 7 giorni, automazione 100%).

RISPOSTA DEL LEAD:
{reply_text}

CONTESTO (email originale inviata):
{email_originale_abstract}

Classifica la risposta in UNA di queste categorie:
- POSITIVO: interessato, vuole saperne di più, chiede info, aperto alla call/demo
- OBIEZIONE: resistenze (di solito è fiducia: "funziona davvero?", "non vi conosco"; o prezzo, tempo, "ci penso")
- NON_INTERESSATO: no chiaro, non interessa, rimuovimi dalla lista
- DOMANDA: chiede dettagli tecnici, come funziona il workflow, su quali server gira, chi sei

Se OBIEZIONE: identifica l'obiezione principale (max 5 parole).
Se DOMANDA: identifica la domanda principale (max 10 parole).

Rispondi SOLO JSON:
{{"categoria": "POSITIVO|OBIEZIONE|NON_INTERESSATO|DOMANDA",
  "obiezione": "<se OBIEZIONE, max 5 parole>",
  "domanda": "<se DOMANDA, max 10 parole>",
  "tono_lead": "aperto|neutro|freddo|ostile",
  "nota": "<1 frase su come approcciarsi>"}}"""


# ── SYSTEM PROMPT RISPOSTE ────────────────────────────────────────────────────

_RISPOSTA_SYSTEM = f"""Sei Max, founder di Digital Empire (firma "Max | Digital Empire").
Stai rispondendo a chi ha risposto alla tua cold email. La conversazione è già avviata:
il tuo obiettivo è portarla verso una CALL / DEMO LIVE in cui mostri il workflow girare dal vivo.
La presentazione ({PRESENTATION_URL}) è il materiale di supporto.

Vendi implementazioni AI: workflow installati sui server del cliente (codice incluso,
€0 canoni mensili, setup in 7 giorni, automazione 100%): Outreach Factory, Content Factory,
Second Brain. NON parli mai di "landing page", "conversioni" o servizi a ore.

REGOLE ASSOLUTE (identiche alla prima email):
1. PRIMA PERSONA SINGOLARE: solo "io", "ho", "mi", "mio". MAI "noi", "offriamo", "vogliamo".
2. ZERO TRATTINI nel corpo. Punti fermi e virgole, mai trattini come separatori.
3. PARAGRAFI SEPARATI con riga vuota.
4. MAX 100 PAROLE. La brevità mantiene il ritmo.
5. RISPONDI DIRETTAMENTE ALLA PERSONA: usa il loro nome se disponibile.
6. ZERO formule di cortesia: niente "Grazie per la risposta", "Perfetto", "Ottimo".
   Inizia direttamente col contenuto.
7. Link presentazione nel corpo quando ha senso: {PRESENTATION_URL}
8. Firma sempre: Max | Digital Empire, con riga {AGENCY_URL}

OBIETTIVO: una call / demo live in cui mostro il workflow girare dal vivo (20 minuti).
L'unica obiezione vera è la fiducia: la sciolgo facendoglielo VEDERE, non promettendo.

OUTPUT (JSON valido, nient'altro):
{{"oggetto": "Re: <oggetto originale>", "corpo": "<testo con \\n\\n tra paragrafi>"}}"""


_RISPOSTA_POSITIVO = f"""TIPO: POSITIVO — il lead è interessato o aperto.
TONO: diretto, concreto, muoviti subito verso la call/demo live senza over-sellare.

STRUTTURA (max 80 parole):
1. Riconosci brevemente (1 frase, non "grazie mille")
2. Proponi la demo live con 2-3 opzioni di orario concrete (es: "Martedì alle 10, Giovedì alle 15, o Venerdì alle 11 — ti va uno di questi?")
3. Rassicura: "20 minuti, ti mostro il workflow girare dal vivo sul tuo caso, poi decidi tu"
4. Link presentazione su riga separata: {PRESENTATION_URL}
5. Firma: Max | Digital Empire + riga {AGENCY_URL}

CONTESTO:
Lead: {{nome}} — {{settore}} — {{citta}}
Loro risposta: {{reply_text}}
Email originale oggetto: {{oggetto_orig}}"""


_RISPOSTA_OBIEZIONE = f"""TIPO: OBIEZIONE — il lead ha una resistenza.
NB: l'unica vera obiezione del prodotto è la FIDUCIA ("funziona davvero per me?", "non vi conosco").
Il prodotto è chiaro al 1000%, quindi riframe SEMPRE verso la prova: demo live + presentazione di qualità estrema.
TONO: comprensivo ma diretto. Non difenderti, non promettere risultati. Mostra.

OBIEZIONE RILEVATA: {{obiezione}}

COME GESTIRE PER TIPO:
- "non vi conosco / funziona davvero?": "Giustissimo non fidarti sulla parola. Per questo te lo mostro dal vivo mentre gira, sul tuo caso. Vedi e decidi."
- "non ho tempo": "Capito. Bastano 20 minuti: ti mostro il workflow girare dal vivo, poi scegli tu se ha senso."
- "costa troppo": "Capito. Considera che il codice è tuo, gira sui tuoi server e non paghi canoni mensili: lo possiedi. C'è anche uno {LAUNCH_OFFER}."
- "ci penso": "Certo. Per darti qualcosa di concreto su cui riflettere ti lascio la presentazione qui sotto. Vale comunque una demo di 20 minuti?"
- altre obiezioni: riportale alla prova (demo live) e alla presentazione.

STRUTTURA (max 90 parole):
1. Riconosci l'obiezione (1 frase, non difenderti)
2. Riframe verso la prova: demo live + presentazione (1-2 frasi concrete)
3. Riproponi la demo in modo leggero
4. Link presentazione su riga separata: {PRESENTATION_URL}
5. Firma: Max | Digital Empire + riga {AGENCY_URL}

CONTESTO:
Lead: {{nome}} — {{settore}}
Loro risposta: {{reply_text}}
Oggetto originale: {{oggetto_orig}}"""


_RISPOSTA_DOMANDA = f"""TIPO: DOMANDA — il lead vuole capire meglio prima di decidere.
TONO: esperto, diretto, non commerciale. Rispondi alla domanda, poi guida verso la demo live.

DOMANDA PRINCIPALE: {{domanda}}

STRUTTURA (max 100 parole):
1. Rispondi alla domanda con 1-2 frasi concrete (es. su quali server gira, che il codice è loro, €0 canoni, 7 giorni)
2. Aggiungi 1 dettaglio operativo rilevante per il loro caso
3. "Te lo mostro girare dal vivo in una demo di 20 minuti — ti va?"
4. Link presentazione su riga separata: {PRESENTATION_URL}
5. Firma: Max | Digital Empire + riga {AGENCY_URL}

NON dare tutto nella email: il workflow si capisce davvero vedendolo girare.
NON rispondere con un muro di testo: la brevità crea curiosità.

CONTESTO:
Lead: {{nome}} — {{settore}}
Loro domanda: {{reply_text}}
Oggetto originale: {{oggetto_orig}}"""


_RISPOSTA_NON_INTERESSATO = f"""TIPO: NON_INTERESSATO — rispetto la loro risposta, uscita dignitosa.
TONO: rispettoso, professionale, zero risentimento.

STRUTTURA (max 40 parole):
1. "Capito, nessun problema — rispetto la tua risposta."
2. 1 frase di porta aperta: "Se mai l'automazione di quel processo tornasse utile, sai dove trovarmi."
3. Link presentazione su riga separata (per quando vorrà): {PRESENTATION_URL}
4. "Buon lavoro." + Firma: Max | Digital Empire + riga {AGENCY_URL}

ASSOLUTAMENTE NIENTE:
- Tentativi di convincere
- "Mi dispiace"
- Follow-up impliciti

CONTESTO:
Lead: {{nome}} — {{settore}}
Risposta ricevuta: {{reply_text}}
Oggetto originale: {{oggetto_orig}}"""


class ConversationManagerAgent:
    """
    Analizza le risposte ai lead e genera il messaggio di continuazione
    per portare la conversazione verso una call / demo live del workflow.
    """

    def __init__(self, openrouter_api_key: str):
        self.rotation = build_rotation(openrouter_api_key)

    def _call_ai(self, system: str, user: str, max_tokens: int = 400) -> str | None:
        for attempt, (client, model) in enumerate(self.rotation):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    max_tokens=max_tokens,
                    temperature=0.4,
                )
                return response.choices[0].message.content.strip()
            except (openai.RateLimitError, openai.APIStatusError) as e:
                if isinstance(e, openai.APIStatusError) and getattr(e, "status_code", 0) != 429:
                    break
                time.sleep(min(15 * (attempt + 1), 60))
            except Exception:
                if attempt < len(self.rotation) - 1:
                    time.sleep(3)
        return None

    def _parse_json(self, testo: str) -> dict | None:
        if not testo:
            return None
        start = testo.find("{")
        end = testo.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                return json.loads(testo[start:end])
            except Exception:
                return None
        return None

    def _classifica_risposta(self, reply_text: str, corpo_originale: str) -> dict:
        """Classifica l'intenzione della risposta del lead."""
        abstract = corpo_originale[:200] if corpo_originale else "email di outreach su implementazioni AI"
        prompt = _CLASSIFICAZIONE_PROMPT.format(
            reply_text=reply_text[:500],
            email_originale_abstract=abstract,
        )
        testo = self._call_ai(
            "Sei un analista di cold email italiane (pivot implementazioni AI). Rispondi SOLO JSON.",
            prompt, max_tokens=200
        )
        result = self._parse_json(testo)
        if result:
            return result
        # Fallback: assumi POSITIVO se non riesce a classificare
        return {"categoria": "POSITIVO", "obiezione": "", "domanda": "", "tono_lead": "neutro", "nota": ""}

    def _genera_risposta(self, lead: dict, classificazione: dict) -> dict | None:
        """Genera la risposta appropriata in base alla classificazione."""
        nome      = lead.get("page_name", "").split()[0] if lead.get("page_name") else ""
        settore   = lead.get("settore_calibrato", lead.get("settore", ""))
        citta     = lead.get("citta", "")
        reply     = lead.get("reply_text", "")
        obj_orig  = lead.get("oggetto_originale", lead.get("oggetto", ""))
        categoria = classificazione.get("categoria", "POSITIVO")

        if categoria == "POSITIVO":
            prompt = _RISPOSTA_POSITIVO.format(
                nome=nome, settore=settore, citta=citta,
                reply_text=reply[:300], oggetto_orig=obj_orig,
            )
        elif categoria == "OBIEZIONE":
            prompt = _RISPOSTA_OBIEZIONE.format(
                obiezione=classificazione.get("obiezione", ""),
                nome=nome, settore=settore,
                reply_text=reply[:300], oggetto_orig=obj_orig,
            )
        elif categoria == "DOMANDA":
            prompt = _RISPOSTA_DOMANDA.format(
                domanda=classificazione.get("domanda", ""),
                nome=nome, settore=settore,
                reply_text=reply[:300], oggetto_orig=obj_orig,
            )
        else:  # NON_INTERESSATO
            prompt = _RISPOSTA_NON_INTERESSATO.format(
                nome=nome, settore=settore,
                reply_text=reply[:300], oggetto_orig=obj_orig,
            )

        testo = self._call_ai(_RISPOSTA_SYSTEM, prompt, max_tokens=400)
        result = self._parse_json(testo)

        if result:
            corpo = result.get("corpo", "")
            if corpo and PRESENTATION_URL.rstrip("/") not in corpo:
                corpo = corpo.rstrip() + f"\n\n{PRESENTATION_URL}"
                result["corpo"] = corpo
            return result

        # Fallback
        return self._fallback_risposta(nome, settore, categoria, obj_orig)

    def _fallback_risposta(self, nome: str, settore: str, categoria: str, obj_orig: str) -> dict:
        oggetto = f"Re: {obj_orig}" if obj_orig else "Re: la mia proposta"
        firma = f"Max | Digital Empire\n{AGENCY_URL}"
        if categoria == "NON_INTERESSATO":
            corpo = (
                f"Capito, nessun problema.\n\n"
                f"Se mai l'automazione di quel processo tornasse utile, sai dove trovarmi.\n\n"
                f"{PRESENTATION_URL}\n\n"
                f"Buon lavoro.\n\n{firma}"
            )
        elif categoria == "OBIEZIONE":
            corpo = (
                f"Capito, giusto non fidarsi sulla parola.\n\n"
                f"Proprio per questo te lo mostro dal vivo: in 20 minuti vedi il workflow girare sul tuo caso, poi decidi tu. "
                f"Il codice resta tuo, gira sui tuoi server, zero canoni. C'è anche uno {LAUNCH_OFFER}.\n\n"
                f"{PRESENTATION_URL}\n\n"
                f"Ti va una demo?\n\n{firma}"
            )
        else:
            corpo = (
                f"Ho disponibilità martedì alle 10, giovedì alle 15 o venerdì alle 11.\n\n"
                f"20 minuti, ti mostro il workflow girare dal vivo sul tuo caso, poi decidi tu.\n\n"
                f"{PRESENTATION_URL}\n\n{firma}"
            )
        return {"oggetto": oggetto, "corpo": corpo}

    def run(self, lead_con_risposta: dict) -> dict | None:
        """
        Analizza una risposta e genera il messaggio di continuazione.

        Args:
            lead_con_risposta: dict con reply_text, email, page_name, settore, ecc.

        Returns:
            dict con {email, oggetto, corpo, categoria_risposta, page_name, ...}
            oppure None se manca reply/email.
        """
        reply   = lead_con_risposta.get("reply_text", "")
        email   = lead_con_risposta.get("email", "")
        nome    = lead_con_risposta.get("page_name", email)

        if not reply or not email:
            return None

        print(f"[CONV-MANAGER] Analizzo risposta da {email[:40]}...")
        classificazione = self._classifica_risposta(reply, lead_con_risposta.get("corpo_originale", ""))
        categoria = classificazione.get("categoria", "POSITIVO")
        print(f"[CONV-MANAGER] Categoria: {categoria} (tono: {classificazione.get('tono_lead','?')})")

        risposta = self._genera_risposta(lead_con_risposta, classificazione)
        if not risposta:
            return None

        return {
            **lead_con_risposta,
            "oggetto":           risposta.get("oggetto", ""),
            "corpo":             risposta.get("corpo", ""),
            "categoria_risposta": categoria,
        }

    def run_batch(self, leads_con_risposta: list) -> list:
        """
        Processa una lista di risposte.

        Returns:
            Lista di dict pronti per l'invio (stessa struttura dell'EmailSenderAgent).
        """
        print(f"\n[CONV-MANAGER] Processo {len(leads_con_risposta)} risposte ricevute...")
        risposte_generate = []

        for lead in leads_con_risposta:
            risultato = self.run(lead)
            if risultato:
                risposte_generate.append(risultato)
            time.sleep(2)

        print(f"[CONV-MANAGER] Risposte generate: {len(risposte_generate)}/{len(leads_con_risposta)}")
        return risposte_generate
