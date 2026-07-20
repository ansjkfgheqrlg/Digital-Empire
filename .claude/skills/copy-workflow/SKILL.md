---
name: copy-workflow
description: "Motore copy ufficiale di Digital Empire (orchestration layer APSOC, 8 agenti A1-A8). Usa /copywriting per qualsiasi copy: ads, sales page, email, VSL, social, headline, obiezioni, avatar, funnel, review. Regole: prima il PROBLEMA poi la soluzione (sempre); score QA >=85; tono DE = diretto/sincero/semplice, no tecnichese. Motore vendored in copy-workflow/ (ADR-003: wrap, mai riscrittura)."
---

# Copy-Workflow — Motore copy ufficiale (wrapper)

> **Reparto proprietario:** `04-MARKETING / L2-1 Copywriting` — controllore: gate copy L2-1-qa.
> **Motore (sorgente eseguibile):** `copy-workflow/` alla root del repo — clonato da
> `gh repo clone ansjkfgheqrlg/copy-workflow` (2026-07-20, ADR-009). **ADR-003: si WRAPPA, non si riscrive.**
> Kernel completo: `copy-workflow/SKILL.md` (team 8 agenti, framework APSOC, tutte le modalità).
> Skill interne del motore: `copy-workflow/skills/` (apsoc-builder, copy-review, funnel-designer,
> headline-forge, objections-forge, target-avatar). Workflow: `copy-workflow/workflows/`.

## Quando usarla (obbligo)
Ogni copy prodotto nell'impero — siti, landing, ads, email, VSL, script video, lead magnet,
messaggi di vendita/outreach, preventivi commerciali — passa da qui. Regola aurea APSOC:
**A**ttenzione → **P**roblema (sempre PRIMA della soluzione) → **S**oluzione → **O**biezioni (CPB) → **C**TA.

## Modalità (delega al motore)
`/copywriting full|ad|sales-page|email|vsl|social|headline|objections|avatar|funnel|review`
→ leggi `copy-workflow/SKILL.md` per la modalità scelta e segui il workflow corrispondente in
`copy-workflow/workflows/`. Invocazione naturale: descrivi cosa vuoi scrivere.

## Adattamenti Digital Empire (sopra il motore, mai dentro)
1. **TOV Brand Voice v2.0**: carismatico, diretto, sincero, semplice e chiaro, formazione. Vietato: tecnichese, storytelling melenso.
2. **Brand facts** (da `Materiale Agency - Diglital Empire.txt`): USP progetto-senza-abbonamenti,
   parte legata ai risultati, prima call gratuita con valore vero, "agenzia progettata per essere licenziata".
3. **QA finale**: A8 Copy Reviewer del motore + checklist TOV DE sopra. Score minimo 85.
