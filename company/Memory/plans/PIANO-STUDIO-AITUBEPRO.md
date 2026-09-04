# PIANO DI STUDIO — AI TUBE PRO (Smart Tube) + Bonus Esclusivi

> **Stato: PROPOSTA. Non si parte senza il via di Max.** (ordine esplicito, 2026-09-04)
> Autore: Emperator · Data: 2026-09-04 · Fonte: `corsi.muccarossa.com` (Mirko Delfino)
> Obiettivo: trasformare 167 lezioni in miglioramenti reali e misurabili della
> `YOUTUBE-AUTOMATION-FACTORY`.

---

## 1. COSA HO MISURATO DAVVERO (non stimato)

Entrato nel portale con le credenziali di Max, censiti i corsi uno per uno.

| Corso | Lezioni | Perimetro |
|---|---|---|
| **AI TUBE PRO — SMART TUBE** | **116** | ✅ da studiare |
| **Bonus Esclusivi** | **51** | ✅ da studiare |
| Google Automation Platinum | 181 | ❌ fuori perimetro (ordine di Max) |
| **TOTALE DA STUDIARE** | **167** | |

### 1.1 Le categorie di AI TUBE PRO (11)

| # | Categoria | Lezioni | Mappa sulla fabbrica |
|---|---|---|---|
| 1 | Intelligenza Artificiale | 12 | trasversale / tool |
| 2 | Le Basi di YouTube | 7 | WF1 nicchia + monetizzazione |
| 3 | YouTube Setup & Launchpad | 15 | WF1 + branding canale |
| 4 | Metodo AI Tube | 21 | **WF3 produzione** (il cuore) |
| 5 | Smart Tube (da smartphone) | 16 | perimetro diverso — vedi §5 |
| 6 | YouTube Viral Mastery | 13 | **WF4 pubblicazione + SEO + CTR** |
| 7 | YouTube Masterclass | 7 | strategia / scaling / multicanale |
| 8 | Liveclass Studenti | 11 | casi reali, aggiornamenti |
| 9 | BONUS | 9 | masterclass verticali |
| 10 | Interviste Speciali | 3 | ads, engagement |
| 11 | Workshop | 3 | dietro le quinte, scaling |

### 1.2 Le categorie di Bonus Esclusivi (3)

| # | Categoria | Lezioni | Nota |
|---|---|---|---|
| 1 | Masterclass 2026 | 8 | **il materiale più recente** (Fliki 4.0, miniature ad alto CTR, video automatici infiniti) |
| 2 | Nicchia Criptovalute | 11 | verticale completo di nicchia, dallo script alla pubblicazione |
| 3 | Masterclass Storiche 2019-2025 | 32 | archivio, valore decrescente col tempo |

### 1.3 Il fatto tecnico che decide tutto

- I video **non hanno tasto di scaricamento**. Arrivano a pezzi (HLS) da
  `content.apisystem.tech`, con un **gettone che scade**, in qualità fino a 1080p.
  → serve un ingest dedicato: il browser apre la lezione, si cattura al volo l'indirizzo
  del flusso col gettone, e si scarica con gli strumenti che già abbiamo.
- **Non c'è nessun testo della lezione, nessun sottotitolo, nessun allegato.** La conoscenza
  è **solo dentro il parlato e dentro lo schermo**.
- **Strumenti presenti**: `ffmpeg` 8.1.1 ✅, `yt-dlp` 2026.08.19 ✅.
- **Strumento mancante**: nessun trascrittore installato (`whisper` e `faster-whisper` assenti).
  **Senza questo il corso lo guardo muto.** È l'unica installazione che il piano richiede.

---

## 2. COSA C'È GIÀ IN CASA (e che non va riscritto — ADR-003)

**Empire Studio** ha già la pipeline di studio a 9 stage, gli invarianti giusti
(«il video va visto», «no-finto», tracciabilità `frame-NNN.png`), l'estrattore di frame,
il rilevatore di scene, lo scrittore wiki e il ponte con Memory Empire.
**Manca solo l'ingest**: il suo `yt_ingest.py` parla YouTube/TikTok, non una piattaforma a
login con flusso protetto. Si **affianca** un ingest nuovo, non si tocca quello che gira.

**La fabbrica YouTube** ha 5 flussi (WF1 nicchia → WF5 audit), 33 agenti su 4 livelli
(capi, controllo, operatori, regolatori, supporto) e 5 regolatori con soglie dure in
`regolatori.py`. **È qui che le lezioni devono atterrare.**

---

## 3. IL METODO — cosa succede per OGNI lezione

Sette passi, sempre gli stessi, nessuno saltabile:

1. **Scarico** il video della lezione (flusso + gettone catturati dal browser).
2. **Trascrivo il parlato** — è dove sta il 70% della conoscenza di un corso parlato.
3. **Estraggo i frame** e **tolgo i doppioni** (lo schermo di un tutorial resta fermo a lungo:
   il rilevatore di scene taglia il 90% del materiale senza perdere niente).
