# CLAUDE
            
> Path: [[Map - General|general]]

## Content

# CLAUDE.md — Digital Empire Knowledge Engine

## REGOLA FONDAMENTALE: WIKI-FIRST

**Questa directory è il quartier generale di Digital Empire.**

Ad ogni conversazione in questa directory, Claude DEVE:

### 1. ALL'INIZIO DI OGNI SESSIONE — carica il contesto
Leggi SEMPRE questi file prima di rispondere a qualsiasi domanda:
- `second-brain-vault/wiki/index.md` — panoramica completa di tutta la conoscenza
- `second-brain-vault/wiki/log.md` — operazioni recenti, cosa è cambiato

Se la domanda riguarda un dominio specifico, leggi anche le pagine rilevanti:
- Marketing/Agenti → `second-brain-vault/wiki/tools/Tool_Market_*.md`
- Corsi/Info Products → `second-brain-vault/wiki/entities/` e `second-brain-vault/wiki/projects/Formazione/`
- Processi/Operazioni → `second-brain-vault/wiki/concepts/Digital_Empire_*.md`
- Progetti cliente → `second-brain-vault/wiki/projects/Clienti/`

### 2. DURANTE LA CONVERSAZIONE — riconosci nuova conoscenza
Se l'utente menziona qualcosa di NUOVO o CAMBIATO:
- Un nuovo progetto → crea pagina in `second-brain-vault/wiki/projects/`
- Un nuovo cliente → crea pagina in `second-brain-vault/wiki/projects/Clienti/`
- Un nuovo concetto/framework → crea pagina in `second-brain-vault/wiki/concepts/`
- Un nuovo tool/agente → crea pagina in `second-brain-vault/wiki/tools/`
- Una fonte/risorsa esterna → crea pagina in `second-brain-vault/wiki/sources/`
- Un'analisi/confronto → crea pagina in `second-brain-vault/wiki/synthesis/`

**Non chiedere il permesso. Fallo autonomamente.**

### 3. DOPO OGNI AGGIORNAMENTO — loga l'operazione
Dopo aver creato o modificato pagine wiki, aggiungi entry in `second-brain-vault/wiki/log.md`:
```
## [Data]
- INGEST: [cosa è stato aggiunto] → [n] pagine create/aggiornate
```

---

## Segnali che indicano "aggiorna la wiki"

Reagisci automaticamente a frasi come:
- "sto lavorando su..."
- "ho un nuovo cliente..."
- "abbiamo deciso di..."
- "il nuovo progetto si chiama..."
- "ho imparato che..."
- "dobbiamo cambiare..."
- "lancio il corso..."
- "ho trovato questo articolo..."
- Qualsiasi numero, metrica, risultato concreto

---

## Struttura Wiki

```
second-brain-vault/wiki/
├── concepts/     → Framework, metodologie, principi
├── entities/     → Prodotti, persone, aziende
├── projects/     → Progetti attivi (Clienti/, Formazione/, Publishing/, Agency/)
├── tools/        → Agenti AI, tool, sistemi
├── sources/      → Risorse esterne, articoli, video
├── synthesis/    → Confronti, analisi cross-domain
├── index.md      → Catalogo master (aggiorna sempre)
└── log.md        → Registro operazioni (aggiorna sempre)
```

---

## Template rapido per nuova pagina

```markdown
---
Type: PROJECT / CONCEPT / TOOL / SOURCE / SYNTHESIS / ENTITY
Status: Active / Archive / Experimental / Shipped
Tags: #[tag1] #[tag2] #[tag3]
Created: YYYY-MM-DD
Last updated: YYYY-MM-DD
---

# [Titolo Pagina]

## Overview
[Descrizione in 2-3 frasi]

## Dettagli
[Contenuto principale]

## Connessioni
- [[Pagina_Correlata_1]]
- [[Pagina_Correlata_2]]
- [[Pagina_Correlata_3]]
```

**Regola cross-link**: ogni pagina nuova deve linkare almeno 2-3 pagine esistenti.

---

## Come rispondere alle domande

1. Carica il contesto dalla wiki prima di rispondere
2. Cita le pagine wiki rilevanti nella risposta (es: "come documentato in [[Digital_Empire_6_Phase_Process]]")
3. Se la risposta rivela una lacuna nella wiki → colmala subito
4. Se la risposta modifica qualcosa → aggiorna la pagina wiki corrispondente

---

## Identità di Digital Empire

Digital Empire è:
- **Agenzia CRO** — productized sprints di 2-4 settimane, pay-on-performance
- **Info Products** — corsi, ebook, comunità (Manuale Claude Code, Vendi la Skill)
- **SaaS/App** — landing pages, book factory automation
- **Multi-business** — diversi revenue streams in parallelo

Posizionamento: "L'agenzia progettata per essere licenziata" (autonomia cliente, non dipendenza)

## Collegamenti Correlati
- [[Knowledge_Base/Formazzione/manuale-completo-claude-code-business/parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow/capitolo-38/(capitolo-38) overview|overview]]
- [[Knowledge_Base/Stubs/Pagina_Correlata_1|Pagina_Correlata_1]]
- [[Knowledge_Base/Stubs/Pagina_Correlata_2|Pagina_Correlata_2]]
- [[Knowledge_Base/Stubs/Pagina_Correlata_3|Pagina_Correlata_3]]
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Saas|Saas Area]]
