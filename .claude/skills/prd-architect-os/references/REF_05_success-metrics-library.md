# REF_05 — Success Metrics Library

## Database Metriche di Successo per Categoria di Prodotto

---

## Introduzione: North Star / Primary / Guardrail Framework

Ogni PRD deve definire metriche di successo prima che lo sviluppo inizi. Non dopo. Le metriche definite a posteriori tendono a essere selezionate per giustificare risultati già ottenuti, non per guidare decisioni.

Il framework standard a tre livelli:

### North Star Metric (1 sola)
La singola metrica che cattura il valore core che il prodotto crea per i suoi utenti. Non la metrica più facile da muovere (sessioni, pageviews), ma quella che meglio predice la crescita sostenibile a lungo termine.

**Caratteristiche di una buona North Star:**
- Misura il valore ricevuto dall'utente, non solo l'attività
- Se cresce, la retention tende a migliorare automaticamente
- Tutte le feature possono essere valutate in base all'impatto su di essa
- È comprensibile da tutti i team (non solo analytics)

**Anti-pattern North Star:**
- Revenue (lagging indicator, non misura valore utente)
- DAU/MAU senza contesto (misura presenza, non valore)
- Sessioni/pageviews (misura attività, non outcome)

### Primary Metrics (3-5)
Le metriche che il team ottimizza attivamente sprint per sprint. Coprono le dimensioni critiche: acquisition, activation, retention, revenue. Devono essere correlate alla North Star ma misurabili su timeframe più brevi.

### Guardrail Metrics (2-4)
Le metriche che NON devono peggiorare. Servono a impedire che l'ottimizzazione delle Primary Metrics danneggi silenziosamente altre dimensioni critiche.

**Esempio concreto:**
- Se ottimizzi il conversion rate (Primary) aggiungendo dark patterns → il NPS scenderà (Guardrail)
- Se ottimizzi il tempo di load → il tasso di errore non deve aumentare (Guardrail)
- Se aumenti email marketing → l'unsubscribe rate non deve superare la soglia (Guardrail)

---

## A. SaaS Consumer (B2C)

### Retention Benchmarks

La retention è la metrica più predittiva della crescita SaaS. Questi benchmark sono derivati da analisi di settore (Andreessen Horowitz, Mixpanel Industry Benchmarks, Amplitude Benchmark Report).

| Timeframe | Best-in-class | Buono | Accettabile | Problematico |
|-----------|--------------|-------|-------------|--------------|
| **D1 (Day 1)** | >60% | 40-60% | 25-40% | <25% |
| **D7 (Day 7)** | >30% | 20-30% | 10-20% | <10% |
| **D30 (Day 30)** | >15% | 8-15% | 3-8% | <3% |
| **M3 (Month 3)** | >10% | 5-10% | 2-5% | <2% |

**Variazione per categoria:**

| Categoria App | D7 Retention | D30 Retention | Note |
|---------------|-------------|---------------|------|
| Productivity (Notion-like) | 25-40% | 15-25% | Alto se diventa habit |
| Fitness/Health | 20-35% | 10-20% | Alto churn dopo picchi motivazionali |
| Finance/Budgeting | 15-25% | 8-15% | Stagionale (inizio anno) |
| Learning/Education | 20-30% | 10-18% | Cohort-based migliora retention |
| Social/Community | 30-50% | 20-35% | Network effects |
| AI Tools (consumer) | 20-35% | 8-15% | Alta novelty, churn rapido se valore non chiaro |

### Conversion Trial → Paid

| Modello | Benchmark tipico | Best-in-class |
|---------|-----------------|---------------|
| **Freemium** (free tier permanente) | 2-5% | 8-12% |
| **Free trial** (14 giorni senza CC) | 8-15% | 20-25% |
| **Free trial** (con CC richiesta) | 40-60% | 70%+ |
| **Reverse trial** (Pro gratuito → downgrade) | 15-25% | 30%+ |

### Time-to-Value (TTV)

