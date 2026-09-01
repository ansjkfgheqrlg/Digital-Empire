# REF_09 — Pricing Models SaaS
## 8 Modelli di Pricing con Implicazioni sui Requisiti del PRD

Questo file è il **reference operativo** per integrare il modello di pricing nel PRD in modo che gli sviluppatori sappiano esattamente cosa costruire — dal DB al billing flow all'UX degli upgrade.

---

## 1. Perché il Pricing Model Impatta il PRD

Il pricing non è solo marketing. È architettura di prodotto.

Ogni modello di pricing richiede una struttura tecnica diversa. Sbagliare l'architettura all'inizio significa riscrivere il billing system quando il prodotto è già in produzione — uno dei refactoring più costosi e rischiosi in assoluto.

### Le 4 aree del PRD che cambiano in base al pricing model

**1. Schema del Database**
Come tracciamo il piano di un utente, i suoi limiti, il suo utilizzo. Cambia radicalmente tra un modello per-seat e uno usage-based.

**2. Feature Gating**
Come blocchiamo o mostriamo le feature in base al piano. L'architettura del gating va nel PRD come requisito tecnico, non lasciata all'interpretazione dello sviluppatore.

**3. Billing Complexity**
Quanto è complessa l'integrazione con Stripe (o equivalente). Usage-based richiede Stripe Metered Billing, che ha logiche diverse dal semplice abbonamento fisso.

**4. UX degli Upgrade**
Il flusso che vede l'utente quando incontra un limite o vuole passare a un piano superiore. Questo flusso va progettato nel PRD — non improvvisato durante lo sviluppo.

### Il costo dell'upgrade architecture sbagliata

Uno dei casi più comuni: si parte con un modello flat-rate senza feature gating, poi si vuole introdurre piani diversi. Risultato: refactoring di tutta la UI per aggiungere i check di piano, refactoring del DB per aggiungere la logica di subscription, migrazione degli utenti esistenti. Settimane di lavoro. Zero valore per il cliente finale.

**Regola**: il modello di pricing va nel PRD. Non nella roadmap. Non nel documento di marketing. **Nel PRD, con le implicazioni tecniche.**

---

## 2. I 8 Modelli di Pricing

---

### MODELLO 1 — FREEMIUM

**Descrizione**
Gli utenti accedono a una versione gratuita permanente del prodotto con limitazioni. L'upgrade al piano a pagamento sblocca funzionalità avanzate, limiti più alti, o rimuove le restrizioni.

**Come funziona tecnicamente**
L'utente ha un piano `free` assegnato di default al signup. Le feature sono gatate in base al piano. Non c'è un trial con scadenza — il piano free è permanente.

**Implicazioni PRD Specifiche**
```
Nel PRD devi definire obbligatoriamente:
1. La feature wall: esattamente quale feature è free vs paid (tabella esplicita)
2. I limiti quantitativi: quanti progetti/documenti/utenti/GB su free
3. Il trigger di upgrade: quando l'utente vede il prompt di upgrade?
   - Quando raggiunge il 80% del limite? 100%?
   - Quando clicca su una feature premium?
4. Il messaggio di upgrade: cosa vede l'utente (copy + CTA + piano suggerito)
5. La conversione dei free users: come vengono convertiti in trial o paid
```

**Feature Gating Richieste**
- Per ogni feature premium: check del piano prima del render/esecuzione
- Limite tracking: contatore aggiornato ad ogni utilizzo
- Upgrade prompt: componente UI riutilizzabile chiamato quando si raggiunge un limite

**Billing Complexity**: BASSA — nessuna complessità billing per il tier free. Solo per il tier paid.

**Esempi di Prodotti Noti**
Notion, Spotify, Dropbox, Mailchimp (fino a X contatti), Trello, Canva, Figma (piano free con limitazioni), HubSpot CRM (free + paid tiers).

**When to Use**
- Il prodotto ha un chiaro valore anche nella versione limitata (gli utenti devono sperimentare il valore per upgradare)
- Il CAC (Customer Acquisition Cost) è alto — il free tier abbassa la barriera di ingresso
- Il prodotto ha network effects (più utenti free = più valore per tutti)
- Il costo per servire un utente free è basso (sotto €0.50/mese)

**Attenzione**: il freemium funziona solo se la feature wall è nel posto giusto. Troppo generoso = nessuno upgrada. Troppo restrittivo = nessuno capisce il valore.

