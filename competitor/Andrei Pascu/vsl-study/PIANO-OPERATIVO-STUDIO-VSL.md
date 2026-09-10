# STUDIO VSL ANDREI PASCU → «DIO DELL'EDITING» — impianto operativo

**Codice ripresa:** `EMP-DIOEDIT` · **Aperto:** 2026-09-10 · **Direttore:** Emperator (non delegato)

**Ordine di Max, in sostanza:** studiare nel minimo dettaglio tutti i VSL di Andrei Pascu — con
priorità all'**ultimo lancio (Armageddon)** e a **Claude Speedrun** — non per il contenuto in sé, ma
per **il montaggio, l'approccio, il modo di comunicare e le leve psicologiche**: ogni effetto, ogni
suono e il momento esatto in cui entra, ogni font, ogni colore, ogni stacco, il tono di voce, il tipo
di inquadratura. Poi: un rapporto sulla psicologia di quelle scelte, una critica e un miglioramento
integrale degli appunti, **un piano migliorato cinque volte** su come architettare l'agente, e infine
la costruzione dell'agente ufficiale **«Dio dell'Editing»**, che risponde solo a Emperator, con il suo
libro e una cartella di reference.

**La regola madre di questo studio:** *la macchina misura, l'occhio giudica.* Niente di ciò che si
può misurare (durata di un'inquadratura, decibel, colore esatto, timestamp di uno stacco) va scritto
a impressione. E niente di ciò che va giudicato (perché quell'effetto lì, perché quel suono in quel
punto) va lasciato decidere a uno script.

---

## Le sette fasi

### FASE 0 — Approvvigionamento *(in corso)*
Prendere i **file veri** dei VSL dalle sue pagine pubbliche. Senza i video non esiste studio del
montaggio: si racconterebbe a memoria, e a memoria non si lavora.
→ `vsl-study/sorgenti/<slug>/video.mp4` + `sorgente.json` + `_INVENTARIO.md`.
**È il collo di bottiglia: tutte le fasi successive dipendono da qui.** Ciò che non è pubblicamente
accessibile si dichiara tale e non si aggira.

### FASE 1 — Misura a macchina
Nessun giudizio, solo numeri, tutti con timestamp:
- **ffprobe** — durata, fps, risoluzione, bitrate, codec.
- **Stacchi** — rilevamento scene con ffmpeg: lista dei tagli al centesimo, durata di ogni
  inquadratura, ritmo di montaggio (media, mediana, distribuzione, dove accelera e dove rallenta).
- **Audio** — traccia estratta e misurata nel tempo (loudness EBU R128, picchi, silenzi): dove entra
  la musica, dove c'è uno stinger, dove il parlato resta solo, dov'è il silenzio prima di un colpo.
- **Frame densi** + riduzione ai frame in cui lo schermo cambia davvero.
→ `vsl-study/misure/<slug>/`

### FASE 2 — Visione
Claude **guarda** i frame chiave, uno per uno: testo a schermo, font, colori esatti, tipo di
inquadratura, effetti (zoom, jump cut, b-roll, screen recording, sottotitoli, maschere), grafica,
come è vestito, dove guarda, cosa fa la mano.
→ `vsl-study/visione/<slug>/`

### FASE 3 — Parlato
Trascrizione con timestamp + **come** lo dice: ritmo, pause, dove alza la voce, dove rallenta, quali
parole cadono sullo stacco. Il parlato si incrocia con gli stacchi della Fase 1: **la sincronia fra
parola e taglio è metà del mestiere.**
→ `vsl-study/parlato/<slug>/`

### FASE 4 — I rapporti
1. **Rapporto di montaggio** — ogni effetto, suono, font, colore, transizione, con il timestamp e la
   ricorrenza. Non un riassunto: un catalogo.
2. **Rapporto di psicologia** — perché quella scelta lì: cosa fa allo spettatore quel suono in quel
   punto, quello stacco su quella parola, quel colore su quella cifra.
3. **Rapporto di comunicazione** — approccio, tono, postura, come apre, come tiene, come chiude.
→ `vsl-study/rapporti/`

### FASE 5 — Critica e miglioramento integrale
Ogni rapporto viene attaccato da forze indipendenti, e **ogni giro attacca il giro prima, mai
l'originale**. Ciò che è impressione e non misura viene marcato o ucciso. Gli appunti si riscrivono
interi, non si rattoppano.
→ `vsl-study/critiche/`

### FASE 6 — Il piano dell'agente, migliorato cinque volte
Come va architettato «Dio dell'Editing» al millimetro: identità, poteri, libro, cartella di
reference, gate, chi lo invoca, cosa rifiuta. **P0 → P1 → P2 → P3 → P4 → P5**: cinque miglioramenti
completi, ognuno che attacca il precedente. I giri restano scritti, non si cancellano.
→ `vsl-study/piano-agente/`

### FASE 7 — Costruzione
L'agente ufficiale + la sua cartella di reference (strategie di montaggio, catalogo dei suoni,
tipografia, colore, ritmo, aperture, chiusure). **Vincolo di casa: ogni pezzo nuovo deve nominare chi
lo invoca.** «Dio dell'Editing» risponde a Emperator: è Emperator che gli dà i compiti.
→ `.claude/agents/dio-editing.md` + `.claude/agents/dio-editing/references/`

---

## Vincoli
- **Solo materiale pubblicamente accessibile.** Ciò che sta dietro un acquisto o un login si dichiara
  e non si aggira.
- **Nessun numero senza fonte.** Ogni cifra porta il file e il timestamp da cui viene.
- **Console Windows cp1252:** nessuna emoji nell'output degli script.
- **L'ecosistema LANCI non si tocca** (perimetro di Gael).
- Ciò che è **misurato** e ciò che è **interpretato** stanno in colonne diverse, sempre.
