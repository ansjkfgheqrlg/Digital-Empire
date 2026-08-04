# Architettura

## Struttura

```
config/settings.py      impostazioni da ambiente (.env), nicchia primaria, selettori
src/youtube_automation_factory/
  core/                 modelli, stati, regole, persistenza, report
    enums.py            WorkflowState, AgentLevel, esiti
    models.py           modelli Pydantic v2 con i vincoli codificati nei tipi
    workflow.py         grafo delle transizioni + precondizioni di dominio
    approvals.py        gerarchia applicata: require_level(), record_approval()
    validators.py       verifiche riusabili (restituiscono i motivi di blocco)
    repositories.py     persistenza (in memoria, file JSON)
    reporting.py        report Markdown
    exceptions.py       un tipo per ogni regola violabile
  agents/               un file per agente, con il livello dichiarato
  automation/           client Playwright configurabili (YouTube, Arena)
  integrations/         adapter di produzione video (astratto + mock)
  services/             OriginalityService
  demo.py               workflow dimostrativo end-to-end
  cli.py                interfaccia a riga di comando
```

## Principi

**Le regole stanno nel codice, non solo nella documentazione.** Un modello che accettasse
`derived_from_transcript=True` renderebbe la regola "non copiare" una raccomandazione: il
validatore la rifiuta, quindi e' un vincolo.

**Chi verifica non approva.** `require_level()` nega al livello regolatorio le azioni
`approve_*` e a tutti gli altri `block_workflow`.

**Un errore esplicito e' meglio di un dato falso.** I client Playwright senza selettori
configurati sollevano `AutomationNotConfiguredError` invece di tentare: un selettore obsoleto
non fallisce in modo visibile, restituisce dati sbagliati.

**Cio' che non si sa non si stima.** Transcript non recuperato: `available=False` e una nota.
CTR e retention: dichiarati fra i `data_gaps`.

## Configurazione dei selettori

I selettori arrivano come JSON in una variabile d'ambiente. Chiavi attese:

**`YAF_YOUTUBE_SELECTORS`**

| Chiave | Uso |
|---|---|
| `video_card` | contenitore di un risultato di ricerca |
| `title` | titolo (e `href` del video) dentro la card |
| `channel` | nome del canale dentro la card |
| `views` | testo delle visualizzazioni dentro la card |
| `transcript_button` | apre il pannello del transcript (opzionale) |
| `transcript_segment` | singolo segmento del transcript (opzionale) |

**`YAF_ARENA_SELECTORS`**: `prompt_input`, `submit_button`, `result_image`.

Non sono precompilati di proposito: vanno rilevati e verificati sull'interfaccia reale.

## Estendere il sistema

* **Nuovo agente**: sottoclasse di `BaseAgent`, dichiara `level`, chiama `authorize()` nei
  metodi riservati.
* **Nuovo stato**: aggiungerlo a `WorkflowState` **e** a `ALLOWED_TRANSITIONS` — un test
  verifica che ogni stato sia mappato.
* **Adapter di produzione reale**: implementare `FlikAdapter` e registrarlo in `get_adapter()`.
  Il resto del sistema non cambia.
