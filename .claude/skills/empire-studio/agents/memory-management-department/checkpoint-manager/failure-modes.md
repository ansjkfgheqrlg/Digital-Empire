# checkpoint-manager - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| CP mancante | step senza traccia | post-azione obbligatorio | gap nei CP | CP retroattivo |
| Senza trace | CP non tracciabile | trace richiesta | campo vuoto | aggiungi trace |
| Numerazione rotta | CP fuori sequenza | next_number robusto | salti | rinumera/append |
| Nome non-safe | file problematico | slug del manager | validator | rigenera |
| INDEX non aggiornato | CP non in index | append automatico | mismatch | --index |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
