---
name: web-research-skill
tier: tier2-functional
description: "Ricerca/crawl web con Playwright (render JS) + screenshot delle sezioni chiave, senza API. Degrada con grazia a urllib se Playwright non e' installato."
uses_scripts:
  - scripts/web_research.py
---

# web-research-skill (tier2-functional)

> Ricerca avanzata e crawl di siti, con screenshot che Claude puo' guardare.

## Cosa fa
- Apre URL con Playwright, estrae il testo principale e cattura screenshot.
- Se Playwright manca, scarica l'HTML grezzo con urllib (senza screenshot).
- Registra le fonti in sources.json con trace a URL + screenshot.

## Come si usa
```
python skills/tier2-functional/web-research-skill/scripts/web_research.py --crawl <url> --run myrun
```

## Invarianti
- CLI-only, no API.
- Playwright opzionale (degrada a urllib).
- Trace a URL + screenshot.

## Agenti che la impugnano
- `web-department/web-researcher`
- `web-department/site-crawler`

## Script
`scripts/web_research.py` usa Playwright se presente, altrimenti urllib.

## Trace
risponde a 'siti web o ricerca estremamente avanzata'.
