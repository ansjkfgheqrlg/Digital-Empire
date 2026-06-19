---
Type: ENTITY
Status: Active
Tags: #reparto #infobusiness #community #retention #onboarding #IB-L2-COMM
Created: 2026-06-18
Last updated: 2026-06-18
---

# IB-L2-COMM — COMMUNITY & RETENTION

> **Livello:** L2 — Reparto di 02-INFO-BUSINESS
> **Namespace AgentDB:** `infobusiness/community/`
> **Coordinator:** `IB-COORD-COMMUNITY` (Sonnet)
> **Roster:** 8 agenti · 3 workflow CF-grade
> **Missione-in-una-riga:** il prodotto inizia DOPO l'acquisto — onboarding ≤24h, community
> di valore, completamento corsi, testimonianze reali, lead caldi verso 01-AGENCY su consenso.

---

## Missione

IB-L2-COMM è il reparto che **trasforma un acquirente in uno studente attivo, e uno studente
attivo nel miglior venditore del prossimo lancio**. Onboarda ogni acquirente entro 24h, gestisce
la community come spazio di valore continuativo, presidia il completamento dei corsi, raccoglie
testimonianze solo su metriche reali, e identifica gli studenti pronti per la versione "fatta per
loro" (01-AGENCY) — sempre su segnale esplicito e consenso documentato.

**Il reparto NON vende agli studenti.** La community esiste per gli studenti, non per fare outreach.
Il cross-sell verso AGENCY avviene SOLO su segnale esplicito e consenso verificato (mai automatico).
Il confine è netto: l'esperienza post-acquisto è il prodotto; la conversione verso AGENCY è un
sottoprodotto consensuale, non l'obiettivo della relazione.

**Connessione col Mandato:** le testimonianze rispettano Art.2 ("prove non promesse") — solo
metriche reali e verificabili, mai claim di risultato non sostenuti. Il divieto di outreach
automatico sugli studenti è un vincolo di integrità non negoziabile.

---

## Posizione nella gerarchia

```
02-INFO-BUSINESS (L1) — IB-DIRECTOR
  └── IB-L2-COMM COMMUNITY & RETENTION ← questo reparto
        │
        ├── riceve da: IB-L2-LAUNCH (coorte studenti post cart-close)
        ├── coordina con: formazione-admin / formazione-student (piattaforma corsi)
        ├── coordina con: IB-L2-PRODUCT (segnali completamento = feedback prodotto)
        ├── handoff verso: 01-AGENCY (lead caldi cross-sell, contract HC-IB-AG-01)
        └── riporta a: IB-DIRECTOR (L1) per KPI mensili e escalation
```

---

## Roster agenti (8)

| ID | Agente | Tier | Ruolo sintetico |
|---|---|---|---|
| `IB-COORD-COMMUNITY` | Capo Area Community | Sonnet | Coordinator: orchestra i 3 WF, gestisce piano community, escalation a IB-DIRECTOR |
| `IB-COMM-QA` | Verificatore Community | Sonnet | Gate G-COMM: consenso cross-sell verificato + testimonianze su metrica reale (indipendente) |
| `IB-COMM-ONBOARDER` | Onboarding Specialist | Haiku | Sequenza benvenuto + attivazione: acquisto → email ≤1h → accesso ≤24h → modulo 1 ≤7gg |
| `IB-COMM-HEALTH` | Student Health Monitor | Haiku | Dashboard salute studente: progress, ultimo accesso, alert abbandono precoce |
| `IB-COMM-ENGAGE` | Engagement Runner | Haiku | Rituali community: prompt discussione, Q&A, contenuto bonus, moderazione |
| `IB-COMM-RETENTION` | Retention Specialist | Sonnet | Segnali abbandono → win-back; sequenze recovery; skill `churn-prevention`; mai invasivo |
| `IB-COMM-SOCIAL` | Social Proof Collector | Sonnet | Raccolta testimonianze a milestone: reale, verificabile, non sollecitata prima del milestone |
| `IB-COMM-CROSSSELL` | Cross-Sell Scout | Sonnet | Scoring segnali "vuole l'implementazione fatta" → handoff HC-IB-AG-01 → AGENCY |

---

## Workflow CF-grade (3)

