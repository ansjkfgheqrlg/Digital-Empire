# Evals — conductor

## Casi di accettazione
1. **Happy path (manuale):** `run.py --manual fixture.html --foto fixtures/foto` → `listing.json` valido,
   `listing_it.json.price.final_eur` corretto, exit 0 (S3/S5 skipped se Half B assente).
2. **Prezzo:** esposto 18.000 → `final_eur == 21540`, `final_title` contiene `21.540 €`.
3. **Gate A blocca:** input senza prezzo → exit 3, nessun `listing_it.json.price`.
4. **Gate A blocca:** input senza foto → exit 3.
5. **Dealer alternativo:** `--dealer <x>` con `surcharge_pct` diverso → `final_eur` cambia di conseguenza.
6. **Dealer inesistente:** `--dealer nope` → errore chiaro con lista dealer.
7. **Half B presente:** con `translate_copy`+`render_pdf` mock → `preventivo_*.pdf` prodotto, exit 0.
8. **Idempotenza:** due run stesso URL → due cartelle `runs/<id>` distinte, nessuna collisione.

## Come eseguire
Unit: `pricer.compute_price`, `parser._to_float`, `dealers.load_dealer` (già verdi).
End-to-end: preparare una fixture HTML mobile.de + cartella foto e lanciare in `--manual`.
