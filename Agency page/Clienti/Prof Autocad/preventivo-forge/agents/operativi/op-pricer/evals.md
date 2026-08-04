# Evals — op-pricer

## Casi (deterministici)
1. **Base:** 18.000 → `final_eur == 21540`. ✅ verificato.
2. **Format:** `format_eur(21540) == "21.540"`. ✅ verificato.
3. **Titolo:** `build_title("Mercedes-Benz","GLA 220","d 4MATIC AMG Line",21540)` contiene `21.540 €` e nessun doppio spazio.
4. **Dealer diverso:** `surcharge_pct=5, fixed=1000+1000` su 20.000 → `round(20000*1.05+2000)=23000`.
5. **Merge:** con `listing_it.content` preesistente → dopo `price()` `content` invariato, `price` aggiunto.
6. **Guardia:** `price_listed_eur=None` → `ValueError` (nessun prezzo inventato).
7. **Breakdown:** somma `listed+surcharge_eur+fixed_1+fixed_2` arrotondata == `final_eur`.

## Stato
Casi 1-2 verificati in sessione. 3-7 eseguibili via unit test su `pricer` (nessuna dipendenza esterna).
