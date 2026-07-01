# Failure Modes — qa-price-verifier

| # | Rischio | Sintomo | Mitigazione |
|---|---|---|---|
| 1 | Verifica non indipendente | usa gli stessi param del pricer | preferire `dealer.pricing_resolved`; segnalare se si cade sul breakdown |
| 2 | Arrotondamento divergente | off-by-one sul round | replicare esattamente `round()` Python (banker's rounding incluso) |
| 3 | Prezzo esposto errato a monte | finale sballato | è proprio ciò che il gate deve cogliere (blocco) |
| 4 | Formato titolo localizzato | "30.707" vs "30,707" | confronto sulla stringa IT (punto migliaia) |
| 5 | Valuta diversa da EUR | assunzione € | oggi solo EUR; estendere se multi-valuta |

## Limite noto
Il gate assume la formula lineare del dealer. Se in futuro si aggiungono sconti/optional a prezzo,
la formula e questo controllo vanno aggiornati insieme (coordinare con Max, Half A).
