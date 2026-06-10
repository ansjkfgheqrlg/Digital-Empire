# HANDOFF — Piattaforma Formazione Empire

**Ultimo aggiornamento:** 2026-05-01
**Working dir:** `c:/Users/Utente/Desktop/qui tutto/Digital Empire/Lancio corso skill beast/Sale pag/Siti CCM/formazione-empire`
**Stack:** Next.js 16.2.3 (Turbopack) · Tailwind v4 · Supabase (auth + DB) · Framer Motion · Lenis · Onest · lucide-react

---

## 1. Contesto strategico

L'utente sta lanciando **CCM = Claude Code Mastery**, il suo primo corso — ora brandizzato sulla piattaforma come **"Da AI User a System Architect"**. Il percorso completo di lancio include:

- Sale page CCM (già esistente, in `../ccm-premium/`)
- Piattaforma studenti = questo progetto `formazione-empire`
- VSL per sale page (da produrre, fuori scope tecnico)
- Canale YouTube + strategia contenuti (da produrre, fuori scope tecnico)

Questo HANDOFF copre SOLO la piattaforma `formazione-empire`.

---

## 2. Stato attuale (fine chat 2026-05-01)

### Fix critico — split data.ts / data.server.ts (2026-05-01)

Build error risolto: `next/headers imported in client component`.

**Causa:** `src/lib/data.ts` conteneva sia dati statici (importati da client components) sia funzioni async Supabase che usavano `next/headers`. Il bundler tirava dentro l'import server-only anche nei bundle client.

**Fix applicato:**
- `src/lib/data.ts` — ora contiene SOLO: tipi TypeScript, dati mock statici (`ccmCourse`, `vetrinaCourses`, `mockStudent`), funzioni sincrone (`getCourse`, `getModule`, `getLesson`, `getCourseProgress`, `getModuleProgress`). Nessun import server.
- `src/lib/data.server.ts` — **NUOVO FILE** — contiene tutte le funzioni async Supabase: `fetchCourse`, `fetchModule`, `fetchLesson`, `fetchCourseProgress`, `getEnrolledCourses`. Import server-only confinati qui. Mapping helpers DB→TS anche qui.

**Import aggiornati (→ data.server):**
- `src/app/admin/corsi/[courseSlug]/page.tsx` — `fetchCourse`
- `src/app/corsi/[courseSlug]/moduli/[moduleSlug]/[lessonSlug]/page.tsx` — `fetchLesson`
- `src/app/dashboard/page.tsx` — `getEnrolledCourses`, `fetchCourseProgress` (+ `vetrinaCourses` rimane da `data`)

**Regola da rispettare:** qualsiasi nuova funzione async che usa `createClient()` va in `data.server.ts`, non in `data.ts`.

### Supabase project status (2026-05-01)

Il progetto Supabase `fytrvrsaaubqrfmqbkhn` era in **pausa** (paused il 26 Apr 2026, free tier auto-pause). Scade il 25 Jul 2026. L'utente deve cliccare "Resume project" dal dashboard Supabase prima di testare qualsiasi flusso auth/DB. Le credenziali in `.env.local` sono corrette, non toccare.

---

## 2b. Stato attuale (fine chat 2026-04-20)

### Rinomina corso completa
Tutto il corso CCM è stato rinominato in **"Da AI User a System Architect"** (tagline: _"Il percorso completo Empire"_). Aggiornato in:
- `src/lib/data.ts` linea ~195 (title, tagline)
- `src/app/admin/studenti/page.tsx` (dropdown filter "Tutti i corsi")
- `src/components/sections/landing-hero.tsx` (marquee border-top)
- `src/app/layout.tsx` (meta description)

Slug URL rimane `claude-code-mastery` (non cambiare — rotte interne + link esterni).

### Regola UI non negoziabile — NIENTE dark-on-dark
L'utente ha chiesto ripetutamente durante queste 2 chat di eliminare **ogni card / form / pannello scuro** su fondo scuro. Ogni blocco su `bg-ink` / `bg-ink-2` / `#1c1c1c` / `#2a2a2a` DEVE essere riempito di argento (silver gradient) con testo scuro.

Classi CSS pronte in `src/app/globals.css`:
- `.card-fill-silver` — card neutra silver, testo `#13111a`, accent `#8a2a05`/`#c9370a`
- `.card-fill-silver-orange` — card featured silver + gradient arancione, con sub-class `.progress-track-dark` / `.progress-fill-dark`
- `.silver-chip` — chip fluttuante piccolo argento

