# REF_06 — Tech Stack Combinations per SaaS 2025

> Documento di riferimento per PRD Architect OS — Validazione e selezione tech stack.
> Usato durante la generazione della sezione "Technical Architecture" nei PRD Tipo C e D.

---

## Come scegliere il tech stack per un PRD

La scelta dello stack è una decisione architetturale con impatto diretto su velocità di lancio, costo operativo e scalabilità futura. Un PRD ben fatto non lascia questa scelta al caso: documenta lo stack scelto e giustifica il perché.

### Criteri di valutazione (in ordine di priorità)

| Criterio | Domanda da porsi | Peso |
|---|---|---|
| **Team skill** | Il team sa usarlo? Quanto tempo ci vuole per imparare? | Alto |
| **Time-to-MVP** | Quanto tempo per avere la prima versione funzionante? | Alto |
| **Costo operativo** | Quanto costa a 0, 1K e 10K utenti? | Medio-Alto |
| **Scalabilità** | Regge la crescita senza riscrivere tutto? | Medio |
| **Ecosystem** | Ci sono librerie, template, community per questo stack? | Medio |
| **Vendor lock-in** | Quanto è difficile migrare via se necessario? | Basso-Medio |

### Regola base

> **Non scegliere lo stack più potente. Scegli lo stack che il tuo team riesce a shippare più velocemente con il budget disponibile.**

Un'app in Next.js + Supabase shippata in 3 settimane batte un'architettura microservizi teoricamente perfetta che ci vuole 6 mesi.

---

## Le 10 Combinazioni Tech Stack

---

### Stack 1 — Next.js + Supabase + Vercel

**Il più popolare per vibe coding e indie SaaS nel 2025.**

**Componenti completi:**
- **Frontend**: Next.js 14+ (App Router, React Server Components)
- **Backend**: Next.js API Routes + Supabase Edge Functions
- **Database**: PostgreSQL gestito da Supabase (row-level security nativo)
- **Auth**: Supabase Auth (email, OAuth, magic link)
- **Payments**: Stripe (via webhook + Supabase)
- **Hosting**: Vercel (frontend + API) + Supabase (DB + storage)
- **AI Layer**: Vercel AI SDK + OpenAI / Anthropic

**Profilo ideale:**
- Vibe coder solo o duo
- Developer JavaScript/TypeScript con esperienza React
- Startup early-stage che vuole validare velocemente
- Prodotti B2C e B2B SMB senza compliance estrema

**Time-to-MVP stimato:** 1-3 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier (fino a 500MB DB, 2 progetti) | €0 |
| 1.000 utenti attivi | €25-50/mese |
| 10.000 utenti attivi | €100-200/mese |

**Pro:**
- Documentazione eccellente, template infiniti su GitHub
- Supabase gestisce auth + DB + storage + realtime in un solo servizio
- Vercel deploy automatico da Git, zero config
- Row-Level Security di PostgreSQL elimina logica di autorizzazione custom

**Contro:**
- Vendor lock-in su Supabase (migrazione complessa)
- Cold start su Vercel Serverless per API complesse
- Supabase free tier ha limiti di connessioni DB

**Use case ideale:** SaaS tools, dashboard analytics, app di produttività, piattaforme di contenuto B2B SMB.

**Prodotti noti che usano questo stack (o stack simile):**
- Vercel (parzialmente)
- Numerous.ai
- La maggior parte dei boilerplate SaaS 2024-2025 (ShipFast, Makerkit, SaaStr Starter)

---

### Stack 2 — Next.js + Prisma + PlanetScale + Vercel

**Il classico MySQL cloud per chi preferisce ORM tipizzato.**

**Componenti completi:**
- **Frontend**: Next.js 14+ (App Router)
- **Backend**: Next.js API Routes + tRPC (opzionale)
- **Database**: MySQL gestito da PlanetScale (branching DB)
- **ORM**: Prisma (type-safe, migrazioni)
- **Auth**: NextAuth.js / Auth.js
- **Payments**: Stripe
- **Hosting**: Vercel
- **AI Layer**: OpenAI API diretta o Vercel AI SDK

