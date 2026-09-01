# beast-preventivi

Skill ufficiale Anthropic per costruire preventivi freelance/agenzia che vendono.

## Cosa fa

Trasforma la logica di una discovery call in un preventivo professionale, **problem-first**, con 3 opzioni di pricing e struttura narrativa che porta il cliente a comprare — senza giustificarsi sul prezzo.

Principio fondamentale: tutto ruota attorno al problema del cliente. Il preventivo non è una lista prezzi — è una lettera di vendita.

Specializzata per **agenzie di landing page e performance marketing**, generalizzabile a qualsiasi servizio B2B/freelance.

---

## Come si attiva

Naturalmente quando l'utente dice:
- "quanto chiedo per questo progetto?"
- "aiutami a fare il preventivo per [cliente]"
- "come struturo la proposta per [X]?"
- "il cliente chiede un preventivo / il prezzo"
- "devo rispondere a un cliente che chiede quanto costa"
- "non so quanto farmi pagare"

---

## Cosa fornire quando si usa la skill

```
Cliente: [nome / settore / dimensione]
Problema: [cosa ha detto in discovery — parole sue]
Consapevolezza: aware / unaware
Budget indicato: [range o "non ancora definito"]
Servizio: [landing page / funnel / etc.]
Discovery fatta: sì / no
```

Più contesto fornisci, più il preventivo generato è specifico e chiudibile.

---

## Struttura

```
beast-preventivi/
├── SKILL.md                               # kernel + routing
├── references/
│   ├── concepts/
│   │   └── problem-centric-selling.md    # filosofia problem-first
│   ├── stages/
│   │   ├── 01-discovery.md               # come fare discovery call
│   │   ├── 02-pricing.md                 # strategia 3 opzioni
│   │   ├── 03-document-structure.md      # le 8 sezioni del preventivo
│   │   └── 04-call-presentation.md       # come presentare in call
│   ├── patterns/
│   │   └── client-awareness.md           # aware vs. unaware
│   └── conventions/
│       └── anti-patterns.md              # 11 errori da evitare
├── assets/
│   ├── templates/
│   │   └── preventivo-canvas.md          # template da compilare
│   └── examples/
│       └── landing-page-agency.md        # esempio e-commerce fashion
├── evals/
│   └── evals.json                        # 6 test prompts realistici
└── README.md
```

---

## Generata con

Costruita con `content-forge` (skill meta) da 7 fonti su preventivi e vendita freelance (Federico Presta, Andrea Marke Design, Andrei Pascu, Videomaker Crop, Fiscozen, guida strategica).

KG: 66 atomi in 8 cluster — anti-pattern, struttura documento, discovery, pricing, call presentation, outreach, USP/branding, pagamenti.

Build: 2026-05-24.
