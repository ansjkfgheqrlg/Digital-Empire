# ACTIVATION-GUIDE
            
> Path: [[Map - Crea_Siti|Crea siti > system]]

## Content

# Activation Guide — Digital Empire
> Come rendere operative skill e agenti in Claude Code.

---

## Cos'è l'Attivazione

I file in `Crea siti/agents/` e `Crea siti/skills/` sono la **source of truth** (leggibili, modificabili, versionabili). Per diventare operativi devono essere copiati in `C:\Users\Utente\.claude\`.

```
Crea siti/agents/*  →  C:\Users\Utente\.claude\agents\    (piatto, tutti i .md)
Crea siti/skills/*  →  C:\Users\Utente\.claude\skills\    (struttura intatta)
```

---

## Comando di Attivazione Completo

Per attivare tutto il sistema (agenti + skill):

```bash
# Attiva tutti gli AGENTI (flattening dalle sottocartelle)
find "c:/Users/Utente/Desktop/qui tutto/Digital Empire/Crea siti/agents" -name "*.md" -exec cp {} "C:/Users/Utente/.claude/agents/" \;

# Attiva tutte le SKILL (struttura cartelle intatta)
cp -r "c:/Users/Utente/Desktop/qui tutto/Digital Empire/Crea siti/skills/"* "C:/Users/Utente/.claude/skills/"
```

**Nota importante:** `.claude/agents/` usa file piatti (nomi univoci). La struttura a sottocartelle in `Crea siti/agents/` è solo per la navigazione locale.

---

## Attivazione Selettiva

### Solo un agente
```bash
cp "c:/Users/Utente/Desktop/qui tutto/Digital Empire/Crea siti/agents/orchestrators/opus-director.md" \
   "C:/Users/Utente/.claude/agents/"
```

### Solo una skill
```bash
cp -r "c:/Users/Utente/Desktop/qui tutto/Digital Empire/Crea siti/skills/opus" \
      "C:/Users/Utente/.claude/skills/"
```

### Solo OPUS completo (skill + agente)
```bash
cp -r "c:/Users/Utente/Desktop/qui tutto/Digital Empire/Crea siti/skills/opus" \
      "C:/Users/Utente/.claude/skills/"
cp "c:/Users/Utente/Desktop/qui tutto/Digital Empire/Crea siti/agents/orchestrators/opus-director.md" \
   "C:/Users/Utente/.claude/agents/"
```

---

## Verifica Attivazione

Dopo aver copiato, verifica in Claude Code:
- Le skill appaiono come `/opus`, `/site`, `/market`, ecc.
- Gli agenti appaiono nella lista quando si lancia `Agent tool`
- `opus-director` appare con colore gold `#B8860B`

---

## Struttura `.claude/` Risultante

```
C:\Users\Utente\.claude\
├── agents\
│   ├── cc-master.md
│   ├── opus-director.md
│   ├── market-competitive.md
│   ├── market-content.md
│   ├── market-conversion.md
│   ├── market-strategy.md
│   ├── market-technical.md
│   ├── omega-executor.md
│   ├── omega-verifier.md
│   ├── site-build-shell.md
│   ├── site-build-pages.md
│   ├── site-build-interactions.md
│   ├── site-copy-hero.md
│   ├── site-copy-body.md
│   ├── site-copy-meta.md
│   ├── site-qa-html.md
│   ├── site-qa-accessibility.md
│   ├── site-qa-performance.md
│   └── site-qa-mobile.md
│
└── skills\
    ├── opus\
    │   ├── SKILL.md
    │   ├── OPUS-PROCESS.md
    │   ├── ANTI-AI-BLACKLIST.md
    │   ├── POLISH-LOOP-PROTOCOL.md
    │   ├── TYPOGRAPHY-SYSTEM.md
    │   ├── OPUS-STATUS-template.md
    │   └── templates\
    │       ├── ag-design-manifesto.md
    │       ├── ag-atmosphere.md
    │       ├── ag-token-review.md
    │       ├── ag-typography.md
    │       ├── ag-copy.md
    │       ├── ag-motion.md
    │       ├── ag-polish.md
    │       └── ag-launch.md
    ├── site\
    ├── site-brief\  ... site-report\
    ├── market\
    ├── market-ads\  ... market-social\
    ├── brand-guidelines\
    ├── canvas-design\
    ├── frontend-design\
    ├── omega-create\
    ├── skill-creator\
    └── theme-factory\
```

---

## Workflow di Modifica

1. **Modifica** il file in `Crea siti/agents/` o `Crea siti/skills/`
2. **Di' "attiva"** a Claude → copia in `.claude/` → diventa operativo
3. **Verifica** che il comportamento sia corretto in Claude Code

---

## File Importanti

| File | Percorso | Scopo |
|------|----------|-------|
| README.md | `Crea siti/README.md` | Navigazione master |
| OPUS-CONTEXT.md | `Crea siti/OPUS-CONTEXT.md` | Stato sessione |
| OPUS-PROCESS.md | `Crea siti/skills/opus/OPUS-PROCESS.md` | Processo completo 21 fasi |
| Architettura | `Crea siti/system/ARCHITETTURA-SISTEMA-SITE.md` | Overview sistema |

## Collegamenti Correlati
- [[Knowledge_Base/Formazzione/manuale-completo-claude-code-business/parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow/capitolo-38/(capitolo-38) overview|overview]]
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
- [[Map - Formazzione|Formazzione Area]]