---

### MODELLO 2 — FREE TRIAL

**Descrizione**
L'utente accede a tutte le funzionalità del prodotto (o del piano scelto) per un periodo limitato (tipicamente 7, 14, o 30 giorni), poi deve sottoscrivere un abbonamento per continuare.

**Come funziona tecnicamente**
Al signup viene assegnato un piano trial con una data di scadenza (`trial_ends_at`). Alla scadenza, il piano viene automaticamente downgraded (a free, se esiste) o bloccato finché non si inserisce il metodo di pagamento.

**Implicazioni PRD Specifiche**
```
Nel PRD devi definire obbligatoriamente:
1. Durata del trial: 7, 14, o 30 giorni (e perché — es: ciclo di acquisto del target)
2. Credit card required?: trial con o senza carta di credito (impatta conversion ma riduce churn)
3. Trial-to-paid flow: cosa succede alla scadenza? Downgrade automatico? Blocco?
4. Reminder email sequence: a che punto del trial si mandano i reminder?
   - Giorno 3: "Ti stai trovando bene?"
   - Giorno X-3: "Il tuo trial scade tra 3 giorni"
   - Giorno X: "Il tuo trial è scaduto"
5. Cosa succede ai dati post-scadenza: vengono preservati? Per quanto?
   - Es: "I dati vengono conservati 30 giorni dopo la scadenza del trial"
```

**Feature Gating Richieste**
- `trial_ends_at` timestamp nel profilo utente/account
- Middleware che controlla la validità del trial ad ogni request
- Banner "X giorni rimasti al trial" nell'UI
- Blocco dell'accesso o downgrade automatico post-scadenza

**Billing Complexity**: BASSA-MEDIA — più semplice di usage-based ma richiede gestione degli stati trial/expired.

**Esempi di Prodotti Noti**
Netflix (trial storico, ora eliminato), Salesforce, Shopify (14 giorni), Intercom, Zapier, Adobe Creative Cloud.

**When to Use**
- Il prodotto richiede onboarding e configurazione prima di mostrare il valore (gli utenti hanno bisogno di tempo)
- Il valore è chiaro ma l'investimento iniziale è percepito come rischioso
- Vuoi massimizzare la qualità delle prove (utenti motivati) — specialmente con trial richiedendo carta
- Il prodotto è B2B con ciclo di vendita medio-lungo

---

### MODELLO 3 — FLAT RATE

**Descrizione**
Un unico prezzo per tutto. Tutti gli utenti pagano lo stesso importo e hanno accesso a tutte le funzionalità.

**Come funziona tecnicamente**
La struttura di billing è la più semplice possibile: una subscription con un price_id fisso. Nessun gating, nessun limite da tracciare, nessuna logica di piano.

**Implicazioni PRD Specifiche**
```
Nel PRD devi definire:
1. L'unico prezzo (mensile e/o annuale con sconto)
2. La lista completa delle feature incluse (tutte)
3. I limiti tecnici (se presenti — es: storage massimo)
4. La politica di rimborso / cancellazione
5. Come gestire la fase tra signup e prima fatturazione (di solito: trial di N giorni)
```

**Feature Gating Richieste**
- Nessuna gating per funzionalità (accesso pieno a tutto)
- Solo gating binario: utente ha subscription attiva? Sì → accesso. No → paywall.

**Billing Complexity**: MOLTO BASSA — la più semplice da implementare. Una subscription, un prezzo.

**Esempi di Prodotti Noti**
Basecamp ($99/mese flat per team qualsiasi dimensione), Hey (email), Transistor (podcast hosting).

**When to Use**
- Prodotto con funzionalità stabili e ben definite (non molte variabili da misurare)
- Target con alta sensibilità alla semplicità e prevedibilità del prezzo
- Vuoi minimizzare la complessità di sviluppo del billing system
- Il tuo mercato è principalmente individui o piccoli team con bisogni omogenei

**Attenzione**: il flat rate lascia soldi sul tavolo con i clienti enterprise che usano il prodotto intensamente. Spesso si introduce un enterprise tier dopo.

---

### MODELLO 4 — PER-SEAT

**Descrizione**
Il prezzo è moltiplicato per il numero di utenti attivi nell'account. Più persone usano il prodotto, più si paga.

**Come funziona tecnicamente**
Ogni account (organization/workspace) ha un contatore di `active_seats`. Il totale fatturato = seats × price_per_seat. Stripe usa il quantity parameter nella subscription.

