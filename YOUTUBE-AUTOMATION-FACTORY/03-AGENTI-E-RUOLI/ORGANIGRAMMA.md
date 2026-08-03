---
Type: CONCEPT
Status: Active
Tags: #youtube #agenti #organigramma #gerarchia
Created: 2026-08-03
Last updated: 2026-08-03
Owner: GAEL · Controllore: regolatori L3 · Origine: FORGE · Governo: ADR-006/ADR-008
---

# Organigramma — YouTube Automation Factory

La fabbrica non è una fila di script: è un'**organizzazione con gerarchia, reparti separati e
diritti di decisione espliciti**. Chi esegue non approva, chi approva non esegue, chi regola può
fermare chiunque.

## Principio delle 3 firme
Nessun contenuto arriva alla pubblicazione senza tre firme distinte, di tre livelli diversi:
1. **Esegue** un operatore (L2)
2. **Approva** il capo del reparto competente (L1)
3. **Non è stato bloccato** dai regolatori (L3)

Un capo non può approvare il proprio lavoro. Un regolatore non produce contenuti: può solo
lasciar passare o bloccare, e deve motivare il blocco citando la regola violata.

## Livelli

| Livello | Chi | Potere |
|---|---|---|
| **L0** | `direttore-fabbrica` (ex conductor) | Apre/chiude i run, assegna priorità, arbitra i conflitti fra capi. **Non** scrive contenuti. |
| **L1** | Capi reparto | **Decidono** (sì/no) sul lavoro del proprio reparto. Possono respingere e rimandare indietro. |
| **L2** | Operatori | **Eseguono**. Non decidono se una cosa va pubblicata. |
| **L3** | Regolatori e gate | **Bloccano**. Potere di veto su chiunque, L0 compreso. Non producono. |
| **S** | Supporto | Memoria e auto-miglioramento. Trasversali, nessun potere decisionale. |

**Regola di escalation:** un operatore che trova un conflitto fra due regole non decide: passa al
proprio capo (L1). Un capo che trova un conflitto fra due reparti passa a L0. Un blocco di un
regolatore (L3) **non è appellabile da L1**: solo Gael può sbloccarlo, e la deroga va scritta in
memoria.

---

## Reparti

### 🔍 Reparto RICERCA — *cosa copiamo*
**Capo:** `capo-ricerca` (L1) — decide **quale video si copia**, o che non se ne copia nessuno.

| Agente | Livello | Fa |
|---|---|---|
| [`video-hunter-playwright`](operatori/video-hunter-playwright.md) | L2 | Entra su YouTube con Playwright e raccoglie i video reali del canale target con le loro views |
| [`transcript-collector`](operatori/transcript-collector.md) | L2 | Scarica il transcript reale del video scelto |
| [`video-analyst`](operatori/video-analyst.md) | L2 | Calcola velocity (views/ora), maturità, coerenza col tema della nicchia |
| [`capo-ricerca`](capi/capo-ricerca.md) | L1 | Firma la scelta del video: views **e** argomento, non solo i numeri |

### ✍️ Reparto COPY — *cosa diciamo*
**Capo:** `capo-copy` (L1) — approva **ogni testo** che esce dalla fabbrica.

| Agente | Livello | Fa |
|---|---|---|
| [`copy-researcher`](operatori/copy-researcher.md) | L2 | Studia i copy reali di @dosementale (titoli, hook, descrizioni) e mantiene lo studio nel second brain |
| [`script-writer`](operatori/script-writer.md) | L2 | Riscrive lo script: originale e **migliore** dell'originale, mai una copia |
| [`title-writer`](operatori/title-writer.md) | L2 | Titolo, descrizione e tag |
| [`thumbnail-copywriter`](operatori/thumbnail-copywriter.md) | L2 | Il testo che compare sulla copertina |
| [`capo-copy`](capi/capo-copy.md) | L1 | Firma tutti i testi. **Deve** passare dal settore copy di Digital Empire (skill `cro-copy-architect`) |

### 🎬 Reparto PRODUZIONE — *come lo facciamo*
**Capo:** `capo-produzione` (L1) — decide quando un video è pronto e firma voce, sottotitoli e copertina.

| Agente | Livello | Fa |
|---|---|---|
| [`voice-caster`](operatori/voice-caster.md) | L2 | Sceglie voce e preset sottotitoli su Fliki entro la configurazione approvata |
| [`video-producer`](operatori/video-producer.md) | L2 | Genera il video via API Fliki |
| [`thumbnail-designer`](operatori/thumbnail-designer.md) | L2 | Genera la copertina su Arena via Playwright: **adattamento completo**, originale e migliore |
| [`capo-produzione`](capi/capo-produzione.md) | L1 | Firma il file finale dopo verifica sul **file vero** (ffprobe/fotogrammi), mai sulla risposta API |

