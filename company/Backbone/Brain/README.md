# 🧠 BRAIN — Memoria a 3 strati

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 1.2
> **Backbone component.** Il cervello aziendale: una sola verità, tre rappresentazioni —
> leggibile dagli umani, ricercabile semanticamente dagli agenti, distillata in pattern dagli errori.
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/README.md]]

---

## Architettura a 3 strati

| Strato | Per chi | Tecnologia | Dove | Stato |
|---|---|---|---|---|
| **1. Wiki** (fonte di verità) | Umani + Claude in sessione | Markdown Obsidian, regola wiki-first | `second-brain-vault/wiki/` | ✅ ATTIVO |
| **2. AgentDB** (indice semantico) | Agenti running | Ruflo `memory_store/search`, HNSW 384-dim | namespace per ecosistema (sotto) | da init F2 |
| **3. ReasoningBank** (errori→pattern) | Loop auto-miglioramento | `reasoningbank-*`: trajectory→verdict→distill | namespace `patterns/` | da costruire F8 |

**Regola fondamentale:** conflitto wiki ↔ AgentDB → **vince la wiki** (fonte di verità umana); AgentDB si reindicizza.

---

## Namespace AgentDB per ecosistema

Ogni `BACKBONE.md` di ecosistema dichiara i namespace che usa. Namespace master:

| Namespace | Contenuto | Ecosistema owner |
|---|---|---|
| `agency/` | lead, clienti, preventivi, contratti, status delivery | 01-AGENCY |
| `infobusiness/` | lanci, offerte, prezzi, community, email funnel | 02-INFO-BUSINESS |
| `contentfactory/` | hook vincenti, format, batch completati | 03-CONTENT-FACTORY |
| `marketing/` | copy APSOC validati, angle, swipe file, score gate | 04-MARKETING |
| `multibusiness/` | KDP (titoli, keyword, revenue), YT (canali, script), ecomm | 05-MULTI-BUSINESS |
| `platform/` | decisioni tecniche, ADR tecnici, architetture | 06-PLATFORM |
| `forge/` | template agenti/skill, eval results, MKD documenti | 07-FORGE |
| `intelligence/` | ricerche, trend, abstract ingestiti, fonti | 08-INTELLIGENCE |
| `operations/` | run completati, costi, scheduling, swarm history | 09-OPERATIONS |
| `memory/` | indice semantico checkpoint/ADR/piani (ecosistema 10) | 10-MEMORY |
| `identity/` | agenti, ruoli, performance, stato (mirror HR) | Backbone/Identity-HR |
| `decisions/board/` | decisioni Board, voti hive-mind, rationale | Board/C-Suite |
| `patterns/` | ReasoningBank distillato, prompt library, rubriche | Guilds / trasversale |
| `mandato/` | Articoli Mandato, brand gate G2, APSOC rules | LX / Sentinels |

---

## Inizializzazione AgentDB (F2, task 2.4)

```bash
# In company/ (dopo ruflo init)
claude-flow memory store -k "init" --value "empire-os" --namespace agency
claude-flow memory store -k "init" --value "empire-os" --namespace infobusiness
claude-flow memory store -k "init" --value "empire-os" --namespace contentfactory
claude-flow memory store -k "init" --value "empire-os" --namespace marketing
claude-flow memory store -k "init" --value "empire-os" --namespace multibusiness
claude-flow memory store -k "init" --value "empire-os" --namespace platform
claude-flow memory store -k "init" --value "empire-os" --namespace forge
claude-flow memory store -k "init" --value "empire-os" --namespace intelligence
claude-flow memory store -k "init" --value "empire-os" --namespace operations
claude-flow memory store -k "init" --value "empire-os" --namespace memory
# Trasversali
claude-flow memory store -k "init" --value "empire-os" --namespace identity
claude-flow memory store -k "init" --value "empire-os" --namespace patterns
```

Fallback senza daemon: mirror locale `company/runtime/brain/<ns>.jsonl` + `brain.sh recall` (grep sul mirror).

---

## Wiki Bridge e Regole di Sincronizzazione

Eseguite dal wiki-syncer di Memory Empire (skill `wiki-sync-guard`, da forgiare P0):

1. Ogni pagina wiki nuova/modificata → `memory_store` dell'abstract + path nel namespace giusto (la wiki resta il contenuto integrale; AgentDB indicizza, non duplica).
2. Ogni pattern distillato dal ReasoningBank con ≥3 conferme → promosso a pagina wiki in `concepts/` o `synthesis/`.
3. Ogni operazione rilevante → entry obbligatoria in `wiki/log.md` (Pattern #12 wiki-first). Lag vigilato dal Drift-Sentinel (KPI: < 24h).
4. Conflitto wiki vs AgentDB → vince la wiki; AgentDB si reindicizza automaticamente.

---

## ReasoningBank (da costruire F8)

Schema trajectory:
```json
{
  "task": "email outreach per vertical X",
  "ecosistema": "AGENCY",
  "agente": "AGY-ACQ-email-writer-01",
  "output_attempt": "...",
  "gate_result": "rejected",
  "nota_correttiva": "P troppo generico — mancava dato verticale specifico",
  "fix_applicato": "aggiunto dato '60% degli ecommerce perde lead nel checkout'",
  "outcome_post_fix": "passed",
  "pattern": "P deve contenere dato numerico specifico al verticale"
}
```

Quando un pattern raggiunge ≥3 conferme → distillato in pagina wiki `concepts/` e prompt standard della Prompt Guild.

---

## KPI

| Metrica | Target |
|---|---|
| Lag sync wiki ↔ AgentDB | < 24h (vigilato da Drift Sentinel) |
| Pattern distillati promossi a wiki per mese | ≥ 4 (obiettivo F8) |
| Namespace inizializzati | 12/12 (obiettivo F2) |
| memory_search risponde correttamente | 100% (dopo init) |

---

## Stato

- Wiki `second-brain-vault/wiki/` — ✅ ATTIVO
- `company/Memory/` — ✅ ATTIVO (ecosistema 10)
- AgentDB namespace — ⏳ da inizializzare (F2, task 2.4)
- ReasoningBank — ⏳ da costruire (F8)
- wiki-syncer automatico — ⏳ da forgiare skill `wiki-sync-guard` (P0)
