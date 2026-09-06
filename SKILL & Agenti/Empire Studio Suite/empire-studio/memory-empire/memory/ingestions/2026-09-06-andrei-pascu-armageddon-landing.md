# INGESTIONE — armageddon.bsns.it (Andrei Pascu, pagina di lancio)

**Data:** 2026-09-06 · **Tipo:** sito (non video) · **Run:** studio siti Andrei Pascu, pagina 11
**Fonte:** https://armageddon.bsns.it/ · **Metodo:** cattura forense Playwright (`site_capture.py`) +
visione nativa Claude su tutti e 10 gli screenshot + lettura integrale di CSS (1.020 righe) e JS (5,6 KB)

## Cosa e' stato acquisito
- 6 slice desktop (1440x900) + 4 mobile (390x844) — visionate una per una
- `design-tokens.json` — palette con conteggi d'uso letti da `getComputedStyle`, scala tipografica,
  inventario CTA con misure, inventario media
- `copy-integrale.md` — 57 blocchi di testo in ordine di lettura con posizione, colore, corpo, peso
- `dom-blocks.json` — bounding box e stile computato
- `armageddon.css` integrale (1.020 righe, commentato dall'autore) + IIFE inline (5,6 KB)

## Scoperta maggiore — metodo di produzione del competitor
I commenti del CSS servito citano: `docs/homepage-design/full-page-mockup.pdf` (826,46 x 2.851,92
unita'), **`CLAUDE.md §4`** come autorita' per una deroga, `assets/brand.css`, il ticket **`AP-138`**,
e richieste datate del committente ("Andrei asked on 5 September").

**Andrei Pascu costruisce le sue landing con Claude Code**, con CLAUDE.md numerato, brand.css,
mockup PDF misurato e ticket system. E' intelligence sul suo METODO, non sul suo stile — e vale di piu'.

## Enrichment-research — cosa e' stato trovato

### Skill/workflow che POSSONO essere migliorati (trovato: 4)
| Skill/sistema | Cosa manca oggi | Cosa aggiungere |
|---|---|---|
| `empire-premium-style` | vieta l'HTML statico per principio; nessun sistema di misura proporzionale | la colonna `--u`; togliere il divieto assoluto (una landing di lancio non ha bisogno di Next.js) |
| `website-creator` | vieta i framework per principio; nessun gate | diventa la Corsia A del nuovo sistema, con canone condiviso |
| suite `site-*` (15 skill) | 15 punti d'ingresso senza un arbitro fra loro | assorbita nei 9 passi del flusso |
| `cro-copy-architect` | APSOC c'e', ma non lo standard "FAQ che rispondono contro il proprio interesse" | 6 FAQ su 11 di questa pagina allontanano l'acquisto — pattern da codificare |

### Contraddizione di sistema trovata (BLOCCANTE, non risolvibile in automatico)
`empire-premium-style` ("mai HTML/CSS statico") e `website-creator` ("sempre e solo vanilla, zero
framework") si contraddicono frontalmente e si dichiarano entrambe obbligatorie. Nessuna patch
automatica e' possibile: serve una decisione di Max. Proposta formulata in
`PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` §3 (due corsie, un canone) + ADR da aprire.

### Patch applicate a skill esistenti
**Nessuna.** Motivo dichiarato: ogni patch singola su una delle quattro skill peggiorerebbe la
contraddizione invece di risolverla. Il lavoro e' stato consegnato come piano, non come modifica.

## Artefatti prodotti
- `competitor/Andrei Pascu/site-study/reports/11-armageddon.md` — rapporto strategico
- `competitor/Andrei Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md` — schermata per
  schermata, ogni misura, ogni effetto, ogni colore
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` — il sistema (6 livelli, 5 fasi, 10 gate)
- `second-brain-vault/wiki/sources/Source_Andrei_Pascu_Armageddon_Landing_Lancio.md`
- README site-study aggiornato: 10 pagine su 12 note

## Difetto del nostro strumento trovato durante l'ingestione
`site_capture.py` estrae il testo proprio di un `<p>` escludendo i figli `<strong>`: le risposte FAQ
risultano bucate ("Quattro corsi completi — , , e —"). Il contenuto e' recuperabile dall'HTML, ma il
file `copy-integrale.md` non e' affidabile su paragrafi con inline. **Da correggere prima della
prossima cattura.** Registrato in BACKLOG.
