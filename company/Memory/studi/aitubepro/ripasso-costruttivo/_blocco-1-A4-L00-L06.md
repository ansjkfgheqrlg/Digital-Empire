# Ripasso costruttivo — Blocco 1: A4 / L00 → L06 (metodo AI Tube)

> Non ripropongo le 69 regole già estratte (`regole/A4-metodo-ai-tube/L*.py`): quelle rispondono
> alla domanda "quale documento cambio". Qui rispondo alle quattro domande nuove — AGENTE, SKILL,
> FLUSSO, CODICE — verificando ogni proposta contro `INVENTARIO.md` prima di scriverla.

---

### P-B1-01 · agente
- **Lezione:** A4-metodo-ai-tube/L02 — Scrivere e (ri)scrivere testi originali con A.I
- **Prova:** `L02-riscrivere-testi/appunti.md` — «scrivimi questo testo da zero rendendolo originale come se fossi un giornalista» @ 01:17; il testo che ne esce (`frame-043.png` @ 02:48) contiene nome, età, data, causa di morte e citazioni fra virgolette, riscritti senza nessun controllo mostrato in lezione.
- **Cosa manca oggi:** nessun organo della fabbrica verifica che i FATTI (nomi, date, cifre, citazioni) sopravvivano intatti alla riscrittura. `regolatori.py:153` (`verifica_originalita`) controlla solo se il testo è troppo SIMILE alla fonte (copiato), mai se è ancora VERO. Cercato in tutta la fabbrica "verifica dei fatti / fact-check / controllo dei fatti": zero risultati (verificato nel report L02, confermato contro `INVENTARIO.md`: fra i 5 regolatori — configurazione, copy, nicchia, originalità, qualità — nessuno tocca la veridicità).
- **Cosa nasce:** nuovo agente `03-AGENTI-E-RUOLI/regolatori/regolatore-fatti.md` + script `02-AUTOMAZIONI-E-SCRIPTS/verifica_fatti.py`. Lo script estrae entità (nomi propri, date, numeri, citazioni fra virgolette) dal transcript sorgente + fonti_extra, le confronta con lo script riscritto, e restituisce le discordanze — stesso principio di `verifica_originalita`, ma sul contenuto invece che sulla forma.
- **Perché vale:** oggi un modello può spostare una data, cambiare un'età o attribuire una frase a chi non l'ha detta, e nessun gate se ne accorge prima della pubblicazione. Su una nicchia di cronaca (il caso mostrato in lezione) è il rischio più grave trovato finora in tutto lo studio: sappiamo misurare se un testo è copiato, non sappiamo dire se è ancora vero.
- **Binario:** A per la nascita dell'agente e dello script come modulo testabile in isolamento; **B** quando viene agganciato dentro la pipeline reale (chiamato da `regolatori.py` o `apex7_orchestrator.py`) — quell'aggancio aspetta il gate di categoria.
- **Misura:** esistono `03-AGENTI-E-RUOLI/regolatori/regolatore-fatti.md` e `02-AUTOMAZIONI-E-SCRIPTS/verifica_fatti.py`, con una funzione che confronta due testi e restituisce le entità discordanti; oggi nessuno dei due file esiste.

---

### P-B1-02 · funzione
- **Lezione:** A4-metodo-ai-tube/L03 — Text to speech: cosa è, e come funziona · L04 — Editing Video Automatico con AI All in One
- **Prova:** `L03-text-to-speech/appunti.md` @ 12:27-13:10 «gli accenti sono l'unica cosa difficile... ve le salvate su un file»; `L04-editing-automatico/appunti.md` @ 26:00-26:44, stesso esempio (`iscrivìti`/`iscrìviti`) dentro Fliki, col nome ufficiale **Pronunciation map** (menu More, `frame-224.png` @ 18:35).
- **Cosa manca oggi:** la regola già scritta `A4-L03-03` crea solo una SCHEDA statica (`references/lessico-pronuncia.md`) che un umano dovrebbe leggere prima di scrivere. Non esiste nessuna funzione che applichi automaticamente le sostituzioni al testo prima di costruire il payload: verificato che `fliki_client.py` non importa né legge alcun file di lessico.
- **Cosa nasce:** funzione `applica_lessico_pronuncia(testo, path_lessico)` in `02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py` (o modulo dedicato), chiamata prima di costruire ogni scena del payload: sostituisce ogni occorrenza della parola-problema con la grafia accentata registrata nel lessico.
- **Perché vale:** chiude per davvero il buco già descritto nel report L03 ("il dizionario non impara"). Oggi, anche scrivendo la correzione su un file, il video successivo sbaglia di nuovo la stessa parola perché nessun codice la legge. Con la funzione il lessico smette di essere un promemoria e diventa un controllo automatico — la differenza fra 125 decisioni registrate e zero sulla pronuncia (già misurata nel report L03) smette di ripetersi.
- **Binario:** B (tocca `02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py`, motore in produzione).
- **Misura:** `fliki_client.py` legge `references/lessico-pronuncia.md` (o un json equivalente) e un test unitario mostra che una parola del lessico viene sostituita nel testo di scena prima dell'invio; oggi zero occorrenze di "lessico" o "pronuncia" in `fliki_client.py`.

