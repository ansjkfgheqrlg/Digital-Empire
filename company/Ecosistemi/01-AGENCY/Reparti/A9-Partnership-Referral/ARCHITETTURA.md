---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #partnership #referral #non-icp #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# ARCHITETTURA — A9 Partnership & Referral

> Documento di architettura interna del reparto. Descrive forma, gerarchia, flussi, confini e namespace.
> Reparto L2 di 01-AGENCY. Topologia `star`. Standard CF-grade (ADR-007).
> Wrap-non-riscrittura (ADR-003): A9 **avvolge** le skill esistenti `referrals`, `co-marketing`, `icp-radar` — non le riscrive.

---

## 1. Missione e forma del reparto

A9 è la **casa dei lead che nessun altro reparto vuole** e la **fabbrica di pipeline da relazione**.

Tre superfici operative:

1. **Triage non-ICP** — riceve gli scarti/nurture di A1-Ricerca (`AG-A1-QUAL` → "scarta/nurture")
   e decide con esito tracciato: partner potenziale · lead da nurture · archivio.
   Nessun lead muore senza decisione scritta.
2. **Partnership** — identifica, contatta e onboarda partner complementari (agenzie no-AI,
   consulenti HR, commercialisti) con accordo referral **scritto** e commissione **da catalogo**.
3. **Referral pipeline** — ogni lead in arrivo da partner passa dal gate ICP + consenso e viene
   instradato: caldo → A8-Closing (fast-track); da scaldare → A2-Acquisizione.

**Confine netto:** A9 **non chiude** (A8-Closing) e **non fa outreach a freddo su lead finali**
(A2-Acquisizione). A9 possiede la **relazione** e il **consenso**, non la vendita.

**Forma:** star topology attorno ad `AG-A9-COORD`; un unico verifier bloccante (`AG-A9-QA`) su
tutto ciò che esce dal reparto verso A8/A2; frequenza bassa e a onde (non pipeline quotidiana).

---

## 2. Gerarchia interna

```
01-AGENCY (L1) — AG-CONDUCTOR
   └── A9 Partnership & Referral
         │
         AG-A9-COORD (coordinator, sonnet)
         ├── AG-A9-QUALIFY (worker, sonnet)
         │     → triage lead non-ICP da A1 (skill icp-radar)
         │     → partner potenziale / nurture / archivio — esito SEMPRE tracciato
         ├── AG-A9-OUTREACH (worker, sonnet)
         │     → contatta candidati partner (skill co-marketing)
         │     → proposta referral: commissione DA CATALOGO, mai improvvisata
         ├── AG-A9-MGMT (worker, sonnet)
         │     → relazione con partner attivi (skill referrals)
         │     → accordi, briefing ICP, commissioni maturate
         ├── AG-A9-INTEL (worker, haiku)
         │     → referral ricevuti, conversione per partner, commissioni
         │     → misura, non decide
         └── AG-A9-QA (verifier, sonnet)
               → Partner Gate BLOCCANTE: profilo ICP compilato + consenso VERIFICATO
               → nessun lead freddo, nessuna commissione senza contratto firmato
```

**Principio di coordinamento:** `AG-A9-COORD` riceve i segnali (batch non-ICP da A1, segnale
referral da A7, candidato partner) e orchestra. `AG-A9-QA` è l'unico varco verso l'esterno:
nessun lead lascia A9 verso A8/A2 senza PASS.

---

## 3. Roster

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| `AG-A9-COORD` | Coordinatore Partnership | sonnet | Coordina il reparto; possiede la relazione partner a livello strategico; riporta KPI ad AG-DIR |
| `AG-A9-QA` | Verificatore Partner Gate | sonnet | Gate bloccante: profilo ICP compilato + consenso verificato; no lead freddi; no commissioni senza contratto |
| `AG-A9-QUALIFY` | Lead Non-ICP Router | sonnet | Riceve lead non-ICP da A1; decide partner potenziale / nurture / archivio |
| `AG-A9-OUTREACH` | Partner Outreach | sonnet | Contatta candidati partner; proposta referral con commissione da catalogo |
| `AG-A9-MGMT` | Partner Relationship Manager | sonnet | Mantiene partner attivi: accordi, briefing, commissioni, report |
| `AG-A9-INTEL` | Partnership Intelligence | haiku | Monitora referral ricevuti, conversione per partner, commissioni maturate |

---

## 4. Workflow del reparto

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-PARTNER-ONBOARDING** | `workflow/WF-PARTNER-ONBOARDING.md` | Candidato partner → contatto → accordo referral → registrazione → briefing ICP | Accordo scritto firmato; commissione da catalogo; partner briefato |
| **WF-REFERRAL-PIPELINE** | `workflow/WF-REFERRAL-PIPELINE.md` | Lead da partner (`HC-PT-AG-01`) dal ricevimento all'handoff, con ICP + consenso | AG-A9-QA PASS: ICP compilato + consenso verificato |
| **WF-NONICP-ROUTING** | `workflow/WF-NONICP-ROUTING.md` | Lead non-ICP da A1: partner potenziale / nurture / archivio | Decisione tracciata per ogni lead; zero lead persi |

