# REF_01 — PRD Examples Compiled
## 4 PRD Completamente Compilati — Reference Master

Questi esempi mostrano il **livello di dettaglio atteso** per ogni tipo di PRD.
Usali come benchmark qualitativo: se il tuo output è meno denso di questi, non è finito.

---

## 🔵 ESEMPIO 1 — PRD MVP LEAN (Tipo B)
### Prodotto: "QuickInvoice" — SaaS preventivi per freelance italiani

---

```markdown
---
# PRD: QuickInvoice — MVP v1
**Versione**: 1.2 | **Status**: APPROVED ✅
**Autore**: PM | **Data creazione**: 10/01/2025
**Ultima modifica**: 18/01/2025
**Revisori**: Lead Dev, UI Designer
**Time-box**: 3 settimane (21 giorni)
---

## 📋 CHANGE LOG
| Versione | Data | Autore | Modifica | Motivo |
|----------|------|--------|----------|--------|
| 1.0 | 10/01 | PM | Draft iniziale | — |
| 1.1 | 14/01 | PM | Rimossa firma digitale | Troppo complessa per v1 |
| 1.2 | 18/01 | PM | Aggiunta sezione rollout | Feedback engineering |

---

## ⚡ TL;DR
> **Cosa è**: SaaS web per freelance italiani che crea e invia preventivi professionali in PDF in <10 minuti.
> **Il problema**: I freelance perdono in media 3-4 ore/settimana a costruire preventivi manualmente in Word/Excel.
> **La soluzione**: Editor drag-and-drop con template pre-compilati, calcolo automatico IVA/ritenuta, invio PDF via email con 1 click.
> **North Star**: 1 preventivo inviato entro 10 minuti dal primo accesso — target ≥ 60% degli utenti nuovi.
> **Time-box**: 3 settimane — 1 developer full-stack.

---

## 🎯 PROBLEM STATEMENT

### Il Problema
I freelance italiani (designer, copywriter, consulenti, sviluppatori) non hanno uno strumento dedicato e semplice per creare preventivi professionali. La soluzione più comune è un documento Word/Excel personalizzato manualmente ogni volta.

Questo causa 3 problemi concreti:
1. **Tempo perso**: 45-90 minuti per preventivo, 3-4 ore/settimana in media per chi ha 5+ clienti attivi
2. **Errori di calcolo**: IVA, ritenuta d'acconto, totali sbagliati → dispute con clienti e problemi fiscali
3. **Aspetto non professionale**: layout diverso ogni volta → percezione di scarsa serietà

### Evidenza
- **Dati qualitativi**: 11/15 intervistati usano Word/Excel. Tutti lo considerano una perdita di tempo.
- **Dati quantitativi**: Su un campione di 50 freelance, il tempo medio per preventivo è 67 minuti.
- **Reddit r/freelance_ita**: 23 thread con "preventivo" negli ultimi 6 mesi — 78% lamenta la complessità.
- **Competitor gap**: FattureInCloud e Fattura24 sono orientati alla fatturazione, non ai preventivi pre-vendita. UX pensata per commercialisti, non per creativi.

### Perché Ora
Il mercato dei freelance italiani è cresciuto del 34% dal 2020 (fonte: Eurostat 2024). La digitalizzazione post-COVID ha portato nuovi freelance senza processi strutturati. Momento ideale per un tool verticale e semplice.

---

## 👤 TARGET UTENTE

### Persona Primaria: "Marco il Freelance"
**Ruolo**: Freelance creativo (web designer, copywriter, consulente marketing, sviluppatore)
**Età**: 26-38 anni
**Contesto**: Lavora da casa o coworking, 3-8 clienti attivi, gestisce tutto da solo
**Livello tecnico**: Semi-tecnico — usa Figma, Notion, Slack. Non sa programmare.
**Obiettivo**: Inviare un preventivo professionale velocemente senza pensarci
**Frustrazione**: "Ogni volta che devo fare un preventivo perdo un'ora. E spesso mi dimentico qualcosa."
**Budget**: €9-19/mese per tool che usa ogni giorno

**Jobs-To-Be-Done**:
> "Quando un cliente mi chiede un preventivo, voglio crearlo e mandarlo in meno di 10 minuti
> in modo da sembrare professionale senza perdere il pomeriggio a formattare un Word."

**Quote rappresentativa**:
> "Ho un template Excel che ho modificato 20 volte negli anni. Non è bello, faccio sempre errori
> con i calcoli dell'IVA, e ogni cliente mi dice 'mandami il preventivo' come se fosse semplice."

### Persona Secondaria: "Il Cliente di Marco"
**Ruolo**: Titolare PMI o marketing manager
**Interazione**: Riceve email con PDF allegato + link per approvare online
**NON usa l'app** — vede solo l'output finale

---

## 📊 SUCCESS METRICS

### 🎯 North Star Metric
**Time-to-first-invoice**: % utenti che inviano il primo preventivo entro 10 min dal signup
- **Target**: ≥ 60% entro 30 giorni dal lancio
- **Baseline**: non misurato (prodotto nuovo)
- **Tool**: PostHog — evento `invoice_sent` con property `minutes_since_signup`

### 📈 Primary Metrics
| Metrica | Baseline | Target | Timeframe | Tool |
|---------|----------|--------|-----------|------|
| D7 Retention | — | ≥ 35% | 60gg dal lancio | PostHog |
| Preventivi/utente/settimana | — | ≥ 2 | 30gg dal lancio | PostHog |
| Trial → Paid conversion | — | ≥ 8% | 90gg dal lancio | Stripe |
| NPS dopo primo preventivo | — | ≥ 40 | 60gg dal lancio | Typeform |

### 🛡️ Guardrail Metrics
- **Crash rate**: ≤ 0.5% sessioni (Sentry)
- **Email delivery rate**: ≥ 98% (Resend)
- **Page load**: homepage e editor ≤ 2s P95 (Vercel Analytics)

### 📊 Analytics Events Obbligatori
```javascript
posthog.capture('user_signed_up', { method: 'email'|'google', plan: 'trial' })
posthog.capture('invoice_created', {
  user_id, template_used, items_count, has_iva, has_ritenuta
})
posthog.capture('invoice_sent', {
  user_id, invoice_id, total_amount,
  minutes_since_signup, minutes_to_create, send_method
})
posthog.capture('subscription_started', {
  user_id, plan, trigger: 'limit_reached'|'voluntary'|'trial_ended'
})
```

---

## 📖 CORE USER STORIES

### EPIC 1: Autenticazione e Onboarding

#### US-001: Registrazione con Email
**Come** freelance che scopre QuickInvoice,
**voglio** creare un account con email e password,
**in modo da** iniziare a usare il tool subito.

**Acceptance Criteria**:
- [ ] ✅ Form: nome, email, password (min 8 char)
- [ ] ✅ Validazione inline — errori sotto il campo, senza ricaricare
- [ ] ✅ Dopo submit → redirect a /onboarding/step-1 entro 2s
- [ ] ✅ Email di benvenuto inviata entro 60s
- [ ] ❌ FALLISCE SE: l'utente resta sulla pagina di signup dopo submit corretto
- [ ] ❌ FALLISCE SE: email già registrata non mostra "Questa email è già in uso. [Fai login →]"

**Priority**: P0 | **Effort**: S (0.5 giorni)

---

#### US-002: Onboarding Wizard (3 step)
**Come** nuovo utente appena registrato,
**voglio** essere guidato nella configurazione iniziale,
**in modo da** avere il mio profilo pronto per il primo preventivo.

**Step 1** — Dati: nome/azienda, P.IVA (opzionale), logo upload (max 2MB)
**Step 2** — Fiscale: regime, IVA, ritenuta d'acconto
**Step 3** — Template: scelta colore brand + preview

**Acceptance Criteria**:
- [ ] ✅ Ogni step salvato in real-time (no perdita dati se browser chiuso)
- [ ] ✅ Skip possibile con warning "Il preventivo userà dati incompleti"
- [ ] ✅ Progress bar visibile (Passo 1 di 3)
- [ ] ✅ Dati onboarding pre-compilano il primo preventivo
- [ ] ❌ FALLISCE SE: saltando l'onboarding il primo preventivo ha campi vuoti senza placeholder

**Priority**: P0 | **Effort**: M (2 giorni)

---

### EPIC 2: Creazione Preventivo

#### US-004: Creazione da Template
**Come** freelance che deve inviare un preventivo,
**voglio** partire da un template pre-compilato,
**in modo da** non dover impostare tutto da zero.

**Template disponibili v1**: "Servizi creativi" | "Sviluppo web" | "Consulenza" | "Blank"

**Acceptance Criteria**:
- [ ] ✅ Preview visiva nella scelta template
- [ ] ✅ Click → editor pre-compilato con voci tipiche della categoria
- [ ] ✅ Salvataggio automatico ogni 30 secondi
- [ ] ✅ Indicatore "Salvato ✓" / "Salvataggio..." visibile
- [ ] ❌ FALLISCE SE: modifiche perse navigando via senza conferma

**Priority**: P0 | **Effort**: L (3 giorni)

---

#### US-005: Editor Voci Preventivo
**Come** freelance nell'editor,
**voglio** aggiungere, modificare, rimuovere voci con qty × prezzo,
**in modo da** costruire un preventivo accurato.

```
[ Descrizione          ] [ Qty ] [ Prezzo ] [ Totale ]
[ Servizio di design   ] [  1  ] [ €800   ] [ €800   ] [🗑️]
```

**Acceptance Criteria**:
- [ ] ✅ Totale riga calcolato automaticamente (Qty × Prezzo)
- [ ] ✅ Subtotale, IVA, ritenuta, Totale finale in real-time
- [ ] ✅ Drag-and-drop per riordinare le voci
- [ ] ✅ Campo note aggiuntive + condizioni di pagamento
- [ ] ❌ FALLISCE SE: totali non si aggiornano senza reload
- [ ] ❌ FALLISCE SE: eliminare voce non chiede conferma se campo popolato

**Priority**: P0 | **Effort**: L (3 giorni)

---

#### US-006: Preview e Invio PDF
**Come** freelance che ha compilato il preventivo,
**voglio** vedere l'anteprima e inviarlo con 1 click,
**in modo da** essere sicuro dell'output e agire velocemente.

**Acceptance Criteria**:
- [ ] ✅ "Anteprima PDF" genera lato server e mostra in modal (NON nuova tab)
- [ ] ✅ PDF rispecchia esattamente la preview
- [ ] ✅ Invio: campo email + subject pre-compilato + messaggio personalizzabile
- [ ] ✅ Email inviata entro 30s dall'azione
- [ ] ✅ Stato preventivo → "Inviato" con timestamp
- [ ] ✅ Copia CC all'utente (toggle opzionale)
- [ ] ❌ FALLISCE SE: PDF ha layout rotto su Chrome/Firefox/Safari

**Priority**: P0 | **Effort**: M (2 giorni)

---

### EPIC 3: Dashboard e Gestione

#### US-007: Dashboard Preventivi
**Come** freelance con più clienti,
**voglio** vedere tutti i preventivi con il loro stato,
**in modo da** tenere traccia di cosa è in attesa, accettato o scaduto.

**Stati**: 🟡 Bozza | 🔵 Inviato | 🟢 Accettato | 🔴 Rifiutato | ⚫ Scaduto

**Acceptance Criteria**:
- [ ] ✅ Vista lista: Cliente, Importo, Stato, Data
- [ ] ✅ Filtro per stato + ricerca per cliente/importo
- [ ] ✅ Empty state: illustrazione + "Crea il tuo primo preventivo"
- [ ] ✅ Paginazione: 20 preventivi per pagina
- [ ] ❌ FALLISCE SE: lista non si aggiorna dopo invio senza refresh

**Priority**: P0 | **Effort**: M (1.5 giorni)

---

## ✅ SCOPE: IN / OUT

### IN SCOPE — v1 (21 giorni)
- Auth email + Google OAuth
- Onboarding wizard 3 step
- 4 template preventivo (3 + blank)
- Editor voci con calcolo IVA/ritenuta automatico
- Preview PDF + invio via email
- Dashboard con stati e filtri base
- Piano free: max 3 preventivi/mese
- Piano Pro (€12/mese): illimitati
- Stripe Checkout per upgrade

### OUT OF SCOPE — v1
| Feature Esclusa | Motivazione | Quando Rivalutare |
|-----------------|-------------|-------------------|
| Firma digitale | Complessità legale, costo integrazione | v3 — se richiesta da >30% utenti |
| App mobile iOS/Android | Web-first, validare prima su desktop | Post-PMF (>1.000 paganti) |
| Integrazioni contabili | Scope eccessivo per MVP | v2 — Q3 2025 |
| Template marketplace | Feature social, non core per MVP | v3 |
| Multi-lingua | Target solo Italia per v1 | v2 — se espansione EU |
| Reminder automatici | Nice-to-have | v2 |
| Dashboard analytics revenue | Complessità alta, basso impatto v1 | v2 |
| Accesso team multi-utente | Single user per v1 | v2 — se richiesto |

---

## 🔄 USER FLOWS

### FLOW 1: Onboarding e Primo Preventivo (Happy Path)
**Attore**: Marco, freelance appena registrato
**Obiettivo**: Primo preventivo inviato in <10 minuti

```
1. Marco atterra su /onboarding/step-1
   → Form dati personali pre-compilato con nome da Google OAuth

