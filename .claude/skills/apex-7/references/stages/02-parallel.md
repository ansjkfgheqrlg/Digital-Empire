# Stage 2: Parallel Analysis + Draft

## Obiettivo
Produrre analisi di contesto (ANALYST) e draft iniziale (WRITER) in parallelo.

## Agenti Responsabili
- **ANALYST** (AG-03) — Context Package
- **WRITER** (AG-04) — Draft creation

## Modalità
**PARALLELO** — I due agenti lavorano simultaneamente

## Input
- Subtask assignment da PLANNER
- Working Memory (contesto sessione)
- Decision Log (se rilevante)

## Processo ANALYST

### A1 — Context Mapping
- Identificare dominio, entità chiave, relazioni

### A2 — Memory Deep Dive
- 3 query: CONTEXTUAL RECALL, STRATEGY FETCH, DECISION LOOKUP
- Sintesi in Memory Brief

### A3 — Pattern Detection
- Pattern ricorrenti, anomalie, trend

### A4 — Insight Generation
- CONFERMA, SORPRESA, RISCHIO, OPPORTUNITÀ

### A5 — Context Package
- Impacchettare tutto per WRITER

## Processo WRITER

### W1 — Pre-Writing Analysis
- Leggere subtask e Context Package
- Determinare formato ottimale
- Identificare success criteria

### W2 — Structure Design
- Disegnare struttura prima di scrivere
- Auto-approvare struttura

### W3 — Draft Creation
- Scrivere seguendo la struttura
- No placeholder, no "ecc.", no omissioni
- Ogni affermazione supportata

### W4 — Self-Review
- Rileggere come CRITIC
- Notare dubbi onestamente

### W5 — Output Preparation
- Metadata: versione, subtask ID, context usato
- Self-review notes

## Output

### ANALYST produce:
- Context Package completo
- Memory Brief
- Pattern identificati
- Insight (4 categorie)

### WRITER produce:
- Draft completo (nessuna omissione)
- Self-review notes
- Confidence score

## Post-Actions
1. ANALYST: Memory.WRITE in Working Memory, emetti `analysis.completed`
2. WRITER: Memory.WRITE in Working Memory, emetti `draft.created`
3. Context Package consegnato a WRITER

## Criteri di Completamento
- [x] ANALYST ha completato tutte le 3 query di memoria
- [x] ANALYST ha prodotto almeno 2 insight
- [x] WRITER ha completato struttura prima di scrivere
- [x] WRITER ha eseguito self-review onesta
- [x] Draft non contiene placeholder o omissioni
- [x] Confidence scores assegnati

## Next Stage
→ Stage 3: Critique Loop
