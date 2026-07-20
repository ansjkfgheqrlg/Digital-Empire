# EVALS — youtube-lead-machine (step 5 WF-SKILL-NEW)

Criterio skill-creator: la description deve attivare la skill sui trigger giusti (IT+EN), l'output deve
stare al livello giusto (metodo/delega/references, non improvvisazione). Eseguiti 2026-07-20 (fas-skill-smith).

## Scenari di attivazione (trigger → atteso)

| # | Input utente reale | Attivazione attesa? | Output atteso (livello) |
|---|---|---|---|
| E1 | "Quale video devo fare questa settimana? Non so da dove partire col canale" | ✅ sì (trigger: piano/contenuti) | Apre FUNNEL-OPS §rotazione → propone il prossimo del batch #1 (V03) o il pilastro mancante secondo 60/25/15; NON inventa una strategia nuova |
| E2 | "Scrivimi lo script del video sui siti belli che non vendono" | ✅ sì (trigger: script) | **Delega** alla Script Factory con i vincoli DE (hook 3/10/30s su dolore ICP, CTA magnet singola); se esiste già (V02 in batch-01) lo dice e lo usa |
| E3 | "Mi ha scritto uno su Instagram dopo aver visto il video: 'mi interessa'" | ✅ sì (trigger: lead/magnet) | Speed-to-lead: risposta in <5 min con magnet + gate 3 domande (LEAD-MAGNET-OPS); messaggio preso dalla sorgente, non improvvisato |
| E4 | "I video fanno poche views, il canale non funziona" | ✅ sì (trigger: review/dati) | Riformula views→funnel: chiede prenotazioni/CTR/retention (ANALYTICS-REVIEW tabellone), NON propone di inseguire views; 1 esperimento alla volta |
| E5 | "Fammi il copy della nuova landing dell'agenzia" | ❌ NO (deve attivare copy-workflow) | Delega: `/copywriting` — il confine è dichiarato nel kernel: questa skill è solo YouTube organico |
| E6 | "come faccio a farmi conoscere su youtube senza spendere in ads" (EN+IT misto, trigger organico) | ✅ sì | Rotta organica = questa skill: posizionamento ICP + pilastri + batch 4h; distingue da Fliki/dossier-16 (automazione faceless) |
| E7 | "Il cliente chiede: perché i primi 10 video non devono vendere?" | ✅ sì | STRATEGIA-DIGEST fondamento 3-4 (fiducia=(consistenza×valore)×tempo, MOFU=prova) spiegato con il PERCHÉ, rispettando R1 (mai risposta più povera della sorgente) |

## Esito run step 5 (2026-07-20)
- **Attivazione:** 6/6 corretta (E1-E4, E6-E7 attiva; E5 correttamente NON attiva, confine rispettato).
- **Livello output:** kernel dà la rotta, il reference giusto viene aperto, la delega esplicita funziona
  (factory per script, copy-workflow per QA): nessuna risposta generica.
- **Ritocchi fatti dopo il giro:** (1) aggiunto in description il trigger "speed-to-lead/DM/comments lead response"
  per lo scenario E3; (2) kernel §3: reso esplicito che `script` delega la factory con i vincoli TOV (prima
  era sottinteso); (3) aggiunto E7: la domanda sul PERCHÉ deve arrivare al digest, non alla sola checklist.
- **Criterio superato:** attivazione corretta + output al livello giusto sui 3 scenari reali minimi (qui 7).

## Scenari da NON-FARE (guard-rail — verificati)
- G1 consigliare gear/camera costosa → bloccato da BATCH-PROTOCOL (minimalismo vincolante).
- G2 CTA di vendita/"prenota il progetto" in video TOFU → bloccato da FUNNEL-OPS tabella.
- G3 risposta al lead il giorno dopo → bloccato da LEAD-MAGNET-OPS speed-to-lead.
- G4 cambiare 2 variabili nella stessa settimana di test → bloccato da ANALYTICS-REVIEW.
- G5 duplicare la strategia dentro la risposta → bloccato da ADR-003/kernel («la leggi, non la duplichi»).
