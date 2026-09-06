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

## Gli automatismi

**`gate_qualita.py`** — Prompt 5 del canovaccio Notion ("Il gate di qualità — solo referto"), testo
integrale: *"Crea un [ ] python che faccia [i]l gate di qualità sul cervello di Aurora. Passa 11
cartelle (salta solo sources/ e workspace/, che sono materiale grezzo e scratch) e controllala
contro queste sei regole [...]. Se è tutto in regola, rispondi solo: 'OK, 0 errori'."* —
RnoC5IlOUhs#92:36 (KA-118). **Le 6 regole**, testuali:

1. Frontmatter completo: `title, summary, tags, status, created, updated`.
2. Massimo 300 righe di corpo per nota.
3. Almeno 3 wikilink `[[...]]` in uscita verso note che esistono davvero (bersagli unici, non lo
   stesso link ripetuto; gli `_index` non valgono).
4. Zero link rotti: ogni `[[bersaglio]]` punta a una nota che esiste.
5. Zero orfani: ogni nota ha almeno 1 link in ENTRATA (gli `_index` sono esentati).
6. Una sola componente connessa: tutto il grafo è un unico grappolo, non due isole.

Uso: `python3 gate_qualita.py` (exit code 0 se pulito, 1 se trova errori — utilizzabile in un hook
pre-commit). Codice sorgente aperto in editor e riportato riga per riga fino al taglio del frame
(RnoC5IlOUhs#95:24, KA-125):

```python
#!/usr/bin/env python3
"""
Gate di qualita' sul cervello di Aurora.
Setaccia ogni nota delle 11 cartelle, saltando sources[...taglio bordo destro]
e la controlla contro 6 regole. Stampa un referto ragg[...taglio]
Uso: python3 gate_qualita.py
"""

import os
import re
import sys

VAULT = os.path.dirname(os.path.abspath(__file__))
SKIP = {"sources", "workspace"}          # material[...taglio]
FOLDERS = ["self", "areas", "projects", "c[...taglio]",
           "entities", "data", "code", "outputs"]  # [...taglio]
REQUIRED_FM = ["title", "summary", "tags", "status", [...taglio]
MAX_BODY_LINES = 300
MIN_OUT = 3

def is_index(stem):
    return stem.startswith("_index")

def split_fm(text):
    """Ritorna (dict_chiavi_presenti, corpo). Frontmat[...taglio]"""
    m = FM_RE.match(text)
    if not m:
        return None, text
```

Prompt 6 ("Correggi e ripeti finché esce '0 errori'"), che istituisce il ciclo automatico
correggi→verifica→ripeti: *"Correggi le note che hai appena segnalato [...]. Poi rifai il gate da
capo e mostrami il nuovo referto. Ripeti finché non esce 'OK, 0 errori'."* — RnoC5IlOUhs#95:48
(KA-119). Primo run reale: *"Ha setacciato le 28 note delle 9 cartelle scansionate (le 11 meno
`sources/` e `workspace/`) e tutte e 6 le regole passano"* (numero poi autocorretto: il vero
conteggio, ricalcolato, è **39 note** — 30 di contenuto + 9 hub — RnoC5IlOUhs#95:12, #103:48,
KA-124, KA-141).

**`genera_llms.py` / `llms.txt`** — Prompt 7 ("Genera l'indice per la AI"), testo integrale: *"Genera
il file llms.txt nella radice del vault: è l'indice-porta per la AI. Per ogni cartella di contenuto
(self, areas, projects, docs, entities, data, code, outputs) elenca le note nel formato '- [[nome-
file]] — summary', prendendo il summary dal frontmatter di ogni nota. [...] NON inventare niente:
title e summary vengono SOLO dal frontmatter delle note. Ricordati che llms.txt è DERIVATO: si
rigenera da capo, non si modifica a mano."* — RnoC5IlOUhs#95:48 (KA-120). Scelta motivata di Claude:
esclude i file `_index-` dall'elenco, perché sono scaffolding di navigazione (*"summary del tipo
'Mappa della cartella X'"*), non contenuto — *"un door-index per AI è più utile se punta alle note
vere"* — RnoC5IlOUhs#96:42 (KA-127). Comando reale, concatenato per rigenerare e verificare al volo:

