# EMP-D9HD — V4 ESECUTIVO del Piano Impero Vivo: 7/20 documenti completi, si riprende dal 08

- **Codice di ripresa:** `EMP-D9HD`
- **Aperto:** 2026-09-11 (chat satura, checkpoint d'urgenza su ordine di Max) · **Aggiornato:** 2026-09-11 sera (CP-20260911-H448: 7/20)
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

**Prossimo documento: `08-E2-RINOMINA.md`** (scheletro su disco). Poi 09…20 nell'ordine di
`00-INDICE.md` §2: per 09-20 lo scheletro va creato (`_ISTRUZIONI-SENTINELLA.md` §1 ha il template).
Si riempie con il tool **Write** (heredoc bash con testo lungo fallisce), dopo aver rimisurato ogni
numero sul disco. Checkpoint ogni 3-4 documenti.

**Fatti già raccolti per il 08 (E2), da usare senza rimisurare (11/09):**
- V2 §21-E2 (riga 717) + V3 §9.2 B-1 (le 235 destinazioni si contano ORA) + V3 Appendice C
  (+25-46 h misurate): 391 file toccati, 174 che cambiano fascia, `## Input / Output` → `## Output`.
- Dipende da E1: dopo E1 il perimetro è 407 nomi (non 439). I 43 `LINK-FIXABLE` di doctor e gli
  81 gruppi identici che toccano `company/` passano a E2/E5b (07-E1 §6).
- `scripts/rinomina_io.py` e `scripts/conta_destinazioni.py` **non esistono**: sono specifiche.
- `forge scan` misura per file (`empire/forge.py`, `_CORREDO` a 146-147); `--file` e `--json`
  sono specifiche di 07-E1 2.3/2.7 — E2 le eredita, non le rispecifica.

**Leggi in quest'ordine, a sezioni (mai V2 intero):**
1. `V4-ESECUTIVO/00-INDICE.md` §1-§3 · `_ISTRUZIONI-SENTINELLA.md` §4.
2. I modelli: `01`, `04`, `05`, `07` — stesso livello di dettaglio, stessa forma (intestazione con
   «il disco ha smentito il piano», §0 con «non dipende da Gael» se lo nomini, gate L9 copiabili).
3. Per ogni scaglione, SOLO le sezioni V2 §21 omonime (`grep -n "^### \*\*E" V2-PIANO-AMPLIATO.md`)
   e le correzioni V3 (`grep -n "E<n>" V3-PIANO-ASSESTATO.md`).

## 3. LO STATO DEL LAVORO

| Documento | Stato |
|---|---|
| `00-INDICE.md`, `_ISTRUZIONI-SENTINELLA.md`, `scripts/verifica_v4.py` | ✅ |
| `01-E0a`, `02-E0.5`, `03-E0b`, `06-E0.7` | ✅ conformi (CP-TVMY) |
| `04-E0.9`, `05-E0.6`, `07-E1` | ✅ conformi (CP-H448, a mano, 11/09 sera) |
| `08-E2` | scheletro vuoto su disco ← **SI RIPRENDE DA QUI** |
| `09`…`20` | non esistono |

**Gate:** `python PIANO-MAESTRO/scripts/verifica_v4.py` → **7/20** (11/09 sera).

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