Il TTV è il tempo tra signup e il momento in cui l'utente sperimenta il "valore core" del prodotto per la prima volta. È il predictor più forte della retention a D7.

| Target TTV | Categoria | Metodo misura |
|-----------|-----------|---------------|
| <2 minuti | Tool con output immediato (AI, generatori) | Timestamp primo output generato |
| <10 minuti | App produttività (task manager, note) | Timestamp primo item creato + salvato |
| <30 minuti | App più complesse (CRM, project management) | Timestamp primo "momento AHA" (definito per prodotto) |
| <1 settimana | Marketplace, community | Timestamp prima transazione/connessione |

### NPS Benchmark per Tipo App

| Categoria | NPS Buono | NPS Eccellente |
|-----------|-----------|---------------|
| SaaS Consumer generale | 30-40 | >50 |
| Fitness/Wellness | 40-55 | >65 |
| Finance | 20-35 | >45 |
| AI/Productivity | 35-50 | >60 |
| E-learning | 40-55 | >65 |

---

## B. SaaS B2B

### Metriche Revenue

| Metrica | Formula | Benchmark Tipico | Note |
|---------|---------|-----------------|------|
| **MRR** | Σ ricavi mensili ricorrenti | — (assoluto, cresce) | — |
| **ARR** | MRR × 12 | — | — |
| **CAC** | Spesa marketing+sales / nuovi clienti | $1k-$10k per SMB, $10k-$100k+ per enterprise | — |
| **LTV** | ARPU × Gross Margin % / Churn rate mensile | — | LTV/CAC > 3:1 per sostenibilità |
| **LTV/CAC ratio** | LTV / CAC | Minimo 3:1 | Obiettivo 5:1 |
| **Payback period** | CAC / (ARPU × Gross Margin) | <12 mesi SMB, <18 mesi enterprise | — |
| **Net Revenue Retention** | (MRR inizio + expansion - contraction - churn) / MRR inizio | >100% = crescita senza nuovi clienti | Best: Slack 143%, Snowflake 158% |
| **Gross Revenue Retention** | MRR senza espansione / MRR inizio | >85% buono, >90% eccellente | — |

### Time-to-Activation B2B

L'activation in B2B è il momento in cui il cliente ha completato il setup minimo per ottenere valore. Non il login.

| Tipo prodotto | Activation event | Target TTA |
|---------------|-----------------|-----------|
| Team collaboration (Slack-like) | Primo messaggio inviato in canale team | <1 giorno |
| CRM | Primo contatto importato + primo deal creato | <3 giorni |
| Analytics/BI | Prima dashboard configurata con dati reali | <1 settimana |
| Project management | Primo progetto con >1 membro + task assegnato | <2 giorni |
| QuickInvoice (freelance) | Primo preventivo inviato a cliente reale | <10 minuti |

### Feature Adoption Rate

La feature adoption misura quanti utenti attivi usano una specifica feature. Usata per identificare feature poco scoperte o feature non necessarie.

| Benchmark | Interpretazione |
|-----------|----------------|
| >50% utenti usa la feature | Feature core ben adottata |
| 20-50% | Feature utile per segmento specifico |
| 5-20% | Feature di nicchia o scopribilità bassa — investigare |
| <5% | Feature non necessaria o completamente nascosta |

**Tasso di adoption per tipo di feature:**
- Onboarding features: target >80% (tutti devono completarle)
- Core loop features: target >60%
- Power features: 20-40% accettabile
- Integrations: 10-30% normale

### Expansion Revenue

| Metrica | Benchmark buono | Eccellente |
|---------|----------------|-----------|
| **MRR da expansion** (upsell + cross-sell) | >15% del nuovo MRR | >30% |
| **Expansion MRR rate** | >2% del MRR esistente/mese | >5% |
| **Upsell conversion** (da piano base a pro) | 5-10%/anno | >15% |

---

## C. Marketplace

### Supply/Demand Metrics