**Implicazioni PRD Specifiche**
```
Nel PRD devi definire obbligatoriamente:
1. Definizione di "seat": cosa conta come seat? (invited user? active in last 30 days? any user?)
2. Minimum seats: esiste un minimo di seat acquistabili?
3. Seat management UI: chi può aggiungere/rimuovere seat? Solo admin?
4. Proration: se si aggiunge un seat a metà mese, come viene calcolata la fattura?
   - Stripe gestisce questo automaticamente con proration enabled
5. Unused seats: se si rimuove un utente, il seat diventa disponibile per un altro o viene rimborsato?
6. Overage: se si supera il numero di seat acquistati (es: admin invita più utenti del previsto)
   - Opzione A: blocca l'invito finché non si acquistano più seat
   - Opzione B: auto-add seat e fattura alla prossima invoice
```

**Schema DB per seat tracking**:
```sql
CREATE TABLE organization_subscriptions (
  id UUID PRIMARY KEY,
  organization_id UUID REFERENCES organizations(id),
  stripe_subscription_id VARCHAR,
  plan_id VARCHAR, -- 'pro_monthly', 'pro_annual'
  seats_purchased INTEGER NOT NULL,
  seats_used INTEGER GENERATED ALWAYS AS (
    SELECT COUNT(*) FROM organization_members 
    WHERE organization_id = organization_subscriptions.organization_id 
    AND status = 'active'
  ) STORED,
  billing_cycle_anchor TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ
);
```

**Feature Gating Richieste**
- Check `seats_used < seats_purchased` prima di ogni invito utente
- UI per aggiungere seat direttamente dal pannello di billing (senza contattare il supporto)
- Notifica all'admin quando si avvicina al limite di seat (es: a 90%)

**Billing Complexity**: MEDIA — la gestione della prorazione e degli upgrade/downgrade di seat richiede attenzione.

**Esempi di Prodotti Noti**
Slack, Figma, Linear, Notion (team plan), Airtable, GitHub, Jira.

**When to Use**
- Il prodotto è collaborativo — più persone lo usano nello stesso account
- Il valore cresce con il numero di utenti (network effects interni al team)
- Il target sono aziende con team di dimensione variabile
- Vuoi che il revenue cresca automaticamente man mano che cresce il cliente

---

### MODELLO 5 — USAGE-BASED (PAY-AS-YOU-GO)

**Descrizione**
Il prezzo è proporzionale all'utilizzo effettivo: API call, gigabyte di storage, transazioni processate, minuti di video, messaggi inviati. Non si paga un fisso mensile — si paga per ciò che si consuma.

**Come funziona tecnicamente**
Il sistema deve tracciare il consumo in tempo reale (o quasi), aggregarlo per periodo di billing, e passare il dato a Stripe come metered billing. Stripe genera l'invoice a fine periodo basandosi sul consumo riportato.

Stripe Metered Billing funziona così:
1. Si crea un SubscriptionItem con `usage_type: metered`
2. Ad ogni unità consumata, si chiama `stripe.subscriptionItems.createUsageRecord()`
3. Stripe aggrega e fattura a fine periodo

**Implicazioni PRD Specifiche**
```
Nel PRD devi definire obbligatoriamente:
1. L'unità di misura: cos'è esattamente "1 unità" (1 API call? 1MB? 1 email?)
2. Il prezzo per unità: €X per 1 unità (o per 1000 unità — dipende dalla granularità)
3. Free tier / incluso: quante unità sono incluse prima che si inizi a pagare?
4. Spending cap: esiste un limite di spesa mensile? (importante per evitare bill shock)
5. Il sistema di metering: come tracciamo il consumo?
   - Database counter aggiornato sincrono? (semplice ma non scalabile)
   - Event stream (Kafka/Redis) → aggregazione asincrona? (scalabile)
   - Direct Stripe reporting? (affidabile ma con latency)
6. La dashboard di utilizzo per l'utente: deve essere visibile in real-time
7. Gli alert di soglia: notifica quando si raggiunge X% del budget
```

