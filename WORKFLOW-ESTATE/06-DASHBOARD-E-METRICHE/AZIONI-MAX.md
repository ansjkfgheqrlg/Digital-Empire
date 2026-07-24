---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/PIANO-COMPLETAMENTO-L3.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# 🔵 AZIONI MAX — cosa resta, e solo tu puoi farlo
> Generato dal completamento del Workflow Estate · 2026-07-24 · verdetto: `python -m empire estate`

La costruzione è chiusa: **11 controlli su 13 passano**. I 2 che restano non sono lavoro
mancante, sono atti che richiedono te — un account, una credenziale, una telefonata, un incasso.
Sotto trovi **cosa fare, dove, e cosa si sblocca**. In ordine di soldi.

---

## 🥇 1. Due Payment Link Stripe → il Manuale inizia a incassare
**Tempo: 10 minuti. È la cosa a più alto ritorno di questa lista.**

Oggi la landing del Manuale funziona ed è al **tier 2**: chi vuole comprare apre
`pagamento.html` e manda un ordine via mail a te, poi tu gli mandi le coordinate a mano.
Funziona, ma perdi le vendite di chi non ha voglia di scrivere una mail.

**Cosa fare:**
1. Su Stripe crea 2 Payment Link: uno da **€67** (Manuale) e uno da **€94** (Manuale + pack template €27).
2. Apri `Crea siti/Siti CCM/checkout.config.json` e incolla i due URL:
   ```json
   "stripe_base": { "url": "https://buy.stripe.com/...", "attivo": true },
   "stripe_bump": { "url": "https://buy.stripe.com/...", "attivo": true }
   ```
3. Lancia:
   ```
   python empire/tools/checkout.py --apply
   python empire/tools/checkout.py --check
   ```
   Deve stampare `tier 1`.

**Non toccare l'HTML a mano.** I link stanno in un solo file e lo script li propaga ovunque:
è così che si evita di ritrovarsi fra un mese con un `YOUR_STRIPE` dimenticato in pagina —
che è esattamente quello che è successo e ha tenuto il Gate-FUNNEL rosso per giorni.

---

## 🥈 2. Prezzo di Preventa (DEC-EST-005) → la landing va online
**Tempo: 2 minuti (è una decisione, non un lavoro).**

La landing Preventa è pronta: `Crea siti/Preventa/index.html`. Copy, palette, FAQ, obiezioni,
CTA funzionante, link al case study Novacar. **Manca solo il prezzo**, che è ancora sotto tuo
veto (M-EST-4, default proposto €490 setup / €149 canone).

Nella pagina, al posto della cifra, c'è un riquadro giallo evidente `MAX: prezzo — DEC-EST-005
sotto veto`. **Non ho inventato una cifra plausibile di proposito**: un prezzo sbagliato su una
pagina pubblica è peggio di un prezzo assente, perché lo leggono i concessionari a cui poi devi
chiedere altro.

**Cosa fare:** decidi il prezzo (o lascia scadere il veto), poi cerca nel file i riquadri
`todo` e sostituiscili. Stessa cosa per **P.IVA** e **telefono** nel footer, e per il link
**Calendly/WhatsApp** al posto del `mailto:` nella CTA demo.

---

## 🥉 3. Gate-CONTATTI — ⚠️ prima leggi questo, poi decidi
**Questo non è un adempimento: è un problema che ho trovato misurando.**

Il gate chiede 7 lead contattati su 7. Il file `lead.csv` dice esattamente 7/7. **Ma nessuno di
quei 7 nomi esiste in una sorgente a monte:**

```
python -m empire flow gate Gate-CONTATTI
-> tracciabilita' assente: solo 0/7 voci risultano in una sorgente
   a monte (Outreach/**/*.csv) - righe forse inserite a mano
```

Ho controllato tutti i CSV di `Outreach/`: contengono solo dati di prova dichiarati
(`test_lead_finti.csv` con "Autosalone Test Uno" e "Via Finta 1", `esempio_lead_5_righe.csv`,
`stato_lead_test.csv`). **I 61 lead reali dichiarati in STATO-EMPIRE il 23/07 non esistono come
file su disco.** O lo scraping non è stato salvato, o è stato salvato altrove e va recuperato.

**Cosa fare (una delle due):**
- **(a)** Se i 7 concessionari sono contatti veri tuoi: aggiungi la sorgente da cui vengono
  (export, rubrica, CSV) sotto `Outreach/`, poi conferma il gate:
  ```
  python -m empire flow gate Gate-CONTATTI --confirm --actor Max --evidence "..."
  ```
- **(b)** Se erano dati di esempio: rilancia lo scraper (`Outreach/preventa-maps-scraper/`) con
  le province vere (M-EST-9 è ancora aperta) e riparti da lead reali.

**Non ho confermato io questo gate, e non potevo:** l'ho lasciato rosso apposta. Un 7/7 su nomi
non tracciabili avrebbe fatto sembrare fatto un lavoro commerciale mai avvenuto.

---

## 4. Gate-REV — l'unico che nessun software può chiudere
`anticipi_chiusi = 0`. Si chiude quando incassi. La macchina intorno è pronta: offerta,
script WhatsApp, argomentario obiezioni, follow-up G+2/G+5, case study, landing, checkout.

---

## 5. Canale YouTube + credenziali (M-EST-8) → S5 pubblica
Il pacchetto video è completo e validato:
`WORKFLOW-ESTATE/07-VIDEO-RUN/run-2026-07-23-001/` (scelta, script IT a scene, testo TTS,
shotlist, SEO pack con link al Manuale).

**Non esiste un file video, e il pacchetto lo dichiara apertamente** (`05-STATO.md`).
Verificato con comandi veri: `FLIKI_API_KEY` è **vuota** nel `.env` (gradino 1 della ladder
morto), `ffmpeg` **c'è** (8.1.1), mancano audio narrato e registrazione schermo.

**Cosa serve da te:** canale YouTube di destinazione + credenziali OAuth per l'upload
automatico, e una voce per il TTS (o la chiave Fliki, se la rinnovi).

---

## Come rileggere questo stato fra una settimana
```
python -m empire estate            # verdetto: cosa manca e di chi è
python -m empire estate --verbose  # con le evidenze sotto ogni voce
python -m empire flow gates        # i 6 gate con l'evidenza calcolata
python empire/tools/checkout.py --check   # tier di incasso attuale
```

⛓️ P12: `AZIONI-MAX#estate-2026` · prodotto dal LOTTO 6 · verdetto: `python -m empire estate`
