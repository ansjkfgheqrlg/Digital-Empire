# Libro 01 — "The AI Career Pivot" — Ricerca, Qualificazione, Piano

**Data:** 2026-08-03
**Perché questo file esiste:** il blueprint a 95 agenti (`architettura_completa_7_livelli/`)
valida solo la *struttura* del progetto (agenti/team/regole), non scrive libri — verificato
con esecuzione reale (vedi CP-20260803-006). Max ha chiesto di produrre un libro vero.
Questo documento è la traccia delle fasi Ricerca → Qualificazione → Pianificazione fatte
a mano (da Claude), seguendo la stessa logica del blueprint ma senza i 95 agenti simulati.

## 1. Ricerca (fase Research)

**Metodo REALE usato, dichiarato**: `WebSearch` (ricerca web), NON Playwright su Amazon —
questa sessione non ha un tool Playwright collegato ad Amazon. È un proxy di segnale di
domanda, non lo stesso meccanismo del blueprint (CP-PERF-01 richiede segnali Amazon +
review site). Limite dichiarato esplicitamente, non nascosto.

**Query eseguite:**
1. "best low competition KDP non-fiction niches 2026 self-publishing profitable"
2. "AI job search" OR "using AI to find a job" book guide 2026 career change

**Evidenza trovata:**
- Categorie non-fiction ad alta domanda 2026: AI & Automation guides, personal finance,
  self-help/mental health, **career transition guides**, health/fitness per audience
  specifiche (fonte: automateed.com, bookfoundry.ai, kdpbuilder.com, inkfluenceai.com,
  kdpeasy.com — blog di settore KDP, non dati di vendita verificati Amazon diretti).
- Strategia raccomandata dalla stessa fonte: "niche stacking" — combinare categoria
  ampia + pubblico specifico + beneficio chiaro, per ridurre competizione diretta.
- Verifica su "AI job search 2026": decine di guide/blog reali già pubblicati
  (jobcopy.ai, aiapply.co, flashfirejobs.com, vanessaraath.com, zemith.com) — prova che
  la domanda è reale e attiva, ma anche che il taglio generico "AI job search" è già
  affollato di contenuto (blog, non necessariamente libri KDP — non verificato).

## 2. Qualificazione (5 gate, come da blueprint)

| Gate | Esito | Motivazione |
|---|---|---|
| Performante? | ✅ GO (con riserva) | Domanda reale confermata via web search; competizione KDP diretta NON verificata (nessun accesso Amazon) |
| Riproducibile? | ✅ GO | Formato guida pratica, nessuna dipendenza esterna per scriverlo |
| Sostenibile? | ✅ GO | Scritto in una sessione, nessuna infrastruttura ricorrente richiesta |
| Non assurdo? | ✅ GO | Consigli di carriera generali — nessun consiglio medico/legale/finanziario specifico (rischio reale evitato) |
| Non troppo lento? | ✅ GO | Nessuna attesa di API esterne, scrittura diretta |

**Decisione: GO.**

## 3. Niche-stacking scelto

Non "AI job search" generico (affollato) ma **"cambio carriera con l'AI"** — pubblico
specifico (chi cambia carriera, non solo chi cerca lavoro), argomento caldo (AI), rischio
basso.

## 4. Decisione di lingua (dichiarata, non assunta in silenzio)

**Inglese**, non italiano. Motivo: bacino di acquirenti KDP in inglese enormemente più
grande dell'italiano; l'obiettivo dichiarato del blueprint è "guadagnare attraverso
quantità di libri performanti" — la lingua segue l'obiettivo di revenue, non la lingua
del team. Se Max preferisce l'italiano, si rifà (costo basso: cambia solo la scrittura,
non ricerca/struttura).

## 5. Piano (struttura capitoli)

**Titolo:** *The AI Career Pivot: A Practical Guide to Changing Careers with ChatGPT,
Claude, and AI Tools*

1. The New Career Landscape: How AI Is Reshaping Jobs and Opportunities
2. Before You Pivot: Self-Assessment with AI as Your Thinking Partner
3. Mapping Transferable Skills: Using AI to See What You Don't See
4. Researching New Fields and Roles Without Wasting Months
5. Building a Bridge: Micro-Credentials, Projects, and Portfolio-Building with AI
6. Rewriting Your Story: Resume and LinkedIn with AI (Without Sounding Like a Robot)
7. The AI-Assisted Job Search Engine: Finding and Tracking the Right Roles
8. Networking and Outreach: Using AI to Write, Not Replace, Human Connection
9. Interview Preparation: Practicing with AI Without Overfitting to It
10. Negotiating and Landing: Offer Evaluation and the First 90 Days

Più: Introduzione, Conclusione, Appendice (tool list + prompt template curati).

Target: ~25.000 parole totali (~2.000-2.500 per capitolo) — lunghezza tipica di una guida
KDP short non-fiction di categoria.

## RIPRESA DA
Fase successiva: Produzione (scrittura capitoli reali, non placeholder) → Editing →
Copertina → Assemblaggio finale.