| Workflow | Scopo sintetico | File |
|---|---|---|
| `WF-ONBOARDING-STUDENTE` | Acquisto → accesso ≤24h → modulo 1 completato ≤7gg, zero friction | `workflow/WF-ONBOARDING-STUDENTE.md` |
| `WF-COMMUNITY-ATTIVA` | Rituali settimanali + Q&A + testimonianze + report mensile engagement | `workflow/WF-COMMUNITY-ATTIVA.md` |
| `WF-CROSSSELL-BRIDGE` | Scoring segnali → consenso verificato → handoff HC-IB-AG-01 → AGENCY | `workflow/WF-CROSSSELL-BRIDGE.md` |

---

## Skill del reparto

| Skill | Tipo | Priorità | Descrizione |
|---|---|---|---|
| `crosssell-bridge` | Propria P0 | Nuova da forgiare | Gate consenso/segnale + scoring deterministico per handoff verso AGENCY |
| `onboarding` | Ausiliaria esistente | P1 | Sequenza attivazione studente — usata da IB-COMM-ONBOARDER |
| `churn-prevention` | Ausiliaria esistente | P1 | Win-back e retention — usata da IB-COMM-RETENTION |
| `community-marketing` | Ausiliaria esistente | P2 | Strategia community WhatsApp/Discord — usata da IB-COMM-ENGAGE |
| `signup` · `referrals` | Ausiliarie esistenti | P2 | Attivazione e passaparola studenti |

Skill `crosssell-bridge` (P0): da forgiare via 07-FORGE con PRD + architettura prima della build.
Rende il gate G-COMM eseguibile deterministicamente (check binario consenso + segnale documentato
+ score ≥ soglia). Vedi `skills/SKILLS.md` per la specifica completa.

---

## KPI presidiati

| KPI | Definizione |
|---|---|
| Onboarding ≤24h | % acquirenti con accesso piattaforma attivo entro 24h dall'acquisto |
| Attivazione modulo 1 | % acquirenti che completano il modulo 1 entro 7gg |
| Completamento corso | % studenti che finiscono il corso (per coorte) |
| Engagement community | % studenti attivi per settimana (login o interazione) |
| Cross-sell qualificati | n. lead cross-sell consensuali passati ad AGENCY per coorte |

*[DM] = da misurare, baseline da stabilire al primo lancio reale.*

---

## Handoff principali

| Direzione | Ecosistema/Reparto | Payload tipico |
|---|---|---|
| ← IB-L2-LAUNCH | Lanci | Coorte acquirenti post cart-close (trigger onboarding) |
| ↔ formazione-student | Piattaforma corsi | Stato progress, ultimo accesso, moduli completati (lettura per IB-COMM-HEALTH) |
| → 01-AGENCY | Acquisizione | `HC-IB-AG-01`: {lead_id, fonte_prodotto, segnale, score, consenso} — lead caldo cross-sell |
| → IB-L2-PRODUCT | Prodotto | Pattern completamento basso = feedback prodotto (non solo problema community) |
| → IB-DIRECTOR | Coordinatore L1 | KPI mensili + escalation reclami/rimborsi/completion critico |

**Regola handoff:** nessun lead passa ad AGENCY senza consenso esplicito verificato da IB-COMM-QA
(gate G-COMM). Il segnale deve essere documentato. Mai outreach automatico sugli studenti.

---

## Escalation

- **Completion rate < 20% per una coorte:** IB-COORD-COMMUNITY segnala a IB-L2-PRODUCT + IB-DIRECTOR.
  È un problema di prodotto, non solo di community — la retention non può salvare un corso debole.
- **Reclamo o richiesta rimborso da studente:** escalation immediata a IB-DIRECTOR / Board. La
  community non gestisce dispute commerciali in autonomia.
- **Pressione a fare outreach automatico sugli studenti (es. "manda la promo AGENCY a tutti"):**
  IB-COMM-QA blocca. Si passa solo chi ha dato segnale + consenso. Nessuna eccezione per urgenza lancio.
- **Testimonianza richiesta senza metrica verificabile:** IB-COMM-QA blocca la pubblicazione.
  Si raccoglie solo ciò che è reale e verificabile (Mandato Art.2).

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-COMM
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` Art.2 ("prove non promesse")
- [[ARCHITETTURA]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-COMM-Community-Retention/ARCHITETTURA.md`
- [[IB-COMMUNITY-manager]] · `company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-COMMUNITY-manager.md` (agente v1 wrappato — ADR-003)
- [[IB-R4-COMMUNITY-RETENTION]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-R4-COMMUNITY-RETENTION.md` (reparto v1 wrappato)
- [[01-ECOSISTEMA-AGENCY]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` (destinatario lead cross-sell)
