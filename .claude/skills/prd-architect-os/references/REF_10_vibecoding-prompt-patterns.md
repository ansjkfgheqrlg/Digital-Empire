# REF_10 — Vibecoding Prompt Patterns
## Pattern Library per PRD Tipo D — AI-Ready Development

Questa libreria raccoglie i pattern di scrittura PRD ottimizzati per strumenti AI di sviluppo: **Cursor**, **Claude Code**, **Bolt.new**, **Lovable**, **Replit Agent**, **v0 by Vercel**, **GitHub Copilot Workspace**.

Un PRD Tipo D non è un PRD tradizionale riformattato. È un documento progettato come **prompt strutturato** che l'AI interpreta per costruire software reale.

---

## 🧠 Principio Fondamentale

> Il Vibecoding PRD deve essere leggibile sia da un umano senior che da un LLM con zero contesto pregresso.

Ogni sezione deve rispondere alla domanda implicita dell'AI builder: **"Cosa devo costruire esattamente, in quale ordine, con quale tech stack, con quali vincoli?"**

---

## PATTERN 1 — Tech Stack Vincolante

### Anti-Pattern (vago)
```
Stack: React + Node.js + database relazionale
```

### Pattern Corretto (vincolante)
```markdown
## Tech Stack — VINCOLANTE (non sostituire senza approvazione)

**Frontend**
- Framework: Next.js 14 con App Router (NO Pages Router)
- UI Library: shadcn/ui + Radix UI primitives
- Styling: Tailwind CSS v3.4 (NO CSS modules, NO styled-components)
- State: Zustand per stato globale, React Query per server state
- Form: React Hook Form + Zod validation
- Animazioni: Framer Motion (solo micro-animations, NO heavy animations)

**Backend**
- Runtime: Node.js 20 LTS
- Framework: Next.js API Routes (NO Express separato)
- ORM: Prisma 5.x
- Auth: NextAuth.js v5 (Auth.js)

**Database**
- Primary: PostgreSQL 16 (via Supabase)
- Cache: Redis (via Upstash) — solo se specificato per feature
- File Storage: Supabase Storage

**Deployment**
- Hosting: Vercel
- Database: Supabase (progetto dedicato per ambiente)
- CI/CD: GitHub Actions

**Vincoli assoluti**
- NO class components React
- NO jQuery
- NO moment.js (usa date-fns)
- NO any TypeScript — strict mode obbligatorio
- Tutti i file: TypeScript (.ts / .tsx)
```

### Regola d'uso
Specifica SEMPRE versioni esatte. "React" lascia l'AI libera di usare React 16. "Next.js 14 con App Router" è un constraint preciso.

---

## PATTERN 2 — Fasi di Sviluppo Numerate

### Anti-Pattern (piatto)
```
L'app deve avere autenticazione, dashboard, e funzionalità di export.
```

### Pattern Corretto (fasi numerate con dipendenze)
```markdown
## Fasi di Sviluppo

### FASE 1 — Foundation (Blocco tutto il resto)
**Obiettivo**: App funzionante con auth e struttura routing

**Da costruire:**
1. Setup progetto Next.js + TypeScript + Tailwind + shadcn/ui
2. Schema Prisma: tabelle `users`, `sessions`, `accounts` (NextAuth)
3. NextAuth.js configurato con provider Google + email/password
4. Layout root con header/sidebar responsive
5. Route protetta `/dashboard` — redirect a `/login` se non autenticato

**Criteri di completamento Fase 1:**
- [ ] `npm run dev` funziona senza errori TypeScript
- [ ] Login con Google funziona end-to-end
- [ ] `/dashboard` è accessibile solo se loggato
- [ ] Mobile responsive verificato su 375px

**Non includere in questa fase**: nessuna feature di business logic

---

### FASE 2 — Core Feature (dipende da Fase 1 completata)
**Obiettivo**: Feature principale dell'app funzionante

**Da costruire:**
1. Schema Prisma: tabella `projects` con campi [id, name, userId, status, createdAt, updatedAt]
2. API Route `POST /api/projects` — crea progetto
3. API Route `GET /api/projects` — lista progetti dell'utente loggato
4. API Route `DELETE /api/projects/[id]` — elimina (solo owner)
5. Componente `ProjectList` — card grid con infinite scroll
6. Componente `CreateProjectModal` — form con validazione Zod

**Criteri di completamento Fase 2:**
- [ ] CRUD completo testabile via UI
- [ ] Utente A non può vedere/modificare progetti di utente B
- [ ] Validazione lato client e lato server
- [ ] Empty state quando nessun progetto

---

### FASE 3 — Secondary Features (dipende da Fase 2)
[...]

### FASE 4 — Polish & Launch (dipende da Fase 3)
[...]
```