**Schema DB per usage tracking**:
```sql
CREATE TABLE usage_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  account_id UUID NOT NULL REFERENCES accounts(id),
  metric VARCHAR(50) NOT NULL, -- 'api_calls', 'storage_gb', 'emails_sent'
  quantity DECIMAL NOT NULL,
  recorded_at TIMESTAMPTZ DEFAULT NOW(),
  billing_period VARCHAR(7), -- '2025-01' formato YYYY-MM
  stripe_usage_record_id VARCHAR -- per idempotency
);

CREATE INDEX idx_usage_records_account_period 
  ON usage_records(account_id, billing_period, metric);
```

**Feature Gating Richieste**
- Usage tracking middleware su ogni endpoint/azione che consuma unità
- Dashboard real-time del consumo corrente vs budget
- Alert email quando si raggiunge 80% / 100% del budget impostato
- Hard cap opzionale (blocco al 100% del budget) o soft cap (over-usage fatturato)

**Billing Complexity**: ALTA — la più complessa da implementare correttamente. Richiede: sistema di metering, idempotency, riconciliazione, dashboard real-time.

**Esempi di Prodotti Noti**
Stripe (% per transazione), AWS (tutto), Twilio (SMS/chiamata), SendGrid (email inviate), OpenAI API (token), Cloudflare Workers (requests).

**When to Use**
- Il valore consegnato è direttamente correlato all'utilizzo (pago quanto uso, uso quanto voglio)
- Il consumo è molto variabile tra utenti (alcuni usano 10x più di altri)
- Il target sono developer o technical users abituati a modelli pay-as-you-go
- Vuoi abbassare la barriera di ingresso (nessun costo fisso alto)

---

### MODELLO 6 — TIERED

**Descrizione**
3-5 piani fissi con prezzi diversi, ognuno con un set di feature diverse e/o limiti diversi. L'utente sceglie il piano più adatto alla propria situazione.

**Come funziona tecnicamente**
Ogni account ha un `plan_id` che determina a quali feature ha accesso e quali limiti si applicano. I piani sono fissi nel catalogo. Stripe gestisce subscription con diversi price_id.

**Implicazioni PRD Specifiche**
```
Nel PRD devi definire obbligatoriamente:
1. La tabella piani completa: per ogni piano, ogni feature, ogni limite — nessun "da definire"
2. La feature wall tra piani: esattamente dove è la linea tra Starter e Pro, tra Pro e Business
3. Il piano "anchor": quello più caro che fa sembrare gli altri convenienti
4. L'upgrade flow: come avviene tecnicamente il passaggio da piano inferiore a superiore?
   - Immediato o alla prossima rinnovazione?
   - Con proration?
   - L'utente perde dati/contenuti creati sopra il limite del nuovo piano?
5. Il downgrade flow: spesso ignorato nel PRD — specifica cosa succede ai dati
6. La "recommended" badge: quale piano vuoi spingere?
```

**Feature Gating Richieste**
- `plan_id` su ogni account con lookup alle features e limiti del piano
- Tabella di configurazione piani (idealmente dinamica, non hardcoded):
```sql
CREATE TABLE plan_features (
  plan_id VARCHAR(50) NOT NULL,
  feature_key VARCHAR(100) NOT NULL,
  value JSONB NOT NULL, -- true/false per flag, numero per limiti
  PRIMARY KEY (plan_id, feature_key)
);
-- esempio record:
-- ('starter', 'max_projects', 3)
-- ('pro', 'max_projects', 999999)
-- ('starter', 'ai_features', false)
-- ('pro', 'ai_features', true)
```

**Billing Complexity**: MEDIA — abbonamenti multipli ma tutti fissi. Stripe gestisce bene con price_id diversi.

**Esempi di Prodotti Noti**
HubSpot, Mailchimp, Intercom, ConvertKit, ActiveCampaign, Webflow, Ghost.

**When to Use**
- Il prodotto serve segmenti diversi con esigenze molto diverse (freelance vs team vs enterprise)
- Vuoi ottimizzare il revenue catturando diversi livelli di willingness-to-pay
- Le feature differenziatrici tra piani sono chiare e percepite come preziose
- Il prodotto è abbastanza maturo da conoscere bene i segmenti di clientela

---

### MODELLO 7 — PER-FEATURE (ADD-ONS)

**Descrizione**
Un prodotto core (spesso a prezzo fisso base) con moduli aggiuntivi opzionali acquistabili separatamente. L'utente costruisce il proprio "stack" di funzionalità pagando solo per ciò che usa.

**Come funziona tecnicamente**
L'utente ha un piano base + una lista di add-on attivi. Ogni add-on è una subscription separata o un item aggiuntivo nella stessa subscription Stripe.

