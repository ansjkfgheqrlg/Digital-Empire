> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. PLATFORM

# T-site-design — Funzione L4: Design System e Componenti Visivi

> Funzione L4 · Reparto L2: WEB-ENGINEERING · Workflow: WF-SITE-FULL
> Ecosistema: `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md`

---

## Scopo

Definire il design system del sito: palette token, tipografia, spaziature, componenti UI base — tutto conforme a `empire-premium-style` o al brand kit cliente. Produce i componenti visivi prima del build vero e proprio, garantendo coerenza tra mockup e codice.

---

## Input

```json
{
  "arch_id": "PLT-ARCH-YYYY-NNN",
  "brand_kit": "brands/<slug>/brand-kit.json",
  "palette_override": "ink/orange/silver | custom"
}
```

---

## Output

```json
{
  "design_id": "PLT-DESIGN-YYYY-NNN",
  "tokens": {
    "colors": {"primary": "#...", "secondary": "#...", "bg": "#..."},
    "typography": {"heading": "font+size", "body": "font+size"},
    "spacing": "Tailwind v4 custom scale"
  },
  "components_list": ["Hero", "NavBar", "CTAButton", "CardServizio", "Footer"],
  "reference_sito": "Crea siti/Siti CCM/ | brand specifico",
  "asset_visual": ["paths immagini/icone fornite da CONTENT-FACTORY"]
}
```

---

## Processo

1. Legge `brand-kit.json` — estrae colori, font, logo, immagini
2. Applica `empire-premium-style` come layer base (token ink/orange/silver se brand neutro)
3. Definisce elenco componenti necessari dall'architettura
4. Se asset mancanti → richiesta a CONTENT-FACTORY (visual assets) prima del build
5. Salva `design.json` + eventuale canvas design in `orders/PLT-DESIGN-YYYY-NNN/`
6. Trigger su T-site-components

---

## Skill usate

- skill `frontend-design` — design system component-level
- skill `theme-factory` — generazione token palette
- skill `empire-premium-style` / `empire-style` — stile DE premium (Tailwind v4, ink/orange/silver)
- skill `canvas-design` — mockup canvas se richiesto

---

## Gate G-BRAND

Il design system deve essere approvato (G-BRAND) prima che il build parta:
- Palette conforme a brand-kit
- Tipografia leggibile su mobile (min 16px body)
- Logo in formato corretto (SVG preferred)

---

## Agente responsabile

`plt-site-architect` (definisce token e componenti) con supporto di `plt-motion-eng` per il layer animazioni

---

## KPI

| KPI | Target |
|---|---|
| Design approvato senza revisioni post-build | ≥ 80% |
| Asset visivi richiesti a CF con ≥2gg anticipo | 100% |

## Connessioni

- [[06-PLATFORM/Reparti/Web-Engineering.md]] — reparto padre
- [[06-PLATFORM/Funzioni/T-site-architecture.md]] — funzione precedente
- [[06-PLATFORM/Funzioni/T-site-components.md]] — funzione successiva
- [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]] — dossier completo §3 + §6