4. **Guardo i frame** con i miei occhi, non li deduco. Ogni cosa scritta a schermo che cito
   porta il numero del frame esatto.
5. **Appunti** — grezzi, integrali, con il minuto esatto. Mai riassunti.
6. **Report della lezione** — la lezione digerita: cosa insegna, cosa contraddice quello che
   facciamo oggi, cosa vale per noi e cosa no.
7. **Script Python della lezione** — le regole imparate diventano **codice eseguibile**,
   non prosa. Un file per lezione, tutti con la stessa forma:

```python
# regole/04-metodo-ai-tube/L07_text_to_speech.py
FONTE = "AI TUBE PRO / Metodo AI Tube / lezione 7"
REGOLE = [
    {
        "id": "TTS-01",
        "regola": "...",                    # la regola in italiano
        "prova": "frame-0142.png @ 08:31",  # dove l'ho vista
        "tocca": "fliki_client.py",         # dove si applica nella fabbrica
        "azione": "modifica|nuovo|conferma",
        "rischio": "basso|medio|alto",
    },
]
def verifica(fabbrica): ...   # controlla se la fabbrica rispetta già la regola
```

Un `registro_regole.py` li carica tutti: **le regole diventano interrogabili e
verificabili**, invece di restare 167 documenti che nessuno rilegge.

---

## 4. IL PUNTO PIÙ DELICATO — e la mia obiezione al tuo ordine

**Il tuo ordine:** dopo ogni lezione, migliorare subito il workflow.
**Il rischio vero:** la fabbrica **sta producendo video veri in questo momento**
(tre oggi). 167 modifiche consecutive a un motore in produzione, senza collaudo fra una e
l'altra, è il modo più veloce per romperla — e ADR-003 dice che un sistema attivo non si
riscrive, si avvolge.

**La soluzione che rispetta l'ordine senza rompere niente — due binari:**

| | **BINARIO A — subito, dopo ogni lezione** | **BINARIO B — a fine categoria** |
|---|---|---|
| Cosa tocca | conoscenza, agenti, regolatori documentali, reference, skill, script delle regole | il motore vero (`02-AUTOMAZIONI-E-SCRIPTS/`), le soglie dei gate |
| Rischio | **zero**: non passa da lì nessun video in produzione | reale: qui ci passano i video |
| Collaudo | il validatore delle regole | `test_youtube_apex7.py` (11/11 oggi) + un video di prova |

Così **dopo ogni lezione la fabbrica migliora davvero** — è il binario A, e non è un
contentino: agenti e regolatori sono il cervello della fabbrica. E il motore cambia solo
quando c'è una batteria di regole coerenti e un collaudo che le regge.

**Se preferisci il rischio, lo prendo:** dimmelo e applico tutto subito, anche al motore.
È una tua decisione, non mia.

---

## 5. LA PRIORITÀ — non tutte le lezioni valgono uguale

167 lezioni studiate tutte alla stessa profondità sono ~40 ore di video e settimane di
lavoro. **Studiarle tutte con la stessa cura è esso stesso un errore di pigrizia al
contrario**: spendere su «Come registrarsi alla community» quello che serve a «SEO YouTube
manuale operativo».

**Tre profondità, decise per categoria:**

| Profondità | Cosa faccio | Su cosa |
|---|---|---|
| **ORO** — chirurgica | tutti e 7 i passi, frame fitti, script regole completo | Metodo AI Tube · YouTube Viral Mastery · Masterclass 2026 · Nicchia Crypto · YouTube Masterclass |
| **ARGENTO** — piena ma più rapida | 7 passi, frame più radi | Basi YouTube · Setup & Launchpad · Intelligenza Artificiale · BONUS · Interviste |
| **BRONZO** — parlato + schermate chiave | trascrizione + soli frame unici, appunti, niente script se non emerge nulla di nuovo | Liveclass storiche · Smart Tube (§5.1) · Workshop |

**5.1 Su «Smart Tube» sono onesto:** 16 lezioni su come fare tutto da smartphone. La nostra
fabbrica è un motore Python su PC: quasi niente si trasferisce. Le studio in BRONZO per non
perdere le idee di metodo (nicchie, ottimizzazione canale), ma **non fingerò** di ricavarne
miglioramenti tecnici che non esistono.

**L'ordine di studio che propongo** — dal più utile alla fabbrica:
1. Metodo AI Tube (21) → cuore della produzione
2. YouTube Viral Mastery (13) → SEO, copertine, CTR, pubblicazione
3. Masterclass 2026 (8) → il materiale più fresco, Fliki 4.0
4. Nicchia Criptovalute (11) → un verticale completo, modello replicabile
5. YouTube Masterclass (7) + Basi (7) + Setup (15)
6. Intelligenza Artificiale (12) + BONUS (9) + Interviste (3)
7. Liveclass (11) + Storiche (32) + Smart Tube (16) + Workshop (3)

