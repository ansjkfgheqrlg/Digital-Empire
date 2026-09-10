# Report — A6/L02 «Creiamo la copertina (metodi + A.I)» (24:54)

- **Durata:** 24:54 · parlato integrale · **profondità ORO**
- **Letta:** parlato integrale (767 righe) + 19/172 frame unici (campione motivato,
  vedi `frame-scelti.md`) — la lezione più grande della categoria A6
- **Rapporto grezzo:** [`appunti.md`](appunti.md) · frame: [`frame-scelti.md`](frame-scelti.md)
- **Mandato:** cambiato il 2026-09-10 — non si depositano solo regole, si pongono **sei
  domande** a ogni cosa vista. Le pongo qui esplicitamente.

---

## 1. Cosa insegna

Metodo end-to-end per creare una copertina YouTube senza saper disegnare: (1) guardare cosa
funziona già nella propria nicchia con YouTube + vidIQ (filtrato per anno/visualizzazioni), non a
sensazione; (2) scaricare la copertina originale del video-modello con un tool gratuito (URL →
immagine); (3) ricostruirla in Canva — coprire il testo, riscriverlo, ricolorare, aggiungere
elementi — abbastanza diversa da non essere una copia 1:1; (4) **in alternativa più veloce**,
partire da un template pronto della galleria "Miniatura YouTube" di Canva (ce ne sono per ogni
genere, "breaking news" incluso) e cambiare solo sfondo/testo; (5) **la leva di velocità più
forte**: creare UN template-base personale e duplicarne la pagina per ogni video futuro, invece
di ricreare da zero ogni volta; (6) regole di leggibilità fisse: font unico per canale, testo
grande (pensato per smartphone), contorno nero per garantire leggibilità su qualsiasi sfondo;
(7) rimozione sfondo IA di Canva (3 secondi) per ritagliare un soggetto da una foto; (8) in
alternativa generativa, thumbnail.ai (gratuito all'ingresso, login per personalizzare); (9) un
terzo tool a pagamento citato ma mai usato (Thumbnail Blaster, 36$) — **raccomandazione finale
esplicita del docente: Canva resta lo strumento migliore.**

## 2. Cosa facciamo oggi

Verificato leggendo il codice, non assunto dai nomi dei file — e la scoperta più importante di
questo giro di studio è qui, non nel corso:

**Abbiamo già costruito la metà tecnica del metodo del corso, e non arriva mai a Max.**

- `apex7_orchestrator.py:1364` — `_ensure_source_thumbnail(video_id)` scarica **davvero** la
  copertina originale del video sorgente, via `https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg`
  — esattamente il trucco del corso ("thumbnail YouTube Download", appunti @ 02:45-03:18), ma
  **nativo, senza sito di terze parti**, salvato in `05-TEMPLATES-E-KIT/source-thumbnail/`.
  Verificato su disco: 9 immagini reali già scaricate così (`dosementale-eax7OPi1q0M-maxres.jpg`
  e altre).
- `apex7_orchestrator.py:1443-1460` — `run_phase_5()` scrive `brief-miniatura.json` con
  `source_thumbnail` (il file scaricato sopra), `source_style` ("Copertina reale del video
  sorgente, da adattare mantenendone il linguaggio visivo") e `text_overlay_lines` (titolo
  spezzato in righe corte leggibili) — **la stessa identica idea** della sequenza Canva del
  corso (@ 07:02-09:56: copri il testo originale, riscrivilo, mantieni la struttura).
  Commento in codice, riga 1443: *"regola di Gael, 2026-07-31"* — **decisione presa in casa
  PRIMA di questo studio, indipendentemente**, e coerente col corso.
- `thumbnail-designer.md` (`03-AGENTI-E-RUOLI/operatori/`) descrive lo stesso playbook a parole:
  "studia la miniatura del competitor, identifica cosa funziona e cosa è debole" — un agente
  L2 già specificato per questo lavoro.
- **Ma questo intero brief non arriva mai a Max.** `brief-miniatura.json` viene prodotto solo per
  alimentare `arena_thumbnail.py`, il generatore automatico via Arena — **fallito tre volte**
  (da qui la regola "la copertina la fa Max"). Con `--con-copertina` non passato (il default da
  fine agosto), il ramo che produce e legge `brief-miniatura.json` **non viene nemmeno eseguito**
  nella run che consegna a Max (`produci_video_completo.py:395-396` forza `salta_copertina=True`
  di default — ma la Fase 5 dell'orchestratore che scrive il brief gira comunque prima, agli step
  1-427, e il file resta scritto su disco, semplicemente ignorato dal passo 2).
  `consegna_a_max()` (riga 293) scrive `copy.md` con un brief **hard-coded e generico** — righe
  335-339: *"Formato: 16:9, stampo Legami d'Amore, testo oro/ambra. Leggibilità: il titolo deve
  leggersi anche in miniatura piccola."* — **senza mai leggere `brief-miniatura.json`**, quindi
  senza mai mostrare a Max né l'immagine di riferimento scaricata né le righe di testo già
  spezzate correttamente.
- `thumbnail_analyzer.py` (92 righe, luminosità/contrasto/leggibilità via PIL) esiste, è citato
  nel playbook di `thumbnail-designer.md` (§4, §Playbook punto 7: *"Esegui thumbnail_analyzer.py
  ... prima di inviarlo al metadata-optimizer"*) — **ma zero file `.py` della fabbrica lo
  chiamano davvero** (verificato con grep su tutta `02-AUTOMAZIONI-E-SCRIPTS/`). È un
  criterio di scelta automatico, già scritto, mai collegato a niente: nemmeno alla consegna a
  Max.
- `youtube_uploader_playwright.py` accetta già `--thumbnail <path>` per l'upload — il punto
  finale della catena regge, è il punto di partenza (il riferimento visivo a Max) che manca.

## 3. Delta

**Non è un problema di sapere: è un problema di collegamento.** Il corso non ci insegna niente
che non avessimo già capito da soli — la Fase 5 dell'orchestratore fa la stessa cosa del corso,
decisa indipendentemente il 2026-07-31. Il delta reale è che **il pezzo buono del lavoro già
fatto (scaricare il riferimento reale + preparare il testo) è rimasto agganciato al pezzo che ha
fallito (generarla in automatico con Arena)**, e quando quest'ultimo è stato disattivato per
decisione di Max, si è portato dietro anche il primo — che invece non c'entra nulla col perché
Arena ha fallito, e serve oggi esattamente com'era.

Oggi Max apre una cartella con un file `copy.md` che gli dice "16:9, testo oro/ambra" e basta:
deve rifare da zero, a mano, la parte 1-2-3 del metodo del corso (cercare la nicchia, trovare un
modello, scaricarne la copertina) che la macchina aveva **già fatto e salvato su disco** un
minuto prima, nella stessa run.

Un secondo delta, minore ma concreto: `thumbnail_analyzer.py` è un "criterio di scelta"
automatico e oggettivo (luminosità 40-220, contrasto ≥30) che oggi non giudica **nessuna**
copertina reale — né quelle di Arena (quando girava) né, soprattutto, quelle che Max fa a mano
adesso. Verificare "la mia copertina è abbastanza leggibile" oggi è un giudizio a occhio di Max,
quando potrebbe essere un numero.

## 4. Conflitti

**Nessuno.** Il metodo del corso (studiare i competitor, scaricare un riferimento, non
automatizzare la resa finale) è pienamente compatibile con la regola di casa "la copertina la fa
Max a mano" — anzi la rinforza: il corso stesso raccomanda Canva (uno strumento manuale/assistito)
sopra i generatori 100% automatici, e il docente conclude esplicitamente scegliendo lo strumento
dove l'umano rifinisce, non quello che sforna da solo. Le regole proposte in questo report
**preparano il materiale per Max**, non generano la copertina finale: nessuna tocca il divieto
di automazione della resa (ADR/regola di Max, 2026-08-29/09-04). Va scritto in CONFLITTI.md?
No — non c'è arbitrato da fare, corso e casa dicono la stessa cosa.

## 5. Le sei domande, poste esplicitamente

**5.1 — Cambia un parametro o una procedura?**
Sì, due:
- **A6-L02-01** (procedura): il font va fissato UNO per canale, non lasciato alla scelta libera
  di ogni copertina — dichiarato esplicitamente dal corso (@ 09:58-10:20) e già implicito nella
  logica di `_overlay_lines_from_title` (righe corte, uniformi), ma non scritto in nessuna
  reference.
- **A6-L02-02** (parametro): la soglia di leggibilità di `thumbnail_analyzer.py`
  (luminosità 40-220, contrasto ≥30) è la stessa euristica del "contorno nero" del corso
  (@ 10:58-11:27) — va documentata come lo standard atteso, non lasciata solo nel codice.

**5.2 — Ci manca un AGENTE?**
No, non manca: **esiste già** (`thumbnail-designer.md`), ed è specificato quasi esattamente come
serve. Il problema non è l'assenza dell'agente, è che il suo output (`brief-miniatura.json`) non
viene consegnato al destinatario reale (Max) quando l'automazione della resa è disattivata.
Nessuna regola "costruisci agente" qui: sarebbe reinventare cosa già c'è.

**5.3 — Ci manca una SKILL o un comando?**
Sì, indirettamente: manca l'**ultimo miglio** — nessun comando oggi prende
`brief-miniatura.json` (già scritto) e lo traduce in un brief leggibile da Max dentro `copy.md`,
con l'immagine di riferimento reale aperta accanto. Non serve una skill nuova nel senso di
conoscenza: serve la funzione che manca (vedi 5.5).

**5.4 — Un FLUSSO va ridisegnato?**
Sì — **A6-L02-03**. Il flusso di consegna (`consegna_a_max()` dentro
`produci_video_completo.py`) va ridisegnato per leggere `brief-miniatura.json` quando esiste (lo
scrive comunque la Fase 5, a prescindere da `--con-copertina`) e includere nel brief a Max:
il percorso dell'immagine di riferimento reale scaricata (`source_thumbnail`), le righe di testo
già spezzate (`text_overlay_lines`), e la fonte (`source_style`) — aprendo quell'immagine insieme
alla cartella (stesso pattern già usato con `subprocess.Popen(["explorer", dest])`, riga 363).
Questo non automatizza la copertina: la fa comunque Max, ma parte da un riferimento vero invece
che da un canvas bianco — è esattamente il salto che il corso descrive tra "creare dal nulla" e
"copiare un modello che già funziona" (@ 03:18-03:31: *"con due clic ho la copertina"*).

**5.5 — Serve CODICE — script nuovo, funzione nuova, funzione da rifare?**
Sì, due:
- **A6-L02-04** (funzione, ridisegna): `consegna_a_max()` deve leggere
  `05-TEMPLATES-E-KIT/brief-miniatura.json` (se presente) e aggiungere al blocco "Copertina" di
  `copy.md` il riferimento reale — non sostituendo il brief attuale, arricchendolo.
- **A6-L02-05** (funzione, costruisci): `thumbnail_analyzer.py` va richiamato **davvero** in un
  punto della catena — il candidato naturale è dentro `youtube_uploader_playwright.py`, appena
  prima di caricare il file passato a `--thumbnail`: se luminosità/contrasto sono fuori soglia,
  stampa un avviso a Max (non blocca l'upload — Max decide, la macchina misura). Oggi il file
  esiste, il criterio è scritto, e non lo usa nessuno.

**5.6 — Contraddice qualcosa che facciamo?**
No (vedi punto 4). Il gap trovato è interno alla fabbrica (uno spec dice "chiama
`thumbnail_analyzer.py`", il codice reale non lo chiama mai) — non un conflitto corso-vs-noi, va
segnato come promemoria qui e nelle regole, non in `CONFLITTI.md`.

## 6. Regole estratte

Cinque regole, di cui tre costruttive (nuove per il contratto 2026-09-10) e due procedurali/di
parametro. **Nessuna tocca la generazione automatica della copertina** — tutte preparano
materiale per Max, coerenti con la regola permanente.

| id | tipo | regola in una riga | tocca | azione | binario |
|---|---|---|---|---|---|
| `A6-L02-01` | procedura | Font unico per canale, mai scelto ad-hoc per singola copertina | `04-SKILLS-E-REFERENCE/references/scelta-strumenti.md` | nuovo | A |
| `A6-L02-02` | parametro | Soglia di leggibilità (luminosità 40-220, contrasto ≥30) documentata come standard atteso, non solo nel codice | `04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md` | nuovo | A |
| `A6-L02-03` | flusso | `consegna_a_max()` deve leggere `brief-miniatura.json` e mostrare a Max il riferimento reale scaricato, non solo un brief generico | `02-AUTOMAZIONI-E-SCRIPTS/produci_video_completo.py` | ridisegna | B |
| `A6-L02-04` | funzione | `consegna_a_max()` va riscritta per includere `source_thumbnail`/`text_overlay_lines`/`source_style` nel blocco Copertina di `copy.md`, aprendo l'immagine di riferimento insieme alla cartella | `02-AUTOMAZIONI-E-SCRIPTS/produci_video_completo.py` | ridisegna | B |
| `A6-L02-05` | funzione | `thumbnail_analyzer.py` va richiamato davvero (oggi zero chiamate in tutta la fabbrica) prima dell'upload, come avviso non bloccante a Max | `02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py` | costruisci | B |

Dettaglio completo (prova, misura, rischio) in
`company/Memory/studi/aitubepro/regole/A6-viral-mastery/L02_copertina.py`.

## 7. Applicabilità

**Alta su tutto il delta 5.3-5.5**: non è teoria, è un pezzo di codice già scritto e già
funzionante (`_ensure_source_thumbnail`, `brief-miniatura.json`) a cui manca un ultimo
collegamento di 10-15 righe per arrivare a Max. È il tipo di scoperta più economico da applicare
che questo studio abbia fatto finora: zero nuovo strumento da imparare, un ponte da costruire tra
due pezzi che già esistono. **Media** sul metodo di ricerca competitor/vidIQ (§1 punti 1-2):
conferma quello che L01 aveva già mostrato per il SEO, stesso principio applicato alle immagini.
**Bassa** sui tool specifici (Canva, thumbnail.ai, Thumbnail Blaster): sono strumenti che Max usa
già di sua scelta manuale, il corso non aggiunge un tool nuovo da adottare — al più conferma che
Canva resta la scelta giusta (raccomandazione esplicita e finale del docente stesso).
