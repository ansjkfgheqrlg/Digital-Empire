---
Type: CONCEPT
Status: Active
Tags: #architettura #vendite #funnel #evergreen #info-business #IB-L2-VEND
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — IB-L2-VEND Vendite & Funnel

> Cartella-workflow CF-grade. Standard: Content Factory Exponium = 1 workflow (corpus Maximilian).
> Dossier sorgente: `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-VEND.
> Base wrappata: `IB-R3-VENDITE-FUNNEL.md` + agente `IB-SALES-funnel` (ADR-003).

---

## Topologia del team

```
                   ┌──────────────────────────────────┐
                   │   IB-COORD-VENDITE (Sonnet)        │
                   │  capo area, orchestra i 3 WF       │
                   └──────────────┬───────────────────-┘
                                  │
     ┌──────────────┬─────────────┼─────────────┬──────────────┐
     │              │             │             │              │
┌────▼─────┐  ┌─────▼──────┐ ┌────▼──────┐ ┌────▼─────┐  ┌─────▼──────┐
│IB-VEND-  │  │IB-VEND-    │ │IB-VEND-   │ │IB-VEND-  │  │IB-VEND-    │
│LEAD      │  │OFFER       │ │SALESPAGE  │ │CHECKOUT  │  │CRO         │
│(Sonnet)  │  │(Sonnet)    │ │(Sonnet)   │ │(Haiku)   │  │(Sonnet)    │
│opt-in +  │  │offer stack │ │copy APSOC │ │pagamento │  │test A/B    │
│lead mag. │  │(← B-003)   │ │+ build    │ │+ carrelli│  │1 alla volta│
└────┬─────┘  └─────┬──────┘ └────┬──────┘ └────┬─────┘  └─────┬──────┘
     │              │             │             │              │
     └──────────────┴─────────────┼─────────────┴──────────────┘
                                  │  (tracking trasversale: IB-VEND-TRACK
                                  │   misura ogni step di ogni WF)
                   ┌──────────────▼───────────────┐
                   │   IB-VEND-QA (Sonnet)          │
                   │  gate APSOC ≥80 + gate brand   │
                   │  "prove non promesse" (G-VEND) │
                   │  indipendente — bloccante      │
                   └──────────────────────────────-┘
```

**Topologia:** star da `IB-COORD-VENDITE` → specialisti in parallelo. `IB-VEND-TRACK` opera
trasversalmente (misura ogni step di ogni WF). `IB-VEND-QA` è il gate indipendente in uscita
(G-VEND, bloccante) su ogni elemento di copy/funnel. Sequenza tipica WF-SALESPAGE:
OFFER → SALESPAGE → QA (gate) → handoff PLATFORM → TRACK (verifica eventi).

---

## Livelli gerarchici interni

| Livello | Agente(i) | Tier | Funzione |
|---|---|---|---|
| L0 — Coordinator | `IB-COORD-VENDITE` | Sonnet | Orchestra i 3 WF, coordina cross-reparto, escalation a ib-director |
| L1 — Architect | `IB-VEND-OFFER` · `IB-VEND-SALESPAGE` · `IB-VEND-LEAD` | Sonnet | Progettazione offerta, copy/build sales page, opt-in + lead magnet |
| L2 — Analyst | `IB-VEND-CRO` | Sonnet | Disegno ed esecuzione test A/B sul funnel (1 alla volta) |
| L3 — Technician | `IB-VEND-CHECKOUT` · `IB-VEND-TRACK` | Haiku | Build checkout/recupero carrelli; tracking eventi/UTM/attribution |
| L4 — Verifier | `IB-VEND-QA` | Sonnet | Gate G-VEND su ogni output in uscita dal reparto (bloccante) |

---

## Flussi principali

### WF-SALESPAGE (sales page canonica per prodotto)
```
Trigger: brief prodotto validato (gate prodotto IB-L2-PROD) + richiesta sales page
  → IB-VEND-OFFER: offer stack (value stack + bonus + garanzia + order bump + upsell)
     GATE: prezzi da catalogo approvato B-003 — nessun numero placeholder in produzione
  → IB-VEND-SALESPAGE: copy APSOC (problema → agitazione → soluzione → proof → offerta → CTA)
  → IB-VEND-QA: gate APSOC ≥80/100 + "prove non promesse" — nessun claim senza documentazione
  → Handoff HC-PL-IB-01 → 06-PLATFORM: build empire-premium-style + deploy
     GATE: pagina ≤5s, mobile responsive, link funzionanti, checkout collegato
  → IB-VEND-TRACK: eventi pixel (view, add-to-cart, purchase) + UTM per fonte; test debug verde
