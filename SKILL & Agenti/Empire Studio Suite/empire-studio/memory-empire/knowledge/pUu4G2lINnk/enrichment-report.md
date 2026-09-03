# Enrichment Report — pUu4G2lINnk

**Video:** "Insane Claude Design Skills You Actually Need To Build Beautiful Sites" — Jack Roberts, 22m56
**Run:** `max17-v11-roberts-design`, batch max17 v11
**Stage 1-4 eseguiti:** sessione precedente al 2026-09-03 (ingest, frame, visione, atomi) — interrotti
per limite di sessione prima di Stage 5-9 (ultima parola lasciata: "Ora atoms.json e coverage.md" —
`atoms.json` era in realta' gia' scritto, `coverage.md` no)
**Stage 5-9 eseguiti:** 2026-09-03 (questa sessione — ripresa da `company/Memory/riprese/EMP-QQ2R.md`)
**Atoms disponibili:** 67 KA (66 osservati, 1 inferito) · coverage frame **108/270 scene (40,0%),
108/688 frame totali (15,7%)** — NO-FINTO: PASS con copertura parziale dichiarata **e una
discrepanza di conteggio dichiarata**, dettaglio in `runs/max17-v11-roberts-design/coverage.md`

---

## Stage 5 — la verifica che mancava, e cosa ha trovato

Il buco lasciato dalla sessione morta era `coverage.md`: non esisteva su disco. Prima di scriverlo,
ho verificato — non ricopiato — il numero che l'intestazione di `video-analysis.md` dichiarava
("182/270 frame unici guardati"). Ho estratto con una passata regex ogni citazione esplicita
`frame-NNN.png` nel corpo del testo (inclusi i cluster tipo `frame-373/374.png`), incrociata con
`scenes.json`: il risultato tracciabile e' **108**, non 182.

