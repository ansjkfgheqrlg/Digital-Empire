---
Type: SOURCE
Status: Active
Tags: #voice-ai #agenti-vocali #vapi #retell #n8n #claude-code #ai-receptionist #giovanni-beggiato #max18
Created: 2026-09-09
Last updated: 2026-09-09
---

# Source: Giovanni Beggiato — AGENTI VOCALI IN CLAUDE CODE: Costruisci e Vendi

## Overview

Video di 133m11s (~2h13m, canale Giovanni Beggiato, run `max18-v09-NmoOZVTrTXA`) — **il più lungo
e il più denso del lotto `max18`**: 494 scene, 323 atomi (KA-001..KA-323), 360 archi, 5 componenti
connesse, 0 orfani (numeri ricalcolati e chiusi in questa sessione, checkpoint `CP-20260909-2CWF`,
ripresa `EMP-W4K7`). Corso completo in 13 capitoli su come costruire, personalizzare e vendere
**agenti vocali AI** (voice agent telefonici) usando le piattaforme Vapi e Retell per la pipeline
vocale, n8n per l'automazione di backend, e Claude Code come motore di orchestrazione che scrive
system prompt, crea assistenti via API, costruisce workflow e fa debugging in autonomia. Nota di
fonte: questo video **non aveva sottotitoli YouTube** (verificato con yt-dlp), il transcript è
ricostruito dall'audio con faster-whisper — le citazioni testuali possono contenere imprecisioni di
trascrizione automatica su nomi propri di prodotto (es. "cattare" per "chattare", refusi minori),
mentre i dati letti direttamente dai frame video (dashboard, canvas Excalidraw, codice) restano
affidabili al 100%.

## Cos'è un agente vocale: anatomia e limite senza tool

Il corso apre dichiarando esplicitamente il proprio scopo — *"come costruire agenti vocali da
zero, come integrarli in processi aziendali e qual è il ritorno concreto per le aziende"* —
NmoOZVTrTXA#0:06 (KA-001) — seguito da un'agenda su lavagna Excalidraw che promette **"i 5 tipi di
tool che puoi integrare"** — NmoOZVTrTXA#0:30 (KA-002). Primo segnale di rigore della fonte, colto
dallo studio e non dal video stesso: il diagramma realmente mostrato più avanti si intitola **"4
Tipi di tool"** e ne classifica solo 4 (Default, Custom, Code, Integration) — discrepanza tra
promesso e consegnato, osservabile e non dichiarata a voce — NmoOZVTrTXA#0:30 e #25:18 (KA-003).

L'anatomia di un agente vocale è un diagramma a tre blocchi in sequenza: *"utente parla ->
trascrizione -> LLM genera risposta -> generazione audio -> utente sente la voce"* —
NmoOZVTrTXA#4:00 (KA-011): 1) Riconoscimento Vocale (ASR/Speech-to-Text), 2) LLM (intento,
significato, contesto), 3) Sintesi Vocale (TTS). Il motivo per convertire prima il parlato in
testo invece di far elaborare l'audio grezzo all'LLM: *"definito testo in particolare tende a
capire meglio quello che noi poi vedremo"* — NmoOZVTrTXA#4:54 (KA-013). Il meccanismo che decide
quando questo processo parte è l'**Endpointing** — *"l'ENDPOINTING decide quando il processo parte
/ si ferma"* — NmoOZVTrTXA#4:00 (KA-012).

Il limite fondamentale, dimostrato dal vivo con un test di prenotazione sull'assistente demo: senza
tool collegati l'agente dichiara di voler verificare una disponibilità che **non può realmente
controllare** — *"questo però non può farlo, perché al momento noi non gli abbiamo dato nessun modo
di accedere ad un'agenda, controllare il CRM"* — NmoOZVTrTXA#24:42 (KA-049) — da cui il principio
esplicito: *"La gente ad ora può solo cattare o parlare"* [sic, trascrizione whisper per
"chattare"] — NmoOZVTrTXA#24:48 (KA-050). Un agente vocale senza tool è, testualmente, solo
conversazione: non azione.

## Vapi vs Retell: le due "go to platform"

