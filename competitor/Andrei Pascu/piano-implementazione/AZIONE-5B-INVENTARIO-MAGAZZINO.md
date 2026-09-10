# AZIONE 5B — Inventario vero del magazzino ULTIMO METRO

> Misurato il 2026-09-10, da disco, file per file, nessuna stima. Verifica dei 25 pezzi
> dichiarati da ADR-016 (misurati il 2026-09-03) + fotografia dello stato attuale.
> Nessun file spostato, rinominato o cancellato: solo lettura.

---

## 0. La cosa più importante trovata

**Il numero è cambiato.** ADR-016 (03/09) dichiarava 25 pezzi / 2.137 MB. Rieseguendo lo
stesso script (`scripts/ultimo_metro.py`) oggi, senza modificarlo, risultano **31 pezzi /
3.067 MB**: nei 7 giorni fra le due misurazioni il magazzino è cresciuto di 6 pezzi (video-05,
06, 07, 08 + 2 libri nuovi), non diminuito. **Zero pezzi dei 25 originali sono stati segnati
come pubblicati** — non esiste ancora `company/Memory/pubblicati.json` sul disco (il registro
che lo script crea al primo `--segna` non è mai stato creato): nessuno ha mai pubblicato niente
da quando l'Ultimo Metro esiste.