```
cd "/Users/giovannibeggiato/Desktop/aurora cervello" && python3 genera_llms.py && echo "=== llms.txt ===" && cat llms.txt
```

RnoC5IlOUhs#96:54 (KA-130). Risultato: 30 note indicizzate in 9 cartelle, sources/ e workspace/
esclusi, file `_index-` esclusi (KA-131, KA-132). Regola d'uso, letta a schermo: *"Lo script
`genera_llms.py` riscrive `llms.txt` da capo leggendo i frontmatter correnti. Quando aggiungi o
modifichi note, rilancialo e l'indice si aggiorna da solo."* — con la stessa base di assunzioni del
gate di qualità (stesse 9 cartelle, stesso parsing frontmatter), tanto che il sistema propone di
incatenare i due comandi in un unico hook pre-commit (gate → solo se 0 errori, rigenera llms.txt) —
RnoC5IlOUhs#97:42-97:48 (KA-133). L'autore dichiara esplicitamente che llms.txt **non è uno standard
di settore**, ma una sua raccomandazione personale: *"Non è una best practice, è una raccomandazione
dello zio Jo, vedete voi cosa farne"* — RnoC5IlOUhs#97:48 (KA-134).

**`genera_showcase.py` / `showcase.md`** — Prompt 8 ("Lo showcase — la fotografia per la demo"),
testo integrale: *"Fammi lo showcase del cervello di Aurora: una fotografia da mostrare in una demo.
Conta tutte le note (le 11 cartelle, salta sources/ e workspace/), i wikilink totali che le tengono
insieme, e quante componenti connesse ha il grafo (1 = tutto collegato). Poi dammi una tabella 'note
per cartella' e, sotto, l'elenco degli hub (i più linkati). Prendi il summary dell'`_index` di ogni
cartella. Salva tutto in `_showcase/showcase.md`. È una fotografia DERIVATA: si rigenera, non si
scrive a mano."* — RnoC5IlOUhs#95:48, #98:24-99:18 (KA-121, KA-135). Contenuto reale generato: **39
note totali** (30 contenuto + 9 hub), **262 wikilink**, **1 componente connessa** — RnoC5IlOUhs#99:30
(KA-137, KA-138). Tabella "Note per cartella" (colonne Cartella | Contenuto | Hub | Totale): self
1/1/2, areas 6/1/7, projects 1/1/2, concepts 3/1/4, docs 1/1/2 (KA-140). I tre script
(`gate_qualita.py`, `genera_llms.py`, `genera_showcase.py`) condividono lo stesso scope e lo stesso
parsing di frontmatter, quindi i loro numeri sono sempre coerenti fra loro — RnoC5IlOUhs#103:48
(KA-141).

## La memoria viva

Limite dichiarato dall'autore prima di costruire la soluzione: le note statiche (clienti, KPI,
progetti) non bastano — *"non abbiamo ancora un modo di dire [all'AI] 'Ehi, ascolta, ma a marzo
avevamo parlato di questo argomento? Ti ricordi cos'era? Cosa avevamo deciso?'"* — serve memoria
**episodica**, non solo memoria statica — RnoC5IlOUhs#130:00-130:42 (KA-196). Prompt di costruzione
della skill, testo digitato per intero: *"Costruiamo una skill per il cervello di Aurora che gestisca
il journal: inizio sessione, fine sessione, fine giornata. CONTESTO — memoria viva. Il cervello ha
due strati di memoria: Memoria STATICA [...] Memoria DINAMICA: il diario di lavoro. Ogni sessione e
ogni giornata lasciano una nota che si AGGANCIA sempre alle entità statiche coi [[wikilink]]. Mai una
nota di diario sciolta nel vuoto."* — RnoC5IlOUhs#134:06 (KA-197).