**Implicazioni PRD Specifiche**
```
Nel PRD devi definire obbligatoriamente:
1. Il prodotto core: cosa è incluso nel base e a che prezzo
2. La lista degli add-on: nome, prezzo, descrizione, feature incluse
3. Le dipendenze tra add-on: alcuni add-on richiedono altri per funzionare?
4. Il limite di add-on per piano: tutti possono comprare tutti gli add-on o ci sono restrizioni?
5. Il billing degli add-on: si aggiungono alla subscription esistente (Stripe: add subscription item)
6. La UI di acquisto add-on: dove si comprano? Settings > Billing > Add-ons? 
   O si trovano contestualmente nella UI quando si cerca di usare la feature?
```

**Feature Gating Richieste**
```sql
-- Tabella per tracciare gli add-on attivi per account
CREATE TABLE account_addons (
  account_id UUID REFERENCES accounts(id),
  addon_id VARCHAR(50) NOT NULL, -- 'advanced_analytics', 'white_label', 'api_access'
  stripe_subscription_item_id VARCHAR,
  activated_at TIMESTAMPTZ DEFAULT NOW(),
  expires_at TIMESTAMPTZ,
  PRIMARY KEY (account_id, addon_id)
);
```
- Check `EXISTS (SELECT 1 FROM account_addons WHERE account_id = ? AND addon_id = 'feature_x')` prima di ogni uso della feature premium

**Billing Complexity**: MEDIA-ALTA — ogni add-on è un subscription item separato. La logica di billing può diventare complessa con molti add-on.

**Esempi di Prodotti Noti**
Zendesk (moduli aggiuntivi), WooCommerce (plugin a pagamento), Xero (payroll add-on), GitHub (Actions minutes, Copilot), Shopify (app marketplace).

**When to Use**
- Il prodotto ha funzionalità molto diverse usate da segmenti diversi
- Non vuoi obbligare tutti a pagare per funzionalità che usano in pochi
- Vuoi massimizzare il revenue con upsell mirati
- Il prodotto è complesso e serve flessibilità di configurazione

---

### MODELLO 8 — ONE-TIME PAYMENT

**Descrizione**
L'utente paga una volta e ottiene accesso permanente al prodotto (o a una versione specifica). Nessun abbonamento ricorrente.

**Come funziona tecnicamente**
Un singolo payment con Stripe (non una subscription). Al completamento del pagamento, viene aggiornato il flag `is_lifetime` o `has_purchased_version_X` sul profilo utente.

**Implicazioni PRD Specifiche**
```
Nel PRD devi definire obbligatoriamente:
1. Cosa include esattamente il one-time payment (feature, versione, durata degli aggiornamenti)
2. La politica aggiornamenti: accesso agli aggiornamenti incluso? Per quanto?
   - "Accesso a vita alla versione 1.x" vs "Accesso a vita + tutti i futuri aggiornamenti"
3. Come viene gestito un major upgrade (v1 → v2): pagamento aggiuntivo richiesto?
4. La politica di rimborso: diversa da subscription (tipicamente 30 giorni no-question-asked)
5. Il modello post-payment: l'utente accede via login? Riceve un download? Una licenza key?
6. Come gestire utenti lifetime vs subscription nella stessa codebase
```

**Feature Gating Richieste**
```sql
-- Approccio semplice per lifetime access
ALTER TABLE users ADD COLUMN is_lifetime_customer BOOLEAN DEFAULT FALSE;
ALTER TABLE users ADD COLUMN lifetime_purchase_date TIMESTAMPTZ;
ALTER TABLE users ADD COLUMN lifetime_plan_version VARCHAR(10); -- '1.0', '2.0'

-- Nel feature check:
-- has_access = user.is_lifetime_customer OR (user.subscription_status = 'active')
```

**Billing Complexity**: BASSA — un singolo Stripe payment, nessuna subscription ricorrente.

**Esempi di Prodotti Noti**
Notion (templates), Gumroad (ebook, template), Lemon Squeezy (digital products), Screenium, Affinity (alternative Adobe), alcuni plugin Figma, corsi online (Teachable/Gumroad).

**When to Use**
- Prodotto digitale senza costi variabili di mantenimento (ebook, template, plugin)
- Target con forte resistenza agli abbonamenti ricorrenti
- Prodotto stabile che non richiede infrastruttura cloud continuativa
- Strategia di acquisizione (LTD — Lifetime Deal per early adopters)