Le due piattaforme di riferimento dichiarate esplicitamente: *"Quindi queste sono le due GO TO
PLATFORMS"* — NmoOZVTrTXA#2:24 (KA-004). Il confronto operativo: *"RETELL è molto più
beginner-friendly"* — NmoOZVTrTXA#2:24 (KA-005) — mentre *"vapi permette di fare qualcosa di un
po' più sofisticato"* (più tipi di tool, provider e opzioni) ma con latenza meno controllabile
dall'interfaccia — NmoOZVTrTXA#3:48 (KA-007). Sul lato modelli, il corso mostra a schermo un intero
listino latenza/costo per fascia OpenAI dentro Vapi, dalla fascia più lenta a quella più rapida:
*"GPT 4o Mini Cluster — 390 ms · $ 0.01"* contro *"GPT o3 Mini Cluster"* a 2400ms nella fascia
reasoning — NmoOZVTrTXA#10:18 (KA-020), con l'osservazione pratica che un agente per chiamate
schedulate non real-time (es. fornitori contattati sempre alle 9 del mattino) non ha bisogno del
modello più veloce.

## Il system prompt: "la cosa più importante"

Dichiarazione diretta del relatore, più determinante della scelta di modello/voce/transcriber:
*"Abbiamo detto che questa è la cosa più importante ed è un prompt"* — NmoOZVTrTXA#12:18 (KA-026).
La struttura completa, disegnata componente per componente su Excalidraw — *"abbiamo otto
componenti, se non sbaglio, anzi, nove, perché ho messo anche gli esempi"* — NmoOZVTrTXA#13:42
(KA-031): Identità & Personalità, Stile di Parlata, Regole di Interazione, Azioni Concrete (Flusso
Task), Informazioni Aziendali (Contesto), Rilevamento Urgenza, Profili Chiamante, Tool &
Guardrail, Gestione Errori & Esempio. Un dettaglio d'autore rilevante: la regola "non inventare
mai" nel componente Guardrail non è teoria astratta ma cicatrice reale — *"il primo agente che ho
fatto nove mesi fa era non ho detto non inventare cose"* — NmoOZVTrTXA#17:30 (KA-041).

Il template è reso disponibile gratuitamente su un documento Notion pubblico (accessibile senza
iscrizione a pagamento), un *"80-20 di quello che metterai"* — NmoOZVTrTXA#18:42 (KA-042),
condensato in 5 macro-sezioni Markdown (# IDENTITÀ, # STILE, # LINEE GUIDA RISPOSTA, # TASK, #
CONTESTO) — NmoOZVTrTXA#18:42 (KA-043). Il caso di studio ricorrente per tutto il resto del corso è
un receptionist di nome "Marco" per la "Giovanni Beggiato Clinica Dentale" fittizia — *"Sei Marco,
il receptionist della Giovanni Beggiato Clinica Dentale"* — NmoOZVTrTXA#19:12 (KA-044), poi
riutilizzato identico anche nella build finale end-to-end.

## I 4 tipi di Tool — e la regola d'oro sulla Knowledge Base

Classificazione concettuale a 4 tipi (non i nomi esatti, ma il modello mentale conta): *"Allora,
abbiamo quattro tipologie di strumenti"* — NmoOZVTrTXA#25:18 (KA-051): **Default Tools**
(preinstallati dalla piattaforma, es. trasferimento chiamata), **Custom Tools** (webhook verso un
sistema proprio esterno), **Code Tools** (codice TypeScript eseguito dentro la piattaforma stessa,
senza backend esterno), **Integration Tools** (workflow gia' esistenti su Make/GHL). La differenza
Custom/Code è dove "vivono": *"i custom tools sono cose che si connettono al vostro database... i
code tool vivono dentro vapi"* — NmoOZVTrTXA#26:30 (KA-054).

Il capitolo sulla Knowledge Base annuncia esplicitamente **4 metodi** di inserimento — *"Come
inseriamo una knowledge base & implicazioni"*, presentato come *"una delle cose più importanti che
un sacco di persone sbagliano"* — NmoOZVTrTXA#32:42 (KA-074): 1) Nel Prompt, 2) Inserimento tramite
file, 3) Tramite Tool, 4) Tramite Funzioni Custom. **Seconda discrepanza verificata dallo studio,
gemella di quella sui tool**: il riepilogo finale dello stesso capitolo, poche scene dopo, elenca
solo **tre** metodologie — *"1. Nel Prompt / 2. Inserimento tramite file / 3. Tramite Tool"* —
NmoOZVTrTXA#44:36 (KA-089) — il quarto metodo annunciato ("Tramite Funzioni Custom") non viene mai
ripreso né nel confronto pratico né nel riepilogo. Stesso pattern di over-promise-in-apertura visto
per i tool: titolo/apertura di capitolo dichiara N, il contenuto realmente erogato copre N-1.