Risultato: **una skill sola (`journal`) con tre comandi a frase libera** (o forzabili con
`/journal`) — RnoC5IlOUhs#136:12 (KA-198):

- **"buongiorno"** → briefing di inizio sessione in 5 righe (dove eravamo rimasti, cosa era aperto,
  priorità di oggi), senza scrivere niente.
- **"chiudi sessione"** → prima 3 righe di riassunto, all'ok dell'utente scrive
  `sessione-<data>.md` in `workspace/journal/sessions/`.
- **"fine giornata"** → legge tutte le sessioni del giorno, 3 righe di riassunto, all'ok scrive il
  daily in `workspace/journal/daily/`.

File generati dalla skill: `.claude/skills/SKILL.md` (l'orchestratore), i due template
`workspace/journal/_templates/_template-sessione.md` e `_template-daily.md`, le cartelle
`workspace/journal/sessions/` e `workspace/journal/daily/` (KA-199). Regole imposte dentro la skill:
date sempre `YYYY-MM-DD`, frontmatter conforme al `_template-nota.md` del vault, ogni nota di diario
con almeno un `[[wikilink]]` a un'entità reale — se manca, la skill lo chiede, nessuna entità
inventata (KA-199). Test end-to-end verificato: il primo "buongiorno" produce un briefing di 5 righe
sull'indice `llms.txt` (diario ancora vuoto) — RnoC5IlOUhs#136:12 (KA-200); la prima "chiudi
sessione" salva `sessione-2026-06-10.md` con struttura in tre sezioni Fatto/Deciso/Aperto, agganciata
via wikilink a `[[progetto-arr-5m-2026]]` — RnoC5IlOUhs#137:12 (KA-201); la prima "fine giornata"
fonde l'unica sessione del giorno in un daily con la stessa struttura — RnoC5IlOUhs#137:36-138:00
(KA-202, KA-204). Questo comando realizza in pratica lo stesso schema già anticipato dal Prompt 13
("Apri la sessione — il briefing") del canovaccio: *"Leggi l'indice llms.txt e l'ultima nota dentro
workspace/journal/sessions/ (il diario dell'ultima volta) [...] Non scrivere ancora niente nel
cervello. Solo il briefing."* — RnoC5IlOUhs#112:48 (KA-162).

Anche fuori dalla demo Aurora, l'autore mostra la sua company brain reale: la cartella `workspace`
contiene un journal con **due tipi di nota** — `sessions` (una per conversazione chiusa) e `daily`
(un file per giornata che aggrega e riassume le sessioni chiuse quel giorno, in linguaggio
narrativo) — *"perché dobbiamo averne due, perché il daily è un suo [riassunto]"* — RnoC5IlOUhs#57:24
(KA-075, KA-077).

## Il layer visivo

Introdotto a voce come scelta fra due opzioni: *"Possiamo fare o cruscotti locali, quindi con un HTML
locale [...] oppure possiamo utilizzare Notion."* — RnoC5IlOUhs#126:06 (KA-182).

**Cruscotto HTML locale** — Prompt 12, testo integrale: *"Genera un cruscotto HTML statico dai dati
del canon: gli indicatori dell'ultimo mese, i grafici di andamento (fatturato, organico, edifici), la
classifica clienti e l'organico per reparto. Tutto in un solo file .html che apre con un doppio
click, offline e senza account."* — RnoC5IlOUhs#112:54, eseguito parola per parola a #126:06
(KA-161, KA-184). Risultato aperto in locale (`outputs/cruscotto-aurora.html`): header con titolo
azienda, sottotitolo "Cruscotto direzionale", dichiarazione "Dati riconciliati · nessun dato
inventato"; 6 card KPI (ARR totale, clienti attivi, edifici gestiti, NRR, churn logo, churn
fatturato); due grafici di andamento (fatturato ARR con proiezione tratteggiata all'obiettivo Board,
clienti attivi 2019-2025); classifica clienti per fatturato con barra multicolore per moduli attivi;
grafico a ciambella dell'organico per reparto — RnoC5IlOUhs#127:12-127:48 (KA-185, KA-186, KA-187,
KA-188).

