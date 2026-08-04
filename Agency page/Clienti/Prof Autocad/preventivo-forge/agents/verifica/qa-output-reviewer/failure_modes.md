# Failure Modes — qa-output-reviewer

| # | Rischio | Sintomo | Mitigazione |
|---|---|---|---|
| 1 | PDF valido ma esteticamente rotto | layout sballato non colto | re-render HTML + (futuro) snapshot visivo |
| 2 | Conteggio foto PDF impreciso | difficile contare foto nel PDF | verifica indiretta: foto su disco + `data:image/` nell'HTML |
| 3 | Placeholder solo in alcuni rami | `{{ }}` condizionale | re-render con lo stesso context del render |
| 4 | PDF vecchio di un run precedente | glob prende il file sbagliato | ordina per mtime, prende il più recente |
| 5 | Soglia 20 KB arbitraria | PDF piccolo ma valido | soglia prudente; un preventivo reale con foto supera sempre 20 KB |

## Miglioria futura
Aggiungere un check di rendering visivo (PDF→immagine + euristica) per intercettare difetti di
layout che i controlli testuali non vedono. Oggi la verifica visiva è manuale (a campione).