Del confronto reale a 3 vie: il Metodo 2 (file collegato all'assistente) è giudicato esplicitamente
*"il peggiore che voi potiate fare"* — NmoOZVTrTXA#40:12 (KA-080), perché *"che averlo qua significa
che lo stiamo continuando a ricaricare ogni volta"* ad ogni turno di conversazione, a prescindere
dalla pertinenza — NmoOZVTrTXA#41:48 (KA-081). Il Metodo 3 (tramite tool Query) vince perché
interrogato **onDemand**: *"chiamiamo onDemand. Che cosa vuol dire? Che non viene chiamata sempre,
viene chiamata solo quando ne abbiamo bisogno"* — NmoOZVTrTXA#43:06 (KA-083). Raccomandazione
operativa finale, ripetuta due volte nel video: *"tra queste tre metodologie, se partite per i
vostri primi progetti, qui è dove andiamo... tramite tool è la nostra soluzione"* —
NmoOZVTrTXA#44:36 (KA-090).

## Latency tuning: le tre leve

Definizione operativa: *"È l'intervallo di silenzio, chiamiamolo così, ok, per capirci"* tra la
fine del turno utente e l'inizio della risposta dell'agente (e viceversa) — NmoOZVTrTXA#45:12
(KA-095). La latenza totale si controlla su tre punti distinti della pipeline — *"questi modelli
qui sono quelli che vanno ad impattare la vostra latenza"* — NmoOZVTrTXA#46:30 (KA-099): provider
ASR, provider LLM, provider TTS. Principio di compensazione tra qualità del prompt e potenza del
modello: *"se noi riusciamo ad avere un buon prompt iniziale, dove se il prompt è buono il modello
può essere un po' più scarso"* — NmoOZVTrTXA#47:12 (KA-102) — ma senza un valore universale: *"non
sempre la menor latenza è la migliore dell'universo, ci sono le varie casistiche aziendali"* —
NmoOZVTrTXA#49:12 (KA-103), correggendo esplicitamente l'assunzione ingenua "meno latenza sempre
meglio" appena mostrata coi numeri.

L'esempio operativo più riproducibile del capitolo è una PATCH reale via API applicata da Claude
Code su un assistente Vapi già pubblicato, che cambia 4 parametri insieme per ridurre latenza e
"roboticità": LLM da GPT-4o a GPT-4o-mini, voce ElevenLabs da `eleven_multilingual_v2` a
`eleven_flash_v2_5` (ottimizzato bassa latenza), Stability da 0.5 a 0.3 (più espressiva), Similarity
Boost da 0.75 a 0.85 — NmoOZVTrTXA#91:18 (KA-214), risultato misurato: costo/latenza passano da
~$0.12/min e ~2000ms a ~$0.11/min e ~665ms — NmoOZVTrTXA#89:36 (KA-213).

## I 4 file .md di setup in Claude Code

Il progetto di un agente vocale costruito con Claude Code si organizza attorno a **quattro file
markdown** nella cartella principale, pensati come un anello di riferimenti incrociati e non come
documenti isolati: *"CLAUDE.md, n8n.md, vapi.md, voice_agent.md / avremo bisogno di un Cloud.md che
sono le istruzioni generali di progetto"* — NmoOZVTrTXA#59:12 (KA-140). La distinzione concettuale dietro ogni file esterno documentato: *"l'MCP
dà accesso a i vari strumenti di Anethen [Anthropic]. Le skill dicono a Cloud come deve usare
questi strumenti"* — NmoOZVTrTXA#61:18 (KA-145) — due livelli complementari, non intercambiabili.

Per n8n, il file riscritto impone un **processo obbligatorio a 6 step** per ogni richiesta di
workflow — *"Per OGNI richiesta di workflow, segui questi 6 step in ordine. Non saltarne nessuno"*
— NmoOZVTrTXA#65:42 (KA-155): Clarify & Plan, Research Nodes, Write Expressions/Code, Build,
Validate, Deploy. Per attivare l'MCP server dentro Claude Code, si scrive un `.claude/settings.json`
con `mcpServers` e **si ricarica la sessione** prima che i nuovi tool diventino disponibili —
NmoOZVTrTXA#71:54 (KA-176). Il file `vapi.md` finale, pianificato in 12 sezioni, culmina in una
**Sezione 11** che definisce il template di prompt "definitivo": 12 sezioni obbligatorie da
compilare sempre tutte — IDENTITÀ, STILE, LINEE GUIDA RISPOSTA, TASK, CONTESTO, RILEVAMENTO
URGENZA, TIPI DI CHIAMANTE, TOOL, GUARDRAIL, GESTIONE ERRORI, ESEMPIO DI CONVERSAZIONE, NOTE —
*"Compila TUTTE le sezioni del template — non saltarne nessuna"* — NmoOZVTrTXA#93:18 (KA-218).

## Costruire l'AI Receptionist end-to-end

La build finale segue un principio dichiarato esplicitamente prima ancora di dettare il prompt:
*"vorrei che tu ragionassi per sistemi, quindi non vorrei che tu facessi un mischiotto di tutto"* —
NmoOZVTrTXA#98:24 (KA-228), tradotto in **4 workflow separati**: *"uno e' per il booking - uno e'
per la cancellazione - uno e' per il scheduling"* (+ uno per le FAQ) — NmoOZVTrTXA#101:24 (KA-229),
su un system prompt che replica lo stesso schema a 5 tool con condizioni d'uso non sovrapponibili
(check_availability, book_appointment, cancel_appointment, reschedule_appointment,
search_knowledge_base) — NmoOZVTrTXA#104:48 (KA-254). Il principio metodologico più citabile
dell'intero video, detto a webcam prima di inviare un prompt dettato per 8 minuti filati: *"preferite
dare l'informazione e spiegarla bene ... una volta sola e metterci dieci minuti oppure metterci sei
ore"* — NmoOZVTrTXA#104:00 (KA-243).

Il debugging in produzione è documentato con la stessa onestà del resto del corso: un bug reale di
mismatch di path (*"VAPI invia toolCallList[0].function.arguments ... ma i nostri Code node cercano
toolCallList[0].arguments (manca .function. nel path)"* — NmoOZVTrTXA#120:48, KA-305) viene trovato
lanciando **due sub-agenti Claude Code in parallelo**, uno sui log n8n e uno sullo stato
dell'assistant Vapi — NmoOZVTrTXA#119:48 (KA-302) — e risolto insieme a un secondo bug di
integrazione mancante (booking scritto solo su Google Sheet, senza Google Calendar collegato).
Dopo il fix, il test
end-to-end conferma la doppia scrittura funzionante: una prenotazione via chat appare sia come riga
nel foglio sia come evento su Calendar — NmoOZVTrTXA#123:18 (KA-310) — e una cancellazione rimuove
entrambi correttamente — NmoOZVTrTXA#124:06 (KA-313).

## Le 4 offerte per aziende: i modelli di business

Capitolo di chiusura tecnica, lavagna "Offerte per aziende": classificazione dei modelli voice/AI
per potenziale di reddito annuo — *"01 AI Recruitment ... $200k - $700k ... 05 AI Receptionist —
Few $100 ... $20k - $120k"* — NmoOZVTrTXA#126:24 (KA-315): AI Recruitment $200k-700k (difficoltà
medio-alta, pagato a percentuale su candidato/cliente chiuso — KA-322), Lead Reactivation
$150k-500k (pagato a percentuale sul revenue recuperato, modello win-win — KA-321), AI Customer
Support $120k-400k (valore piu' alto su nicchie a ticket alto, es. e-commerce con recupero ordini
abbandonati — KA-318), AI Receptionist $20k-120k — costo di realizzazione il più basso di tutti
("poche centinaia di euro"), ma per arrivare a circa 20.000 euro al mese servono *"un ottantino, un
centinaio di clienti"* — NmoOZVTrTXA#127:18 (KA-316), venduto a retainer mensile contenuto.

Framework aggiuntivo per leggere il valore economico di una funzione aziendale: *"le cose dentro, le
cose nel bordo, le cose fuori, questo vale un po' per tutto"* — NmoOZVTrTXA#131:24 (KA-319) — le
funzioni "dentro" (processi interni, basso impatto), "di bordo" (lead che già conoscono l'azienda,
valore medio — il marketing vi rientra), "fuori"/outbound (chi non conosce l'azienda, valore più
alto, esecuzione più difficile — vendite e tech vi rientrano, *"sono quelli che prendono piu' soldi.
Perche'? Perche' siamo sempre in outbound"* — NmoOZVTrTXA#132:18, KA-320). Il video chiude con una
doppia call-to-action: soluzione su misura per PMI, e coaching program di 90 giorni per chi vuole
imparare a vendere queste soluzioni — NmoOZVTrTXA#132:42 (KA-323).

## Cosa ne ricava Digital Empire

Sezione mia, dichiarata come tale: nessuna patch applicata, nessuno script toccato — Fase 1 resta
solo studio. Verifica fatta con `Grep` su `company/Memory/` e `second-brain-vault/wiki/`, non a
naso.

**Il gap è reale e verificato: DE non ha nessun canale vocale.** Cercando "agente vocale", "voice
agent", "Vapi", "Retell", "AI Receptionist" in tutto `company/Memory/` e in tutta la wiki, gli unici
riscontri sono il checkpoint di questa stessa sessione (`CP-20260907-MUPD.md` cita esplicitamente
"agenti vocali AI — VAPI/11labs/n8n/Claude Code" come task in corso) e alcuni falsi positivi
generici in file legacy non pertinenti. **Nessuna occorrenza precedente.** L'intera infrastruttura
di outreach automatico di DE — [[tools/Tool_Outreach_Message_Team]] (4 agenti: rule-keeper,
message-writer, case-study-forge, followup-sequencer) e il progetto Preventa Outreach Automation —
opera **esclusivamente su canali testuali asincroni**: WhatsApp, email, LinkedIn DM. Zero telefonia,
zero voce, zero tempo reale. Questo video documenta un canale completamente scoperto in casa.

**La connessione più diretta, non inventata**: le "4 offerte per aziende" del capitolo finale (KA-315)
sono un candidato letterale per un nuovo servizio produttizzato dell'agenzia CRO di DE
("l'agenzia progettata per essere licenziata", sprint 2-4 settimane, pay-on-performance).
L'AI Receptionist in particolare ha il costo di build più basso del lotto ("poche centinaia di
euro" per assistente, KA-315) e richiede un modello a volume (80-100 clienti/retainer, KA-316) — lo
stesso schema "un motore, N istanze clonate" che DE ha già validato e in produzione su
[[01 - Projects/Project_Prof_Autocad_PreventivoForge|PreventivoForge]] (un motore condiviso, N app
clonate per concessionario, kill-switch via Gist). Non un'ipotesi: è lo stesso pattern di
scalabilità applicato a un dominio diverso (voice invece di PDF).

**Cosa questo video aggiunge, tecnicamente, rispetto a quanto DE ha già letto sullo stesso autore
nello stesso lotto**: [[sources/Source_Giovanni_Beggiato_Company_Brain_Karpathy]] (max18-v02)
documenta il pattern "memoria persistente tra sessioni Claude Code" applicato a un Company Brain;
questo video applica lo **stesso identico pattern** (cartella `.claude/projects/<progetto>/memory`
con `MEMORY.md` indice, comando breve "ok continua" per riprendere — KA-178/KA-179) a un progetto
tecnico di automazione, confermando che non è un caso isolato ma un'abitudine riproducibile
dell'autore su Claude Code. Non l'ho verificato altrove in DE: se questo pattern di memoria non è
già codificato in una skill DE riusabile, è un gap tecnico a sé (distinto dal gap sul voice channel)
degno di una nota separata in futuro, che qui mi limito a segnalare.

**Cosa non ho verificato**: se il framework "dentro/bordo/fuori" (KA-319) sia già presente, con
nome diverso, in `agency-scalping` o `cro-empire` per la definizione dei servizi produttizzabili —
domanda aperta, non chiusa in questa sessione.

## Connessioni

- [[tools/Tool_Outreach_Message_Team]] — il sistema di outreach automatico reale di DE: stesso
  obiettivo (contattare/servire lead automaticamente) ma su canali testuali asincroni, mai voce.
  Il contrasto più diretto di tutta questa pagina.
- [[01 - Projects/Project_Prof_Autocad_PreventivoForge|PreventivoForge — Cliente Novacar srl]] — lo
  stesso pattern di scalabilità ("un motore, N istanze clonate per cliente", kill-switch via Gist)
  che il modello di business AI Receptionist di questo video (KA-315/KA-316) replicherebbe su un
  dominio diverso.
- [[sources/Source_Giovanni_Beggiato_Company_Brain_Karpathy]] — stesso autore, stesso lotto max18:
  lo stesso pattern di memoria persistente tra sessioni Claude Code (MEMORY.md + "ok continua")
  osservato qui in un contesto di automazione tecnica invece che di company knowledge.
- [[sources/Source_Riccardo_Belli_Risparmiare_Token_Claude_Code]] — stesso lotto max18, stesso
  strumento (Claude Code): tecniche di gestione token/contesto (sub-agenti paralleli, CLAUDE.md per
  cartella) osservate qui applicate in pratica durante il debugging del bug toolCallList (KA-302).
- [[sources/Source_Giovanni_Beggiato_LinkedIn_Generare_Clienti]] — stesso autore, stesso lotto
  max18: lì il canale di acquisizione clienti è LinkedIn/cold DM, qui il prodotto venduto è un
  agente vocale — nessuna sovrapposizione di contenuto, utile lette insieme per il quadro completo
  del posizionamento commerciale dello stesso creator.