---

### P-B1-03 · funzione
- **Lezione:** A4-metodo-ai-tube/L01 — Scaricare testi già pronti per generare video in 3 click
- **Prova:** `L01-scaricare-testi/appunti.md` @ 04:58 «magari questo qui è un video abbastanza corto»; report L01 §3: «il brief scritto dalla macchina dice "servono ~2.000 parole"... senza contare le parole né avvisare che non bastano».
- **Cosa manca oggi:** la regola già scritta `A4-L01-01` chiede a `transcript-collector.md` di "dichiarare" la carenza — è un'istruzione testuale rivolta a un agente-lettore, non una funzione. Verificato: `apex7_orchestrator.py:1189-1214` costruisce il file `<videoId>.DA-SCRIVERE.md` senza mai contare le parole del transcript né confrontarle con `PAROLE_MINIME_SCRIPT`.
- **Cosa nasce:** funzione `verifica_sufficienza_materiale(transcript, fonti_extra)` in `apex7_orchestrator.py`, chiamata prima di scrivere il `DA-SCRIVERE.md`: conta le parole reali, calcola il rapporto con `PAROLE_MINIME_SCRIPT` (2.220), e sotto una soglia dichiarata blocca la generazione del brief finché non sono allegate almeno 2 fonti esterne con link — lo stesso principio di `verifica_originalita`, applicato PRIMA della scrittura invece che dopo.
- **Perché vale:** oggi il vincolo delle 2.220 parole minime e il materiale realmente disponibile possono divergere in silenzio: chi scrive riceve un ordine impossibile, e la via più breve per eseguirlo è inventare o riempire — su una nicchia di cronaca, il rischio più concreto già segnalato nel report L01 ma mai chiuso in codice.
- **Binario:** B (tocca `02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py`, motore in produzione).
- **Misura:** `apex7_orchestrator.py` contiene una funzione che conta le parole del transcript e blocca/avvisa sotto soglia; oggi (verificato nel report L01) quel conteggio non esiste da nessuna parte nel codice.

---

### P-B1-04 · skill
- **Lezione:** A4-metodo-ai-tube/L00 — A.I Artificial Intelligence Tutte le AI + aggiornamenti + Opportunity Business
- **Prova:** `L00-tutte-le-ai/appunti.md` @ 03:07 «visitare ogni giorno questi portali... dedica un quarto d'ora, 20 minuti»; @ 04:48 «cercare principalmente quelli verificati o popolari».
- **Cosa manca oggi:** le regole già scritte `A4-L00-01/02` chiedono a `self-improver.md` di avere "un compito periodico di sorveglianza con un tetto di tempo scritto" — di nuovo, un'istruzione testuale per un agente, non un comando invocabile che produca un output verificabile. Non esiste, nell'inventario script (33 agenti, nessuno scanner cataloghi) né fra le reference, nessuno strumento che interroghi i cataloghi (futurepedia, futuretools, aifinder) e restituisca la lista dei nuovi strumenti verificati/popolari.
- **Cosa nasce:** nuova skill (es. `.claude/skills/scan-strumenti-ai/`), invocabile a comando, che interroga i tre cataloghi per le categorie rilevanti alla fabbrica (video generator, text to speech, ai video) e produce un report — nome, categoria, verificato/popolare sì/no — su disco, con data.
- **Perché vale:** oggi, come dice il report L00, "non esiste nessun processo che si chieda se [Fliki e Arena] siano ancora i migliori". La copertina automatica è già fallita tre volte su Arena senza che nessuno si sia mai chiesto se esistesse un'alternativa migliore, perché non esiste il comando che pone la domanda.
- **Binario:** A (skill/script nuovo, fuori dal motore in produzione — non tocca `02-AUTOMAZIONI-E-SCRIPTS`).
- **Misura:** la skill esiste e produce un file di report con data ad ogni invocazione, verificabile sul disco; oggi zero menzioni di futuretools/futurepedia/aifinder in tutta la fabbrica (già verificato nel report L00).

---

