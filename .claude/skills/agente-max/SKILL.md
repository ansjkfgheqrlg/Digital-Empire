---
name: cc-master
description: System expert for Claude Code: creating skills, creating agents, and managing project context.
---
# MEMORIA SESSIONE — CC-Master v2.0 Upgrade
**Data:** 2026-03-08
**Stato:** COMPLETATO AL 100%

---

## COSA ABBIAMO FATTO IN QUESTA SESSIONE

### 1. Trovato l'agente CC-Master
- Era in: `C:\Users\Utente\.claude\plugins\cc-master\`
- Copiato in: `C:\Users\Utente\Desktop\qui tutto\Digital Empire\SKILL & Agenti\SKILL\Agente Max\`

### 2. Upgrade Drastico CC-Master v1.0 → v2.0

**Problema risolto:** L'agente leggeva 436KB di CONOSCIENZA.md ad ogni task (54% del contesto).

**Soluzione implementata:**

#### STEP 1 — Knowledge Base Partizionata ✅
Diviso CONOSCIENZA.md in 9 moduli selettivi:
- `K01-fondamenta.md` — 28.4 KB (Cap 1-4)
- `K02-installazione.md` — 39.0 KB (Cap 5-8)
- `K03-progetti.md` — 47.8 KB (Cap 13-16)
- `K04-permessi.md` — 33.6 KB (Cap 17-19)
- `K05-context.md` — 66.5 KB (Cap 20-23)
- `K06-sub-agenti.md` — 62.4 KB (Cap 24-26)
- `K07-skill-system.md` — 52.7 KB (Cap 27-30)
- `K08-mcp.md` — 39.3 KB (Cap 31-34)
- `K09-avanzate.md` — 67.4 KB (Cap 35-38)

**NOTA:** I capitoli 9-12 (CLAUDE.md system, PARTE 3) sono ASSENTI dal file CONOSCIENZA.md originale. Non esistono nel documento sorgente.

#### STEP 2 — cc-master.md riscritto completamente ✅
Nuovo framework: **OPDV (Orient → Plan → Dispatch → Verify)**
- Knowledge Router: mappa task → modulo KB specifico
- Lazy loading: legge solo il modulo rilevante, mai tutto
- Plan gate obbligatorio prima di ogni esecuzione file
- Internal Skill Dispatcher: mappa task → skill interna

#### STEP 3 — plugin.json v2.0 ✅
Aggiunto: agents, skills, knowledge, scripts, capabilities, settings

#### STEP 4 — 7 Skill Interne create ✅
In `skills/`:
- `skill-forge.md` — crea skill da zero
- `agent-forge.md` — crea agenti da zero
- `workflow-architect.md` — pianifica workflow complessi
- `context-doctor.md` — diagnostica e ottimizza contesto
- `claude-md-builder.md` — crea/ottimizza CLAUDE.md
- `system-auditor.md` — audit ecosistema CC
- `mcp-installer.md` — installa e configura MCP

#### STEP 5 — 4 Python Scripts creati ✅
In `scripts/`:
- `generate_skill.py` — scaffolding skill da CLI
- `generate_agent.py` — scaffolding agente da CLI
- `context_calculator.py` — report consumo token con soglie Cap.23
- `validate_structure.py` — validazione skill/agenti/plugin con scoring

#### STEP 6 — Tutto copiato in .claude/plugins/cc-master/ ✅

---

## STRUTTURA FINALE

```
C:\Users\Utente\.claude\plugins\cc-master\
├── .claude-plugin\
│   └── plugin.json              ✅ v2.0
├── agents\
│   └── cc-master.md             ✅ riscritto con OPDV
├── knowledge\
│   ├── CONOSCIENZA.md           ✅ originale intatto
│   ├── K01-fondamenta.md        ✅ NUOVO
│   ├── K02-installazione.md     ✅ NUOVO
│   ├── K03-progetti.md          ✅ NUOVO
│   ├── K04-permessi.md          ✅ NUOVO
│   ├── K05-context.md           ✅ NUOVO
│   ├── K06-sub-agenti.md        ✅ NUOVO
│   ├── K07-skill-system.md      ✅ NUOVO
│   ├── K08-mcp.md               ✅ NUOVO
│   └── K09-avanzate.md          ✅ NUOVO
├── skills\
│   ├── skill-forge.md           ✅ NUOVO
│   ├── agent-forge.md           ✅ NUOVO
│   ├── workflow-architect.md    ✅ NUOVO
│   ├── context-doctor.md        ✅ NUOVO
│   ├── claude-md-builder.md     ✅ NUOVO
│   ├── system-auditor.md        ✅ NUOVO
│   └── mcp-installer.md         ✅ NUOVO
└── scripts\
    ├── generate_skill.py        ✅ NUOVO
    ├── generate_agent.py        ✅ NUOVO
    ├── context_calculator.py    ✅ NUOVO
    └── validate_structure.py    ✅ NUOVO
