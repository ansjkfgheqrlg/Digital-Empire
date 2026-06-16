# WF-REVIEW-MAXIMILIAN
## Il passo 5-bis del ciclo a 9 passi — "Max approverebbe questo?"

> Organo: MAXIMILIAN (LX, accanto al Mandato) · Conductor: MX-PRIME · Stato: DEFINED
> Il cuore operativo: un deliverable di fase entra, esce un **verdetto bloccante** nella voce di
> Max. RIFAI = la fase NON si chiude. Come il Gate Bibbia: blocca, non suggerisce.
> Fonte: `12-DOSSIER-MAXIMILIAN.md` §3 · §1 (i test) · §0. Collega: [[10-METODO-CICLO-FASE]] 5-bis.

---

## Trigger
- **Automatico**: ogni fase di costruzione EMPIRE OS, dopo la REVIEW INDIPENDENTE (passo 5) e
  PRIMA del COMMIT (passo 7), da V2-3 in poi. Nessuna fase si chiude senza l'APPROVA dell'organo.
- **Manuale**: Max o il Board chiedono un giudizio di standard su un deliverable già esistente.
- **Natura**: OBBLIGATORIO. Gira SOLO al passo 5-bis e su decisioni che contano — mai ad alto
  volume (è l'organo opus, raro e costoso: §2 dossier, contromisura rischio #2).

---

## Input (JSON)
```json
{
  "review_id": "MX-REV-2026-0617-003",
  "fase_id": "V2-3-MAXIMILIAN",
  "deliverable_ref": "company/MAXIMILIAN/ (struttura prodotta dalla fase)",
  "spec_ref": "company/Memory/checkpoints/CP-20260616-NNN.md#spec",
  "dossier_ref": "PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md",
  "committente": "conductor-di-fase | Board | Max"
}
```
- Se manca `spec_ref` o `dossier_ref` → l'organo NON giudica al buio: ritorna `verdetto=RIFAI`
  con motivo `"manca la fonte di verità — non giudico senza SPEC+dossier"`.

---

## Pipeline (passi · agente owner)
```
1. APERTURA RECORD                       (MX-PRIME)
   └── registra maximilian/verdetti/<review_id> stato=OPEN; carica SPEC + dossier + deliverable.

2. RECUPERO PRECEDENTI                    (MX-MEMORY)
   └── cerca nel corpus i precedenti pertinenti all'oggetto → "Max su questo disse…" (citazioni
        integrali, mai riassunte). Output: corpus_refs[] con riga e citazione.

3. GIUDIZIO PARALLELO (mesh)              (MX-VISION ‖ MX-CRITIC ‖ MX-ANTICIPATE ‖ MX-STYLE ‖ MX-CHALLENGE)
   ├── MX-VISION    → Scala + Ambizione: "è grande quanto dovrebbe? o è un giocattolo?"
   ├── MX-CRITIC    → Standard chirurgico + Visibilità: "un .md per una figura? INACCETTABILE."
   ├── MX-ANTICIPATE→ Anticipazione: "cosa vorrà DOPO? l'hai già preparato?"
   ├── MX-STYLE     → Voce: tono diretto, provocatorio, prove-non-promesse (usa maximilian-voice)
   └── MX-CHALLENGE → "fai di più": "hai fatto solo il chiesto o anche l'ovvio non detto?"
        Ognuno applica i propri test §1 e ritorna rilievi:[{test, esito PASS|FAIL, prova, citazione}].

4. TRIAGE MINUZIE                         (MX-FAST)
   └── scarta i rilievi-minuzia (dettagli rimandabili, ADR-005) → vanno in BACKLOG, NON bloccano.
        Tiene solo i FAIL che toccano scala/standard/visibilità/voce (i bloccanti).

5. APPLICA IL GATE                        (MX-PRIME → maximilian-standard-gate)
   └── esegue la checklist binaria del gate: 1 solo FAIL bloccante non risolto = RIFAI.

6. SINTESI NELLA VOCE DI MAX              (MX-PRIME)
   └── compone il verdetto unico, diretto, con motivi citati dal corpus + cosa Max vorrebbe in più.
        Marca record CLOSED, scrive l'esito in maximilian/verdetti/<review_id>.
```

---

## Gate
- **G-MX1 (blocco cardine):** ≥1 test §1 con esito FAIL bloccante (non-minuzia) → `verdetto=RIFAI`.
  La fase TORNA al passo 3 BUILD coi motivi. Non si commita un RIFAI. Determinato da `maximilian-standard-gate`.
- **G-MX2 (no-giudizio-al-buio):** manca SPEC o dossier → RIFAI con motivo, non si prosegue (deriva da G-ARCH4 spirit).
- **G-MX3 (loop-guard):** stesso FAIL bloccante 2 review di fila → STOP + escala a Max (decisione o ADR), debito registrato in maximilian/calibrazione.
- **G-MX4 (voce):** la sintesi NON suona come Max (gentile/da-Claude) → MX-STYLE rimanda a MX-PRIME prima dell'output (contromisura rischio #1 dossier).

---

## Output (JSON)
```json
{
  "review_id": "MX-REV-2026-0617-003",
  "fase_id": "V2-3-MAXIMILIAN",
  "verdetto": "APPROVA | RIFAI",
  "motivi": [
    "MX-CRITIC: il reparto X è un singolo .md — INACCETTABILE, serve team+workflow (corpus §32-34)"
  ],
  "cosa_max_vorrebbe_in_piu": [
    "MX-ANTICIPATE: dopo questo vorrà i 2 workflow di calibrazione già scaffoldati"
  ],
  "minuzie_in_backlog": ["naming di un sotto-file da uniformare"],
  "corpus_refs": ["direttiva-20260611-scala-v2.md:22-27"],
  "torna_a_passo": 3,
  "verdetto_tracciato": "maximilian/verdetti/MX-REV-2026-0617-003"
}
```
- `verdetto=APPROVA` → `torna_a_passo: null`, si procede al COMMIT (passo 7).
- `verdetto=RIFAI` → `torna_a_passo: 3`, la fase rientra in BUILD coi `motivi`.

---

## Innesto nel ciclo 9 passi
Passo **5-bis** ([[10-METODO-CICLO-FASE]]): dopo la REVIEW INDIPENDENTE (5, sostanza vs dossier)
e prima del COMMIT (7). Mandato e MAXIMILIAN sono complementari: Mandato = "è LECITO?", MAXIMILIAN
= "è all'ALTEZZA?". Un output può essere lecito ma bocciato qui, e viceversa (§6 dossier). Da V2-3
lo applica questo workflow; prima lo faceva il conductor a mano sui tratti del corpus.

---

## Dry-run
Test reale (DONE WHEN §0.7): entra un deliverable v1 "fatto giusto per farlo" — un reparto =
un solo file markdown. MX-MEMORY recupera dal corpus *"il reparto ricerca è un semplice file
markdown… INACCETTABILE… serve un TEAM di agenti (6-10) e un workflow"* (§32-38). MX-CRITIC FAIL
su Standard+Visibilità, MX-VISION FAIL su Scala, MX-FAST conferma che NON è minuzia. MX-PRIME →
`verdetto=RIFAI`, motivo nella voce di Max, `torna_a_passo:3`. Record ricostruibile a freddo da
`maximilian/verdetti/<review_id>` (test-amnesia §8). L'organo BOCCIA come Max.

---

## Connessioni
- [[WF-ANTICIPAZIONE]] — gira a inizio fase; i suoi brief diventano gli slot che qui si verificano
- [[maximilian-standard-gate]] — la checklist binaria eseguita al passo 5
- [[maximilian-voice]] — usata da MX-STYLE (passo 3) e MX-PRIME (sintesi passo 6)
- [[10-METODO-CICLO-FASE]] passo 5-bis — il punto d'innesto nel ciclo a 9 passi
- [[12-DOSSIER-MAXIMILIAN]] §1 (i test) · §3 (questo workflow) · §8 (state/namespace verdetti)
- ADR-006 (ciclo 9 passi) · ADR-007 (pivot V2, istituisce l'organo) · ADR-005 (minuzie → BACKLOG)
