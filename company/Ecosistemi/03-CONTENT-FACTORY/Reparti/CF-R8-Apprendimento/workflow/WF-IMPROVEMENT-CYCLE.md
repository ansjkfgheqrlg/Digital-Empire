---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R8 #improvement-cycle #pattern #fix #adr #forge #apprendimento #mensile
Created: 2026-06-30
Last updated: 2026-06-30
---

# WF-IMPROVEMENT-CYCLE — Ciclo Mensile di Miglioramento Strutturato

> **Reparto:** CF-R8 Apprendimento & Ottimizzazione · **Area:** Post-Produzione
> **Cadenza:** Mensile (ciclo 4 settimane di osservazione post-implementazione)
> **Gate bloccante:** nessuna modifica strutturale senza approvazione CF-Director; ogni proposta tracciabile in `cf/improvements`

---

## Scopo

Trasformare i pattern distillati in WF-PATTERN-DISTILLATION in miglioramenti concreti,
approvati, implementati e misurati. Il ciclo dura un mese: dalla proposta all'implementazione,
più 4 settimane di osservazione per verificare l'effetto. Nessun improvement viene dichiarato
"completato" senza misura reale del delta KPI.

---

## Passi del workflow

| # | Passo | Agente | Timing | Input | Output | Gate / Condizione |
|---|---|---|---|---|---|---|
| 0 | Verifica slot disponibili | CF-R8-COORD | Inizio ciclo mensile | `cf/improvements` stato attuale | Slot liberi (max 3 improvement attivi) | Blocco se già 3 attivi; segnalazione a L1-POST |
| 1 | Aggregazione top-3 problemi | CF-R8-COORD | Prima settimana del mese | Patterns da WF-PATTERN-DISTILLATION + WF-QUALITY-AUDIT CF-R6 | Lista top-3 ordinata per impatto atteso (n_occorrenze × gravità_gate) | Solo problemi con ≥1 pattern confermato a supporto |
| 2 | Formulazione proposta fix | CF-R8-REASONING | Prima settimana del mese | Top-3 problemi | Lista proposte con `{lezione, reparto_destinatario, fix_proposto, tipo_fix, verifica_attesa, pattern_ids}` | Max 3 proposte; tipo_fix: puntuale/strutturale/architetturale |
| 3 | Presentazione a CF-Director | CF-R8-COORD | Fine prima settimana | Liste proposte | Report decisionale per CF-Director con impatto stimato | Gate: BLOCCO se CF-Director non approva — nessuna implementazione senza ok esplicito |
| 4 | Tracking in `cf/improvements` | CF-R8-COORD | Post-approvazione | Proposta approvata | Entry in `cf/improvements` con stato "approvato" | Ogni improvement ha un id, reparto, fix, verifica_attesa, ts_approvazione |
| 5 | Implementazione | Reparto destinatario / 07-FORGE | Seconda settimana | Spec fix approvata | Fix implementato (reparto) o skill creata/modificata (07-FORGE) | CF-R8-COORD traccia stato "in_implementazione"; non implementa direttamente |
| 6 | Osservazione 4 settimane | CF-R8-COORD | Settimane 2-5 | `cf/failures` + metriche CF-R6 post-implementazione | Log settimanale n_occorrenze del pattern corrispondente | Osservazione passiva: CF-R8-COORD non interviene; registra solo |
| 7 | Validazione effetto | CF-R8-QA | Fine settimana 5 | Delta KPI prima/dopo (first-pass rate, n_occorrenze pattern) | Verdetto: RISOLTO / PARZIALE / RECIDIVA | Gate: il delta deve essere calcolato su dati reali (≥2 misurazioni); non su stime |
| 8 | Chiusura o escalation | CF-R8-COORD | Post-validazione | Verdetto CF-R8-QA | Aggiornamento `cf/improvements` + `cf/failures` status | RISOLTO → status "RISOLTO"; RECIDIVA → escalation L1-POST + riavvio analisi |
| 9 | Neural feeding (asincrono) | CF-R8-NEURAL | Post-chiusura (se soglia ok) | Pattern validati in `cf/patterns` | Sessione `neural_train` | Solo se CF-R8-COORD autorizza (dati sufficienti) |

---

## Topologia del ciclo

