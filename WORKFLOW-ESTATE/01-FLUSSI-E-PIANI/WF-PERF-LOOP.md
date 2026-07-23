# ⚡ WF-PERF-LOOP — il micro-ecosistema di performance (ciclo confermato)
> Richiesta Max (21/07): **ogni azione del workflow, ogni singola volta**, viene analizzata (debug + soluzione + struttura + modifiche), salvata in uno spazio dedicato della memoria, studiata da agenti specifici che emettono **micro-input** verso gli altri agenti — e il miglioramento deve essere **confermato**, non auspicato.
> Posizione: gira DOPO ogni azione, trasversale a tutti i WF (S1..S6, MEM-*, MASTER). Sponsor: TRUTH-CMD · Esecuzione: Performance Cell (`empire/inspect/`).

## 1. IL CICLO (T0 → T5, chiuso e confermato)

```
T0 AZIONE CHIUSA ──(post-task hook del router)──►
T1 CAPTURE    perf-collector scrive PERF record in company/Ispettorato/telemetry/runs/
              ⚠️ scrittura diretta su file: NON consuma la quota 30 msg/giorno
      │
T2  ANALYZE   perf-analyst legge il record ENTRO L'EOD e compila la scorecard 5D:
              ① correctness/debug (errori, retry, escalation)  ② qualità soluzione
              ③ struttura risposta/artefatto  ④ scope-fit (DoD rispettata?)
              ⑤ efficiency (TTD vs benchmark di ruolo)  + gate: traceability (CP presente?)
      │
T3  SYNTHESIZE segnale nuovo → pattern candidato (ReasoningBank DRAFT)
               segnale già visto → +1 ricorrenza (contatore sul pattern)
      │
T4  DISPATCH   feedback-dispatcher emette micro-output MIRATI (via board, FB-* in memoria):
              · TIP → all'agente coinvolto (micro-input: "la prossima volta fai X")
              · RULE-NOTE → al regolatore (se una regola intralcia il lavoro reale)
              · MUTATION-PROP → al comandante di casta (se lo stesso problema ricorre ≥3x)
              regola anti-nagging: stesso TIP, stesso agente → non ripetere entro 3 task
      │
T5  CONFIRM   alla PROSSIMA performance della stessa famiglia-task dell'agente:
              ✅ problema NON ricorre → FB → status: confirmed → pattern → ReasoningBank UFFICIALE
              ❌ problema ricorre    → FB → status: recurred  → escalation automatica:
                                        mutation obbligatoria del prompt (v4) o pairing repair
```

**Il punto chiave ("ciclico confermato")**: un miglioramento ESISTE solo quando T5 lo conferma. Un TIP senza conferma alla performance successiva non è un miglioramento: è un suggerimento. Il loop tiene i conti.

## 2. LO SCHEMA — Performance Record (`company/Ispettorato/telemetry/runs/RUN-PERF-*.json` / memoria)

```yaml
agente / task / wf / esito (success|partial|failed)
timestamps → TTD calcolato
debug: {errori, retry, escalation, fix applicati}
output_ref: path artefatto prodotto
verification: {verificatore, first_pass: bool, note}
scorecard 5D: correctness·solution·structure·scope-fit·efficiency (1-5) + gate traceability
feedback_collegati: [FB-ids]   # chiusura loop T5: confirmed | recurred
```

Comando: `python -m empire inspect capture --agent <id> --task <id> --wf <WF> --family <f> --result success --started <iso> --ended <iso>`

## 3. LO SCHEMA — Feedback Record (in memoria centrale, kind feedback)

```yaml
tipo: TIP | RULE-NOTE | MUTATION-PROP
da: feedback-dispatcher (su analisi di perf-analyst)
a: agente | regolatore | comandante
micro-input: "..."            # piccolo, azionabile, da ricordare
su_performance: PERF-id
status: open → acked (obbligatorio) → confirmed | recurred
```

Comando: `python -m empire inspect dispatch`

## 4. REGOLE DI CONVIVENZA (con l'ecosistema v4)
1. **P-LOOP non è un verificatore**: non blocca nulla, non ha gate. Analizza DOPO, non giudica PRIMA. (Casta distinta dai verificatori — che approvano l'output; il loop migliora l'attore.)
2. **Budget rumore**: capture=T1 fuori quota (file write); TIP/RULE-NOTE = P3 (vanno nel digest EOD); MUTATION-PROP = P2 (4h hold). Max riceve la sintesi del loop SOLO nel digest e al COUNCIL.
3. **Niente surveillance-state**: i punteggi 5D servono a migliorare il SISTEMA (prompt, regole, assegnazioni), non a punire. Feed negativi → causano mutation del PROMPT, mai "colpa" (coerente con failure-modes come first-class).
4. **Chiusura garantita**: se un FB resta >5 task senza conferma/ricorrenza → TRUTH-CMD lo riesuma in EOD-SYNC (task marcio).
5. **ReasoningBank è il deposito finale**: solo i pattern `confirmed` entrano come ufficiali e vengono precaricati dal pre_task hook nei task futuri della stessa famiglia. È qui che il miglioramento diventa memoria operativa.

## 5. ESEMPI CONCRETI (dal workshop reale)
- forge-builder chiude la landing S2 → PERF: TTD 3h, first-pass NO (checkout rotto al test €1), debug: fallback Gumroad usato. → perf-analyst: structure OK, correctness −1 setup KYC, scope-fit OK. → dispatcher: TIP a funnel-engineer "test €1 SEMPRE prima di dichiarare live" + pattern DRAFT "Stripe KYC lento → aprire Gumroad in parallelo il giorno prima". Alla prossima prima-pass ✅ su WF-S6 landing → FB confirmed → pattern ufficiale.
- closer-ops invia follow-up → PERF: esito success ma 2h dopo la finestra (cadence). → TIP: "contatti S1 solo nelle finestre 9:30/18:00". Ricorre ancora → 3ª ricorrenza → MUTATION-PROP a REVENUE-CMD: inserire le finestre nel system-prompt di closer-ops.

## 6. ATTIVAZIONE
- **Ora (file-based)**: ogni reparto emette `perf` a chiusura task (l'hook è nel post_task di workflows.yaml); la Performance Cell analizza in EOD (T2–T4) e conferma alla next run (T5).
- **F5/F6 (runtime)**: il router invoca T1 automaticamente su `post_task`; T5 schedulato su ogni nuovo PERF della stessa famiglia.
- Validazione: ogni domenica al COUNCIL — tabella "TIP confermati vs ricorsi" = il vero termometro del miglioramento ciclico.

---
⛓️ Trace P12: `WF-PERF-LOOP#estate-2026` · input: direttiva Max 21/07 · aggancia: v4-MASTER §7 (punto 8) · agenti: empire/inspect/ · storage: company/Ispettorato/telemetry + memory