2. Marco inserisce P.IVA → clicca "Avanti →"
   → Sistema salva → mostra step-2 (config fiscale)

3. Marco seleziona "Forfettario" e "Nessuna IVA"
   → Preview template si aggiorna in real-time

4. Marco sceglie colore brand → "Crea il tuo primo preventivo →"
   → Sistema crea preventivo con template "Servizi creativi"
   → Redirect a /invoices/new

5. Marco modifica voci pre-compilate (descrizione, qty, prezzo)
   → Totale si aggiorna automaticamente

6. Marco clicca "Anteprima PDF"
   → PDF generato → modal laterale

7. Marco clicca "Invia al cliente"
   → Campo email + subject + messaggio
   → Clicca "Invia"

8. Sistema: "✅ Preventivo inviato a cliente@esempio.it"
   → Stato diventa "Inviato"
   → Redirect a /dashboard
```
**Tempo previsto**: 6-8 minuti per utente medio

**Error Paths**:
- P.IVA non valida → "Formato non valido. La P.IVA italiana ha 11 cifre." (inline, non blocca)
- PDF generation fallisce → "Non riusciamo a generare il PDF ora. I tuoi dati sono salvati." + [Riprova] + [Supporto]
- Email non valida → "Inserisci un indirizzo email valido" (inline, focus ritorna al campo)
- Invio fallisce dopo 3 retry → "Email non inviata. Puoi scaricare il PDF e inviarlo manualmente." + [Scarica PDF]

**Edge Cases**:
- Browser chiuso durante onboarding → Al prossimo login: "Continua da dove hai lasciato" + link step
- Accesso a /dashboard prima di completare onboarding → Redirect a /onboarding/step-corrente + banner
- Logo >2MB → "Il logo deve essere max 2MB. Il tuo file è X MB."

---

### FLOW 2: Utente Free Raggiunge Limite (Upgrade Flow)
```
1. Marco clicca "Crea nuovo preventivo" (il 4°)
   → Sistema: utente ha 3/3 preventivi free