```

Stessa struttura IDENTICA anche in:
`C:\Users\Utente\Desktop\qui tutto\Digital Empire\SKILL & Agenti\SKILL\Agente Max\`

---

## COSA RESTA DA FARE (potenziali miglioramenti futuri)

### PRIORITÀ ALTA
1. **Testare cc-master v2.0** — aprire nuova sessione Claude Code e verificare:
   - Il Knowledge Router funziona? (es: chiedere "come installo CC" → deve leggere K02)
   - Il Plan gate funziona? (es: "crea una skill" → deve presentare piano prima)
   - skill-forge viene invocato quando si chiede di creare una skill?

2. **Aggiungere CLAUDE.md globale** — il file `C:\Users\Utente\.claude\CLAUDE.md` non è stato modificato. Potrebbe essere ottimizzato per integrare le regole di cc-master.

### PRIORITÀ MEDIA
3. **Verificare i capitoli 9-12 mancanti** — Il manuale CONOSCIENZA.md non contiene i capitoli 9-12 (PARTE 3 — CLAUDE.md system). Potrebbero essere stati omessi nell'originale o essere in un altro file. Se esistono, andrebbero aggiunti.

4. **Creare un CLAUDE.md locale per "Agente Max"** — un CLAUDE.md nella cartella Agente Max che guidi cc-master quando lavora in quel progetto specifico.

5. **Test degli script Python** — Eseguire:
   ```bash
   python scripts\context_calculator.py --show-breakdown
   python scripts\validate_structure.py --target . --type all
   ```

### PRIORITÀ BASSA
6. **Aggiungere altri trigger alla description di cc-master** per coprire più casi d'uso

7. **Creare skill per casi d'uso specifici di Digital Empire** — es: skill per gestire il workflow di creazione contenuti, skill per gestire il workflow commerciale

---

## METRICHE UPGRADE

| Metrica | Prima (v1.0) | Dopo (v2.0) |
|---------|-------------|-------------|
| Token consumati per task | ~108.000 (54%) | ~10.000-25.000 (5-12%) |
| Reasoning esplicito | Nessuno | OPDV obbligatorio |
| Skill specializzate interne | 0 | 7 |
| Scripts di supporto | 0 | 4 |
| Moduli KB selettivi | 0 (1 monolite) | 9 |

---

## FILE PRINCIPALI DA CONOSCERE

| File | Funzione |
|------|----------|
| `agents\cc-master.md` | Il cuore dell'agente — Framework OPDV + Knowledge Router |
| `skills\skill-forge.md` | Usare per creare nuove skill |
| `skills\workflow-architect.md` | Usare per pianificare workflow complessi |
| `skills\context-doctor.md` | Usare quando il contesto è troppo pieno |
| `scripts\context_calculator.py` | Report consumo token ecosistema |
| `scripts\validate_structure.py` | Validare skill/agenti/plugin |

---

## NOTE TECNICHE

- **Capitoli 9-12 assenti:** La CONOSCIENZA.md salta da Cap.8 a Cap.13. Non c'è PARTE 3 nel file. Non è un errore nostro.
- **Percorsi:** Tutto usa Windows backslash. I moduli KB usano percorso assoluto nella cc-master.md.
- **Doppia posizione:** I file esistono sia in `Agente Max\` (copia di lavoro) che in `.claude\plugins\cc-master\` (installato). Aggiornare entrambi quando si fanno modifiche.
- **Plugin attivo:** Il plugin è installato e attivo in Claude Code. Per aggiornarlo, modificare in `Agente Max\` e poi copiare in `.claude\plugins\cc-master\`.
