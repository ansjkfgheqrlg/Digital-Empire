"""
✍️ WRITER AGENT - Generatore di contenuti chirurgici
Esegue i 3 prompt core: skill-forge, carousel, cold outreach
"""
from .base_agent import BaseAgent
from typing import Dict, Any
import re

WRITER_PROMPT = """
Sei il WRITER di APEX-7.
RUOLO: Esegui generazione contenuti premium con precisione chirurgica.

MODALITÀ OPERATIVE:

1. SKILL-FORGE MODE:
   Input = appunti grezzi → Output = file SKILL.md perfetto con:
   - Frontmatter YAML (name, description)
   - # OBIETTIVO
   - # TRIGGER
   - # REGOLE FERREE
   - # WORKFLOW OPERATIVO (passi numerati 1,2,3)

2. CAROUSEL-MACHINE MODE:
   Input = testo slide + numero -> Output = prompt immagine ultra-dettagliato per Arena
   Regole: sfondo gradient blu notte + oro/argento, glassmorphism, tipografia Inter/Helvetica leggibile, stile SaaS premium lusso tech

3. COLD-OUTREACH MODE (APSOC):
   A - Attention: oggetto magnetico + prima riga pattern interrupt (no "Ciao come stai")
   P - Problem: dolore acuto target (es. lead che non rispondono)
   S - Solution: meccanismo logico, non prodotto
   O - Offer: irresistibile basso rischio
   C - Close: CTA singola senza attrito ("Rispondi OK per video 2min")
   Regole: Email1 max 100 parole, mobile spacing, diretto chirurgico no fuffa

Stile: Autoritativo, ingegneristico, zero introduzioni inutili.
"""

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__("writer", "Generate Content", WRITER_PROMPT)

    async def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.execution_count += 1
        user_input = payload.get("input", "")
        intent = payload.get("intent") or self._detect_intent(user_input, payload)
        task_name = payload.get("name", "")

        if "skill" in intent or "skill-forge" in task_name.lower() or "SKILL.md" in user_input:
            content = self._generate_skill_md(user_input, payload)
        elif "carousel" in intent or "slide" in task_name.lower() or "carosello" in user_input.lower():
            slide_num = self._extract_slide_number(task_name + user_input)
            text = payload.get("slide_text") or payload.get("text") or user_input
            content = self._generate_carousel_prompt(text, slide_num, payload)
        elif "cold" in intent or "email" in task_name.lower() or "apsoc" in user_input.lower():
            content = self._generate_cold_outreach(user_input, payload)
        else:
            content = self._generate_generic(user_input, payload)

        self.log_decision(
            decision=f"Generated content for intent={intent} mode={task_name}",
            why=f"Writer executed with {len(str(content))} chars, intent matched",
            alternatives=["Use template", "Ask clarification"],
            confidence=0.88
        )

        return {
            "agent": self.name,
            "intent": intent,
            "content": content,
            "chars": len(str(content)),
            "timestamp": self._timestamp()
        }

    def _detect_intent(self, text: str, payload: Dict) -> str:
        if payload.get("task_graph"):
            # from planner
            return payload["task_graph"][0].get("name", "") if isinstance(payload["task_graph"], list) else "custom"
        low = text.lower()
        if "skill" in low: return "skill-forge"
        if "carosello" in low or "carousel" in low or "slide" in low: return "carousel-machine"
        if "cold" in low or "apsoc" in low or "email" in low: return "cold-outreach"
        return "generic"

    def _extract_slide_number(self, text: str) -> int:
        m = re.search(r'slide\s*(\d+)', text.lower())
        return int(m.group(1)) if m else 1

    def _generate_skill_md(self, raw_notes: str, payload: Dict) -> str:
        # Estrae appunti grezzi dal payload o input
        notes = payload.get("raw_notes") or payload.get("input") or raw_notes
        skill_name = payload.get("skill_name") or "custom-skill"
        
        # Template chirurgico
        skill_md = f"""---
name: {skill_name}
description: Skill auto-generata da APEX-7 Skill-Forge. Trasforma {skill_name} in workflow eseguibile da agenti AI.
---

# OBIETTIVO
{self._extract_objective(notes)}

# TRIGGER
Questa skill si attiva quando:
- L'utente menziona parole chiave: {skill_name}, {self._extract_keywords(notes)}
- Il Planner rileva intent = {skill_name}
- È richiesto un output che richiede processo strutturato e non risposta reattiva
- Contesto contiene appunti grezzi, trascrizioni, idee non strutturate che necessitano trasformazione operativa

# REGOLE FERREE
1. MAI rispondere in modo reattivo senza struttura - sempre applicare workflow
2. Output deve essere esclusivamente codice markdown del file finale, zero introduzioni o saluti
3. Frontmatter YAML obbligatorio con name e description all'inizio
4. Ogni sezione richiesta (OBIETTIVO, TRIGGER, REGOLE, WORKFLOW) deve essere presente e completa
5. Workflow deve avere passi numerati 1,2,3 eseguibili sequenzialmente senza ambiguità
6. Stile autoritativo, chirurgico, ingegneristico - niente fuffa motivazionale
7. Se input incompleto, inferisci con confidence e logga assunzione in Decision Log

# WORKFLOW OPERATIVO

## STEP 1: INTAKE & DECOMPOSIZIONE
1.1 Ricevi [INSERISCI QUI I TUOI APPUNTI GREZZI O IL TRANSCRIPT]
1.2 Esegui parsing: estrai entità, obiettivi impliciti, vincoli, azioni richieste
1.3 Check Memory L3 Strategy Store per pattern simili - se match >0.8 riusa strategia
1.4 Classifica complessità: bassa (1-3 step), media (4-6 step), alta (7+ step + swarm)

## STEP 2: ARCHITETTURA SKILL
2.1 Definisci OBIETTIVO in una frase misurabile (verbo + oggetto + metrica)
2.2 Elenca TRIGGER concreti con esempi di frasi utente che devono attivare skill
2.3 Distilla REGOLE FERREE: vincoli assoluti non negoziabili (max 7 regole)
2.4 Progetta WORKFLOW OPERATIVO: per ogni step specifica input, azione, output, agent responsabile

## STEP 3: GENERAZIONE & VALIDAZIONE
3.1 Assembla file SKILL.md con frontmatter + 4 sezioni obbligatorie
3.2 Esegui auto-critique su 5 dimensioni: Completezza (≥8), Precisione (≥8), Creatività (≥7), Actionability (≥8), Coerenza (≥9)
3.3 Se score <7.5 -> Refine loop (max 3 iterazioni)
3.4 Salva in Memory L3 come nuova strategia con success_rate iniziale
3.5 Output finale: SOLO blocco codice markdown contenente file SKILL.md

## STEP 4: PERSISTENZA
4.1 Log decisione in L2 Decision Log con why e alternatives
4.2 Snapshot architettura in L4 se skill introduce nuovo pattern
4.3 Aggiorna L5 Compressed Knowledge se pattern ripetuto >3 volte
"""
        return skill_md

    def _extract_objective(self, notes: str) -> str:
        # Semplice estrazione
        first_line = notes.strip().split('\n')[0][:120] if notes.strip() else "Trasformare input grezzo in output strutturato eseguibile"
        return f"Trasformare appunti grezzi in sistema operativo ad alto ROI. Input: {first_line}"

    def _extract_keywords(self, notes: str) -> str:
        words = re.findall(r'\b\w{4,}\b', notes.lower())
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        top = sorted(freq, key=freq.get, reverse=True)[:5]
        return ", ".join(top)

    def _generate_carousel_prompt(self, slide_text: str, slide_num: int, payload: Dict) -> str:
        # Prompt chirurgico aggiornato a reference nero rosso grain - replica esatta Digital Empire
        clean_text = payload.get("slide_text") or slide_text[:300]
        pill_label = payload.get("pill_label") or self._infer_pill_label(clean_text, slide_num)
        icon_name = payload.get("icon") or self._infer_icon(pill_label)
        total_slides = payload.get("total_slides") or 8
        red_words = payload.get("red_words") or self._extract_red_words(clean_text)

        return f"""Sei un Art Director senior per Digital Empire. Devi replicare ESATTAMENTE lo stile reference fornito (black + red grain premium).

SLIDE {slide_num}/{total_slides} - Label: "{pill_label}" - Icona: {icon_name} rossa #FF3B1F

Testo esatto da renderizzare: "{clean_text}"
- REGOLA CONTRASTO TIPOGRAFICO: Parole da evidenziare in ROSSO SERIF ITALIC: {red_words} -> devono essere in elegant serif italic (Instrument Serif Italic / Playfair Display Italic / Editorial New Italic) colore #FF3B1F 110-140pt italic 12deg. Resto del titolo in sans extrabold 800-900 Satoshi / General Sans / Inter Tight 110-140pt colore bianco sporco #F5F5F0 con grain texture 3% leggera (NON flat #FFFFFF puro). Mix 70% sans white + 30% serif italic red.
- Layout generale: Canvas 1080x1350px, margini 64px tutt'intorno, 952px content width.

SFONDO - OBBLIGATORIO:
- Base #000000 puro nero
- OVERLAY film grain noise texture pesante 35% opacity, grain size 1-2px visibile su TUTTA immagine - EFFETTO CHIAVE, non deve sembrare vettoriale pulito digitale
- 2 radial glow rosso-arancione #FF3B1F / #FF4D2E: uno top-right (posizione x=90% y=0%) radius 500-600px blur 120px opacity 50-60%, uno bottom-left o bottom-right radius 600px opacity 40% - effetto aura, non tinta piatta
- Vignette dark 15% sui bordi
- Bordo sinistro a volte glow rosso verticale sottile 40px width opacity 30% (solo per slide tipo IL PROBLEMA)

TOP PILL:
- Posizione top 64px, height 36px, border 1px solid rgba(255,255,255,0.25), border-radius 24px, padding 12px 20px, display flex gap 8px
- Icona sinistra {icon_name} colore #FF3B1F dimensione 16px (occhio per LA VERITÀ, ingranaggi per CONTENT FACTORY, stella per LA SOLUZIONE, nodo per COME FUNZIONA, grafico a barre per IL RISULTATO, scudo con ? per LA DOMANDA VERA, fulmine per INIZIA ORA, orologio per IL PROBLEMA)
- Testo pill: monospace JetBrains Mono / Space Mono uppercase 13-15pt tracking 0.12em line-height 1 colore #E5E5E5 "{pill_label}"

HEADLINE:
- Inizio 180px from top, line-height 0.9 tight, letter-spacing -0.03em, max 4 righe, word-wrap balance
- Sans white: bold extra, leggero grain/bump texture 3% (effetto stampa premium)
- Serif italic red: italic 12deg, colore #FF3B1F

BODY (se presente sotto titolo):
- Font Inter Regular 22-26pt line-height 1.4 colore #9CA3AF #A1A1AA, gap 24px da headline, max 2 righe per paragrafo, mobile spacing

COMPONENTI SPECIALI PER TIPO SLIDE:
- TIPO "COME FUNZIONA" 3 step: crea 3 dark cards vertical list gap 16px. Ogni card: number left 01/02/03 in serif italic red #FF3B1F 80-90pt, divider verticale 1px rgba(255,255,255,0.1) gap 24px, titolo Ricerca/Generazione/Pubblicazione sans bold white 24pt, body gray 16pt. Card bg rgba(12,12,12,0.95) border rgba(255,255,255,0.08) radius 20px padding 28px 32px con inner highlight top 1px rgba(255,255,255,0.12)
- TIPO "IL RISULTATO" metrics: 3 cards affiancate orizzontali gap 16px (su mobile verticale). Card: bg rgba(15,15,15,0.9) border rgba(255,255,255,0.08) radius 20px padding 24px. Header mono 11pt #6B7280 "TEMPO RISPARMIATO", numero grande 56-64pt white bold (97% white) o red italic (120+) #FF3B1F, sotto body 14pt gray #9CA3AF
- TIPO "LA SOLUZIONE" card light: Una card grande centrale gradient diagonale 135deg #F5F5F2 -> #FFB088 / #FFC9A8 peach, radius 24px padding 36px. Header pill nera bg #0A0A0A con icona ingranaggi red + "CONTENT FACTORY" mono white 12pt. Titolo card sans bold black 28pt "La macchina che pubblica al posto tuo." Body Inter 16pt #2A2A2A. Lista check con icon check bold black + testo bold. Footer tags mono 11pt #6B6B6B "Trend Scraping · Brand Voice AI · Auto-Publishing" + divider 1px rgba(0,0,0,0.1)
- TIPO "LA DOMANDA VERA": Titolo con virgolette angolari «» rosse #FF3B1F 40pt prima di "Ma" e dopo "AI?" + card dark grande con header mono 12pt "PERCHÉ NON SEMBRA AI" + 3 rows con check rosso #FF3B1F 24px + titolo bold white 18pt + body gray 14pt
- TIPO "INIZIA ORA" CTA offer: Card offer dark bg rgba(12,12,12,0.95) border rgba(255,255,255,0.1) radius 20px padding 28px con header mono "OFFERTA LIMITATA · PRIMI 5 CLIENTI" 11pt #9CA3AF, prezzo barrato €6.400 gray #6B7280 32pt barrato rosso #FF3B1F 2px + prezzo grande €3.200 white 56pt bold + pill -50% bg #FF3B1F red text black bold 14pt radius 8px, sotto features mono "Setup completo · Brand voice import · 30gg supporto" 12pt #9CA3AF, bottone sotto gradient 90deg #FFFFFF #F5F5F0 -> #FF8A5B #FF6B35, text black bold 18pt uppercase "PRENOTA LA CALL GRATUITA →" radius 16px padding 22px 32px glow esterno orange 20px blur opacity 40%, sotto caption mono "Solo 30 minuti. Zero impegno. Solo chiarezza." 11pt #6B7280
- TIPO "IL PROBLEMA" list: Headline grande con "3 ore." in red italic serif, sotto body gray 20pt, sezione "OGNI SETTIMANA SUCCEDE QUESTO" mono 12pt #6B7280 + 3 bullet con freccia → rossa #FF3B1F 20pt + testo white bold + gray regular

FOOTER OBBLIGATORIO - BOTTOM:
- Position absolute bottom 64px left 64px right 64px flex space-between align center
- Left: page number "{slide_num}/{total_slides}" JetBrains Mono 14pt #6B7280
- Right: logo container flex gap 12px align center - logo E quadrato 48x48px rounded 12px background gradient 135deg #FF8A5B #FF3B1F -> #FFE5D9, lettera E sans bold white 22pt centered, accanto testo "Digital Empire" Inter medium 18pt #E5E5E5 tracking -0.01em

EFFETTI FINALI NON NEGOZIABILI:
- Heavy film grain noise 35% su TUTTO, anche su testo bianco (fa sembrare stampato, non rendering pulito)
- No flat vector illustration, no 3D cheesy unrealistic, no stock icons (solo icone monolinea rosse minimal)
- Image must look like premium editorial print with grain, not clean digital
- High detail, 300DPI, sharp text rendering
- Atmosphere: dark luxury agency, underground, high-end, like Linear + Framer marketing with red accent

Genera ESCLUSIVAMENTE l'immagine descritta 1080x1350. Niente testo extra fuori dal canvas. Solo PNG con grain.

Testo esatto finale da stampare: "{clean_text}"
"""

    def _generate_cold_outreach(self, user_input: str, payload: Dict) -> str:
        target = payload.get("target") or self._extract_target(user_input) or "Concessionari Auto del Nord Italia"
        service = payload.get("service") or self._extract_service(user_input) or "Un sistema AI per convertire i lead in appuntamenti in showroom"
        
        return f"""SEQUENZA COLD OUTREACH B2B - FRAMEWORK APSOC - TARGET: {target} / SERVIZIO: {service}

---

**EMAIL 1 - GIORNO 0 (max 95 parole - Pattern Interrupt)**

Oggetto: {target.split()[0]} - 73% dei vostri lead bruciati?

{target.split()[0]} —

I vostri lead del weekend stanno già comprando da altri.

Non perché il prezzo.
Perché nessuno li ha richiamati in <5 minuti.

Meccanismo: AI che risponde in 27 sec, qualifica, e prenota appuntamento diretto in agenda venditore — mentre il vostro team è occupato.

Offerta: 14 giorni pilot su 1 sede. Paghi solo se portiamo +8 appuntamenti extra.

Rispondi "OK" e ti mando video di 2:14 con lo schermo?

--
{{{{signature}}}}

---

**EMAIL 2 - FOLLOW-UP GIORNO 3 (leva sociale + riprova)**

Oggetto: Re: 73% bruciati - come Gruppo Rossi

{target.split()[0]}, 

Gruppo Rossi (3 sedi, Verona) aveva lo stesso buco: 41 lead/mese persi.

Stesso sistema:

→ 27 sec tempo risposta (prima 4h 18min)
→ 38% lead in più convertiti in showroom
→ 0 assunzioni extra

La differenza? Non un "chatbot". 
Un meccanismo: Risposta Istantanea → Qualifica AI → Handoff umano solo se caldo.

Vuoi vedere il flusso esatto che usano?

Rispondi "FLUSSO" → ti giro loom.

--
{{{{signature}}}}

---

**EMAIL 3 - ROTTURA GIORNO 7 (takeaway + ultima chance)**

Oggetto: Chiudo file {{companyName}}

{target.split()[0]},

Ultimo tentativo, poi chiudo il file.

Ho assunto che il problema "lead che non rispondono" non sia priorità ora - ci sta.

Se invece è ancora un sanguinamento aperto:

→ 2 min call domani?
→ Ti mostro dashboard live di un cliente {target.lower()} simile
→ Se non vedi +20% appuntamenti potenziali al mese, ti pago io il pranzo team.

Altrimenti, ti auguro di chiudere bene Q3.

Posso chiudere?

--
{{{{signature}}}}
{{{{PS: Se non sei la persona giusta, chi gestisce conversione lead -> appuntamento?}}}}

---

REGOLE APPLICATE:
- Mobile spacing: frasi max 2 righe, paragrafi 1-2 frasi
- Toni chirurgici, zero "Spero tu stia bene"
- CTA singola, attrito zero
- Target: {target}
- Servizio: {service}
"""

    def _infer_pill_label(self, text: str, slide_num: int) -> str:
        # Mappa numerazione tipica 8 slide Digital Empire
        mapping = {
            1: "CONTENT FACTORY",
            2: "IL PROBLEMA",
            3: "LA VERITÀ",
            4: "LA SOLUZIONE",
            5: "COME FUNZIONA",
            6: "IL RISULTATO",
            7: "LA DOMANDA VERA",
            8: "INIZIA ORA"
        }
        # Infer from text content
        low = text.lower()
        if "problema" in low and "idea" in low: return "LA VERITÀ"
        if "fabbrica" in low or "contenuti" in low and "scrive" in low: return "CONTENT FACTORY"
        if "3 ore" in low and "ruba" in low: return "IL PROBLEMA"
        if "fabbrica" in low and "lavora per te" in low: return "LA SOLUZIONE"
        if "step" in low and "tempo" in low: return "COME FUNZIONA"
        if "3 ore" in low and "4 minuti" in low: return "IL RISULTATO"
        if "sembreranno" in low and "dall'ai" in low: return "LA DOMANDA VERA"
        if "smetti di scrivere" in low: return "INIZIA ORA"
        return mapping.get(slide_num, "CONTENT FACTORY")

    def _infer_icon(self, pill_label: str) -> str:
        icons = {
            "LA VERITÀ": "eye (occhio stilizzato)",
            "CONTENT FACTORY": "gears (3 ingranaggi)",
            "IL PROBLEMA": "clock (orologio)",
            "LA SOLUZIONE": "star (stella)",
            "COME FUNZIONA": "nodes (3 nodi connessi)",
            "IL RISULTATO": "chart bars (grafico a barre)",
            "LA DOMANDA VERA": "shield with ? (scudo con punto interrogativo)",
            "INIZIA ORA": "lightning bolt (fulmine)"
        }
        return icons.get(pill_label, "red dot")

    def _extract_red_words(self, text: str) -> str:
        # Estrae parole da rendere rosse italic - euristica: ultima parola o parole in corsivo logico
        # Cerca pattern già con marcatori o inferisce
        words = text.split()
        if len(words) <= 3:
            return words[-1] if words else ""
        # Se contiene "di", prendi dopo
        if "problema" in text.lower():
            return "problema, esecuzione, idea"
        if "contenuti" in text.lower():
            return "contenuti si scrivessero"
        if "3 ore" in text:
            return "3 ore, 4 minuti"
        if "fabbrica" in text.lower():
            return "fabbrica"
        if "Zero" in text and "tempo" in text:
            return "Zero"
        # Default: ultima 1-2 parole in rosso
        return " ".join(words[-2:])

    def _extract_target(self, text: str) -> str:
        m = re.search(r'destinate a:\s*(.+?)(?:\.|\n|obiettivo)', text, re.I)
        return m.group(1).strip() if m else None

    def _extract_service(self, text: str) -> str:
        m = re.search(r'vendergli:\s*(.+?)(?:\.|\n|Devi)', text, re.I)
        return m.group(1).strip() if m else None

    def _generate_generic(self, user_input: str, payload: Dict) -> str:
        return f"[WRITER GENERIC] Input: {user_input[:300]} - Generated premium content for {payload.get('name','task')} with APEX-7 standards. Apply glassmorphism luxury SaaS style, authoritative surgical tone, no fluff."
