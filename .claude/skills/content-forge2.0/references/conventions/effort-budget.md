# Budget di sforzo: segue il riuso, non la dimensione

> Regola di allocazione dello sforzo computazionale. La legge ogni builder **prima** di scegliere
> modello/tier per uno step, insieme ad `anti-patterns.md`.

## La domanda che si fa prima di scegliere il tier

**"Quante volte questo artefatto verra' riletto da qui in avanti?"**

Non "quanto e' grande il task". Il costo di un artefatto fatto male non si paga una volta: si paga a
ogni riuso.

| Tipo di artefatto | Sforzo |
|---|---|
| **Usa-e-getta** — output di una singola run, bozza intermedia, scratch | tier normale |
| **Riusato indefinitamente** — `SKILL.md`, file in `references/`, token di brand, system prompt, schema, MKD canonico | massimo sforzo, una volta sola |

Il criterio della fonte, testuale: *"se lo fai male, lo paghi ogni volta che lo usi"*.

## Dentro un task multi-step: lo sforzo va sulla validazione

Il massimo sforzo non si spalma su tutti gli step. Va sullo step che **valida**, non su quello che
**produce**. Nella pipeline osservata alla fonte, il parametro "effort max" era applicato solo allo
step di validazione, mentre lo step successivo di generazione del PDF finale girava a sforzo normale.

Tradotto in Content Forge: gli stage di CRITIQUE, coverage e schema-validation meritano il tier alto
piu' di quanto lo meriti lo stage che scrive la prima bozza.

## Perche' e' un asse diverso da quelli gia' in casa

Digital Empire alloca gia' su due criteri — il routing a 3 tier (Haiku/Sonnet/Opus) e la gerarchia
forze scagnozzo/sentinella/doom bot (ADR-015) — ed entrambi guardano il **grado del compito**. Questa
regola aggiunge un secondo asse, **la vita dell'artefatto**, che i due precedenti non coprono: un
compito piccolo che produce un file letto per sempre sta in basso sul primo asse e in alto su questo.

Fonte: studio Andrei Pascu, cs2online Lezione 6 (KA-04, workflow PDF->JSON osservato per intero ai
frame t9m15s / t10m15s / t10m45s) e cs2online Bonus 6 (KA-08, "effort max" applicato solo allo step
di validazione, frame t19m30s) — candidato AP-019, innestato 2026-09-10.
