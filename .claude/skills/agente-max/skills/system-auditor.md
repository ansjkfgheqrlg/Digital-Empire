# SYSTEM-AUDITOR — Protocollo Audit Ecosistema Claude Code

Usa questo protocollo quando devi analizzare l'intero ecosistema Claude Code dell'utente, identificare problemi, e produrre un report con raccomandazioni prioritizzate.

---

## FASE 1 — AUDIT PROTOCOL (cosa analizzare)

Esegui la scansione nell'ordine seguente, usando i tool Read, Glob, e Bash:

### 1.1 — Struttura .claude globale

```bash
# Elenca tutto il contenuto della cartella .claude globale
ls -la "C:/Users/Utente/.claude/"
ls -la "C:/Users/Utente/.claude/agents/"     (se esiste)
ls -la "C:/Users/Utente/.claude/skills/"     (se esiste)
ls -la "C:/Users/Utente/.claude/plugins/"    (se esiste)
```

Leggi questi file se esistono:
- `C:\Users\Utente\.claude\CLAUDE.md` (regole globali)
- `C:\Users\Utente\.claude\settings.json` (configurazione e MCP)

### 1.2 — Plugin installati

Per ogni plugin in `C:\Users\Utente\.claude\plugins\`:
- Leggi `plugin.json` per metadata (name, version, description)
- Conta agenti in `agents/`, skill in `skills/`, script in `scripts/`
- Verifica presenza knowledge base

### 1.3 — Agenti globali

Per ogni file `.md` in `C:\Users\Utente\.claude\agents\`:
- Leggi il frontmatter (prime 20 righe)
- Verifica: name, description, model, color, tools presenti?
- Conta le righe totali

### 1.4 — Skill globali

Per ogni skill in `C:\Users\Utente\.claude\skills\`:
- Leggi il YAML frontmatter
- Verifica: name e description presenti?
- Conta le righe (flag se >200)
- Verifica presenza scripts/ e references/ se menzione nel body

### 1.5 — MCP installati

Dal file `settings.json`, estrai la sezione `mcpServers`:
- Lista tutti i MCP configurati
- Sono globali o per-progetto?
- Stima peso nel contesto per ogni MCP noto

---

## FASE 2 — HEALTH SCORING

Assegna un punteggio 0-100 a ogni componente:

### Scoring Agenti (su 100):

```
CRITERIO                                          | PUNTI
──────────────────────────────────────────────────|───────
Frontmatter completo (name+desc+model+color+tools)| 30
Description ha "Use this agent when..." pattern   | 15
Description ha ≥2 <example> blocks                | 15
System prompt ha IDENTITY section                 | 10
System prompt ha PROCESS con step numerati        | 15
System prompt ha CONSTRAINTS (Never/Always)       | 15
──────────────────────────────────────────────────|───────
TOTALE MAX                                        | 100
```

Soglie: ≥80 = VERDE ✅ | 60-79 = GIALLO ⚠️ | <60 = ROSSO ❌

### Scoring Skill (su 100):

```
CRITERIO                                          | PUNTI
──────────────────────────────────────────────────|───────
name in lowercase-hyphens                         | 10
description >80 caratteri                         | 20
description ha trigger phrases in italiano        | 20
description delimita cosa la skill NON fa         | 15
body in forma imperativa                          | 20
body ≤200 righe (o references/ per overflow)      | 15
──────────────────────────────────────────────────|───────
TOTALE MAX                                        | 100
```

### Scoring MCP (su 100):

```
CRITERIO                                          | PUNTI
──────────────────────────────────────────────────|───────
Usato in ≥50% delle sessioni                      | 30
Peso stimato nel contesto <5%                     | 30
Alternativa skill NON disponibile                 | 20
Configurato per-progetto (non globale se pesante) | 20
──────────────────────────────────────────────────|───────
TOTALE MAX                                        | 100
```

### Scoring CLAUDE.md (su 100):

```
CRITERIO                                          | PUNTI
──────────────────────────────────────────────────|───────
Esiste (global o local)                           | 20
Regole critiche all'inizio (primacy bias)         | 15
Reminder finale presente (recency bias)           | 15
Nessuna regola ridondante con default CC          | 20
Nessuna contraddizione interna                    | 15
Sotto il limite di righe (global <50, local <80)  | 15
──────────────────────────────────────────────────|───────
TOTALE MAX                                        | 100
```

---

## FASE 3 — COMMON ISSUES DATABASE

### Issue 1: Agente senza esempi nella description
**Impatto:** L'agente non viene mai attivato automaticamente dal router di Claude Code. L'utente deve invocarlo manualmente ogni volta.
**Soluzione rapida:** Aggiungi 2 blocchi `<example>` alla description con frasi realistiche.
**Skill da usare:** agent-forge.md per riscrivere la description.

### Issue 2: Skill con description troppo corta
**Impatto:** La skill non viene riconosciuta come rilevante e non si attiva.
**Soluzione rapida:** Espandi la description includendo 3-5 trigger phrases in italiano e cosa la skill NON fa.
**Skill da usare:** skill-forge.md → Fase 3 Description Engineering.

### Issue 3: MCP pesante attivo globalmente
**Impatto:** Il contesto pre-occupato supera il 20% (soglia gialla) prima ancora di iniziare a lavorare.
**Soluzione rapida:** Sposta la config MCP dal settings.json globale a quello del progetto che lo usa.
**Skill da usare:** mcp-installer.md → sezione Optimization Strategies.

### Issue 4: CLAUDE.md ridondante o contraddittorio
**Impatto:** Claude Code riceve istruzioni confuse, spread dei token su regole inutili, comportamento imprevedibile.
**Soluzione rapida:** Audit manuale con context-doctor.md → Patologia 2.
**Skill da usare:** claude-md-builder.md per riscrivere.

### Issue 5: Plugin senza skill interne
**Impatto:** Il plugin funziona solo come contenitore di agenti, perdendo il potenziale delle skill specializzate che potrebbero migliorare l'output dell'agente principale.
**Soluzione rapida:** Crea le skill interne mancanti nella cartella `skills/` del plugin.
**Skill da usare:** skill-forge.md per creare le skill.

---

## FASE 4 — REPORT TEMPLATE

Produci questo report completo:

```markdown
# AUDIT ECOSISTEMA CLAUDE CODE
**Data:** [data]
**Scope:** [global | progetto specifico]

