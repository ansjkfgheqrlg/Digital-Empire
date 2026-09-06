# ADR-023 — La Fabbrica Siti: una legge, un canone, due corsie

- **Stato:** ATTIVO
- **Data:** 2026-09-06
- **Ordinato da:** Max — *"Tu devi avere un sistema per la produzione di tutti i siti futuri.
  Consistente. Va a prendere tutti i nostri standard, la nostra qualità, le nostre performance,
  le nostre capacità di fare siti e quelle di Andrei, sia in grafica che in copy. Questo sistema
  deve essere vivo e attivo dentro di te, Emperator, e anche al di fuori di te come workflow
  dentro Digital Empire."*
- **Dossier:** `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md`
- **Legge:** `.claude/skills/fabbrica-siti/CLAUDE-SITI.md`
- **Nasce da:** lo studio forense di `armageddon.bsns.it` (2026-09-06)

---

## 1. Il fatto

Contato sul disco il 2026-09-06, prima di scrivere una riga:

> **Digital Empire ha quattro sistemi per fare siti, e due di essi si vietano a vicenda.**

| Sistema | Stack imposto | Dichiarazione |
|---|---|---|
| `empire-premium-style` | Next.js 16 + Tailwind v4 + Lenis + Framer + GSAP | *"Mai HTML/CSS statico. Mai Pages Router."* |
| `website-creator` | vanilla HTML+CSS+JS in un file solo | *"Zero framework. Zero build step."* |
| suite `site-*` — **15 skill, 4.052 righe** | `site-stack` e `site-premium-stack` dicono cose diverse da entrambe | ognuna un punto d'ingresso |
| agente `site-premium-builder` | Next.js **15** + shadcn + Radix + Headless UI + Chakra + Three.js + Theatre.js | *"stack OBBLIGATORIO"* |

Le prime due sono in contraddizione frontale ed entrambe si dichiarano obbligatorie.
**Conseguenza reale: quale sistema parte dipende da quale frase Max pronuncia, non da quale
lavoro va fatto.** Non è un sistema: sono quattro opinioni con lo stesso grado.

E il secondo fatto, altrettanto misurato:

> **Le 2.362 righe di studio sui 10 siti di Andrei Pascu non sono dentro nessuna skill.**
> Vivono in `competitor/Andrei Pascu/site-study/reports/`, che nessun agente legge quando
> costruisce. Tre mesi di lavoro archiviati, non operativi.

---

## 2. Cosa ha deciso il fatto nuovo

Il CSS di `armageddon.bsns.it` è servito in chiaro e commentato. Cita `CLAUDE.md §4`,
`assets/brand.css`, un mockup PDF misurato in unità (826,46 × 2.851,92) e un ticket `AP-138`.

**Andrei Pascu costruisce le sue landing con Claude Code, con una legge numerata che i suoi
agenti citano per giustificare una deroga.** Noi avevamo quattro skill che si smentivano e
nessun arbitro.

Il pezzo da copiare non è il rosso. È l'arbitro.

---

## 3. La decisione

### 3.1 Nasce la Fabbrica Siti
Organo unico, in `.claude/skills/fabbrica-siti/`, su sei livelli:
legge → canone → pattern → flusso a 9 passi → gate a macchina → memoria dei cantieri.
Vive **fuori** come skill invocabile e **dentro** Emperator come `emperator.md §6.20`, che è un
puntatore alla skill e non una copia — stessa forma già usata per il PDF (§6.19).

### 3.2 Due corsie, un canone

> **Corsia A — PAGINA.** ≤ 3 pagine **e** nessuno stato lato server.
> → HTML + CSS + JS vanilla, colonna `--u`, zero build, zero dipendenze.

> **Corsia B — SITO.** Tutto il resto.
> → Next.js 16 + Tailwind v4 + Lenis + Framer + GSAP.

**Entrambe leggono lo stesso `canone.css`.** Il canone è uno, la resa è due. Due pagine delle
due corsie messe fianco a fianco devono sembrare la stessa mano.

Un pattern nuovo si scrive **prima in vanilla**, poi la Corsia B lo avvolge in un componente.
Mai il contrario: dal vanilla al framework si sale, dal framework al vanilla si riscrive.

