---
Type: CONCEPT
Status: Active
Tags: #cmo #state #agentdb #memoria #namespace #persistenza
Created: 2026-06-17
Last updated: 2026-06-17
---

# STATE — CMO (Chief Marketing Officer)

> Definisce il namespace di persistenza del team CMO in AgentDB e su filesystem.
> Ogni agente del team scrive e legge dal namespace corretto. Nessun dato critico
> vive solo nella sessione: tutto ciò che conta è persistito qui.

---

## Namespace AgentDB: `board/cmo/`

```
board/cmo/
│
├── campagne/                        — STATO PER CAMPAGNA
│   └── <campaign-id>/
│       ├── brief.json               — input iniziale (pre-condizioni)
│       ├── strategia.json           — output cmo-campaign-strategist
│       ├── funnel.json              — output cmo-funnel-architect
│       ├── brief-liaison/
│       │   ├── marketing-brief.json — brief per 04-MARKETING
│       │   └── content-brief.json   — brief per 03-CONTENT-FACTORY
│       ├── assets/                  — asset prodotti con gate-log per ognuno
│       ├── gate-log.json            — tutti i check APSOC (score, esito, sezioni)
│       ├── launch-log.json          — timestamp attivazione canali
│       └── performance/             — report settimanali e retrospettiva
│
├── brand-gate-log/                  — LOG GATE APSOC (always-on)
│   ├── <copy-id>.json               — ogni check: input, score, G2, esito, timestamp
│   └── aggregate-stats.json         — first-pass rate, score medio, sezioni più fallite
│
├── icp-patterns/                    — LIBRERIA PATTERN ICP (skill icp-pattern-library)
│   ├── <nicchia>/
│   │   └── <formato>/
│   │       └── <pattern-id>.json    — pattern con metrica conferma + flag validità
│   └── index.json                   — indice per query rapida
│
├── funnel/                          — MAPPA FUNNEL ATTIVI
│   ├── <funnel-id>.json             — schema funnel (fasi, nodi, metriche)
│   └── gap-report.json              — ICP senza funnel, prodotti senza entry point
│
├── lancio-history/                  — STORICO LANCI
│   └── <lancio-id>/
│       ├── brief.json
│       ├── piano-lancio.json
│       ├── icp-brief-lancio.json
│       ├── funnel-lancio.json
│       ├── allineamento-cro.json    — conferma allineamento CMO ↔ CRO
│       ├── gate-sales-page.json     — score APSOC ≥85 + G2
│       ├── dry-run.json             — stima costi + flag ok-umano
│       ├── lancio-log.json
│       └── report-72h.json
│
└── performance/                     — DATI PERFORMANCE AGGREGATI
    ├── campagne-chiuse.json         — lista campagne con KPI finali
    └── trend-apsoc.json             — trend score APSOC nel tempo
```

---

## Regole di scrittura/lettura

1. **Write after gate:** nessun output di campagna viene scritto in `campagne/<id>/assets/`
   senza che `gate-log.json` abbia un record per quell'asset con `gate_pass: true`.
   Un asset senza record di gate = non verificato = non pubblicabile.

2. **Immutabilità dei log:** i file `-log.json` sono append-only. Nessun agente sovrascrive
   un record esistente. Se c'è una correzione, si aggiunge un nuovo record con timestamp.

3. **brand_kit in ogni record:** ogni record che contiene testo di conversione deve avere
   il campo `brand_kit` popolato. Mandato Art.6.1.

4. **PII fuori dal namespace:** nessun dato personale identificabile (email, nome, telefono
   di lead reali) entra nel namespace AgentDB del CMO senza anonimizzazione. Mandato Art.7.2.

5. **Dry-run flag:** ogni record `dry-run.json` deve avere `ok_umano: true` prima che
   il workflow possa procedere allo step successivo. Il flag è scritto SOLO dopo conferma
   umana esplicita, non automaticamente.

---

## Ripartibilità a freddo (test amnesia)

Il namespace CMO deve permettere di ricostruire lo stato di qualsiasi campagna o lancio
leggendo solo i file del namespace:
- Da `campagne/<id>/brief.json` + `strategia.json` → obiettivo e strategia della campagna.
- Da `brand-gate-log/<copy-id>.json` → perché un output è stato approvato o bloccato.
- Da `lancio-history/<id>/gate-sales-page.json` → con che score è stata approvata la sales page.
- Da `icp-patterns/` → quali pattern erano attivi al momento della campagna.

Se queste 4 domande non hanno risposta nel namespace → il namespace è incompleto.

---

## Sincronizzazione con wiki

Il namespace AgentDB è l'indice semantico per gli agenti. La fonte di verità leggibile
dall'uomo è la wiki (`second-brain-vault/wiki/`). In caso di conflitto: **vince la wiki**
(Mandato Art.5.2).

Ogni operazione rilevante del CMO che produce una decisione o un risultato misurabile
viene loggata in `second-brain-vault/wiki/log.md` (Drift-Sentinel vigila: lag < 24h).

---

## Connessioni

- [[kpi/KPI.md]] — i KPI che questo namespace alimenta
- [[cmo-memoria]] · `agenti/cmo-memoria.md` — agent che scrive/legge `icp-patterns/`
- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md` — scrive `brand-gate-log/`
- [[cmo-performance-analyst]] · `agenti/cmo-performance-analyst.md` — scrive `performance/`
- [[WF-CAMPAGNA]] · `workflow/WF-CAMPAGNA.md` — scrive `campagne/<id>/`
- [[WF-LANCIO-COORD]] · `workflow/WF-LANCIO-COORD.md` — scrive `lancio-history/<id>/`
- [[MANDATO-EMPIRE]] Art.5.2 (wiki-first) + Art.6.1 (brand_kit) + Art.7.2 (PII)