### P-B1-05 · funzione
- **Lezione:** A4-metodo-ai-tube/L01 — Scaricare testi già pronti per generare video in 3 click
- **Prova:** `L01-scaricare-testi/appunti.md` @ 06:01 «può succedere che DownSub qualche volta non funziona»; report L01 §2: «Cosa si fa se il transcript manca: ci si ferma e si passa al candidato B. Nessuna via di riserva».
- **Cosa manca oggi:** la regola già scritta `A4-L01-02` chiede a `transcript-collector.md` di "nominare" una via di riserva — ancora testo per un agente-lettore, non codice. `transcript-collector.md` §Playbook 3 oggi dice solo "fermati, candidato B", e non esiste nessuna funzione di fallback quando `yt-dlp` non trova sottotitoli automatici.
- **Cosa nasce:** funzione `scarica_transcript_fallback(video_id)`, in un modulo indipendente, che prova un metodo alternativo (es. libreria `youtube-transcript-api`, o un endpoint diretto dei sottotitoli) SOLO quando `yt-dlp` fallisce, e distingue nel log i due guasti diversi — strumento muto vs video davvero senza sottotitoli — invece di limitarsi a scartare il candidato.
- **Perché vale:** oggi un candidato con VPH alto può venire scartato per un guasto strumentale che non ha niente a che fare con la qualità del video: la fabbrica perde candidati validi senza saperlo, e senza distinguere le due cause non si può nemmeno misurare quanto spesso succede.
- **Binario:** A finché resta un modulo indipendente testabile da solo; **B** quando viene agganciato nella catena reale di raccolta (`apex7_orchestrator.py` / `transcript-collector`) — l'aggancio aspetta il gate.
- **Misura:** esiste una funzione di fallback testabile in isolamento (chiamata su un video senza sottotitoli auto e uno con, restituisce esiti diversi e distinti); oggi nessun modulo di fallback esiste (verificato: `transcript-collector.md` non nomina nessun secondo metodo oltre `yt-dlp`).

---

### P-B1-06 · script
- **Lezione:** A4-metodo-ai-tube/L05 — Come creare un video da zero con il metodo A.I tube (IL METODO COMPLETO)
- **Prova:** `L05-metodo-completo/appunti.md` @ 00:35 «sono le 13 e 18» + @ 06:48 «ci ho impiegato veramente 5 minuti per fare tutto» — l'intera lezione è cronometrata passo per passo (tabella "Il metodo in una tabella" nel report L05).
- **Cosa manca oggi:** la regola già scritta `A4-L05-04` chiede di aggiungere una voce "tempo per video" a `BASELINE.md` — un campo da riempire a mano, non una misura automatica. Verificato: nessun file fra gli script del motore (elenco in `INVENTARIO.md`) contiene logica di cronometraggio per fase (nessun "tempo", "cronometro", "benchmark", "duration_stage").
- **Cosa nasce:** script `02-AUTOMAZIONI-E-SCRIPTS/misura_tempo_produzione.py`, un wrapper che avvolge (senza modificarle) le chiamate esistenti di `apex7_orchestrator.py`, timestampando inizio e fine di ogni fase (candidate pool → transcript → script → regolatori → Fliki → export → QA) e scrivendo il risultato in un log leggibile (fase, secondi, video_id) — lo stesso cronometro della lezione, ma automatico e ripetibile invece che dichiarato a voce una volta sola.
- **Perché vale:** senza un numero reale, il confronto con `ADR-016` (25 pezzi finiti mai pubblicati, il più vecchio fermo da 135 giorni) resta un'impressione. Con un log per fase si vede DOVE la produzione rallenta, non solo CHE rallenta — ed è la misura che manca per rendere "puntiamo sulla qualità" una scelta dichiarata invece che una scusa (parole del report L05).
- **Binario:** A se resta un wrapper esterno che chiama gli script esistenti senza modificarli; **B** se invece si preferisce instrumentare `apex7_orchestrator.py` dall'interno.
- **Misura:** esiste il log con almeno una produzione reale cronometrata fase per fase, su disco, con data; oggi `BASELINE.md` non contiene un solo minuto misurato di produzione (verificato nel report L05).

---

