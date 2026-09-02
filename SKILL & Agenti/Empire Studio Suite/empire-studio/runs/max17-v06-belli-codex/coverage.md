# Coverage — max17-v06-belli-codex

## Range guardato
- Frame guardati: **197/197 unici** (su 926 frame densi estratti, 1 ogni 2.0s)
- Copertura temporale: intero video, da 0:00 a 30:50 (durata totale 30:52)
- Ordine: sequenziale, dal frame-001 al frame-926, seguendo esattamente l'elenco di `scenes.md`

## Criterio di selezione
- Estrazione densa: 1 frame ogni 2.0s → 926 frame totali
- Deduplicazione per similarità visiva: soglia 3.0 → **197 frame unici** trattenuti, **729 frame duplicati esclusi** (riduzione 78.7%)
- Nessun frame è stato cancellato dal disco: tutti i 926 restano in `frames/`, l'elenco in `scenes.md` indica solo quali 197 mostrano un cambio di schermata reale

## Trascrizione
- Letta integralmente `runs/max-17-2026-09/subs/T7PPX5M6Puo.it-orig.vtt` (6800 righe raw, formato VTT con caption a scorrimento progressivo)
- Deduplicata programmaticamente in `clean_transcript.txt` (850 segmenti puliti, 1 riga per frase incrementale) per renderla leggibile senza il rumore delle caption sovrapposte del formato YouTube auto-generato
- Letta interamente in 4 blocchi sequenziali (righe 1-30, 30-280, 280-549, 549-800, 799-850)

## Frame illeggibili o parzialmente illeggibili
Nessun frame è risultato completamente illeggibile (nessun `[media removed: request limit]` persistente — dove capitato al primo tentativo, il frame è stato riletto con successo). I seguenti frame contenevano testo molto piccolo (screen-recording di terminale/browser compresso) dove alcuni dettagli sono stati trascritti con **confidenza moderata** anziché piena certezza — segnalato esplicitamente nel testo di `video-analysis.md` e in KA-038/KA-061/KA-068 di `atoms.json`:
- **frame-609.png / frame-630.png / frame-346.png** — sintassi esatta di `--model` negli esempi `/codex:rescue` del README (nome modello in font molto piccolo); la stringa `spark → gpt-5.1-codex-spark` è invece leggibile con piena certezza.
- **frame-563.png / frame-570.png** — porzione di un finding di sicurezza su MaReply (leak OAuth/token via endpoint diagnostico) parzialmente illeggibile per compressione JPEG su testo piccolo; il contenuto sostanziale corrisponde comunque a quanto narrato a voce nella stessa finestra temporale (falle alte su autenticazione/token), quindi non è stato incluso come atomo a sé stante per evitare di riportare dettagli non pienamente verificabili.
- **frame-008.png** — testo overlay "GPT-5.6 Sol" / "Fable 5": nomi non ufficiali di modello, marcati `➕ inferito` in quanto nickname personali del presentatore, non terminologia di prodotto verificabile.

## Segmenti puramente promozionali/B-roll (guardati ma non generano atomi tecnici)
Frame 002-038 (intro con overlay animati e B-roll di formazioni aziendali Martes AI), 904-926 (chiusura pitch commerciale + frame neri di fine video) sono stati visionati integralmente ma non contengono contenuto tecnico aggiuntivo rispetto a quanto già riportato nel walkthrough — usati solo per confermare branding, statistiche aziendali (65+ aziende, 75+ soluzioni AI) e la struttura narrativa del video.

## Riepilogo copertura per fasi del video
| Fase | Timestamp | Frame chiave | Stato |
|---|---|---|---|
| Intro + posizionamento Martes AI | 0:00-1:16 | 001-038 | coperto integralmente |
| Lavagna: forze/debolezze | 1:16-3:18 | 039-118 | coperto integralmente |
| Lavagna: 5 comandi | 3:18-4:14 | 118-130 | coperto integralmente |
| Lavagna: 2 pattern d'uso | 6:20-8:25 | 170-222 | coperto integralmente |
| Installazione plugin (VS Code) | 8:25-10:40 | 239-330 | coperto integralmente |
| Caso 1 — audit MaReply | 10:40-19:00 | 333-448 | coperto integralmente |
| Caso 2 — audit form candidature | 19:00-24:00 | 563-690 | coperto integralmente |
| Caso 3 — piano Bitly contestato | 24:00-27:44 | 694-807 | coperto integralmente |
| Comandi extra + transfer | 27:44-28:47 | 833-846 | coperto integralmente |
| Costi e chiusura | 27:44-30:45 | 846-926 | coperto integralmente |

## Output prodotti
- `video-analysis.md` — walkthrough cronologico completo, setup integrale, confronto con Digital Empire, consigli
- `atoms.json` — 70 atomi di conoscenza (target 50-70 rispettato)
- `coverage.md` — questo file