**Attenzione**: il LTD è spesso usato come strategia di lancio (AppSumo), non come modello definitivo. Se il prodotto richiede server/infrastruttura, molti LTD sono insostenibili economicamente nel lungo periodo.

---

## 3. Matrice Decisionale — Quale Modello Scegliere

| Scenario | Modello Consigliato | Motivo |
|---|---|---|
| SaaS B2C, valore immediato, acquisizione volume | Freemium | Abbassa barriera, scala con word-of-mouth |
| SaaS B2B, ciclo vendita >30 giorni | Free Trial (14-30gg) | Permette onboarding senza rischio percepito |
| Tool creativo/produttività per individui | Flat Rate o Tiered | Semplicità e prevedibilità |
| Platform collaborativa per team | Per-Seat | Revenue cresce con crescita del cliente |
| API / developer tool | Usage-Based | Allineato al valore consegnato |
| SaaS con segmenti molto diversi (SMB vs Enterprise) | Tiered (3-4 piani) | Cattura willingness-to-pay diversa |
| Piattaforma con moduli opzionali complessi | Per-Feature Add-Ons | Flessibilità + upsell mirati |
| Template, ebook, plugin | One-Time Payment | Adatto a prodotti digitali senza infrastruttura |
| SaaS con molti early adopters da monetizzare | Free Trial → Paid | Converti il traction iniziale |
| Infrastructure SaaS (storage, compute) | Usage-Based | Standard del settore |
| Tool enterprise con contratti annuali | Tiered + Annual discount | Allineato al ciclo di budget enterprise |

---

## 4. Implicazioni Tecniche nel PRD — Schema per Modello

### SCHEMA DB BASE — Struttura Universale

Indipendentemente dal modello, ogni SaaS con billing ha bisogno di:

```sql
-- Core billing tables (valide per tutti i modelli)
CREATE TABLE accounts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255),
  owner_user_id UUID REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  account_id UUID NOT NULL REFERENCES accounts(id),
  stripe_subscription_id VARCHAR UNIQUE,
  stripe_customer_id VARCHAR NOT NULL,
  plan_id VARCHAR(50) NOT NULL, -- 'free', 'starter', 'pro', 'enterprise'
  status VARCHAR(20) NOT NULL, -- 'active', 'trialing', 'past_due', 'canceled', 'paused'
  trial_ends_at TIMESTAMPTZ,
  current_period_start TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ,
  cancel_at_period_end BOOLEAN DEFAULT FALSE,
  canceled_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### STRIPE SETUP PER MODELLO

| Modello | Stripe Product Type | Stripe Price Config | Note |
|---|---|---|---|
| Freemium | Recurring | price con interval month/year | Free tier: nessuna subscription Stripe |
| Free Trial | Recurring | `trial_period_days: N` nel price | O gestire trial_ends_at lato app |
| Flat Rate | Recurring | Un singolo price | Il più semplice |
| Per-Seat | Recurring | `billing_scheme: per_unit`, `quantity: N` | Aggiornare quantity a ogni aggiunta/rimozione seat |
| Usage-Based | Recurring | `usage_type: metered`, `aggregate_usage: sum` | Richiedere createUsageRecord ad ogni consumo |
| Tiered | Recurring | price diversi per ogni piano | Upgrade = switch price_id |
| Per-Feature | Recurring | Subscription + Subscription Items | Ogni add-on = item separato |
| One-Time | One-off (non recurring) | `type: one_time` | Payment Intent, non Subscription |

### UPGRADE / DOWNGRADE FLOW

**Il flusso più delicato da documentare nel PRD — spesso ignorato.**

```
Upgrade Flow (piano inferiore → superiore):

1. L'utente clicca "Upgrade" da Settings > Billing o da upgrade prompt
2. Scelta del nuovo piano
3. Conferma con preview dell'addebito (inclusa proration)
4. Stripe: subscriptions.update() con nuovo price_id
   - proration_behavior: 'create_prorations' (addebitare subito la differenza)
   - o 'none' (iniziare il nuovo piano al prossimo rinnovo — più semplice UX)
5. Immediate access: l'utente ottiene immediatamente le nuove feature
6. Email di conferma

Downgrade Flow (piano superiore → inferiore):