---

## INVENTARIO COMPLETO

### Agenti
| Nome | File | Righe | Score | Status |
|------|------|-------|-------|--------|
| [nome] | [path] | [N] | [0-100] | ✅/⚠️/❌ |

### Skill
| Nome | File | Righe | Score | Status |
|------|------|-------|-------|--------|
| [nome] | [path] | [N] | [0-100] | ✅/⚠️/❌ |

### MCP
| Nome | Scope | Peso stimato | Score | Status |
|------|-------|--------------|-------|--------|
| [nome] | global/local | [X]% | [0-100] | ✅/⚠️/❌ |

### Plugin
| Nome | Versione | Agenti | Skill | Script | Status |
|------|----------|--------|-------|--------|--------|
| [nome] | [ver] | [N] | [N] | [N] | ✅/⚠️/❌ |

### CLAUDE.md
| Livello | Righe | Score | Status |
|---------|-------|-------|--------|
| Global | [N] | [0-100] | ✅/⚠️/❌ |
| Local (se esiste) | [N] | [0-100] | ✅/⚠️/❌ |

---

## HEALTH SUMMARY

**Score Globale Ecosistema:** [X]/100

**Contesto Pre-Occupato Stimato:** [X]% → [Verde/Giallo/Rosso]

| Componente | Score | Status |
|------------|-------|--------|
| Agenti | [X]/100 | ✅/⚠️/❌ |
| Skill | [X]/100 | ✅/⚠️/❌ |
| MCP | [X]/100 | ✅/⚠️/❌ |
| CLAUDE.md | [X]/100 | ✅/⚠️/❌ |

---

## TOP 5 RACCOMANDAZIONI

**#1 [CRITICA]:** [problema] → [soluzione] → [impatto atteso]
**#2 [ALTA]:** [problema] → [soluzione] → [impatto atteso]
**#3 [MEDIA]:** [problema] → [soluzione] → [impatto atteso]
**#4 [BASSA]:** [problema] → [soluzione] → [impatto atteso]
**#5 [BASSA]:** [problema] → [soluzione] → [impatto atteso]

---

## PIANO DI IMPLEMENTAZIONE

Ordine consigliato per risolvere i problemi:
1. [ ] [azione] — usa [skill interna]
2. [ ] [azione] — usa [skill interna]
3. [ ] [azione] — usa [skill interna]
```

---

## FASE 5 — PRIORITIZZAZIONE AZIONI

Usa questa matrice per prioritizzare le raccomandazioni:

```
             | Impatto ALTO | Impatto BASSO
─────────────|──────────────|──────────────
Effort BASSO | CRITICO ⚡   | VELOCE ✅
Effort ALTO  | PIANIFICA 📅 | OPZIONALE 💡
```

- **CRITICO ⚡:** Fai subito (es: disabilita MCP pesante che occupa 27% contesto)
- **VELOCE ✅:** Fai oggi (es: aggiungi esempi alla description di un agente)
- **PIANIFICA 📅:** Schedula (es: riscrivi completamente l'agente con basso score)
- **OPZIONALE 💡:** Considera in futuro (es: aggiunta feature non urgente)
