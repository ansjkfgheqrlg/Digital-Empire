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