Output: sales page live + tracking attivo → ready per WF-LANCIO (T-14)
Gate di uscita: IB-VEND-QA PASS + tracking debug verde + checkout testato
```

### WF-FUNNEL-EVERGREEN (vendita continua 365 giorni)
```
Trigger: offerta validata da un lancio (o decisione ib-director di aprire l'evergreen)
  → IB-VEND-LEAD: lead magnet → opt-in page (APSOC + brand voice) → utente in lista email
  → IB-VEND-SALESPAGE: sequenza nurture (frame Founder Authority Stack — intelligence Beggiato)
     valore → autorità → offerta (5-7 email; max 1 CTA per email)
  → IB-VEND-SALESPAGE: sales page evergreen (variante lancio, senza deadline finte — Art.2)
  → IB-VEND-CHECKOUT: checkout + order bump + upsell (prezzi da B-003)
  → Acquirente → handoff IB-L2-COMM (WF-ONBOARDING-STUDENTE) → community → cross-sell scout
  → Loop: IB-VEND-TRACK misura ogni step → IB-VEND-CRO 1 test A/B alla volta → ≥14gg → adozione/scarto
Output: revenue continua + pipeline lead per AGENCY senza dipendere dai lanci
Gate di uscita: IB-VEND-QA PASS su ogni email + sales page; tracking 100% step
```

### WF-CRO-OTTIMIZZAZIONE (ciclo continuo basato su dati)
```
Trigger: settimanale (loop evergreen) o su anomalia metrica rilevata da IB-VEND-TRACK
  → IB-VEND-TRACK: analisi settimanale → identifica step con conversione più bassa
  → IB-VEND-CRO: formula ipotesi falsificabile (non "proviamo a vedere")
     → variante con 1 SOLO elemento cambiato → approvazione IB-COORD-VENDITE
  → rollout su % traffico (non su tutto) → attesa dati (campione minimo statistico)
  → IB-VEND-CRO: analisi → conclusione solo a campione minimo raggiunto → adozione o scarto
Output: variante adottata (o scartata con rationale) + documentazione in infobusiness/vendite/funnel
Gate di uscita: nessun test "conclusivo" prima del campione minimo; risultato documentato
```

---

## Flussi con ecosistemi esterni

### IB-L2-VEND ← team-prezzi (B-003)
```
IB-VEND-OFFER slotta l'offer stack pronto (value stack, bonus, garanzia, bump, upsell)
ma NON i numeri. Riceve da B-003: catalogo prezzi approvati per prodotto.
Schema: {prodotto_id, prezzo_base, prezzi_bump[], prezzi_upsell[], approvato_da, data_approvazione}
Vincolo B-002/B-003: nessun prezzo placeholder in produzione. Prima dell'approvazione → go live slitta.
```

### IB-L2-VEND → 06-PLATFORM (HC-PL-IB-01)
```
IB-VEND-SALESPAGE consegna copy approvato → PLATFORM costruisce con empire-premium-style + deploy.
IB-VEND-CHECKOUT coordina con PLATFORM la pagina pagamento, paywall, recupero carrelli.
Schema: {prodotto_id, copy_approvato_path, offer_stack, eventi_da_tracciare[], checkout_config}
Acceptance: pagina ≤5s, mobile responsive, ogni link funzionante, checkout testato con transazione reale.
```

### IB-L2-VEND → IB-L2-COMM (post-purchase)
```
All'acquisto, IB-VEND-CHECKOUT emette handoff post-purchase a IB-L2-COMM.
Schema: {acquirente_id, prodotto_id, data_acquisto, canale_acquisizione, segnale_lead_caldo}
IB-L2-COMM avvia WF-ONBOARDING-STUDENTE; il segnale lead caldo alimenta cross-sell scout → AGENCY.
```

### IB-L2-VEND ← 08-INTELLIGENCE
```
IB-VEND-SALESPAGE richiede a 08-INTELLIGENCE il frame Founder Authority Stack (intelligence Beggiato)
per la sequenza nurture. Schema: {prodotto_id, frame: "founder_authority_stack", asset_autorita[]}
Risposta: struttura valore → autorità → offerta + asset di autorità (casi, credenziali verificabili).
```

---

## Handoff contract

| Contract | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-B003-IB-VEND-01` | B-003 → IB-VEND-OFFER | catalogo prezzi approvati | prezzo approvato presente prima di ogni build in produzione |
| `HC-PL-IB-01` | IB-VEND → 06-PLATFORM | copy_approvato + offer_stack + eventi[] | pagina ≤5s, mobile, link ok, checkout collegato e testato |
| `HC-IB-VEND-COMM-01` | IB-VEND-CHECKOUT → IB-L2-COMM | acquirente_id + prodotto_id + canale | onboarding avviato ≤24h dall'acquisto |
| `HC-INT-IB-VEND-01` | 08-INT → IB-VEND-SALESPAGE | frame Founder Authority Stack | asset di autorità verificabili (no claim senza proof) |
| `HC-MKT-IB-VEND-01` | 04-MKT → IB-VEND-SALESPAGE | direction APSOC + brand_kit + email base | brand_kit dichiarato; framework copy fornito |

---

## Namespace memoria

```
infobusiness/vendite/
├── salespage/
│   ├── {prodotto_id}/
│   │   ├── offer_stack.json     → value stack, bonus, garanzia, bump, upsell, naming
│   │   ├── copy_apsoc.md        → copy sales page approvato (APSOC ≥80)
│   │   ├── qa_log.json          → esiti gate G-VEND (PASS/FAIL + feedback)
│   │   └── state.json           → stato build, deploy, tracking, versione
│   └── _catalogo.md             → indice sales page canoniche per prodotto
├── evergreen/
│   ├── {prodotto_id}/
│   │   ├── opt_in.md            → opt-in page + lead magnet collegato
│   │   ├── nurture_sequence.md  → sequenza email (5-7) frame Founder Authority Stack
│   │   └── state.json           → step attivi, metriche per step, A/B in corso
│   └── _config.md               → configurazione evergreen globale
├── funnel/                       → namespace CRO (dossier §IB-L2-VEND)
│   ├── tests/{test_id}.json     → ipotesi, variante, campione, esito, decisione
│   ├── metriche_step.json       → conversione per step (loop settimanale)
│   └── offer_stack_corrente.md  → offer stack attivo (snapshot)
└── tracking/
    ├── eventi_config.json       → mappa eventi pixel + UTM per fonte
    └── report/{periodo}.md      → report conversioni per step
```

---

## Skill del reparto

| Skill | File | Funzione |
|---|---|---|
| `funnel-gate` (P1, nuova) | `skills/SKILLS.md` | Gate G-VEND deterministico: percorso end-to-end + eventi 100% + checkout testato |
| `cro-copy-architect` (esistente) | mapping dossier | Copy APSOC sales page + email (IB-VEND-SALESPAGE) |
| `empire-premium-style` (esistente) | mapping dossier | Build pagina premium → handoff PLATFORM |
| `lead-magnets` (esistente) | mapping dossier | Opt-in page + lead magnet (IB-VEND-LEAD) |
| `ab-testing` · `cro` (esistenti) | mapping dossier | Disegno ed esecuzione test funnel (IB-VEND-CRO) |
| `analytics` (esistente) | mapping dossier | Tracking eventi, UTM, attribution (IB-VEND-TRACK) |
| `paywalls` (esistente) | mapping dossier | Order bump, upsell, upgrade path (IB-VEND-OFFER/CHECKOUT) |

---

## Connessioni

- [[README]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-VEND-Vendite-Funnel/README.md`
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-VEND
- [[WF-SALESPAGE]] · `workflow/WF-SALESPAGE.md`
- [[WF-FUNNEL-EVERGREEN]] · `workflow/WF-FUNNEL-EVERGREEN.md`
- [[WF-CRO-OTTIMIZZAZIONE]] · `workflow/WF-CRO-OTTIMIZZAZIONE.md`
- [[IB-SALES-funnel]] · `company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-SALES-funnel.md` (agente wrappato)
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — prove non promesse, no scarcity falsa)
