# Reference — Policy YouTube per canali Automation

> Checklist operativa, **non parere legale**. Per diffide, strike ripetuti o uso di identità reali:
> serve un avvocato. Le policy YouTube cambiano: questa è la struttura del rischio, non un testo
> normativo da citare.

---

## 1. Contenuto riutilizzato (il rischio n°1 per l'automation)

YouTube monetizza contenuto **originale o significativamente trasformato**. Il "contenuto
riutilizzato" è la causa più comune di **rifiuto della monetizzazione** per i canali automation.

**Cosa viene considerato riutilizzato:**
- Re-upload di video altrui (anche con lievi modifiche).
- Contenuto di terzi con **solo** una voce fuori campo sopra.
- Compilation senza apporto narrativo.
- Traduzione dell'audio mantenendo il video originale.

**Cosa rende trasformativo:**
- Script **riscritto** con angolo proprio, esempi e contesto aggiunti.
- **Voce nuova** (sintetica di libreria o propria).
- **Materiale visivo proprio o d'archivio con licenza** — mai i frame dell'originale.
- **Struttura ripensata** (hook, ordine, CTA).
- **Valore aggiunto** verificabile (dati, commento, confronto).

→ Misurato da `scripts/originality_score.py`. Soglia di pubblicazione: **≥70**.

> **Il caso cross-lingua.** Replicare un format che funziona in un'altra lingua è pratica comune e
> accettabile: quello che riusi è **l'idea e il formato**, non i file. Se rifai script, voce e
> visivo, sei trasformativo. Se scarichi il video e ci metti la voce italiana sopra, non lo sei.

---

## 2. Copyright e Content ID

- **Content ID è automatico**: la musica commerciale viene riconosciuta dal sistema, non "se ti
  beccano". Esito: rivendicazione (i ricavi vanno al titolare) o blocco del video.
- **Musica sicura**: libreria Fliki, YouTube Audio Library, tracce con licenza acquistata.
- **Immagini/clip sicure**: archivio con licenza (incluso quello di Fliki), materiale proprio.
- **Mai**: frame di film/TV, spezzoni di altri video YouTube, immagini da ricerca web.
- **Fair use / citazione**: esiste ma è una **difesa**, non un permesso — e si valuta caso per caso
  in giudizio. Non è una strategia su cui costruire un canale.

**Strike vs rivendicazione:**
| | Rivendicazione (Content ID) | Strike (rimozione per copyright) |
|---|---|---|
| Effetto | ricavi al titolare / blocco | avvertimento formale sul canale |
| Accumulo | non chiude il canale | **3 strike = canale chiuso** |

---

## 3. Nicchie sensibili

| Nicchia | Requisiti extra |
|---|---|
| **Salute/medicina** | fonti; disclaimer "non sostituisce il parere medico"; niente cure miracolose |
| **Finanza/investimenti** | disclaimer "non è consulenza finanziaria"; niente promesse di rendimento |
| **Esoterismo/rituali** | disclaimer "a scopo di intrattenimento"; nessuna promessa di risultati; nessuna pratica dannosa |
| **Notizie/attualità** | accuratezza e fonti; la disinformazione dannosa è rimossa |
| **Contenuti per bambini** | dichiarazione obbligatoria "fatto per bambini" (COPPA); commenti disattivati; monetizzazione ridotta |
| **Violenza/sesso** | non adatto agli inserzionisti: da evitare in automation |

---

## 4. Monetizzazione (YPP) — requisiti di accesso

Requisiti storicamente richiesti per il Programma Partner (verifica sempre i valori correnti):
- **1.000 iscritti** +
- **4.000 ore di visualizzazione** negli ultimi 12 mesi **oppure** 10M di visualizzazioni di Short
  negli ultimi 90 giorni;
- rispetto delle policy, nessuno strike attivo, AdSense collegato, 2FA attiva.

**Adatto agli inserzionisti** (icona verde/gialla): linguaggio forte, temi controversi, tragedie e
contenuti scioccanti riducono o azzerano i ricavi pubblicitari anche su video conformi.

---

## 5. Clickbait e coerenza

Titolo e miniatura **devono corrispondere** al contenuto. Non è solo policy: è economia del canale.
Un titolo falso alza il CTR e **distrugge la retention** → l'algoritmo smette di mostrarlo. Il
`policy-checker` verifica la coerenza, il `ctr-analyst` (thumbnail-lab) verifica l'effetto.

---

## 6. Regola d'oro operativa

> **Copi l'idea. Non copi mai un file.**
> Se un asset del tuo video potrebbe essere scaricato dal video originale, va sostituito.

## Connessioni
- [[originality-auditor]] — misura la trasformazione
- [[copyright-scanner]] — inventario provenienza asset
- [[policy-checker]] — nicchie sensibili e monetizzazione
- [[compliance-gate]] — verdetto bloccante
