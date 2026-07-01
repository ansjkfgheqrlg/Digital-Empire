# Playbook — qa-price-verifier

## Quando gira
Dopo S4 (pricing), prima di S5. Chiamata: `gate_c(ctx, dealer)` (passare `dealer` per indipendenza piena).

## Interpretare i risultati
| Issue | Significato | Chi corregge |
|---|---|---|
| `prezzo finale non riproducibile` | formula o esposto errati | S4 pricer / S2 parsing prezzo |
| `parametri prezzo incompleti` | manca pct/fixed o listed | config dealer / estrazione |
| `surcharge_eur incoerente` | breakdown sbagliato | S4 pricer |
| `final_title senza prezzo formattato` | titolo mal costruito | `pricer.build_title` |
| `final_title senza marca` | marca persa | S2 / build_title |

## Caso critico: prezzo esposto mal parsato
Il prezzo tedesco "€ 28.900" può essere letto male (punto migliaia). Gate C lo intercetta perché
ricalcola dal `price_listed_eur`: se l'esposto è sbagliato, il finale non torna → blocco.

## Riferimento verificato
BMW 320d: esposto 26.900 → finale 30.707 €, ricalcolo indipendente combacia → Gate C PASS.