### P-B1-07 · funzione
- **Lezione:** A4-metodo-ai-tube/L05 — IL METODO COMPLETO · L06 — Metodo Copia e Incolla
- **Prova:** `L05-metodo-completo/appunti.md` @ 01:09 «5.700 pollici in su, 89.000 visualizzazioni, 13 ore fa»; `L06-metodo-copia-incolla/appunti.md` @ 07:02 «è normale che un video appena pubblicato faccia tante visualizzazioni, soprattutto se ci sono tanti iscritti al canale».
- **Cosa manca oggi:** le regole già scritte `A4-L05-01` e `A4-L06-01` chiedono di correggere la SOGLIA scritta in `video-analyst.md` — ma la formula di velocity vive nel codice, non nell'agente. Verificato: `build_candidate_pool.py:125-138` calcola `VPH = views / età` e ordina, senza mai recuperare o usare il numero di iscritti del canale sorgente. Le due regole già scritte cambiano cosa l'agente DICE di fare; nessuna cambia cosa lo SCRIPT fa davvero.
- **Cosa nasce:** in `build_candidate_pool.py`, per i candidati sotto le 24h, recupero del `subscriber_count` del canale sorgente (dati già raggiunti dalle stesse chiamate che leggono viste/like) e calcolo di una `velocity_rapportata = VPH / subscriber_count`, usata per ammettere o scartare il candidato al posto della sola soglia temporale fissa.
- **Perché vale:** oggi, anche correggendo il testo dell'agente, lo script che genera davvero il pool di candidati continua a scartare (o ammettere) per età, non per credibilità del segnale. La correzione scritta nella regola non si applica da sola finché il codice non cambia — è esattamente il tipo di buco che questo ripasso costruttivo esiste per trovare.
- **Binario:** B (tocca `02-AUTOMAZIONI-E-SCRIPTS/build_candidate_pool.py`, motore in produzione).
- **Misura:** `build_candidate_pool.py` calcola e logga `velocity_rapportata` per i candidati sotto le 24h; oggi (verificato: `build_candidate_pool.py:125-138`) il calcolo usa solo `views/età`, senza mai leggere il `subscriber_count` del canale.

---

### P-B1-08 · flusso
- **Lezione:** A4-metodo-ai-tube/L01 + L02 + L05 — l'intera catena materia-prima → testo, vista in tre lezioni diverse
- **Prova:** L01 @ 05:44 (link salvato nella colonna NOTE del piano editoriale); L02 @ 02:43 «aggiungi questa parte di testo senza essere ripetitivo e rendi l'articolo originale»; L05 @ 05:53 «se io inserissi altre parti di testo... sarebbe ancora meglio».
- **Cosa manca oggi:** nel nostro flusso una "fonte esterna" non è un oggetto che attraversa la catena — è, nella migliore delle ipotesi, una colonna che ancora non esiste (`assemble_piano_editoriale.py`, regola `A4-L01-03`) e un elenco di parole scritto nel brief. Non c'è uno stadio dove il pacchetto DA-SCRIVERE viene giudicato insufficiente (P-B1-03), uno stadio dove le fonti diventano "fatti da preservare" per il controllo dopo la riscrittura (P-B1-01), o uno stadio che misura quanto ci è voluto (P-B1-06). Sono tre buchi che le regole già scritte trattano come tre documenti da correggere separatamente, ma nella lezione sono UN flusso solo, eseguito in un'unica sequenza cronometrata.
- **Cosa nasce:** ridisegno del flusso candidato→pubblicazione con uno stadio esplicito e nominato — "Bilancio Materiale" — inserito fra `transcript-collector` e `script-writer`. Riceve transcript + fonti_extra, calcola se il materiale copre il fabbisogno di parole e, se non basta, ORDINA la ricerca di fonti aggiuntive invece di scartare il candidato; passa allo stadio successivo un pacchetto con un elenco esplicito di "fatti da preservare" che `regolatore-fatti` userà per il controllo dopo la riscrittura, con timestamp di inizio/fine registrato.
- **Perché vale:** oggi i tre buchi si toccano l'uno con l'altro e nessuna toppa isolata li chiude tutti insieme: un pacchetto può avere poche parole (L01), i fatti possono cambiare nella riscrittura (L02), e nessuno misura quanto ci vuole (L05) — sono la stessa catena vista da tre lezioni diverse, e il corso la esegue come un flusso unico in 5 minuti mentre noi la trattiamo come tre problemi scollegati affidati a tre agenti diversi che si parlano solo attraverso un file markdown.
- **Binario:** B (il nuovo stadio si innesta fra `transcript-collector` e `script-writer` nella pipeline reale, quindi tocca `02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py`).
- **Misura:** esiste uno stadio nominato nella pipeline (non tre agenti scollegati) che produce un unico artefatto con: parole contate, fonti allegate, fatti da preservare, timestamp di fase; oggi questi tre pezzi vivono — o dovrebbero vivere, se le regole già scritte venissero applicate una per una — in tre punti indipendenti e non comunicanti della fabbrica.

---

## FINITO — 8 proposte, lezioni ripassate: L00, L01, L02, L03, L04, L05, L06
