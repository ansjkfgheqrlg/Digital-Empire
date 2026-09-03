# Enrichment Report — sno_IcNbYFM

**Video:** "Ho creato un CFO AI che controlla l'azienda H24 con Claude" — Giovanni Beggiato, 34m52s
**Run:** `max17-v15`, batch max17 v15
**Stage 1-9 eseguiti:** tutti in questa sessione, 2026-09-03 — ripresa dopo che la sentinella
`sentinella-cfo-ai` era morta per limite di sessione **prima ancora di scrivere un solo file**
("formati letti, niente scritto", `company/Memory/riprese/EMP-QQ2R.md` sezione 4). Il run
conteneva solo materiale grezzo (`frames/`, `video.mp4`, `transcript_clean.txt`,
`sno_IcNbYFM.info.json`, `.it.vtt`, nessuno `scenes.json`) — tutto il lavoro (visione, atomi,
coverage, deliverable dedicato, wiki, memory close) è stato fatto da zero in questa sessione.
**Atoms disponibili:** 40 KA · coverage frame **82/226 scene uniche (36,3%), 82/523 frame
totali (15,7%)** — NO-FINTO: PASS con copertura parziale dichiarata (dettaglio in
`runs/max17-v15/coverage.md`); tutti i 6 prompt del video letti per intero.

---

## Correzione preliminare — un bug nel tooling, non nel contenuto

Prima di guardare un solo frame, lanciato `scripts/scene_detector.py --run max17-v15` per
ridurre i 523 frame densi a un elenco di scene uniche (come già fatto nei run gemelli v01 e
v07). Il primo lancio, coi valori di default, ha prodotto `scenes.md` con timestamp **dimezzati
e sbagliati**: lo script assumeva un intervallo di estrazione di 2.0s, mentre questo run usa
4.0s (confermato in `frames/manifest.json`). Verificato confrontando `frame-523` (ultimo
frame): il manifest lo colloca a 34:48, coerente con la durata dichiarata (2092s); `scenes.md`
lo collocava invece a 17:24. Rilanciato con `--interval 4`: stessa selezione di 226 frame
unici, timestamp ora corretti e coerenti con i capitoli di `ingest.json`.

Non è un errore di contenuto (nessun frame è stato descritto in base al timestamp sbagliato,
perché la correzione è avvenuta prima di iniziare la visione), ma un difetto di processo degno
di nota: lo script non legge l'intervallo reale dal manifest del run, si affida a un default
che può non corrispondere.

---

## Stage D — Relevance / Gap / Scout

### La tesi trasferibile del video