**Profilo ideale:**
- Developer con background PHP/MySQL o Laravel
- Team 2-4 persone con workflow Git-based
- Prodotti con schema dati relazionale complesso
- Team che vuole DB branching per staging/produzione separati

**Time-to-MVP stimato:** 2-4 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier (Hobby plan PlanetScale) | €0 |
| 1.000 utenti attivi | €30-60/mese |
| 10.000 utenti attivi | €150-300/mese |

**Pro:**
- Prisma genera tipi TypeScript dal schema DB (zero errori runtime)
- PlanetScale branching = deploy DB sicuri senza downtime
- Ecosystem maturo, tutorial ovunque
- NextAuth supporta 50+ provider OAuth out of the box

**Contro:**
- PlanetScale ha chiuso il free plan nel 2024 (ora Hobby a pagamento)
- Setup iniziale più lento rispetto a Supabase
- Prisma aggiunge latenza nelle query (ORM overhead)

**Use case ideale:** CRM, project management tool, piattaforme con dati relazionali complessi (multi-tenant, relazioni many-to-many).

**Prodotti noti:** Cal.com (open source, stack simile), Papermark

---

### Stack 3 — Remix + Supabase + Fly.io

**SSR-first, edge-first, per chi vuole performance massima.**

**Componenti completi:**
- **Frontend**: Remix (full-stack, loader/action pattern)
- **Backend**: Remix server routes (loaders + actions)
- **Database**: PostgreSQL via Supabase o Neon
- **Auth**: Supabase Auth o Remix Auth
- **Payments**: Stripe
- **Hosting**: Fly.io (container Docker, regioni globali)
- **AI Layer**: OpenAI / Anthropic API

**Profilo ideale:**
- Developer avanzato con focus su web performance
- Team 2-5 persone con esperienza DevOps
- Prodotti con SEO critico (e-commerce, marketplace contenuti)
- App con heavy server-side logic

**Time-to-MVP stimato:** 3-5 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier (Fly.io machines piccole) | ~€5/mese |
| 1.000 utenti attivi | €40-80/mese |
| 10.000 utenti attivi | €150-400/mese |

**Pro:**
- Performance superiore: nessun hydration mismatch, tutto SSR
- Fly.io deploy vicino agli utenti (edge deployment globale)
- Remix error boundaries e data loading pattern molto puliti
- Ottimo per app con molte route dinamiche

**Contro:**
- Curva di apprendimento Remix più ripida di Next.js
- Comunità più piccola, meno template disponibili
- Fly.io richiede più configurazione rispetto a Vercel

**Use case ideale:** Marketplace, piattaforme di contenuto con SEO, app con tantissime route dinamiche.

**Prodotti noti:** Shopify (ha contribuito a Remix), Epic Stack di Kent C. Dodds

---

### Stack 4 — SvelteKit + PocketBase + Railway

**Il più leggero. Perfetto per tool interni e prodotti con budget €0.**

**Componenti completi:**
- **Frontend**: SvelteKit (SSR + SPA, framework Svelte)
- **Backend**: SvelteKit endpoints + PocketBase API
- **Database**: SQLite gestito da PocketBase (embedded)
- **Auth**: PocketBase Auth nativo (email, OAuth)
- **Payments**: Stripe (manuale via webhook)
- **Hosting**: Railway (container Docker, PocketBase self-hosted)
- **AI Layer**: OpenAI API o Ollama (locale)

**Profilo ideale:**
- Solo developer o micro-team
- Prodotti interni, admin panel, dashboard
- Progetti con budget operativo minimo
- Developer che preferisce Svelte per la sintassi più pulita

**Time-to-MVP stimato:** 1-2 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier (Railway Hobby) | €5/mese (crediti inclusi) |
| 1.000 utenti attivi | €10-20/mese |
| 10.000 utenti attivi | €30-80/mese |

**Pro:**
- PocketBase = backend completo in un singolo file Go (auth + DB + API + UI admin)
- Svelte genera bundle JavaScript minuscoli (performance eccellente)
- Costo operativo bassissimo
- Setup in meno di 30 minuti per un CRUD completo