2. Modal:
   "Hai raggiunto il limite del piano gratuito.
   Con Pro invii illimitati per €12/mese."
   [Upgrade a Pro] [Continua con gratuito →]

3. Marco: "Upgrade a Pro"
   → Redirect a Stripe Checkout (sessione creata server-side)

4. Pagamento completato → webhook Stripe aggiorna piano
   → Redirect a /dashboard con banner:
   "🎉 Sei ora su QuickInvoice Pro!"

5. Marco crea il 4° preventivo normalmente
```

---

## ⚠️ EDGE CASES & ERROR STATES COMPLETI

### Empty States
| Schermata | Trigger | Contenuto | CTA |
|-----------|---------|-----------|-----|
| Dashboard preventivi | Nessun preventivo | Illustrazione + "Crea il tuo primo preventivo" | "Crea preventivo →" |
| Lista clienti | Nessun cliente | "I clienti appariranno quando invii il primo preventivo" | "Crea preventivo →" |
| Risultati ricerca | Nessun match | "Nessun preventivo trovato per '[query]'" | "Cancella filtri" |

### Error States
| Errore | Contesto | Messaggio | Azione |
|--------|----------|-----------|--------|
| Network offline | Qualsiasi salvataggio | "Connessione persa. Modifiche salvate appena torni online." | Auto-retry |
| Sessione scaduta | Mid-flow | "Sessione scaduta. Fai login — non perderai il lavoro." | [Login →] |
| PDF generation failed | Preview/invio | "Errore generazione PDF. Riprova tra 30 secondi." | [Riprova] |
| Email bounce | Post-invio | Email a Marco: "L'email al cliente non è stata consegnata." | [Aggiorna email] |
| Upload logo fallito | Onboarding | "File non caricabile. JPG/PNG max 2MB." | [Riprova] |

### Loading States
| Operazione | Durata | Feedback Visivo |
|------------|--------|-----------------|
| Login/Signup | <2s | Spinner sul bottone |
| Salvataggio auto | <1s | "Salvataggio..." → "Salvato ✓" |
| Generazione PDF | 2-5s | "Generando il PDF..." |
| Invio email | 1-3s | "Invio in corso..." |
| Caricamento dashboard | <1.5s | Skeleton screen 3 righe |

---

## ⚡ REQUISITI TECNICI

```
Frontend:  Next.js 14 (App Router) + TypeScript + Tailwind CSS + shadcn/ui
PDF:       Puppeteer server-side (qualità > React-PDF)
Backend:   Supabase (database + auth + edge functions)
Database:  PostgreSQL con Row Level Security
Auth:      Supabase Auth (email + Google OAuth)
Email:     Resend (transactional)
Payments:  Stripe (Checkout + webhooks + Customer Portal)
Hosting:   Vercel
Analytics: PostHog
Errors:    Sentry
```

### Requisiti Non-Funzionali
| Categoria | Requisito | Target |
|-----------|-----------|--------|
| Performance | Page load (LCP) | ≤ 2s su 4G |
| Performance | API response | ≤ 300ms P95 |
| Performance | PDF generation | ≤ 5s P95 |
| Uptime | Availability | ≥ 99.5% mensile |
| Security | RLS | Ogni query filtrata per user_id |
| Compatibilità | Browser | Chrome 100+, Firefox 100+, Safari 15+ |

---

## ⏱️ TIMELINE — 21 GIORNI

| Settimana | Focus | Milestone |
|-----------|-------|-----------|
| W1 (gg 1-7) | Auth, DB schema, onboarding wizard | Utente si registra e completa onboarding |
| W2 (gg 8-14) | Editor preventivo, calcoli, template | Preventivo creato e PDF generato |
| W3 (gg 15-21) | Email invio, dashboard, Stripe, bug fix | Launch — utente può pagare e inviare |

### Rollout Plan
- **Giorni 19-20**: Dogfooding interno (5+ preventivi reali, crash rate = 0)
- **Giorno 21**: Beta chiusa (10 freelance da network personale)
- **Giorno 28+**: Launch pubblico (go/no-go: D7 retention beta ≥ 25%)

---

## ❓ OPEN QUESTIONS

| # | Domanda | Owner | Deadline | Status |
|---|---------|-------|----------|--------|
| 1 | Il piano free richiede carta di credito? | PM | 20/01 | 🔴 Open |
| 2 | Supportiamo anche la ricevuta fiscale? | PM | 22/01 | 🟡 In review |
| 3 | PDF: Puppeteer vs React-PDF? | Dev | 18/01 | 🟢 Risolto: Puppeteer |
| 4 | Dominio: quickinvoice.it o .io? | PM | 15/01 | 🟢 Risolto: .it |

---
*PRD Quality Score: 94/100 — 🔵 ECCELLENTE*
*Versione 1.2 — Approvato il 18/01/2025 | Prossima review: fine W1*
```

