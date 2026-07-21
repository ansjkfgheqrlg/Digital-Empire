# S4 — Pipeline automatica Mentalità Brutale

## Stato

La pipeline è ora separata in gate deterministici e adapter esterni:

1. **Produzione**: `carousel-factory` resta il motore canonico (ADR-003).
2. **QA**: `mentalita_pipeline.py` controlla schema, brand, 1–10 slide, numerazione,
   tipi supportati, caption, CTA e formule vietate.
3. **Rendering**: solo dopo QA verde viene invocato `scripts/generate.js`.
4. **Pubblicazione**: non viene eseguita automaticamente finché non esiste un adapter
   con credenziali e URL HTTPS pubblici configurati fuori dal repository.
5. **Report**: ogni run salva un JSON in `reports/` con pass/fail per file.

## Uso

Dalla root del repo:

```bash
python "SKILL & Agenti/Workflow pubblicazione automatica/mentalita_pipeline.py" \
  --input "Workfolw crea caroselli à/carousel-factory/input" --qa-only
```

Per renderizzare dopo il gate:

```bash
python "SKILL & Agenti/Workflow pubblicazione automatica/mentalita_pipeline.py" \
  --input "Workfolw crea caroselli à/carousel-factory/input" --render
```

`--publish` è volutamente un fail-closed guard: non pubblica nulla. La condizione
"100% auto" di S4 richiede prima di definire e testare un adapter reale (Meta Graph API
o publisher già esistente), un sistema per URL pubblici degli asset e una policy di
retry/idempotenza. Non si devono simulare pubblicazioni né registrare un post come
pubblicato prima della conferma dell'API.

## Gate QA

- brand esatto `mentalita-brutale`;
- titolo e caption non vuoti;
- 1–10 slide, numeri consecutivi;
- template tra quelli presenti nel carousel-factory;
- almeno un contenuto per slide;
- CTA `link in bio` (warning se manca);
- blocco di formule motivazionali vaghe già vietate dalle regole del brand.

## Adapter Meta Graph API

`meta_publisher.py` implementa il passaggio pubblicazione in modo isolato e idempotente:

- crea i container immagine figli;
- crea il container `CAROUSEL` padre;
- esegue `media_publish`;
- salva lo stato soltanto dopo aver ricevuto il `media_id` pubblicato;
- rifiuta URL locali/non HTTPS e non stampa mai il token.

Esempio da macchina operativa (token solo nell'ambiente):

```bash
set META_IG_USER_ID=...
set META_ACCESS_TOKEN=...
set META_GRAPH_VERSION=vXX.X
```

L'adapter richiede URL HTTPS pubblici per ogni slide. Non carica file locali e non
considera un container creato come pubblicazione riuscita. Prima di collegarlo al
runner giornaliero va provato su account di test e con un batch dedicato.

## Prossimo passo reale

Configurare su macchina operativa, senza commit di token:

- account professionale Instagram e Page/Business ID verificati;
- `META_ACCESS_TOKEN`, `META_IG_USER_ID` e base URL degli asset in `.env` locale;
- adapter API con idempotency key per carousel e stato `planned → containers → published`;
- test su un contenuto non pubblico / account di prova;
- report con reach, impressions, saves, shares, comments e timestamp UTC.

Finché questi prerequisiti non sono verificati, il sistema deve restare in dry-run: è il
solo modo coerente con la richiesta di riattivazione automatica senza inventare risultati.