**Contro:**
- SQLite non scala facilmente oltre 1-2M record senza tuning
- PocketBase ha meno estensioni e plugin rispetto a Supabase
- Svelte ha ecosistema più piccolo di React

**Use case ideale:** Tool interni, MVP rapidi, admin dashboard, prodotti con utenti limitati (<10K).

**Prodotti noti:** Numerosi tool interni aziendali, SaaS micro indie

---

### Stack 5 — Next.js + Django REST + PostgreSQL + AWS

**Per chi vuole Python backend con frontend React moderno.**

**Componenti completi:**
- **Frontend**: Next.js (App Router, client-side fetching da Django API)
- **Backend**: Django + Django REST Framework (API RESTful)
- **Database**: PostgreSQL su AWS RDS
- **Auth**: Django Allauth + JWT (djangorestframework-simplejwt)
- **Payments**: Stripe via Django (django-stripe)
- **Hosting**: AWS (EC2 o ECS per Django, Vercel per Next.js, RDS per DB)
- **AI Layer**: OpenAI SDK per Python, LangChain

**Profilo ideale:**
- Team con background Python/Django
- Prodotti con logica business complessa (calcoli, ML pipeline)
- Startup con developer fullstack Python
- SaaS con compliance e audit log richiesti

**Time-to-MVP stimato:** 4-8 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier (AWS Free Tier 12 mesi) | €0 (primo anno) |
| 1.000 utenti attivi | €50-100/mese |
| 10.000 utenti attivi | €200-600/mese |

**Pro:**
- Django admin genera UI backoffice completa in automatico
- Python ecosistema ML/AI nativo (scikit-learn, pandas, etc.)
- PostgreSQL su RDS = scalabilità enterprise
- Maturità: Django esiste dal 2005, tutte le edge case sono risolte

**Contro:**
- Setup e deploy più complesso (2 servizi separati da orchestrare)
- Costo AWS cresce rapidamente con il traffico
- Overhead di sviluppo maggiore rispetto a Supabase
- Più lento da iterare rispetto agli stack full-JS

**Use case ideale:** SaaS con logica business complessa, prodotti con ML integrato, fintech, healthtech con compliance.

**Prodotti noti:** Instagram (Django originariamente), Disqus, Eventbrite

---

### Stack 6 — React + FastAPI + Supabase + Railway

**Python API moderno, veloce, con DB gestito.**

**Componenti completi:**
- **Frontend**: React (Vite o Create React App)
- **Backend**: FastAPI (Python, async, OpenAPI auto-generata)
- **Database**: PostgreSQL via Supabase (solo DB, senza auth Supabase)
- **Auth**: FastAPI + JWT personalizzato o Supabase Auth
- **Payments**: Stripe via Python SDK
- **Hosting**: Railway (FastAPI containerizzato) + Vercel (React)
- **AI Layer**: OpenAI Python SDK, LangChain, LlamaIndex

**Profilo ideale:**
- Developer Python che non vuole Django (troppo opinionated)
- Prodotti con API-first design (consumati anche da mobile)
- AI-heavy products con pipeline Python
- Team che ama la documentazione automatica di FastAPI

**Time-to-MVP stimato:** 3-6 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier | €5-10/mese (Railway) |
| 1.000 utenti attivi | €40-80/mese |
| 10.000 utenti attivi | €150-350/mese |

**Pro:**
- FastAPI genera documentazione Swagger/OpenAPI automatica
- Async nativo = performance eccellente per AI workloads
- Python per backend = integrazione nativa con librerie ML/AI
- Validazione dati con Pydantic (type-safe)

**Contro:**
- Due servizi separati da deployare e monitorare
- FastAPI meno "batteries included" di Django
- Più configurazione manuale rispetto a stack full-JS

**Use case ideale:** AI tools, API-first SaaS, prodotti con heavy data processing.

**Prodotti noti:** Numerosi AI startup 2023-2025, tool di automazione