---

## 🟣 ESEMPIO 2 — PRD VIBECODING AI-READY (Tipo D)
### Prodotto: "FocusBoard" — Task manager con AI prioritization

```markdown
---
# PRD: FocusBoard
**File**: /docs/PRD.md — Leggi questo file all'inizio di ogni sessione
**Versione**: 1.1 | **Data**: GG/MM/AAAA
**Contesto**: Sviluppo con Cursor AI + Claude Sonnet
**Time-box**: 14 giorni — 1 developer (vibe coder)
---

## 🧠 PRODUCT OVERVIEW

**Cosa è**: Web app di task management che usa AI per suggerire automaticamente le 3 priorità del giorno.
**Per chi è**: Professionisti autonomi (freelance, founder, consulenti) con troppe cose da fare.
**Problema risolto**: La "paralisi da lista infinita" — avere 50 task ma non sapere quali fare oggi.
**Come funziona**:
1. L'utente inserisce i propri task con deadline e importanza
2. Ogni mattina, l'AI analizza la lista e suggerisce "Le tue 3 priorità di oggi" con spiegazione
3. L'utente lavora su quelle 3, le completa, e si sente in controllo

---

## 🔧 TECH STACK VINCOLANTE

```
⚠️ NON deviare da questo stack. Se hai dubbi, chiedi.

FRONTEND:
- Next.js 14 con App Router
- TypeScript (strict: true in tsconfig)
- Tailwind CSS per tutti gli stili
- shadcn/ui per TUTTI i componenti UI — NON creare custom se shadcn li ha
- Lucide React per le icone (NON Font Awesome, NON Heroicons)
- React Hook Form + Zod per tutti i form

BACKEND:
- Supabase (database + auth + realtime + edge functions)
- Row Level Security su TUTTE le tabelle
- Prisma come ORM (NON query SQL raw)

DATABASE:
- PostgreSQL via Supabase
- Ogni tabella: id UUID, user_id UUID FK, created_at TIMESTAMPTZ, updated_at TIMESTAMPTZ
- Soft delete: colonna deleted_at nullable (MAI DELETE fisico su dati utente)

AUTH: Supabase Auth — solo email/password per v1

AI LAYER:
- OpenAI API (gpt-4o-mini)
- Chiamate AI SOLO da server-side (Edge Functions) — MAI esporre API key al client
- Retry con exponential backoff (max 3 tentativi)

