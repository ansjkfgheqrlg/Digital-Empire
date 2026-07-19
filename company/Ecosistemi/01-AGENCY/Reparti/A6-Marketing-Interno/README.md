---
Type: REPARTO
Status: Active
Tags: #reparto #agency #marketing-interno #proof #case-study #upsell #A6
Created: 2026-07-11
Last updated: 2026-07-11
---

# A6 — Marketing Interno & Proof

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6`
> **Standard:** CF-grade (ADR-007) · **Topologia:** `star` — task paralleli, a bassa frequenza

---

## Missione

Presidiare la **vetrina e la prova sociale** dell'agency: case study, testimonianze, landing e
presentazione, upsell mapping. A6 genera inbound e produce le **munizioni** che A2 usa
nell'outreach e A3 nei preventivi.

Regola fondamentale: **"prove non promesse"** (Mandato Art.1-2). Le metriche si raccolgono
attivamente dal cliente, non si presumono. Se il cliente non fornisce numeri → case study
qualitativo, mai numeri fabbricati.

**Confine netto: A6 possiede la PROVA, non l'implementazione.** Non scrive il copy lungo
(A5 / 04-MARKETING), non costruisce né deploya pagine (06-PLATFORM), non decide l'upsell
(segnala ad A3; la proposta passa da Max).

---

## Roster del reparto (6 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A6-COORD` | Coordinatore Marketing Interno | `agenti/ag-a6-coord.md` | coordinator | sonnet | Riceve i segnali (Gate Delivery, 90gg chiusi, gap vetrina) e orchestra i task in parallelo |
| `AG-A6-PROOF` | Proof Collector | `agenti/ag-a6-proof.md` | worker | haiku | Raccoglie testimonianze e metriche reali a fine 90gg — raccolta attiva, mai presunta |
| `AG-A6-CASE` | Case Study Writer | `agenti/ag-a6-case.md` | worker | sonnet | Case study in struttura APSOC (skill `case-study-forge`); solo numeri verificati |
| `AG-A6-UPSELL` | Upsell Mapper | `agenti/ag-a6-upsell.md` | worker | sonnet | Matrice cliente → offerta successiva (skill `upsell-mapper`); attivo solo dopo Gate Delivery + NPS alto |
| `AG-A6-INBOUND` | Inbound Tracker | `agenti/ag-a6-inbound.md` | worker | sonnet | Traccia i lead da landing/presentazione; misura la conversione; propone ottimizzazioni |
| `AG-A6-QA` | Brand Gate | `agenti/ag-a6-qa.md` | verifier | sonnet | **Bloccante** su ogni asset pubblico: no claim senza proof; conformità Mandato Art.1-2 |

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-CASE-STUDY** | `workflow/WF-CASE-STUDY.md` | Da delivery chiusa a case study pubblicato: raccolta proof → scrittura APSOC → asset → pubblicazione | AG-A6-QA (Brand Gate): solo metriche verificate con `fonte` e `consenso_cliente` |
| **WF-ASSET-VETRINA** | `workflow/WF-ASSET-VETRINA.md` | Manutenzione di landing e presentazione: identifica i gap, apre ticket a 06-PLATFORM | AG-A6-QA: Brand Gate su ogni modifica; **mai deploy autonomo da A6** |
| **WF-UPSELL-REFERRAL** | `workflow/WF-UPSELL-REFERRAL.md` | Cliente a 90gg con NPS alto → mappa l'offerta successiva o la richiesta di referral | AG-A6-QA: nessun upsell automatico; la proposta passa da A3 e da Max |

---

## Gate del reparto — Brand Gate

**Presidio: AG-A6-QA. Bloccante su ogni asset pubblico, prima della pubblicazione.**