---

## 5. Flussi principali

### 5.1 Onboarding partner (WF-PARTNER-ONBOARDING)

```
[candidato partner: da lead non-ICP (AG-A9-QUALIFY) o ricerca proattiva (A1)]
         │
         ▼
AG-A9-COORD — valuta complementarità (no concorrenti diretti su prodotti DE)
         │
         ▼
AG-A9-OUTREACH — contatto (skill co-marketing) → proposta referral
  → commissione DA CATALOGO (mai negoziata a braccio)
         │
         ▼
AG-A9-MGMT — accordo scritto → registrazione in agency/a9/partners → briefing ICP DE
         │
         ▼
AG-A9-QA — Gate: accordo firmato presente? commissione = catalogo? briefing ICP fatto?
  → PASS: partner ATTIVO, abilitato a inviare referral
  → FAIL: partner resta CANDIDATO; nessun lead accettato da lui
```

### 5.2 Pipeline referral (WF-REFERRAL-PIPELINE)

```
[lead da partner — HC-PT-AG-01]  ·  [segnale referral da A7-Account-Management]
         │
         ▼
AG-A9-MGMT — registra provenienza (partner_id o cliente_id) in agency/a9/referrals
         │
         ▼
AG-A9-QA — GATE BLOCCANTE
  → profilo ICP compilato dal partner? (skill icp-radar)
  → CONSENSO del lead VERIFICATO e datato? (GDPR-light — vedi R3)
  → FAIL: lead respinto al partner; AG-A9-MGMT richiama al briefing
         │
         ▼ PASS
AG-A9-COORD — routing:
  → lead CALDO (ha già chiesto di parlare)  → A8-Closing (fast-track)
  → lead TIEPIDO (da scaldare)              → A2-Acquisizione (outreach su lead consenziente)
         │
         ▼
AG-A9-INTEL — traccia esito; a deal chiuso → commissione maturata (solo con contratto firmato)
```

### 5.3 Routing non-ICP (WF-NONICP-ROUTING)

```
[A1-Ricerca — AG-A1-QUAL: verdetto "scarta" / "nurture"]
         │
         ▼
AG-A9-QUALIFY — triage (skill icp-radar), 3 esiti possibili:
  → PARTNER POTENZIALE (fa un mestiere complementare) → coda WF-PARTNER-ONBOARDING
  → NURTURE (fuori ICP oggi, dentro domani)           → agency/a9/nurture + risveglio programmato
  → ARCHIVIO (mai ICP)                                → agency/a9/archive con motivo
         │
         ▼
caso AMBIGUO → NON archiviare in autonomia → escalation AG-A9-COORD
         │
         ▼
AG-A9-INTEL — % lead con esito tracciato (target 100%)
```

---

## 6. Gate del reparto

| Gate | Owner | Condizione di PASS | Effetto del FAIL |
|---|---|---|---|
| **Partner Gate** | `AG-A9-QA` | Accordo scritto firmato + commissione da catalogo + briefing ICP eseguito | Partner NON attivo; nessun suo lead entra |
| **Referral Gate (ICP)** | `AG-A9-QA` | Profilo ICP compilato su ogni campo obbligatorio | Lead respinto al partner con motivo |
| **Consent Gate (GDPR-light)** | `AG-A9-QA` | Consenso del lead VERIFICATO, datato, con fonte | Lead respinto; MAI passato ad A2/A8 (R3, bloccante) |
| **Commission Gate** | `AG-A9-MGMT` + `AG-A9-QA` | Contratto firmato + deal chiuso confermato da A8 | Nessuna commissione maturata; escalation AG-DIR |
| **Zero-Loss Gate** | `AG-A9-QUALIFY` | 100% lead non-ICP con esito tracciato | Batch non chiudibile finché resta un lead senza esito |

Nessun gate è bypassabile. Un FAIL è un rework, mai un'eccezione.

---

## 7. Handoff in / out

| Direzione | Controparte | Cosa transita | Handoff |
|---|---|---|---|
| ← riceve | A1-Ricerca (`AG-A1-QUAL`) | Lead non-ICP "scarta/nurture" (batch) | input WF-NONICP-ROUTING |
| ← riceve | A7-Account-Management | Segnale referral da cliente attivo | input WF-REFERRAL-PIPELINE |
| ← riceve | Partner esterni | Lead referral con profilo ICP + consenso | `HC-PT-AG-01` |
| → consegna | A8-Closing | Lead partner qualificato e CALDO (fast-track) | post-PASS AG-A9-QA |
| → consegna | A2-Acquisizione | Lead referral TIEPIDO da scaldare | post-PASS AG-A9-QA |
| → consegna | AG-DIR | KPI partnership, commissioni maturate, pipeline referral | report periodico |
| ↔ scambia | A3-Preventivi | Commissione da catalogo (fonte di verità pricing) | lettura catalogo |

