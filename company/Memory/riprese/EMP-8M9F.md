# EMP-8M9F — Libro dell'Agency, Edizione Integrale (700+ pagine, 2.128 atomi)

- **Codice di ripresa:** `EMP-8M9F`
- **Aperto:** 2026-09-10
- **Stato:** APERTO — Fase 0 non ancora iniziata, si aspetta il via di Max
- **Chi riprende:** basta dire `EMP-8M9F` in una chat nuova dentro Digital Empire.
- **Predecessore:** `EMP-W4K7` (chiuso 2026-09-10) — ha prodotto la **prima edizione bocciata**.

---

## 1. IL LAVORO IN UNA FRASE

Ricostruire da zero **Il Libro dell'Agency** secondo il piano V4 in
`PIANO-MAESTRO/35-PIANO-LIBRO-AGENCY-V2.md`: otto Libri, **almeno 700 pagine**, **tutti e 2.128
gli atomi di conoscenza** dell'Impero coperti al 100%, motore PDF in flusso continuo, e un gate
meccanico che rifiuta i capitoli magri prima che arrivino a Max.

---

## 2. PERCHE' ESISTE QUESTA MISSIONE — la bocciatura, testuale

Max, 2026-09-10, sulla prima edizione (`34-LIBRO-AGENCY.pdf`, 11 pagine):

> *"È veramente schifoso a livello di contenuti [...] ti ho detto chiaramente che deve esserci
> tutta la formazione acquisita, tutta la conoscenza, tutto su ogni argomento. Può essere enorme,
> questo libro deve essere una risorsa enorme. Devi rivedere completamente il modo in cui
> strutturi e inserisci il contenuto nella documentazione. Il PDF deve raggiungere minimo 100
> pagine, ma questo come minimo."*

**Estetica e design: APPROVATI da Max, non si toccano.** Il CSS standard-oro resta identico.
Il difetto era tutto e solo nel contenuto.

---

## 3. I NUMERI VERI — contati sul disco il 2026-09-10, non stimati

| Giacimento | Misura |
|---|---|
| Atomi di conoscenza (`atoms.json`, 24 run) | **2.128 KA** |
| Contenuto integrale (`memory-empire/knowledge/`, 78 cartelle) | **753.606 parole** |
| Pagine wiki fonte (73) | **79.737 parole** |
| Studio competitor Andrei Pascu (130 file) | **413.292 parole** |
| Skill di dominio CRO/agency (8 skill) | **254.732 parole** |
| **Totale disponibile** | **≈ 1.500.000 parole** |
| Prima edizione consegnata | 14.000 parole = **1,8% del materiale** |

**I dieci run più ricchi** (qui sta la conoscenza densa): v09 NmoOZVTrTXA 323 · v08 DI5aWJiFAt8 229 ·
v06 JTn5pqm9ecM 228 · v01 RnoC5IlOUhs 205 · doc justin-sung 88 · v04 140FuW7b9pk 78 ·
max17-v02 beggiato-team 77 · v05 RnNSRF4s9nk 72 · max17-v07 rizzo-prompt 71 ·
max17-v05 jaye-agenticos 70.

---

## 4. IL MOTORE — già provato, non da ipotizzare

Test reale girato il 2026-09-10 (`scratchpad/test_flusso.py`, perso alla chiusura chat ma la
logica è tutta qui sotto): CSS standard-oro applicato a **flusso continuo** invece che a pagine
ad altezza fissa.

| Misura | Risultato |
|---|---|
| 7.920 parole → | **13 pagine** |
| Parole per pagina (testo denso puro) | **609** |
| Parole per pagina (con titoli/tabelle/citazioni) | **≈ 420-450** |
| Peso | **12,4 KB/pagina** → 700 pagine ≈ 8,7 MB |
| Grana | incorporata **1 volta sola**, riusata su tutte le pagine |
| Font | 3 incorporati (Onest + IBM Plex Mono) |
| Header/footer per pagina | sì, via `display_header_footer` di Playwright |

