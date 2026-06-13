# WF-LANDING-RAPIDA — Landing Singola < 48 ore

> **Fast-track:** landing page singola da zero al deploy in meno di 48 ore. Usa `market-landing` per il copy e `site-premium-stack` per il build. Gate ridotti ma non eliminati.

## Trigger
- AGENCY ha lead caldo che chiede mockup/landing entro 48h
- INFO-BUSINESS vuole landing di pre-lancio o sales page urgente
- MARKETING ha bisogno di landing per campagna ads con deadline stretta

## Input
```json
{
  "obiettivo_landing": "lead gen / vendita diretta / pre-lancio / waitlist",
  "prodotto_servizio": "cosa viene venduto/presentato",
  "icp": "a chi è rivolta",
  "copy_disponibile": "già scritto / da generare con market-landing",
  "deadline_ore": "massimo 48",
  "brand_kit": "esistente o DE standard"
}
```

## Pipeline (Passi)

### Ora 0-4 — SETUP & COPY
```
plt-cc-master riceve brief
plt-site-architect: architettura semplificata (1 pagina, max 6 sezioni)
  → struttura fissa: Hero → Problem/Pain → Solution → Social Proof → CTA → FAQ

SE copy non disponibile:
  → market-landing (skill MARKETING): genera copy APSOC per la landing
  → copy review da plt-site-copy-merger (consistenza brand)

plt-site-builder: setup repo Next.js 15/16 + Tailwind v4 (template landing base)
  → usa site-premium-stack per scaffold rapido
```

### Ora 4-16 — BUILD
```
plt-site-builder: costruisce 6 sezioni (componenti predefiniti DE)
  → Hero con CTA primaria
  → Sezione pain/problem
  → Sezione soluzione + benefici
  → Social proof (testimonial, numeri, loghi)
  → CTA finale
  → FAQ accordion

plt-site-copy-merger: integra copy nelle sezioni
plt-seo-tech: meta title, description, OG (base — no JSON-LD esteso)
plt-motion-eng: scroll reveal Framer Motion (light touch — no Three.js)
```

### Ora 16-24 — GATE G-SEC (fast track)
```
plt-sec-sentinel: scan fast (focus su: no secret, no PII form, CSRF form action)
  → landing senza autenticazione = profilo rischio basso
  → scansione < 15 min
  → se verde → G-QA
```

### Ora 24-36 — GATE G-QA (fast track)
```
plt-qa-runner: playwright-dev (1 pagina → test CTA, form, mobile 375px)
  → verify: npm run build verde
  → Lighthouse performance ≥ 85 (soglia ridotta per velocità, 90 target comunque)
  → G-BRAND: plt-director check rapido stile
```

### Ora 36-48 — DEPLOY
```
plt-deploy-op: vercel:deploy + smoke test
  → smoke: HTTP 200 + CTA cliccabile + form submit funzionante
plt-custodian: registro nel registry (entry rapida)
OPERATIONS: evento costo
```

## Gate
| Gate | Owner | Criterio (fast track) |
|---|---|---|
| G-SPEC | plt-cc-master | Struttura 6 sezioni approvata (no plt-director se scope è standard) |
| G-SEC | plt-sec-sentinel | 0 secret, 0 PII esposti — scan < 15 min |
| G-QA | plt-qa-runner | Build verde, mobile ok, CTA funzionante, Lighthouse ≥ 85 |
| G-DEPLOY | plt-deploy-op | Smoke test verde, URL live |

**Nota:** G-BRAND è semplificato (check visivo < 10 min). Se il cliente chiede deviazioni significative dallo stile DE → escalation a plt-director che può estendere la timeline (non più WF-LANDING-RAPIDA).

## Output
- Landing page live su Vercel (URL consegnato entro 48h)
- Repo nel registry PLATFORM
- Report QA one-pager
- Evento costo per OPERATIONS

## Owner Agente
`plt-cc-master` — tutta la pipeline. Per scope standard non richiede plt-director.

## Skill Usate
`market-landing` · `site-premium-stack` · `site-build` · `site-components` · `site-copy` · `site-animate` (light) · `site-seo` (base) · `site-qa` · `playwright-dev` · `verify` · `security-review` · `vercel:deploy`