---

### Stack 7 — Next.js + tRPC + Prisma + PlanetScale

**Type-safety end-to-end senza REST né GraphQL.**

**Componenti completi:**
- **Frontend**: Next.js (App Router)
- **Backend**: tRPC (procedure chiamate direttamente dal frontend, type-safe)
- **ORM**: Prisma (schema → tipi TypeScript automatici)
- **Database**: MySQL su PlanetScale o PostgreSQL su Neon
- **Auth**: NextAuth.js / Auth.js
- **Payments**: Stripe
- **Hosting**: Vercel
- **AI Layer**: Vercel AI SDK

**Profilo ideale:**
- Team TypeScript avanzato
- Prodotti con codebase grande e complessa
- Team che vuole eliminare completamente i bug di tipo API
- Developer che odiano scrivere e mantenere client API REST

**Time-to-MVP stimato:** 3-5 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier | €0 (Neon free tier) |
| 1.000 utenti attivi | €30-60/mese |
| 10.000 utenti attivi | €150-300/mese |

**Pro:**
- Zero errori di tipo tra frontend e backend: il compilatore li trova tutti
- Nessun codice di serializzazione/deserializzazione da scrivere
- Refactoring sicuro: se cambi la procedura, TypeScript segnala tutti i punti rotti
- Ottimo per team grandi con molti developer

**Contro:**
- tRPC non è standard REST → difficile integrare client mobile o terze parti
- Curva di apprendimento per chi viene da REST/GraphQL
- Overhead concettuale iniziale

**Use case ideale:** SaaS con codebase grande, prodotti B2B con molte feature, team 3+ developer TypeScript.

**Prodotti noti:** t3.gg (il boilerplate di riferimento), Cal.com

---

### Stack 8 — Nuxt.js + Strapi + PostgreSQL + DigitalOcean

**Vue.js + headless CMS per prodotti content-heavy.**

**Componenti completi:**
- **Frontend**: Nuxt.js 3 (Vue 3, SSR/SSG)
- **Backend/CMS**: Strapi (headless CMS, API REST + GraphQL auto-generate)
- **Database**: PostgreSQL su DigitalOcean Managed Databases
- **Auth**: Strapi Users & Permissions plugin
- **Payments**: Stripe via Strapi plugin
- **Hosting**: DigitalOcean App Platform (Nuxt + Strapi) o Droplets
- **AI Layer**: OpenAI API via plugin Strapi o Nuxt server routes

**Profilo ideale:**
- Team Vue.js o developer che preferisce Vue a React
- Prodotti con gestione contenuti centrale (blog, docs, media)
- Marketing team che vuole modificare contenuti senza developer
- Agenzia che fa prodotti per clienti non-tecnici

**Time-to-MVP stimato:** 3-6 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier | Limitato (DigitalOcean non ha free tier robusto) |
| 1.000 utenti attivi | €50-100/mese |
| 10.000 utenti attivi | €200-500/mese |

**Pro:**
- Strapi admin panel = CMS potente per non-developer
- Nuxt eccellente per SEO (SSR/SSG nativo)
- DigitalOcean pricing prevedibile (non a sorpresa come AWS)
- API REST e GraphQL generate automaticamente da Strapi

**Contro:**
- Strapi richiede un server Node.js sempre attivo (no serverless)
- DigitalOcean più costoso di Vercel + Supabase per traffico basso
- Ecosistema Vue più piccolo di React

**Use case ideale:** Piattaforme editorial, siti corporate con sezioni app, marketplace con catalogo prodotti.

**Prodotti noti:** Numerosi siti editorial e corporate su Strapi + Nuxt

---

### Stack 9 — React Native + Expo + Supabase

**Mobile-first cross-platform (iOS + Android) con backend cloud.**

**Componenti completi:**
- **Frontend Mobile**: React Native con Expo (iOS + Android da unica codebase)
- **Backend**: Supabase (Edge Functions per logica server)
- **Database**: PostgreSQL via Supabase
- **Auth**: Supabase Auth (supporta deep linking per OAuth mobile)
- **Payments**: RevenueCat (abbonamenti IAP) + Stripe (web payments)
- **Hosting**: Expo EAS Build (compilazione cloud) + Supabase
- **AI Layer**: OpenAI API via Supabase Edge Functions