**Come si costruisce** (ricetta verificata):
- Riusare `CSS_TEMPLATE` e `grain_data_uri()` da `PIANO-MAESTRO/scripts/pdf_engine_empire.py`.
- Aggiungere: `@page { size:A4; margin:24mm 20mm 20mm 20mm; }`, la grana su
  `body::before { position:fixed; inset:0; z-index:0 }` (Chromium la replica su ogni pagina),
  e un contenitore `.flow { position:relative; z-index:1 }`.
- Chiamare `page.pdf(..., display_header_footer=True, header_template=..., footer_template=...)`
  con `margin` passato a Playwright (NON `prefer_css_page_size`), e nel footer
  `<span class='pageNumber'>` per la numerazione automatica.
- **Trappola:** il motore vecchio ha `.page { height:297mm; overflow:hidden }` — qualunque
  contenuto in eccesso viene **tagliato in silenzio**. Per il libro NON si usa quel contenitore
  se non per copertine e aperture di Libro (dove il taglio non può avvenire).

---

## 5. I CINQUE ERRORI CHE HANNO PRODOTTO LA PRIMA EDIZIONE — non rifarli

1. **Nessun gate.** Come il battito prima di `verifica_recap.py`: senza una macchina che
   rifiuta, la versione corta passa sempre perché costa meno a chi scrive. **È l'errore madre.**
2. **Target di lunghezza invece che di copertura.** Nei prompt agli scagnozzi c'era
   *"orientativamente 250-450 righe"*: l'agente aveva materiale per 2.000 righe, ha letto 450 e
   ha tagliato. **Mai più un range di righe: si dà la lista di atomi da coprire.**
3. **Doppia compressione.** Agli agenti erano state date solo le pagine wiki (livello L4, già
   sintesi) invece del contenuto integrale (L2) e degli atomi (L3). Riassumere una sintesi
   produce la sintesi della sintesi.
4. **Formato scelto prima del contenuto.** Il motore dei dossier da 10 pagine ha deciso quanto
   contenuto poteva esistere.
5. **Perimetro ristretto con una scusa metodologica.** 7 fonti su 73, "solo quelle taggate
   agenzia" — comodità travestita da criterio, e scritta nel libro come se fosse un pregio.

---

## 6. IL PIANO — dove sta, cosa dice

**`PIANO-MAESTRO/35-PIANO-LIBRO-AGENCY-V2.md`** — piano V4, dopo tre giri di critica (P1, P2, P3
tutti scritti dentro). **Leggerlo per intero prima di iniziare.** In sintesi:

### Gli otto Libri (tassonomia già fissata, §8.2 del piano)

| # | Libro | Atomi stimati |
|---|---|---|
| I | Il Metodo Digital Empire (materiale interno: 9 skill + BACKBONE reparti + ADR) | interni |
| II | Trovare clienti (ICP, outreach, LinkedIn, SEO, lead gen, caroselli) | ~280 |
| III | Vendere e prezzare (call, diagnosi, preventivi, obiezioni, retainer) | ~260 |
| IV | Consegnare e scalare (fulfillment, team, hiring, qualità, handover) | ~230 |
| V | Costruire con l'AI (agenti, Claude Code, Cowork, voce, token, orchestrazione) | ~1.100 |
| VI | Contenuto, brand, lanci (copy, funnel, storytelling, personal brand) | ~200 |
| VII | Imparare e decidere (apprendimento, mindset, numeri) | ~180 |
| VIII | Apparati (indice analitico, fonti, tutti i 2.128 atomi, glossario) | — |

### Le quattro fasi

- **FASE 0 — Indicizzazione (blocca tutto):** `indicizza_atomi.py` estrae i 2.128 atomi in
  `atomi-index.json`; poi 24 agenti (uno per run, a ondate da 6) assegnano a ogni atomo
  **Libro + capitolo + peso** (portante ≥150 parole nel corpo / supporto = citazione nel flusso /
  contesto = riga in appendice) scegliendo SOLO dalla tassonomia sopra; poi `dedup_atomi.py`
  unisce gli atomi che dicono la stessa cosa da fonti diverse. **Uscita: zero atomi orfani.**