---

## 6. COSA CONSEGNO, E DOVE

```
company/Memory/studi/aitubepro/
├── PIANO.md                      questo file
├── DURATE.md                     censimento durate (passo 0)
├── <categoria>/
│   ├── L01-<slug>/
│   │   ├── appunti.md            grezzi, integrali, col minuto
│   │   ├── report.md             la lezione digerita
│   │   └── frame-scelti.md       quali frame ho guardato e perché
│   ├── REPORT-CATEGORIA.md       ← a fine categoria, come hai chiesto
│   └── APPUNTI-CATEGORIA.md      ← a fine categoria
└── regole/
    ├── registro_regole.py        carica e interroga tutte le regole
    └── <categoria>/L<NN>_*.py    uno script per lezione
```

I video e i frame **restano fuori da git** (ADR-013: un push è già morto a 899 MB, e un
`git stash pop` ha quasi spedito 13,4 GB su un repo pubblico).

**A fine categoria**, come hai ordinato: report completo, appunti completi, analisi
trasversale su tutto quello che ho studiato, **più** il gate del binario B.

---

## 7. IL PASSO ZERO (prima di qualunque lezione)

Prima di studiare voglio sapere **quanto dura davvero** quello che sto per studiare — senza,
qualunque stima di tempo che ti do è aria.

1. **Censimento durate**: apro le 167 lezioni una per una, leggo la durata dal lettore, e
   scrivo `DURATE.md`. Costo: ~40 minuti di macchina, zero di ragionamento.
2. **Installo il trascrittore** (`faster-whisper`) e lo collaudo su **una** lezione.
3. **Prova completa end-to-end su UNA sola lezione** — la prima del Metodo AI Tube.
   Se i sette passi reggono su una, reggono su 167. Se non reggono, l'ho scoperto al primo
   video e non al centesimo.

**Solo dopo questi tre, e solo col tuo via, parte lo studio vero.**

---

## 8. PRE-MORTEM — è il giorno dopo e questo piano è fallito. Perché?

| Causa | Probabilità | Come la disinnesco |
|---|---|---|
| **Il gettone del video scade a metà scaricamento** | alta | catturo il gettone e scarico subito, una lezione per volta; se scade, riapro la pagina e ricatturo — mai code lunghe |
| **La trascrizione è lenta o sbagliata** | media | collaudata al passo zero su una lezione vera; se la macchina non regge, scendo di modello e lo dichiaro |
| **Il contesto della chat finisce a metà corso** | **certa** | checkpoint di ripresa a **ogni categoria chiusa** (`EMP-XXXX`): la chat nuova riparte esatta |
| **Le modifiche rompono la fabbrica** | media | binario B con collaudo, `test_youtube_apex7.py` verde prima di ogni commit |
| **Studio tutto e non cambia niente** | media | ogni lezione produce regole **eseguibili** con `tocca:` e `azione:`; a fine categoria conto quante sono state applicate. Zero applicate = categoria fallita, e lo scrivo |
| **Il disco si riempie** | media | 360p per i frame, video cancellato dopo l'estrazione, solo i frame scelti restano |

---

## 9. COSA È CAMBIATO NEI TRE GIRI DEL PIANO

| Giro | Il difetto che ho trovato | Cosa ho cambiato |
|---|---|---|
| v1 → v2 | studiavo 167 lezioni tutte uguali, e modificavo il motore in produzione dopo ognuna | tre profondità (§5) + due binari di applicazione (§4) |
| v2 → v3 | davo per scontato di poter scaricare i video, e non sapevo quanto dura il corso | ricognizione tecnica reale (§1.3) + passo zero obbligatorio (§7) |
| v3 → finale | 167 script Python sarebbero stati 167 documenti morti | forma unica con `REGOLE` + `verifica()` + registro che li interroga (§3) |

---

## 10. L'OBIEZIONE PIÙ FORTE CONTRO QUESTO PIANO — e cosa rispondo

> *«Stai per spendere settimane su un corso di YouTube automation mentre l'azienda ha
> 25 pezzi finiti mai pubblicati (ADR-016) e non misura un euro. Il collo di bottiglia
> non è la conoscenza: è che non pubblichiamo.»*

**È vera, e va detta prima di partire.** La risposta onesta è che le due cose non si
escludono, ma **l'ordine conta**: le categorie che ho messo per prime — Metodo AI Tube,
Viral Mastery, Masterclass 2026 — sono esattamente quelle che toccano produzione,
copertine, CTR e pubblicazione, cioè il collo di bottiglia. Se dopo le prime due categorie
la fabbrica non pubblica più e meglio di adesso, **il piano ha fallito la sua prova**, e va
fermato invece di continuare per inerzia.

**Questa è la mia raccomandazione**, non una condizione: decidi tu.