Override CSS aggiunti in `globals.css` (dopo `.card-fill-silver:hover .link-orange-dark`) per quando i seguenti stanno DENTRO una `.card-fill-silver*`:
- `.eyebrow-silver-orange` → gradient orange deep scuro leggibile
- `.text-silver-white` → gradient dark leggibile
- `.text-silver-soft` / `.text-silver-mute` / `.text-silver-dim` → toni scuri
- `.field-silver` / `.field-silver-label` / `.field-silver-hint` → bg chiaro, testo scuro
- `.link-silver-orange` → gradient orange scuro

### Conversioni silver-fill già eseguite

| File | Da | A |
|------|-----|-----|
| `src/components/sections/landing-courses.tsx` | `card-dark` | `card-fill-silver` (in arrivo) + `card-fill-silver-orange` (CCM available) |
| `src/app/dashboard/page.tsx` | card scura "Corso in corso" + `card-dark` vetrina | `card-fill-silver-orange` featured + `card-fill-silver` vetrina |
| `src/app/(auth)/login/page.tsx` | wrapper dark gradient | `card-fill-silver` |
| `src/app/(auth)/signup/page.tsx` | wrapper dark gradient | `card-fill-silver` |
| `src/app/(auth)/signup/signup-form.tsx` | success box dark + error box rosso scuro | success box silver+orange chiaro + error box rosso chiaro |
| `src/app/(auth)/login/login-form.tsx` | error box rosso scuro | error box rosso chiaro |

**Build verificato OK** (`npm run build` — 2026-04-20, tutte le 12 pagine generate, nessun errore TS/lint).

### Hero corso `/corsi/[courseSlug]`

`src/app/corsi/[courseSlug]/page.tsx` + `src/components/course-banner-hero.tsx`:
- Sfondo pagina corso: bianco-argento con macchie arancione (4 layer `position: fixed z-index 101-103`, content z-index 120).
- Hero = sezione NERA compatta in alto: title "Da AI User a **Architect**" (silver-white + silver-orange italic), subtitle, 5 SilverChip floating (moduli / lezioni / durata / risorse / % completato), CTA btn-orange "Riprendi/Inizia il corso" + ghost "Esplora i moduli".
- Sotto hero: accordion moduli, sezione "Risorse premium" nera.

### Bug noti / trappole ricorrenti

1. **`.grain-fine` body pseudo z-index:100 fixed**
   - `src/app/layout.tsx` body ha class `grain-fine`. In `globals.css`, `.grain-fine::before` e `.grain-fine::after` sono `position: fixed; inset: -50%; z-index: 100`.
   - Qualsiasi pagina con background custom DEVE usare 1+ layer `position: fixed; z-index: ≥101` per dipingere sopra la grana, e content `position: relative; z-index: ≥120`.
   - **Non rimuovere `grain-fine` dal body** — serve ad altre pagine (homepage, dashboard, auth).

2. **`mix-blend-mode: multiply` con opacity alta uccide il colore**
   - Su layer grana, multiply con opacity >0.15 rende tutto grigio. Tenere overlay dominante e multiply ≤0.10.

3. **`card-dark` su bg dark = bug ripetuto**
   - Grep periodico per `card-dark` dentro `src/app/**/page.tsx` e componenti. Se è su bg scuro → sostituire con `card-fill-silver` o `card-fill-silver-orange`.

---

## 3. Piano residuo — AGGIORNATO 2026-05-05

### Audit completato (2026-05-05)

**Grep card-dark `src/app/corsi/**`** → ZERO match. ✓
**Grep card-dark `src/components/**`** → 2 residui solo sulla landing homepage (`landing-faq.tsx:55`, `landing-method.tsx:52`) — fuori scope lancio.
**Lesson page audit** → PULITA. description card + ResourceCard + nav prev/next usano tutti silver gradient. Nessun dark-on-dark reale.
**Video player** → funzionante. Gap: wrapper YouTube manca `background: #0a0a0a` (flash bianco al caricamento); placeholder minimale da polish.

### Tasks aperte — ordine d'attacco

