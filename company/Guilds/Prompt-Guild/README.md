# 💬 Prompt Guild — Guild

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 4.2
> **Expertise:** prompt engineering, system prompt design, prompt review, chain-of-thought, anti-pattern
> **Serve:** tutti gli ecosistemi — ogni agente L5 ha un system prompt revisionabile dalla Guild
> **Sponsor C-level:** CTO (empire-cto)
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/Brain/README.md]]

---

## Identità

| Campo | Valore |
|---|---|
| **Guild Master** | `prompt-guild-master` (L5 coordinator, namespace AgentDB: `patterns/prompt/`) |
| **Tipo** | Guild trasversale — expertise su richiesta, non gerarchia verticale |
| **Deliverable principale** | Prompt Library nel Brain (`patterns/prompt/`) |
| **Ingaggio** | Passivo (memory_search sul namespace) o attivo (richiesta via gbus) |

---

## Cosa standardizza

La Prompt Guild definisce e mantiene gli standard per tutti i prompt della holding:

1. **Struttura obbligatoria di ogni system prompt** (invariante):
   - `Identità`: chi è l'agente, ruolo, a chi risponde
   - `Responsabilità`: lista ordinata di cosa fa
   - `Input / Output`: schema JSON o formato atteso
   - `Acceptance criteria`: quando l'output è accettabile (misurabili, non generici)
   - `Failure handling`: cosa fare se l'input è malformato o il task non è eseguibile
   - `Esempi`: almeno 1 esempio positivo e 1 negativo

2. **Context engineering**: come strutturare il context window per massimizzare la qualità dell'output senza sprecare token (pattern #7 progressive disclosure: kernel ≤500 righe, dettaglio in `references/`).

3. **Template per tipo di task DE** — prompt ottimizzati per i task ricorrenti:
   - Classificazione/tagging (Tier 1 Haiku)
   - Copy APSOC (Tier 2 Sonnet, si coordina con Copy/APSOC Guild)
   - Architettura e ADR (Tier 3 Opus)
   - QA checklist (Tier 1 Haiku)
   - Ricerca e sintesi (Tier 2 Sonnet)

4. **Anti-pattern da evitare**:
   - Prompt senza acceptance criteria → output non valutabile
   - Context overloading (tutto nel system prompt → degrada la qualità)
   - Roleplay aperto senza boundaries → drift comportamentale
   - Zero-shot su task complessi → usa few-shot o chain-of-thought

5. **Chaining**: template per chain-of-thought multi-step e per handoff tra agenti in pipeline.

---

## Deliverable

- **Prompt Library** — `company/runtime/brain/patterns/prompt/` (namespace AgentDB `patterns/prompt/`)
- **Template repository** — template per tipo di task, versionati e benchmark-testati
- **Anti-pattern register** — lista degli anti-pattern rilevati dagli ecosistemi, con fix
- **Benchmark results** — quality score prima/dopo revisione prompt (misurato via gate verify)

---

## Come si richiede supporto alla Guild

```json
{
  "from": "<ecosistema_richiedente>",
  "to": "Prompt-Guild",
  "tipo": "guild_request",
  "sottotipo": "prompt_review | template_request | anti_pattern_report | chain_design",
  "brief": "agente X produce output Y — il prompt attuale è allegato",
  "prompt_attuale": "...",
  "problema_rilevato": "output troppo lungo / acceptance criteria mancanti / ...",
  "formato_atteso": "prompt revisionato con changelog",
  "deadline": "YYYY-MM-DD"
}
```

**Flusso tipico:**
1. Ecosistema nota un agente con bassa pass-rate gate
2. Manda guild_request alla Prompt Guild con prompt attuale e score del gate
3. Guild Master assegna un prompt engineer
4. Revisione → nuovo prompt + note diff + benchmark
5. Risultato consegnato via gbus; aggiornamento in Prompt Library

---

## Funzionamento interno

- **Raccolta pattern**: dagli ecosistemi via ReasoningBank (`patterns/incidents/` di ogni tipo) → la Guild analizza i prompt associati ai fallimenti più frequenti
- **Validazione su benchmark**: ogni template nuovo viene testato su 10 casi reali before/after
- **Pubblicazione nel Brain**: namespace `patterns/prompt/` — consultabile dagli agenti via `memory_search`
- **Notifica via Bus**: quando un template viene aggiornato o un anti-pattern classificato → notifica agli ecosistemi impattati

---

## KPI

| Metrica | Target |
|---|---|
| Agenti L5 con system prompt conforme allo standard | 100% (obiettivo F3) |
| Template disponibili per tipo di task principale | ≥ 10 (obiettivo F3) |
| Pass-rate gate dopo revisione prompt Guild | miglioramento ≥ 10 punti |
| Anti-pattern classificati e documentati | tracking attivo |
| Latenza risposta guild_request | < 24h per P1, < 4h per P0 |

---

## Stato

Struttura creata (F1). Agenti L5 da assegnare in F3 (migrazione asset + registro Identity-HR).
Guild Master attivo in consultazione manuale (F1-F3): richiedi revisione prompt nelle sessioni Claude Code.