- **FASE 1 — Motore:** `pdf_engine_libro.py` + test di tenuta su 200 pagine finte.
- **FASE 2 — Scrittura, otto ondate:** un agente per capitolo, riceve gli atomi assegnati con
  l'ancora verbatim + i puntatori ai `contenuto-integrale.md`, **nessun target di lunghezza**.
  Ogni capitolo chiude col blocco dichiarato *"Cosa fa Digital Empire su questo punto"*.
  PDF rigenerato ad ogni ondata: il libro cresce e si vede crescere.
- **FASE 3 — Apparati:** i quattro indici generati da codice, vaglio pubblico, doppione.

### Il gate — `scripts/gate_densita_libro.py` (da costruire, è il pezzo che mancava)

Rifiuta un capitolo se: copertura atomi < 100% · parole per atomo portante < 150 · ancora
verbatim presente in < 90% degli atomi portanti · manca il blocco "Cosa fa DE" · marker NO-STUB.
Stampa l'elenco esatto dei KA mancanti, così chi riscrive sa cosa aggiungere.

### Criterio di "finito", verificabile da macchina (§8.5)

2.128/2.128 atomi mappati · gate passa su tutti i capitoli · PDF ≥ 700 pagine · quattro indici
generati e risolti · vaglio pubblico passato · doppione esistente.

### Costo dichiarato

~30 run di agente, **≈ 6 milioni di token**, 8-10 ondate su più sessioni.

---

## 7. IDENTITA' DEL PRODOTTO

| Voce | Valore |
|---|---|
| Titolo | Il Libro dell'Agency — Edizione Integrale |
| Sorgente | `PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE.md` (da creare) |
| Motore | `PIANO-MAESTRO/scripts/pdf_engine_libro.py` (da creare) |
| Costruttore | `PIANO-MAESTRO/scripts/build_libro_integrale_pdf.py` (da creare) |
| PDF | `PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE.pdf` + doppione in `documentazione Empire/Piani/Agency/` |
| Prima edizione | `34-LIBRO-AGENCY.*` — **resta archiviata, non si cancella** (termine di paragone) |
| Bersaglio | ≥ 700 pagine, 2.128/2.128 atomi |
| Pavimento | 100 pagine (sotto: respinto in partenza) |

---

## 8. PROSSIMO PASSO ESATTO

1. **Chiedere/attendere il via di Max** sul piano (era in attesa di approvazione al momento del
   checkpoint).
2. Al via: **Fase 0**, che comincia con `scripts/indicizza_atomi.py` — nessun capitolo si scrive
   prima che `atomi-index.json` esista completo.
3. Regola di condotta per tutta la missione: **mai dare a un agente un target di righe**, sempre
   una lista di atomi da coprire e una soglia di parole per atomo.

---

## 9. TRAPPOLE

- **`overflow:hidden` del motore vecchio taglia in silenzio.** Mai usarlo per il corpo del libro.
- **Il peso:** 700 pagine ≈ 8,7 MB, sopra la soglia di attenzione di 8 MB del motore. Rimedio già
  deciso: grana rigenerata a `size=90`; se sfora 12 MB, consegna in due tomi con numerazione continua.
- **La console Windows è cp1252:** niente emoji negli `print` degli script, o crashano.
- **Il formato del battito è cambiato due volte in due giorni** (🟠 → 🟩): prima di consegnare un
  battito si rilegge `scripts/verifica_recap.py`, che è l'unica fonte di verità, e si genera con
  `costruisci(...)`. Il battito va **in cima al messaggio**, mai dopo l'analisi (il gate blocca).
- **Altre sessioni scrivono sullo stesso repo:** `git status` prima di committare, e `STATO-EMPIRE.md`
  può cambiare sotto i piedi fra una lettura e l'altra.

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-8M9F`*
