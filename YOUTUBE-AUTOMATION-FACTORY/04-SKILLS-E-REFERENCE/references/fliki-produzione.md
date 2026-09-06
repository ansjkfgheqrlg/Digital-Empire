# Reference — Produzione con Fliki (testo → video)

> Conoscenza on-demand per `video-producer`. Fonte: MKD §3. Sito: fliki.ai.

> ## ⚠️ LEGGI QUESTO PRIMA DEL RESTO (A4-L04-03 · 2026-09-05)
>
> **Tutto ciò che segue descrive Fliki usato A MANO nell'interfaccia. La nostra fabbrica non usa
> l'interfaccia.** Genera **via API** (`02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py`), con
> `shouldExport: True`: nessun browser aperto, nessuna anteprima, nessun clic.
>
> **Cosa imposta davvero la nostra catena (via API):**
> `aspectRatio` (oggi `16:9` fisso) · `resolution: 1080p` · `voiceId` · `visuals` (ai/stock) ·
> `sceneBreakdown: lineBreak` · `subtitlePresetId` + `highlightSubtitles` · `aiVideoModel` +
> `aiVideoClipPercentage` + `imageAnimationPreset` · `duration` (1-15 minuti, campo inerte sulla
> durata finale) · `fileName`.
>
> **Cosa esiste in Fliki ma la nostra catena NON tocca** (verificato sul payload il 2026-09-05):
> musica di sottofondo e suo volume · transizioni fra scene · durata della singola scena ·
> pause (`Add pause`) · velocità e intonazione (`Tune → Rate`) · mappa delle pronunce
> (`More → Pronunciation map`) · anteprima prima dell'export · caricamento di clip proprie.
>
> **Regola d'uso di questa scheda:** i passaggi qui sotto valgono per capire *lo strumento* e per
> un eventuale intervento manuale straordinario. **Non sono istruzioni per la catena**, e non
> vanno copiati in una spec di produzione. Le pronunce si correggono nel testo dello script, con
> `references/lessico-pronuncia.md`.

---

## ⚠️ DUE COSE CHE STANNO NELL'ACCOUNT, NON NEL CODICE (A4-L19 · 2026-09-06)

### 1. L'ID del canale YouTube va registrato nel profilo Fliki

Fliki espone in **`Profile`** un campo **`YouTube channel ID(s)`** (due caselle), il cui scopo
dichiarato è **prevenire i reclami di copyright** sui contenuti generati con la piattaforma: si
registra l'ID del canale su cui quei video verranno pubblicati, e in caso di reclamo si dispone
della **licenza Fliki** da opporre.

**Come si trova l'ID del canale:** YouTube → il proprio canale → in basso a sinistra
**Impostazioni** → **Visualizza impostazioni avanzate** → si copia **l'ID del canale**. Poi si
incolla nel campo di Fliki e si preme **Update**.

**Cosa copre e cosa non copre — leggere prima di stare tranquilli:**

| ✅ Copre | ❌ Non copre |
|---|---|
| le **clip stock** che Fliki ci fornisce | il materiale che **carichiamo noi** |
| le **musiche** della libreria Fliki | qualunque contenuto di **terzi** |

Non è un interruttore che spegne il problema del diritto d'autore: è la registrazione della nostra
licenza presso il fornitore delle clip. *(Il corso lo presenta come «da questo momento non avrò
più problemi di copyright», e aggiunge «nel 99,9% dei casi» — che è **una stima detta a voce**,
non un dato.)*

**Stato nostro:** ⏳ **DA FARE.** Verificato il 2026-09-06: in tutta la fabbrica questo campo non
era mai stato nominato. Va compilato **a mano** per **`dosementale`** e **`legamidiamore`**.
**Assegnato al gate di categoria A4.** Finché non è fatto, questa scheda descrive una cosa giusta
e non eseguita — ed è scritto qui perché non venga scambiata per fatta.

### 2. I minuti sono un plafond mensile, e il tetto è negoziabile

L'abbonamento dà un monte minuti **al mese**, che si consuma in base a **cosa** si genera (testo,
immagini, musica: dentro Fliki c'è un tutorial sui crediti, che cambia spesso).

**Il tetto non è rigido:** si può scrivere all'assistenza (live chat o email) e **chiedere un
piano su misura** — più minuti, o un abbonamento dedicato. Nel corso: «ad alcuni clienti hanno
risposto in maniera positiva, ad altri no».

**Perché sta scritto qui:** il monte minuti è **il vincolo fisico della capacità produttiva** di
questa fabbrica. Se un giorno il collo di bottiglia diventa «non possiamo generare abbastanza
video», la prima mossa non è tagliare la qualità: è **chiedere**.