| Metrica | Formula | Benchmark |
|---------|---------|-----------|
| **Supply/Demand ratio** | N seller attivi / N buyer attivi | 1:10 per marketplace sano |
| **Liquidity rate** | Listing che ricevono almeno 1 transazione/mese / totale listing | >20% buono, >40% eccellente |
| **Fill rate** (richieste soddisfatte) | Richieste con match / richieste totali | >60% target, >80% eccellente |
| **Time-to-match** | Tempo medio tra listing e prima transazione | Dipende da verticale (ore-giorni) |

### GMV e Take Rate

| Metrica | Formula | Benchmark verticale |
|---------|---------|-------------------|
| **GMV** | Σ valore transazioni (lordo) | — (cresce) |
| **Net Revenue** | GMV × Take rate | — |
| **Take rate** | Revenue / GMV | 10-30% marketplace servizi, 5-15% marketplace prodotti fisici, 15-30% digital |
| **Average Transaction Value (ATV)** | GMV / N transazioni | Specifico per verticale |

### Repeat Purchase Rate

| Tipo marketplace | Repeat rate buono | Note |
|-----------------|------------------|------|
| E-commerce generalista | >30% a 6 mesi | Amazon: >90% |
| Servizi professionali | >40% a 12 mesi | Relazione continuativa |
| Viaggi/Esperienze | >20% a 12 mesi | Stagionalità alta |
| Freelance/Services | >50% (cliente → stesso seller) | Network effects |

### Activation Rate per Lato

**Buyer activation:** primo acquisto completato
- Target: >30% dei buyer registrati completa il primo acquisto entro 7 giorni

**Seller activation:** primo listing pubblicato + prima transazione
- Target listing: >60% dei seller registrati pubblica almeno 1 listing entro 48h
- Target prima transazione: >30% dei seller ottiene prima vendita entro 30 giorni

---

## D. AI Tool

### Task Completion Rate

Il TCR misura quante sessioni AI portano a un output accettato dall'utente (non solo generato).

| Benchmark | Interpretazione |
|-----------|----------------|
| >70% | AI molto utile, output raramente rifiutato |
| 50-70% | Buono — utenti trovano valore nella maggioranza dei casi |
| 30-50% | AI utile ma richiede troppa iterazione |
| <30% | Problema critico — valore AI non chiaro o qualità bassa |

**Come misurare:** utente accetta/usa output vs. rigenera/abbandona

### AI Success Rate

La percentuale di richieste che ottengono una risposta AI (non fallback, non errore, non timeout).

| Soglia | Status |
|--------|--------|
| >99% | Eccellente |
| 97-99% | Buono |
| 95-97% | Accettabile — monitorare |
| <95% | Problematico — utenti incontrano fallback troppo frequentemente |

### Time-to-First-Value AI

| Tool | Definizione first value | Target TTV |
|------|------------------------|-----------|
| Generatore testi | Primo output generato accettato | <60 secondi |
| AI coding assistant | Prima suggestion accettata | <2 minuti |
| AI analytics | Prima insight generata da dati reali | <5 minuti |
| AI design tool | Primo design generato | <90 secondi |
| FocusBoard AI | Primo piano giornaliero generato + accettato | <3 minuti |

### Feedback Loop Quality

| Metrica | Formula | Target |
|---------|---------|--------|
| **Thumbs up rate** | Positivi / (positivi + negativi) | >75% |
| **Regeneration rate** | Regenerazioni / totale generazioni | <30% |
| **Edit rate** | Output editati prima dell'uso / output accettati | <40% (editing leggero ok, riscrittura totale no) |
| **Copy-paste rate** | Output usati direttamente / output accettati | >60% |

---

## E. E-commerce

### Funnel Conversion

| Stage | Benchmark settore | Note |
|-------|-----------------|------|
| **Visitor → Product page view** | 40-60% | Dipende da traffic quality |
| **Product view → Add to cart** | 8-15% | Ottimizzato da foto, prezzo, reviews |
| **Add to cart → Checkout** | 50-70% | Cart abandonment inizia qui |
| **Checkout start → Purchase** | 50-75% | Ottimizzato da checkout UX |
| **Overall conversion (visit → purchase)** | 1-4% | E-commerce tipico: 2-3% |

