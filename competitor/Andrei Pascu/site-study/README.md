---
Type: PROJECT
Status: Active
Tags: #competitor #andrei-pascu #site-study #design-system #copy-teardown
Created: 2026-09-01
Last updated: 2026-09-02
---

# STUDIO SITI ANDREI PASCU — indice

Studio forense di tutti i siti dell'ecosistema Andrei Pascu: design system, palette con hex esatti, tipografia misurata, posizione degli elementi, teardown del copy sezione per sezione.

Fa parte del **Reparto Competitor Research** di Digital Empire (ecosistema #1: Andrei Pascu), insieme allo studio dei 33 video già ingeriti in Empire Studio.

---

## Stato: 9 report su 9 ✅

| # | Pagina | Altezza | Blocchi copy | Report |
|---|--------|---------|--------------|--------|
| 01 | [andrei-copy.com](reports/01-andrei-copy-home.md) — hub | 3.384px | 38 | ✅ |
| 02 | [/funnel-operator](reports/02-funnel-operator.md) — 434 € | 24.019px | 178 | ✅ |
| 03 | [/outheadline](reports/03-outheadline.md) — 98 € | 21.119px | 241 | ✅ |
| 04 | [/outfunnel](reports/04-outfunnel.md) | 26.993px | 163 | ✅ |
| 05 | [/copy](reports/05-copy-mentorship.md) — 349/999 € | 26.952px | 337 | ✅ |
| 06 | [/manuale-del-copywriter](reports/06-manuale-del-copywriter.md) — 79 € | 11.067px | 139 | ✅ |
| 07 | [claude-speedrun.com](reports/07-claude-speedrun.md) — 249 € | 33.756px | 380 | ✅ 🔴 |
| 08 | [apsales.eu](reports/08-apsales.md) — **agenzia CRO** | 12.565px | 168 | ✅ 🔴 |
| 09 | [linktr.ee/andrei.bsns](reports/09-linktree.md) — bio-link | 1.287px | 119 | ✅ |

**9 pagine su 9 catturate e studiate.** 371 screenshot · 1.832 blocchi di copy · 2.362 righe di report.

> ⚠️ **L'ecosistema però ha almeno 11 pagine.** Lo storico del bio-link (report 09) rivela due prodotti mai catturati: **`outViral`** (terzo membro della famiglia `out*`) e **`Timer`**. Da aggiungere al prossimo giro.

---

## Come è stato costruito

`scripts/site_capture.py` — cattura forense via Playwright. Per ogni URL produce:

| File | Contenuto |
|------|-----------|
| `capture/<slug>/desktop-NN.png` | Screenshot a fette verticali, viewport 1440×900 |
| `capture/<slug>/mobile-NN.png` | Idem, 390×844 |
| `capture/<slug>/design-tokens.json` | Palette testo e sfondi **con conteggio d'uso**, font, scala tipografica, raggi, inventario CTA con misure e colori, inventario media, headings |
| `capture/<slug>/copy-integrale.md` | **Ogni testo della pagina** in ordine di lettura, con posizione `y`, tag, colore, dimensione, peso, href |
| `capture/<slug>/dom-blocks.json` | Blocchi testuali con bounding box e stile computato |

I colori sono letti dal **DOM renderizzato** (`getComputedStyle`), non stimati dagli screenshot: gli hex sono esatti.

```bash
python scripts/site_capture.py "https://esempio.com/pagina" --slug "10-nome-pagina"
```

**Gli screenshot (371 file, 76 MB) sono esclusi dal repo** via `.gitignore` — restano su disco e si rigenerano col comando sopra. Nel repo entrano i report e tutti i dati testuali.

---

## Le scoperte trasversali

### 1. Un prodotto = una pelle cromatica
Griglia, tipografia e componenti sono comuni; **l'accento cambia per prodotto**:

| Prodotto | Accento | Prezzo |
|---|---|---|
| Hub istituzionale | Blu `#0062ff` | — |
| `funnel-operator` | Blu + light-leak | 434 € |
| `outheadline` | Rosso `#d50101` (problema) / verde `#7ab641` (soluzione) | 98 € |
| `outfunnel` | Teal | n/d |
| `copy` Mentorship | Giallo-ambra `#efab00` | 349 / 999 € |
| **Claude Speedrun** | **Arancione `#fb4604`** | 249 € |

Il blu `#0062ff` resta **il colore dell'azione** su tutte le pagine — e viene rotto solo dal bottone che incassa davvero.

### 2. 🔴 Claude Speedrun usa il nostro identico linguaggio visivo
`#fb4604` + font `Onest` = esattamente ciò che `empire-premium-style/SKILL.md` dichiara per `ccm-premium`. Ed è un corso su Claude per marketer italiani a 249 €. **Concorrente diretto di Claude Code Mastery.** Dettagli e azioni in [07-claude-speedrun.md](reports/07-claude-speedrun.md).
**Da verificare prima di ogni conclusione:** le date di pubblicazione delle due pagine (Wayback Machine).

### 3. La lunghezza del copy è funzione del prezzo
98 € → dimostrazione · 249 € → workflow reali · 434 € → 12.000px di biografia · 999 € → ecosistema + testimonianze video.

### 4. Nessuna garanzia di rimborso su nessun info-prodotto — ma sull'agenzia sì
Sui 7 prodotti informativi: sostituita dall'assistenza (*"non sei più solo"*), da uno storico verificabile (*"5 aggiornamenti gratuiti in 4 anni"*) o **dall'anteprima gratuita del prodotto stesso** (`manuale-del-copywriter`).
Su `apsales.eu`, invece, la garanzia esiste ed è di **rimedio, non di rimborso**: *"Se le conversioni non aumentano, rimettiamo mano alla pagina. Gratis, a condizioni chiare."*
**Regola:** il B2B compra la garanzia di rimedio, il B2C la garanzia di rimborso — e chi vende informazione può sostituirle entrambe con un campione del prodotto.

### 5. Più la pagina è lunga, più grassetta
Rapporto grassetto/corpo: 13% nell'hub → 52% in `/copy` → 69% in `outfunnel` → 80% in `outheadline`. Chi scorre in diagonale deve capire tutto leggendo solo i grassetti.

### 6. Incoerenza numerica diffusa
`3700` / `3600+` / `3100` ordini · `1000+` / `1500+` / `2000+` studenti · **`270 mila` (andrei-copy) contro `250.000` (apsales) follower**. **Otto cifre per quattro metriche**, tra pagine dello stesso store e a volte nella stessa pagina.

### 7. La lunghezza del copy non dipende dal prezzo, ma da quanto lavoro deve fare la pagina
Correzione alla scoperta #3, imposta dai dati: 79 € su 11.067px contro 98 € su 21.119px. Il `manuale-del-copywriter` è corto perché **a metà pagina regala un'anteprima vera del prodotto**, e da lì in poi vende quella. Se un campione fa il lavoro, la pagina si dimezza.

### 8. Quando fa sul serio, abbandona Squarespace/Framer
Due pagine su nove hanno un design system vero — `claude-speedrun.com` e `apsales.eu` — ed entrambe sono i progetti recenti. Segni riconoscibili: `oklch`, raggi coerenti (o zero raggi), poche famiglie di font, **nessun banner "stiamo aggiornando il brand"**. Le sette pagine storiche hanno 5 font, 8 raggi diversi e un avviso di cantiere fisso in basso a sinistra.

### 9. `claude-speedrun.com` è un prodotto suo — misurato, non dedotto
Il link è **nella barra di navigazione di `andrei-copy.com`** (`<a href="https://claude-speedrun.com">Claude Speedrun</a>`, presente su tutte le pagine) ed è il terzo link del suo bio-link (`Claude Speedrun 2`). Resta aperta solo la domanda sulle **date**: chi ha usato per primo `#fb4604` + Onest, lui o `ccm-premium`. Si risponde con Wayback Machine, non con il ragionamento.

### 10. Il punto d'ingresso del funnel è la cosa meno curata dell'ecosistema
Il bio-link (report 09) è un Linktree stock: 3 link, zero copy, zero raccolta email, **55 CTA su 58 che portano ad altri profili Linktree**. Contraddice la lezione che lui stesso insegna nel video 5 cat2. È la conferma pratica che quel gradino lo salta anche chi lo insegna.

---

## Connessioni

- [[Source_Andrei_Pascu_10_Lead_Magnet]] — video 4 cat2: le regole applicate in queste pagine
- [[Source_Andrei_Pascu_Importanza_Landing]] — video 5 cat2: la teoria della landing minima
- [[Source_Andrei_Pascu_Ordine_Funnel]] — video 2 cat2: `outfunnel` è quel video fatto prodotto
- `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/andrei-pascu-001/` — lo studio dei 33 video
- `.claude/skills/empire-premium-style/SKILL.md` — la nostra skill con `#fb4604` + Onest
