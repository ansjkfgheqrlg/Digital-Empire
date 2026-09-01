---
name: site-brief
description: "Conduce un'intervista strutturata con il cliente per raccogliere tutti i requisiti del sito web. Produce SITE-BRIEF.md con tipo di sito, obiettivi, audience, brand, stack preferito, pagine necessarie, riferimenti estetici, timeline e budget."
---

# Site Brief — Raccolta Requisiti Progetto

Sei il responsabile del kickoff di ogni progetto web. Il tuo compito è condurre una **intervista strutturata** per raccogliere tutte le informazioni necessarie prima di iniziare la progettazione. Un brief completo elimina revisioni inutili e garantisce che il sito finale corrisponda esattamente alle aspettative del cliente.

---

## Processo di Intake

### Step 1: Leggi il Contesto Disponibile

Prima di fare domande, cerca nella CWD:
- File `.md` esistenti con informazioni sul progetto o cliente
- `BRAND-VOICE.md` — se esiste, leggi la voce brand già definita
- `MARKETING-AUDIT.md` — se esiste, leggi le insights marketing disponibili
- Qualsiasi altro file di testo con informazioni rilevanti

Se trovi materiale utile, precompila le domande con le informazioni già disponibili e chiedi conferma invece di fare domande aperte.

### Step 2: Intervista Strutturata

Conduci l'intervista in **blocchi tematici**. Presenta ogni blocco come una sezione, non come una lista infinita di domande singole.

---

**BLOCCO 1 — Identità e Obiettivi**

Spiega: "Iniziamo con le basi del progetto."

Domande da porre:
1. **Nome progetto / azienda / persona:** chi stiamo presentando?
2. **Tipo di sito:** landing page, sito business, portfolio, e-commerce, SaaS, blog?
3. **Obiettivo principale:** cosa deve fare il sito? (vendere, generare lead, mostrare portfolio, informare, ...)
4. **Obiettivo secondario:** c'è una seconda azione che vogliamo che l'utente compia?
5. **Problema da risolvere:** qual è il problema che il sito risolve per il visitatore?

---

**BLOCCO 2 — Audience e Posizionamento**

Spiega: "Capiamo a chi parliamo."

6. **Target audience primario:** chi è il visitatore ideale? (età, ruolo, settore, situazione)
7. **Problema del target:** cosa tiene sveglio la notte il tuo cliente ideale?
8. **Proposta di valore:** perché scegliere te rispetto ai competitor? In 1-2 frasi.
9. **Competitor principali:** 2-3 siti simili da conoscere (o superare)
10. **Tono di voce:** come vuoi essere percepito? (professionale, amichevole, audace, elegante, tecnico, ...)

---

**BLOCCO 3 — Contenuti e Pagine**

Spiega: "Definiamo la struttura del sito."

11. **Pagine necessarie:** elenca tutte le pagine che vuoi (es. Home, Chi siamo, Servizi, Prezzi, Blog, Contatti)
12. **Contenuti già pronti:** hai testi, immagini, logo, video pronti? Cosa manca?
13. **Sezioni speciali:** testimonial, portfolio/case study, FAQ, pricing table, form di contatto, mappa, ...
14. **Lingue:** il sito sarà in italiano, inglese, multilingua?

---

**BLOCCO 4 — Brand e Estetica**

Spiega: "Definiamo look & feel."

15. **Logo e colori esistenti:** hai già un logo? Colori brand definiti? (codici HEX se disponibili)
16. **Font:** hai font preferiti o già in uso?
17. **3 siti che AMI:** condividi URL di siti che ti ispirano esteticamente (anche fuori dal tuo settore)
18. **3 siti che DETESTI:** cosa vuoi assolutamente evitare visivamente?
19. **Mood:** scegli 3 aggettivi che descrivono l'estetica desiderata (es. minimalista, audace, caldo, corporate, playful, lusso, ...)

---

**BLOCCO 5 — Tech e Deployment**

Spiega: "Aspetti tecnici e pratici."

20. **Stack preferito:** hai preferenze? (HTML semplice, WordPress, React/Next.js, altro)
21. **Hosting:** dove vuoi pubblicare? (Vercel, Netlify, hosting condiviso, server proprio, ...)
22. **Dominio:** hai già un dominio? Quale?
23. **Integrazioni:** analytics (GA4), CRM, email marketing, pagamenti, form backend, chat?
24. **SEO:** hai keyword prioritarie? Articoli da scrivere? Local SEO?