### Cart Abandonment

- **Benchmark globale:** 70-75% degli utenti abbandona il carrello
- **Cause principali (in ordine):**
  1. Shipping costs inaspettati (49%)
  2. Richiesto account obbligatorio (24%)
  3. Processo checkout troppo complesso (18%)
  4. Totale ordine non visibile fino al checkout (17%)
  5. Sito lento o problemi tecnici (13%)

**Recovery rate email:**
- Email 1 (entro 1h): 5-8% conversion
- Email 2 (24h): 3-5%
- Email 3 (72h con sconto): 3-6%
- Sequenza totale: 10-15% recovery

### Average Order Value (AOV)

| Tecnica | Impatto AOV tipico |
|---------|-----------------|
| Product recommendations ("Altri hanno comprato") | +10-15% |
| Bundle offers | +20-30% |
| Free shipping threshold (es. "gratis sopra €50") | +15-25% |
| Upsell al checkout | +5-12% |

### Return Rate

| Categoria prodotto | Return rate normale |
|-------------------|-------------------|
| Abbigliamento | 20-30% |
| Elettronica | 8-12% |
| Libri/Media | 2-5% |
| Home decor | 5-10% |
| Software/Digital | <5% (se no-refund policy) |

---

## Database Metriche — Tabella Completa

