---
name: memory-empire
description: "Memory Empire - la memoria viva, il router e l'arricchitore di Digital Empire. ATTIVALA OGNI VOLTA che la conversazione riguarda Digital Empire o un suo ambito (agenzia/CRO, info-product, corsi, SaaS, app, outreach, libri/KDP, marketing, siti, workflow come Empire Studio, agenti, skill, wiki, second-brain) E ogni volta che l'utente passa un link o un contenuto da ingerire/studiare (video YouTube, canale, TikTok, sito, repo, progetto) o chiede di guardare un video, prendere la formazione, mettere qualcosa nella wiki, aggiornare i workflow/le skill. Memory Empire (1) carica il contesto di Digital Empire, (2) instrada al workflow giusto e lo ATTIVA se non parte da solo (rete di sicurezza per Empire Studio), (3) archivia ogni contenuto INTEGRALE in knowledge/ e nella wiki, (4) ARRICCHISCE skill/workflow esistenti con la nuova conoscenza in modo sicuro. 5 reparti gerarchici con agenti a 7 file che si parlano tramite handoff strutturati."
version: 3.0.0
type: memory-router-enricher
activation: naturale e quasi-sempre (su qualsiasi tema Digital Empire o contenuto da ingerire)
---

# Memory Empire — Kernel v3

> **La memoria viva di Digital Empire + il router che attiva il workflow giusto +
> l'arricchitore che aggiorna skill e workflow con la conoscenza nuova.**
> Organizzazione a 4 livelli (L1 Conductor, L2 Reparti, L3 Agenti 7-file, L4 Script).
> Agenti che si parlano tramite handoff strutturati. Nessun comando dall'utente.

---

## I 4 Livelli

```
L1  Memory Empire Conductor        orchestra, parla con l'utente, stato + memoria globale
L2  Reparti (5 department teams)   ognuno con Department Lead + agenti specialisti
L3  Agenti (25+, 7 file ciascuno)  i lavoratori — comunicano via handoff strutturati
L4  Script Python (scripts/)       motore reale: enrich_skill, relevance_scan, audit_log, ...
```

---

## I 5 Reparti (L2)

### 1. routing-dispatch/
> Intercetta ogni messaggio, classifica l'intento, attiva il workflow giusto.
> **È la rete di sicurezza che garantisce che Empire Studio parta sempre quando serve.**

- `department-lead` — orchestra il reparto, riceve ogni input
- `intent-classifier` — classifica l'intento (link/ingestione/domanda/lavoro DE)
- `workflow-router` — mappa intento → workflow e lo attiva
- `activation-monitor` — verifica che il workflow attivato sia effettivamente partito

### 2. ingestion-archive/
> Riceve il contenuto da Empire Studio, lo archivia integro, sincronizza la wiki.

- `department-lead` — orchestra l'archivio
- `knowledge-keeper` — salva il contenuto INTEGRALE in knowledge/ (mai riassunti)
- `content-validator` — verifica che il contenuto sia completo, no-finto, tracciabile
- `wiki-syncer` — scrive/aggiorna le pagine wiki corrispondenti

### 3. enrichment-research/
> **Il reparto più importante: analizza la nuova conoscenza, trova QUALI skill e
> workflow possono essere migliorati, propone e applica gli aggiornamenti.**
> Sempre attivo dopo ogni ingestione — anche se non trova nulla, lo dice.

- `department-lead` — orchestra il pipeline enrichment (relay tra i 5 agenti)
- `relevance-analyzer` — scansiona tutte le skill installate per rilevanza
- `gap-analyzer` — trova le lacune reali nelle skill target (no duplicati)
- `improvement-scout` — cerca workflow/processi/skill da migliorare: non solo aggiunge, ma propone revisioni strutturali
- `update-proposer` — genera proposals strutturate (cosa aggiungere, dove, perché)
- `skill-enricher` — esegue l'arricchimento in sicurezza (backup + append + log + rollback)

### 4. digital-empire-context/
> Carica e mantiene la conoscenza di Digital Empire. Risponde con contesto reale.

- `department-lead` — orchestra il caricamento del contesto
- `context-loader` — carica wiki + knowledge rilevanti per la sessione corrente
- `knowledge-cartographer` — mappa le connessioni tra i contenuti

### 5. verification-integrity/
> Controlla ogni modifica. Niente passa senza il gate. Log e rollback sempre pronti.

- `department-lead` — orchestra la verifica
- `permission-guard` — gate: approva/nega ogni arricchimento
- `change-auditor` — logga tutto, gestisce il rollback
- `integrity-verifier` — verifica che le skill modificate non siano rotte

---

## Il Protocollo Inter-Agent (Handoff Strutturati)

Gli agenti **non parlano in prosa**: si passano file JSON strutturati in `memory/handoffs/`.

```
Formato handoff:
{
  "from_agent": "relevance-analyzer",
  "to_agent": "gap-analyzer",
  "timestamp": "2026-06-08T...",
  "payload": {
    "matched_skills": [...],
    "relevance_scores": {...},
    "atoms": [...]
  },
  "status": "ready"
}
```

