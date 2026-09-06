# Reference — Produzione Avanzata su Fliki (SSML & Pronunce)

> Conoscenza on-demand per `video-producer` e `qa-audio-video`.
> Obiettivo: Ottimizzare l'espressività vocale dei render AI, correggere le pronunce errate ed evitare un feeling robotico.

> ## ⚠️ COSA DI QUESTA SCHEDA È RAGGIUNGIBILE **VIA API** — E COSA NO (A4-L04-03 · 2026-09-05)
>
> Verificato sul payload reale di `fliki_client.py` il 2026-09-05:
>
> | Leva | Dov'è in Fliki | La nostra catena |
> |---|---|---|
> | **Pause** (`Add pause`, 0,2 s fra parole · 1-3 s a fine clip) | menu contestuale sul testo selezionato | ❌ **non via API** — si ottiene solo con la punteggiatura nel testo |
> | **Velocità / intonazione** (`Tune → Rate`) | menu contestuale sul testo selezionato | ❌ **non via API** — nessun campo nel payload |
> | **Mappa delle pronunce** | `More → Pronunciation map` | ❌ **non via API** — si corregge **riscrivendo la parola nello script** |
> | **Musica di sottofondo e volume** | `More → Background music` | ❌ **non via API** — nessun campo `backgroundMusic`/`musicId`/`audioTrack` nel payload |
> | **Sottotitoli** (preset, karaoke) | Settings | ✅ `subtitlePresetId` + `highlightSubtitles` |
> | **Movimento delle scene** | Ken Burns / zoom | ✅ meglio: `aiVideoModel` + `aiVideoClipPercentage=100` |
>
> **Conseguenza operativa:** le tre voci della checklist §3 su velocità, pause e volume musica
> **non sono eseguibili dalla nostra catena**. Restano qui come conoscenza dello strumento, non
> come ordini. L'unica leva che ci resta davvero sul parlato è **il testo che mandiamo**: grafia
> delle parole (`references/lessico-pronuncia.md`) e punteggiatura.

---

## 1. Gestione delle Pause e dell'Intonazione (SSML)
Su Fliki, l'intonazione e la cadenza del parlato influenzano drasticamente la ritenzione dello spettatore ( retention rate). Utilizza queste tecniche nello script per forzare una narrazione umana:

* **Pause Silenziose (Break):** Per inserire una pausa respiratoria o un cambio di scena logico, inserisci il marcatore di pausa. Fliki permette di aggiungere pause (in secondi) tra le frasi o all'interno di una casella di testo.
  * *Consigliato:* `[pause: 0.5s]` dopo concetti complessi o prima di rivelare una risposta (curiosità).
* **Enfasi:** Per caricare di importanza una parola chiave target nel parlato, racchiudila o modificala per forzare l'accento naturale della voce AI.
* **Velocità di Narrazione (Pace):** Imposta la velocità della voce narrante al 95% o 90% se lo speaker AI tende a correre troppo o a mangiare le parole. Una narrazione leggermente più calma aumenta la percezione di autorevolezza del canale.

---

## 2. Dizionario delle Pronunce (Pronunciation Override)
Le voci sintetiche sbagliano spesso i termini inglesi inseriti in un contesto italiano (es. *"YouTube"*, *"Cash Cow"*, *"Automation"*, *"View"*) o nomi di brand specifici.

* **Regola di trascrizione fonetica:** Se una parola viene pronunciata in modo errato:
  1. Vai alla sezione **Pronunciation** (Dizionario) all'interno delle impostazioni vocali del progetto Fliki.
  2. Aggiungi la parola originale (es. `YouTube`).
  3. Specifica la trascrizione fonetica semplificata per ingannare la voce AI (es. `Iutub` o `Iutjiub`).
* **Trascrizioni comuni consigliate per l'italiano:**
  * `Cash Cow` ➔ `Cescau`
  * `VPH (Views Per Hour)` ➔ `Viu per ora`
  * `SEO` ➔ `Seo` (pronunciato all'italiana) o `Esse-E-O` (se si preferisce lo spelling)
  * `Automation` ➔ `Automescion`
  * `Fliki` ➔ `Flichi`

---

## 3. Checklist per l'Esportazione e Controllo Voce
- [ ] La velocità della voce narrante è impostata in modo confortevole (tra 0.9x e 1.0x)?
- [ ] Sono state inserite pause di almeno 0.5 secondi dopo ogni punto fermo o cambio di scena?
- [ ] Le parole straniere o tecniche sono state verificate nell'anteprima audio e corrette nel dizionario pronunce se storpiate?
- [ ] Il volume della traccia musicale è impostato al 10% - 15% rispetto alla voce (100%) per non sovrastare il parlato?

> **Da dove viene il 10% (A4-L19-03 · 2026-09-06).** Fino a oggi quel numero era una
> prescrizione senza fonte. Ora ha una prova: nel pannello `More → Background music` di Fliki
> lo slider del volume è una **percentuale**, e il valore mostrato a schermo nella lezione
> A4/L19 è **10%** (`frame-088.png @ 05:52`). La nostra prescrizione era già giusta: adesso si
> sa perché. **Resta non eseguibile via API** (vedi la tabella in testa): è conoscenza dello
> strumento, non un ordine alla catena.

---

## 4. Riconciliazione del volume della musica, e una funzione nuova (A4-L20-02/05 · 2026-09-06)

### Il numero: 10%, 15%, 5% — non si contraddicono

Abbiamo tre cifre da due lezioni diverse, e vanno lette per quello che sono:

| cifra | da dove | cos'è davvero |
|---|---|---|
| **10%** | A4/L19, **visto a schermo** (`frame-088.png @ 05:52`) | il valore che lo slider **mostrava** in quel progetto: un default, non una prescrizione |
| **15%** | A4/L20, parlato @ 07:13-07:25 | il **massimo** che il relatore applica normalmente |
| **5%** | A4/L20, parlato @ 07:39-07:48 | il valore che chiama **«gradevole»**, cioè il suo tipico |

**Quindi la banda è 5-15%, con il tipico in basso**, e la nostra vecchia prescrizione «10-15%»
aveva **il pavimento troppo alto**. Il relatore aggiunge la condizione che conta più dei numeri
[07:25-07:39]: dipende **dalla traccia, dal narratore e dal volume del narratore** — cioè si
regola ascoltando, esattamente come dice il metro dei −35 dB in `qa-audio-video.md` §9.

**Nota che evita fraintendimenti:** oggi tutto questo è **teoria dello strumento**. I nostri video
**non hanno musica** (accertato: `qa-audio-video.md` §10). Serve il giorno in cui ce la metteremo.

### Generazione di effetti sonori da prompt (`Add Layer → Audio → Generate`)

Fliki genera un **effetto sonoro** da una descrizione testuale — nella lezione, il ruggito di un
leone — e lo si posiziona al secondo esatto col pannello `Timing` [A4/L20, 44:53-46:56]. È la
funzione dell'aggiornamento con **più probabilità di esistere anche via API**, ed è fra le tre
verifiche assegnate al gate A4.

⚠️ **Un vuoto da tenere presente:** delle tracce musicali di libreria il corso dice che sono
«tutte licenziate» [06:06-06:20]; **sugli effetti sonori generati dall'AI non dice nulla.** Prima
di metterne uno in un video pubblicato, il titolo d'uso si legge nei termini di Fliki — non si
assume per analogia con la musica (stessa regola del §9 di `monetizzazione-compliance.md`).