- [ ] **P1** `src/components/lesson-drawer.tsx` — audit visivo completo + card-dark check
- [ ] **P1** `src/components/sticky-progress-bar.tsx` — audit visivo + card-dark check
- [ ] **P2** `src/components/video-player.tsx` — aggiungere `background: '#0a0a0a'` al wrapper YouTube; polish placeholder; il glow orange esterno è già nel wrapper di `page.tsx` (righe 71–85)
- [ ] **P3** `src/app/corsi/[courseSlug]/moduli/[moduleSlug]/page.tsx` — redirect server-side al primo lesson del modulo
- [ ] **P4** `src/components/student-header-client.tsx` + `src/components/admin-shell.tsx` — verificare assenza card-dark
- [ ] **P5** `src/lib/data.ts` — popolare campo `cover` per tutti i corsi
- [ ] **BASSA** `src/components/sections/landing-faq.tsx:55` + `landing-method.tsx:52` — card-dark sulla homepage (post-lancio)

---

## 4. Convenzioni chiave del codebase

### Token colori (da `globals.css`)
- `#fb4604` orange-pure · `#ff6a2e` orange-bright · `#c9370a` orange-deep · `#8a2a05` orange deep (eyebrow on silver)
- `#fafafa` paper · `#e8e8e6` grey · `#0a0a0a` ink-2 · `#1c1c1c` ink · `#2a2a2a` body
- `#13111a` dark text on silver · `rgba(19,17,26,0.72)` body text on silver
- Silver gradient base: `linear-gradient(135deg, #ffffff 0%, #e8e3ef 25%, #d9d4e1 45%, #8a8594 100%)`
- Silver+orange gradient: `linear-gradient(135deg, #ffffff 0%, #ece7f1 18%, #d9d4e1 38%, #ffb78a 70%, #ff8a4a 88%, #fb4604 100%)`

### Sezioni pattern
- Marquee border-t in ogni hero dark
- 4 `silver-chip float-a/b/c/d` fluttuanti in hero ampie
- `bubble-orange` come eyebrow primario
- `pre-headline` con 2 trattini laterali
- H1/H2 sempre mix: `text-silver-white` + `text-silver-orange` (dark) o colore scuro + `text-orange-pure italic` (silver/paper)
- CTA = `btn-orange` con `ArrowRight` icon
- `<Reveal delay={0}/0.1/0.2/0.3>` su ogni blocco principale

### Struttura rotte
- `/` — landing marketing
- `/login` + `/signup` — auth Supabase (form silver-fill)
- `/dashboard` — hub studente (welcome + corso in corso + vetrina)
- `/corsi/[courseSlug]` — course page (hero nero + accordion moduli)
- `/corsi/[courseSlug]/moduli/[moduleSlug]/[lessonSlug]` — pagina lezione
- `/admin/**` — backoffice (studenti, corsi, risorse, impostazioni)
- `/auth/callback` — Supabase auth redirect

---

## 5. Dev commands

```bash
cd "c:/Users/Utente/Desktop/qui tutto/Digital Empire/Lancio corso skill beast/Sale pag/Siti CCM/formazione-empire"
npm run dev      # http://localhost:3000
npm run build    # verifica tipi + lint + pages
```

Rotte chiave da testare visivamente ad ogni modifica:
- `http://localhost:3000/` — landing (verifica card corsi silver)
- `http://localhost:3000/login` — form silver
- `http://localhost:3000/signup` — form silver
- `http://localhost:3000/dashboard` — (serve login Supabase) featured silver+orange card
- `http://localhost:3000/corsi/claude-code-mastery` — hero nero + accordion

---

## 6. PROMPT DA INCOLLARE NELLA PROSSIMA CHAT