### 3.3 Perché due e non una
Non esiste un vincitore assoluto perché **fanno due mestieri diversi**, e i fatti lo dicono:

- `armageddon` non ha framework, non ha build, pesa 21 KB di HTML + 25 di CSS, **funziona con
  JavaScript spento**, e visivamente non gli manca niente. Oggi noi mandiamo in produzione una
  landing di lancio con `npm install`, un build step e sette dipendenze che invecchiano — peso
  pagato per sempre su un artefatto che vive tre settimane.
- Ma un LMS in HTML statico è masochismo, e `website-creator` che lo impone va corretto.

---

## 4. Cosa cambia per i sistemi esistenti

| Sistema | Destino |
|---|---|
| `empire-premium-style` | diventa la **Corsia B**. Perde il divieto "mai HTML statico" |
| `website-creator` | diventa la **Corsia A**. Perde il divieto "zero framework". La sua Legge Cosmica #0 (silver mixing) entra nel canone |
| suite `site-*` (15 skill) | assorbita nei 9 passi del flusso. Restano come riferimento, **smettono di essere punti d'ingresso** |
| `site-premium-builder` | allineato alla Corsia B. Via le librerie UI in concorrenza fra loro |

**Nessuna delle quattro viene cancellata in questo ADR.** Perdono l'autorità, non i file: una
cancellazione a caldo romperebbe lavori in corso. La rimozione, se servirà, sarà un ADR suo.

---

## 5. Cosa prendiamo da chi

**Da Andrei (12):** la colonna `--u` · il prezzo che si somma dal DOM · il titolo in due strati ·
la cucitura fotografica sullo stesso valore di opacità · `is-locked` · il contatore accessibile ·
`<details>`/`<dialog>` nativi · `font-display: block` quando il carattere è il design · le FAQ che
rispondono contro il proprio interesse · il testo che spiega il timer · le negazioni che chiudono
le contestazioni prima del pagamento · **il CLAUDE.md numerato e citabile**.

**Nostro, e resta (8):** la grana doppio strato · il silver mixing · `#0a0a0a` invece del nero
puro (misurato: sul nero assoluto il testo bianco sfrangia) · Onest variabile · i fondi alternati ·
APSOC · la Corsia B · **il gate a macchina** — lui si affida alla disciplina, noi no: la disciplina
si stanca.

**E tre suoi difetti diventano nostri controlli automatici:** contatore senza comportamento a
scadenza (gate 10), link col colore di default del browser (gate 7), FAQ senza JSON-LD (gate 8).

---

## 6. Conseguenze accettate

- **Due implementazioni per ogni pattern nuovo.** Mitigato dalla regola "prima vanilla, poi il
  componente": il costo è una volta sola e nella direzione facile.
- **Un canone in più da mantenere.** Mitigato da `canone_sync.py`, che fallisce se `canone.css` e
  `canone.json` divergono — la promessa "non possono divergere" è verificata da una macchina, non
  affidata alla buona volontà.
- **Il rischio ULTIMO METRO (ADR-016).** Un sistema perfetto produrrà siti perfetti mai messi
  online. Per questo il passo 9 del flusso **non è "consegna", è deploy**: un cantiere senza URL
  vivo resta aperto nell'indice e continua ad apparire nel battito finché non chiude.

---

## 7. Come si cambia

Solo con un altro ADR, che dica quale articolo di `CLAUDE-SITI.md` cambia, perché, e cosa si
rompe. Un articolo modificato in silenzio riporta il sistema al 5 settembre 2026, quando quattro
skill si contraddicevano e nessuna aveva torto.

---

## 8. Stato di costruzione

| Fase | Cosa | Stato |
|---|---|---|
| 1 | Legge + canone + questo ADR | **CHIUSA 2026-09-06** |
| 2 | I 20 pattern (11 nostri + 9 di Andrei) | aperta |
| 3 | Il flusso a 9 passi + `SKILL.md` + `emperator.md §6.20` | aperta |
| 4 | `gate_siti.py` (10 controlli) + `qa_sito.py` (Playwright) | aperta |
| 5 | Collaudo: rifare `armageddon` col nostro canone (Corsia A) + un sito reale (Corsia B) | aperta |