## Setup (registrazione)
1. fliki.ai → "Get Started".
2. Registrati con **email valida** (arriva mail di conferma) o Google/Facebook.
3. Conferma l'email (controlla spam se non arriva).
4. Dashboard: progetti recenti · "Create New Project" · menù a sinistra.

## Creazione video (pipeline)
1. **Nuovo progetto**: nome + **formato** — 16:9 YouTube · 1:1 Instagram · 9:16 short/TikTok.
2. **Contenuti**: carica testo/documento/audio → Fliki converte in video con immagini/clip pertinenti
   (oppure scegli dall'archivio Fliki).
3. **Personalizzazione**:
   - **Musica** di sottofondo a tono, **volume sotto la voce**.
   - **Testi/titoli/sottotitoli** (rende il video accessibile e coinvolgente).
   - **Durata scene** regolata per uno scorrimento fluido.
4. **Voce narrante**: scegli voce/lingua/accento (usa l'anteprima), incolla lo script → Fliki
   sincronizza voce↔immagini. Rivedi il testo (grammatica/sintassi).
5. **Modifica avanzata**:
   - **Transizioni** tra scene, con cura (influenzano la qualità percepita).
   - **Bilancia i volumi** (musica sotto la narrazione).
   - **Anteprima obbligatoria** prima di esportare (non saltarla mai).
6. **Export**: risoluzione **≥1080p** per YouTube · formato **MP4** (più versatile) · "Export" →
   rendering (**non chiudere il browser** durante l'export).

## Upload + ottimizzazione su YouTube (aggancio a WF4)
- YouTube Studio → "Carica video" → seleziona l'MP4.
- Titolo + descrizione (prime 2 righe decisive) + tag + miniatura + sottotitoli → vedi
  `references/seo-certificazione.md`.
- **Pubblica o programma** (programma in orario di massimo traffico → più views iniziali).
- Poi: **analizza e ottimizza** (WF5) — il successo è un processo continuo.

## Checklist produzione (per video-producer)
- [ ] Formato corretto per la piattaforma
- [ ] Voce scelta con anteprima, tono coerente col canale
- [ ] Musica a tono, sotto la voce
- [ ] Scene mappate dallo script, durate fluide, transizioni curate
- [ ] Sottotitoli ON
- [ ] Anteprima fatta prima dell'export
- [ ] Export ≥1080p MP4, browser non chiuso durante il rendering

---

## ⚠️ DUE COSE IMPARATE DALL'AGGIORNAMENTO DI LUGLIO 2024 (A4-L20 · 2026-09-06)

### 3. Il piano base ha un tetto di **50 scene** per file

Oltre alla capacità in minuti (§2), Fliki ha un **secondo tetto, per file: 50 scene** sul piano
base [A4/L20, 66:59-67:23]. È un vincolo di forma, non di durata, e nessuno da noi lo aveva mai
nominato.

Il modo di aggirarlo mostrato nella lezione: **impacchettare molto testo in un'unica scena** e poi
frazionarlo con il **B-roll**, che crea media temporizzati **dentro** la scena senza contarli come
scene nuove — nell'esempio, **40 immagini in una scena sola** [67:29-67:53]. (Sulla capacità di
caratteri per scena la lezione si contraddice: «mille» a 65:29 e «10.000» a 67:41. Non normalizzato:
va misurato, non creduto.)

**Verifica assegnata al gate A4:** questo tetto vale anche per i file creati **via API**, o è un
conteggio dell'editor web? La risposta cambia il numero massimo di scene che la fabbrica può
generare per video, e va saputa **prima** di alzare i volumi di produzione.

### 4. La difesa dai reclami: il «trafiletto» del corso, e la nostra

La lezione dichiara che le tracce musicali di libreria di Fliki sono «tutte licenziate»
[06:06-06:20], e che in caso di reclamo su YouTube «noi abbiamo una frase, **un trafiletto** che
andiamo a incollare nella disputa e YouTube risolve subito la questione» [06:20-06:39].

**Due osservazioni, e la seconda è quella che conta.**

1. Quel trafiletto **non lo fornisce Fliki**: è un testo che passa la community del corso
   [06:39-06:48]. È quindi **un processo umano di supporto**, non una funzione della piattaforma:
   dipende da qualcuno che risponde.
2. **Nei settantasei minuti dedicati a Fliki, il campo `YouTube channel ID(s)` non viene nominato
   una sola volta** — mentre è lo strumento **nativo della piattaforma** per lo stesso identico
   problema (§1 di questa scheda, `A4-L19-01`). Il corso insegna la difesa **dopo** il reclamo e
   ignora quella **prima**.

**La nostra difesa è nell'ordine opposto:** prima si registra l'ID del canale nel profilo Fliki
(gratis, una volta), e solo dopo, se il reclamo arriva lo stesso, si discute. Una disputa che si
apre con una casella già compilata non è la stessa disputa.