HOSTING: Vercel (auto-deploy da GitHub main)
MONITORING: Sentry + PostHog
```

---

## 🎯 TARGET UTENTE

**Chi è**: Marco, 34 anni, consulente/freelance
**Problema**: Ha 30-50+ task aperti, finisce la giornata con sensazione di aver fatto molto ma non le cose importanti
**Livello tecnico**: Non tecnico
**JTBD**: "Ogni mattina voglio sapere le 3 cose più importanti da fare oggi, senza doverci pensare."

---

## 🏗️ CORE FEATURES — PER FASE

### ⚡ FASE 1 (Giorni 1-4): Auth + Task CRUD Base
**Obiettivo**: L'utente può registrarsi, creare task, vederli, completarli, eliminarli.
**NON includere**: AI, prioritizzazione avanzata, dashboard analytics.

#### FEATURE 1.1: Autenticazione
```
/login:
1. Form: email + password
2. Submit → POST Supabase Auth
3. Success → redirect /dashboard
4. Error (credenziali errate) → "Email o password non corretti" (NON specificare quale)

/register:
1. Form: nome + email + password (min 8 char)
2. Submit → crea utente + riga in tabella users
3. Success → redirect /dashboard (NO verifica email in v1)
4. Error (email esistente) → "Email già in uso. [Fai login →]"
```

**Acceptance Criteria**:
- [ ] ✅ Login funziona → redirect /dashboard
- [ ] ✅ Login errato → messaggio specifico
- [ ] ✅ Register crea riga in `users` con name, email
- [ ] ✅ Session persiste dopo refresh
- [ ] ✅ Logout → redirect /login
- [ ] ❌ NON implementare "Dimentica password" in Fase 1

**Schema DB**:
```sql
CREATE TABLE public.users (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users see only their profile"
ON public.users FOR ALL USING (auth.uid() = id);
```

---

#### FEATURE 1.2: Task CRUD

**Struttura Task**:
```typescript
interface Task {
  id: string           // UUID
  user_id: string      // UUID FK to users
  title: string        // max 200 char — required
  description?: string // max 1000 char
  status: 'todo' | 'in_progress' | 'done'
  priority: 'low' | 'medium' | 'high' | null
  deadline?: Date
  energy_required: 'low' | 'medium' | 'high'  // default: 'medium'
  ai_suggested_today: boolean  // default: false
  created_at: Date
  updated_at: Date
  deleted_at?: Date  // soft delete
}
```

**User Flow — Creare Task**:
```
1. /dashboard → clicca "Aggiungi task"
2. Dialog shadcn: Titolo (required, autofocus) + Descrizione + Deadline + Energia
3. Submit → POST /api/tasks
4. Dialog chiude → task appare in cima con animazione slide-in
5. Toast: "Task aggiunto ✓"
```

**User Flow — Eliminare Task**:
```
1. Hover su task → icona cestino (Lucide: Trash2)
2. Click → Dialog: "Eliminare questo task? Non può essere annullato."
3. Conferma → soft delete (deleted_at = NOW())
4. Fade-out + Toast: "Task eliminato" + [Annulla] (undo 5 secondi)
```

**Acceptance Criteria**:
- [ ] ✅ Task creato appare senza refresh
- [ ] ✅ Task completato mostra strikethrough
- [ ] ✅ Task eliminato ha undo 5 secondi
- [ ] ✅ Lista vuota → empty state (non pagina bianca)
- [ ] ✅ RLS: utente non vede task di altri
- [ ] ❌ FALLISCE SE: eliminazione non è soft delete

```sql
CREATE TABLE public.tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  title TEXT NOT NULL CHECK (char_length(title) <= 200),
  description TEXT CHECK (char_length(description) <= 1000),
  status TEXT NOT NULL DEFAULT 'todo' CHECK (status IN ('todo','in_progress','done')),
  priority TEXT CHECK (priority IN ('low','medium','high')),
  deadline TIMESTAMPTZ,
  energy_required TEXT NOT NULL DEFAULT 'medium' CHECK (energy_required IN ('low','medium','high')),
  ai_suggested_today BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  deleted_at TIMESTAMPTZ
);
CREATE INDEX tasks_user_id_idx ON public.tasks(user_id);
CREATE INDEX tasks_deleted_at_idx ON public.tasks(deleted_at);
ALTER TABLE public.tasks ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users see their tasks"
ON public.tasks FOR ALL USING (auth.uid() = user_id AND deleted_at IS NULL);
```

---

### 🤖 FASE 2 (Giorni 5-9): AI Prioritization
**Prerequisito**: Fase 1 completata e testata manualmente.

#### FEATURE 2.1: Daily AI Briefing

**Logica**:
```
1. Fetch task dell'utente (status != 'done', deleted_at IS NULL)
2. Prompt per OpenAI gpt-4o-mini
3. Risposta: array 3 task IDs + spiegazione
4. Marca quei 3: ai_suggested_today = true
5. Mostra "Le tue 3 priorità di oggi" in cima alla dashboard
```

**Prompt Template** (Edge Function):
```typescript
const systemPrompt = `Sei un assistente di produttività.
Seleziona le 3 priorità del giorno da questa lista di task.
Criteri (in ordine):
1. Deadline imminente (oggi o domani = massima priorità)
2. Priorità 'high'
3. Energia 'low' o 'medium' (mattine)
4. Task più vecchi

Rispondi SOLO con JSON:
{
  "priorities": [
    {"task_id": "uuid", "reason": "Spiegazione max 20 parole in italiano"}
  ]
}`;
```

**Acceptance Criteria**:
- [ ] ✅ Mostra esattamente 3 task (o tutti se meno di 3)
- [ ] ✅ Ogni priorità ha spiegazione leggibile
- [ ] ✅ Se OpenAI fallisce → fallback: ordina per deadline + banner "AI non disponibile"
- [ ] ✅ Rigenerabile manualmente con bottone "Rigenera priorità"
- [ ] ❌ NON chiamare OpenAI più di 1 volta ogni 30 min per stesso utente

**API**:
```
POST /api/ai/daily-briefing
Auth: JWT required
Body: {}
Response: { success, data: { priorities: [{task_id, title, reason}], generated_at, fallback } }
```

---

### 🎨 FASE 3 (Giorni 10-14): Dashboard + UX Polish

#### FEATURE 3.1: Dashboard Layout

```
HEADER: Logo | "Ciao [Nome] 👋" | [Logout]