**Profilo ideale:**
- Prodotto mobile come core (non web + mobile opzionale)
- Developer JavaScript con esperienza React
- App consumer B2C, fitness, productivity, social
- Team che vuole evitare Objective-C / Swift / Kotlin

**Time-to-MVP stimato:** 4-8 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier (Expo free, Supabase free) | €0 |
| 1.000 utenti attivi | €25-60/mese |
| 10.000 utenti attivi | €100-250/mese + RevenueCat ~€80 |

**Pro:**
- Una codebase per iOS e Android (risparmio enorme)
- Expo OTA updates: aggiorna l'app senza passare per App Store review
- Supabase Realtime funziona perfettamente con React Native
- RevenueCat gestisce tutta la complessità degli abbonamenti IAP

**Contro:**
- Performance inferiore a app native per animazioni complesse
- Alcune librerie native richiedono "ejecting" da Expo
- Review App Store / Google Play aggiunge 1-7 giorni al ciclo di rilascio

**Use case ideale:** App consumer mobile-first, tool di produttività personale, app fitness/wellness, social app.

**Prodotti noti:** Molte app indie su Expo, Universi (parzialmente)

---

### Stack 10 — Next.js + Convex + Clerk + Stripe

**Real-time first, auth semplificata, pagamenti integrati.**

**Componenti completi:**
- **Frontend**: Next.js 14+ (App Router)
- **Backend**: Convex (backend reattivo, funzioni TypeScript, real-time nativo)
- **Database**: Convex Database (document-oriented, real-time subscriptions)
- **Auth**: Clerk (componenti UI auth prebuilt, SSO enterprise)
- **Payments**: Stripe (via Convex actions)
- **Hosting**: Vercel (frontend) + Convex Cloud (backend)
- **AI Layer**: OpenAI via Convex actions, Vercel AI SDK

**Profilo ideale:**
- Prodotti con real-time come feature core (collaborative tools, chat, live dashboard)
- Developer che vuole auth enterprise-ready senza configurazione
- Startup B2B che vuole SSO da day 1
- Team che vuole type-safety anche nel backend

**Time-to-MVP stimato:** 2-4 settimane

**Costo mensile stimato:**
| Fase | Costo |
|---|---|
| Free tier (Convex + Clerk generosi) | €0 |
| 1.000 utenti attivi | €30-80/mese |
| 10.000 utenti attivi | €200-500/mese |

**Pro:**
- Convex reactive queries = real-time automatico senza WebSocket manuale
- Clerk gestisce tutto: UI login, MFA, SSO, organizations, user management
- TypeScript end-to-end incluso Convex schema
- Ottimo per prodotti collaboration-heavy

**Contro:**
- Convex è vendor lock-in forte (diverso da SQL standard)
- Clerk costa di più rispetto a Supabase Auth per volumi alti
- Convex document DB non ideale per dati fortemente relazionali

**Use case ideale:** Tool collaborativi real-time, project management, chat integrata, dashboard live.

**Prodotti noti:** Numerous collaborative tools, alcuni AI coding assistant UI

---

## Matrice Decisionale

> Usa questa tabella per scegliere velocemente lo stack in base allo scenario del prodotto.

