# R3 — Traduzione + Copy (S3, Half B / Gael)

> RBI operabile a freddo. Motore: `implementation/translate_copy.py` (+ `glossary_de_it.py`).
> Agente responsabile: `op-translator-copy`. Gate a valle: **Gate B** (`qa-translation-verifier`).

## OBIETTIVO
Trasformare i dati tedeschi normalizzati (`listing.json`) nella parte **testuale** italiana
`content.*` di `listing_it.json`: traduzione **fedele** DE→IT + copy di vendita migliorato,
**senza inventare** fatti non presenti nel sorgente.

## TRIGGER
- `run.py` step 3, subito dopo Gate A (estrazione) e prima di S4 (pricing).
- Chiamata: `translate_copy.translate(ctx, dealer)`.

## INPUT
| Fonte | Campo | Uso |
|---|---|---|
| `runs/<id>/listing.json` | `make, model, variant` | titolo IT, nome vettura |
| | `year, first_registration, mileage_km` | specs + highlights + descrizione |
| | `fuel, gearbox, drivetrain, power_kw/hp` | specs (già IT dal parser) + descrizione |
| | `body_type, color, interior, doors, seats, emission_class, co2_g_km` | specs (tradotti dove serve) |
| | `equipment_de[]` | → `equipment_it[]` (allineato 1:1) |
| | `description_de` | riferimento (arricchimento LLM opzionale) |
| `dealer` | (nessun campo obbligatorio) | firma contratto; riservato a usi futuri |

## OUTPUT
`runs/<id>/listing_it.json` → **solo** `content.*` (MERGE: NON tocca `price` di Max):
- `title_it` — titolo IT **senza prezzo**
- `headline_it` — riga gancio (anno · km · alimentazione)
- `description_it` — descrizione di vendita composta dai fatti
- `highlights_it` — 3–6 punti di forza (dai fatti)
- `equipment_it` — optional tradotti, **len == len(equipment_de)**
- `specs_it` — scheda tecnica con label IT

## STEP-BY-STEP
1. Carica `listing.json`.
2. `translate_equipment()` — traduce ogni voce con il glossario (frase → parola, umlaut ASCII gestiti). Mantiene l'ordine e il numero di voci.
3. `build_specs_it()` — compone la scheda; traduce `color/interior/body_type` col glossario; omette `color_manufacturer` (nome marketing).
4. `build_title_it()` — `make model variant`, senza prezzo.
5. `build_highlights_it()` / `build_description_it()` — copy **solo** dai fatti presenti.
6. `_merge_content()` — riscrive `listing_it.json` preservando `price` se già presente.
7. Logga eventuali residui tedeschi (avviso; il blocco è di Gate B).

## TEMPLATE (glossario)
`glossary_de_it.py`: `PHRASES` (termini composti, match più lungo prima) + `WORDS` (fallback
token). **Estendere qui** ogni volta che compare un termine DE non coperto. Esempi:
`Allrad`→trazione integrale · `Schaltgetriebe`→cambio manuale · `Standheizung`→riscaldamento
autonomo · `Anhängerkupplung (AHK)`→gancio traino · `Rückfahrkamera`→telecamera posteriore.

## GESTIONE ERRORI / SELF-HEALING
- Termine non nel glossario → resta invariato (Gate B lo segnala → si estende il glossario).
- Umlaut ASCII (`ue/oe/ae`) → `_restore_umlauts()` tenta il match con l'umlaut vero.
- `description_de` vuota → la descrizione si compone comunque dai campi strutturati.
- Arricchimento LLM (`TRANSLATE_BACKEND=llm`) è **OFF di default** (Mandato Art.4.3 dry-run):
  nessuna spesa API senza ok esplicito di Max.

## CASI LIMITE
- `equipment_de` vuoto → `equipment_it` vuoto (ok, Gate B allinea 0==0).
- Campi numerici assenti → semplicemente omessi da specs/highlights (mai inventati).
- Nomi colore costruttore con umlaut (`Alpinweiß`) → esclusi dalle specs per non falsare Gate B.

## NO-INVENZIONE (invariante)
Ogni frase di `description_it`/`highlights_it` deriva da un campo di `listing.json`.
Vietato aggiungere optional, allestimenti o dati non presenti nel sorgente.

## LOG
`ctx.logger`: n. optional tradotti, n. specs, n. highlights; warning sui residui tedeschi.
Stato/trace gestiti da `common.RunContext` (`state.json` + `trace.jsonl`).
