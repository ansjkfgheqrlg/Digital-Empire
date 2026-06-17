# WF-HR-REGISTRY — Censimento e Aggiornamento Identity-HR

> Workflow CF-grade | Owner: `cf-conductor` + `cf-agent-registry` | Figura: Chief-Forge
> Blueprint: [[BP-Chief-Forge]] | Versione: 1.0 · 2026-06-17

---

## Scopo

Mantenere il registro Identity-HR di EMPIRE OS aggiornato al 100% in ogni momento: ogni agente
attivo, il suo costo, il suo eval score, il suo ecosistema owner. Include il ciclo periodico di
audit (censimento completo) e il processo formale di ritiro agenti obsoleti o degradati.

**Regola fondamentale:** 0 agenti operativi senza registrazione in Identity-HR. L'identità
organizzativa di EMPIRE OS è questo registro.

---

## Trigger

- **Evento-driven:** ogni volta che FORGE consegna un nuovo agente (via WF-CAPABILITY-INTAKE, Fase 6)
- **Periodico:** audit completo settimanale (ogni lunedì) eseguito da `cf-agent-registry`
- **On-demand:** CEO o conductor richiedono snapshot Identity-HR aggiornato
- **Anomalia:** `cf-agent-registry` rileva agenti non registrati o con dati incoerenti

---

## Input

**Input evento-driven (nuovo agente da FORGE):**
```json
{
  "trigger": "NUOVO_AGENTE",
  "agente_id": "nome-agente",
  "ruolo": "...",
  "tier": "haiku | sonnet | opus",
  "ecosistema_owner": "XX-ECO",
  "path_scheda": "company/...",
  "eval_score": 0,
  "data_build": "YYYY-MM-DD"
}
```

**Input audit periodico:**
```json
{
  "trigger": "AUDIT_SETTIMANALE",
  "data": "YYYY-MM-DD",
  "richiedente": "cf-conductor | CEO | automatico"
}
```

---

## Flusso passo-passo

```
CASO A — REGISTRAZIONE NUOVO AGENTE (evento-driven)
  cf-agent-registry
    ├─ Riceve notifica da cf-forge-liaison: nuovo agente consegnato
    ├─ Verifica unicità ID: l'agente_id è già nel registro?
    │     └─ Se sì → CONFLITTO → segnala a cf-conductor per risoluzione
    ├─ Crea record completo:
    │     {id, ruolo, tier, ecosistema_owner, path_scheda, eval_score, data_registrazione,
    │      costo_stimato_mese, stato: "active", ultimo_invoco: null}
    ├─ Aggiorna snapshot Identity-HR (totale_agenti_registrati, costo_totale_stimato)
    ├─ cf-skill-portfolio: verifica che le skill associate all'agente siano nel catalogo
    └─ Notifica cf-conductor: registrazione completata

  [Gate G1: record completo senza campi nulli critici]
  Tempo atteso: ≤1h dalla notifica FORGE

CASO B — AUDIT SETTIMANALE
  cf-agent-registry
    ├─ STEP 1: SCANSIONE COMPLETA
    │     ├─ Legge tutti i record nel namespace board/chief-forge/registry
    │     ├─ Confronta con: cartelle agenti in company/ (esiste la scheda?)
    │     ├─ Confronta con: log invocazioni (se disponibili) → ultimo_invoco aggiornato
    │     └─ Confronta con: cf-skill-portfolio → ogni agente ha skill associate?
    │
    ├─ STEP 2: CLASSIFICAZIONE ANOMALIE
    │     ├─ Agenti senza path_scheda → CRITICO
    │     ├─ Agenti non invocati da >30gg → OBSOLETO_CANDIDATO
    │     ├─ Agenti con eval_score <70 → DEGRADATO
    │     ├─ Agenti senza ecosistema_owner → ORFANO
    │     └─ Agenti nel registro ma non trovati in company/ → FANTASMA
    │
    ├─ STEP 3: GENERAZIONE REPORT AUDIT
    │     {data, totale_agenti, anomalie_critiche: [], obsoleti_candidati: [],
    │      degradati: [], orfani: [], fantasmi: [], costo_totale_stimato}
    │
    └─ cf-conductor: consegna report con raccomandazioni

  [Gate G2: report audit completo]

  cf-conductor — DECISIONI SU ANOMALIE
    ├─ CRITICO (no scheda, fantasma) → risolvi subito (crea scheda o rimuovi record)
    ├─ OBSOLETO_CANDIDATO → valuta: ritira | mantieni per uso raro | trasferisci ecosistema
    ├─ DEGRADATO → avvia WF-CAPABILITY-INTAKE tipo EXTEND per aggiornamento
    └─ ORFANO → assegna ecosistema_owner

CASO C — RITIRO AGENTE FORMALE
  cf-conductor → cf-agent-registry
    ├─ Riceve decisione di ritiro (da audit o da conductor)
    ├─ Verifica dipendenze: altri agenti o workflow dipendono da questo agente?
    │     └─ Se sì → segnala dipendenze; ritiro non parte finché le dipendenze non sono aggiornate
    ├─ Esegue ritiro:
    │     ├─ Aggiorna record: stato → "deprecated", data_ritiro → oggi
    │     ├─ Archivia scheda: sposta path_scheda in /archivio/ o aggiunge header DEPRECATED
    │     ├─ Notifica ecosistema_owner: "agente X ritirato, sostituzione: Y (se esiste)"
    │     └─ cf-memoria: registra evento ritiro con pattern (perché è stato ritirato)
    └─ Aggiorna snapshot: costo_totale ridotto, agenti_deprecated +1

  [Gate G3: record aggiornato, ecosistema notificato, memoria aggiornata]
```

---

## State machine agente in Identity-HR

| Stato | Descrizione | Transizione |
|---|---|---|
| `registered` | Appena registrato, primo eval completato | → `active` |
| `active` | Operativo, invocato regolarmente | → `obsoleto_candidato` o `degradato` o `deprecated` |
| `obsoleto_candidato` | Non invocato >30gg — in review | → `active` (se riconfermato) o `deprecated` |
| `degradato` | eval_score sceso <70 — richiede update | → `active` (dopo EXTEND) o `deprecated` |
| `deprecated` | Ritirato formalmente | terminale |

---

## KPI di flusso

| Metrica | Target |
|---|---|
| Copertura registro (agenti_registrati / agenti_esistenti) | 100% |
| Ritardi registrazione nuovo agente dopo consegna FORGE | 0 entro 1h |
| Audit settimanali eseguiti | da misurare |
| Agenti orfani dopo audit | 0 |
| Agenti FANTASMA nel registro | 0 |

---

## Connessioni

- [[agenti/cf-agent-registry.md]] — agente owner del workflow
- [[agenti/cf-conductor.md]] — decisioni su anomalie e ritiri
- [[agenti/cf-skill-portfolio.md]] — cross-verifica skill/agenti
- [[agenti/cf-memoria.md]] — registra pattern ritiri e audit
- [[state/README.md]] — schema stato namespace registry
- [[07-FORGE/Agenti/frg-hr-registrar.md]] — operativo FORGE per build-side HR
- [[workflow/WF-CAPABILITY-INTAKE.md]] — per agenti degradati che richiedono EXTEND