```
Continuiamo lo sviluppo della piattaforma Formazione Empire in:
c:/Users/Utente/Desktop/qui tutto/Digital Empire/Lancio corso skill beast/Sale pag/Siti CCM/formazione-empire

Prima di toccare qualsiasi cosa leggi questi file per assorbire tutto lo stato:
1. HANDOFF.md (nella root del progetto) — sezioni 2, 2b, 3, 4 sono le più critiche
2. C:/Users/Utente/.claude/projects/c--Users-Utente-Desktop-qui-tutto-Digital-Empire-Lancio-corso-skill-beast-Sale-pag-Siti-CCM/memory/formazione-empire-stato-ui.md
3. C:/Users/Utente/.claude/projects/c--Users-Utente-Desktop-qui-tutto-Digital-Empire-Lancio-corso-skill-beast-Sale-pag-Siti-CCM/memory/formazione-empire-stack.md

ARCHITETTURA DATA LAYER (critico — non rompere):
- src/lib/data.ts → tipi + dati statici + funzioni SINCRONE (usabile da client components)
- src/lib/data.server.ts → funzioni async Supabase (fetchCourse, fetchLesson, getEnrolledCourses, ecc.)
  Solo i server components importano da data.server.ts.
Mai mettere import da "@/lib/supabase/server" dentro data.ts.

SUPABASE: il progetto era in pausa. Se vedi "fetch failed" all'auth, vai su
supabase.com/dashboard e clicca Resume sul progetto formazione-empire.
Le credenziali in .env.local sono già corrette.

REGOLA UI NON NEGOZIABILE: zero dark-on-dark.
Ogni card/form/pannello su fondo scuro DEVE usare .card-fill-silver o .card-fill-silver-orange.
Mai .card-dark su bg-ink / bg-ink-2 / #1c1c1c / #2a2a2a.

Il corso si chiama "Da AI User a System Architect", slug URL: claude-code-mastery.

STATO AUDIT (già eseguito — non ripetere):
- src/app/corsi/** → zero card-dark. ✓
- Lesson page → PULITA, nessun dark-on-dark. ✓
- 2 card-dark residui in landing-faq.tsx:55 e landing-method.tsx:52 → bassa urgenza (homepage)
- video-player.tsx → funzionale, manca background sul wrapper YouTube

PIANO RESIDUO (attacca in questo ordine senza aspettare):
P1 — Leggi src/components/lesson-drawer.tsx e src/components/sticky-progress-bar.tsx,
     fai audit visivo, correggi eventuali dark-on-dark.
P2 — Fixa src/components/video-player.tsx:
     aggiungere background: '#0a0a0a' al wrapper div YouTube (flash bianco),
     polish del placeholder state.
P3 — src/app/corsi/[courseSlug]/moduli/[moduleSlug]/page.tsx →
     redirect server-side al primo lesson del modulo.
P4 — Controlla src/components/student-header-client.tsx e src/components/admin-shell.tsx
     per card-dark.

Esegui P1 e P2 in parallelo, poi P3 e P4. Poi dammi un recap e aspetta.
```

---

## 7. File chiave (riferimento rapido)

**Globale:**
- `src/app/layout.tsx` — body `grain-fine` (non toccare)
- `src/app/globals.css` — tutti i token + utility class (ultimo blocco: override silver-fill per form/testi)
- `src/lib/data.ts` — mock corsi/moduli/lezioni (title CCM già rinominato)

**UI già silver-fill (OK):**
- `src/components/sections/landing-courses.tsx`
- `src/app/dashboard/page.tsx`
- `src/app/(auth)/login/page.tsx` + `login-form.tsx`
- `src/app/(auth)/signup/page.tsx` + `signup-form.tsx`

**Hero corso (OK recentemente):**
- `src/components/course-banner-hero.tsx` (hero nero compatto + SilverChip row)
- `src/app/corsi/[courseSlug]/page.tsx` (bg bianco-argento 4 layer fixed)

**Da ispezionare/rifinire:**
- `src/app/corsi/[courseSlug]/moduli/[moduleSlug]/[lessonSlug]/page.tsx`
- `src/components/video-player.tsx`
- `src/components/lesson-drawer.tsx`
- `src/components/sticky-progress-bar.tsx`
- `src/components/modules-accordion.tsx`
- `src/components/student-header-client.tsx`
- `src/components/admin-shell.tsx`

---

## 8. Storia delle iterazioni chiave (per capire il "perché")

- **Iter 1** — piano ridisegno course page (file `~/.claude/plans/partitioned-sprouting-hearth.md`): accordion inline moduli, hero banner, sticky progress, video page verticale, lesson drawer.
- **Iter 2** — bg pagina corso: lunga battaglia tra body `#2a2a2a + grain-fine::before/::after` (z-index 100) e tentativo di bg bianco-argento. Risolto con 4 layer `position: fixed z-index 101-103` + content z-index 120.
- **Iter 3** — hero banner troppo grande / rosso acceso: riscritto come sezione NERA compatta con SilverChip row. Stesso momento: rinomina corso → "Da AI User a System Architect".
- **Iter 4** (questa chat, pre-compact) — utente segnala che **tanti** altri blocchi sono ancora dark-on-dark (landing cards, dashboard CCM card, login, signup). Convertiti tutti a silver-fill. Build passa.

La regola "silver-on-dark" deve guidare ogni prossima modifica.
