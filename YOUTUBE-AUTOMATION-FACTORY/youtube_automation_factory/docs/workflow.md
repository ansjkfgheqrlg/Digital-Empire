# Workflow

## Percorso completo

```
DISCOVERED
  → UNDER_REVIEW                          ReviewAgent verifica dati e nicchia
    → NEEDS_MORE_DATA                     mancano campi: torna agli operativi
    → REJECTED                            fuori nicchia
    → APPROVED_AS_REFERENCE               richiede approvazione SENIOR
      → SCRIPT_DRAFT                      ScriptAgent scrive brief e script originale
        → SCRIPT_PENDING_APPROVAL
          → SCRIPT_APPROVED               richiede originalita' + approvazione SENIOR
            → PRODUCTION_PENDING          richiede script approvato
              → IN_PRODUCTION
                → VIDEO_READY_FOR_QA
                  → COPY_DRAFT
                    → COPY_PENDING_DIGITAL_EMPIRE_REVIEW
                      → COPY_APPROVED     richiede l'esito della revisione esterna
                        → THUMBNAIL_DRAFT
                          → THUMBNAIL_PENDING_REVIEW
                            → THUMBNAIL_APPROVED  richiede originalita' + brief
                              → QUALITY_CONTROL
                                → COMPLETED       richiede TUTTI i requisiti
```

Da qualunque stato si puo' passare a `BLOCKED`. Da `BLOCKED` si torna solo a uno stato di
lavorazione, e solo dopo che un regolatore ha verificato che le cause non ci sono piu'.

`COMPLETED` e `REJECTED` sono terminali: `ALLOWED_TRANSITIONS` non ha successori per loro.

## Transizioni non valide

Sollevano `InvalidTransitionError` **e** registrano un evento `transition_rejected`: un
tentativo respinto resta tracciato. Lo stato non cambia.

## Requisiti per `COMPLETED`

`validate_ready_for_completion()` richiede, tutti insieme:

* job di produzione presente, con **sottotitoli abilitati**;
* script approvato;
* copy presente, con originalita' verificata, **approvato da Digital Empire** e `approved=True`;
* copertina presente, con originalita' verificata, brief presente e `approved=True`.

Se manca anche una sola voce, la transizione solleva `RegulatoryBlockError` con l'elenco
completo dei motivi — non con il primo trovato.

## Il registro eventi

Ogni `WorkflowRun` accumula `WorkflowEvent` immutabili (`frozen=True`) con attore, livello,
azione, stati di partenza e arrivo, motivazione e istante. Il report finale li elenca tutti:
serve a ricostruire chi ha fatto cosa, comprese le azioni respinte.

## Il workflow dimostrativo

`demo.py` esegue l'intero percorso con dati locali e adapter mock. Con `complete=False`
(`yaf run-demo --stop-before-copy-review`) si ferma prima della revisione esterna, per mostrare
che il workflow **non** si chiude senza di essa: il comando esce con codice `2`.
