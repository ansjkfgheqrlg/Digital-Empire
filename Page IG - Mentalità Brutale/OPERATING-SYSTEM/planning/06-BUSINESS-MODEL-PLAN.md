# 06 — Business Model Plan: Mentalità Brutale

## 1. Tesi economica

Mentalità Brutale deve diventare un **asset media proprietario**, non una pagina dipendente da reach casuale. Instagram acquisisce attenzione; il business nasce quando quell'attenzione passa a un asset posseduto, un'offerta coerente e un ledger di attribuzione.

```text
CONTENT IP → ATTENTION → TRUST SIGNAL → OWNED AUDIENCE → OFFER → REVENUE
     ↑                                                       ↓
     └──────────── DATA / MEMORY / REINVESTMENT ─────────────┘
```

## 2. Quattro asset prodotti

1. **Audience asset** — follower e soprattutto email/contatti con consenso.
2. **Content IP** — hook, framework, storie, visual grammar e pattern validati.
3. **Operating asset** — MB-OS, processi, skill e dati riusabili.
4. **Commercial asset** — lead magnet, offerte, affiliate/sponsor fit e P&L.

Il valore non è solo il profilo. È il sistema che produce e misura questi quattro asset.

## 3. Revenue ladder

### L0 — Attention / nessuna monetizzazione aggressiva

Obiettivo: baseline, fiducia e qualità. CTA: salva/condividi/segui. Nessuna sponsorizzazione casuale.

**Gate uscita:** 28 post + 56 snapshot o gap dichiarati; profilo coerente; incidenti severity alta = 0.

### L1 — Owned audience

Asset:

- lead magnet operativo;
- landing;
- email delivery/welcome;
- UTM e privacy/consenso;
- una promessa coerente col brand.

**Gate uscita:** percorso bio→landing→lead testato end-to-end; tassi misurabili, anche se bassi.

### L2 — Entry offer

Candidati da validare, non decisioni:

- workbook/sistema disciplina;
- mini-corso operativo;
- challenge guidata;
- bundle libro + worksheet;
- community/evento tematico.

Prezzo deciso dal team-pricing dopo intent signal, costo delivery, benchmark e posizionamento. Nessun prezzo viene scritto nel piano senza quel gate.

### L3 — Core/continuity

Solo se L2 dimostra domanda e supportabilità:

- percorso più profondo;
- community con rituali/standard;
- libreria o membership;
- prodotti editoriali/KDP collegati.

### L4 — Affiliate e sponsorship

Non è il core iniziale. Accettare solo:

- fit con audience;
- prodotto provato/valutato;
- disclosure chiara;
- rights e durata usage definiti;
- prezzo basato su dati, non follower vanity;
- nessuna erosione della fiducia.

### L5 — B2B / MB-OS productization

- setup di pagine first-party;
- managed content operations;
- licenza/implementazione MB-OS;
- audit e certificazione social automation.

Parte solo dopo due cicli interni e onboarding tenant senza fork.

## 4. Tre modelli candidati

| Modello | Time-to-value | Margine potenziale | Complessità | Fit iniziale | Verdict |
|---|---|---|---|---|---|
| Lead-gen verso prodotto proprio | medio | alto | media | alto | PRIMARY |
| Affiliate/sponsor | medio | medio | bassa/media | medio | SECONDARY |
| MB-OS B2B | lungo | alto | alta | alto dopo prova | STRATEGIC LATER |

## 5. Funnel minimo

```text
Post/Reel
  → visita profilo
  → bio/pinned post
  → landing singola
  → lead magnet
  → welcome email
  → segmentazione intent
  → offerta quando appropriata
```

Niente link multipli senza gerarchia nel primo test. Una destinazione, una promessa, una metrica.

## 6. Attribution contract

Ogni link usa:

```text
utm_source=instagram
utm_medium=organic
utm_campaign=mb_<cycle_id>
utm_content=<content_id>
```