| # | Metrica | Categoria | Formula | Benchmark Settore | Tool Consigliato | Note |
|---|---------|-----------|---------|-------------------|-----------------|------|
| 1 | D1 Retention | Consumer SaaS | Utenti attivi giorno 1 / nuovi utenti | 40-60% buono | Mixpanel, Amplitude | |
| 2 | D7 Retention | Consumer SaaS | Utenti attivi giorno 7 / nuovi utenti | 20-30% buono | Mixpanel, Amplitude | |
| 3 | D30 Retention | Consumer SaaS | Utenti attivi giorno 30 / nuovi utenti | 8-15% buono | Mixpanel, Amplitude | |
| 4 | Freemium Conversion | Consumer SaaS | Utenti paganti / utenti free totali | 2-5% | Stripe, ChartMogul | |
| 5 | Trial Conversion | Consumer SaaS | Paganti post-trial / trial avviati | 8-15% | Stripe | |
| 6 | Time-to-Value | Consumer SaaS | Mediana minuti da signup a first value | <10 min | Mixpanel, custom | |
| 7 | NPS | Tutti | (% Promoters - % Detractors) × 100 | >30 SaaS | Typeform, Delighted | Survey trimestrale |
| 8 | MRR | B2B SaaS | Σ ricavi mensili ricorrenti | — cresce | ChartMogul, Baremetrics | |
| 9 | ARR | B2B SaaS | MRR × 12 | — | ChartMogul | |
| 10 | CAC | B2B SaaS | Spesa totale / nuovi clienti | <1/3 LTV | Custom | |
| 11 | LTV | B2B SaaS | ARPU × Gross Margin / Churn mensile | 3-5x CAC | Custom | |
| 12 | LTV/CAC | B2B SaaS | LTV / CAC | >3:1 | Custom | Sotto 3:1 = non sostenibile |
| 13 | Payback Period | B2B SaaS | CAC / MRR netto per cliente | <12 mesi | Custom | |
| 14 | Net Revenue Retention | B2B SaaS | (MRR start + expansion - contraction - churn) / MRR start | >100% | ChartMogul | >100% = crescita senza nuovi clienti |
| 15 | Gross Revenue Retention | B2B SaaS | MRR senza espansione / MRR precedente | >85% | ChartMogul | |
| 16 | Monthly Churn Rate | B2B SaaS | Clienti persi / clienti inizio mese | <2% mensile | ChartMogul | <0.5% = eccellente |
| 17 | Feature Adoption Rate | B2B SaaS | Utenti che usano feature / utenti attivi | >20% per features core | Amplitude, Pendo | |
| 18 | Time-to-Activation | B2B SaaS | Mediana ore da signup a activation event | <72h | Mixpanel | |
| 19 | Expansion MRR Rate | B2B SaaS | Expansion MRR / MRR totale precedente | >2%/mese | ChartMogul | |
| 20 | GMV | Marketplace | Σ valore transazioni lordo | — cresce | Custom | |
| 21 | Take Rate | Marketplace | Revenue / GMV | 10-30% servizi | Custom | |
| 22 | Liquidity Rate | Marketplace | Listing con transazione / listing totali | >20% | Custom | |
| 23 | Supply/Demand Ratio | Marketplace | Seller attivi / buyer attivi | 1:10 | Custom | |
| 24 | Repeat Purchase Rate | Marketplace | Clienti con >1 acquisto / clienti totali | >30% a 6 mesi | Custom | |
| 25 | Buyer Activation Rate | Marketplace | Buyer con primo acquisto / registrati | >30% a 7 gg | Mixpanel | |
| 26 | Seller Activation Rate | Marketplace | Seller con primo listing / registrati | >60% a 48h | Mixpanel | |
| 27 | AI Task Completion Rate | AI Tool | Output accettati / output generati | >60% | Custom | |
| 28 | AI Success Rate | AI Tool | Richieste con risposta AI / totale | >97% | Datadog, custom | |
| 29 | AI Regeneration Rate | AI Tool | Rigenerazioni / totale generazioni | <30% | Amplitude | |
| 30 | AI Thumbs Up Rate | AI Tool | Feedback positivi / feedback totali | >70% | Custom | |
| 31 | Time-to-First-Value AI | AI Tool | Mediana secondi da primo prompt a output accettato | <60s | Mixpanel | |
| 32 | Overall E-com Conversion | E-commerce | Ordini / visitatori unici | 1-4% | GA4, Hotjar | |
| 33 | Cart Abandonment Rate | E-commerce | Cart abbandonati / cart creati | <70% target | GA4 | |
| 34 | Average Order Value | E-commerce | GMV / numero ordini | Specifico verticale | GA4, Shopify | |
| 35 | Return Rate | E-commerce | Resi / ordini spediti | <10% non-abbigliamento | Shopify | |
| 36 | Email Open Rate | Tutti | Aperture / email consegnate | >20% | Mailchimp, Klaviyo | |
| 37 | Email Click Rate | Tutti | Click / email consegnate | >2% | Klaviyo | |
| 38 | Unsubscribe Rate | Tutti | Disiscritti / email inviate | <0.5% | Klaviyo | Guardrail critico |
| 39 | App Store Rating | Mobile | Media stelle | >4.2 | App Store Connect | |
| 40 | Crash Rate | Mobile | Sessioni con crash / sessioni totali | <0.1% | Firebase Crashlytics | |
| 41 | Session Length | Tutti | Durata media sessione | Specifico per prodotto | GA4, Mixpanel | |
| 42 | DAU/MAU Ratio | Consumer | DAU / MAU | >20% buono, >50% eccellente | Amplitude | |
| 43 | Virality / K-factor | Consumer | (Inviti inviati × conversion rate inviti) | >1 = crescita virale | Custom | |
| 44 | Support Ticket Rate | Tutti | Ticket / utenti attivi | <5% mensile | Intercom, Zendesk | |

---

## Metriche Tecniche (Non-Funzionali)

### Core Web Vitals (Google)

| Metrica | Buono | Da migliorare | Scarso | Impatto |
|---------|-------|--------------|--------|---------|
| **LCP** (Largest Contentful Paint) | <2.5s | 2.5-4s | >4s | SEO + UX |
| **FID** (First Input Delay) | <100ms | 100-300ms | >300ms | Interattività |
| **CLS** (Cumulative Layout Shift) | <0.1 | 0.1-0.25 | >0.25 | Stabilità visiva |
| **FCP** (First Contentful Paint) | <1.8s | 1.8-3s | >3s | Perceived load |
| **TTFB** (Time to First Byte) | <800ms | 800ms-1.8s | >1.8s | Server performance |
| **INP** (Interaction to Next Paint) | <200ms | 200-500ms | >500ms | Responsività |

