# COPY-F5-delta — scagnozzo δ («CTA prodotto», dossier F5)

Riferimento: `brief/F5-allegati/08.jpg` (funneloperator.it). Tre pagine CTA parametriche, una per
prodotto, componente `src/sezioni-aggiunte/cta-prodotto.tsx`. Ogni prezzo/numero è da LISTINO/FATTI,
mai scritto a mano.

## outreach
- Eyebrow: «Installa il tuo»
- Titolo: «OUTREACH **FACTORY**»
- Tessera «Outreach Factory»: Setup in 7 giorni · 300 messaggi al giorno · Codice tuo, per sempre · 90 giorni di supporto
- Prezzo: 4.000 € — «Pagamento unico. Codice tuo, zero canoni. Metà alla firma, metà al go-live.»
- Confronto (solo qui): «Un SaaS equivalente: 200 € al mese, per sempre.»
- Slot: «Prossimo slot di installazione: su chiamata»
- Bottone pieno: «Prenota la chiamata di 30 minuti →» → `/prenota/?da=cta-outreach`
- Bottone ghost: «Cosa contiene, nel dettaglio ↓» → `#prezzi` (nessun id di dettaglio outreach esistente nel sito)
- Riga finale: «Setup in 7 giorni · garanzia 30 giorni · 90 giorni di supporto»

## content
- Eyebrow: «Accendi la tua»
- Titolo: «CONTENT **FACTORY**»
- Tessera «Content Factory»: Setup in 7 giorni · Caroselli, script e caption su Drive · Codice tuo, per sempre · 90 giorni di supporto
- Prezzo: 3.500 € — «Pagamento unico. Codice tuo, zero canoni. Metà alla firma, metà al go-live.»
- Slot: «Prossimo slot di installazione: su chiamata»
- Bottone pieno: «Prenota la chiamata di 30 minuti →» → `/prenota/?da=cta-content`
- Bottone ghost: «Cosa contiene, nel dettaglio ↓» → `#content-output` (id esistente, sezione ContentOutputV2)
- Riga finale: «Setup in 7 giorni · garanzia 30 giorni · 90 giorni di supporto»

## brain
- Eyebrow: «Dai memoria alla tua»
- Titolo: «SECOND **BRAIN**»
- Tessera «Second Brain»: Setup in 7 giorni · Wiki indicizzata, query in secondi · Codice tuo, per sempre · 90 giorni di supporto
- Prezzo: 2.500 € — «Pagamento unico. Codice tuo, zero canoni. Metà alla firma, metà al go-live.»
- Slot: «Prossimo slot di installazione: su chiamata»
- Bottone pieno: «Prenota la chiamata di 30 minuti →» → `/prenota/?da=cta-brain`
- Bottone ghost: «Cosa contiene, nel dettaglio ↓» → `#prezzi` (nessun id di dettaglio second-brain esistente nel sito)
- Riga finale: «Setup in 7 giorni · garanzia 30 giorni · 90 giorni di supporto»

## Nota sull'ancora `#prezzi`
Il sito non ha oggi un id `#prezzi` né `#outreach-inside` né `#second-brain-inside`: cercati in
`outreach-inside.tsx`, `second-brain-inside.tsx`, `pricing-roi.tsx` (nessuna sezione ha id, solo
`#content-output` in `content-output-v2.tsx` e `#prenota` in `final-cta`/`final-offer`). Per non
toccare `page.tsx` né i file di sezione fuori dal mio perimetro, ho usato `#content-output` dove
esiste e `#prezzi` come fallback dichiarato dall'ordine di Max altrove: oggi scrolla in cima alla
pagina (nessun elemento con quell'id). Da segnalare a Max/altro scagnozzo per aggiungere gli id
mancanti se vuole gli ancoraggi precisi.