### 📊 Reparto INTELLIGENCE — *dove andiamo*
**Capo:** `capo-strategia` (L1) — decide se aprire una nicchia o un canale nuovo. **Non** può cambiare la nicchia in corso.

| Agente | Livello | Fa |
|---|---|---|
| [`competitor-analyst`](operatori/competitor-analyst.md) | L2 | Analizza i competitor della nicchia: cosa funziona e perché |
| [`channel-performance-analyst`](operatori/channel-performance-analyst.md) | L2 | Analizza le performance del **nostro** canale |
| [`channel-scout`](operatori/channel-scout.md) | L2 | Trova **altri canali** della stessa nicchia oltre a @dosementale |
| [`niche-scout`](operatori/niche-scout.md) | L2 | Trova **nicchie profittevoli** nuove (proposte, non attivazioni) |
| [`capo-strategia`](capi/capo-strategia.md) | L1 | Firma le proposte di espansione. Ogni cambio di nicchia richiede l'ok di Gael |

### 🛡️ REGOLATORI (L3) — *cosa non si fa mai*
Trasversali a tutti i reparti, potere di blocco.

| Regolatore | Blocca se… |
|---|---|
| [`regolatore-nicchia`](regolatori/regolatore-nicchia.md) | il contenuto esce dalla nicchia, o qualcuno prova a cambiare canale target |
| [`regolatore-originalita`](regolatori/regolatore-originalita.md) | lo script somiglia troppo al transcript sorgente (copia mascherata) |
| [`regolatore-qualita`](regolatori/regolatore-qualita.md) | durata < 12 min, voce sbagliata, sottotitoli assenti — verificato sul file vero |
| [`regolatore-configurazione`](regolatori/regolatore-configurazione.md) | qualcuno modifica la configurazione Fliki approvata da Gael |
| [`regolatore-copy`](regolatori/regolatore-copy.md) | un testo non è passato dal settore copy di Digital Empire |

**Gate storici** (restano, sono regolatori a tutti gli effetti): [`niche-gate`](controllo/niche-gate.md),
[`seo-gate`](controllo/seo-gate.md), [`qa-audio-video`](controllo/qa-audio-video.md),
[`performance-auditor`](controllo/performance-auditor.md).

### 🧠 SUPPORTO
[`memory-keeper`](supporto/memory-keeper.md) · [`self-improver`](supporto/self-improver.md)

---

## Flusso di un video, con le firme

```
[L2 video-hunter-playwright] naviga YouTube → lista video reali con views
        ↓
[L2 video-analyst] velocity + coerenza nicchia
        ↓
[L1 capo-ricerca] ⚖️ DECIDE: questo video si copia?  ──no──→ torna alla ricerca
        ↓ sì
[L2 transcript-collector] transcript reale
        ↓
[L2 copy-researcher] studio copy @dosementale (second brain)
        ↓
[L2 script-writer] script originale e migliore
        ↓
[L3 regolatore-originalita] 🛡️ è una copia? ──sì──→ BLOCCO, riscrivi
        ↓ no
[L1 capo-copy] ⚖️ FIRMA i testi (via settore copy Digital Empire)
        ↓
[L2 voice-caster + video-producer] video su Fliki
[L2 thumbnail-copywriter + thumbnail-designer] copertina su Arena
        ↓
[L3 regolatore-qualita + regolatore-configurazione] 🛡️ verifica sul FILE VERO
        ↓
[L1 capo-produzione] ⚖️ FIRMA il video finito
        ↓
[L3 seo-gate] 🛡️ → pubblicazione
        ↓
[L2 channel-performance-analyst] → [S self-improver] → memoria
```

## Invarianti (nessuno può violarle, nemmeno L0)
1. **La nicchia non cambia mai** senza ok esplicito di Gael.
2. **Mai copia verbatim**: lo script è riscritto, e deve essere *migliore* dell'originale.
3. **La configurazione Fliki approvata non si tocca** (blocco ⛔ in `fliki_client.py`).
4. **Si verifica sempre il file vero**, mai la risposta dell'API.
5. **Ogni errore va in memoria** e non si ripete (`errori-da-non-ripetere`).

## Connessioni
- [[conductor]] — il direttore di fabbrica
- [[Digital_Empire_6_Phase_Process]] — il metodo di cui questa fabbrica è un'istanza
- `company/Memory/RULES-VIDEO-FACTORY-DOSEMENTALE.md` — le regole operative vincolanti
