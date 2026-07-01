# Failure modes — op-pricer

| Failure | Sintomo | Prevenzione | Rilevazione | Recupero |
|---|---|---|---|---|
| `price_listed_eur` mancante | ValueError | Gate A a monte | eccezione in `price()` | stop; sistema estrazione (S1/S2) |
| Parametri dealer assenti | prezzo con default inattesi | `pricing_resolved` con fallback `.env` | ispezione breakdown | correggi `config.json` dealer |
| Arrotondamento errato | centesimi nel titolo | `round()` a intero + `format_eur` int | Gate C | correggi format |
| Separatore migliaia sbagliato | `21540` o `21,540` nel titolo | `format_eur` (`,`→`.`) | review titolo | correggi format_eur |
| `content` sovrascritto | traduzione persa | merge esplicito preserva `content` | diff `listing_it.json` | ripristina merge |
| Divergenza col Gate C | final_eur ≠ ricalcolo | formula unica + breakdown | qa-price-verifier | allinea formula/parametri |
