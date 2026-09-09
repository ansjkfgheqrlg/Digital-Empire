# -*- coding: utf-8 -*-
"""Regole COSTRUTTIVE del ripasso all'indietro — categoria A4, 2026-09-10.

PERCHE' QUESTO FILE ESISTE SEPARATO DAI FILE PER LEZIONE.
Le 21 lezioni di A4 furono lette con un contratto che ammetteva una sola domanda: «quale
documento esistente cambio?». Resa misurata: 69 regole, 64 su file .md, 5 sul codice,
zero agenti nuovi, zero skill, zero script, zero flussi ridisegnati. Max ha corretto il
mandato il 2026-09-10 — lo studio deve MIGLIORARE LA FABBRICA, non depositare regole.

Queste regole nascono dal ripasso all'indietro dello stesso materiale (appunti, report,
rapporti grezzi gia' su disco: nessun video e' stato riguardato), con le quattro domande
che non erano mai state poste: manca un AGENTE? una SKILL? un FLUSSO da ridisegnare?
del CODICE?

Restano in un file a parte per un motivo di verita' storica: non sono cio' che la lezione
diede la prima volta, sono cio' che la lezione avrebbe dato se le avessimo fatto la
domanda giusta. Mescolarle alle originali cancellerebbe la prova dell'errore.

Origine integrale, con le motivazioni per esteso:
  ../../ripasso-costruttivo/_blocco-1-A4-L00-L06.md
  ../../ripasso-costruttivo/_blocco-2-A4-L07-L18.md
  ../../ripasso-costruttivo/_blocco-3-fliki-A6-trasversali.md
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / ripasso costruttivo 2026-09-10"
LEZIONE = "ripasso all'indietro delle 21 lezioni A4 con le quattro domande costruttive"

REGOLE = [
    {
        "id": "A4-RC-01",
        "tipo": "agente",
        "regola": ("La fabbrica deve avere un organo che verifichi se un testo riscritto e' "
                   "ancora VERO. Oggi ne ha uno che misura se e' troppo SIMILE alla fonte "
                   "(regolatori.py:153) e nessuno che guardi nomi, date, cifre e citazioni: "
                   "davanti a un fatto storpiato l'originalita' da' via libera, perche' meno "
                   "somiglianza significa meno n-grammi condivisi."),
        "prova": ("L02-riscrivere-testi/appunti.md — «scrivimi questo testo da zero rendendolo "
                  "originale come se fossi un giornalista» @ 01:17; il testo prodotto "
                  "(frame-043.png @ 02:48) porta nome, eta', data, causa di morte e citazioni "
                  "fra virgolette, riscritti senza alcun controllo mostrato in lezione"),
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/regolatori/regolatore-fatti.md",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "alto",
        "misura": ("regolatore-fatti.md esiste ed e' agganciato nel 'blocca' di script-writer.md; "
                   "uno script di prova con una data alterata rispetto alla fonte produce un "
                   "BLOCCO che nomina la discordanza. Oggi il buco e' gia' descritto in "
                   "script-writer.md §8 (regola A4-L02-02) come istruzione in prosa, che nessun "
                   "gate applica"),
    },
    {
        "id": "A4-RC-02",
        "tipo": "script",
        "regola": ("Il confronto dei fatti fra sorgente e riscrittura si esegue in codice, non a "
                   "lettura: estrarre entita' (nomi propri, date, numeri, citazioni fra "
                   "virgolette) dal transcript e dalle fonti esterne, confrontarle con lo script "
                   "finale, restituire le discordanze. E' verifica_originalita applicata al "
                   "contenuto invece che alla forma."),
        "prova": ("stessa prova di A4-RC-01: L02-riscrivere-testi/appunti.md @ 01:17 + "
                  "frame-043.png @ 02:48"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/verifica_fatti.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "alto",
        "misura": ("verifica_fatti.py esiste e passa un test con una data alterata; l'aggancio "
                   "dentro regolatori.py / apex7_orchestrator.py aspetta il gate di categoria"),
    },
    {
        "id": "A4-RC-03",
        "tipo": "funzione",
        "regola": ("Il lessico delle pronunce si applica in codice prima di costruire il payload, "
                   "non si legge in una scheda. Una correzione scritta che nessun codice legge "
                   "lascia sbagliare la stessa parola al video successivo: e' un promemoria, non "
                   "un controllo."),
        "prova": ("L03-text-to-speech/appunti.md @ 12:27-13:10 «gli accenti sono l'unica cosa "
                  "difficile... ve le salvate su un file»; L04-editing-automatico/appunti.md "
                  "@ 26:00-26:44 stesso esempio dentro Fliki, nome ufficiale «Pronunciation map» "
                  "(menu More, frame-224.png @ 18:35)"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("fliki_client.py legge references/lessico-pronuncia.md e applica le "
                   "sostituzioni prima di costruire ogni scena; oggi non importa ne' legge alcun "
                   "file di lessico (grep 'lessico|pronunc' sul motore: zero risultati)"),
    },
    {
        "id": "A4-RC-04",
        "tipo": "funzione",
        "regola": ("Prima di ordinare uno script si misura se il materiale basta: contare le "
                   "parole reali del transcript, confrontarle con PAROLE_MINIME_SCRIPT, e sotto "
                   "soglia pretendere fonti esterne invece di consegnare un ordine impossibile. "
                   "Un brief che chiede 2.220 parole a chi ne ha 400 insegna a inventare."),
        "prova": ("L01-scaricare-testi/appunti.md @ 04:58 «magari questo qui e' un video "
                  "abbastanza corto»; report L01 §3: «il brief scritto dalla macchina dice "
                  "\"servono ~2.000 parole\"... senza contare le parole ne' avvisare che non "
                  "bastano»"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "alto",
        "misura": ("apex7_orchestrator.py conta le parole prima di scrivere DA-SCRIVERE.md e si "
                   "ferma sotto soglia; oggi le righe 1189-1214 costruiscono il brief senza mai "
                   "contarle. La regola A4-L01-01 chiedeva la stessa cosa a un agente-lettore"),
    },
    {
        "id": "A4-RC-05",
        "tipo": "skill",
        "regola": ("La sorveglianza del mercato degli strumenti e' un comando invocabile che "
                   "produce un file datato, non un compito periodico scritto nel playbook di un "
                   "agente. Nessuno ha mai chiesto se Fliki e Arena siano ancora i migliori, "
                   "perche' non esiste il comando che pone la domanda."),
        "prova": ("L00-tutte-le-ai/appunti.md @ 03:07 «visitare ogni giorno questi portali... "
                  "dedica un quarto d'ora, 20 minuti»; @ 04:48 «cercare principalmente quelli "
                  "verificati o popolari»"),
        "fonte": "parlato",
        "tocca": ".claude/skills/scan-strumenti-ai/SKILL.md",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "basso",
        "misura": ("la skill esiste ed e' invocabile; il suo primo output elenca gli strumenti "
                   "trovati per categoria con data. Le regole A4-L00-01/02 chiedevano a "
                   "self-improver.md di avere «un compito periodico», mai eseguito"),
    },
    {
        "id": "A4-RC-06",
        "tipo": "funzione",
        "regola": ("Quando lo strumento di raccolta transcript fallisce si prova una via di "
                   "riserva e si distinguono i due guasti — strumento muto contro video davvero "
                   "senza sottotitoli — invece di scartare il candidato. Senza distinguerli non "
                   "si puo' nemmeno misurare quanti buoni candidati si perdono."),
        "prova": ("L01-scaricare-testi/appunti.md @ 06:01 «puo' succedere che DownSub qualche "
                  "volta non funziona»; report L01 §2: «Cosa si fa se il transcript manca: ci si "
                  "ferma e si passa al candidato B. Nessuna via di riserva»"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/transcript_fallback.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("esiste una funzione di riserva che scrive nel log quale dei due guasti si e' "
                   "verificato; oggi transcript-collector.md §Playbook 3 dice solo «fermati, "
                   "candidato B» e la regola A4-L01-02 chiedeva di «nominare» la via di riserva"),
    },
    {
        "id": "A4-RC-07",
        "tipo": "script",
        "regola": ("Il tempo di produzione si cronometra per fase in automatico. Senza un numero "
                   "reale, «puntiamo sulla qualita'» non e' una scelta dichiarata ma una scusa "
                   "non falsificabile, e non si sa DOVE la catena rallenta."),
        "prova": ("L05-metodo-completo/appunti.md @ 00:35 «sono le 13 e 18» e @ 06:48 «ci ho "
                  "impiegato veramente 5 minuti per fare tutto» — l'intera lezione e' "
                  "cronometrata passo per passo"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/misura_tempo_produzione.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "basso",
        "misura": ("esiste un log per fase (fase, secondi, video_id) su almeno una produzione "
                   "vera; la regola A4-L05-04 chiedeva una voce da riempire a mano in "
                   "BASELINE.md, e nessuno script del motore contiene logica di cronometraggio"),
    },
    {
        "id": "A4-RC-08",
        "tipo": "funzione",
        "regola": ("La velocity di un video giovane si rapporta agli iscritti del canale "
                   "sorgente, altrimenti misura la base iscritti e non l'appeal del video. La "
                   "correzione va nel codice che genera il pool, non solo nel testo dell'agente."),
        "prova": ("L05-metodo-completo/appunti.md @ 01:09 «5.700 pollici in su, 89.000 "
                  "visualizzazioni, 13 ore fa»; L06-metodo-copia-incolla/appunti.md @ 07:02 «e' "
                  "normale che un video appena pubblicato faccia tante visualizzazioni, "
                  "soprattutto se ci sono tanti iscritti al canale»"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/build_candidate_pool.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("build_candidate_pool.py recupera subscriber_count e calcola una velocity "
                   "rapportata; oggi le righe 125-138 calcolano VPH = views/eta' e ordinano, "
                   "senza mai leggere gli iscritti. Le regole A4-L05-01 e A4-L06-01 cambiavano "
                   "solo cio' che l'agente DICE di fare"),
    },
    {
        "id": "A4-RC-09",
        "tipo": "flusso",
        "regola": ("Fra la raccolta del materiale e la scrittura manca uno stadio: «Bilancio "
                   "Materiale». Giudica se il materiale copre il fabbisogno, ordina fonti "
                   "aggiuntive invece di scartare il candidato, e consegna allo stadio dopo un "
                   "elenco esplicito di fatti da preservare. Oggi tre agenti si parlano solo "
                   "attraverso un file markdown e nessuno tiene insieme la catena."),
        "prova": ("L01 @ 05:44 (link salvato nella colonna NOTE del piano editoriale); L02 "
                  "@ 02:43 «aggiungi questa parte di testo senza essere ripetitivo e rendi "
                  "l'articolo originale»; L05 @ 05:53 «se io inserissi altre parti di testo... "
                  "sarebbe ancora meglio» — nel corso e' una sequenza unica cronometrata"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "ridisegna",
        "binario": "B",
        "rischio": "alto",
        "misura": ("la catena ha uno stadio nominato fra transcript-collector e script-writer che "
                   "riceve transcript + fonti e consegna un pacchetto con i fatti da preservare; "
                   "raccoglie in un punto solo cio' che A4-RC-02, A4-RC-04 e A4-RC-07 chiudono "
                   "separatamente"),
    },
    {
        "id": "A4-RC-10",
        "tipo": "script",
        "regola": ("Da un video orizzontale gia' prodotto si ricavano Shorts verticali tenendo il "
                   "soggetto a centro-inquadratura. La fabbrica genera un formato per canale e "
                   "non riusa mai un video lungo per produrne varianti brevi: e' una capacita' "
                   "assente, non uno strumento diverso per fare la stessa cosa."),
        "prova": ("RAPPORTO-GREZZO-L11.md §2.2 — «quando si cambia il formato della sequenza da "
                  "orizzontale a verticale, il soggetto principale sparisce dall'inquadratura» "
                  "@ 06:55-07:05; il reframe automatico lo ricentra anche in bulk @ 10:18-11:06"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/reframe_shorts.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("reframe_shorts.py esiste e produce un 9:16 col soggetto centrato da un MP4 "
                   "16:9 gia' esportato, senza rigenerare nulla da Fliki (zero costo API). La "
                   "regola A4-L11-01 diceva «noi generiamo gia' nel formato di destinazione», "
                   "vero solo per il caso diretto"),
    },
    {
        "id": "A4-RC-11",
        "tipo": "script",
        "regola": ("Il livello audio si misura in dB sul file esportato. Un gate bloccante che "
                   "ordina «ascolto obbligatorio ad alta fedelta'» a un agente chiede una cosa "
                   "che nessuna macchina puo' fare: e' un metro senza righello."),
        "prova": ("L08 @ 44:39-45:06 — musica portata da 0 dB a -25 dB («ancora troppo alta»), "
                  "chiusa a -35 dB; L18 @ 15:38-16:05 — «l'audio fa la differenza nel caso in cui "
                  "e' scadente»"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/audio_level_check.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "alto",
        "misura": ("audio_level_check.py misura livello medio e di picco con ffmpeg, e "
                   "quality_gate.py registra il gate corrispondente; oggi qa-audio-video.md §4.2 "
                   "dice «Controlla il video tramite l'anteprima» e quality_gate.py valuta solo "
                   "JSON di specifica, mai il file audio reale"),
    },
    {
        "id": "A4-RC-12",
        "tipo": "agente",
        "regola": ("Serve un gate di conformita' che legga lo script PRIMA della generazione e "
                   "cerchi nomi di persone reali con dichiarazioni messe in bocca loro, "
                   "personaggi protetti, e richieste che implicano materiale di terzi. Le nove "
                   "porte chiuse scritte in monetizzazione-compliance.md sono regole lette da un "
                   "umano, mai controllate da nessuno."),
        "prova": ("L15 @ 11:36-11:48 — l'avatar legge una finta notizia di lutto su un cantante "
                  "italiano reale, senza una parola su consenso; @ 09:08-10:52 — personaggio "
                  "Dragon Ball generato e fatto parlare, senza menzione di copyright"),
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/controllo/compliance-gate.md",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "alto",
        "misura": ("compliance-gate.md esiste, e' agganciato fra script-writer e video-producer, e "
                   "uno script di prova con un nome reale inventato produce un BLOCCO che cita la "
                   "porta chiusa esatta. Oggi regolatore-originalita misura solo somiglianza "
                   "n-gram e nessun agente legge lo script cercando nomi reali"),
    },
    {
        "id": "A4-RC-13",
        "tipo": "script",
        "regola": ("Cosa dice davvero l'audio generato si confronta con cosa doveva dire lo "
                   "script. I sottotitoli Fliki nascono dal testo inviato, non dall'audio: se il "
                   "TTS storpia o salta una parola, i sottotitoli mentono in silenzio su cio' che "
                   "si sente."),
        "prova": ("L12 @ 07:14-07:35 — il docente seleziona una frase trascritta male («grande "
                  "affetto dei suoi figli») e la corregge a mano dopo aver sentito che la "
                  "trascrizione non coincideva col parlato"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/verifica_pronuncia.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("verifica_pronuncia.py produce un diff testo-atteso contro testo-riconosciuto "
                   "(ASR locale) e scrive proposte in lessico-pronuncia.md; oggi il lessico si "
                   "riempie solo con gli errori che qualcuno ha sentito"),
    },
    {
        "id": "A4-RC-14",
        "tipo": "script",
        "regola": ("Lo strumento per intro e outro si costruisce ora e resta spento: la decisione "
                   "se usarli spetta a Max (BACKLOG), ma il lavoro tecnico non deve aspettarla. "
                   "Il giorno del si', il costo scende da «scrivere uno script» a «attivare un "
                   "flag» (ADR-028: l'attesa di una decisione non ferma il lavoro intorno)."),
        "prova": ("L10 @ 04:01 «ecco perche' vi consiglio di creare un'intro e anche un outro»; "
                  "@ 07:27 — l'intro allunga il video e lo rende riconoscibile come proprio"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/intro_outro_stitcher.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "basso",
        "misura": ("intro_outro_stitcher.py esiste e concatena due MP4 di prova senza ricodifica, "
                   "restando scollegato dalla produzione; oggi fliki_client.py:252 non ha alcun "
                   "campo per clip di apertura o chiusura e nessuno script concatena asset fissi"),
    },
    {
        "id": "A4-RC-15",
        "tipo": "flusso",
        "regola": ("La retention dei nostri video si legge dalla YouTube Analytics API sul canale "
                   "di proprieta', non si lascia a null. Finche' resta null, la regola «l'apertura "
                   "e' ritenzione» e' un atto di fede preso da un tutorial, che il nostro canale "
                   "non puo' ne' confermare ne' smentire."),
        "prova": ("L14 @ 09:36 e @ 11:35 — «e' fondamentale cambiare tutte le clip dei primi 30 "
                  "secondi... il tuo obiettivo non e' solo farlo cliccare, ma fargli vedere "
                  "l'intero video»"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/youtube_analytics_client.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("almeno un report di channel-performance-analyst mostra una retention reale "
                   "accanto allo stile di apertura; oggi l'agente dichiara che CTR e retention "
                   "«richiedono YouTube Studio, che e' privato» e scrive sempre null, usando solo "
                   "scraping pubblico — ma il canale e' nostro e l'API e' autenticabile"),
    },
    {
        "id": "A4-RC-16",
        "tipo": "agente",
        "regola": ("Serve un ruolo che confronti a cadenza fissa i campi del nostro payload con la "
                   "superficie reale dell'API del fornitore. Nessuno lo fa di mestiere: "
                   "regolatore-configurazione difende lo status quo, self-improver guarda solo le "
                   "nostre metriche. Le leve trovate il 2026-09-07 furono trovate per caso, "
                   "cercando altro."),
        "prova": ("VERIFICA-PAYLOAD-L20-GATE-A4.md — «il payload reale ha un campo che il nostro "
                  "codice non manda mai: bgMusicVolume»; RAPPORTO-GREZZO-L20 @ 44:53-46:04 su "
                  "generateSfx; L19/appunti.md — «Non nomina mai l'API, che pure e' una voce del "
                  "menu che ha davanti (frame-040)»"),
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/regolatori/regolatore-capacita-fliki.md",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "medio",
        "misura": ("il file esiste e il suo primo output elenca, con data, le leve API mai usate "
                   "dal nostro client; senza questo ruolo una leva gratuita resta invisibile per "
                   "mesi, come e' gia' successo"),
    },
    {
        "id": "A4-RC-17",
        "tipo": "skill",
        "regola": ("Il confronto fra payload nostro e schema del fornitore deve essere un comando "
                   "ripetibile in minuti, non una sessione di ricerca a mano una tantum. Il "
                   "metodo esiste gia' scritto (doppia lettura indipendente); manca il comando "
                   "che lo esegue."),
        "prova": ("VERIFICA-PAYLOAD-L20-GATE-A4.md riga 8 — «Non richiedono una sentinella sul "
                  "video: sono domande sull'API reale, non sul corso»; REPORT-CATEGORIA.md §6 — "
                  "«Tre verifiche nuove, assegnate al gate A4... tutte contro il payload reale»; "
                  "RAPPORTO-GREZZO-L20 @ 44:53"),
        "fonte": "parlato",
        "tocca": ".claude/skills/fliki-capability-audit/SKILL.md",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "basso",
        "misura": ("la skill esiste ed e' invocabile, e produce una tabella campo-per-campo "
                   "usato/non-usato con citazione della documentazione; e' il braccio operativo "
                   "di A4-RC-16"),
    },
]