SEZIONE HERO (se briefing generato):
┌─────────────────────────────────────────────┐
│ 🎯 Le tue 3 priorità di oggi                │
│ □ [Task 1] — "Scadenza oggi"               │
│ □ [Task 2] — "Alta priorità"               │
│ □ [Task 3] — "Rimandato da 3 giorni"       │
│                           [Rigenera →]      │
└─────────────────────────────────────────────┘

TASK LIST:
Tabs: [Tutti] [Oggi] [Alta priorità] [Completati]
[+ Aggiungi task]
Lista con: checkbox, titolo, badge deadline, badge energia, cestino (hover)
```

**Acceptance Criteria**:
- [ ] ✅ Funziona su mobile, tablet, desktop
- [ ] ✅ Empty state per ogni tab
- [ ] ✅ Deadline scadute → badge rosso
- [ ] ✅ Loading skeleton durante fetch
- [ ] ✅ Transizioni animate (no flash secco)

---

## 🤖 AI CONSTRAINTS — LEGGILE PRIMA DI OGNI SESSIONE

```
FARE:
✅ Costruisci una FASE alla volta — non andare avanti senza conferma
✅ TypeScript strict (no 'any' mai)
✅ SEMPRE shadcn/ui se il componente esiste
✅ SEMPRE gestire loading, error e empty state
✅ Try/catch su ogni chiamata API
✅ API key MAI nel codice client

NON FARE:
❌ Non aggiungere feature non nel PRD
❌ Non cambiare il tech stack (chiedi prima)
❌ Non DELETE fisico su dati utente
❌ Non esporre SUPABASE_SERVICE_ROLE_KEY al client
❌ Non passare alla Fase 2 prima che Fase 1 sia testata

SE HAI DUBBI → chiedi prima di interpretare
```

---

## ❓ OPEN QUESTIONS

| # | Domanda | Priorità | Status |
|---|---------|----------|--------|
| 1 | Il briefing AI si rigenera automaticamente (cron) o solo on-demand? | Alta | 🔴 Da decidere |
| 2 | Piano free include AI o solo paid? | Alta | 🔴 Da decidere |
| 3 | Notifiche push/email per briefing mattutino? | Media | 🟡 Post-v1 |

---
*PRD Quality Score: 91/100 — 🔵 ECCELLENTE*
```

---

## 🟠 ESEMPIO 3 — PR/FAQ AMAZON-STYLE (Tipo E)
### Prodotto: "ContentCalendar AI" — Pianificatore contenuti con AI

```markdown
---
# PR/FAQ: ContentCalendar AI
**Tipo**: Validazione strategica pre-sviluppo
**Data**: GG/MM/AAAA
**Status**: DRAFT — Da validare con 5 potenziali utenti
---

## 📰 PRESS RELEASE SIMULATO

### ContentCalendar AI: Il Primo Pianificatore Contenuti che Conosce la Tua Audience Prima di Te

**Milano, [Data]** — ContentCalendar AI ha annunciato oggi il lancio della sua piattaforma che risolve il problema numero uno dei creator e delle PMI: **il blocco del "cosa pubblico questa settimana?"**

**Il Problema**
Ogni social media manager, freelance e piccola impresa spreca in media 4-6 ore a settimana a pianificare i contenuti. Non perché non abbiano idee — ma perché non sanno quali idee funzioneranno per la loro audience specifica. Il risultato è un calendario pieno di contenuti mediocri, engagement in calo, e la sensazione costante di correre senza direzione.

**La Soluzione**
ContentCalendar AI analizza il profilo social del cliente (follower, engagement history, topic di successo) e genera un piano editoriale settimanale con: topic specifici per la nicchia, format ottimale per ogni contenuto (reel, carousel, post testo), orario di pubblicazione ottimale per quella audience, e angolo narrativo differenziante rispetto ai competitor.

**Il Primo Risultato**
Nel beta con 50 creator italiani: engagement medio +34% dopo 4 settimane di utilizzo. Tempo di pianificazione ridotto da 5 ore a 45 minuti a settimana.

**Come Iniziare**
ContentCalendar AI è disponibile da oggi su contentcalendar.ai con un piano free (1 profilo social, piano mensile) e un piano Pro (€29/mese, 5 profili, piano multipiattaforma + analisi competitor).

---

## ❓ FAQ — CUSTOMER FACING

**D: Funziona anche per account piccoli (sotto 1.000 follower)?**
R: Sì. ContentCalendar AI usa i tuoi dati specifici — non benchmark di mercato. Con 500 follower sei in grado di capire cosa funziona sul tuo pubblico reale meglio che guardare cosa fanno i grandi creator.

**D: Devo dare accesso al mio account Instagram/LinkedIn?**
R: Solo accesso in lettura per analizzare le metriche esistenti. Non publichiamo mai a tuo nome senza la tua conferma manuale.

**D: Posso usarlo per più clienti se sono un social media manager?**
R: Sì. Il piano Pro gestisce fino a 5 profili. Per agenzie con più di 10 profili, contattaci per il piano Agency.

**D: In quanto tempo vedo risultati?**
R: Il piano editoriale ottimizzato richiede 2-3 settimane di dati per calibrarsi. Da settimana 4 in poi, gli utenti vedono in media +30% di engagement.

**D: ContentCalendar AI scrive anche i caption?**
R: Genera una bozza per ogni contenuto pianificato. Tu la modifichi e approvi prima della pubblicazione.

---

## ❓ FAQ — INTERNE (per il team)

**D: Come gestiamo la dipendenza dall'API di Instagram (rate limits e deprecation)?**
R: Implementiamo un layer di caching aggressivo (24h per dati non critici, 1h per metriche recenti) e manteniamo connessioni ufficiali via Meta Graph API. Rischio di deprecation monitorato attivamente.

**D: L'AI genera contenuti fuori topic o inappropriati?**
R: Ogni output passa attraverso un layer di filtro + revisione umana. Beta ha mostrato 2% di rigenera richiesti — accettabile. In v2 aggiungiamo feedback loop per migliorare.

**D: Come differenziamo da Buffer AI Assistant e Hootsuite AI?**
R: Loro generano contenuti generici. Noi generiamo piani basati sui dati specifici dell'account. La differenza è: "cosa postare in generale" vs "cosa funzionerà per la TUA audience questa settimana".

**D: Qual è il costo infrastrutturale per utente a settimana?**
R: Stimato €0.08 per utente/settimana (API OpenAI + infra). Con pricing €29/mese → margine lordo ~65%.

---

## 📊 SUCCESS METRICS CHIAVE

- **North Star**: Piano editoriale attivato entro 7 giorni dal signup — target ≥ 70%
- **Engagement improvement**: +20% engagement medio dopo 30 giorni — target 60% utenti
- **D30 retention**: ≥ 40%
- **Trial → Paid conversion**: ≥ 12% (premium per la categoria)

---

## ▶️ NEXT STEPS

1. Validazione PR/FAQ con 5 SMM italiani — Owner: PM — Deadline: [+7 giorni]
2. Se feedback positivo: avvio PRD Tipo B — Owner: PM — Deadline: [+14 giorni]
3. Se feedback negativo: pivot su angolo differente o pausa — Owner: PM — Deadline: [+7 giorni]

---
*Status: Pre-sviluppo — Non iniziare il PRD Tipo B prima della validazione*
```

