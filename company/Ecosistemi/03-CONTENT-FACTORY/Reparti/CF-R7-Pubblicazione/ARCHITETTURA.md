---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #pubblicazione #CF-R7 #publish #pipeline #orchestratori
Created: 2026-06-23
Last updated: 2026-06-23
---

# ARCHITETTURA — CF-R7 Pubblicazione & Distribuzione

> **Reparto:** CF-R7 · **Area:** Post-Produzione · **Orchestra:** CF-R7-COORD riporta a L1-POST
> **[WRAPPA] orchestratori Python ATTIVI — runtime NON modificato (ADR-003)**
> **Gate manuale obbligatorio:** nessuna pubblicazione senza review umana (policy Board)

---

## 1. Posizione nella gerarchia CF-DE

```
CF-DIRECTOR (L0)
  └── L1-POST (Capo Area Post-Produzione)
        ├── CF-R6 — QA & Gate (gate indipendente su ogni asset)
        ├── CF-R7 — PUBBLICAZIONE & DISTRIBUZIONE  ← questo reparto
        └── CF-R8 — Apprendimento & Ottimizzazione
```

CF-R7-COORD riceve dalla coda WF-CALENDAR (CF-R1) gli slot assegnati e da CF-R6 gli asset
con gate verdi. Ogni pubblicazione è preceduta obbligatoriamente da CF-R7-QA (check pre-publish:
gate verdi + review umana + token validi). Nessun asset entra in questo reparto senza aver
superato CF-R6.

---

## 2. Orchestratori Python wrappati (ADR-003)

CF-R7 wrappa senza modificare i motori di pubblicazione esistenti:

| Motore | Path | Canali | Stato | Wrapper |
|---|---|---|---|---|
| `main_orchestrator.py` | `SKILL & Agenti/Workflow pubblicazione automatica/` | IG, TikTok, LinkedIn, Drive | ATTIVO | `scripts/wrap-main-orchestrator.sh` [WRAPPA] |
| `mentalita_orchestrator.py` | `SKILL & Agenti/Workflow pubblicazione automatica/` | IG (brand Mentalità Brutale) | ATTIVO | `scripts/wrap-mentalita-orchestrator.sh` [WRAPPA] |

**Regola ADR-003 SUPREMA:** i file Python sopra non si modificano, non si riscrivono, non si
toccano durante il runtime. Ogni file CF-R7 che li utilizza dichiara esplicitamente:
`[WRAPPA] orchestratore Python — runtime non modificato`.

Il wrapper espone al reparto le operazioni:
- `publish(ordine, canale, asset_path, caption)` → pubblica via orchestratore
- `check_token(canale, brand_slug)` → verifica validità token; se scaduto → blocco + alert
- `dry_run_plan(ordine)` → produce piano di pubblicazione senza toccare canali (zero effetti)

Token scaduti = BLOCCO immediato. CF-R7-COORD avvisa committente e attende rinnovo.

---

## 3. Gate pre-publish (invariant assoluto)

Prima di ogni pubblicazione CF-R7-QA verifica **tre condizioni**. Tutte e tre devono essere verdi:

```
1. GATE VERDI in state.json
   └── orders/<id>/state.json → "05-qa": { "gate_formato": "PASS", "gate_brand": "PASS",
                                            "gate_copy": "PASS", "gate_mandato": "PASS" }
       Se manca anche un solo gate verde → BLOCCO. Non si pubblica.

2. REVIEW UMANA ESEGUITA
   └── orders/<id>/state.json → "review_umana": { "eseguita": true, "ts": "...", "nome": "..." }
       Se review_umana.eseguita != true → BLOCCO. Il gate manuale è policy Board non bypassabile.

3. TOKEN CANALE VALIDI
   └── check_token(canale, brand_slug) → OK
       Se token scaduto → BLOCCO + alert CF-R7-COORD + notifica committente.
```

Qualsiasi condizione non soddisfatta → FAIL strutturato con motivo; CF-R7-COORD riceve l'alert.

---

## 4. Topologia pipeline (sequenza obbligatoria)

