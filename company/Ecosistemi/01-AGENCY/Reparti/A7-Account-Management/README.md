---
Type: REPARTO
Status: Active
Tags: #reparto #agency #account-management #customer-success #retention #upsell #A7
Created: 2026-06-23
Last updated: 2026-06-23
---

# A7 — Account Management & Customer Success

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A7`
> **Standard:** CF-grade (ADR-007) · **Reparto NUOVO v2 — colma il gap "nessuno possiede la relazione post-firma"**

---

## Missione

Presidiare la relazione con il cliente dalla firma del contratto fino al termine del supporto
90gg e oltre — onboarding, monitoraggio salute, intercettazione churn, closure, upsell, referral,
reingaggio.

**A7 (questo reparto) possiede la RELAZIONE post-firma.**
**A4-Delivery possiede l'ESECUZIONE dello sprint.**

Il v1 aveva un gap netto: il cliente veniva "consegnato" e poi non aveva più un interlocutore
strutturato. In v2 ogni cliente riceve un Key Account Manager (AG-A7-COORD) alla firma, che resta
proprietario della relazione per tutto il ciclo. A7 non lavora i ticket tecnici (quello è A4): li
supervisiona a livello di SLA e agisce sul rischio. Trasforma un cliente soddisfatto a fine 90gg
in upsell (→ A3), referral (→ A6) o cross-sell (→ 02-INFO).

---

## Roster del reparto (7 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A7-COORD` | KAM Lead (Key Account Manager) | `agenti/ag-a7-coord.md` | coordinator | sonnet | Proprietario della relazione cliente post-firma; assegnato alla firma; riporta ad AG-DIR |
| `AG-A7-ONBOARD` | Onboarding Specialist | `agenti/ag-a7-onboard.md` | worker | sonnet | Prima settimana post-firma: introduce processo e milestone al cliente |
| `AG-A7-MID` | Mid-Point Reviewer | `agenti/ag-a7-mid.md` | worker | sonnet | Check a metà delivery (G+3-4): clima cliente, aggiustamenti di scope |
| `AG-A7-CLOSE` | Closure Manager | `agenti/ag-a7-close.md` | worker | sonnet | Fine 90gg: NPS survey, feedback, proposta upsell/referral |
| `AG-A7-HEALTH` | Account Health Monitor | `agenti/ag-a7-health.md` | worker | haiku | Dashboard salute cliente; alert automatici di rischio churn |
| `AG-A7-COMM` | Comunicatore Cliente | `agenti/ag-a7-comm.md` | worker | sonnet | Drafta comunicazioni formali sulla voce di Max (milestone, anomalie) |
| `AG-A7-QA` | Verificatore Customer Success | `agenti/ag-a7-qa.md` | verifier | sonnet | Controlla SLA ticket (A4), milestone, NPS; bloccante su rischio |

---

## Workflow del reparto (2 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-CUSTOMER-LIFECYCLE** | `workflow/WF-CUSTOMER-LIFECYCLE.md` | Presidiare ogni cliente dalla firma al termine dei 90gg con touchpoint strutturati | AG-A7-QA: NPS raccolto entro G+90; milestone loggate; nessun cliente senza KAM |
| **WF-RETENTION-ALERT** | `workflow/WF-RETENTION-ALERT.md` | Intercettare rischi di churn PRIMA che diventino perdita del cliente | AG-A7-QA: alert entro 24h dal segnale; azione registrata in `agency/07-account/alerts` |

---

## Skill del reparto

| Skill | Priorità | File |
|---|---|---|
| `churn-prevention` (esistente, mappata) | — | Motore di AG-A7-HEALTH + WF-RETENTION-ALERT |
| `support-90` (esistente, mappata) | — | Playbook supporto 90gg per AG-A7-COORD |
| `upsell-mapper` (esistente, mappata) | — | Mappatura opportunità per AG-A7-CLOSE |
| `revops` (esistente, mappata) | — | Ausiliaria: retention/expansion metrics per AG-A7-QA |
| `account-health-monitor` | P2 | `skills/SKILLS.md` |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| NPS medio fine 90gg | AG-A7-CLOSE | Media NPS raccolto a G+90 su clienti chiusi nel periodo; baseline [DM] |
| % clienti con upsell/referral attivato | AG-A7-COORD | Clienti con handoff a A3/A6/02-INFO / tot clienti chiusi; [DM] |
| SLA ticket rispettato (da A4) | AG-A7-QA | % ticket entro SLA contrattuale; letto da A4-Delivery |
| % clienti con KAM assegnato | AG-A7-QA | Clienti con campo `kam` popolato / tot clienti attivi; target 100% |
| Alert churn risolti entro 24h | AG-A7-HEALTH | Alert con azione registrata entro 24h / tot alert; [DM] |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | A4-Delivery | Cliente live (contratto firmato) + SLA ticket + artefatti milestone |
| ← riceve da | 09-OPERATIONS (A10-QA) | Gate Delivery G+7: conferma milestone loggate |
| → consegna a | A3-Preventivi | Upsell mappato a fine ciclo (nuovo sprint / retainer) |
| → consegna a | A6-Marketing-Interno | Referral + richiesta case study quando NPS alto |
| → consegna a | 02-INFO-BUSINESS | Cross-sell (corso / info-product) per clienti con bisogno formativo |
| → consegna a | 08-INTELLIGENCE | NPS + churn rate aggregati per report di ecosistema (sola lettura) |

---

## Escalation

- Cliente senza KAM assegnato rilevato in `agency/07-account/clients` → AG-A7-QA blocca; AG-A7-COORD assegna prima di qualsiasi altra azione.
- NPS intermedio ≤6 o segnale churn senza azione entro 24h → AG-A7-HEALTH escala ad AG-DIR.
- Cliente a rischio che richiede intervento commerciale → AG-A7-COORD coinvolge Max (no decisione autonoma su sconti/rimborsi).
- Conflitto su scope tra cliente e A4-Delivery → AG-A7-MID media; se non risolto → AG-DIR.
- NPS non raccolto a G+90 → AG-A7-QA blocca la closure; il ciclo non è chiuso senza NPS.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`

---

## Connessioni

- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A7`
- [[A4-Delivery]] · fornitore di cliente live + SLA ticket
- [[A3-Preventivi]] · destinatario degli upsell mappati
- [[A6-Marketing-Interno]] · destinatario di referral e case study
- [[WF-CUSTOMER-LIFECYCLE]] · `workflow/WF-CUSTOMER-LIFECYCLE.md`
- [[WF-RETENTION-ALERT]] · `workflow/WF-RETENTION-ALERT.md`