| Scenario | Stack Consigliato | Motivo |
|---|---|---|
| **Solo vibe coder** | Stack 1 (Next.js + Supabase + Vercel) | Setup in ore, documentazione eccellente, zero DevOps |
| **Team 2 developer** | Stack 7 (Next.js + tRPC + Prisma) | Type-safety previene bug da comunicazione tra developer |
| **Prodotto con real-time** | Stack 10 (Next.js + Convex + Clerk) | Convex reactive queries eliminano tutta la complessità WebSocket |
| **Prodotto con AI pesante** | Stack 6 (React + FastAPI + Supabase) | Python nativo per ML pipeline, LangChain, embedding |
| **Marketplace 2 lati** | Stack 5 (Next.js + Django + PostgreSQL) | Django gestisce logica complessa, PostgreSQL per transazioni ACID |
| **SaaS enterprise B2B** | Stack 5 o Stack 7 | Compliance, audit log, SSO enterprise, scalabilità |
| **Mobile + web** | Stack 9 (React Native + Expo) + Stack 1 per web | Una codebase mobile, backend Supabase condiviso |
| **Budget €0 per tool** | Stack 4 (SvelteKit + PocketBase + Railway) | PocketBase self-hosted, Railway con crediti gratuiti |

---

## AI Layer Options

> Come integrare AI nel tech stack. Questi layer si aggiungono a qualsiasi stack sopra.

### OpenAI API (GPT-4o, GPT-4o-mini)

**Quando sceglierlo:** Prodotto general-purpose, massima capacità, utenti si aspettano "la migliore AI".

| Metrica | Valore |
|---|---|
| Latenza tipica (GPT-4o-mini) | 1-3 secondi per risposta media |
| Latenza tipica (GPT-4o) | 3-10 secondi per risposta complessa |
| Costo per 1K chiamate (4o-mini) | ~€0.30-0.60 (dipende dai token) |
| Costo per 1K chiamate (4o) | ~€5-15 (dipende dai token) |
| Contesto massimo | 128K token |
| Multimodale (immagini/audio) | Sì |

**Nota:** GPT-4o-mini è il default per la maggior parte dei casi d'uso: 95% della qualità al 5% del costo.

---

### Anthropic Claude API

**Quando sceglierlo:** Prodotti che richiedono ragionamento lungo, analisi documenti complessi, casi d'uso con context window enorme.

| Metrica | Valore |
|---|---|
| Latenza tipica (Claude 3.5 Haiku) | 1-3 secondi |
| Latenza tipica (Claude 3.5 Sonnet) | 3-8 secondi |
| Costo per 1K chiamate (Haiku) | ~€0.25-0.50 |
| Costo per 1K chiamate (Sonnet) | ~€3-8 |
| Contesto massimo | 200K token |
| Multimodale | Sì (immagini) |

**Nota:** Eccellente per analisi di documenti lunghi, codice complesso, contenuti professionali. Ragionamento superiore a GPT-4o su task complessi.

---

### Groq

**Quando sceglierlo:** Prodotti dove la velocità di risposta è UX critica (chat in tempo reale, completamento testo, voce).

| Metrica | Valore |
|---|---|
| Latenza tipica (Llama 3.1 70B) | 0.3-1 secondo |
| Costo per 1K chiamate | ~€0.05-0.20 |
| Modelli disponibili | Llama 3.x, Mixtral, Gemma |
| Contesto massimo | 32K-128K token |

**Nota:** 5-10x più veloce di OpenAI. Ideale per streaming, completamento testo in tempo reale. Non ideale per ragionamento complesso.

---

### Ollama (Local / Privacy)

**Quando sceglierlo:** Prodotti con dati sensibili, compliance GDPR stretta, nessun dato verso API esterne, budget operativo €0 per AI.

