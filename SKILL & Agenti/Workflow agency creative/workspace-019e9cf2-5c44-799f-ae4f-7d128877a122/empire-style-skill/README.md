# empire-style

**Claude Code skill** — trasforma qualsiasi sito esistente nello stile ultra-premium **Digital Empire** in 8 step automatizzati.

---

## Struttura

```
.
├── commands/
│   └── empire-style.md                        # Entry-point slash command /empire-style
└── skills/
    └── empire-premium-style/
        ├── SKILL.md                           # Logica principale della skill (8 step)
        └── references/
            ├── build-playbook.md              # Istruzioni di build e deploy
            ├── components.md                  # Libreria componenti Empire
            ├── design-tokens.css              # Token CSS: colori, font, spacing
            ├── layout-template.md             # Template struttura pagine
            ├── package.json.md                # Dipendenze npm standard
            ├── reference-layout.tsx           # Layout root Next.js di riferimento
            ├── reference-page-full.tsx        # Pagina completa di riferimento
            └── section-patterns.md            # Pattern per hero, CTA, pricing, footer
```

---

## Cosa fa

Prende un sito sorgente (HTML statico, Next.js, React, Vue, export WordPress, ecc.) e lo riscrive completamente applicando il design system Digital Empire:

- Palette `ink / paper / grey` + arancione `#fb4604` + silver-metallic
- Tipografia premium con gerarchia serrata
- Componenti UI con effetti `glass`, `grain-texture`, `glow`
- Scaffold **Next.js 15 + Tailwind CSS 3**
- Metadata SEO e Open Graph ottimizzati
- Output pronto con `npm run dev`

---

## Installazione

Copia le cartelle nella home di Claude Code:

```bash
# macOS / Linux
cp -r commands/* ~/.claude/commands/
cp -r skills/*   ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse commands\* "$env:USERPROFILE\.claude\commands\"
Copy-Item -Recurse skills\*   "$env:USERPROFILE\.claude\skills\"
```

---

## Utilizzo

```
/empire-style <path-del-sito-sorgente>
```

**Esempio:**

```
/empire-style ./mio-sito-vecchio
```

Output generato in: `./mio-sito-vecchio-empire/` — compilato e pronto.

---

## I 8 step del processo

| # | Step | Descrizione |
|---|------|-------------|
| 1 | Acquisizione source | Legge e classifica tutti i file del sito sorgente |
| 2 | Classificazione sezioni | Mappa hero, features, pricing, CTA, footer ecc. |
| 3 | Scaffold Next.js | Inizializza il progetto con lo stack corretto |
| 4 | Generazione pagine | Ricrea ogni pagina con componenti Empire |
| 5 | Applicazione pattern | Applica design system: colori, font, spacing |
| 6 | Microcopy cohesion | Allinea testi e tono al brand Empire |
| 7 | Metadata + SEO | Inietta meta tag, OG, JSON-LD schema |
| 8 | Build + verifica | Compila e verifica `npm run build` |

---

## Stack output

- **Framework:** Next.js 15
- **Styling:** Tailwind CSS 3
- **Animazioni:** Framer Motion
- **Font:** Inter + sistema tipografico Empire
- **Node.js:** 18+

---

*Digital Empire — build different.*