### Regola d'uso
- Ogni fase deve avere **checklist di completamento** — l'AI sa quando fermarsi
- Le dipendenze tra fasi devono essere esplicite
- Max 5-7 item per fase — non sovraccaricare

---

## PATTERN 3 — User Flow Testuale (senza diagrammi)

### Anti-Pattern (ambiguo)
```
L'utente si registra e viene portato al dashboard.
```

### Pattern Corretto (passo per passo)
```markdown
## User Flows Principali

### Flow 1: Onboarding nuovo utente

**Trigger**: Utente clicca "Inizia gratis" su landing page

**Step 1 — Landing → Signup**
- URL: `/signup`
- Form campi: email, password (min 8 caratteri, 1 maiuscola, 1 numero), nome
- Validation: real-time con React Hook Form + Zod
- Submit: chiama `POST /api/auth/register`
- Loading state: bottone disabilitato + spinner

**Step 2 — Verifica email**
- Redirect a `/verify-email?email=[email]`
- UI: messaggio "Controlla la tua inbox"
- Email inviata via: Resend API con template HTML custom
- Link verifica valido: 24 ore
- Se non ricevuta: bottone "Reinvia email" (rate limit: 1 click ogni 60s)

**Step 3 — Email verificata → Onboarding**
- Utente clicca link → `GET /api/auth/verify?token=[token]`
- Se token valido: redirect a `/onboarding/step-1`
- Se token scaduto: pagina errore con CTA "Richiedi nuovo link"

**Step 4 — Onboarding wizard (3 step)**
- Step 1/3: "Come ti chiami?" + "A cosa serve [AppName]?" (select 3 opzioni)
- Step 2/3: "Invita colleghi" (skippabile)
- Step 3/3: "Crea il tuo primo progetto" — shortcut diretta a Fase 2 flow
- Progress bar in alto: 3 step visibili
- Skip complessivo: link "Salta → vai al dashboard"

**Step 5 — Dashboard**
- Prima visita: empty state con tooltip contestuale
- Se ha creato progetto in step 4: progetto già visibile
- Tour guidato: 4 highlight con Shepherd.js (dismissibile)

**Risultato finale**: utente loggato, email verificata, dashboard caricata
```

### Regola d'uso
- Ogni step deve avere: trigger, URL, componente, API call, stato UI, edge case
- Non usare frecce o diagrammi — l'AI li ignora
- Usa **Step N** numerati sempre

---

## PATTERN 4 — Schema DB Outline

### Anti-Pattern (generico)
```
Database con tabelle per utenti, progetti e risorse.
```

### Pattern Corretto (Prisma schema outline)
```markdown
## Schema Database — Outline

> Nota: questo è un outline semantico. L'AI deve generare il Prisma schema completo
> rispettando questi campi, relazioni e vincoli.

### Tabella: `users`
| Campo | Tipo | Vincoli | Note |
|-------|------|---------|------|
| id | String | PK, CUID | auto-generato |
| email | String | UNIQUE, NOT NULL | lowercase always |
| name | String | nullable | display name |
| avatarUrl | String | nullable | da Google OAuth o upload |
| plan | Enum | NOT NULL, default: FREE | FREE / PRO / ENTERPRISE |
| createdAt | DateTime | default: now() | |
| updatedAt | DateTime | auto-update | |

### Tabella: `projects`
| Campo | Tipo | Vincoli | Note |
|-------|------|---------|------|
| id | String | PK, CUID | |
| name | String | NOT NULL, max 100 chars | |
| description | String | nullable, max 500 | |
| userId | String | FK → users.id | owner |
| status | Enum | NOT NULL, default: ACTIVE | ACTIVE / ARCHIVED / DELETED |
| isPublic | Boolean | default: false | |
| createdAt | DateTime | default: now() | |
| updatedAt | DateTime | auto-update | |

**Indici da creare:**
- `projects.userId` — per query "tutti i progetti dell'utente"
- `projects.(userId, status)` — compound per filtri frequenti

**Relazioni:**
- `users` → `projects`: one-to-many (un utente ha molti progetti)
- `projects` → `members`: many-to-many via `project_members` junction table

### Row Level Security (se Supabase)
```sql
-- Utente vede solo i propri progetti
CREATE POLICY "users_own_projects" ON projects
  FOR ALL USING (auth.uid() = user_id);

