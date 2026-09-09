# EMP-LAN1 — ANATOMIA DEI LANCI: restano la forma Python e il PDF

- **Aperto:** 2026-09-09
- **Stato:** APERTA
- **Come si riprende:** basta dire `EMP-LAN1` in una chat nuova dentro Digital Empire.
- **Checkpoint di origine:** [CP-20260909-J2TJ](../checkpoints/CP-20260909-J2TJ.md)
- **Checkpoint precedente (studio chiuso):** [CP-20260909-GRVC](../checkpoints/CP-20260909-GRVC.md)

---

## LA PRIMA COSA DA FARE ALLA RIPRESA

**Misurare sul disco. Non fidarsi di questa riga — vale anche per lei.**

```
python "competitor/Andrei Pascu/site-study/scripts/stato_onde.py"
ls "competitor/Andrei Pascu/"
ls "documentazione Empire/Lanci/"
```

Atteso: `stato_onde.py` deve dire **56 su 56, tutte e sette le onde chiuse**.

---

## DOVE SIAMO

### ✅ FATTO — lo studio dei siti è chiuso

**56 su 56.** 52 pagine catturate su 7 domini, ~50 rapporti, oltre 100.000 parole, tre sintesi
(`SINTESI-METODO.md`, `SINTESI-SISTEMA-VISIVO.md`, `SINTESI-SISTEMA-COPY.md`), fusione di
`empire-premium-style` nella Fabbrica eseguita. Tutto in `CP-20260909-GRVC`.

### ✅ FATTO — la prima delle tre forme del documento sui lanci

`competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md` — **committato**. Dieci parti: il lancio vivo
catturato, le sei mosse con cui costruisce un lancio, il funnel gradino per gradino, l'offerta, le
otto costanti dei suoi lanci, come ragiona, cosa non fa mai, i sette difetti (sei diventati nostri
controlli), il modello in dodici passi per Digital Empire, e cosa consegniamo a LANCI.

### ⬜ RESTA DA FARE — due forme su tre

Ordine di Max: *«un documento dovrà avere la sua forma originale in Markdown, poi una forma in
Python e poi quella documentata più bella esteticamente, che è quella in PDF.»*

1. **`competitor/Andrei Pascu/anatomia_lanci.py`** — i dati del lancio in struttura interrogabile
   (fasi, gradini del funnel, stampo della pre-cassa a sei variabili, leve dell'offerta, gli otto
   controlli di gate, i dodici passi del modello) **+ il generatore del PDF**. Chi costruisce LANCI
   deve poterci chiamare dentro invece di rileggere una prosa.
2. **Il PDF** — motore obbligatorio `PIANO-MAESTRO/scripts/pdf_engine_empire.py` (standard-oro
   dossier 28, `emperator.md` §6.19). Interfaccia già letta:
   ```python
   from pdf_engine_empire import PDFDoc
   doc = PDFDoc(title=..., doc_label=..., footer_left=..., out_html=..., out_pdf=...)
   doc.page(doc.head("A", "Eyebrow", "Titolo", "Lead.") + PDFDoc.tab(cols, rows, cap))
   doc.build()
   ```
   Metodi disponibili: `page()`, `head()`, `tab()`, `figure()`, `render_html()`, `build()`.
   Stile già deciso, **non si ridiscute**: fondo chiaro + grana leggera, copertina scura, UN heading
   per pagina, `#fb4604` sotto il 10% dell'area, **nessuna linea o bordo**, grana PNG mai SVG.
3. **Doppione obbligatorio** del PDF in `documentazione Empire/Lanci/` (legge `emperator.md` §6.17).
4. **La consegna** — spuntare `company/Memory/tasks/TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md`.
   **È "fatta" solo quando la sessione LANCI l'ha ricevuta e può usarla** (ADR-016, l'Ultimo Metro),
   non quando il PDF esiste.

---

## I NUMERI DA NON RICALCOLARE — sono già misurati

| Cosa | Misura |
|---|---|
| Il pacchetto Armageddon | 585 € listino + 199 € voucher = 784 €, venduti a **199 €** |
| Le pagine del lancio | 1 madre (5.103 px) + 4 figlie, **un solo link Stripe** |
| Il funnel freddo | `/define` → `/asa` → `/copy-base`, **86 parole** dall'apertura al clic |
| Lo stampo di pre-cassa | 9 pagine, cornice identica al pixel, **sei variabili** |
| Il codice sconto | «CWSHOP» 20%, pubblico e permanente: il listino vero è **78,40 €** |
| La tipografia dell'offerta | «Risparmi €585» a **81,6 px**, prezzo pagato a **14,88 px** |
| La scala dei prezzi | 98 → 400 → 999 €: fonti esterne 0 → 2 → 5, prova sociale solo sopra 349 € |
| Il difetto più costoso | `/vendita` → `/acquista-v101` = **404**, cassa vera orfana di link |

---

## TRAPPOLE GIÀ PAGATE

- **Gli scagnozzi cadono per infrastruttura** (server, stallo, OAuth): oggi cinque volte. Nel prompt
  va sempre l'ordine **«scrivi presto e salva, poi arricchisci»** e un limite duro di letture.
- **Mai più di 2-3 scagnozzi in parallelo**: il limite di sessione è stato colpito una volta oggi.
- **Il CRLF su `EMP-W4K7.md`** blocca i commit (B-059): la fonte è un'altra sessione viva.
  Si sblocca con `python .githooks/check_memory.py --fix`. Successo **quattro volte** in due giorni.
- **Un numero prodotto da una macchina non è un fatto** finché non si guarda *cosa* ha contato: due
  dei miei strumenti hanno mentito oggi, entrambi corretti alla fonte.
- **La console è cp1252**: niente emoji negli script Python.

---

## I FILE DA RIAPRIRE

| File | Cosa |
|---|---|
| `competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md` | **la fonte**: le altre due forme nascono da qui |
| `PIANO-MAESTRO/scripts/pdf_engine_empire.py` | il motore PDF, standard-oro |
| `PIANO-MAESTRO/scripts/build_dossier28_pdf.py` | l'esempio d'uso già funzionante |
| `company/Memory/tasks/TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md` | la consegna e le spunte |
| `PIANO-MAESTRO/33-...ANDREI-PASCU.md` PARTE VI | il perimetro del secondo scopo |
| `competitor/Andrei Pascu/site-study/SINTESI-*.md` | le tre sintesi, materiale per il PDF |
