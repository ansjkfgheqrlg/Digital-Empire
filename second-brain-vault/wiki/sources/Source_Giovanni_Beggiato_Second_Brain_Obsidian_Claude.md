---
Type: SOURCE
Status: Active
Tags: #company-brain #obsidian #second-brain #claude-code #wikilink #zettelkasten #luhmann #gate-qualita #llms-txt #skill-journal #notion-mcp #giovanni-beggiato #max18
Created: 2026-09-06
Last updated: 2026-09-06
---

# Source: Giovanni Beggiato — Corso Completo Second Brain: Claude + Obsidian

## Overview

Corso di 2h18m50s (canale Giovanni Beggiato, agenzia Gentes/gentes.ai) in cui l'autore costruisce
**dal vivo, passo per passo, un'intera Company Brain** su un caso di studio fittizio (Aurora
Sistemi S.p.A.), usando Obsidian + Claude Code dentro l'IDE Antigravity. Non è una demo isolata
come il video "Karpathy" dello stesso autore ([[sources/Source_Giovanni_Beggiato_Company_Brain_Karpathy]]):
è il corso intero da cui quel deliverable tecnico viene poi venduto, e copre l'intero ciclo di vita
del cervello aziendale — dalla prima nota scritta a mano in Obsidian, all'estrazione del canon dai
documenti grezzi, alle 11 cartelle, al gate di qualità automatizzato, all'indice per le AI, allo
showcase per una demo commerciale, al version control, ai due layer visivi (cruscotto HTML +
Notion via MCP), fino alla memoria viva (skill journal con sessioni e diario giornaliero). Video 1
del lotto `max18` (l'altro è appunto il Karpathy, video 2).

**La tesi**: una company brain non è un esperimento di produttività personale, è la tecnologia che
separa chi usa l'AI per moltiplicare il proprio business da chi la usa solo per giocarci — perché
senza dati proprietari organizzati, un'azienda e il suo competitor che usano lo stesso modello
ricevono la stessa identica risposta, cioè zero vantaggio competitivo.

## Dati Tecnici

- **Video ID:** RnoC5IlOUhs · **Durata:** 2h18m50s · **Canale:** Giovanni Beggiato
- **Copertura:** 352 scene su 352 (100%), `video-analysis.md` 2.776 righe
- **KA:** 205 atomi, 333 archi tipizzati, **1 sola componente connessa, 0 orfani**
- **Run:** `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/max18-v01-second-brain-obsidian`
- **Formato:** talking-head + lavagna Excalidraw disegnata dal vivo + screen-share denso (Antigravity
  IDE, Obsidian, Notion, GitHub, Google, Skool) — 5 applicazioni tenute aperte in parallelo
  (RnoC5IlOUhs#105:24, KA-151)

## La tesi economica

Tre soli numeri di terze parti citati con fonte in tutto il video, il resto è materiale proprietario
dell'autore o dell'azienda-caso di studio:

- **19% della settimana lavorativa** (1 giorno su 5) speso dal settore impiegatizio a cercare
  informazioni — fonte dichiarata a schermo **McKinsey Global Report**, ricerchiata in rosso per
  enfasi — RnoC5IlOUhs#10:42, #16:30 (KA-016)
- **8-12 mesi** perché un nuovo assunto diventi davvero produttivo — fonte dichiarata **HBR**
  (Harvard Business Review); la trascrizione automatica del video rende erroneamente questo dato
  come "8-1 mesi", il frame mostra chiaramente 8-12 — RnoC5IlOUhs#10:42, #16:30 (KA-017)
- **"Quando una persona se ne va, si porta via la sua conoscenza"** — terzo dato della stessa slide,
  senza fonte citata — RnoC5IlOUhs#10:42 (KA-018)

**La conca della curva di apprendimento**, disegnata a mano sulla lavagna (assi Apprendimento/Tempo):
sale, scende in una conca, risale fino a un plateau. I tempi per superarla, raggruppati in rosso:
**3-6 mesi** per un top performer, **8-12 mesi** per un mid performer, **14-18 mesi** per un low
performer — RnoC5IlOUhs#13:54 (KA-019, KA-020). Sulla stessa curva, l'autore annota chi guadagna in
quale metà: la prima parte ("VOI GUADAGNATE", il dipendente durante l'apprendimento), la seconda
("AZIENDA GUADAGNA", dopo la risalita) — con un riquadro **"≤ 2 anni"** vicino all'asse Tempo: tesi
che l'azienda trattiene il dipendente almeno 2 anni perché solo dopo la conca comincia a guadagnarci
— RnoC5IlOUhs#15:12 (KA-021). Accorciare la conca ha tre implicazioni scritte a mano in rosso:
AZIENDA↑↑, JOB ROTATION↑↑, CHURN(%)↓↓ ⟹ $ — RnoC5IlOUhs#16:24 (KA-022).

**I 22.870 documenti** della company brain reale mostrata a schermo (graph view Obsidian a schermo
intero, sfera densissima di nodi con anello esterno di orfani): cifra letta sulla lavagna Excalidraw
dell'agenda. Nota **divergenza non riconciliata nel materiale**: la voce a 25:04 dice invece
"22.500 note" — il video usa entrambe le cifre senza risolvere lo scarto — RnoC5IlOUhs#0:18, #0:54,
voce 1:10/25:04 (KA-003, KA-004).

**L'arbitraggio**, definizione esplicita data a voce: *"la differenza tra quello che fate voi oggi e
quello che fa il mercato domani"* — vale sia per chi applica la company brain alla propria azienda
sia per chi la insegna/rivende (freelancer, agenzia, community) — RnoC5IlOUhs#23:18-23:36 (KA-031).
Il grafico ROI/Tempo che la precede mostra due curve: quella **senza** company brain cresce uguale
per tutti (competitor inclusi, quindi zero vantaggio competitivo), quella **con** company brain è
ripida e personale perché l'AI comincia a conoscere l'azienda sempre meglio — ed è esattamente
questo il vantaggio competitivo — RnoC5IlOUhs#21:54-22:06, #22:06 (KA-027, KA-028). Le aziende
grandi hanno il ROI migliore perché hanno già processi e conoscenza accumulata su cui allenare l'AI
(KA-028); un competitor entrato più tardi ha un **"LAG"** — il ritardo da colmare — RnoC5IlOUhs#23:12
(KA-030). Principio "data first": *"con l'AI i dati sono il nuovo oro [...] ma in questo caso sono i
vostri dati per la vostra azienda"* — RnoC5IlOUhs#22:24 (KA-029).

## L'architettura

**Tassonomia vs Ontologia** (schema Excalidraw dedicato, RnoC5IlOUhs#59:36): la **tassonomia**
risponde a *"che tipo di cosa è?"* e dice dove archiviare — è l'albero di cartelle (l'esempio dato:
"Progetti" che si dirama in "Progetti Interni"/"Progetti Clienti"). L'**ontologia** risponde a
*"cosa sono le cose e come si collegano?"* ed è "leggibile da una macchina" — esempio: "Aurora
Sistemi" (azienda) e "Marco" (persona) collegati da una freccia etichettata "lavora nel commerciale"
(KA-068, KA-069). Differenza pratica dichiarata: la tassonomia dell'autore è pensata per essere
agnostica rispetto al business e la fornisce già pronta; l'ontologia (la logica di collegamento) va
costruita da ciascuno — *"dovrete dare ad Obsidian il come colleghiamo queste cosine qui"*
(KA-070, KA-071).

**Le 11 cartelle**, poste alla radice del vault, ciascuna un "lavoro" specifico del cervello
aziendale. La decisione di archiviazione è una sola — quanto è azionabile il contenuto, non il suo
tipo — RnoC5IlOUhs#48:42, schema completo e annotato a #60:48 (KA-055, KA-056–066):

1. **`self`** — *chi è l'azienda*: obiettivi, missione, clienti, offerte. Punto di partenza
   gerarchico da cui discendono le aree (KA-056).
2. **`areas`** — *responsabilità continue*: i reparti stabili dell'azienda, distinti dai progetti
   che hanno un traguardo temporale (KA-057).
3. **`projects`** — *lavoro a tempo, con traguardo*: collegato al concetto di automazione una volta
   reso ricorrente (KA-058).
4. **`sources`** — *la inbox grezza*: articoli, appunti, note sparse non ancora elaborate
   (KA-059).
5. **`concepts`** — *idee, una per nota*: i concetti-chiave di business (es. ARR, churn) come note
   atomiche singole (KA-060).
6. **`docs`** — *procedure intere*: a differenza di concepts (un'idea per nota), ospita la
   procedura per intero, non spezzata — SOP (KA-061).
7. **`entities`** — *schede dei nomi propri*: persone/ruoli interni e fornitori/tool esterni
   (KA-062).
8. **`data`** — *i numeri*: i KPI e le metriche quantitative (KA-063).
9. **`code`** — *script e automazioni*: dove atterra un progetto one-off diventato processo
   ricorrente (KA-064, KA-067).
10. **`outputs`** — *deliverable finiti*: proposte, case study, contratti — l'altra destinazione
    possibile per un progetto che ha raggiunto il traguardo (KA-065, KA-067).
11. **`workspace`** — *bozze e diario*: diario di sessioni e riepiloghi giornalieri (journal/sessions
    e journal/daily), materiale non ancora finale (KA-066).

Regola del ciclo di vita: quando un progetto one-off (in `projects`) diventa ricorrente si sposta in
`code`; quando si conclude con un deliverable, si sposta in `outputs` (KA-067). Le 11 cartelle non
sono solo teoria: una finestra di sistema macOS mostra la company brain **reale** dell'autore, già in
produzione, con esattamente le stesse 11 cartelle — prova che lo schema Excalidraw corrisponde 1:1 a
una struttura di file operativa (RnoC5IlOUhs#57:00, KA-074). Prompt 1 del canovaccio (testo
integrale, eseguito parola per parola): *"Crea nel mio vault, alla radice, queste 11 cartelle vuote,
una per ciascun lavoro del cervello: self, areas, projects, sources, concepts, docs, entities, data,
code, outputs, workspace. Non crearne altre e non metterci dentro nessun file. Solo le 11
cartelle."* — tradotto da Claude Code nell'unico comando bash `mkdir -p self areas projects sources
concepts docs entities data code outputs workspace` (RnoC5IlOUhs#64:12, #65:18, KA-078, KA-079).

**La nota atomica** (slide "LA NOTA ATOMICA", sottotitolo *"Niklas Luhmann: una idea per scheda"*):
contrappone un PDF da 40 pagine tutto insieme ("nessuno lo riusa") a cinque caselle colorate, ognuna
un'idea, collegate in rete ("il valore è nei legami", "riusabile in 20 contesti") —
RnoC5IlOUhs#70:18, #74:24 (KA-089). Base teorica dichiarata a schermo ma non pronunciata a voce
dall'autore: lo **Zettelkasten di Niklas Luhmann**, **90.000+ schede** autonome con cui scriveva i
suoi libri, esemplificato con due schede collegate "FIDUCIA" e "SOLDI" — RnoC5IlOUhs#71:36 (KA-090).

**Hub-and-spoke** ("l'ordine di costruzione", *"come una ruota di bicicletta"*): al centro un HUB
(identità azienda, reparti), attorno sei nodi "dettaglio" collegati al centro e tra loro. Ordine:
*"1) prima gli hub, 2) poi i dettagli"*, con la regola conseguente *"Ogni link punta a qualcosa che
esiste già, quindi i link rotti sono impossibili"* — RnoC5IlOUhs#74:30, #75:54 (KA-091). Il Prompt 3
impone lo stesso ordine sulle note reali: prima gli hub/note-mappa (`self-identita-aurora` come hub
centrale), poi il dettaglio, con vincolo assoluto *"Un wikilink punta solo a una nota che esiste
già"* (KA-092, KA-093).

**Il Canon**, definito dal Prompt 2 ("Estrai il canon"): *"Congela i fatti duri dell'azienda in un
unico canon coerente"* — un file unico che copre identità, prodotti, reparti, persone, clienti (con
i loro numeri) e KPI di fine anno — RnoC5IlOUhs#65:48, #68:12 (KA-084). Regole d'oro: nessun fatto
inventato (*"se non è nel materiale in sources/, NON scriverlo"*) e i numeri devono **quadrare** tra
loro (KA-085). Il canon è dichiaratamente *"un file di lavoro, non una nota finale"*
(`workspace/canon.md`, KA-088): un'analogia disegnata a mano lo mostra come un "bacinello" pieno che
si spezza in 11 "microbacinelle", una per cartella (KA-086).

**Canon vs override** — il meccanismo che rende il canon aggiornabile senza riscriverlo: quando un
fatto cambia (es. l'ARR di un cliente), Claude Code non tocca la scheda canonica in `entities/` ma
scrive un file separato in `workspace/overrides/` (es. `cliente-polo-universitario-sud.md`),
dichiarato "non sarà coperto da generate_notes" — cioè uno script che rigenera le schede canoniche
non lo cancella — RnoC5IlOUhs#28:36-28:42 (KA-034, KA-037). Comando ricostruito per scrivere
l'override: `python3 scripts/edit_fact.py --nome "<Nome Cliente>" --campo <campo> --valore <valore>
--date <data>`, seguito dalla propagazione completa `python3 scripts/propagate.py` (canon, views,
Qdrant, Notion, audit) — RnoC5IlOUhs#28:42 (KA-036). Prima di rispondere a una domanda, Claude Code
controlla **sempre** se esiste un override più recente sul record specifico prima di usare la vista
aggregata (RnoC5IlOUhs#28:36, KA-034) — verificato end-to-end fino a Notion, che riflette il nuovo
valore senza intervento manuale (RnoC5IlOUhs#29:18, KA-038).

## Il problema degli orfani e la soluzione `_index`

Distinzione chiave enunciata a sola webcam, in sequenza di sei scene: *"Vogliamo avere file orfani a
livello concettuale, ma non orfani a livello grafo, ok?"* — RnoC5IlOUhs#84:54-85:24 (KA-105). Un
**orfano concettuale** (nessuno lo cita a voce nella conversazione quotidiana, es. gli appunti presi
a un meeting "buttati lì a calcioni") è accettabile; un **orfano di grafo** (zero wikilink in
entrata) no, *"perché vogliamo comunque che lei [l'AI] vada dentro"* — se una nota non è collegata a
nulla, l'AI non ha modo di raggiungerla anche quando l'utente le chiede di recuperarla (KA-105). La
metrica che conta per un vault non è quante diramazioni ha una nota, ma **quanti file la
referenziano**: *"non c'è nessuno che va a parlare con il nostro Canon [...] il problema [...] è
quanti file riferiscono alla nostra nota"* — dimostrato dal vivo su `canon.md` con "0 backlinks"
nella barra di stato di Obsidian, prova diretta che il file era orfano di grafo — RnoC5IlOUhs#78:30,
#86:24-86:42 (KA-098, KA-107).

**La soluzione**, annunciata a voce come *"SL/index"* (slash-index) durante una dissolvenza
incrociata webcam→graph view: un file `_index` per ogni cartella, che dà a ogni nota almeno un link
in entrata dal suo indice — RnoC5IlOUhs#85:30-85:36 (KA-106). Comando dell'utente che innesca la
creazione effettiva: *"[...] assicurati di avere: un front matter, un indice (un `_index`) che possa
evitare note orfane all'interno del progetto"* — RnoC5IlOUhs#88:30 (KA-113). Risultato: **11 `_index`
di cartella + 1 indice madre `_index-aurora.md`** alla radice, struttura a tre livelli — indice madre
→ indice di cartella → nota — con nomi unici (`_index-<cartella>`) per non rompere la risoluzione
wikilink di Obsidian. Esito dichiarato: *"44 file .md, tutti con frontmatter [...] Zero link rotti,
zero note orfane"* — RnoC5IlOUhs#88:42, #93:36 (KA-114). Esempio completo del pattern, file
`outputs/_index-outputs.md`: frontmatter + corpo con sezione "## Salendo" che rimanda all'indice
madre e ai reparti proprietari — RnoC5IlOUhs#88:54 (KA-116). Verifica finale in Obsidian: *"E come
vedete ora abbiamo il collegamento a Canon [...] il nostro Canon non è più una nota orfana"* —
RnoC5IlOUhs#89:06 (KA-117).

Nota d'uso del Graph view, ribadita a sola webcam: *"il grafo sarà per l'AI, ma noi dobbiamo sapere
leggere cosa va male nel grafico [...] abbiamo anche una maniera visiva e il toggle [...] trova gli
orfani"* — il grafo non è uno strumento di lavoro quotidiano per l'utente umano, ma resta il
diagnostico visivo per individuare note isolate — RnoC5IlOUhs#86:54-87:24 (KA-109).