---

## 🟤 ESEMPIO 4 — FEATURE SPEC (Tipo C)
### Feature: "Notifiche Real-Time" su TaskFlow (prodotto esistente)

```markdown
---
# Feature Spec: Notifiche Real-Time — TaskFlow v3.2
**Tipo**: Feature Spec (Tipo C)
**Versione**: 1.0 | **Status**: IN REVIEW 🟡
**Prodotto**: TaskFlow — SaaS project management B2B
**Autore**: PM | **Data**: GG/MM/AAAA
**Revisori**: Lead Engineering, Design Lead
**Rilascio target**: Sprint 14 (2 settimane)
---

## ⚡ TL;DR
> **Cosa aggiunge**: Sistema di notifiche in-app real-time per aggiornamenti su task assegnati, commenti e scadenze.
> **Perché ora**: Principale motivo di abbandono citato da 23% utenti nel churn survey. Competitor Asana e Linear già ce l'hanno.
> **Impatto atteso**: Riduzione churn mensile da 5.2% a 4.5% entro 60 giorni dal lancio.
> **Effort**: M — 2 settimane per 2 developer (1 BE, 1 FE).

---

## 🎯 PROBLEMA SPECIFICO E EVIDENZA

### Il Problema
Gli utenti TaskFlow perdono aggiornamenti critici sui task perché il sistema attuale richiede di caricare la pagina manualmente per vedere le modifiche.

### Evidenza Quantitativa
- **Churn survey (n=89)**: 23% degli utenti che hanno lasciato citano "mancanza di notifiche real-time" come principale motivo
- **NPS detractors interviews (n=12)**: 7/12 menzionano spontaneamente la mancanza di notifiche
- **Support tickets**: 18 richieste per notifiche negli ultimi 3 mesi
- **Competitor feature parity**: Asana, Linear, Monday — tutti hanno notifiche real-time

---

## 👤 USER STORIES CON ACCEPTANCE CRITERIA

### US-001: Notifica Assegnazione Task
**Come** membro del team,
**voglio** ricevere una notifica in-app quando mi viene assegnato un task,
**in modo da** sapere subito di nuove responsabilità senza controllare manualmente.

**Acceptance Criteria**:
- [ ] ✅ Notifica appare entro 3 secondi dall'assegnazione
- [ ] ✅ Icona campanella nell'header mostra badge con numero notifiche non lette
- [ ] ✅ Click su notifica → redirect alla pagina del task
- [ ] ✅ Notifica marcata come "letta" dopo il click
- [ ] ✅ Push notification email opzionale (toggle nelle settings)
- [ ] ❌ FALLISCE SE: notifiche non appaiono senza refresh della pagina
- [ ] ❌ FALLISCE SE: il badge non si aggiorna in real-time

**Priority**: P0 | **Effort**: M

---

### US-002: Notifica Commento su Task
**Come** utente che segue un task,
**voglio** ricevere una notifica quando qualcuno commenta,
**in modo da** mantenere il contesto delle discussioni.

**Acceptance Criteria**:
- [ ] ✅ Notifica per commenti sui task che possiedo o a cui sono assegnato
- [ ] ✅ Notifica include preview del commento (max 100 char)
- [ ] ✅ @mention notifica sempre l'utente menzionato
- [ ] ✅ Non notificare per propri commenti
- [ ] ❌ FALLISCE SE: utente riceve notifica per propri commenti

**Priority**: P0 | **Effort**: S

---

### US-003: Centro Notifiche
**Come** utente con molte notifiche,
**voglio** vedere tutte le notifiche in un pannello dedicato,
**in modo da** gestirle senza perdere il contesto di lavoro.

**Acceptance Criteria**:
- [ ] ✅ Pannello slide-out da destra (non modal fullscreen)
- [ ] ✅ Lista cronologica notifiche con: icona tipo, testo, timestamp relativo ("2 min fa")
- [ ] ✅ "Segna tutto come letto" in cima al pannello
- [ ] ✅ Scroll infinito (non paginazione) per notifiche storiche
- [ ] ✅ Notifiche non lette in bold o con indicatore blu
- [ ] ✅ Empty state: "Sei aggiornato su tutto 🎉"

**Priority**: P1 | **Effort**: M

---

## ✅ SCOPE E NON-GOALS

### IN SCOPE — Feature v1
- Notifiche in-app real-time (WebSocket via Supabase Realtime)
- Tipi: assegnazione task, commento, @mention, scadenza (24h before)
- Centro notifiche con pannello slide-out
- Badge contatore non lette sull'icona campanella
- Email notification opzionale per ogni tipo (toggle per utente)

### OUT OF SCOPE — v1
| Feature | Motivazione | Quando |
|---------|-------------|--------|
| Push notification mobile | App mobile non esiste ancora | Post-app (Q4) |
| Slack/Teams integration | Complessità alta, uso limitato | v2 — Q3 |
| Notifiche digest (settimanale) | Nice-to-have | v2 |
| Notification rules personalizzate | Molto complesso, richiede test UX | v3 |
| Suono/vibrazione desktop | Intrusivo, feedback negativo da beta | Mai (rimosso dal roadmap) |

---

## 🔌 IMPATTO SU FEATURE ESISTENTI

| Feature Esistente | Impatto | Azione Richiesta |
|-------------------|---------|------------------|
| Task assignment (già esiste) | Aggiunge trigger notifica | Aggiungi hook post-assignment |
| Comments system (già esiste) | Aggiunge trigger per commenti + @mention | Parser @mention nel testo commento |
| User settings | Aggiunge sezione "Notification Preferences" | Nuova tab nelle settings |
| Header navigation | Aggiunge campanella con badge | Componente NotificationBell |

**Rischio di regressione**:
- Assegnazione task esistente: BASSO — aggiungiamo solo hook, non modifichiamo logica
- Comments: MEDIO — il parser @mention è nuovo, richiede test su commenti esistenti

---

## ⚠️ EDGE CASES E ERROR STATES

### Edge Cases Specifici
- **Utente offline al momento della notifica** → Notifica salvata nel DB, appare al prossimo accesso
- **Utente elimina account** → Tutte le sue notifiche vengono eliminate (CASCADE)
- **Notifica su task già eliminato** → Click su notifica → mostra banner "Task non più disponibile" (non 404)
- **100+ notifiche non lette** → Badge mostra "99+" (non numero esatto)
- **Stessa notifica in loop** → Rate limiting: max 1 notifica per tipo per task per 5 minuti

### Error States
- **WebSocket connection lost** → Banner discreto in header: "Aggiornamenti in tempo reale non disponibili" + icona info
- **Email notification failed** → Retry 3 volte, poi silenzio (non bloccare il flusso principale)

---

## 📊 ANALYTICS EVENTS

```javascript
// Notifica ricevuta (solo per notifiche non lette all'apertura del pannello)
posthog.capture('notification_received', {
  user_id, notification_type: 'task_assigned'|'comment'|'mention'|'deadline',
  task_id, read_at: null
})

