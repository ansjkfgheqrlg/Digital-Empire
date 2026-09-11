# BRIEF — cantiere «Sito Agency Vivo» (Dossier 37)

**Data apertura:** 2026-09-11 · **Via di Max:** «procedi, salva questa versione, ti do il via» ·
**Ripresa:** `EMP-ZP2J` · **Piano:** `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` (leggere fino al V4 esecutivo)

## Corsia (CLAUDE-SITI §5)
**Corsia B — SITO.** Motivo in una riga: il sito è già Next.js 16.2.3 App Router + Tailwind v4 + Lenis +
Framer Motion + GSAP, ha due route (`/`, `/prenota`) e un embed Calendly con stato lato client; riscriverlo
in vanilla sarebbe la direzione vietata (dal framework al vanilla si riscrive, mai si scende). I pattern
nuovi nascono comunque **prima in vanilla** nella Fabbrica e poi si avvolgono in componenti.

## Versione salvata (prima di toccare un file)
- tag `agency-empire-v1-20260911` · branch `agency-empire-v1` · entrambi su origin
- zip sorgente `C:\Users\Utente\Desktop\qui tutto\agency-empire-SNAPSHOT-v1-2026-09-11.zip` (fuori repo, 304 file)
- ripristino: `git checkout agency-empire-v1-20260911 -- agency-empire/`

## Il committente e il design (§4)
Committente = Digital Empire stessa: vince il canone Empire (`fabbrica-siti/canone/canone.css`) con le
due leggi di Max del 2026-09-11: **grana su tutto, anche sulle sfumature** (4 strati fissi + grana locale)
e **ogni scritta su foto si legge sempre** (banda scura ≥ 7:1). Riferimento visivo: la Tavola Estetica
(`cantiere/aura-preview/tavola-estetica-agency.html`, 10 tavole).

## Baseline misurata (F0)
- capture live (2026-09-11 19:55, `61-agency-baseline/`): **21.215 px** desktop · 32.482 mobile · **7 CTA** · 0 fotografie ·
  90 dimensioni tipografiche · 10 sfondi · 56 heading · 129 media (icone). **Il live è più corto del sorgente locale**
  (43.359 px, 21 sezioni): il deploy su Vercel è precedente all'ultimo restyling locale. Il "prima" ufficiale è il live.
- misure note dalla cattura del 2026-09-07 (`10-noi-post-restyling`): 43.359 px desktop · 70.173 mobile ·
  11 CTA · 0 fotografie · 195 dimensioni tipografiche · 48 sfondi · 125 heading
- footer: **nessuna P.IVA, indirizzo, privacy** — da inserire (dati di Max, non bloccano: `src/lib/legal.ts`
  stampa solo i campi presenti)

## Obiettivi del dopo (si misurano con lo stesso strumento)
≤ 24.000 px (il live + 13%, il sorgente locale − 45%) · 10 CTA a temperatura (dopo N1, N4, N5, N7, N8, N10, N12, N14, N16, N18) · 14 foto ·
≤ 12 dimensioni tipografiche · 3 sfondi + 1 fascia · 1 H1 · a11y ≥ 95 · perf mobile ≥ 85 · 100% link 200.

## Traffico e analytics
Due porte: chi cerca (home, calda) e chi clicca da un DM/email dell'outreach (pagina-ponte `/ponte`, F7.5,
solo se linkata dalla Bibbia dei Messaggi). Analytics: Vercel Web Analytics + eventi `cta_click`
(`{sezione}`) e `call_prenotata` (postMessage Calendly `calendly.event_scheduled`). Baseline sul vecchio
finché il nuovo non è in produzione.

## Immagini
Manifest: `public/aura/manifest.json` (41 file AURA + 3 non-AURA). In `public/aura/` entrano solo
`sorgente ∈ {generata, team, screenshot}`. Le originali vivono in `cantiere/aura-preview/` (gitignored) e
si vedono solo con `next dev` in locale. Swap = una riga del manifest.

## Ordine di costruzione (non si inverte)
F0 baseline → F1a copy N1-N9 + VOCE.md + gate_voce.py → F1b copy N10-N19 → F2 immagini → F3 pattern
vanilla + canone v3 **taggato** → F4 build 19 sezioni → F5 gate + misura → F6 test → F7 deploy → F7.5 ponte → F8 retro.

## Cosa dipende da Max (non blocca)
ritratto per l'hero (posto 1) · foto team (N11) · Higgsfield Plus per le 12 generate · P.IVA/indirizzo per il footer.
