# EMP-APDOC1 — Documentazione ufficiale Andrei Pascu: 1 di 4 pezzi fatta

- **Aperto:** 2026-09-09
- **Stato:** APERTA
- **Come si riprende:** dire `EMP-APDOC1` in una chat nuova dentro Digital Empire.
- **Checkpoint di origine:** [CP-20260909-22YQ](../checkpoints/CP-20260909-22YQ.md)
- **Ordine di Max (testuale, 2026-09-09):** *"voglio un documento documentazione ufficiale per
  ogni corso di Andrei Pascu... deve esserci all'interno della documentazione una cartella
  competitor con dentro cartella Andrei Pascu con dentro i documenti su di lui. Inizia da
  outFunnel e poi Claude Speedrun — poi basta gli altri per ora hanno meno priorità. Poi voglio
  anche una documentazione ufficiale su Andrei Pascu... tutto un documento dove c'è tutto su di
  lui... Poi dobbiamo pensare a miglioramenti e implementazioni... voglio anche una
  documentazione un documento su tutto ciò che miglioriamo o implementiamo grazie allo studio su
  Andrei Pascu."*

---

## LA PRIMA COSA DA FARE ALLA RIPRESA

Misurare sul disco, non fidarsi di questa riga:
```
ls "competitor/Andrei Pascu/"
ls "documentazione Empire/competitor/Andrei Pascu/"
```

---

## I QUATTRO PEZZI ORDINATI DA MAX

### 1. Documentazione ufficiale per corso — outFunnel

**✅ FATTO, completo.** `competitor/Andrei Pascu/OUTFUNNEL-DOCUMENTAZIONE-UFFICIALE.md` + `.pdf`
(6 pagine, standard-oro) + doppione in `documentazione Empire/competitor/Andrei Pascu/`.

### 2. Documentazione ufficiale per corso — Claude Speedrun 2 (cs2online)

**⬜ MD scritto, PDF NON generato.** `competitor/Andrei Pascu/CLAUDE-SPEEDRUN-2-DOCUMENTAZIONE-UFFICIALE.md`
esiste, riflette lo stato reale **20/40 lezioni (50%)** — non è tutto il corso, è onesto su cosa
manca (sezione "RESTA DA FARE" nel documento).

**Resta da fare:**
- Generare il PDF (stesso motore di `build_outfunnel_pdf.py`, adattare a questo documento —
  6-7 pagine plausibili: copertina, cos'è, i due blocchi completi, scoperta+patch applicata,
  anomalie aperte, resta da fare).
- Copiare il doppione in `documentazione Empire/competitor/Andrei Pascu/`.
- **Non è richiesto** completare le 20 lezioni mancanti di cs2online per chiudere questo pezzo —
  Max ha chiesto la documentazione, non il completamento del corso. Se in futuro si completano
  altre lezioni, il documento va aggiornato (non riscritto da zero).

### 3. Documento-mondo — "tutto su Andrei Pascu"

**⬜ NON iniziato.** Deve unire: studio dei siti (56 pagine, `site-study/`, le tre SINTESI-*.md),
`ANATOMIA-DEI-LANCI.md`, `OUTFUNNEL-DOCUMENTAZIONE-UFFICIALE.md`,
`CLAUDE-SPEEDRUN-2-DOCUMENTAZIONE-UFFICIALE.md` — un profilo integrale (chi è, il suo metodo, il
suo sistema visivo, il suo sistema di copy, come lancia, cosa insegna vs cosa fa davvero — vedi
la scoperta della Lezione 13 di outFunnel, l'autore vende il controllo che lo avrebbe salvato dal
suo stesso difetto piu' costoso). **Non ri-derivare i contenuti: sintetizzare e linkare** le fonti
gia' scritte, che sono gia' >150.000 parole in totale — questo documento e' l'indice ragionato,
non un copia-incolla.

**Nome file pianificato:** `competitor/Andrei Pascu/ANDREI-PASCU-DOSSIER-COMPLETO.md` + PDF +
doppione.

### 4. Documento dei miglioramenti/implementazioni per Digital Empire

**⬜ NON iniziato.** Consolidare OGNI "Connessione con Knowledge Base esistente" gia' scritta nei
20 `lesson-analysis.md` di outFunnel, piu' quelle di outHeadline/cs2online quando pronte, piu' i
candidati gia' segnalati in `ANATOMIA-DEI-LANCI.md` — un elenco unico con colonna stato
(proposto/applicato), matching lo stile di `company/Memory/BACKLOG.md`. Include la **patch gia'
applicata per davvero**: `copywriting/SKILL.md` sezione "Customer Language Over Company Language"
(2026-08-29, da cs2online lezione 13 + 2 video YouTube gratuiti, convergenza a 3 fonti).

**Nome file pianificato:** `competitor/Andrei Pascu/MIGLIORAMENTI-DIGITAL-EMPIRE.md` — MD puro,
niente PDF (documento vivo che cresce, come BACKLOG.md, non un deliverable formale chiuso).

---

## LAVORO PARALLELO IN PAUSA (priorita' piu' bassa, dichiarata da Max)

**outHeadline** (secondo corso del bundle Armageddon, 30 lezioni) — cattura testo delle 30 lezioni
GIA' FATTA (`runs/andrei-pascu-armageddon-outheadline-001/lessons/lezione-01..30/_page_raw.txt`,
gia' salvata dal sync automatico). **Non ancora fatto**: classificazione teoria/pratica (la
Sezione 4 "Andrei scrive headlines", Lezione 28, 19:53, e' candidata forte a PRATICA vera — questo
corso di copywriting usa un player video DIVERSO da outFunnel/cs2online, niente iframe Vimeo
rilevato nella prima scansione, da investigare prima di classificare), `lesson-analysis.md`,
Memory Empire. **outEmail e outViral 2**: non iniziati.

Max ha detto esplicitamente che outHeadline/outEmail/outViral hanno **meno priorita'** dei quattro
pezzi sopra, per ora.

---

## FILE GIA' SCRITTI IN QUESTA SESSIONE (da riaprire, non rifare)

| File | Cosa |
|---|---|
| `competitor/Andrei Pascu/OUTFUNNEL-DOCUMENTAZIONE-UFFICIALE.md` + `.pdf` | Pezzo 1, chiuso |
| `competitor/Andrei Pascu/build_outfunnel_pdf.py` | Motore PDF del pezzo 1, riusabile come modello per il pezzo 2 |
| `competitor/Andrei Pascu/CLAUDE-SPEEDRUN-2-DOCUMENTAZIONE-UFFICIALE.md` | Pezzo 2, manca solo il PDF |
| `SKILL & Agenti/.../runs/andrei-pascu-armageddon-outfunnel-001/` | Dettaglio grezzo outFunnel, 20/20 |
| `SKILL & Agenti/.../runs/andrei-pascu-cs2online-001/MASTER-RUN-TRACKER.md` | Dettaglio grezzo cs2online, 20/40, fonte di verita' per lo stato |
| `SKILL & Agenti/.../runs/andrei-pascu-armageddon-outheadline-001/` | Testo grezzo 30/30, nient'altro |
