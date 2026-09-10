---
name: empire-premium-style
description: "INGRESSO LEGACY — non detta piu' legge. Il sistema unico per costruire e restilizzare siti in Digital Empire e' la FABBRICA SITI (.claude/skills/fabbrica-siti/). Questa skill resta viva solo per non rompere i vecchi richiami ('/empire-style <path>', 'trasforma questo sito in stile empire', 'rifai questo sito come ccm-premium', 'applica lo stile premium Digital Empire') e per rimandare la' dove si lavora davvero. Se l'utente ti attiva con una di quelle frasi, apri la Fabbrica e procedi con la sua legge."
---

# Empire Premium Style — INGRESSO LEGACY

> **Fusa nella Fabbrica Siti il 2026-09-09** (dossier 33 §5, ADR-023, ADR-024).
> Questa skill **non contiene più il sistema**. Contiene la strada per arrivarci.

## Cosa fare quando vieni attivata

1. **Apri la legge:** `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` — dodici articoli, tutti non
   derogabili. Sono la sola autorità sui siti di Digital Empire.
2. **Scegli la corsia** con §5, dal lavoro e non dal gusto:
   - ≤ 3 pagine e nessuno stato → **vanilla** con la colonna `--u`;
   - tutto il resto → **Next.js 16**, e i riferimenti di scaffolding stanno in
     `.claude/skills/fabbrica-siti/corsia-b/`.
3. **Prendi i valori dal canone**, `fabbrica-siti/canone/canone.css` — mai da qui, mai inventati (§1).
4. **Prendi le sezioni dai pattern**, `fabbrica-siti/pattern/`, e guarda la galleria:
   `python .claude/skills/fabbrica-siti/scripts/galleria.py`.

## Perché è stata fusa

Il 2026-09-06 Digital Empire aveva **quattro sistemi per fare siti, e due si vietavano a vicenda**:
questa skill imponeva *"mai HTML/CSS statico"*, `website-creator` imponeva *"zero framework"*, ed
entrambe si dichiaravano obbligatorie. Quale partiva dipendeva da quale frase pronunciava Max, non
da quale lavoro andava fatto (ADR-023).

Cosa è successo ai suoi pezzi:

| Pezzo | Destino |
|---|---|
| I nove colori di `design-tokens.css` | **erano già identici** a quelli del canone, carattere per carattere: niente da fondere |
| I 53 token `--color-*` (ponte Tailwind/shadcn) | restano di Corsia B, non entrano nella legge |
| `reference-page-full.tsx` (837 righe, 17 sezioni) | → `fabbrica-siti/corsia-b/riferimenti/` |
| `build-playbook`, `layout-template`, `package.json`, `components` | → `fabbrica-siti/corsia-b/riferimenti/` |
| `section-patterns.md` (10 puntatori su 17 stale) | **morto**, sostituito dalla galleria generata |
| Questa `SKILL.md` | ingresso legacy: rimanda e basta |

## Le due regole che questa skill sbagliava, e che la legge ha corretto

1. **Imponeva uno stack unico** (*"Next.js 16 obbligatorio, mai HTML statico"*). La legge sceglie
   dalla vita del pezzo: una pagina di cassa da 1.500 px in Next.js è un motore acceso per spostare
   una sedia.
2. **Congelava i pattern in un file di prosa.** Una prosa non si accorge di diventare falsa: dieci
   dei suoi diciassette puntatori erano già sbagliati quando è stata fusa. La galleria si rigenera
   dal disco.

---

## Connessioni
- `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` — la legge
- `.claude/skills/fabbrica-siti/corsia-b/LEGGIMI.md` — dove sono finiti i riferimenti
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` · `PIANO-MAESTRO/33-...` §5
- `company/Memory/decisions/ADR-023-fabbrica-siti-due-corsie.md` · `ADR-024-canone-v2-primo-strato.md`

---

## Nota per chi cerca il canone visivo di Andrei Pascu (Sentinella, 2026-09-10)

Chi cerca dove innestare i risultati del site-study visivo di Andrei Pascu
(`competitor/Andrei Pascu/site-study/SINTESI-SISTEMA-VISIVO.md`) **non trova qui la destinazione
giusta**: questa skill non porta più contenuto proprio. La legge vera (`fabbrica-siti/CLAUDE-SITI.md`)
già incorpora buona parte dello studio Andrei Pascu (§8, §11, §12 citano
`site-study/reports/11-armageddon...`, `24-25-27-28-macchina-del-funnel...`). Ciò che resta NUOVO
nella sintesi dell'onda G del 2026-09-09 (temperatura del traffico che governa la forma della
pagina, densità immagini/1.000px come gate, carattere sempre dichiarato) non è stato ancora
proposto come articolo di legge qui: farlo richiede un ADR (vedi "Come si cambia questa legge" in
`CLAUDE-SITI.md`), fuori dal perimetro di questa patch — segnalato a Max/Emperator, non applicato
in silenzio.