1. L'utente richiede il downgrade
2. Warning: "Perderai accesso a [lista feature]. I tuoi dati sopra il limite X
   (es: progetti oltre il massimo del nuovo piano) saranno in read-only."
3. Conferma
4. Stripe: subscriptions.update() con cancel_at_period_end: true per il vecchio piano
   + scheduled update per il nuovo piano
5. Il downgrade effettivo avviene al termine del periodo già pagato
6. Email di conferma con data effettiva del downgrade
```

---

## 5. Feature Gating Patterns — 3 Approcci

### PATTERN A — Database-Level Plan Field

**Come funziona**: ogni account/user ha un `plan_id` nel DB. Ogni feature check va a leggere il piano e confronta con la configurazione.

```typescript
// Esempio implementazione
async function hasFeatureAccess(
  accountId: string, 
  featureKey: string
): Promise<boolean> {
  const account = await db.accounts.findById(accountId, { 
    include: 'subscription' 
  });
  
  const planConfig = PLAN_FEATURES[account.subscription.plan_id];
  return planConfig?.[featureKey] ?? false;
}

// Configurazione piani (può stare nel DB o nel codice)
const PLAN_FEATURES = {
  free: {
    max_projects: 3,
    ai_features: false,
    export_csv: false,
    team_members: 1,
  },
  pro: {
    max_projects: Infinity,
    ai_features: true,
    export_csv: true,
    team_members: 10,
  },
  enterprise: {
    max_projects: Infinity,
    ai_features: true,
    export_csv: true,
    team_members: Infinity,
    sso: true,
    audit_log: true,
  }
};
```

**Pro**: semplice da implementare, nessuna dipendenza esterna, facile da debuggare.
**Contro**: ogni cambio ai piani richiede un deploy. Nessuna possibilità di A/B test sul pricing.

**Quando usarlo**: prodotti early-stage, piani stabili, team piccolo.

---

### PATTERN B — Feature Flags

**Come funziona**: strumento dedicato (LaunchDarkly, Unleash, o sistema custom) gestisce i flag. I piani di pricing diventano segmenti di utenti nel sistema di flag.

```typescript
// Con LaunchDarkly
const showAIFeatures = await ldClient.variation(
  'ai-features-enabled', 
  { key: user.id, custom: { plan: user.plan } },
  false // default value
);

// Con sistema custom (simple implementazione Redis-based)
async function isFeatureEnabled(userId: string, flag: string): Promise<boolean> {
  const userPlan = await getUserPlan(userId);
  const flagConfig = await redis.get(`feature_flag:${flag}`);
  const config = JSON.parse(flagConfig);
  return config.enabled_plans.includes(userPlan);
}
```

**Pro**: cambio configurazione senza deploy. A/B test su pricing. Roll-out graduale di feature. Utile anche per feature non legate al billing.
**Contro**: dipendenza esterna (costo + latency). Complessità aggiuntiva. Potenziale single point of failure se non gestito con fallback.

**Quando usarlo**: prodotti in fase di crescita, team che fa A/B test frequenti, prodotti con molti piani e feature.

---

### PATTERN C — Stripe Entitlements (2024+)

**Come funziona**: Stripe ha introdotto un sistema di entitlements nativi che collega i prodotti Stripe alle feature del tuo applicativo. Non serve più sincronizzare lo stato Stripe con il tuo DB — chiedi direttamente a Stripe se l'utente ha diritto a una feature.

```typescript
// Stripe SDK
const customer = await stripe.customers.retrieve(customerId, {
  expand: ['subscriptions', 'subscriptions.data.items.data.price.product']
});

// Oppure con Stripe Entitlements (beta 2024)
const entitlements = await stripe.entitlements.activeEntitlements.list({
  customer: customerId,
});

const hasAIFeatures = entitlements.data.some(
  e => e.lookup_key === 'ai_features'
);
```

**Pro**: fonte di verità unica (Stripe). Nessuna sincronizzazione da gestire. Riduce bug da stato inconsistente.
**Contro**: feature in beta/evoluzione al momento. Dipendenza totale da Stripe. Latency per ogni check se non cachato.

**Quando usarlo**: prodotti che già usano Stripe estensivamente, team che preferisce ridurre la complessità del DB billing.

---

**Template Acceptance Criteria per Feature Gating nel PRD**:

```markdown
### Feature: [Nome Feature Premium]

**Livello minimo di piano**: [es: Pro]

