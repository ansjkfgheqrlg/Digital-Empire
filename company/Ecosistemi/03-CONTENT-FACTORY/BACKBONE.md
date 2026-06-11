# BACKBONE — 🏭 03-CONTENT-FACTORY

> Come CONTENT-FACTORY si collega al Corporate Backbone di EMPIRE OS.
> Organigramma holding: `company/GRUPPO.md` · Dettagli Backbone: `company/Backbone/`
> Fonte vincolante: `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §1, §8.

---

## BUS (Message bus)

### Punto d'ingresso unico: il contratto di ordine

Ogni richiesta a CF entra SOLO come ordine strutturato (pattern #2 + #11):

```json
{
  "order_id": "CF-2026-0001",
  "committente": "01-AGENCY | 02-INFO | 04-MKT | 05-MB-YT | 05-MB-KDP | cliente:<slug> | DE-interno",
  "brand_kit": "brands/<slug>/brand-kit.json",
  "icp": "brands/<slug>/icp.json",
  "formato": "carosello-ig | video-ugc | video-avatar | articolo | newsletter | thumbnail | grafica | publish-only",
  "quantita": 10,
  "deadline": "YYYY-MM-DD",
  "budget": {"crediti_engine": 120, "tier_max": "sonnet"},
  "note": "vincoli specifici, CTA richiesta, canali di destinazione"
}
```

Ordine incompleto → rifiuto con escalation al committente (mai improvvisazione).

### Handoff contract interno (tra team CF)

```json
{
  "from": "CF-R4/WF-CAROSELLO", "to": "CF-R5/WF-PUBLISH",
  "order_id": "CF-2026-0001",
  "payload": {"asset_dir": "orders/CF-2026-0001/06-delivery/", "manifest": "manifest.json"},
  "acceptance_criteria": ["3 gate verdi in state.json", "caption presente per ogni canale richiesto"],
  "on_reject": "torna a CF-R4 con motivo strutturato; 2 reject → escalation CF-A00"
}
```

### Matrice handoff inter-ecosistema (sintesi — dettaglio nel dossier §1)

| Ecosistema | Ordina a CF | Fornisce a CF |
|---|---|---|
| 01 AGENCY | contenuti per clienti, creative outreach, case study visuali | brand_kit + icp dei clienti, accessi account |
| 02 INFO-BUSINESS | asset lancio (caroselli, VSL, email-ready, grafiche) | calendario lancio, offerta, price point |
| 04 MARKETING | creative per ads, visual A/B test | **copy APSOC validato** (il copy che vende è SEMPRE di MKT) |
| 05 MULTI-BUSINESS | video YouTube, copertine/interni KDP, creative e-comm | brand_kit canale/libro, nicchia, formato |
| 06 PLATFORM | (raro) grafiche siti | render farm, fix Puppeteer/ffmpeg, hosting asset |
| 07 FORGE | — | nuove skill/agenti CF quando i KPI calano |
| 08 INTELLIGENCE | — | brief trend/hook/competitor; riceve log per la wiki |
| 09 OPERATIONS | — | runtime swarm, cron, storage, cost guard centrale |
| LX/L0 Board | contenuti corporate DE | Mandato Empire (gate non parametrici) |

---

## BRAIN (Memoria)

**Namespace AgentDB (convenzione `cf/...`):**

| Namespace | Contenuto |
|---|---|
| `cf/orders` | stato ordini (mirror di state.json a fine ordine) |
| `cf/brand-kits` | tenant registrati (slug, path, canali, soul_id) — namespace separati per brand contro il drift |
| `cf/patterns` | hook/formati che performano per brand (alimentato da WF-FEEDBACK a 48h/7gg) |
| `cf/failures` | ReasoningBank: errori gate distillati `{pezzo, gate, motivo}` |

**Fonte di verità operativa: il project state su disco** (eredità CF Exponium) — Ruflo
coordina, mai il contrario:

```
orders/<order_id>/
├── order.json        # il contratto
├── state.json        # fase corrente, gate superati, costi consumati
├── trace.jsonl       # ogni evento append-only {ts, agent, event, payload}
├── 01-brief/  02-copy/  03-design/  04-render/  05-qa/  06-delivery/
```

Fonte di verità umana: `second-brain-vault/wiki/` (pattern #12 wiki-first — ogni ordine
chiuso logga in `wiki/log.md`; il log lo scrive il conductor).

---

## COORDINATION (Ruflo)

**Topologia: `hierarchical` di default + `mesh` SOLO nei batch.**

- `swarm_init` **hierarchical**: CF-A00-conductor → 5 lead di reparto → worker.
- `swarm_init` **mesh** per i fan-out di mass-production (batch caroselli/video):
  N job indipendenti, pool di W worker paralleli — equivalente di
  `swarm.sh ugc batch.csv --parallel N --budget C`. Parallelismo default 4,
  cap dal campo `budget` dell'ordine.
- `agent_spawn` / `managed_agent_*` on-demand: i worker L5 esistono solo durante
  l'ordine (costo zero a riposo); coordinator persistenti solo durante i batch.
- Init: `ruflo memory init --namespace cf`.

**Hook concreti per ordine (pattern Dynamic Workflow):**

```
pre-order   → memory_search("cf/patterns", brand+formato)   # cosa ha funzionato per questo brand
pre-render  → estimate() Σ engine vs budget → block/allow    # budget guard, exit 2 se sfora
post-gate   → se rosso: memory_store("cf/failures", {pezzo, gate, motivo})
post-order  → memory_store("cf/orders", state finale) + entry wiki/log.md (conductor)
post-publish→ (a 48h/7gg) memory_store("cf/patterns", {brand, formato, hook, metriche})
```

**Fallback (ADR-005 CF, rischio daemon Windows):** se Ruflo non è disponibile, i workflow
girano in modalità pipeline sequenziale via script bash/python con lo stesso `state.json`.

---

## GOVERNANCE (Gate qualità)

- **3 gate sequenziali su OGNI deliverable**: GATE-FORMATO (oggettivo) → GATE-BRAND
  (parametrico sul brand_kit dell'ordine + Mandato Empire sempre attivo) → GATE-COPY-APSOC
  (cro-copy-architect, in handoff con la Copy Guild di 04-MKT). Un rosso ferma il pezzo, non il batch.
- **Dry-run default** (pattern #3): prima esecuzione di ogni workflow = stima costi, zero effetti.
- **Review umana obbligatoria** prima di ogni pubblicazione (vincolo Piano Maestro, fase iniziale).
- **Sicurezza**: `aidefence_scan/has_pii` su ogni contenuto in uscita (specie clienti agency).
- Verifica struttura: `scripts/verify-empire.sh` (F2 della roadmap globale).

## SENTINELS (always-on, istanze locali dei Sentinels di Backbone)

| Sentinel | Tier | Funzione |
|---|---|---|
| CF-SENT-cost | wasm | blocca ordini oltre budget PRIMA dello sforamento (exit 2); alert al Conductor; cost-attribution per agente in trace.jsonl |
| CF-SENT-brand | haiku | campiona output vs brand_kit (anti brand-drift multi-tenant) |

## IDENTITY-HR (Registro agenti)

31 agenti L5 (schede in `Agenti/`), censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`.
Routing modello 3-tier: WASM/regex → Haiku → Sonnet (Opus solo su richiesta esplicita per
QA finale o creative critiche). Nuove assunzioni/ritiri: via 07-FORGE → Chief-Forge → registro.

## OBSERVABILITY

- `trace.jsonl` per ordine = telemetria primaria (eventi append-only con costo per agente).
- Report batch aggregato a fine ordine: pezzi ok / rework / costo.
- La coda ordini è visibile al Board (precedenza `deadline → revenue → interno`);
  conflitti di pari priorità → hive-mind C-Suite, mai risolti localmente.

*Fonte: dossier 03 §1, §8 · Aggiornato: 2026-06-11*
