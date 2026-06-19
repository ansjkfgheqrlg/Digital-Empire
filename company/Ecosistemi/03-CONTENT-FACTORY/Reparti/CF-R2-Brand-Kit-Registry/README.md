---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #brand-kit #multi-tenant #pre-produzione #CF-R2
Created: 2026-06-19
Last updated: 2026-06-19
---

# CF-R2 — Brand-Kit & Tenant Registry

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Pre-Produzione · **Livello:** L2 Reparto
> **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R2`
> **Standard:** CF-grade (ADR-007) · **Wrappa asset brand v1 esistenti (ADR-003 — mai riscrivere)**

---

## Missione

Creare, mantenere e validare tutti i `brand_kit` e `icp.json` dell'ecosistema CF-DE.
Il reparto è il **custode dell'identità** visiva e vocale di ogni tenant: nessun contenuto
viene prodotto senza brand_kit approvato e icp.json valido.

CF-R2 impedisce il brand-drift a monte (prevenzione) e lo rileva a valle (monitoraggio
ciclico degli output). Il principio è semplice: un asset prodotto fuori specifica non è
un errore di produzione — è un errore di presidio del registry.

---

## Cosa fa il reparto

1. **Onboarda nuovi tenant** — da brief di onboarding a struttura `brands/<slug>/` completa.
2. **Valida ogni brand_kit** — schema, palette HEX, voice con esempi si/no, canali.
3. **Sincronizza con Canva** — brand kit e template Canva aggiornati per ogni tenant.
4. **Monitora il brand-drift** — campionamento sistematico output vs brand_kit ogni ciclo.
5. **Gestisce gli ICP** — crea e aggiorna `brands/<slug>/icp.json` (dolori, desideri, obiezioni).
6. **Approva i tenant** — nessun ordine CF-DE processato per brand non approvato da CF-R2-COORD.

## Cosa NON fa

- Non produce contenuti: quello è R3 (Video), R4 (Testuale), R5 (Visual).
- Non scrive brief: quello è CF-R1 (Strategia & Brief).
- Non valida gli ordini di produzione: quello è CF-D-QA (Director team).
- Non pubblica: quello è CF-R7 (Pubblicazione & Distribuzione).
- Non tocca i file originali in `carousel-factory/brands/`: wrappa come seed, mai riscrive (ADR-003).
- Non approvato il budget di crediti engine: quello è CF-SENT-COST (Director).

---

## Roster del reparto (6 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CF-R2-COORD` | Coordinatore Brand-Kit | `agenti/cf-r2-coord.md` | coordinator | sonnet | Gestisce registry brand; approva nuovi tenant; riporta a L1-PRE |
| `CF-R2-QA` | Verificatore Brand Gate | `agenti/cf-r2-qa.md` | verifier | sonnet | Valida brand_kit: schema, palette HEX, voice con esempi; BLOCCA incompleti |
| `CF-R2-CREATOR` | Brand-Kit Builder | `agenti/cf-r2-creator.md` | worker | sonnet | Crea `brands/<slug>/` completo da brief onboarding |
| `CF-R2-CANVA` | Canva Brand Sync | `agenti/cf-r2-canva.md` | worker | haiku | Sync brand_kit con Canva brand kits via MCP; template per brand |
| `CF-R2-DRIFT` | Brand Drift Monitor | `agenti/cf-r2-drift.md` | monitor | haiku | Campiona output vs brand_kit ogni ciclo; alert se deviazione |
| `CF-R2-ICP` | ICP Profiler | `agenti/cf-r2-icp.md` | worker | sonnet | Crea/aggiorna `brands/<slug>/icp.json` |

---

## Workflow del reparto (2 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-BRAND-ONBOARDING** | `workflow/WF-BRAND-ONBOARDING.md` | Brief tenant → struttura brands/ completa → approvazione | CF-R2-QA: schema completo; CF-R2-COORD: approvazione; BLOCCANTE |
| **WF-BRAND-MAINTENANCE** | `workflow/WF-BRAND-MAINTENANCE.md` | Campionamento drift → alert → correzione → re-validazione | CF-R2-QA: re-validazione brand_kit patchato |

---

## Brand seed (4 tenant dal carousel-factory v1 — WRAPPATI, non riscritti)

I seguenti brand esistono già come asset v1 in `carousel-factory/brands/`. CF-R2 li
tratta come **seed del registry**: legge i loro `config.json` per compilare i
brand_kit CF-grade, senza mai modificare i file originali (ADR-003).

| Slug | Display name | Handle | Fonte seed |
|---|---|---|---|
| `mentalita-brutale` | Mentalità Brutale | @mentalita.brutale | `carousel-factory/brands/mentalita-brutale/config.json` |
| `brand-agency` | Brand Agency DE | — | `carousel-factory/brands/brand-agency/config.json` |
| `brand-education` | Brand Education DE | — | `carousel-factory/brands/brand-education/config.json` |
| `brand-personal` | Brand Personal DE | — | `carousel-factory/brands/brand-personal/config.json` |

---

## Namespace memoria

| Namespace | Contenuto |
|---|---|
| `cf/brand-kits` | Registry globale brand_kit (index tenant attivi) |
| `brands/<slug>/` | Brand_kit, icp.json, state.json, assets/ per ogni tenant |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| N. tenant attivi | CF-R2-COORD | N. brand con brand_kit approvato nel registry; [DM] baseline |
| Brand_kit completi/incompleti | CF-R2-QA | N. brand_kit che superano il gate / tot brand nel registry |
| Drift alerts per ciclo | CF-R2-DRIFT | N. alert emessi per deviazione brand nel periodo |
| Latenza onboarding | CF-R2-COORD | Ore da brief tenant a brand_kit approvato; [DM] baseline |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | CF-Director (CF-D-DISPATCH) | Richiesta onboarding nuovo tenant o aggiornamento brand_kit |
| ← riceve da | Committenti (Agency, Info-Business, Marketing) | Brief brand per onboarding nuovi tenant |
| → consegna a | CF-R1 (Strategia & Brief) | brand_kit validato per ogni tenant (input obbligatorio brief) |
| → consegna a | CF-D-QA | Conferma brand_kit + icp.json presenti e validi (gate ordine) |
| → consegna a | CF-R3/R4/R5 (Produzione) | brand_kit come riferimento per ogni asset prodotto |
| → consegna a | Canva (via MCP) | Brand kit sincronizzato + template per brand |

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R2`
- [[CF-R1-Strategia-Brief]] · destinatario brand_kit validati
- [[CF-R0-Director]] · riporta a CF-D-DISPATCH per onboarding; CF-D-QA usa registry
- [[WF-BRAND-ONBOARDING]] · `workflow/WF-BRAND-ONBOARDING.md`
- [[WF-BRAND-MAINTENANCE]] · `workflow/WF-BRAND-MAINTENANCE.md`