Acceptance Criteria:
- PASSA SE: utenti su piano Free vedono il componente in read-only/blurred con overlay "Upgrade to Pro"
- PASSA SE: utenti su piano Pro vedono e possono usare la feature senza restrizioni
- PASSA SE: l'overlay di upgrade mostra chiaramente il prezzo del piano Pro e un CTA diretto
- PASSA SE: cliccando l'overlay si apre il flow di upgrade (non rimanda a una pagina generica di pricing)
- PASSA SE: dopo l'upgrade, l'utente ha accesso immediato alla feature senza necessità di logout/login
- PASSA SE: un utente Free non può accedere alla feature tramite manipolazione diretta dell'URL o API call diretta
  (il check del piano è server-side, non solo client-side)
```

---

## 6. Template Sezione Billing per PRD

```markdown
## 💳 BILLING E PRICING

### Modello di Pricing: [tipo — es: Tiered, Per-Seat, Usage-Based]

---

### Piani e Prezzi

| Piano | Prezzo Mensile | Prezzo Annuale | Target Segmento |
|---|---|---|---|
| [Nome Piano 1] | €X/mese | €Y/anno (save Z%) | [descrizione target] |
| [Nome Piano 2] | €X/mese | €Y/anno | |
| [Nome Piano 3] | Custom | Custom | Enterprise |

**Piano in evidenza** (recommended badge): [nome piano]

---

### Feature per Piano

| Feature | [Piano 1] | [Piano 2] | [Piano 3] |
|---|---|---|---|
| [Feature 1] | ✓ | ✓ | ✓ |
| [Feature 2] | ✗ | ✓ | ✓ |
| [Feature 3] | ✗ | ✗ | ✓ |
| Max [risorsa] | N | M | Unlimited |
| Max utenti | 1 | 5 | Unlimited |
| Support | Email | Priority | Dedicated |

---

### Upgrade Flow

1. Utente raggiunge un limite / clicca su feature premium
2. Appare modal/overlay: "[Feature] disponibile dal piano [X]"
3. Preview del prezzo con proration (se upgrade mid-cycle)
4. Click "Upgrade" → Stripe checkout o payment confirmation
5. Conferma → accesso immediato al nuovo piano
6. Email di conferma con dettagli billing

**Proration policy**: [immediata con credito / a partire dal prossimo ciclo]

---

### Downgrade Flow

1. Utente richiede downgrade da Settings > Billing
2. Warning: "Il downgrade avverrà il [data fine periodo]. Perderai accesso a [lista feature]."
3. Dati sopra il limite del nuovo piano: [read-only / eliminati dopo X giorni / esportabili]
4. Conferma
5. Il downgrade è effettivo il [data fine periodo attuale]

---

### Feature Gating Rules

| Feature | Piano Minimo | Comportamento se sotto piano | Upgrade CTA |
|---|---|---|---|
| [Feature premium 1] | Pro | Overlay con messaggio + CTA | Modal upgrade immediato |
| [Feature premium 2] | Business | Nascosta nell'UI | Banner in Settings |
| Max [risorsa] superato | Pro | Blocco azione + messaggio | Modal upgrade |

---

### Stripe Configuration

- **Product ID**: [da compilare con ID reale in fase di development]
- **Price IDs**: 
  - [Piano 1] Monthly: `price_xxx`
  - [Piano 1] Annual: `price_yyy`
  - [Piano 2] Monthly: `price_zzz`
- **Billing Scheme**: [per_unit / tiered / volume / metered]
- **Trial**: [N giorni / nessun trial]
- **Proration**: [create_prorations / none]

---

### Webhook Events da Gestire

| Stripe Event | Azione nel Sistema |
|---|---|
| `customer.subscription.created` | Attiva piano, invia email benvenuto |
| `customer.subscription.updated` | Aggiorna piano_id nel DB |
| `customer.subscription.deleted` | Downgrade a free o blocco accesso |
| `invoice.payment_succeeded` | Log pagamento, rinnova accesso |
| `invoice.payment_failed` | Email warning, grace period 7 giorni |
| `customer.subscription.trial_will_end` | Email reminder 3 giorni prima |

---

### Idempotency e Reliability

- Tutti i webhook handler sono idempotenti (verificare event ID già processato)
- Stripe webhook signature verification obbligatoria
- Fallback: se Stripe è irraggiungibile, l'utente mantiene il suo piano corrente (fail open)
- Log di tutti gli eventi billing per audit e debugging
```
