# Processo di approvazione

## Le tre firme

Nessun contenuto arriva alla pubblicazione senza tre passaggi distinti:

1. **esegue** un agente operativo (L2);
2. **approva** il livello competente (revisore o senior);
3. **non hanno bloccato** i regolatori.

## Approvazioni registrate

Ogni decisione formale diventa un `Approval` con: soggetto, decisione, autore, **livello**
dell'autore e motivazione. `record_approval()` verifica il livello *prima* di registrare, quindi
non esiste un'approvazione salvata senza autorizzazione.

`WorkflowRun.has_senior_approval(subject_id)` cerca specificamente un'approvazione di livello
`SENIOR`: un'approvazione di un revisore non soddisfa il requisito, ed esiste un test dedicato
(`test_approvazione_di_un_revisore_non_basta`).

## Dove le approvazioni bloccano davvero

`YouTubeFactoryWorkflow._check_preconditions()` applica i vincoli:

| Transizione verso | Richiede |
|---|---|
| `APPROVED_AS_REFERENCE` | candidato presente **e** approvazione senior |
| `SCRIPT_APPROVED` | `originality_checked=True` **e** approvazione senior |
| `PRODUCTION_PENDING` | script con `approved=True` |
| `COPY_APPROVED` | `digital_empire_status=APPROVED` |
| `THUMBNAIL_APPROVED` | `originality_checked=True` **e** brief presente |
| `COMPLETED` | tutti i requisiti di `validate_ready_for_completion()` |

## Rifiuti

Un rifiuto e' un `Approval` con `decision=REJECTED` e una motivazione obbligatoria: il campo
`reason` non ammette stringhe vuote. Il livello senior spiega **quali criteri** non sono stati
superati, non un giudizio generico.

## Revisione esterna del copy

Il copy attraversa uno stato dedicato, `COPY_PENDING_DIGITAL_EMPIRE_REVIEW`. Il modello
`CopyAsset` rifiuta `approved=True` finche' `digital_empire_status` non e' `APPROVED`: il
vincolo vale anche se qualcuno tenta di forzare il campo direttamente.