**Seconda cosa importante**: la AZIONE-5 (§5) dichiara "3 video già montati, a tema Claude
Code, pronti" nella cartella `da pubblicare`. Verificato pezzo per pezzo: **solo 1 dei 3 è
davvero dentro quella cartella** (quella sorvegliata dall'Ultimo Metro). Gli altri 2 sono un
livello sopra, in mezzo a decine di altri grezzi non montati — vedi §3.

---

## 1. I 25 pezzi ADR-016 — verifica uno per uno

Tutti e 25 esistono ancora sul disco, nessuno è sparito. Percorso pieno, peso reale, data
dell'ultima modifica (mtime), giorni di fermo da oggi (2026-09-10), tema.

### Deposito A — `Lancio corso skill beast/Page/Leo/da pubblicare/` (16 file, granularità file)

| Nome file | Percorso | Peso | Data (mtime) | Fermo da | Tema |
|---|---|---|---|---|---|
| youtube page claude code.mp4 | `Lancio corso skill beast/Page/Leo/da pubblicare/youtube page claude code.mp4` | 97 MB (101.449.107 B) | 2026-04-23 22:41 | 140 gg | **CLAUDE CODE / DIGITAL EMPIRE** |
| 1776705362_1776703930_fdfffffffddx.mp4 | stessa cartella | 237 MB (248.090.213 B) | 2026-04-20 21:14 | 143 gg | NON CLASSIFICABILE (nome non parlante) |
| youtube page ce.mp4 | stessa cartella | 104 MB (108.712.434 B) | 2026-04-23 22:49 | 140 gg | NON CLASSIFICABILE (variante "ce", non identificata da qui) |
| youtube page mb.mp4 | stessa cartella | 95 MB (99.665.000 B) | 2026-04-23 22:44 | 140 gg | NON CLASSIFICABILE (variante "mb", non identificata da qui) |
| Il nuovissimo pronto per la pubblicazione CE.mp4 | stessa cartella | 98 MB (103.280.154 B) | 2026-04-24 22:53 | 139 gg | NON CLASSIFICABILE |
| Il nuovissimo pronto per la pubblicazione CL.mp4 | stessa cartella | 88 MB (92.730.157 B) | 2026-04-24 22:49 | 139 gg | NON CLASSIFICABILE |
| Il nuovissimo pronto per la pubblicazione MB.mp4 | stessa cartella | 87 MB (90.860.163 B) | 2026-04-24 22:46 | 139 gg | NON CLASSIFICABILE |
| Video nuovissimo da fare con canva.mp4 | stessa cartella | 23 MB (24.140.582 B) | 2026-04-24 21:39 | 139 gg | NON CLASSIFICABILE |
| file spec CL.mp4 | stessa cartella | 19 MB (19.425.499 B) | 2026-04-25 02:09 | 138 gg | NON CLASSIFICABILE |
| file spec MB.mp4 | stessa cartella | 18 MB (18.925.471 B) | 2026-04-25 02:13 | 138 gg | NON CLASSIFICABILE |
| the beadt claude  Da fare con canva.mp4 | stessa cartella | 29 MB (30.115.252 B) | 2026-04-24 18:35 | 139 gg | **CLAUDE CODE / DIGITAL EMPIRE** (nome cita "claude"; il resto — "Da fare con canva" — indica però che manca ancora il montaggio: leggi come materiale non finito, non pubblicabile as-is) |
| video oggi .mp4 | stessa cartella | 120 MB (126.034.751 B) | 2026-04-24 18:46 | 139 gg | NON CLASSIFICABILE |
| video oggi 2 .mp4 | stessa cartella | 110 MB (114.830.401 B) | 2026-04-24 19:09 | 139 gg | NON CLASSIFICABILE |
| video oggi 3  (1).mp4 | stessa cartella | 109 MB (113.907.449 B) | 2026-04-24 19:09 | 139 gg | NON CLASSIFICABILE |
| video oggi 3 .mp4 | stessa cartella | 109 MB (113.904.297 B) | 2026-04-24 19:09 | 139 gg | NON CLASSIFICABILE |
| viedeo nuovo.mp4 | stessa cartella | 24 MB (24.765.108 B) | 2026-04-24 19:34 | 139 gg | NON CLASSIFICABILE |

Nota tema: "CE"/"MB"/"CL" sono etichette ricorrenti in tutta la cartella madre (`Page/Leo/`,
vedi §3) accanto a varianti esplicite "claude code" — sembrano 3 varianti/persone/hook diversi
dello stesso girato, ma **non esiste sul disco, in questa cartella, un file che dica cosa
significano** ("ce" e "mb" non sono spiegati né in un README né in un copy.md qui dentro).
Dichiarato come non classificabile, non indovinato.

### Deposito B — `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/` (4 cartelle, granularità cartella)

| Cartella | Percorso | Peso tot. | Data video.mp4 | Fermo da | Tema |
|---|---|---|---|---|---|
| video-01 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-01/` | 275 MB | 2026-08-17 13:31 | 24 gg | **ALTRA NICCHIA** — `copy.md`: "5 SEGNALI che una Donna Vuole che TU Faccia la Prima Mossa", canale dichiarato **@Legamidiamore** |
| video-02 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-02/` | 144 MB | 2026-08-23 23:52 | 18 gg | **ALTRA NICCHIA** (stesso canale/nicchia, verificato via `copy.md`) |
| video-03 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-03/` | 132 MB | 2026-08-26 01:19 | 15 gg | **ALTRA NICCHIA** (stesso canale) |
| video-04 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-04/` | 203 MB | 2026-08-29 14:39 | 12 gg | **ALTRA NICCHIA** (stesso canale, `metadata.json` presente) |

Contenuto interno tipo (video-01): `video.mp4` + `copy.md` + copertina placeholder PNG.
`video-02/03/04` hanno anche `metadata.json`. Tema verificato leggendo `copy.md`/`metadata.json`,
non solo il nome del file: tutti e 4 parlano di psicologia relazionale/segnali d'amore,
esplicitamente per il canale **@Legamidiamore**.

### Deposito C — `.../LIBRI/libri_pronti/` (5 cartelle libro, granularità cartella)

| Libro | Percorso | Peso tot. | Data ultimo tocco | Fermo da | Tema |
|---|---|---|---|---|---|
| The_Ninth_Winter | `company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/LIBRI/libri_pronti/The_Ninth_Winter/` | 4 MB | 2026-09-02 11:07 | 8 gg | **ALTRA NICCHIA** — narrativa (Amish suspense/thriller, "An Amish Suspense Novel"), niente a che fare con Claude Code |
| The_Quiet_Hours | stesso percorso base, `/The_Quiet_Hours/` | 6 MB | 2026-09-02 11:07 | 8 gg | **ALTRA NICCHIA** — narrativa |
| The_Second-Hand_Spellbook | `/The_Second-Hand_Spellbook/` | 7 MB | 2026-09-02 11:07 | 8 gg | **ALTRA NICCHIA** — narrativa |
| The_Winter_Term | `/The_Winter_Term/` | 1 MB | 2026-09-04 14:23 | 6 gg | **ALTRA NICCHIA** — narrativa |
| Proof_of_Murder | `/Proof_of_Murder/` | 0 MB (solo metadati) | 2026-09-04 11:01 | 6 gg | **ALTRA NICCHIA** — narrativa (giallo/thriller, dal titolo) |

Ogni cartella contiene `KDP_METADATA.txt`, `REPORT.md`, `validazione.json`, `README.txt`; le 3
complete al 100% hanno anche `.pdf`/`.epub`/`.docx` e copertina PNG già pronta (generata,
non da Max — vedi §4 per la contraddizione con la regola copertina).

**Totale verificato**: 16 (deposito A) + 4 (deposito B) + 5 (deposito C) = **25**, combacia
con ADR-016.

---

## 2. Conteggio per tema (sui 25 dichiarati + i 6 nuovi comparsi dopo)

| Tema | Pezzi (sui 25 originali) | Pezzi nuovi (comparsi 04-08/09, oltre i 25) |
|---|---|---|
| **CLAUDE CODE / DIGITAL EMPIRE** | **2** (`youtube page claude code.mp4`, `the beadt claude Da fare con canva.mp4` — quest'ultimo dichiaratamente non montato) | 0 |
| **ALTRA NICCHIA** | **9** (4 video Legami d'Amore + 5 libri narrativa) | 6 (video-05/06/07/08 = altri video Legami d'Amore; The_Coven_of_Lost_Ember + The_Midnight_Ledger = altri libri narrativa) |
| **NON CLASSIFICABILE** | **14** (i restanti file della cartella `da pubblicare`, nomi generici o etichettati "ce"/"mb"/"cl" senza fonte che li spieghi) | 0 |

**Sui 25 pezzi dell'ADR: 2 a tema (8%), 9 altra nicchia (36%), 14 non classificabili (56%).**
La AZIONE-5 dichiarava "3 video on-topic pronti"; verificato che **solo 1** è realmente dentro
il deposito sorvegliato e pronto al 100%, **1** è a tema ma esplicitamente non montato
("Da fare con canva"), e il terzo citato in AZIONE-5 (`call page claude code.mp4`) **non è
nella cartella `da pubblicare`**: sta un livello sopra, vedi §3.

---

## 3. La discrepanza — dove sono davvero i video "claude code"

AZIONE-5 §5 cita 3 file:
`Lancio corso skill beast/Page/Leo/da pubblicare/youtube page claude code.mp4`,
`.../Leo/call page claude code.mp4`, `.../Leo/contesto page claude code.mp4`.

Verificato sul disco: i primi due percorsi indicati per il 2° e 3° file sono **sbagliati** —
`call page claude code.mp4` e `contesto page claude code.mp4` non sono dentro `da pubblicare`,
sono un livello sopra, in `Lancio corso skill beast/Page/Leo/` (la cartella grezza, non
sorvegliata dall'Ultimo Metro), insieme a **decine** di altri file grezzi con lo stesso schema
di nomi (varianti "ce"/"mb"/"claude code" per: Framework, Progetti, contesto, call):

| File | Percorso reale | Peso | Data |
|---|---|---|---|
| call page claude code.mp4 | `Lancio corso skill beast/Page/Leo/call page claude code.mp4` | 173 MB (181.289.155 B) | 2026-04-23 21:04 |
| contesto page claude code.mp4 | `Lancio corso skill beast/Page/Leo/contesto page claude code.mp4` | 92 MB (96.876.248 B) | 2026-04-22 17:39 |
| Progetti page claude code .mp4 | `Lancio corso skill beast/Page/Leo/Progetti page claude code .mp4` | 141 MB (147.695.549 B) | 2026-04-22 22:56 |

Questi 3 (+ le varianti "ce"/"mb" degli stessi: `call page ce.mp4`, `call page mb.mp4`,
`contesto page ce.mp4`, `contesto page mb.mp4`, `Progetti page ce.mp4`, `Progetti page mb.mp4`,
+ `Framework.mp4`/`Framework (1).mp4`/`Framework (2).mp4`) **non sono nel deposito
sorvegliato dall'Ultimo Metro, non compaiono nei 25/31 pezzi contati da ADR-016, e non hanno
`copy.md`/`metadata.json` che ne dichiari lo stato di montaggio**. Non è verificabile da qui
se siano girato grezzo, spezzoni per un montaggio futuro, o video finiti mai spostati nella
cartella giusta. Sono materiale potenzialmente a tema Claude Code (7 file "claude code"-named,
~750 MB), ma **fuori dal perimetro dichiarato "pronto"** — servono verifica di contenuto e
decisione editoriale, non sono pubblicabili come sono oggi secondo la stessa logica con cui
l'Ultimo Metro giudica gli altri depositi.

---

## 4. Cosa manca per pubblicare (solo i pezzi a tema Claude Code)

| Pezzo | Titolo | Descrizione | Copertina | Metadati (metadata.json/copy.md) | Manca |
|---|---|---|---|---|---|
| `youtube page claude code.mp4` | **NO** — nessun file titolo trovato in cartella | **NO** — nessun copy.md/descrizione in `da pubblicare` | **NO** | **NO** | Tutto: titolo, descrizione, copertina (da Max, mai dalla macchina — regola fissa), tag. La cartella `da pubblicare` ha SOLO i file .mp4, nessun copy.md/metadata.json come invece hanno `video-01..08` in VIDEO-PRONTI. Il flusso standard Digital Empire (`video.mp4`+`copy.md`+`metadata.json`) **non è stato applicato qui** |
| `the beadt claude Da fare con canva.mp4` | — | — | — | — | Il nome stesso dichiara "da fare con canva": non è nemmeno montato/finito, va escluso dal conteggio "pronti" |
| `call page claude code.mp4`, `contesto page claude code.mp4`, `Progetti page claude code.mp4` | **NO** | **NO** | **NO** | **NO** | Fuori dal deposito sorvegliato (§3): prima ancora di copy/copertina, serve decidere se sono utilizzabili e spostarli nel posto giusto — decisione, non compito di questo inventario |

**Nessuno dei pezzi a tema Claude Code ha oggi titolo, descrizione o metadata.json.** L'unico
che è "pronto" secondo la logica dei 3 file richiesti dal deposito (solo `.mp4`, i requisiti
del deposito A in `ultimo_metro.py` sono `[".mp4"]` senza copertina/metadati obbligatori) è
`youtube page claude code.mp4` — ma è pronto solo secondo la definizione ristretta dello
script, non secondo lo standard Digital Empire reale (`video.mp4`+`copy.md`+`metadata.json`)
che il deposito B (VIDEO-PRONTI) rispetta e il deposito A no.

**Copertina**: confermato, in nessuna delle cartelle esiste già una copertina fatta da Max per
questi file — coerente con la regola (la fa sempre Max, mai la macchina), ma vuol dire che va
fatta da zero, non recuperata.

---

## 5. Il canale — cosa è vivo, cosa è morto (fatti, con fonte)

| Canale | Stato | Prova sul disco |
|---|---|---|
| **@Legamidiamore** (YouTube) | **VIVO e attivo** — 14.700 iscritti, 471 video, la fabbrica YouTube ci carica sopra davvero (upload reali, non simulati) | `second-brain-vault/wiki/log.md` righe 811-812 (dati yt-dlp), righe 1160-1191 (fabbrica cablata + upload reale confermato `youtu.be/2t4BZR3KAiU`); `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-01..04/copy.md` dichiarano esplicitamente questo canale come destinazione |
| Canale YouTube per il funnel "Manuale Claude Code" | **MORTO** — dichiarato esplicitamente morto e dirottato | `second-brain-vault/wiki/log.md` righe 1093-1103 (2026-07-29): "il primo contenuto YouTube reale generato era ancora sul funnel morto 'Manuale Claude Code' — pivot deciso da Gael a @dosementale" |
| @dosementale | **Non nostro** — canale replicato per studio/rivendita, 198k iscritti ma ratio view/iscritti 0,3% (vanità, "iscritti gonfiati"), **zero legame dichiarato con il Manuale** | `second-brain-vault/wiki/log.md` riga 811 + `entities/Entity_Dose_Mentale_Channel.md`; confermato già in `AZIONE-5-CONTA-DEL-PUBBLICO.md` §2 |
| Instagram `crea.illtuo_impero` | **Morto/non aziendale** — è la pagina personale di Gael, non un canale Digital Empire; follower a zero per il lancio | `second-brain-vault/wiki/log.md` riga 805 ("Chiarita con Gael l'identità... sua pagina personale") + riga 787 ("IG crea.illtuo_impero a zero") |

**Conclusione fatti, non opinione**: oggi (2026-09-10) l'unico canale YouTube di proprietà
davvero vivo e in produzione è **@Legamidiamore**, ed è a tema sbagliato per il Manuale
(psicologia relazionale, non Claude Code/agenti/automazione). Non esiste nessun canale
attivo, di proprietà, a tema Claude Code su cui pubblicare i pezzi del deposito A.

---

## 6. Pezzi dichiarati dall'ADR ma NON trovati sul disco

**Nessuno.** Tutti i 25 pezzi elencati in `company/Memory/ULTIMO-METRO.md` (generato
03-09-2026) sono stati ritrovati, verificati e pesati uno per uno in §1. Zero file mancanti,
zero file spostati fuori posto rispetto ai 3 depositi ufficiali.

L'unica discrepanza reale è quella di §3: **2 dei 3 file citati testualmente in AZIONE-5**
(non nell'ADR-016 — l'ADR non li cita per nome) stanno in un percorso diverso da quello
scritto nel documento, un livello sopra la cartella sorvegliata. Puntatore da correggere in
`AZIONE-5-CONTA-DEL-PUBBLICO.md` §5 secondo la regola "mai stale" di CLAUDE.md.

---

## 7. Riepilogo numeri

- Pezzi ADR-016 (03/09): 25 — tutti verificati esistenti oggi (10/09).
- Pezzi reali oggi rieseguendo lo stesso script: **31** (+6 in 7 giorni, magazzino in crescita).
- Registro pubblicazioni (`company/Memory/pubblicati.json`): **non esiste** — zero pezzi
  segnati come usciti da quando l'Ultimo Metro è stato istituito.
- A tema Claude Code, dentro il deposito sorvegliato e realmente pronti: **1** su 25/31
  (`youtube page claude code.mp4`, 97 MB, fermo da 140 giorni) — e anche questo senza titolo,
  descrizione, copertina o metadata.json.
- A tema Claude Code fuori dal deposito sorvegliato, stato di montaggio non verificabile da
  qui: **7 file, ~750 MB** (`call/contesto/Progetti page claude code` + varianti ce/mb).
- Canale attivo di proprietà su cui questi pezzi potrebbero uscire oggi, a tema corretto:
  **zero**.