-- Admin può vedere tutto
CREATE POLICY "admin_all_projects" ON projects
  FOR ALL USING (
    EXISTS (SELECT 1 FROM users WHERE id = auth.uid() AND role = 'ADMIN')
  );
```

### Pattern relazioni obbligatorie
- Soft delete con `deletedAt DateTime nullable` — mai DELETE fisico su dati business
- `createdAt` + `updatedAt` su OGNI tabella
- Audit trail via tabella `events` separata se GDPR rilevante
```

---

## PATTERN 5 — AI Constraints Section

### Anti-Pattern (assente o troppo vago)
```
Rispetta le best practice di sviluppo.
```

### Pattern Corretto (constraints operativi espliciti)
```markdown
## AI Constraints — Regole Operative per l'AI Builder

### Cosa FARE sempre

**Sicurezza**
- Valida TUTTI gli input lato server (non solo client)
- Usa Zod schema su ogni API route
- Rate limiting su tutte le route auth: 5 tentativi/15 minuti
- Sanitizza ogni output HTML per prevenire XSS
- Variabili d'ambiente: mai hardcodare API key o segreti nel codice

**Qualità codice**
- TypeScript strict mode — zero `any` impliciti
- Ogni componente React ha prop types definiti
- Error boundaries su ogni page component
- Loading + error state per ogni data fetch
- Console.log rimossi prima di ogni commit

**UX**
- Ogni azione > 300ms ha loading feedback visivo
- Form validation: errori mostrati inline, non solo al submit
- Confirma distruttiva (modal + "digita per confermare") per delete irreversibili
- Redirect a login se sessione scaduta (intercetta 401)

**Database**
- Transazioni Prisma per operazioni multi-step
- Mai eseguire query N+1 — usa `include` o batch
- Tutti i campi nullable devono avere fallback nel codice

---

### Cosa NON FARE mai

**Architettura**
- NON creare file >300 righe — splitta in componenti/moduli
- NON usare Context API per stato che deve persistere (usa Zustand)
- NON mescolare logica di business nei componenti UI
- NON bypasare autenticazione per testing — usa test user dedicato

**UI**
- NON usare colori inline — solo classi Tailwind o variabili CSS
- NON usare `!important` nel CSS
- NON creare animazioni >500ms per interazioni frequenti

**Database**
- NON fare DELETE fisico su dati utente (soft delete sempre)
- NON esporre l'ID interno del database nelle URL pubbliche (usa slug o CUID)
- NON eseguire query raw SQL senza parametrizzazione

**Sicurezza**
- NON loggare dati sensibili (password, token, carta di credito)
- NON fare fetch client-side di API key — proxy sempre lato server
- NON usare eval() o dangerouslySetInnerHTML senza sanitizzazione

---

### Gestione Errori Standard
```typescript
// Pattern obbligatorio per tutte le API Route
try {
  // business logic
  return NextResponse.json({ data: result }, { status: 200 });
} catch (error) {
  if (error instanceof ZodError) {
    return NextResponse.json(
      { error: "Dati non validi", details: error.errors },
      { status: 400 }
    );
  }
  if (error instanceof Prisma.PrismaClientKnownRequestError) {
    if (error.code === "P2025") {
      return NextResponse.json({ error: "Risorsa non trovata" }, { status: 404 });
    }
  }
  console.error("[API Error]", error); // Log strutturato
  return NextResponse.json({ error: "Errore interno del server" }, { status: 500 });
}
```
```

---

## PATTERN 6 — Componente Spec

### Anti-Pattern (vago)
```
Creare una tabella per mostrare i progetti.
```

