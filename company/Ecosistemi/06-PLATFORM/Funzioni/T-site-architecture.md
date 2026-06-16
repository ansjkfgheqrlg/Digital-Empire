> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. PLATFORM

# T-site-architecture — Funzione L4: Architettura e Stack

> Funzione L4 · Reparto L2: WEB-ENGINEERING · Workflow: WF-SITE-FULL
> Ecosistema: `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md`

---

## Scopo

Definire l'architettura informativa del sito (struttura pagine, gerarchia sezioni, routing) e lo stack tecnologico finale. Produce il documento di architettura che autorizza il build. Ogni scelta di stack è preceduta da ricerca INTELLIGENCE (benchmark, librerie, competitor tecnici).

---

## Input

```json
{
  "brief_id": "PLT-BRIEF-YYYY-NNN",
  "brief": "orders/PLT-BRIEF-YYYY-NNN/brief.json",
  "ricerca_tecnica": "opzionale — fornita da INTELLIGENCE se disponibile"
}
```

---

## Output

```json
{
  "arch_id": "PLT-ARCH-YYYY-NNN",
  "stack": {
    "framework": "Next.js 15 | Next.js 16",
    "css": "Tailwind v4",
    "animation": "Lenis | Framer Motion | GSAP",
    "3d": "Three.js/R3F | nessuno",
    "deploy": "Vercel"
  },
  "sitemap": ["pagine e routing"],
  "sezioni_per_pagina": {},
  "componenti_stimati": 12,
  "dipendenze_esterne": [],
  "note_architetturali": "ADR inline se scelte non standard"
}
```

---

## Processo

1. Legge brief + eventuali ricerche INTELLIGENCE (`market-competitors`, benchmark stack)
2. Definisce sitemap e gerarchia sezioni
3. Sceglie stack (default: Next.js 15 + Tailwind v4 + Lenis) — deviazioni richiedono nota ADR
4. Stima componenti e dipendenze esterne
5. Salva `arch.json` in `orders/PLT-ARCH-YYYY-NNN/`
6. Trigger su T-site-design

---

## Skill usate

- skill `site-architecture` — architettura informativa
- skill `site-stack` — selezione e razionalizzazione stack
- skill `site-premium-stack` — stack premium DE (Next15+Tailwind v4+Lenis)
- `memory_search("platform/decisions", "stack "+tipo_sito)` — scelte precedenti

---

## Regola stack-radar

Prima di ogni scelta di upgrade di major version (es. Next.js 16) → consultare `int-trend-scout` (INTELLIGENCE) per verifica compatibilità. La skill `stack-radar` (da creare in FORGE) automatizzerà questo check trimestrale.

---

## Agente responsabile

`plt-site-architect`

---

## KPI

| KPI | Target |
|---|---|
| Architetture senza revisione post-build | ≥ 90% |
| Stack conformi a standard DE | 100% (deviazioni documentate come ADR) |

## Connessioni

- [[06-PLATFORM/Reparti/Web-Engineering.md]] — reparto padre
- [[06-PLATFORM/Funzioni/T-site-brief.md]] — funzione precedente
- [[06-PLATFORM/Funzioni/T-site-design.md]] — funzione successiva
- [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]] — dossier completo §3