### Uptime SLA Standard

| Tier | Uptime | Downtime massimo/anno | Adatto per |
|------|--------|----------------------|-----------|
| **99%** | 99% | ~87 ore | Tool interni, beta |
| **99.9%** | "tre nove" | ~8.7 ore | SaaS consumer standard |
| **99.95%** | — | ~4.4 ore | SaaS B2B con contratti |
| **99.99%** | "quattro nove" | ~52 minuti | Enterprise, fintech, health |
| **99.999%** | "cinque nove" | ~5 minuti | Infrastruttura critica |

Nota: "99.9% SLA" è lo standard minimo dichiarabile per qualsiasi SaaS con clienti paganti. Sotto questo livello, i contratti enterprise non vengono firmati.

### API Latency Benchmarks

| Percentile | Soglia accettabile | Soglia critica | Note |
|------------|------------------|---------------|------|
| **P50** (mediana) | <200ms | >500ms | 50% delle request |
| **P95** | <500ms | >1s | 95% delle request |
| **P99** | <1s | >2s | 1% delle request più lente |
| **P99.9** | <2s | >5s | Casi estremi |

**Per endpoint specifici:**

| Tipo endpoint | P95 target |
|---------------|-----------|
| Auth (login, token refresh) | <300ms |
| Lettura dati (GET) | <200ms |
| Scrittura dati (POST/PUT) | <400ms |
| Query aggregate/report | <1s |
| AI generation | <5s (con streaming se >2s) |
| File upload | <2s per MB (progress bar obbligatoria) |

### Error Rate Acceptable Range

| Tipo | Soglia accettabile | Alert critico |
|------|--------------------|---------------|
| **4xx errors** (client errors) | <5% delle request | >10% |
| **5xx errors** (server errors) | <0.1% delle request | >1% |
| **Timeout rate** | <0.5% | >2% |
| **Failed payments** | <1% (esclude card declined) | >3% |

---

## North Star per Tipo di Prodotto — Esempi

### Prodotti di riferimento noti

| Prodotto | North Star Metric | Perché |
|---------|-----------------|--------|
| **Notion** | Spazi attivi creati per settimana | Misura se gli utenti usano realmente Notion come sistema di lavoro |
| **Airbnb** | Notti prenotate per settimana | Misura il valore creato per entrambi i lati del marketplace |
| **Slack** | Messaggi inviati per utente per giorno | Misura l'engagement e il valore di comunicazione real-time |
| **Spotify** | Minuti di ascolto per utente per giorno | Misura l'abitudine di ascolto, predice retention |
| **Duolingo** | Utenti che completano streak >7 giorni | Misura l'habit formation, predice LTV |
| **Figma** | File condivisi e commentati per settimana | Misura la collaborazione, non solo la creazione individuale |
| **HubSpot** | Deal attivi nel CRM per account | Misura se il tool è nel flusso di vendita reale |
| **GitHub** | Commit per developer per settimana | Misura l'integrazione nel workflow di sviluppo |
| **Dropbox** | File salvati e acceduti per utente | Misura l'uso come storage primario, non secondario |
| **LinkedIn** | Connessioni di qualità stabilite per settimana | Misura il valore di networking, non i meri login |

### Prodotti di riferimento PRD Architect OS

| Prodotto | North Star Metric | Rationale |
|---------|-----------------|----------|
| **QuickInvoice** | Preventivi inviati entro 10 minuti dal signup | Se l'utente invia il primo preventivo rapidamente, c'è retention. TTV misura l'efficacia dell'onboarding |
| **FocusBoard** | Sessioni mattutine attivate per settimana per utente | L'app vale solo se diventa una routine mattutina, non un tool usato sporadicamente |

### Template North Star per categoria

