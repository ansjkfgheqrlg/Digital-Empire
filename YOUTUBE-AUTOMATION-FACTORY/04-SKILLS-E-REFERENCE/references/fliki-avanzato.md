# Reference — Produzione Avanzata su Fliki (SSML & Pronunce)

> Conoscenza on-demand per `video-producer` e `qa-audio-video`.
> Obiettivo: Ottimizzare l'espressività vocale dei render AI, correggere le pronunce errate ed evitare un feeling robotico.

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
