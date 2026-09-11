# EMP-D9HD — V4 ESECUTIVO del Piano Impero Vivo: 3/20 documenti completi, si riprende dal 04

- **Codice di ripresa:** `EMP-D9HD`
- **Aperto:** 2026-09-11 (chat satura, checkpoint d'urgenza su ordine di Max)
- **Stato:** APERTO
- **Chi riprende:** basta dire `EMP-D9HD` in una chat nuova dentro Digital Empire.
- **Predecessore:** `EMP-MCC4` (il piano intero V1→V4; V3 chiusa il 10/09, CP-20260910-RYHK)

---

## 1. IL LAVORO IN UNA FRASE

Scrivere i 20 documenti di scaglione di `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/V4-ESECUTIVO/` —
il piano ESECUTIVO (comandi esatti, file esatti, gate L9, prompt d'ingaggio) — finché
`python PIANO-MAESTRO/scripts/verifica_v4.py` dice **20/20 conformi**. Poi checkpoint di chiusura
V4, `00-LEGGIMI.md` §7 → V4 ✅, e la lista di `00-INDICE.md` §5 che Max spunta per il **via alla
costruzione**. Il divieto costruttivo (EMP-MCC4 §1) è **ancora in vigore**: V4 è carta.

---

## 2. DOVE SI RIPRENDE — SUBITO

**Prossimo documento: `04-E0.9-ATTO-DI-VENDITA.md`.** Poi 05, 07, 08, 09…20 nell'ordine di
`00-INDICE.md` §2. Lo scheletro a 7 sezioni di 04, 05, 07, 08 è **già su disco** (segnaposto
`_(in scrittura)_`): si riempie sezione per sezione con Edit, non si ricrea. Per 09-20 lo
scheletro va creato (`_ISTRUZIONI-SENTINELLA.md` §1 ha il template).

**Fatti già raccolti per il 04 (E0.9), da usare senza rimisurare:**
- Il prezzo è **già sul disco**: `Crea siti/Siti CCM/checkout.config.json` → `prezzo_lancio_eur
  67`, `prezzo_listino_eur 97`, `bump_eur 27`. È il default della decisione 8 (V3 §11).
- `scadenza_lancio: 2026-07-31` è **passata**: E0a (2.3) la sposta con `checkout.py --scadenza`.
- BACKLOG B-002/B-003 (righe 10-11): «NON si decide a mano: lo proporrà il team prezzi» — E0.9
  lo scavalca con un **default reversibile** (forma di V2 §26), non con una decisione definitiva.
- `29-ECOSISTEMA-LANCI/00-LEGGIMI.md:311`: «Il Manuale si vende o è un regalo?» — scadenza 7 gg
  dal 05/09, default «vendita»: è la **stessa** decisione 8, non duplicarla.
- `python scripts/tesoreria.py entrata --importo X --da <chi> --per corsi --stato incassato` è il
  comando reale per la riga `tipo: vendita` (il campo è `--per`/`--stato`, non `tipo`: **R5 in
  V3 §12 va letto come `--stato incassato --per corsi`**, correggere nel documento).
- La scala prezzi di Pascu (98→434→999) è in `competitor/Andrei Pascu/ANDREI-PASCU-DOSSIER-COMPLETO.md`.
- 23 video + 3 libri caricabili (`ultimo_metro.py`, 11/09 17:53: 31 fermi, 26 caricabili).

**Leggi in quest'ordine, a sezioni (mai V2 intero):**
1. `V4-ESECUTIVO/00-INDICE.md` — leggi §1, ordine §2, **template §3** (le 7 sezioni obbligatorie).
2. `V4-ESECUTIVO/_ISTRUZIONI-SENTINELLA.md` §4 — le regole di contenuto verificate a macchina.
3. `V4-ESECUTIVO/01-E0a-MERCE.md`, `02-E0.5-AGGANCI.md`, `03-E0b-ROTAZIONE.md` — i tre modelli
   già conformi: **stesso livello di dettaglio, stessa forma**.
4. Per ogni scaglione, SOLO le sezioni di V2/V3 citate in `00-INDICE.md` §2 e nei prompt
   originali (sono in questa chat, persi: si ricavano da V3 §10 + le sezioni V2 §21 omonime).

---

## 3. LO STATO DEL LAVORO

| Documento | Stato |
|---|---|
| `00-INDICE.md` | ✅ (leggi, ordine, template, gate globali, lista via-alla-costruzione) |
| `_ISTRUZIONI-SENTINELLA.md` | ✅ (contratto d'ingaggio, scheletro-prima-di-leggere) |
| `01-E0a-MERCE.md` | ✅ conforme (scritto a mano) |
| `02-E0.5-AGGANCI.md` | ✅ conforme (a mano) |
| `03-E0b-ROTAZIONE.md` | ✅ salvo **1 tilde a riga 32** (`~`+numero, L10) — togliere |
| `06-E0.7-HOOK.md` | ✅ conforme (unica sentinella riuscita, 43 KB) |
| `04`, `05`, `07`, `08` | scheletri vuoti su disco |
| `09`…`20` | non esistono |
| `scripts/verifica_v4.py` | ✅ il gate: 7 sezioni, niente `~`, INV-GAEL, lunghezza minima |

**Gate:** `python PIANO-MAESTRO/scripts/verifica_v4.py` → oggi 3/20 (+06 = 4/20 dopo il fix del tilde).

---

## 4. TRE CORREZIONI FATTE AL PIANO MENTRE SI SCRIVEVA (il disco vince) — non riscoprirle

1. **`python -m empire trace` ESISTE** (`scrivi/elenco/cerca/stato`, 25 tracce). L'Appendice B
   di V3 lo dava assente: corretto in V3 §7 punto 1. Il buco vero è il campo `origine` in
   `empire/trace.py:57-66` e i filtri `--origine/--finestra/--json`: sono di **F3** (doc 09).
2. **`scripts/ultimo_metro.py` NON ha `--json`** (solo `--scrivi`, `--segna ID`): V2 lo usa nei
   gate. È il passo 2.9 di E0.5. I gate di E0a usano l'output testuale.
3. **`company/REGISTRO-NUMERI.md` è in `company/Ecosistemi/REGISTRO-NUMERI.md`**; il doppio 08
   (`08-INTELLIGENCE` + `08-STREAM-S7-BOT`) è già dichiarato lì (righe 23-24). Passo 2.10 di E0.5.
   `00-INDICE.md` §1 e V3 Appendice B punto 6 hanno ancora il percorso vecchio: **da correggere**
   (REGOLA PUNTATORI).

Altri fatti misurati l'11/09: 19 file consumano `OPENROUTER_API_KEY` (non «20+»); B-020 è a metà
(commit `aa20b8e6`: chiamata Brevo lato server, resta solo revoca+variabile Netlify); B-061 nuova
(form webinar con segnaposto, non è una falla); `13-ARENA-APEX/orchestrator.py --help` → exit 1
cp1252, fix = 3 righe di `11-APEX-7-CORE/main.py:12-14`; `checkpoint.py cp` ha solo `--titolo`
(parser a riga 382); i 4 rail non-Stripe di `checkout.config.json` restano `attivo: false`.

---

## 5. TRAPPOLE — pagate oggi, non ricalpestarle

1. **Le sentinelle in background STALLANO** (watchdog 600 s, zero righe) — 11 su 11 con opus,
   anche a perimetro di UN documento, anche con scheletro pre-scritto. Non è il prompt: è lo
   stream dei sub-agenti dopo un'interruzione di rete (ENOTFOUND alle ~15:40). **Non rilanciare
   sentinelle per V4: si scrive a mano, un documento alla volta, salvando ogni sezione.** Se in
   una chat nuova vuoi riprovarne UNA, prova prima con un compito da 2 minuti: se stalla, basta.
2. **Chat satura**: un documento V4 sono 8-15 KB; dopo 3-4 documenti fai un checkpoint nuovo
   (`python scripts/checkpoint.py nuovo`), non aspettare l'ordine di Max.
3. **Il formato del battito è 🟩** (8º giro, `scripts/verifica_recap.py`): generarlo SEMPRE con
   `costruisci(...)` via script su file (non `python -c` con backtick: bash li interpreta) e
   validarlo prima di incollare; incollare il testo del file **verbatim** (una volta ho saltato
   la riga Forze ritrascrivendo a mano: il gate ha bloccato).
4. **Altre sessioni scrivono sullo stesso repo** (EMP-8M9F libro, LANCI di Gael, YouTube):
   `STATO-EMPIRE.md` cambia sotto i piedi → Read prima di ogni Edit in cima. Il blocco
   ⚠️ COORDINAMENTO di V4 è già dichiarato: perimetro `V4-ESECUTIVO/` + `00-LEGGIMI.md`.
5. **INV-GAEL** in `verifica_v4.py`: se nomini Gael fuori da `15-E5b-INGRESSI.md` senza la
   frase «non dipende da Gael», il gate boccia (successo sul 02, corretto).
6. `python -c` con virgolette annidate su Windows: usare uno script su file nello scratchpad.

---

## 6. CHIUSURA DI V4 — cosa manca dopo il 20º documento

1. `verifica_v4.py` → 20/20. Correggere ogni `~`, ogni sezione mancante.
2. Correggere i puntatori a `REGISTRO-NUMERI.md` in `00-INDICE.md` §1 e V3 Appendice B punto 6.
3. `00-INDICE.md` §6 (avanzamento) tutti ✅; `00-LEGGIMI.md` §7 → V4 ✅ + header di stato.
4. `python scripts/checkpoint.py cp --titolo "V4 ESECUTIVO chiusa: 20/20 documenti conformi, via alla costruzione pronto"`.
5. Riga in cima a `STATO-EMPIRE.md` + togliere il blocco ⚠️ COORDINAMENTO di V4.
6. **Non** iniziare la costruzione: serve l'ordine di Max («via alla costruzione»), lista di
   `00-INDICE.md` §5.

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-D9HD`*