```
INIZIO MESE
     │
CF-R8-COORD: verifica slot (≤3 improvement attivi)
     │
     ▼
CF-R8-COORD: aggrega top-3 problemi
   (da cf/failures CONFERMATI + WF-QUALITY-AUDIT CF-R6)
     │
     ▼
CF-R8-REASONING: proposta fix per ogni problema
   tipo_fix: puntuale | strutturale | architetturale
     │
     ▼
CF-R8-COORD → CF-Director: presentazione + approvazione
     │ APPROVAZIONE
     ▼
Apertura entry in cf/improvements (stato: "approvato")
     │
     ▼
Reparto destinatario / 07-FORGE: implementazione
     │
     ▼
4 settimane di osservazione (CF-R8-COORD monitora cf/failures)
     │
     ▼
CF-R8-QA: validazione delta KPI
     │         │
     │ RISOLTO │ RECIDIVA o PARZIALE
     │         ▼
     │    Escalation a L1-POST
     │    + riavvio analisi causa radice
     ▼
Chiusura improvement (status: "RISOLTO")
     │
     ▼ (se dati sufficienti)
CF-R8-NEURAL: feeding neural_train
     │
FINE CICLO
```

---

## Gate 3: Approvazione CF-Director (non bypassabile)

**Ogni proposta di fix richiede approvazione esplicita di CF-Director prima dell'implementazione.**

Il CF-Director riceve un report decisionale che include:
- Il problema (pattern_id di riferimento, n_occorrenze, gate coinvolto).
- La proposta fix (cosa cambia, dove, come).
- Il tipo di fix (puntuale / strutturale / architetturale).
- La verifica attesa (quale KPI si misura, in quale timeframe).
- L'impatto atteso (ripetuto senza esagerazioni: "riduzione attesa di [pattern] in 30gg").

**CF-Director può:**
- Approvare → improvement aperto e tracciato.
- Rifiutare con motivazione → proposta archiviata in `cf/improvements` con stato "rifiutato".
- Richiedere modifica → CF-R8-REASONING riformula; nuova presentazione.

**CF-Director NON può:**
- Approvare più di 3 improvement contemporaneamente (limite di CF-R8-COORD).
- Approvare proposte senza pattern_id di riferimento (nessun improvement senza evidenza).

---

## Gate 7: Validazione effetto (criteri CF-R8-QA)

CF-R8-QA valida il miglioramento a fine ciclo di osservazione.

| Scenario | Criteri | Verdetto | Azione |
|---|---|---|---|
| RISOLTO | Il pattern di failure corrispondente non si ripresenta in 4 settimane (0 nuove occorrenze) | RISOLTO | `cf/failures` → status "RISOLTO"; `cf/improvements` → stato "chiuso" |
| PARZIALE | Il pattern si riduce ma non si azzera (n_occorrenze_post < n_occorrenze_pre) | PARZIALE | Mantiene "in_osservazione" per altre 4 settimane; nuova validazione |
| RECIDIVA | Il pattern si ripresenta con n_occorrenze_post ≥ n_occorrenze_pre | RECIDIVA | Escalation a L1-POST; riavvio analisi causa radice (il fix non ha risolto) |

**Invariant:** il delta KPI deve essere calcolato su ≥2 misurazioni reali (una prima,
una dopo). CF-R8-QA FAIL se il delta è presunto o basato su una sola misurazione.

---

## Classificazione tipo_fix e destinatario

| Tipo | Definizione | Destinatario | Tempi tipici |
|---|---|---|---|
| Puntuale | Modifica a un prompt, a un parametro, o a un check esistente | Reparto corrispondente (CF-R1, CF-R4, CF-R5…) | 1-3 giorni |
| Strutturale | Nuova skill, nuovo agente, o modifica a un workflow CF-grade | 07-FORGE (via CF-Director) | 1-3 settimane |
| Architetturale | Modifica al contratto di ordine, alla gerarchia, o a un invariant | Board (via ADR-bozza approvata da CF-Director) | 2-6 settimane |

---

## Schema `cf/improvements` (entry per improvement)