| Metrica | Valore |
|---|---|
| Latenza tipica (dipende dall'hardware) | 2-30 secondi (GPU locale) |
| Costo per 1K chiamate | €0 (hardware già posseduto) |
| Modelli supportati | Llama 3.x, Mistral, Phi, Gemma, etc. |
| Privacy | 100% locale, zero dati out |

**Nota:** Richiede server con GPU per performance accettabili. Ottimo per prodotti enterprise on-premise o tool developer locali.

---

### Vercel AI SDK

**Quando sceglierlo:** Stack Next.js + Vercel. È un'astrazione unificata che ti permette di switchare tra provider (OpenAI, Anthropic, Groq, etc.) cambiando una riga di codice.

| Metrica | Valore |
|---|---|
| Latenza aggiuntiva | Trascurabile (<50ms overhead) |
| Provider supportati | OpenAI, Anthropic, Google, Groq, Mistral, etc. |
| Feature extra | Streaming nativo, tool calling, structured output |
| Costo | Gratuito (open source) |

**Nota:** Raccomandato per tutti i prodotti Next.js. Elimina il coupling con un singolo provider AI.

---

## Payments Integration

> Confronto tra le principali soluzioni di pagamento per SaaS.

| Feature | Stripe | Paddle | Lemon Squeezy | RevenueCat |
|---|---|---|---|---|
| **Tipo** | Payment processor | Merchant of Record | Merchant of Record | IAP manager |
| **VAT/IVA handling** | Manual (devi gestirlo tu) | Automatico (MoR) | Automatico (MoR) | N/A (usa app store) |
| **Fee transazione** | 1.4-2.9% + €0.25 | 5% + €0.50 | 5% + €0.50 | 1% su revenue |
| **Payout** | Giornaliero/settimanale | Settimanale | Settimanale | Mensile |
| **SaaS subscriptions** | Sì (Stripe Billing) | Sì | Sì | Solo IAP |
| **One-time payments** | Sì | Sì | Sì | No |
| **Dashboard analytics** | Base | Buona | Ottima (indie-first) | Eccellente |
| **Compliance globale** | Tu (con Stripe Tax) | Automatica | Automatica | App Store |
| **Setup complexity** | Media-Alta | Bassa | Molto bassa | Bassa |
| **Ideal for** | Startup tech, enterprise | SaaS B2B globale | Indie SaaS, plugin | App mobile |

**Raccomandazione rapida:**
- **Stripe** → Se hai un developer, vuoi controllo totale, prodotto complesso
- **Paddle** → Se vendi globalmente e non vuoi gestire IVA/compliance
- **Lemon Squeezy** → Se sei indie, vuoi setup veloce, prodotti digitali semplici
- **RevenueCat** → Se il tuo prodotto vive nell'App Store o Google Play

---

## Template Sezione Tech Stack per PRD Tipo D

> Copia questo blocco nella sezione "Technical Architecture" del PRD. Compila i campi tra `[...]`.

```markdown
## Technical Architecture

### Stack Overview

| Layer | Tecnologia | Motivazione |
|---|---|---|
| Frontend | [Next.js 14 / SvelteKit / Nuxt.js] | [Motivo della scelta] |
| Backend | [Next.js API Routes / FastAPI / Django] | [Motivo della scelta] |
| Database | [Supabase PostgreSQL / PlanetScale MySQL / Convex] | [Motivo della scelta] |
| Auth | [Supabase Auth / Clerk / NextAuth.js] | [Motivo della scelta] |
| Payments | [Stripe / Paddle / Lemon Squeezy] | [Motivo della scelta] |
| Hosting | [Vercel / Railway / Fly.io / AWS] | [Motivo della scelta] |
| AI Layer | [OpenAI / Anthropic / Groq / Vercel AI SDK] | [Motivo della scelta] |

### Profilo Stack

- **Categoria**: [Vibe-coder solo / Startup 2-5 dev / Team enterprise]
- **Time-to-MVP stimato**: [X settimane]
- **Costo mensile stimato (1K utenti)**: [€ X/mese]
- **Costo mensile stimato (10K utenti)**: [€ X/mese]

### Decisioni tecniche chiave

1. **[Decisione 1]** — [Perché questa scelta vs alternative]
2. **[Decisione 2]** — [Perché questa scelta vs alternative]
3. **[Decisione 3]** — [Perché questa scelta vs alternative]

### Integrazioni esterne

| Servizio | Scopo | Piano |
|---|---|---|
| [Nome servizio] | [Cosa fa] | [Free/Paid/Enterprise] |

### Scalabilità e limiti

- **Bottleneck attuale**: [Dove rompe per primo con la crescita]
- **Piano di scaling a 100K utenti**: [Cosa cambia]
- **Vendor lock-in rischi**: [Dipendenze critiche difficili da sostituire]
```

---

*Documento aggiornato: 2026-05-01 | Versione: 1.0 | Parte di PRD Architect OS*