// Notifica cliccata
posthog.capture('notification_clicked', {
  user_id, notification_type, time_to_click_seconds
})

// "Segna tutto come letto" usato
posthog.capture('notifications_all_marked_read', {
  user_id, count_marked
})
```

---

## 🚀 ROLLOUT E ROLLBACK

### Rollout
- **Feature flag**: `realtime_notifications` — off per default, on per 10% utenti in W1
- **Week 1**: Monitor crash rate + WebSocket stability
- **Week 2**: Rollout a 100% se metriche ok

### Rollback Plan
Se crash rate aumenta > 0.5% o error rate WebSocket > 5%:
1. Disabilita feature flag → notifiche scompaiono per tutti
2. Nessun dato perso (DB preservato)
3. Investiga issue, fix, ri-deploy

---

## ❓ OPEN QUESTIONS

| # | Domanda | Owner | Status |
|---|---------|-------|--------|
| 1 | Supabase Realtime o socket.io custom? | Engineering | 🟢 Risolto: Supabase Realtime |
| 2 | Retention delle notifiche nel DB: 30 giorni o 90 giorni? | PM | 🔴 Open |
| 3 | Limite massimo notifiche non lette prima di mostrare "svuota tutto"? | Design | 🟡 In review |

---
*PRD Quality Score: 88/100 — 🟢 BUONO*
```

---

## Note Operative per PRD Architect OS

Quando generi un nuovo PRD:
1. **Usa questi esempi come benchmark** — se il tuo output è meno denso, non è finito
2. **QuickInvoice** → usa come reference per qualsiasi SaaS consumer/B2B semplice
3. **FocusBoard** → usa come reference per qualsiasi progetto vibecoding
4. **ContentCalendar AI** → usa come reference per validazione strategica pre-sviluppo
5. **Notifiche Real-Time** → usa come reference per feature spec su prodotto esistente

**Il segnale di qualità**: se leggi il PRD e puoi iniziare a sviluppare senza fare una singola domanda, il PRD è completo. Se hai ancora dubbi, il PRD non è finito.