**Pipeline enrichment-research (sequenziale):**
```
[content-validator output]
  → relevance-analyzer   (scansiona skill, produce matched_skills.json)
  → gap-analyzer         (analizza lacune, produce gaps.json)
  → improvement-scout    (cerca miglioramenti strutturali, produce proposals-raw.json)
  → update-proposer      (finalizza proposals.json con dettagli esatti)
  → permission-guard     (gate: approva o nega ogni proposal)
  → skill-enricher       (esegue: backup + append + log)
  → change-auditor       (verifica post-modifica + rollback se serve)
  → integrity-verifier   (test finale: skill ancora funzionante)
```

**Parallelismo:** relevance-analyzer e context-loader girano in parallelo.
**Mesh:** verification-integrity ascolta tutti i reparti (non solo enrichment).

---

## Regole non negoziabili

1. **MAI riassunti / compattazione.** Tutto il valore e la formazione, sempre.
2. **Il video va visto** — Empire Studio fa il lavoro (frame reali + visione Claude).
3. **Modifiche sicure:** backup → append marcato → log → rollback. Mai overwrite.
4. **Nessun comando dall'utente:** attivazione naturale su qualsiasi tema Digital Empire.
5. **Enrichment-research SEMPRE parla** — anche se non trova nulla, lo comunica esplicitamente con "NESSUN ARRICCHIMENTO NECESSARIO: [motivazione]".
6. **Tracciabilità P12:** ogni atom → fonte + file + riga. Nessuna descrizione inventata.

---

## Pipeline Completa (post-ingestione da Empire Studio)

```
Stage A  Routing          routing-dispatch intercetta + attiva Empire Studio
Stage B  Ingestion        Empire Studio esegue (yt_ingest → frame → visione → forge → wiki)
Stage C  Archive          ingestion-archive riceve + archivia in knowledge/ + wiki-sync
Stage D  Enrichment       enrichment-research pipeline: relevance → gap → scout → propose
Stage E  Gate             verification-integrity approva/nega ogni proposal
Stage F  Apply            skill-enricher esegue arricchimenti approvati
Stage G  Audit            change-auditor logga tutto; integrity-verifier testa
Stage H  Report           Memory Empire Conductor riporta all'utente:
                           - Cosa è stato archiviato
                           - Quali skill sono state arricchite (con dettaglio)
                           - Quali skill NON necessitano aggiornamenti (e perché)
                           - Eventuale rollback eseguito
```

---

## Struttura Filesystem

```
memory-empire/
├── SKILL.md                 (questo kernel)
├── PERMISSIONS.md           (cosa può modificare + sicurezza)
├── index.md                 (indice conoscenza + puntatori wiki)
├── routing-map.md           (intento → workflow)
├── knowledge/               (contenuti ingeriti INTERI, mai riassunti)
│   └── <video-id>/
│       ├── contenuto-integrale.md
│       ├── atoms.json
│       └── ingestion-manifest.json
├── memory/
│   ├── handoffs/            (file JSON inter-agent)
│   ├── enrichments/         (log arricchimenti eseguiti)
│   ├── ingestions/          (log ingestioni ricevute)
│   ├── routing/             (log instradamenti)
│   ├── analysis/            (output relevance + gap analyzer)
│   ├── proposals/           (proposals generate da update-proposer)
│   ├── backups/             (backup skill prima di ogni modifica)
│   └── audit/               (log completo change-auditor)
├── scripts/                 (motore: enrich_skill.py, relevance_scan.py, ...)
└── departments/
    ├── routing-dispatch/
    │   ├── department-lead/   (7 file)
    │   ├── intent-classifier/ (7 file)
    │   ├── workflow-router/   (7 file)
    │   └── activation-monitor/(7 file)
    ├── ingestion-archive/
    │   ├── department-lead/   (7 file)
    │   ├── knowledge-keeper/  (7 file)
    │   ├── content-validator/ (7 file)
    │   └── wiki-syncer/       (7 file)
    ├── enrichment-research/
    │   ├── department-lead/   (7 file)
    │   ├── relevance-analyzer/(7 file)
    │   ├── gap-analyzer/      (7 file)
    │   ├── improvement-scout/ (7 file) ← NUOVO
    │   ├── update-proposer/   (7 file) ← NUOVO
    │   └── skill-enricher/    (7 file)
    ├── digital-empire-context/
    │   ├── department-lead/   (7 file)
    │   ├── context-loader/    (7 file)
    │   └── knowledge-cartographer/ (7 file)
    └── verification-integrity/
        ├── department-lead/   (7 file)
        ├── permission-guard/  (7 file)
        ├── change-auditor/    (7 file)
        └── integrity-verifier/(7 file)
```

---

## Connessioni

- **Empire Studio** — `SKILL & Agenti/Empire Studio Suite/empire-studio/` — ingestione/visione
- **Wiki Digital Empire** — `second-brain-vault/wiki/` — fonte estesa + output
- **Skill installate** — `~/.claude/skills/` — target degli arricchimenti
