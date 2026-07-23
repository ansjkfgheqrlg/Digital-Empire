# Campagna "concessionari-preventa" (G-A2)

> ADR-003: questa campagna WRAPPA il motore outreach esistente e i template già scritti in
> `Outreach/preventa-outreach-pack/`. Non modifica `empire_auto_v3.py` né alcun file esistente:
> vive in questa cartella a fianco, come config/campagna dedicata.

## Cosa fa

`personalizza_messaggi.py` prende in input il CSV prodotto da `Outreach/preventa-maps-scraper/`
(`nome_attivita, telefono, sito_web, ha_sito, numero_recensioni, priorita_lead, note_qualifica,
citta_ricerca, ...`) e per ogni lead genera:

1. **Gancio scelto** (1-5, da `04_5_VARIANTI_GANCIO_AB.md`), con la logica già definita nel
   LEGGIMI dello scraper (§8): ALTA senza sito → Gancio 3 · ALTA poche recensioni → Gancio 2 ·
   MEDIA/altro → Gancio 1 (control).
2. **WhatsApp MSG1** personalizzato (nome attività, zona), pronto per l'invio — canale primario
   se c'è un telefono.
3. **Email 1** (oggetto + corpo) personalizzata come fallback se non c'è telefono/WhatsApp.

Non firma né invia nulla: produce solo i messaggi pronti in un JSON, stato iniziale
`da_contattare`. L'invio reale (G-A4) e il follow-up automatico G+2/G+5 (G-A3) sono task
successivi, gated dall'ok di Max.

## Uso

```bash
python personalizza_messaggi.py --input <path-csv-lead> --output <path-json-output>

# Dry-run di test (5 lead finti, incluso in questa cartella):
python personalizza_messaggi.py --input test_lead_finti.csv --output output_dry_run.json
```

## Nota onesta

`[Nome]` (nome del titolare) non è disponibile da Google Maps: i messaggi generati salutano con
il nome dell'attività, non un nome di persona finto. Il nome del titolare si scopre nella
chiamata a freddo (script `01_SCRIPT_CHIAMATA_FREDDA_APSOC.md`, resta umana) e va aggiunto a
mano nei messaggi successivi (MSG2/MSG3), non in questo step automatico.
