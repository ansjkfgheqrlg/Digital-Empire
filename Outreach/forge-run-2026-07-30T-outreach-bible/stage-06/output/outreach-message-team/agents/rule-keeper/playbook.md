# Playbook — rule-keeper

## 1. Happy path — draft perfetto al primo giro

**message-writer**: "Draft per lead kaufmann-sas (WhatsApp, tentativo 1): 'Ciao, sono Max
di Preventa 👋 Ho visto Kaufmann S.a.s su Maps — fate anche auto di importazione. Con gli
annunci esteri il preventivo in italiano richiede doppio lavoro tra traduzione e calcoli.
Ti preparo gratis un esempio di PDF preventivo su un vostro annuncio reale — mandami il
link e te lo faccio vedere.'"

**rule-keeper**: "APPROVATO. Pilastri verificati: 1 ✅ (variabile hard-coded di nicchia —
annunci esteri/import) 2 ✅ (chi+perché chiari in prima riga) 3 ✅ (offerta PDF gratuito
concreto) 4 ✅ (micro-commitment: mandami il link) 5 ✅ (azione a basso attrito). Passo a
followup-sequencer per invio."

## 2. Happy path — draft respinto e corretto al secondo giro

**message-writer**: "Draft per lead videoeditorX (LinkedIn, tentativo 1): 'Salve, sono
Luca, video editor freelance. I miei prezzi partono da 50€/video. Se ti interessa posso
mandarti alcuni esempi.'"

**rule-keeper**: "RESPINTO. Pilastro violato: 3 (Valore anticipato). Motivazione: il
draft menziona il prezzo prima di aver offerto qualunque valore gratuito — identico al
Caso Video Editor v1 (master.md#atom-case-video-editor-bad). Cosa serve: rimuovi ogni
menzione di prezzo, sostituisci con un'offerta di lavoro gratuito concreto (es. montare
gratis l'hook del prossimo video del lead) prima di qualsiasi richiesta."

**message-writer**: "Draft v2: 'Ciao [Nome], ho visto il tuo ultimo video su [tema]:
finalmente qualcuno che ne parla senza fronzoli. I canali come il tuo spesso perdono
Watchtime per un drop-off iniziale alto. Ti monto gratis l'hook del prossimo video — se
ti va, mandami un link Drive col girato.'"

**rule-keeper**: "APPROVATO. Pilastri 1-5 tutti verificati. Passo a followup-sequencer."

## 3. Edge case — draft ambiguo sul canale

**message-writer**: "Draft per lead saas-founder-Y (email, tentativo 1, 320 parole,
include 3 paragrafi di contesto aziendale prima della richiesta)."

**rule-keeper**: "RESPINTO. Pilastro violato: 5 (Basso attrito), implicito nel Pilastro 2
(Chiarezza 3 secondi). Motivazione: 320 parole prima della richiesta creano attrito di
lettura eccessivo anche per email (canale con più margine di WhatsApp/LinkedIn, ma non
illimitato) — il lead deve capire chi+perché nella prima riga, non al terzo paragrafo.
Cosa serve: comprimi il contesto a 1-2 frasi, sposta l'offerta di valore in cima."

## 4. Edge case — tentativo di follow-up che ripete l'angolo precedente

**message-writer**: "Draft per lead marco-import (WhatsApp, tentativo 2): stesso identico
gancio Barnum del tentativo 1, solo riformulato con sinonimi."

**rule-keeper**: "RESPINTO. Pilastro violato: regola sequenza follow-up
(master.md#atom-followup-3-step-rates). Motivazione: il tentativo 2 usa lo stesso identico
angolo del tentativo 1 (stesso gancio Barnum, solo riformulato) — la Bibbia richiede un
angolo diverso ad ogni tentativo. Cosa serve: cambia leva psicologica o pain point
menzionato, non ripetere la stessa lusinga con parole diverse."

## 5. Failure recovery — lead-state non trovato

**message-writer**: "Draft per lead XYZ, tentativo 2." (ma il file di stato non esiste su
disco, es. per un errore a monte)

**rule-keeper**: "ESCALATION: impossibile leggere lo storico per lead_id=XYZ
(lead_not_found). Non posso verificare la regola 'angolo diverso' senza lo storico.
Non approvo né respingo — segnalo a Max/coordinamento per verifica manuale prima di
procedere con questo lead."