| Categoria | Formula North Star consigliata | Variante |
|-----------|-------------------------------|---------|
| **Task/Project manager** | Task completati per utente per settimana | Progetti attivi per account |
| **CRM/Sales** | Deal aggiornati nel CRM per settimana | Pipeline revenue gestita per account |
| **AI writing tool** | Documenti pubblicati con AI assist / settimana | Parole generate accettate senza edit |
| **Analytics/BI** | Dashboard consultate per utente per settimana | Insight condivise con team |
| **E-learning** | Lezioni completate per utente per settimana | Corsi portati al 100% |
| **Marketplace servizi** | Transazioni completate per settimana | GMV per seller attivo |
| **Community/Forum** | Post con almeno 1 risposta per settimana | Utenti con >3 interazioni/settimana |
| **Health/Fitness** | Sessioni allenamento loggate per settimana | Streak giorni consecutivi |
| **Finance/Budget** | Transazioni categorizzate per mese | Budget rispettati per categoria |
| **Email/Outreach** | Email inviate con tasso di risposta >10% | Sequenze completate |

---

## Guardrail Metrics — Soglie Critiche

### Crash Rate

| Piattaforma | Soglia massima accettabile | Alert immediato |
|-------------|--------------------------|----------------|
| Web app | <0.5% sessioni con errore JS critico | >2% |
| iOS app | <0.1% crash-free sessions invertito | <99.5% crash-free sessions |
| Android app | <0.3% crash rate | <99% crash-free sessions |
| PWA | <0.2% fatal errors | >1% |

### Email Delivery Rate

| Metrica | Soglia minima | Note |
|---------|--------------|------|
| **Delivery rate** | >98% | Sotto questo: reputation issue |
| **Spam rate** (Google Postmaster) | <0.1% | Sopra: rischio blocco Gmail |
| **Bounce rate (hard)** | <2% | Pulire liste regolarmente |
| **Unsubscribe rate** | <0.5% per invio | Sopra: contenuto irrilevante |

### Latency Guardrail

| Scenario | Soglia critica — non superare mai |
|---------|----------------------------------|
| Homepage load (LCP) | >4 secondi |
| API P99 latency | >3 secondi |
| Checkout completion | >2 secondi dall'ultimo click |
| Auth token validation | >500ms |
| AI generation start (first token) | >3 secondi (streaming) |

### Churn Rate Guardrail

| Tipo SaaS | Churn mensile massimo accettabile |
|-----------|----------------------------------|
| Consumer SaaS | <8% mensile (>100% annuo = insostenibile) |
| SMB SaaS | <3% mensile |
| Mid-market SaaS | <1.5% mensile |
| Enterprise SaaS | <0.5% mensile (>5% annuo = problema) |

---

## Come Costruire il Measurement Plan

### Template Analytics Events

Ogni PRD deve includere questa sezione prima della consegna. Documenta gli eventi analytics necessari per misurare le metriche definite.

