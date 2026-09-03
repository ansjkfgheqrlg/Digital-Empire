# Enrichment Report — P-BQ-AGS0ck

**Video:** "Become a Master Storyteller (The Dopamine Trick Elite Speakers Use)" — Vishen, 25m55s
**Run:** `max17-v14`
**Stage 1-9 eseguiti:** tutti in questa sessione, 2026-09-03. Il run conteneva **solo materiale
grezzo** su disco (`frames/` con 390 immagini, `video.mp4`, `P-BQ-AGS0ck.info.json`, `.en.vtt`,
nessuno `scenes.json`/`scenes.md`, nessun `transcript_clean.txt`) — nessun lavoro precedente
esisteva per questo video, coerente con quanto dichiarato in `EMP-QQ2R.md` ("genuinamente
nuovo, 390 frame — DA FARE").
**Atoms disponibili:** 35 KA (tutti `osservato`) · coverage frame **83/338 scene uniche
(24,6%), 83/389 frame totali (21,3%)** — NO-FINTO: PASS con campionamento sistematico dichiarato
(dettaglio in `runs/max17-v14/coverage.md`); trascrizione letta al 100% (674/674 righe pulite).

---

## Correzione preliminare — un errore di stato nel checkpoint, non nel contenuto

Prima di guardare un solo frame, letto `company/Memory/riprese/EMP-QQ2R.md` come richiesto dalla
Regola Zero. Il checkpoint (versione precedente a questa sessione) dichiarava che "il video vero
di Vishen (Mindvalley) non risulta scaricato da nessuna parte" e andava "recuperato con un task
di ricerca a parte" — mentre la stessa sezione del checkpoint elencava `max17-v14` come
"genuinamente nuovo... DA FARE", senza collegare i due fatti.

**Verificato con prove concrete durante la visione**: la trascrizione (00:01:24) dice
esplicitamente *"my name is Vish[en] Lak[h]ani. I'm the founder of Mind Valley"*, e
`P-BQ-AGS0ck.info.json` conferma `uploader`/`channel`: "Vishen", `uploader_id`: "@vishen". **Il
video di Vishen non era mai stato "perso"**: era proprio questo run, mai ancora elaborato.
Correzione dichiarata in testa a `video-analysis.md`, in questo enrichment report, nel checkpoint
di chiusura e nell'entry di `wiki/log.md` — non corretta silenziosamente nel vecchio checkpoint
(che resta un documento storico di quella sessione), ma segnalata per chi lo rilegge.

---

## Stage D — Relevance / Gap / Scout

### La tesi trasferibile del video

Non è "un altro video motivazionale sullo storytelling". È un framework a 5 passi con nomi
memorabili (HSTSS) applicato in modo dimostrativo alla stessa storia reale per tutto il video —
una scelta didattica precisa: invece di 5 esempi diversi (uno per passo), Vishen usa **una sola
storia** e mostra come ogni passo la arricchisce, rendendo il framework più facile da
interiorizzare che da spiegare in astratto. Il pezzo più riusabile per Digital Empire non è la
storia in sé (personale, non trasferibile) ma due pattern tecnici: la costruzione dell'hook
tramite **"idea collision"**, e il device di montaggio **reveal progressivo** legato ai
capitoli.

### Perché il perimetro di questa sessione era chiudere il video, non patchare skill condivise

Il checkpoint `EMP-QQ2R` (sezione 4) indicava come prossimo passo esplicito "i quattro con i
fotogrammi pronti (v12, v13, v14, v16)", con la regola "massimo 2-3 sentinelle in parallelo
quando leggono immagini" (la sessione era saltata due volte per eccesso di parallelismo). Questa
sessione ha chiuso `v14` end-to-end (visione, atomi, coverage, wiki, memory close) senza toccare
skill o agenti condivisi, per non collidere con altre sentinelle attive in parallelo sullo stesso
lotto (es. `v16`).

### Skill/agenti candidati e verdetto

| Target | Verdetto | Motivo |
|---|---|---|
| `.claude/skills/cro-copy-architect/SKILL.md` | **Gap confermato, proposta non applicata** | La sezione "Attenzione" del framework APSOC non nomina esplicitamente la tecnica "idea collision" come pattern di hook, pur avendo altre tecniche documentate. |
| `.claude/skills/script-video-lancio-ccm/SKILL.md` | **Gap confermato, proposta non applicata** | Nessuna sezione esplicita "framework di storytelling a passi nominati" per script di lancio con storia personale/fondativa. |
| `.claude/skills/case-study-forge/SKILL.md` | **Gap confermato, proposta non applicata** | Nessun agente/step dedicato a estrarre stakes reali e un turn verificabile dalla storia di un founder/cliente DE — verificato con `ls` prima di proporre. |
| Nuova skill `mnemonic-forge` | **Proposta, non costruita** | Non esiste oggi in `.claude/skills/` (verificato) una skill che genera mnemoniche/acronimi memorabili per framework interni DE, sul modello "HSTSS → Holy Sh*t That's So Smart". |

---

## Stage E — Gate

Nessuna patch applicata in questa sessione = nessun diff da validare su file condivisi. Le
uniche scritture sono: i tre file di questo `knowledge/P-BQ-AGS0ck/`, i deliverable in
`runs/max17-v14/`, la pagina wiki nuova, l'indice/log della wiki, il checkpoint di chiusura.

---

## Stage H — Cosa ha trovato Memory Empire

**Arricchite:** nessuna skill/agente esistente in questa sessione (nessuna patch — solo 4
proposte scritte per intero in `video-analysis.md` §CONSIGLI e nella pagina wiki, verificate con
`ls`/grep prima di essere scritte).

**Create:**
- `second-brain-vault/wiki/sources/Source_Vishen_Lakhiani_Master_Storyteller_HSTSS.md` — pagina
  wiki del video, cross-linkata a 3 pagine esistenti (`Concept_Hook_Anti_Cliche_Checklist`,
  `Framework_Barnum_Rainbow_5Pilastri`, `Source_Artem_Novitckii_Caroselli_ChatGPT`).
- `empire-studio/runs/max17-v14/transcript_clean.txt` — non esisteva su disco, scritto da zero
  con uno script Python di dedup del `.vtt` (674 righe pulite).
- `empire-studio/runs/max17-v14/scenes.json` / `scenes.md` — generati con
  `scripts/scene_detector.py --interval 4.0` (non esistevano su disco).

**Esplicitamente NON arricchite, e perché:** `cro-copy-architect`, `script-video-lancio-ccm`,
`case-study-forge` — i 4 consigli concreti restano proposte scritte per intero, non applicate,
per rispettare il perimetro di questa ripresa (chiudere il video, non patchare skill condivise
mentre altre sentinelle lavorano in parallelo sul lotto max17).

**Tensioni aperte da questo video:** nessuna tensione di contenuto interna (il video è
internamente coerente, con le proprie omissioni dichiarate — es. il secondo video promesso "going
deeper" non è disponibile in questo download). La tensione reale è lo **stato del checkpoint
`EMP-QQ2R.md`**, che conteneva un'affermazione fattualmente sbagliata sulla disponibilità di
questo video — corretta in questa sessione ma non riscritta retroattivamente nel checkpoint
storico (compito lasciato al prossimo checkpoint di chiusura, coerente con la pratica del lotto).

---

## Tracciabilità

- Contenuto integrale: `knowledge/P-BQ-AGS0ck/contenuto-integrale.md` (per categoria, non riassunto)
- Atoms: `knowledge/P-BQ-AGS0ck/atoms.json` (35 KA)
- Manifest: `knowledge/P-BQ-AGS0ck/ingest-manifest.json`
- Analisi visiva: `runs/max17-v14/video-analysis.md` (walkthrough cronologico completo)
- Coverage: `runs/max17-v14/coverage.md` (copertura dichiarata capitolo per capitolo)
- Pagina wiki: `second-brain-vault/wiki/sources/Source_Vishen_Lakhiani_Master_Storyteller_HSTSS.md`
- Checkpoint di chiusura: `company/Memory/checkpoints/` (vedi ultimo CP-20260903-*)