```json
{
  "improvement_id": "IMP-R8-2026-06-001",
  "pattern_id_riferimento": "PAT-R8-FAILURE-COPY-HOOK-001",
  "problema": "hook_type non obbligatorio in brief.json — Gate-COPY FAIL per hook assente (5 occorrenze giugno 2026)",
  "proposta_fix": "Aggiungere hook_type come campo obbligatorio in brief.json; gate CF-R1-QA blocca brief privi di hook_type",
  "tipo_fix": "puntuale",
  "reparto_destinatario": "CF-R1",
  "verifica_attesa": "Riduzione Gate-COPY fail rate per criterio hook nei 30gg successivi",
  "stato": "approvato | in_implementazione | in_osservazione | chiuso | rifiutato",
  "ts_proposta": "2026-06-30T12:00:00Z",
  "ts_approvazione": "2026-06-30T14:00:00Z",
  "ts_implementazione": null,
  "ts_chiusura": null,
  "verdetto_finale": null,
  "delta_kpi_misurato": null,
  "note": ""
}
```

---

## Esempio operativo end-to-end (ciclo luglio 2026)

**Passo 0 — Verifica slot:** `cf/improvements` ha 1 improvement attivo (IMP-R8-2026-05-001 in osservazione).
Slot disponibili: 2. CF-R8-COORD apre il ciclo.

**Passo 1 — Top-3 problemi:**
1. PAT-R8-FAILURE-COPY-HOOK-001 (n=5, Gate-COPY, impatto alto).
2. PAT-R8-ENGINE-CANVA-CAROSELLO-001 (n=3, routing engine, impatto medio).
3. PAT-R8-FAILURE-BRAND-PALETTE-001 (n=3, Gate-BRAND, impatto medio).
(Solo 2 nuovi improvement apribili — si selezionano i top-2 per impatto.)

**Passo 2 — CF-R8-REASONING:** proposta per PAT-R8-FAILURE-COPY-HOOK-001: fix puntuale → CF-R1.
Proposta per PAT-R8-ENGINE-CANVA-CAROSELLO-001: fix puntuale → CF-R5 routing.

**Passo 3 — CF-Director:** approva entrambe le proposte.

**Passo 4 — Tracking:** IMP-R8-2026-07-001 (hook) e IMP-R8-2026-07-002 (routing) aperti.

**Passo 5 — Implementazione:** CF-R1 aggiorna gate WF-BRIEF in 2 giorni.
CF-R5 aggiorna routing capability→engine in 1 giorno.

**Passi 6-7 — Osservazione 4 settimane:** CF-R8-COORD monitora `cf/failures`.
Fine settimana 5: IMP-R8-2026-07-001 → 0 nuove occorrenze hook fail → CF-R8-QA: RISOLTO.
IMP-R8-2026-07-002 → riduzione n_rework Puppeteer carosello → CF-R8-QA: RISOLTO.

**Passo 8 — Chiusura:** entrambi gli improvement → stato "chiuso". `cf/failures` → status "RISOLTO".

**Passo 9 — Neural:** CF-R8-COORD autorizza CF-R8-NEURAL → 4 pattern in training.

---

## Regole di esecuzione (non negoziabili)

1. **Max 3 improvement attivi** — non si apre un nuovo improvement se già 3 sono in corso.
2. **Ogni proposta tracciabile** — nessun fix implementato senza entry in `cf/improvements`.
3. **Nessuna modifica strutturale senza approvazione** — CF-Director deve approvare prima
   dell'implementazione; il reparto destinatario non riceve la spec senza approvazione.
4. **ADR se architetturale** — ogni improvement di tipo "architetturale" genera un ADR-bozza
   prima di procedere; l'improvement non parte finché il Board non approva l'ADR.
5. **Validazione su dati reali** — CF-R8-QA non emette verdetto RISOLTO senza ≥2 misurazioni
   reali (prima e dopo l'implementazione); i delta stimati non sono accettati.

---

## Connessioni

- [[cf-r8-coord]] · `agenti/cf-r8-coord.md` — orchestra l'intero ciclo; apre e chiude le entry cf/improvements
- [[cf-r8-qa]] · `agenti/cf-r8-qa.md` — valida l'effetto del miglioramento (passo 7)
- [[WF-PATTERN-DISTILLATION]] · `workflow/WF-PATTERN-DISTILLATION.md` — produce i pattern che alimentano questo WF