**Notion via MCP** — comando reale, letto dalla documentazione ufficiale Notion a schermo
(`developers.notion.com/guides/mcp/get-started-with-mcp`):

```
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

seguito da `/mcp` in Claude Code per l'autenticazione OAuth — RnoC5IlOUhs#127:48 (KA-189). Sequenza
osservata in terminale: `/fast` (attiva "Fast mode", modello Opus 4.6), `/clear` per ripartire con
contesto vuoto, poi il comando MCP sopra e la verifica "sei connesso con Notion?" —
RnoC5IlOUhs#127:54-129:18 (KA-190). Risultato: Claude crea in Notion una pagina "Cervello Pino" con
KPI, tabella revenue a ponte, key account e obiettivo 2026 — RnoC5IlOUhs#129:18-129:36 (KA-191,
KA-192, KA-193). **Principio anti-invenzione applicato in pratica**: quando l'ARR per cliente non è
certo nel vault, Claude dichiara il buco o usa un placeholder esplicito invece di inventare un
numero — *"il vault cita 9 clienti attivi ma ne nomina solo 8: ho messo un placeholder 'Cliente
settore PA' [...] invece di inventare un nome"* — RnoC5IlOUhs#129:54 (KA-195, confidenza:
osservato).

## I prompt del canovaccio

Documento Notion companion "Company Brain — Tutti i prompt del tutorial", indice integrale
(RnoC5IlOUhs#3:12, #30:48, KA-010):

1. **Passo 1 — Obsidian a mano, nessun prompt**: installare Obsidian, creare il vault vuoto, prima
   nota, wikilink di ritorno, backlink, vista grafo, frontmatter — l'unico passo senza AI.
2. **Prompt 2 — Estrai il canon**: prima un piano, poi l'ok dell'utente.
3. **Prompt 3 — Trasforma il canon in note atomiche** (prima gli hub).
4. **Prompt 4 — Completa il cervello** (fino a circa 28 note).
5. **Prompt 5 — Il gate di qualità** (solo referto, contro le 6 regole).
6. **Prompt 6 — Correggi e ripeti** finché esce "0 errori".
7. **Prompt 7 — Genera l'indice per la AI** (`llms.txt`).
8. **Prompt 8 — Lo showcase** (la fotografia per la demo).
9. **Prompt 9 — Metti il vault sotto git** (versione con contraddizione osservata: prima "senza
   push", poi con "commit e push" nella stessa pagina riletta due volte — vedi Nota di trasparenza).
10. **Prompt 10 — Interroga il cervello** (a ~28 note, senza RAG, regola d'oro: cita sempre il file,
    "Non presente nel cervello" se assente).
11. **Prompt 11 — La domanda di incrocio** (dove le cartelle si arrendono: due fatti in due note
    diverse, la risposta si costruisce camminando sui collegamenti).
12. **Prompt 12 — Il cruscotto HTML locale**.
13. **Prompt 13 — Apri la sessione** (il briefing, dal diario dell'ultima volta).
14. **Prompt 14 — Chiudi la sessione** (il diario, agganciato alle entità vere toccate).

Nota di rilievo osservata direttamente nel canovaccio: leggendo lo stesso riquadro "Prompt 9" due
volte in momenti diversi del video, il contenuto **non coincide** — a 100:30 dice esplicitamente
*"NON fare push da nessuna parte"*, a 103:42 lo stesso riquadro dice *"fai commit e push"* — non un
errore di lettura ma un contenuto realmente diverso, probabilmente riscritto con l'AI fra una ripresa
e l'altra. Lezione operativa dichiarata nella fonte: *"un'espansione di prompt via AI può capovolgere
in silenzio un vincolo di sicurezza scritto a mano — da controllare sempre dopo un 'espandi questo
prompt'"* — RnoC5IlOUhs#100:30, #103:42 (KA-145, KA-146, KA-147).
