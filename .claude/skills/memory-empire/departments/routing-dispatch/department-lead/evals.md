# Evals — routing-dispatch / department-lead

## PASS se:
- [ ] Ogni URL YouTube/TikTok/web → Empire Studio attivato entro il ciclo corrente
- [ ] `memory/routing/routing-<ts>.json` creato per ogni ciclo
- [ ] Se activation-monitor segnala "failed" → re-attivazione manuale eseguita
- [ ] Nessun ciclo senza log
- [ ] Nessun caso di "WebFetch come sostituto di Empire Studio"

## FAIL se:
- [ ] Link YouTube ricevuto e Empire Studio NON attivato
- [ ] Log mancante per un ciclo
- [ ] Intent-classifier non invocato prima del routing
- [ ] Activation-monitor saltato

## Test manuale
```
Input: "https://www.youtube.com/watch?v=XYZ"
Expected: Empire Studio attivato, run creata, log scritto
```
