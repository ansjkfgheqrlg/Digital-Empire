# Playbook — case-study-forge

## 1. Happy path — nicchia nota, pattern esistente (Preventa/import auto)

**Input**: lead Kaufmann S.a.s, nicchia `concessionario-auto-import`, nessun case study
reale disponibile.

**case-study-forge**: "Nessun case study reale per questa nicchia. Applico pattern noto:
`{tipo: artificial_case_study, descrizione: 'PDF preventivo di esempio generato su un
annuncio reale del concessionario', asset_prodotto: null}`. Passo a message-writer."

## 2. Happy path — case study reale disponibile

**Input**: lead creator YouTube nicchia AI, case study reale disponibile ("portato
Andrea Ciraolo da 15k a 26k iscritti in 2 mesi con script ottimizzati").

**case-study-forge**: "Trovato case study reale pertinente. `{tipo: real_case_study,
descrizione: 'portato un canale AI da 15k a 26k iscritti in 2 mesi ottimizzando gli
script', asset_prodotto: null}`. Passo a message-writer."

## 3. Edge case — lead con riferimento specifico disponibile (annuncio reale)

**Input**: lead con link a un annuncio auto specifico già raccolto dallo scraper.

**case-study-forge**: personalizza l'artificial case study includendo il riferimento:
`{tipo: artificial_case_study, descrizione: 'PDF preventivo generato specificamente
sull'annuncio [link] del lead', asset_prodotto: null}` — più forte del pattern generico
perché già ancorato a un dato reale del lead.

## 4. Failure recovery — nicchia mai vista

**Input**: lead in una nicchia completamente nuova (es. "consulente fiscale") mai
processata dal team.

**case-study-forge**: "ESCALATION: nicchia non coperta — consulente fiscale. Non ho un
pattern di artificial case study collaudato per questa categoria. Serve decidere
insieme a Max quale tipo di lavoro gratuito ha senso offrire prima di procedere con
questo lead (e con l'intera nicchia, per riutilizzo futuro)."

## 5. Edge case — offerta proporzionata alla dimensione del lead

**Input**: due lead della stessa nicchia (import auto), uno concessionario locale
piccolo, uno gruppo multi-sede grande.

**case-study-forge**: mantiene la STESSA offerta base (PDF preventivo di esempio) per
entrambi — la Bibbia non richiede di scalare l'offerta con la dimensione del lead, anzi
la scalabilità del pattern (stessa offerta, riutilizzabile) è parte del punto di forza
del metodo. Non genera un'offerta "più grande" per il lead più grande senza un motivo
esplicito.
