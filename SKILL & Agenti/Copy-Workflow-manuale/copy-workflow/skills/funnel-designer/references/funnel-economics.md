# Funnel Economics — Matematica del Funnel e KPI Operativi

> La differenza tra un funnel "teorico" e uno che genera revenue sta nella matematica. Questo file contiene le conversion rate benchmark, il calcolo del CAC/LTV, e i KPI da monitorare per ogni tipo di funnel.

---

## Perché la Matematica Prima della Strategia

Un funnel senza numeri è una mappa senza scala. Prima di costruire il funnel, devi sapere:
- Quante persone devono entrare per ottenere X vendite?
- Dove il funnel "perde" di più e quanto è tollerabile?
- Il funnel è profittevole con i margini del prodotto?

Risposta a queste domande → strategia del funnel. Non il contrario.

---

## Benchmark Conversion Rate per Step

Questi sono benchmark realistici per il mercato italiano. I valori variano per settore e qualità del traffico.

### Cold Traffic (traffico freddo — ads a persone che non ti conoscono)

| Step | Metrica | Benchmark Basso | Benchmark Alto |
|---|---|---|---|
| Ad → Click | CTR | 0.5% | 3% |
| Click → Lead (opt-in) | Opt-in rate | 15% | 40% |
| Lead → Apertura email #1 | Open rate | 20% | 50% |
| Email → Click link | CTR email | 3% | 15% |
| Landing page → Acquisto | CR sales page | 1% | 5% |
| Checkout → Completato | Checkout completion | 50% | 80% |

### Warm Traffic (lista email, community, retargeting)

| Step | Metrica | Benchmark Basso | Benchmark Alto |
|---|---|---|---|
| Email → Apertura | Open rate | 25% | 60% |
| Email → Click | CTR email | 5% | 25% |
| Landing page → Acquisto | CR sales page | 2% | 10% |

### Social Organico

| Step | Metrica | Benchmark |
|---|---|---|
| Post → Click link in bio | 0.5% - 3% dei follower |
| DM → Risposta | 20% - 60% (dipende dalla relazione) |
| Link in bio → Acquisto | 1% - 5% |

---

## Calcolo del Funnel — Modello Operativo

**Esempio: Corso online €297, goal: 50 vendite/mese**

```
Step 1: Vendite necessarie = 50
Step 2: CR sales page = 2% → Lead necessari = 50 / 0.02 = 2.500 lead/mese
Step 3: Opt-in rate = 25% → Click necessari = 2.500 / 0.25 = 10.000 click/mese
Step 4: CTR ads = 1.5% → Impression necessarie = 10.000 / 0.015 = 667.000/mese
Step 5: CPC medio = €0.50 → Budget ads = 10.000 × €0.50 = €5.000/mese
Step 6: Revenue = 50 × €297 = €14.850
Step 7: ROAS = €14.850 / €5.000 = 2.97 (profittevole se margine > 33%)
```

**Come usare questo modello:**
1. Parti dalla vendita target (step 1)
2. Risali il funnel con le conversion rate stimate
3. Calcola il budget necessario
4. Valuta la profittabilità prima di costruire il funnel

---

## CAC — Customer Acquisition Cost

```
CAC = Spesa totale acquisizione / Numero clienti acquisiti

Esempio:
Budget ads: €5.000
Gestione agenzia: €1.000
Tool (landing, email): €200
Totale: €6.200

Clienti acquisiti: 50
CAC = €6.200 / 50 = €124 per cliente

Margine prodotto: €297 × 70% = €208
Net per cliente: €208 - €124 = €84 (profittevole)
```

**Regola**: il CAC non deve mai superare il 40-50% del valore del prodotto per un business sano. Per prodotti con high LTV (upsell, rinnovi, continuative), il CAC può essere più alto.

---

## LTV — Lifetime Value

Il LTV è il valore totale che un cliente porta nel tempo — non solo il primo acquisto.

```
LTV semplice = Valore medio acquisto × Numero acquisti medi nel tempo

Esempio (info-product con upsell):
Acquisto 1: Corso base €297
Acquisto 2 (upsell): Workshop avanzato €497 (30% la acquistano)
Acquisto 3 (membership): €47/mese × 6 mesi media (20% la acquistano)

LTV = €297 + (€497 × 0.30) + (€47 × 6 × 0.20)
LTV = €297 + €149 + €56.4 = €502.4
```

**Implicazione strategica**: con LTV = €502, puoi permetterti un CAC fino a €200 (40%) rimanendo profittevole. Questo cambia radicalmente il budget ads sostenibile.

---

## KPI per Fase del Funnel

### KPI Fase Awareness (Top of Funnel)

| KPI | Descrizione | Come monitorarlo |
|---|---|---|
| CPM | Costo per 1.000 impression | Business Manager Facebook/Google |
| Reach | Persone raggiunte unico | Business Manager |
| Frequency | Media impression per persona | Business Manager (>3 = saturazione) |
| CTR | Click / Impression | Business Manager |

### KPI Fase Considerazione (Middle of Funnel)

| KPI | Descrizione | Come monitorarlo |
|---|---|---|
| CPC | Costo per click | Business Manager |
| Opt-in rate | Lead / Visitatori landing | Analytics + CRM |
| CPL | Costo per lead | Budget / Lead totali |
| Open rate email | % aperture sulla lista | ESP (Mailchimp, ActiveCampaign...) |
| CTR email | Click / Email aperte | ESP |

### KPI Fase Conversione (Bottom of Funnel)

| KPI | Descrizione | Come monitorarlo |
|---|---|---|
| CR sales page | Acquisti / Visitatori | Analytics |
| CPA | Costo per acquisizione | Budget / Acquisti |
| ROAS | Revenue / Spesa ads | Business Manager |
| Cart abandonment | % abbandoni checkout | Analytics / Funnel tool |
| Checkout completion | % acquisti completati | Payment processor |

---

## Segnali di Funnel Rotto

### CR sales page < 0.5%
**Problema probabile**: sezione P debole (dolore non amplificato), USP non differenziante, obiezioni principali non gestite.
**Azione**: rivedi la sezione P con show don't tell, aggiungi CPB per la top-2 obiezione.

### Opt-in rate < 10%
**Problema probabile**: lead magnet non abbastanza allettante, mismatch tra promessa ad e promessa landing.
**Azione**: allinea il messaggio dell'ad con quello della landing (message match).

### Open rate email < 20%
**Problema probabile**: oggetto non abbastanza curioso/urgente, lista non segmentata, orario di invio.
**Azione**: A/B test 2-3 oggetti con strategie diverse.

### CTR email < 3%
**Problema probabile**: CTA non abbastanza chiaro, valore dell'email non sufficiente a motivare il click.
**Azione**: un solo CTA per email, link testuale oltre al pulsante.

### ROAS < 1.5 su traffico freddo
**Problema probabile**: traffico non qualificato (targeting largo), landing page con CR bassa, prezzo del prodotto troppo basso per sostenere il costo del traffico.
**Azione**: ristrigi il targeting, ottimizza la landing, valuta il funnel con lead magnet intermedio.

---

## Regola del Funnel Profittevole

```
(LTV × CR) > CAC

dove:
LTV = lifetime value del cliente
CR = conversion rate media funnel
CAC = customer acquisition cost

Se questa equazione è vera, il funnel scala.
Se è falsa, qualsiasi volume di traffico brucia denaro.
```

Controlla questa equazione prima di scalare il budget ads.