### Pattern Corretto (spec di componente dettagliata)
```markdown
## Componente: ProjectTable

**Path file**: `src/components/projects/ProjectTable.tsx`

**Props**:
```typescript
interface ProjectTableProps {
  projects: Project[];
  isLoading: boolean;
  onDelete: (projectId: string) => void;
  onArchive: (projectId: string) => void;
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}
```

**Comportamenti**:
- Loading: skeleton di 5 righe (usa `Skeleton` da shadcn/ui)
- Empty state: illustrazione + "Nessun progetto ancora. Creane uno →"
- Sorting: click su header colonna, freccia indicatore, ascending/descending
- Row hover: background `gray-50`, actions visibili (edit, archive, delete)
- Delete: apre `ConfirmDialog` con testo "Scrivi il nome del progetto per confermare"
- Responsive: su mobile <768px diventa card stack invece di tabella

**Colonne** (ordine fisso):
| Colonna | Larghezza | Sortable | Note |
|---------|-----------|---------|------|
| Nome | flex-grow | Sì | link cliccabile a `/projects/[id]` |
| Stato | 100px | Sì | badge colorato: verde/grigio/rosso |
| Creato | 150px | Sì | formato "DD MMM YYYY" |
| Owner | 120px | No | avatar + nome (solo in vista team) |
| Azioni | 80px | No | ... menu con Edit/Archive/Delete |

**Accessibilità**:
- `role="table"` con `aria-label="Lista progetti"`
- Header celle: `scope="col"`
- Row con `aria-label="Progetto [nome]"`
- Delete action: `aria-label="Elimina progetto [nome]"`
```

---

## PATTERN 7 — Environment Variables Setup

```markdown
## Environment Variables

### Obbligatorie (app non si avvia senza)
```env
# Database
DATABASE_URL="postgresql://..."
DIRECT_URL="postgresql://..."  # Supabase connection pooling

# Auth
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="[genera con: openssl rand -base64 32]"

# OAuth providers
GOOGLE_CLIENT_ID="..."
GOOGLE_CLIENT_SECRET="..."
```

### Opzionali per feature aggiuntive
```env
# Email (Resend)
RESEND_API_KEY="re_..."
EMAIL_FROM="noreply@tuodominio.com"

# Storage (Supabase)
NEXT_PUBLIC_SUPABASE_URL="https://xxx.supabase.co"
NEXT_PUBLIC_SUPABASE_ANON_KEY="eyJ..."
SUPABASE_SERVICE_ROLE_KEY="eyJ..."  # SOLO lato server, mai esposta

# Analytics
NEXT_PUBLIC_POSTHOG_KEY="phc_..."
NEXT_PUBLIC_POSTHOG_HOST="https://app.posthog.com"
```

### Regole di naming
- `NEXT_PUBLIC_*` → accessibile lato client (attenzione: visibile nel bundle)
- Senza prefisso → solo lato server
- Mai esporre `SERVICE_ROLE_KEY` lato client
```

---

## PATTERN 8 — Testing Spec per Vibecoding

```markdown
## Test Plan Minimo

### Unit Tests (Vitest)
- [ ] Schema Zod: testa ogni caso di validazione valido e invalido
- [ ] Utility functions: 100% coverage
- [ ] Hook custom: testa stati loading/error/success

### Integration Tests (Playwright)
- [ ] Flow login completo (Google mock + email/password)
- [ ] CRUD progetto: crea, modifica nome, archivia, elimina
- [ ] Autorizzazione: utente B non può accedere a dati utente A

### Smoke Tests (pre-deploy)
- [ ] Home page carica < 3s
- [ ] Login funziona
- [ ] Dashboard mostra dati reali
- [ ] Nessun errore 500 nelle route principali

### Non testare (deliberatamente escluso da scope)
- Third-party integrations (mock, non test reali)
- Performance exhaustive (solo smoke)
- Cross-browser completo (Chrome + Firefox, non IE/Safari legacy)
```

---

## Quick Reference — Checklist PRD Tipo D

Prima di consegnare un PRD Vibecoding, verifica:

```
□ Tech stack specificato con versioni esatte
□ Ogni libreria ha motivazione ("perché X invece di Y")
□ Fasi numerate con dipendenze esplicite
□ Ogni fase ha criteri di completamento (checklist)
□ Schema DB con tipi, vincoli e indici
□ RLS policies se usa Supabase
□ User flows in formato step numerati (no diagrammi)
□ AI Constraints: DO list + DON'T list
□ Environment variables categorizzate
□ Error handling pattern definito con codice TypeScript
□ Almeno 1 componente spec con props TypeScript
□ Test plan con scope IN e OUT espliciti
```

Se mancano più di 3 item → il PRD non è pronto per il vibecoding.