```
[Asset con gate verdi CF-R6]
         │
         ▼
  [CF-R7-QA] ← pre-publish check (gate verdi + review umana + token)
         │ FAIL → BLOCCO + alert
         │ PASS
         ▼
  [CF-R7-ADAPT] ← adattamento per canale (caption, hashtag, aspect)
         │
         ▼
  [REVIEW UMANA] ← gate manuale obbligatorio (non bypassabile)
         │ NO → asset in attesa; non si avanza
         │ SI (documentata in state.json)
         ▼
  ┌──────────────────────────────────┐
  │  CF-R7-PUBLISH (IG/TK/LinkedIn)  │  oppure  │  CF-R7-YT (YouTube)  │  oppure  │  CF-R7-DELIVER (non-social)  │
  └──────────────────────────────────┘
         │
         ▼
  [CF-R7-CHECK] ← verifica live post/URL
         │
         ▼
  [log trace.jsonl + url definitivo in state.json]
         │
         ▼
  [CF-R7-FEEDBACK] ← 48h + 7gg metriche → cf/patterns + handoff MARKETING
```

La sequenza è non bypassabile: ogni passo dipende da quello precedente.
Il dry-run di WF-PUBLISH-SOCIAL produce un piano di pubblicazione (cosa/dove/quando/caption)
senza toccare alcun canale.

---

## 5. Ciclo di vita di un ordine in CF-R7 (state machine)

```json
{
  "order_id": "CF-2026-0088",
  "workflow": "WF-PUBLISH-SOCIAL",
  "fasi": {
    "00-pre-check": { "stato": "completato", "gate_verdi": true, "review_umana": true, "token_ok": true },
    "01-adapt":     { "stato": "completato", "canali": ["instagram", "linkedin"], "caption_adattata": true },
    "02-review-umana": { "stato": "completato", "eseguita": true, "ts": "2026-06-23T09:00:00Z", "nome": "Gael" },
    "03-publish": {
      "instagram":  { "stato": "pubblicato", "ts": "2026-06-23T09:05:00Z", "url": "https://www.instagram.com/p/..." },
      "linkedin":   { "stato": "pubblicato", "ts": "2026-06-23T09:06:00Z", "url": "https://www.linkedin.com/posts/..." }
    },
    "04-check": { "stato": "completato", "instagram": "URL_ATTIVO", "linkedin": "URL_ATTIVO" },
    "05-feedback-48h": { "stato": "in_attesa", "ts_previsto": "2026-06-25T09:05:00Z" }
  },
  "publish": [
    { "canale": "instagram", "esito": "PUBBLICATO", "url": "https://www.instagram.com/p/...", "ts": "2026-06-23T09:05:00Z" },
    { "canale": "linkedin",  "esito": "PUBBLICATO", "url": "https://www.linkedin.com/posts/...", "ts": "2026-06-23T09:06:00Z" }
  ]
}
```

---

## 6. Namespace AgentDB

```
cf/publish/<order_id>/<canale>  → { esito, url, ts, n_check }
cf/delivery/<order_id>          → { manifest_path, checksum, conferma_ts, conferma_da }
```

**Schema trace.jsonl (ogni riga append-only):**
```json
{"ts":"2026-06-23T09:05:00Z","agent":"cf-r7-publish","event":"publish_done","canale":"instagram","url":"https://www.instagram.com/p/...","orchestratore":"mentalita_orchestrator.py"}
{"ts":"2026-06-23T09:06:00Z","agent":"cf-r7-check","event":"check_ok","canale":"instagram","url_attivo":true}
```

---

## 7. Dry-run WF-PUBLISH-SOCIAL

Il dry-run produce un piano di pubblicazione senza toccare i canali:

```json
{
  "order_id": "CF-2026-0088",
  "dry_run": true,
  "brand": "mentalita-brutale",
  "piano_pubblicazione": [
    { "canale": "instagram", "asset": "orders/.../04-render/carousel-001/", "caption": "...", "orario": "2026-06-23T09:00:00Z", "orchestratore": "mentalita_orchestrator.py" },
    { "canale": "linkedin",  "asset": "orders/.../04-render/carousel-001/", "caption": "...", "orario": "2026-06-23T09:05:00Z", "orchestratore": "main_orchestrator.py" }
  ],
  "pre_check": { "gate_verdi": true, "review_umana_presente": true, "token_ig": "VALIDO", "token_li": "VALIDO" },
  "decisione": "PRONTO — in attesa review umana prima di eseguire"
}
```

Zero effetti reali. Serve per review umana: il committente o il socio legge il piano e approva.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R7`
- [[CF-R7-Pubblicazione/README]] · `README.md` — roster e handoff
- [[CF-R6-QA-Gate]] · fornitore asset con gate verdi; precedente obbligatorio
- [[principi/PRINCIPI]] · `principi/PRINCIPI.md` — regole non negoziabili del reparto
