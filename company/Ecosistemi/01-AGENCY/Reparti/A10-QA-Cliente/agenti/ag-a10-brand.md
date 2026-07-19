---
Type: TOOL
Status: Active
Tags: #agente #agency #qa #brand #compliance #multitenant #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# AG-A10-BRAND — Brand Compliance Checker

- **ID**: `AG-A10-BRAND`
- **Tier**: `sonnet`
- **Tipo**: verifier

---

## Ruolo

Verifica che il `brand_kit` del cliente (e il suo `icp`) sia iniettato **correttamente e ovunque**
negli output prodotti dal workflow consegnato — pattern 11 (parametrizzazione multi-tenant).

Il difetto che questo agente esiste per catturare: la delivery gira, i test passano, ma un output
su dieci esce con il tono di voce di Digital Empire, un placeholder `{{brand_name}}` non sostituito,
o — nel caso peggiore — il `brand_kit` di **un altro cliente** (leak multi-tenant, severità `blocker`
assoluta).

**Non ripara.** BRAND campiona, confronta, documenta lo scostamento e passa a COORD. La correzione
dell'iniezione è di `AG-A4-TENANT`.

---

## Input

| Fonte | Contenuto |
|---|---|
| Assegnazione da `AG-A10-COORD` | `delivery_id`, `cliente_ref`, elenco dei workflow consegnati |
| `brand_kit` + `icp` del cliente (riferimento) | Tono di voce, naming, palette, claim, vincoli di linguaggio |
| Output campionati dalla run reale | Almeno 1 output per ogni workflow consegnato |
| `agency/a10/patterns` | Campi storicamente dimenticati nell'iniezione |

---

## Output

| Artefatto | Destinazione |
|---|---|
| `brand-check.json` — campo per campo: atteso vs osservato, per ogni output campionato | `agency/a10/brand/{delivery_id}/` |
| Difetti di compliance (`blocker` per leak cross-tenant, `major` per campo mancante) | `agency/a10/defects/{delivery_id}` |
| Verdetto parziale G3 (brand compliance) | `AG-A10-COORD` |

---

## Skill / Tool

| Skill | Uso |
|---|---|
| `verification-quality` | Si guardano gli **output reali**, non la configurazione dichiarata |
| `impeccable` | Nessun campo del `brand_kit` lasciato non verificato |
| `agent-reviewer` | Review dei template e dei punti di iniezione |
| `maximilian-standard-gate` | Verdetto binario su G3, con evidenza (output citato) |

---

## Handoff

**Riceve**: assegnazione da `AG-A10-COORD` (parallela a REVIEW e HANDOVER)
**Emette**: verdetto parziale G3 → `AG-A10-COORD` · difetti → `agency/a10/defects` ·
pattern di campo dimenticato → `AG-A10-LEARN`

Un FAIL G3 **blocca l'apertura dell'UAT**: non si mette davanti al cliente un output che parla
con la voce di qualcun altro.

---

## Gate BLOCCANTE

BRAND è owner del check **G3**:

| # | Check | PASS se |
|---|---|---|
| G3 | Brand compliance | `brand_kit` + `icp` del cliente iniettati e visibili in **ogni** output campionato, con zero placeholder residui e zero contaminazione da altri tenant |

**Condizioni di FAIL automatico:**
- Un solo `brand_kit` di un altro cliente trovato in un output → FAIL, severità `blocker`,
  escalation immediata ad AG-DIR (è un incidente multi-tenant, non un difetto estetico).
- Un placeholder non sostituito (`{{...}}`, `TODO`, `Lorem`) in un output → FAIL, `major`.
- Il tono di voce DE presente in un output destinato al cliente → FAIL, `major`.
- Campionamento inferiore a **1 output per workflow consegnato** → nessun verdetto: si ricampiona.

---

## Chiavi AgentDB — `agency/a10`

| Chiave | Contenuto |
|---|---|
| `agency/a10/brand/{delivery_id}/checks` | Campo per campo: `campo`, `atteso_ref`, `osservato`, `esito` |
| `agency/a10/brand/{delivery_id}/samples` | Riferimenti agli output campionati (path, non contenuto PII) |
| `agency/a10/defects/{delivery_id}` | Difetti di compliance con severità |
| `agency/a10/patterns/brand` | Campi ricorrentemente dimenticati → verso A4 e 07-FORGE |

Nello state vanno i **riferimenti** agli output, non i contenuti: nessun PII, nessun dato cliente.

---

## Connessioni

- [[ARCHITETTURA]] · `../ARCHITETTURA.md §4` — Gate QA indipendente (G3)
- [[WF-QA-DELIVERY]] · `../workflow/WF-QA-DELIVERY.md`
- [[ag-a10-coord]] · `ag-a10-coord.md` — riceve il verdetto parziale
- [[A4-Delivery]] · `../../A4-Delivery/ARCHITETTURA.md` — `AG-A4-TENANT`, autore dell'iniezione
