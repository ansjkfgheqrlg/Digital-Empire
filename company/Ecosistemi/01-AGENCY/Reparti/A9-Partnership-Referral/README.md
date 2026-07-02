---
Type: REPARTO
Status: Active
Tags: #reparto #agency #partnership #referral #non-icp #A9
Created: 2026-06-23
Last updated: 2026-06-23
---

# A9 — Partnership & Referral

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A9`
> **Standard:** CF-grade (ADR-007) · **Reparto NUOVO v2 — greenfield (non esisteva nel v1)**

---

## Missione

Dare una casa ai lead che non rientrano nei 3 prodotti DE (lead **non-ICP**) e costruire un
ecosistema di **partner** che inviano **referral** qualificati. Nel v1 questa casa non esisteva:
i lead non-ICP venivano persi e nessun canale strutturato di referral alimentava la pipeline.

In v2, A9 fa tre cose:
1. **Triage non-ICP** — riceve i lead scartati/parcheggiati da A1-Ricerca (AG-A1-QUAL → "scarta/nurture")
   e decide: partner potenziale · lead da nurture · archivio. Nessun lead muore senza decisione tracciata.
2. **Partnership** — identifica, contatta e onboarda partner complementari (agenzie no-AI, consulenti HR,
   commercialisti) con accordo referral scritto e commissione da catalogo.
3. **Referral pipeline** — gestisce ogni lead in arrivo da un partner, ne verifica il profilo ICP,
   e lo instrada in fast-track ad A8-Closing (se già caldo) o ad A2-Acquisizione (se richiede outreach).

A9 **non chiude i deal** (lo fa A8-Closing) e **non fa ricerca lead a freddo** (lo fa A1-Ricerca):
trasforma relazioni e scarti in pipeline qualificata, con consenso verificato su ogni lead.

---

## Roster del reparto (6 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A9-COORD` | Coordinatore Partnership | `agenti/ag-a9-coord.md` | coordinator | sonnet | Coordina il reparto; gestisce relazioni partner; risponde KPI ad AG-DIR |
| `AG-A9-QA` | Verificatore Partner Gate | `agenti/ag-a9-qa.md` | verifier | sonnet | Gate bloccante: ogni referral entra con profilo ICP compilato + consenso verificato; no lead freddi |
| `AG-A9-QUALIFY` | Lead Non-ICP Router | `agenti/ag-a9-qualify.md` | worker | sonnet | Riceve lead non-ICP da A1; valuta: partner potenziale / lead nurture / archivio |
| `AG-A9-OUTREACH` | Partner Outreach | `agenti/ag-a9-outreach.md` | worker | sonnet | Contatta potenziali partner; proposta referral con commissione da catalogo |
| `AG-A9-MGMT` | Partner Relationship Manager | `agenti/ag-a9-mgmt.md` | worker | sonnet | Mantiene la relazione con partner attivi; aggiornamenti, commissioni, report |
| `AG-A9-INTEL` | Partnership Intelligence | `agenti/ag-a9-intel.md` | worker | haiku | Monitora referral ricevuti, tasso conversione per partner, commissioni maturate |

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-PARTNER-ONBOARDING** | `workflow/WF-PARTNER-ONBOARDING.md` | Identificare + onboardare partner complementari: candidato → contatto → accordo referral → registrazione → briefing | Accordo scritto firmato; commissione da catalogo; partner briefato su ICP DE |
| **WF-REFERRAL-PIPELINE** | `workflow/WF-REFERRAL-PIPELINE.md` | Gestire ogni lead da partner (`HC-PT-AG-01`) dal ricevimento alla chiusura, con verifica ICP + consenso | AG-A9-QA: profilo ICP compilato + consenso verificato; nessun lead freddo |
| **WF-NONICP-ROUTING** | `workflow/WF-NONICP-ROUTING.md` | Instradare i lead non-ICP da A1 (scarta/nurture): partner potenziale / nurture / archivio | Decisione tracciata per ogni lead; nessun lead perso senza esito |

---

## Skill del reparto

| Skill | Priorità | File |
|---|---|---|
| `partner-onboarder` | P2 | `skills/SKILLS.md` |
| `referral-router` | P3 | `skills/SKILLS.md` |
| `referrals` (esistente, mappata) | — | Motore programma referral; ausiliaria AG-A9-MGMT |
| `co-marketing` (esistente, mappata) | — | Ausiliaria AG-A9-OUTREACH per partnership/joint |
| `icp-radar` (esistente, mappata) | — | Triage non-ICP: usata da AG-A9-QUALIFY e AG-A9-QA |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Lead da referral / mese | AG-A9-INTEL | N. lead entrati via partner nel periodo; baseline [DM] dal primo mese live |
| Tasso conversione referral vs outreach diretto | AG-A9-INTEL | % chiusura lead da referral confrontata con lead da A2; [DM] |
| Commissioni maturate | AG-A9-MGMT | Somma commissioni dovute ai partner su deal chiusi; solo con contratto firmato |
| Lead non-ICP con esito tracciato | AG-A9-QUALIFY | % lead non-ICP da A1 con decisione (partner/nurture/archivio); target 100% |
| Gate AG-A9-QA PASS al primo tentativo | AG-A9-QA | % referral che passano il gate ICP+consenso senza rework |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | A1-Ricerca (AG-A1-QUAL) | Lead non-ICP parcheggiati/scartati ("scarta/nurture") → input WF-NONICP-ROUTING |
| ← riceve da | A7-Account-Management | Segnale referral da cliente attivo (cliente che indica un contatto) |
| → consegna a | A8-Closing | Lead partner qualificato e caldo → fast-track chiusura |
| → consegna a | A2-Acquisizione | Lead referral che richiede outreach prima della chiusura |
| → consegna a | AG-DIR | Report KPI partnership; commissioni maturate; pipeline referral |

---

## Escalation

- Partner che invia lead senza profilo ICP o senza consenso → AG-A9-QA blocca; AG-A9-MGMT richiama il partner al briefing.
- Lead non-ICP ambiguo (potrebbe rientrare in un prodotto DE futuro) → AG-A9-QUALIFY segnala ad AG-A9-COORD, non archivia in autonomia.
- Commissione richiesta da partner senza contratto firmato → AG-A9-MGMT rifiuta; escalation ad AG-DIR (no pagamenti senza accordo).
- Conflitto su ownership di un lead (referral vs già in pipeline A2) → AG-A9-COORD + coordinatore A2; escalation AG-DIR se non risolto.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`

---

## Connessioni

- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A9`
- [[A1-Ricerca]] · fornitore lead non-ICP (AG-A1-QUAL "scarta/nurture")
- [[A7-Account-Management]] · fornitore segnale referral da clienti attivi
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — gerarchia, flussi, namespace
- [[WF-PARTNER-ONBOARDING]] · `workflow/WF-PARTNER-ONBOARDING.md`
- [[WF-REFERRAL-PIPELINE]] · `workflow/WF-REFERRAL-PIPELINE.md`