**Regola d'oro:** ciò che esce da A9 è già *consenziente e profilato*. Se A2 o A8 devono
"ricostruire il contesto" di un lead A9, il gate ha fallito.

---

## 8. Namespace memoria — `agency/a9/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a9/partners` | Anagrafica partner: `partner_id`, tipo, stato (candidato/attivo/sospeso), accordo, commissione, data briefing | `AG-A9-MGMT` |
| `agency/a9/referrals` | Referral ricevuti: `referral_id`, `partner_id`, ICP status, consenso (flag+data+fonte), routing, esito | `AG-A9-QA` (gate) + `AG-A9-MGMT` |
| `agency/a9/nonicp` | Lead non-ICP in triage: `lead_ref`, verdetto A1, esito A9, motivo, timestamp | `AG-A9-QUALIFY` |
| `agency/a9/nurture` | Lead parcheggiati: `lead_ref`, motivo, data risveglio programmata | `AG-A9-QUALIFY` |
| `agency/a9/commissions` | Commissioni: `partner_id`, `deal_id`, importo da catalogo, stato (maturata/pagata), contratto | `AG-A9-MGMT` |
| `agency/a9/intel` | Metriche: referral/mese, conversione per partner, gate PASS-first-try | `AG-A9-INTEL` |

**Regola PII (bloccante):** negli schemi state si scrivono **riferimenti** (`lead_ref`, `partner_id`),
**mai** PII in chiaro (nome, email, telefono). Il consenso si registra come `consent: {flag, data, fonte}`,
non come copia del dato personale. Vedi `regole/REGOLE.md` R3 e R4, e `state/README.md`.

---

## 9. Integrazione con altri namespace e sistemi

| Namespace / Sistema | Relazione |
|---|---|
| `agency/a1/leads` | Sorgente dei lead non-ICP (verdetto "scarta/nurture" di AG-A1-QUAL) |
| `agency/clients` | AG-A9-MGMT verifica se un referral è già cliente (anti-duplicato/ownership) |
| `agency/a2/pipeline` | Destinazione dei referral tiepidi; check anti-collisione ownership |
| `agency/a8/deals` | Conferma deal chiuso → sblocca maturazione commissione |
| `agency/kpi` | AG-A9-INTEL pubblica i KPI del reparto per AG-DIR |
| Catalogo commissioni (A3-Preventivi) | Fonte di verità: nessuna commissione fuori catalogo |

---

## 10. State e ripartibilità

Ogni esecuzione di workflow scrive uno `state.json` nel namespace di competenza (vedi
`state/README.md`). Campi minimi comuni:
`run_id` · `workflow` · `step_corrente` · `gate_status` (pending/PASS/FAIL + motivo) ·
`last_updated` · `next_action`.

Questo garantisce **ripartibilità a freddo**: un agente rientra dal punto esatto di interruzione
senza riestrarre il contesto (test amnesia V2).

---

## 11. Struct-checklist del reparto

- [x] `README.md` — missione, roster, KPI, handoff
- [x] `ARCHITETTURA.md` — questo file
- [x] `agenti/ag-a9-coord.md` · `ag-a9-qa.md` · `ag-a9-qualify.md` · `ag-a9-outreach.md` · `ag-a9-mgmt.md` · `ag-a9-intel.md` (6/6)
- [x] `workflow/WF-PARTNER-ONBOARDING.md` · `WF-REFERRAL-PIPELINE.md` · `WF-NONICP-ROUTING.md` (3/3)
- [x] `kpi/KPI.md` — KPI con baseline [DM]
- [x] `principi/PRINCIPI.md` — P1..P6
- [x] `regole/REGOLE.md` — R1..R8 bloccanti
- [x] `skills/SKILLS.md` — skill del reparto + mappatura skill esistenti (wrap ADR-003)
- [x] `scripts/README.md` — automazioni ammesse
- [x] `state/README.md` — namespace `agency/a9` + schema FS + lifecycle + accessi
- [ ] Baseline KPI popolate — **[DM]** al primo mese live

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A9`
- [[REGOLE]] · `regole/REGOLE.md` — R1..R8 bloccanti (consenso, catalogo, PII)
- [[WF-REFERRAL-PIPELINE]] · `workflow/WF-REFERRAL-PIPELINE.md`
- [[WF-NONICP-ROUTING]] · `workflow/WF-NONICP-ROUTING.md`
