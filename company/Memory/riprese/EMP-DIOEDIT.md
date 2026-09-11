# EMP-DIOEDIT — Studio dei VSL di Andrei Pascu → agente «Dio dell'Editing»

- **Aperto:** 2026-09-10 · **Stato:** APERTA (pausa chiesta da Max)
- **Come si riprende:** dire `EMP-DIOEDIT` in una chat nuova dentro Digital Empire.
- **Checkpoint di origine:** [CP-20260910-A6YV](../checkpoints/CP-20260910-A6YV.md)
- **Impianto completo (leggilo per primo):**
  `competitor/Andrei Pascu/vsl-study/PIANO-OPERATIVO-STUDIO-VSL.md`

**L'ordine di Max, in sostanza:** studiare nel minimo dettaglio tutti i VSL di Andrei — priorità
**Armageddon (ultimo lancio)** e **Claude Speedrun** — non per il contenuto ma per **il montaggio**:
ogni effetto, ogni suono e il momento esatto in cui entra, ogni font, colore, stacco, il tono di
voce, l'approccio, le leve psicologiche. Poi un rapporto sulla psicologia di quelle scelte, poi
critica e miglioramento integrale degli appunti, poi **un piano migliorato cinque volte** su come
architettare l'agente, e infine costruire l'agente ufficiale **«Dio dell'Editing»** — che risponde
solo a Emperator, con il suo libro e una cartella di reference ricchissima.

**Regola madre dello studio:** *la macchina misura, l'occhio giudica.*

---

## LA PRIMA COSA DA FARE ALLA RIPRESA

Misurare sul disco, non fidarsi di questa pagina:
```
ls "competitor/Andrei Pascu/vsl-study/misure/"
ls "competitor/Andrei Pascu/vsl-study/parlato/"
```
**Attenzione:** due Doom Bot erano ancora al lavoro quando è arrivata la pausa. Gli agenti non
sopravvivono alla chiusura della chat, **ma il loro lavoro resta sul disco** — e può essere
completo, parziale o mancante. Si guarda, non si assume. Entrambi gli script sono **rieseguibili e
idempotenti**: `vsl-study/scripts/misura_vsl.py` e `vsl-study/scripts/parlato_misura.py`.

---

## DOVE SIAMO

| Fase | Cosa | Stato |
|---|---|---|
| **0** | Approvvigionamento dei VSL veri | ✅ **FATTO** — 10 video, 36:52, 989 MB |
| **1** | Misura a macchina (stacchi, audio, frame) | 🔁 fatta su `armageddon-home`, gli altri da verificare |
| **3** | Parlato con i tempi | 🔁 fatta su `armageddon-home`, gli altri da verificare |
| **2** | Visione dei frame (Claude guarda davvero) | ⬜ non iniziata |
| **4** | I tre rapporti (montaggio · psicologia · comunicazione) | ⬜ non iniziata |
| **5** | Critica e miglioramento integrale | ⬜ non iniziata |
| **6** | Piano dell'agente, **migliorato 5 volte** (P0→P5) | ⬜ non iniziata |
| **7** | Costruzione di «Dio dell'Editing» + reference | ⬜ non iniziata |

---

## COSA C'È GIÀ (non rifare)

### I 10 VSL — `vsl-study/sorgenti/<slug>/video.mp4`
`armageddon-home` (13:28, 357 MB, il pezzo grosso) · `claude-speedrun-hero` / `-sez9` / `-sez14` ·
`arma-outfunnel-vsl` · `arma-outemail-vsl` / `-secondo` · `outfunnel-vsl-1` / `-2` · `outheadline-vsl`.
Tutti 1080p h264 + aac 48 kHz. Inventario e metodo di ripetizione in `sorgenti/_INVENTARIO.md`.
**Non presi:** `apsales.eu` (server con TLS rotto, `SSLV3_ALERT_HANDSHAKE_FAILURE` — da ritentare,
non è protezione), `arma-outheadline` e `arma-outviral` (**non hanno un VSL**, verificato dal vivo).
I video sono fuori da git (`*.mp4` nel `.gitignore`), come i frame estratti.

### I primi numeri veri di `armageddon-home` (13:28)
- **266 tagli**, 267 inquadrature, **19,7 tagli al minuto**; durata media 3,03 s, **mediana 1,84 s**,
  minima 0,2 s, massima 31,6 s.
- **Il montaggio è caricato all'inizio:** minuto 1 = **50 tagli**; minuto 14 = **6**.
- **Parlato al 97,9%** del video (13:11 su 13:28), 2.959 parole, **219,5 parole al minuto**,
  225 segmenti vocali.
- Soglia scene score **0,040**, calibrata guardando i fotogrammi prima/dopo su quattro bande di
  punteggio — non scelta a caso. **Limite dichiarato dallo script stesso:** i tagli in dissolvenza
  restano sotto qualsiasi soglia per fotogramma e sono sotto-contati (esempio misurato a 8,32 s).

### Tre fatti emersi già dall'approvvigionamento
1. Il player è **Vimeo** ovunque, tranne un residuo del vecchio sito su Squarespace.
2. **Due video sono riusati fra i lanci** (stessi id su due domini): riusa il girato invece di
   rigirarlo — è il «si specchia e si rilancia» applicato al video.
3. I tre VSL nuovi di Armageddon hanno **id consecutivi**: girati e caricati nella stessa sessione.

---

## VINCOLI DA NON DIMENTICARE
- **Solo materiale pubblicamente accessibile.** Ciò che sta dietro acquisto o login si dichiara e
  non si aggira.
- **Misurato e interpretato in colonne diverse, sempre.** Nessun aggettivo nelle fasi di misura.
- **Console Windows cp1252: nessuna emoji** nell'output degli script.
- **LANCI non si tocca** (perimetro di Gael).
- Scrivere i file di memoria con fine-riga **LF** (`newline=""` in Python), o il pre-commit blocca.
- I frame sono migliaia di PNG: restano fuori dal repo, si rigenerano con lo script.