Non è "un altro modo di collegare QuickBooks a un LLM". È che un sistema che produce numeri
per una decisione aziendale ha bisogno di **tre cancelli separati e non negoziabili**: un
confine netto fra estrazione e calcolo (per non far allucinare il modello sui dati grezzi), un
motore di calcolo verificabile per riproducibilità (test di determinismo che ha trovato bug
veri), e un controllo automatico separato sull'output interpretato dall'AI (perché è proprio
lì, nell'interpretazione, che un errore si infila senza che nessuno se ne accorga). Questa
architettura è generica, non specifica di QuickBooks o di caroselli finanziari — si applica a
qualunque agente Digital Empire che produce un report o una risposta numerica per una
decisione.

### Perché il perimetro di questa sessione era il deliverable dedicato, non le patch

Il checkpoint `EMP-QQ2R` (sezione 4) elenca tre sentinelle morte in parallelo sullo stesso
lancio (`studia-rizzo`, `studia-roberts`, `sentinella-cfo-ai`) e il compito esplicito di questa
ripresa era: chiudere il video end-to-end **con un confronto dedicato contro la Tesoreria**
(`confronto-tesoreria.md`), non patchare skill/agenti condivisi mentre altre due sentinelle
lavoravano sullo stesso repo. Nessuna modifica è stata fatta a `scripts/tesoreria.py` o agli
agenti `.claude/agents/tesoreria-*.md`: i cinque consigli concreti restano proposte scritte per
intero, non applicate.

### Skill/agenti candidati e verdetto

| Target | Verdetto | Motivo |
|---|---|---|
| `scripts/tesoreria.py` | **Gap confermato, 5 proposte non applicate** | Nessuna soglia di allerta in codice, nessun campo data-scadenza, nessun test di determinismo/regressione — dettaglio completo in `confronto-tesoreria.md`, sezione 3. |
| `.claude/agents/tesoreria-conductor.md` (Legge 2, "un numero che non esiste si dichiara") | Principio già identico al video, nessuna patch | La disciplina è già scritta come legge; il gap è solo l'assenza di un controllo automatico equivalente a `verifica_dashboard.py` — proposta 3 in `confronto-tesoreria.md`, non applicata perché tocca un sistema condiviso in costruzione parallela. |
| `.claude/agents/tesoreria-entrate.md` (regole "fatture ferme >30gg", "previsti fermi >60gg") | Gap confermato: regole scritte in prosa, non in codice | Proposta 1 in `confronto-tesoreria.md` (dizionario di soglie in `tesoreria.py`) le porterebbe in codice — non applicata in questa sessione. |

---

## Stage E — Gate

Nessuna patch applicata in questa sessione = nessun diff da validare su file condivisi. Le
uniche scritture sono: i tre file di questo `knowledge/sno_IcNbYFM/`, i deliverable in
`runs/max17-v15/`, la pagina wiki nuova, l'indice/log della wiki, il checkpoint di chiusura.

---

## Stage H — Cosa ha trovato Memory Empire

**Arricchite:** nessuna skill/agente esistente in questa sessione (nessuna patch a
`scripts/tesoreria.py` o agli agenti Tesoreria — solo proposte, coerenti col perimetro
dichiarato).

**Create:**
- `second-brain-vault/wiki/sources/Source_Giovanni_Beggiato_CFO_AI_Claude.md` — pagina wiki
  del video, con sezione "Confronto con Digital Empire" che riassume i 5 consigli.
- `second-brain-vault/wiki/tools/Tool_Tesoreria_Digital_Empire.md` — **prima pagina wiki mai
  scritta per la Tesoreria** (ADR-020 esisteva solo in `company/Memory/decisions/`, mai
  ancora sincronizzato nella wiki pubblica). Necessaria per non lasciare un link a vuoto nel
  confronto e per rendere la Tesoreria trovabile dalla wiki come ogni altro ecosistema DE.

**Esplicitamente NON arricchite, e perché:** `scripts/tesoreria.py` e i cinque agenti
`tesoreria-*` — i 5 consigli concreti restano proposte scritte per intero in
`confronto-tesoreria.md`, non applicate, perché toccare un sistema nato lo stesso giorno
(ADR-020) e potenzialmente in uso da altri lavori in corso non rientrava nel perimetro
dichiarato di questa ripresa (chiudere il video + il confronto, non patchare la Tesoreria).

**Tensioni aperte da questo video:** nessuna tensione di contenuto interna al video stesso (il
sistema mostrato è internamente coerente, con le proprie discrepanze dichiarate a schermo dal
Claude del video, es. i percorsi delle skill scaricate che non combaciavano col progetto
reale). La tensione reale è esterna: la Tesoreria di DE, nata lo stesso giorno di questo video,
non ha ancora nessuno dei tre cancelli che il video dimostra essere concretamente costruibili
con poco codice (soglie, scadenzario, anti-invenzione) — non risolvibile da questa sessione in
generale, richiede lavoro dedicato sul reparto Tesoreria.

---

## Tracciabilità

- Contenuto integrale: `knowledge/sno_IcNbYFM/contenuto-integrale.md` (per categoria, non riassunto)
- Atoms: `knowledge/sno_IcNbYFM/atoms.json` (40 KA)
- Manifest: `knowledge/sno_IcNbYFM/ingest-manifest.json`
- Analisi visiva: `runs/max17-v15/video-analysis.md` (walkthrough cronologico completo)
- Coverage: `runs/max17-v15/coverage.md` (copertura dichiarata capitolo per capitolo)
- Deliverable speciale: `runs/max17-v15/confronto-tesoreria.md`
- Pagina wiki: `second-brain-vault/wiki/sources/Source_Giovanni_Beggiato_CFO_AI_Claude.md`
- Pagina wiki Tesoreria (creata in questa sessione): `second-brain-vault/wiki/tools/Tool_Tesoreria_Digital_Empire.md`
- Checkpoint di chiusura: `company/Memory/checkpoints/` (vedi ultimo CP-20260903-*)