Non ho corretto il numero originale in silenzio (sarebbe stato disonesto nell'altra direzione:
sostituire un numero non verificato con uno "verificato" senza dirlo) e non ho validato 182 per
fiducia. Ho scritto entrambi in `coverage.md` con una sezione dedicata ("Discrepanza dichiarata —
182 vs 108") che elenca le spiegazioni plausibili (frame confrontati ma non citati singolarmente,
frame di orientamento senza informazione nuova, o un conteggio mai riconciliato prima
dell'interruzione di sessione) senza scegliere quale sia vera, perche' non e' verificabile dagli
artefatti su disco.

Un secondo scostamento minore, piu' piccolo: `atoms.json` (KA-001) cita `frame-001.png`, che non
compare mai come citazione esplicita nel corpo di `video-analysis.md` (l'Intro cita 003/011/016).
Non invalida l'atomo (la trascrizione e' la fonte primaria dichiarata per quel KA), ma e' un'altra
piccola imprecisione di tracciabilita' P12 registrata onestamente in `coverage.md`.

---

## Stage D — Relevance / Gap / Scout

### La tesi trasferibile del video

Non e' "usa questi sette strumenti". E' che bello e vendente sono due assi indipendenti, e che
esistono pattern puntuali e riusabili per il secondo asse (mobile, copy, verifica del lavoro di
design) che un design system da solo non copre. Il pezzo piu' trasferibile in assoluto e'
l'invariante del Design Loop: non e' specifico di Claude Code, si applica a qualunque pipeline
Digital Empire dove lo stesso agente costruisce E giudica il proprio output.

### Skill/agenti candidati e verdetto (verificato con grep prima di proporre)

| Target | Verdetto | Motivo |
|---|---|---|
| `.claude/agents/guild-design.md` (380 righe) | **Gap confermato, proposta non applicata** | Grep mirato su "contesto fresco" / "fresh context" / "shares memory" / "grading its own homework" — zero risultati nel file. Ha due standard A/B con 14 principi non negoziabili sullo STILE, ma nessuna regola sul PROCESSO di giudizio. |
| `.claude/skills/site-design/SKILL.md` (509 righe) | **Gap confermato ma piu' piccolo del dichiarato** | Ha gia' "Mobile-first nei token" (riga 509) — la disciplina mobile-first esiste. Manca solo il numero operativo 390px per l'audit. Grep su "390px" nell'intero `.claude/agents/` e `.claude/skills/site-design/`: zero risultati. |
| `.claude/skills/copy-editing/SKILL.md` (righe 327-334) | **Gap ridimensionato rispetto a quanto l'analisi originale in video-analysis.md dichiarava** | Il file ha GIA' una tabella di sostituzione lessicale che include 3 delle 6 parole bandite dal video (Leverage→Use, Robust→Strong, Seamless→Smooth). Quello che manca non e' la lista di parole ma il LIVELLO: il video lavora a frase intera (esempio completo prima/dopo + regola discorsiva) e include tell strutturali (three-item flourish, empty superlatives, m-dash pileup, numeri inventati) che non sono problemi di vocabolario. |
| `.claude/agents/sentinel-quality.md`, `apex-critic.md` | Nessuna patch, connessione registrata | Entrambi fanno gia' review/gate, ma nessuno dei due formula esplicitamente l'invariante "il critico non deve condividere memoria col costruttore" — stesso grep del punto 1, stesso esito zero. Non proposta patch diretta: sono gate generici multi-dominio, il posto giusto per l'invariante specifico di design resta `guild-design.md`. |

### Perche' nessuna patch e' stata scritta in questa sessione

Il checkpoint `EMP-QQ2R` (sezione 4) elenca tre sentinelle morte in parallelo sullo stesso lancio
(`studia-rizzo`, `studia-roberts`, `sentinella-cfo-ai`) e il ciclo Empire a 9 passi impone
coordinamento prima di un lavoro che tocca skill/agenti condivisi in parallelo con altri. La
sentinella `studia-rizzo` lavorava in parallelo sullo stesso repo mentre questa sessione chiudeva
Roberts. Modificare `guild-design.md`, `site-design/SKILL.md` o `copy-editing/SKILL.md` ora
rischiava una collisione non necessaria: il compito esplicito di questa ripresa era chiudere il
video (coverage + wiki + memory), non patchare skill condivise. Le tre proposte restano scritte
per intero (con posizione esatta: riga/sezione target) nella pagina wiki, pronte per essere
applicate in una sessione dedicata.

---

## Stage E — Gate

Nessuna patch applicata in questa sessione = nessun diff da validare su file condivisi. Le uniche
scritture sono: `coverage.md` (nuovo, dentro il run — non condiviso con altri reparti),
`memory-empire/knowledge/pUu4G2lINnk/` (nuovo, non condiviso), la pagina wiki (nuova), e le due
righe di indice/log della wiki.

---

## Stage H — Cosa ha trovato Memory Empire

**Arricchite:** nessuna skill/agente esistente in questa sessione.

**Creata:** `second-brain-vault/wiki/sources/Source_Jack_Roberts_7_Claude_Design_Skills.md` —
pagina wiki nuova con sezione "Consigli" che porta le tre proposte sopra fino al livello di
dettaglio di una patch pronta da applicare (file, riga/sezione target, testo esatto da aggiungere),
senza applicarle.

**Esplicitamente NON arricchite, e perche':** `sentinel-quality.md` e `apex-critic.md` (fuori
perimetro — sono gate generici, l'invariante specifico di design appartiene a `guild-design.md`);
`nerve-solve` (nessuna connessione diretta trovata in questo video, a differenza del video di
Rizzo dello stesso batch).

**Tensioni aperte da questo video:** la discrepanza 182 vs 108 (vedi Stage 5 sopra) non e' una
tensione di contenuto ma un difetto di processo dello stesso tipo gia' trovato dalla sentinella
`studia-rizzo` sul video gemello (un `ingest-manifest.json`/intestazione che dichiarava un numero
mai riconciliato con un conteggio reale). **Pattern ricorrente su due video dello stesso batch,
in due sessioni diverse**: vale la pena segnalarlo a chi gestisce il ciclo Empire Studio come
possibile difetto sistemico (una sessione che si interrompe per limite lascia numeri di copertura
non verificati in testa ai documenti) piu' che come errore isolato — non risolto qui, solo
osservato e registrato in entrambi i coverage.md.

---

## Tracciabilita'

- Contenuto integrale: `knowledge/pUu4G2lINnk/contenuto-integrale.md` (1199 righe, copia integrale
  di `video-analysis.md`, non riassunto)
- Atoms: `knowledge/pUu4G2lINnk/atoms.json` (67 KA)
- Manifest: `knowledge/pUu4G2lINnk/ingest-manifest.json`
- Analisi visiva: `runs/max17-v11-roberts-design/video-analysis.md` (1199 righe, walkthrough
  cronologico completo, 7 livelli)
- Coverage: `runs/max17-v11-roberts-design/coverage.md` (scritta in questa sessione — verifica
  onesta, non compilazione del numero dichiarato)
- Pagina wiki: `second-brain-vault/wiki/sources/Source_Jack_Roberts_7_Claude_Design_Skills.md`
- Checkpoint di chiusura: `company/Memory/checkpoints/` (vedi ultimo CP-20260903-*)
