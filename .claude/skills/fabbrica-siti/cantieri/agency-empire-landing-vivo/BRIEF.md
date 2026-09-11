# BRIEF — cantiere «Sito Agency Vivo v2» su `agency-empire-landing` (Dossier 37 v2)

**Data apertura:** 2026-09-12 · **Via di Max:** «vai» (dopo «Emperator EMP-2AW3 — continua esattamente da dove ti sei
fermato» e «missione») · **Ripresa:** `EMP-2AW3` · **Piano:** `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` (V4 esecutivo, righe 280-373)

## IL SITO — confermato dal proprietario (gate F0, PM0)
> **Max, 2026-09-11 22:05:** *«Il sito della Agency era https://agency-empire-landing.vercel.app. Hai modificato un altro
> sito, rifai tutto il piano completamente.»*

- cartella: `agency-empire-landing/` · `.vercel/project.json` → `projectName: "agency-empire-landing"`,
  `projectId: prj_34bLuVZNA8iqh9t2MAaK2j7M9D0c` (letto il 2026-09-12)
- `npx vercel project ls` (2026-09-12): `agency-empire-landing → https://agency-empire-landing.vercel.app`, ultimo deploy **100 giorni fa**
  (il sorgente locale del 2026-09-02 non è mai stato deployato: il "prima" ufficiale è il live, LEZIONE v1 n.5)
- **l'altro sito** `agency-empire/` → `agency-empire-kohl.vercel.app` (progetto Vercel `digital-empire-leandingpagestudio`) è **CHIUSO**:
  F7 controlla che il suo H1 «Automatizziamo la tua operatività» resti online intatto
- live 200 (curl 2026-09-12) · Calendly `https://calendly.com/max-infoproducer/30min` → 200

## Corsia (CLAUDE-SITI §5)
**Corsia B — SITO.** Next.js 16.2.3 App Router + Tailwind v4 + Lenis + Framer Motion + GSAP, `output: "export"` (statico in `out/`),
`trailingSlash: true`, `basePath` opzionale per l'anteprima GitHub Pages (`GH_PAGES_BASE`). Non si riscrive in vanilla.

## Versione salvata (prima di toccare un file)
- tag `agency-empire-landing-v1-20260912` su origin (commit `8ed2ea6f`)
- zip sorgente `%TEMP%\agency-empire-landing-v1-20260912.zip` (579 KB, fuori repo)
- ripristino: `git checkout agency-empire-landing-v1-20260912 -- agency-empire-landing/`

## Il committente e il design (§4)
Committente = Digital Empire: vince il canone Empire con le due leggi di Max del 2026-09-11 (**grana su tutto, anche sulle sfumature**;
**ogni scritta su foto si legge sempre**, banda scura ≥ 7:1). Neri del sito vero: `#1c1c1c` / `#0a0a0a`. Tavola Estetica invariata:
https://claude.ai/code/artifact/f3fc31e1-b258-4be6-8074-341c021781c9

## Baseline misurata (F0) — live 2026-09-11 22:15, `capture/63-agency-landing-vero/`
**38.683 px** desktop · 64.255 mobile · **37 sezioni + 5 divider** · **10 CTA** · **0 fotografie** · 186 dimensioni · 42 sfondi ·
5 famiglie di gradiente · 880 blocchi · **noindex** (`layout.tsx:31`) · CTA chiamata in 3 salti col brand «Claude Code Mastery» ·
`#prenota` = ancora del listino · prezzi in 3 file · footer `href="#"`, `TODO(N1)` P.IVA/sede/PEC.

## Obiettivi del dopo (si misurano con lo stesso strumento, F5, DUE volte)
manifest **vuoto** (quello che va online il giorno del deploy) ≤ **21.000 px** desktop / 36.000 mobile ·
manifest **pieno** ≤ **24.000** / 40.000 · 20 sezioni + coda, 0 divider · 10 CTA tutte a `/prenota/` via `<Link>` ·
15 posti-foto con `alt` 15/15 e composizione B · ≤ 12 dimensioni · 3 sfondi + fascia · 0 famiglie di gradiente-card ·
0 placeholder / numeri senza fonte (`gate_fatti.py`) · `netlify.app` = 0 · `#prenota` = 0 · `href="#"` = 0 ·
home perf ≥ 85, a11y ≥ 95 · `/prenota/` perf ≥ 70, a11y ≥ 95 · 100% link 200 · noindex tolto nel commit di F7.

## Porta d'uscita (C1.1)
Tutte le CTA → `/prenota/` (pagina nostra, brand agenzia, Calendly inline caricato on demand, `?da=Nxx` → evento).
`src/lib/contatti.ts` è l'unica fonte di `PRENOTA` e `CALENDLY`. Sitemap a 4 URL: `/`, `/prenota/`, `/privacy/`, `/cookie/`.

## Analytics
`src/components/analytics.tsx` (dal wip): Vercel Web Analytics + `cta_click {sezione}` + `call_prenotata` (postMessage Calendly).
Vercel Web Analytics **si accende dal cruscotto** (gesto di Max, in STATO-EMPIRE, non blocca): il componente è muto finché non si accende.

## Gesti di Max — nessuno blocca (ADR-026/028)
ritratto suo (posto 1, 10) · ritratti Gael (11) e Leonardo (12) · Higgsfield per i 9 posti generati · screenshot dashboard (6) ·
`src` del video (N4) · P.IVA / sede / PEC (`legal.ts`) · consenso scritto Novacar / Preventa per il nome in N11 · Vercel Web Analytics.

## Deroghe dichiarate in apertura
- Lighthouse baseline sul live: non rifatta (la cattura 63 basta come "prima"; il "dopo" si misura in F6 sullo stesso URL).
- `canone_sync.py` confronta `canone.css`↔`canone.json` della Fabbrica, non un sito: il gate colore del sito è
  `gate_siti.py out/` + grep degli hex fuori canone in `src/` (F3).