```javascript
// MEASUREMENT PLAN — [Nome Prodotto]
// Versione: 1.0
// Tool: [Mixpanel / Amplitude / PostHog / GA4]

// ─────────────────────────────────────────
// EVENTO 1: SIGNUP
// ─────────────────────────────────────────
track("user_signed_up", {
  method: "email" | "google" | "github",  // come si è registrato
  source: "organic" | "paid" | "referral" | "direct",  // da dove viene
  plan: "free" | "trial" | "pro",  // piano iniziale
  referrer_id: string | null,  // se venuto da referral link
  timestamp: ISO8601
})

// ─────────────────────────────────────────
// EVENTO 2: FIRST VALUE (North Star trigger)
// ─────────────────────────────────────────
// Definire in base al prodotto:

// QuickInvoice:
track("invoice_sent_first_time", {
  minutes_since_signup: number,  // TTV misura
  invoice_value: number,
  client_type: "new" | "existing",
  used_template: boolean,
  used_ai_draft: boolean
})

// FocusBoard:
track("morning_session_completed", {
  tasks_planned: number,
  ai_assist_used: boolean,
  session_start_time: "HH:mm",  // per analisi orario ottimale
  tasks_from_yesterday_reviewed: boolean
})

// ─────────────────────────────────────────
// EVENTO 3: CONVERSION (free → paid)
// ─────────────────────────────────────────
track("plan_upgraded", {
  from_plan: "free" | "trial",
  to_plan: "pro" | "business" | "enterprise",
  trigger: "organic" | "paywall_hit" | "email_campaign" | "in_app_prompt",
  paywall_feature: string | null,  // quale feature ha scatenato l'upgrade
  days_since_signup: number,
  mrr_delta: number
})

// ─────────────────────────────────────────
// EVENTO 4: RETENTION SIGNAL (ripetizione comportamento core)
// ─────────────────────────────────────────
// Segnale settimanale che indica utente "retained":

// QuickInvoice:
track("invoice_sent", {
  is_repeat_user: boolean,  // ha già inviato almeno 1 preventivo
  week_number_since_signup: number,
  total_invoices_sent: number,
  value: number
})

// ─────────────────────────────────────────
// EVENTO 5: CHURN SIGNAL (comportamento pre-abbandono)
// ─────────────────────────────────────────
track("subscription_cancelled", {
  reason: "too_expensive" | "not_using" | "missing_feature" | "found_alternative" | "other",
  days_as_customer: number,
  last_active_days_ago: number,
  total_revenue: number,
  exit_survey_completed: boolean
})

// ─────────────────────────────────────────
// EVENTO 6: FEATURE ADOPTION
// ─────────────────────────────────────────
track("feature_used", {
  feature_name: string,  // nome consistente e snake_case
  is_first_time: boolean,
  user_plan: string,
  context: string  // da dove è stata accessata
})

// ─────────────────────────────────────────
// EVENTO 7: ERRORI (per guardrail metrics)
// ─────────────────────────────────────────
track("error_encountered", {
  error_type: "network" | "server" | "validation" | "auth" | "ai_failure",
  error_code: string,
  feature_context: string,  // in quale feature è avvenuto
  was_retry_successful: boolean | null,
  user_plan: string
})
```

### Funnel Analysis Setup

Per misurare la North Star e le Primary Metrics, definire i funnel nel tool analytics:

```
FUNNEL — Activation (QuickInvoice)
Step 1: user_signed_up
Step 2: client_added (primo cliente inserito)
Step 3: invoice_draft_created (prima bozza preventivo)
Step 4: invoice_sent_first_time (ACTIVATION EVENT)

Finestra: 7 giorni
Breakdowns: method, source, plan
Target: >50% utenti completa il funnel in 7 giorni

---

FUNNEL — Conversion to Paid
Step 1: user_signed_up (piano free/trial)
Step 2: paywall_encountered (opzionale — se tracciato)
Step 3: plan_upgrade_started
Step 4: plan_upgraded

Finestra: 30 giorni
Target freemium: >3%, trial: >10%
```

### Dashboard Metriche — Struttura Consigliata

```
DASHBOARD NORTH STAR (aggiornamento: settimanale)
- North Star metric — valore corrente vs. settimana precedente
- North Star trend — grafico 90 giorni
- Cohort analysis — NSM per cohort di signup

DASHBOARD PRODUCT HEALTH (aggiornamento: giornaliero)
- DAU / WAU / MAU e ratio
- D1/D7/D30 retention — cohort più recente
- Error rate — ultime 24h
- API P95 latency — ultime 24h

DASHBOARD REVENUE (aggiornamento: giornaliero)
- MRR corrente e trend
- Nuovi MRR vs. Expansion MRR vs. Churned MRR
- Trial conversions ultime 30 giorni
- Churn rate mensile — trend

DASHBOARD ACQUISITION (aggiornamento: giornaliero)
- Nuovi signup per source
- CAC per canale
- Activation rate per cohort
- Time-to-value mediana
```

---

*Fine REF_05 — Success Metrics Library*  
*Versione 1.0 — PRD Architect OS Knowledge Base*