Eventi minimi:

1. `profile_visit` dove disponibile;
2. `bio_link_click` dove disponibile;
3. `landing_view`;
4. `lead_submit`;
5. `email_confirmed` se double opt-in;
6. `offer_view`;
7. `purchase`;
8. `refund`.

Revenue non viene attribuita a Instagram senza campaign/content id o regola di attribution dichiarata.

## 7. Formule di gestione

```text
profile_visit_rate = profile_visits / reach
bio_ctr = bio_link_clicks / profile_visits
lead_cr = leads / landing_views
sale_cr = purchases / qualified_leads
revenue_per_1k_reached = revenue_attributed / reach * 1000
content_cost = human_time_cost + tools + hosting + API
contribution_margin = revenue_attributed - variable_costs - refunds
```

I denominatori zero producono `null`, non zero o infinito.

## 8. Ledger P&L minimo

Per mese/ciclo:

| Voce | Fonte |
|---|---|
| hosting/media | invoice provider |
| tool/AI/render | invoice/usage |
| ore umane | time ledger |
| produzione asset | run cost |
| lead | CRM |
| vendite/refund | checkout |
| affiliate/sponsor | payout/invoice |
| revenue attribuita | UTM/CRM rule |
| contribution margin | formula |

CFO vede numeri reali; ogni valore non disponibile resta `[DM]`.

## 9. Content-to-offer mapping

| Pilastro | Intent | Asset posseduto candidato | Offerta futura candidata |
|---|---|---|---|
| P1 Disciplina | implementare routine | worksheet/sistema | workbook/challenge |
| P2 Identità | definire standard | manifesto/esercizi | percorso identità/standard |
| P3 Ambizione/lavoro | produrre output | scorecard | mini-corso sistemi lavoro |
| P4 Confini | chiarire relazioni | checklist | contenuto educativo, no terapia |
| P5 Storia/potere | apprendere principi | reading list | libro/KDP/affiliate libri |

P4 non diventa consulenza psicologica. P5 non usa storia inventata.

## 10. Gate di monetizzazione

| Gate | Condizione |
|---|---|
| BM-G1 | baseline editoriale completa |
| BM-G2 | destination e attribution testate |
| BM-G3 | intent signal osservato (click, reply, lead) |
| BM-G4 | offerta e prezzo approvati da team-pricing |
| BM-G5 | delivery/support pronti |
| BM-G6 | refund/privacy/terms definiti |
| BM-G7 | P&L e kill criteria attivi |

Nessuna vendita prima di BM-G2; nessuna scala paid prima di BM-G7.

## 11. Review cadence

### Ogni settimana

- contenuti pubblicati e incidenti;
- buffer giorni;
- quality actions;
- domande audience;
- click/lead se funnel attivo;
- una sola decisione editoriale primaria.

### Ogni 28 giorni

- pattern validati/respinti;
- P&L ciclo;
- offerta/funnel;
- costo per contenuto;
- manual minutes/content;
- decisione KEEP/ITERATE/KILL.

### Ogni 90 giorni

Board decide:

- investire;
- mantenere organico;
- monetizzare;
- replicare tenant;
- fermare/riposizionare.

## 12. Kill criteria

- trust/safety incident ripetuto;
- rights violations;
- costo operativo cresce senza learning/revenue;
- page drift verso contenuto generico;
- funnel non misurabile;
- offerta non coerente con audience;
- productizzazione richiede fork e lavoro manuale per tenant;
- sponsor/affiliate erode il posizionamento.

## 13. Decisione business raccomandata

1. costruire audience e baseline;
2. attivare owned audience con un lead magnet operativo;
3. testare una entry offer tramite team-pricing;
4. aggiungere affiliate solo se coerenti;
5. trasformare MB-OS in capability B2B dopo prova interna.

Il modello non dipende da una singola fonte di ricavo: usa la pagina per creare IP, audience, dati e tecnologia riutilizzabile.
