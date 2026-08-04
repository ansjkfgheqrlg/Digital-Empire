# YouTube Automation Factory

Fabbrica multi-agentica per la produzione di contenuti YouTube **originali**, con gerarchia
decisionale, workflow di approvazione e controlli regolatori **applicati dal codice** — non
soltanto descritti nella documentazione.

La nicchia operativa e' **Dose Mentale**, ed e' protetta: nessun agente operativo, revisore o
di produzione puo' cambiarla durante un workflow.

## Posizione sui contenuti di terzi

I video dei competitor sono **riferimenti analitici**. Se ne studiano tema, concetti trattati e
bisogni dell'audience per capire cosa interessa al pubblico. **Non** se ne replicano transcript,
script, copy, titoli o copertine.

Questa non e' solo una dichiarazione d'intenti: i modelli rifiutano di costruire uno script
marcato come derivato dal transcript (`derived_from_transcript=True`), una copertina marcata
come replica di layout altrui (`replicates_competitor_layout=True`) o un candidato non marcato
come riferimento (`reference_only=False`).

## Prerequisiti

* Python **3.11+**
* `pip`
* (solo per le integrazioni browser reali) Playwright e i suoi browser

## Installazione

```bash
cd youtube_automation_factory
python -m pip install -e ".[dev]"          # progetto + strumenti di sviluppo
python -m pip install -e ".[dev,browser]"  # in piu' Playwright
python -m playwright install chromium       # browser, solo se serve l'automazione reale
```

## Configurazione

```bash
cp .env.example .env
```

`.env` **non e' versionato** (`.gitignore`). Il file `.env.example` e' un template senza valori
sensibili: non contiene ne' deve contenere chiavi, token o credenziali.

I selettori CSS di YouTube e Arena **non hanno valori predefiniti**, per scelta. Il layout di
quelle pagine cambia nel tempo: un selettore obsoleto non fallisce in modo visibile, restituisce
dati *sbagliati*. Senza selettori configurati i client sollevano `AutomationNotConfiguredError`
invece di tentare comunque.

Configurare Playwright **senza mettere credenziali nel repository**:

1. i selettori si passano come JSON in `YAF_YOUTUBE_SELECTORS` / `YAF_ARENA_SELECTORS`;
2. se serve una sessione autenticata, si usa un profilo browser persistente indicato da
   `YAF_BROWSER_PROFILE_DIR`, che punta a una cartella **fuori** dal repository (le cartelle
   di profilo sono comunque escluse da `.gitignore`);
3. il login si esegue a mano una volta in quel profilo. Il codice non automatizza login, non
   gestisce credenziali e non aggira CAPTCHA o controlli di accesso.

## Uso della CLI

```bash
yaf --help                    # oppure: python -m youtube_automation_factory.cli --help
yaf check-config              # cosa e' configurato e cosa no
yaf init-demo                 # prepara cartelle e dati demo
yaf run-demo                  # workflow completo simulato, senza rete
yaf run-demo --stop-before-copy-review   # mostra il blocco: senza revisione esterna non si chiude
yaf list-states               # stati e transizioni ammesse
yaf generate-report           # genera i report Markdown in reports/
yaf validate-workflow <id>    # valida un workflow salvato
```

Codici di uscita: `0` successo, `1` errore d'uso o configurazione, `2` blocco regolatorio.

## Test, lint e formattazione

```bash
python -m pytest              # test, nessuna rete e nessun browser richiesti
python -m ruff check .        # lint
python -m ruff format .       # formattazione
```

## Modalita' demo/mock e integrazioni reali

| Componente | In demo | Integrazione reale |
|---|---|---|
| Ricerca YouTube | dati locali | `YouTubePlaywrightClient` con selettori configurati |
| Transcript | `available=False` + nota | tentato solo dal flusso pubblico previsto |
| Produzione video ("Flik") | `MockFlikAdapter` | **non implementata** (vedi sotto) |
| Copertina | brief prodotto, non generata | `ArenaPlaywrightClient` con selettori configurati |

Il mock di produzione **non genera alcun video**: lo dichiara in ogni output e imposta
`is_real_render=False`. Nessun test dipende da rete, browser o credenziali.

## Regole di originalita'

`OriginalityService` esegue una checklist **di processo**: brief proprio presente, assenza del
flag "copy mode", nessuna derivazione dichiarata da materiale di terzi. Un asset non puo' essere
approvato se `originality_checked` e' `False`, e la macchina a stati lo impedisce.

> **Limite dichiarato.** Questo e' un controllo di *processo*, non una certificazione legale di
> assenza di plagio. Non confronta il testo con archivi esterni e non sostituisce una
> valutazione legale. Un esito positivo significa "la procedura interna e' stata seguita".

## Limitazioni note

* **Flik non ha un client reale.** In questo repository non esiste una specifica API verificata
  del fornitore: esistono l'interfaccia astratta `FlikAdapter` e il mock locale. Un adapter
  reale va scritto sulla documentazione ufficiale, implementando la stessa interfaccia.
* **I selettori browser non sono forniti.** Vanno rilevati e verificati dall'operatore. Senza,
  l'automazione si rifiuta di partire.
* **Nessun aggiramento di protezioni.** Niente automazione di login, CAPTCHA, controlli di
  accesso o limitazioni delle piattaforme.
* **CTR e retention non sono ottenibili** dalle pagine pubbliche: sono dichiarati come dati
  mancanti, mai stimati.
* **Il quality control non guarda i file prodotti**: verifica stati, approvazioni e coerenza
  degli asset, non la qualita' percettiva di un video.

## Documentazione

[architettura](docs/architecture.md) · [workflow](docs/workflow.md) ·
[gerarchia](docs/agent_hierarchy.md) · [regole e originalita'](docs/rules_and_originality.md) ·
[approvazioni](docs/approval_process.md) · [selezione video](docs/video_selection_criteria.md) ·
[copywriting](docs/copywriting_workflow.md) · [copertine](docs/thumbnail_workflow.md) ·
[competitor](docs/competitor_analysis.md) · [ricerca nicchie](docs/niche_research.md)