| Blocca se | Motivo |
|---|---|
| Claim numerico senza metrica verificata dal cliente | Mandato Art.2 — prove, non promesse |
| Metrica senza campo `fonte` o senza `consenso_cliente` | Non può esistere in namespace |
| Testimonianza parafrasata o ricostruita | Si cita testualmente, non si riscrive |
| Brand voice non conforme / dependency-language | Mandato Art.1 — identità "agenzia da licenziare" |
| Upsell attivato durante i 90gg di supporto | L'upsell parte solo a supporto chiuso e con NPS alto |

FAIL → rework sulla sezione non conforme. **Mai bypass.**
Cliente che non risponde alla richiesta di testimonianza → un solo follow-up dopo 7gg, poi si
chiude senza case study. Nessuna pressione: rovinerebbe il rapporto e violerebbe il gate.

---

## KPI del reparto

| KPI | Owner | Definizione | Baseline |
|---|---|---|---|
| Case study per cliente chiuso | AG-A6-CASE | Case study prodotti / delivery chiuse (con metriche o qualitativo) | Target 1 per delivery |
| Testimonianze raccolte | AG-A6-PROOF | % clienti che forniscono testimonianza a fine 90gg | [DM] |
| Call da inbound | AG-A6-INBOUND | Call prenotate da landing/case study (non da outreach) | [DM] |
| Upsell/referral mappati | AG-A6-UPSELL | Clienti con opportunità mappata / clienti chiusi con NPS alto | [DM] |
| Claim senza proof pubblicati | AG-A6-QA | Asset pubblici con claim non verificato | Target 0 |

Dettaglio completo → `kpi/KPI.md`.

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | A4-Delivery | Segnale "Gate Delivery firmato" + metriche reali della delivery |
| ← riceve da | A7-Account-Management | Referral + richiesta case study a fine 90gg quando l'NPS è alto |
| ← riceve da | 04-MARKETING | `HC-MK-AG-01` — copy sales page e case study maggiore (refresh strutturali) |
| → consegna a | A2-Acquisizione | Case study e metriche reali come munizioni per l'outreach |
| → consegna a | A3-Preventivi | Proof per i preventivi + opportunità di upsell da trasformare in proposta |
| → consegna a | A5-Copywriting-Interno | Testimonianze reali come prove per copy e libreria obiezioni |
| → consegna a | 03-CONTENT-FACTORY | `HC-AG-CF-01` — brief case study → asset grafici/video |
| → consegna a | 06-PLATFORM | `HC-AG-PL-01` — feature request per landing e presentazione (il deploy è loro) |

---

## Namespace AgentDB

**Chiave canonica: `agency/a6`** — fonte di verità: `../../NAMESPACE.md`.

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a6/case-studies` | Case study per cliente: problema, soluzione, metriche verificate, stato gate | AG-A6-CASE |
| `agency/a6/proof` | Testimonianze e metriche per cliente: fonte, consenso, valore | AG-A6-PROOF |
| `agency/a6/vetrina` | Stato landing/presentazione: gap aperti, ticket 06-PLATFORM, deploy | AG-A6-COORD |
| `agency/a6/upsell` | Proposte upsell/referral: prodotto attuale, next, segnale NPS, esito | AG-A6-UPSELL |
| `agency/a6/inbound` | Lead da inbound: fonte, conversione, ottimizzazioni proposte | AG-A6-INBOUND |

**Regola di integrità:** ogni case study con metriche numeriche deve avere `fonte` e
`consenso_cliente` popolati. Un claim numerico senza fonte verificata **non può esistere**
in namespace.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md` (prove non promesse · no deploy autonomo)
- Stato e ripartibilità a freddo → `state/README.md`

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — gerarchia, flussi, confini, namespace
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6`
- [[ag-a6-qa]] · `agenti/ag-a6-qa.md` — presidio del Brand Gate
- [[WF-CASE-STUDY]] · `workflow/WF-CASE-STUDY.md`
- [[WF-UPSELL-REFERRAL]] · `workflow/WF-UPSELL-REFERRAL.md`
- [[A4-Delivery]] · fornitore del segnale "delivery chiusa" + metriche reali
- [[A7-Account-Management]] · fornitore di referral e segnale NPS