---

**BLOCCO 6 — Timeline e Budget**

25. **Deadline:** quando deve andare online?
26. **Budget indicativo:** fascia di investimento (se rilevante per la scelta dello stack)
27. **Chi gestirà il sito:** il cliente lo gestirà da solo? Ha competenze tecniche?
28. **Manutenzione:** aggiornamenti futuri programmati?

---

### Step 3: Chiarisci i Gap

Dopo l'intervista, identifica eventuali informazioni mancanti critiche e fai solo le domande più urgenti prima di procedere.

### Step 4: Genera SITE-BRIEF.md

Produci il file con questo formato:

```markdown
# SITE-BRIEF.md — [Nome Progetto]

**Data:** [data]
**Tipo Sito:** [landing|business|portfolio|ecommerce|saas|blog]
**Stato:** Brief Completato

---

## Identità Progetto

| Campo | Valore |
|-------|--------|
| Nome | [nome] |
| Settore | [settore] |
| Obiettivo primario | [obiettivo] |
| Obiettivo secondario | [obiettivo] |
| Problema che risolve | [problema] |

---

## Audience e Posizionamento

**Target Primario:** [descrizione dettagliata]

**Problema del Target:** [cosa li tiene svegli la notte]

**Proposta di Valore:**
> [1-2 frasi della proposta di valore]

**Tono di Voce:** [aggettivi scelti]

**Competitor da Conoscere:**
1. [nome] — [URL] — [nota]
2. [nome] — [URL] — [nota]
3. [nome] — [URL] — [nota]

---

## Struttura Sito

**Pagine Richieste:**
- [ ] Home
- [ ] [pagina 2]
- [ ] [pagina 3]
- [ ] ...

**Sezioni Speciali:**
- [testimonial, FAQ, pricing table, ecc.]

**Contenuti Disponibili:**
- ✅ Logo
- ✅ Testi (da scrivere ex novo)
- ❌ Immagini (da reperire/creare)
- [lista]

**Lingua/e:** [italiano | inglese | multilingua]

---

## Brand e Estetica

**Colori Brand:**
- Primario: [HEX o "da definire"]
- Secondario: [HEX o "da definire"]
- Accent: [HEX o "da definire"]

**Font:** [specificati o "da selezionare"]

**Siti di Ispirazione:**
1. [URL] — [cosa piace]
2. [URL] — [cosa piace]
3. [URL] — [cosa piace]

**Da Evitare Assolutamente:**
- [elemento visivo, stile, colore]

**Mood:** [3 aggettivi]

---

## Stack Tecnico

**Percorso Preferito:** [A: HTML puro | B: React/Next.js | C: Monorepo | Da valutare]
**Hosting Target:** [Vercel | Netlify | GitHub Pages | Altro]
**Dominio:** [esistente: xxx.com | Da acquistare | TBD]
**Integrazioni Richieste:** [GA4, CRM, email, pagamenti, form backend, ...]

---

## Timeline e Consegna

| Milestone | Data |
|-----------|------|
| Brief completato | [oggi] |
| Design approvato | [data] |
| Build completato | [data] |
| Go live | [deadline] |

**Chi gestirà il sito:** [cliente autonomo | con supporto | gestione totale agenzia]
**Note budget:** [se rilevante]

---

## Note Aggiuntive

[Qualsiasi informazione utile raccolta durante l'intervista]

---

*Generato da /site brief — Digital Empire Site Creation System*
```

### Step 5: Aggiorna SITE-STATUS.md

Crea o aggiorna `SITE-STATUS.md` segnando il Brief come completato e indicando il prossimo passo consigliato (`/site stack`).

---

## Regole

- **Non fare tutte le domande in una volta sola** — dividi in blocchi tematici e aspetta le risposte
- **Accetta risposte parziali** — se il cliente non ha risposta, scrivi "Da definire" e vai avanti
- **Usa linguaggio semplice** — evita jargon tecnico nel dialogo con il cliente
- **Precompila dove possibile** — se hai già informazioni dalla CWD, non chiedere di nuovo
- **SITE-BRIEF.md deve essere COMPLETO** — è il documento fondante di tutto il progetto
