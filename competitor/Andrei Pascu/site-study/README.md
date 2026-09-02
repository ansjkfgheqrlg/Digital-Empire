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

## Stato: 6 report su 9

| # | Pagina | Altezza | Blocchi copy | Report |
|---|--------|---------|--------------|--------|
| 01 | [andrei-copy.com](reports/01-andrei-copy-home.md) — hub | 3.384px | 38 | ✅ |
| 02 | [/funnel-operator](reports/02-funnel-operator.md) — 434 € | 24.019px | 178 | ✅ |
| 03 | [/outheadline](reports/03-outheadline.md) — 98 € | 21.119px | 241 | ✅ |
| 04 | [/outfunnel](reports/04-outfunnel.md) | 26.993px | 163 | ✅ |
| 05 | [/copy](reports/05-copy-mentorship.md) — 349/999 € | 26.952px | 337 | ✅ |
| 06 | /manuale-del-copywriter | 11.067px | 139 | ⬜ **da fare** |
| 07 | [claude-speedrun.com](reports/07-claude-speedrun.md) — 249 € | 33.756px | 380 | ✅ 🔴 |
| 08 | apsales.eu — sito agenzia | 12.565px | 168 | ⬜ **da fare** |
| 09 | linktr.ee/andrei.bsns | 1.287px | 119 | ⬜ **da fare** |

**Materiale grezzo catturato: 9 pagine su 9.** Mancano solo i report scritti per 06, 08, 09.

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

### 4. Nessuna garanzia di rimborso, su nessuna pagina
Sostituita dall'assistenza (*"non sei più solo"*) o da uno storico verificabile (*"5 aggiornamenti gratuiti in 4 anni"*).

### 5. Più la pagina è lunga, più grassetta
Rapporto grassetto/corpo: 13% nell'hub → 52% in `/copy` → 69% in `outfunnel` → 80% in `outheadline`. Chi scorre in diagonale deve capire tutto leggendo solo i grassetti.

### 6. Incoerenza numerica diffusa
`3700` / `3600+` / `3100` ordini · `1000+` / `1500+` / `2000+` studenti. Sei cifre per tre metriche, tra pagine dello stesso store e a volte nella stessa pagina.

---

## Connessioni

- [[Source_Andrei_Pascu_10_Lead_Magnet]] — video 4 cat2: le regole applicate in queste pagine
- [[Source_Andrei_Pascu_Importanza_Landing]] — video 5 cat2: la teoria della landing minima
- [[Source_Andrei_Pascu_Ordine_Funnel]] — video 2 cat2: `outfunnel` è quel video fatto prodotto
- `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/andrei-pascu-001/` — lo studio dei 33 video
- `.claude/skills/empire-premium-style/SKILL.md` — la nostra skill con `#fb4604` + Onest
