# SCHEMA CANONICO — Skill

> Forma LEGGERA-MEDIA. Capability riusabile a invocazione (slash o naturale), con kernel snello
> + progressive disclosure. Motore reale: `skill-creator`, `Skill Master Architecture` (P02, P06).

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando serve una capability ripetibile, attivabile da una frase/comando, che un singolo
  agente esegue (es. scrivere copy, validare uno schema, generare un carosello).
- **NO se** serve coordinazione di più ruoli in parallelo → **Team**. NO se è un processo a passi
  con gate e owner ma senza descrizione invocabile → **Workflow**. NO se è solo una regola di
  giudizio → **Principio**/**Stile**. NO se è una singola entità always-on con I/O JSON → **Agente**.

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **Cartella** `<skill-slug>/` in kebab-case.
2. **`SKILL.md`** = kernel, 80–500 righe (MAI oltre). Contiene:
   - **Frontmatter YAML**: `name:` (kebab-case, == slug) + `description:` (in 3ª persona, dice
     COSA fa + QUANDO usarla + trigger espliciti + un "DO NOT use for…"; questa è il prodotto —
     è ciò che fa scattare l'attivazione).
   - **Titolo + comando di invocazione** (slash + invocazione naturale).
   - **Invarianti/regole cardinali** non negoziabili.
   - **Input supportati** + limiti.
   - **Pipeline/uso** ad alto livello (il dettaglio sta nelle references, non qui).
3. **`references/`** ≥3 file, ≥300 righe totali — il dettaglio caricato on-demand (progressive
   disclosure): `concepts/`, `processes/`, `patterns/`, `schemas/`, `conventions/anti-patterns.md`.
4. **`evals/evals.json`** ≥4 prompt di test (incl. ≥1 negativo: NON deve attivarsi).
5. **`README.md`** breve: installazione + uso.
6. *(Opzionali se serve)* `agents/`, `scripts/` (logica deterministica), `assets/templates/`.

## Template vuoto (copiabile)
```
<skill-slug>/
├── SKILL.md            # frontmatter name+description + kernel ≤500 righe
├── references/         # ≥3 file, ≥300 righe tot — dettaglio on-demand
│   ├── concepts/...
│   ├── processes/...
│   └── conventions/anti-patterns.md
├── evals/evals.json    # ≥4 prompt (≥1 negativo)
├── scripts/            # (opz.) logica deterministica
├── assets/templates/   # (opz.)
└── README.md
```
```yaml
---
name: <skill-slug>
description: '<Cosa fa, 3ª persona>. Use when <trigger 1>, <trigger 2>, "<frase utente>". DO NOT use for <esclusione>.'
---
```

## Checklist di completezza (per struct-gate)
- [ ] Esiste `SKILL.md` con frontmatter contenente `name` E `description`.
- [ ] `name` è kebab-case e identico allo slug della cartella.
- [ ] `description` contiene COSA + QUANDO + ≥1 trigger esplicito + ≥1 esclusione "DO NOT".
- [ ] Kernel `SKILL.md` ≤ 500 righe.
- [ ] `references/` esiste con ≥3 file e ≥300 righe totali.
- [ ] `evals/evals.json` esiste con ≥4 prompt, di cui ≥1 negativo.
- [ ] `README.md` presente con installazione + uso.
- [ ] Nessun placeholder `<REPLACE>` / sezione vuota nel kernel (anti AP01).

## Esempio minimo compilato
```yaml
---
name: headline-forge
description: 'Genera e itera headline ad alto CTR per landing/ad. Use when "scrivimi un titolo", "headline per la hero", "varianti di headline". DO NOT use for full sales page (vedi cro-copy-architect).'
---
# headline-forge — kernel
> /headline <brief> · oppure descrivi prodotto + audience.
## Invarianti
1. Ogni headline porta un beneficio misurabile, mai vaga.
## Uso
Carica references/frameworks/ per i 7 pattern di headline. Output: 10 varianti + rationale.
```
references/frameworks/patterns.md (220 righe), references/conventions/anti-patterns.md (90 righe),
evals/evals.json (5 prompt). → struct-gate: COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- `description` che dice solo COSA senza QUANDO/trigger → la skill non si attiva mai (P15).
- Kernel gonfio >500 righe con tutto inline → viola progressive disclosure (P02).
- `references/` assente o thin (1 file, <300 righe) → "scaffold as deliverable" (AP01).
- Nessuna eval → non verificabile.
- `name` diverso dallo slug → installazione rotta.

## Connessioni
- [[README]] — indice libreria + principio della FORMA GIUSTA
- [[Schema-Agente]] — se la capability è una entità con stato/I-O JSON, non una skill
- [[Schema-Workflow]] — se è un processo a passi con gate/owner
- 14-DOSSIER-ARCHITETTURA §1 (forma Skill) · §5 (skill `arch-blueprint`, `canonical-schema`)
