---
Type: WORKFLOW
Status: Active
Tags: #workflow #infobusiness #ebook #mkd #impaginazione #pdf #epub #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# WF-EBOOK — Ebook Pronto Vendita / Lead Magnet

> **ID:** WF-IB-PROD-003 · **Owner:** `IB-COORD-PRODOTTO` + `IB-PROD-EBOOK`
> **Reparto:** IB-L2-PROD Produzione Prodotti
> **Trigger:** brief validato (WF-VALIDAZIONE PASS) + cartella/file raw

---

## Scopo

Trasformare materiale raw in un ebook impaginato pronto alla vendita o come lead magnet. La pipeline
trasforma raw → MKD (100% atomi) → struttura capitoli (1 CTA + 1 esercizio per capitolo) → testo →
impaginazione PDF/ePub + copertina → storage sicuro con link protetto. Il Manuale Claude Code
(203 pagine esistente) è il prototipo validato di questo workflow.

**Regola fondamentale:** nessuno step avanza senza gate QA verde di IB-PROD-QA. Nessun ebook esce
con placeholder o link rotto (R6); ogni claim ha prova (R7).

**Nota vincolo reale:** il routing del Manuale Claude Code (lead magnet gratuito vs prodotto a
pagamento) è ANCORA INDECISO → B-002 BACKLOG; la decisione spetta al team-prezzi (B-003, ADR-005).
Il workflow è pronto end-to-end ma lo Step 5 (checkout vs download gratuito) attende quella decisione.

---

## Attori

| Step | Agente IB-L2-PROD | Agente/Reparto esterno |
|---|---|---|
| MKD | `IB-PROD-MKD` | skill `content-forge` (motore raw → MKD) |
| Gate atomi | `IB-PROD-QA` | — |
| Struttura capitoli | `IB-PROD-EBOOK` | skill `book-to-skill` (PDF lunghi) |
| Gate CTA+esercizio | `IB-PROD-QA` | — |
| Testo capitoli | `IB-PROD-WRITER` | — (voce DE, Mandato Empire) |
| Gate prove non promesse | `IB-PROD-QA` | — |
| Impaginazione + copertina | `IB-PROD-DESIGN` | skill `printing-press` (PDF/ePub) |
| Gate leggibilità | `IB-PROD-QA` | — |
| Storage + link protetto | `IB-PROD-PLATFORM` | PLATFORM (storage + checkout se a pagamento) |
| Pattern di ciclo | `IB-PROD-LEARN` | — |

---

## Flusso passo-passo

```
[TRIGGER]
WF-VALIDAZIONE PASS → brief validato + cartella/file raw
         │
         ▼
[STEP 1] IB-PROD-MKD — content-forge → MKD (stesse regole WF-CORSO)
  → content_forge_runner.py [WRAPPA] produce MKD + atomi-check.json
  → GATE QA-1 (atomi): copertura = 100% atomi fonte; rapporto espansione ≥1?
    PASS → prosegui; FAIL → IB-PROD-MKD recupera atomi mancanti (R2)
         │
         ▼
[STEP 2] IB-PROD-EBOOK — struttura capitoli
  → introduzione, sezioni, conclusione, call-to-action; mappa capitoli da MKD
  → GATE QA-2 (CTA+esercizio): ogni capitolo ha 1 CTA chiara + 1 esercizio pratico?
    PASS → prosegui; FAIL → capitoli senza esercizio riprogettati
         │
         ▼
[STEP 3] IB-PROD-WRITER — testo capitolo per capitolo
  → voce DE; zero contenuto generico
  → GATE QA-3 (prove non promesse): ogni claim ha prova/motivazione (Mandato Art.2)?
    PASS → prosegui; FAIL → capitolo riscritto sulle sezioni non conformi (R7)
         │
         ▼
[STEP 4] IB-PROD-DESIGN — impaginazione PDF/ePub + copertina
  → printing-press: export PDF + ePub; copertina professionale
  → GATE QA-4 (leggibilità): leggibile su mobile + link funzionanti + zero placeholder?
    PASS → prosegui; FAIL → impaginazione corretta (R6)
         │
         ▼
[STEP 5] IB-PROD-PLATFORM — storage + accesso
  → carica ebook su storage sicuro; link con accesso protetto
  → routing: a pagamento → checkout attivo | lead magnet gratuito → pagina download libera
    [VINCOLO: routing Manuale Claude Code attende decisione team-prezzi — B-002 BACKLOG]
  → GATE-5 (accesso): link protetto risolve correttamente; download integro?
         │
         ▼
[STEP 6] HANDOFF → IB-L2-VEND
  → file ebook (PDF+ePub) + pagina download + asset lancio
  → ebook in stato_finale: "pronto"
         │
         ▼
[STEP 7] IB-PROD-LEARN — pattern di ciclo
  → quale formato/capitolo converte, difetti ricorrenti di impaginazione
  → infobusiness/prod/reasoning/pattern-{YYYYMMDD}.md
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| QA-1 — Atomi 100% | MKD copre il 100% atomi fonte; rapporto espansione ≥1 | IB-PROD-QA | Struttura capitoli |
| QA-2 — CTA + esercizio | 1 CTA + 1 esercizio pratico per capitolo | IB-PROD-QA | Scrittura testo |
| QA-3 — Prove non promesse | Ogni claim con prova/motivazione | IB-PROD-QA | Impaginazione |
| QA-4 — Leggibilità | Leggibile mobile + link ok + zero placeholder | IB-PROD-QA | Storage + consegna |
| G5 — Accesso | Link protetto risolve; download integro | IB-PROD-PLATFORM | Consegna IB-L2-VEND |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trigger": "WF-VALIDAZIONE PASS",
  "prodotto_id": "EBOOK-001",
  "titolo": "Manuale Claude Code",
  "raw_folder": "Formazzione/Manuale Claude Code/",
  "brief_validato": true,
  "formato_target": ["pdf", "epub"]
}
```

**Output finale:**
```json
{
  "prodotto_id": "EBOOK-001",
  "export": {"pdf": true, "epub": true, "pagina_download": true},
  "link_protetto": "https://piattaforma/download/manuale-claude-code",
  "routing_free_paid": "indeciso (B-002 BACKLOG, attende team-prezzi B-003)",
  "gate_qa_tutti": "PASS",
  "stato_finale": "pronto",
  "handoff": "IB-L2-VEND",
  "namespace": "infobusiness/prod/ebook/state.json"
}
```

---

## State

File: `infobusiness/prod/ebook/state.json`
- Creato all'avvio del workflow su brief validato.
- `fase_corrente` aggiornato ad ogni step; `gate_qa` traccia ogni gate (PASS/FAIL).
- `routing_free_paid` resta "indeciso" finché team-prezzi non chiude B-002/B-003 (ADR-005).
- `stato_finale: "pronto"` solo con tutti i gate QA a PASS (R4/R6).

---

## Connessioni

- [[ib-prod-ebook]] · `agenti/ib-prod-ebook.md` — owner della pipeline ebook
- [[ib-prod-design]] · `agenti/ib-prod-design.md` — impaginazione PDF/ePub + copertina (Step 4)
- [[ib-prod-qa]] · `agenti/ib-prod-qa.md` — presidia i 4 gate QA bloccanti
- [[WF-VALIDAZIONE]] · `workflow/WF-VALIDAZIONE.md` — trigger del workflow (brief validato)
- [[WF-CORSO]] · `workflow/WF-CORSO.md` — pipeline gemella per formato corso
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-PROD WF-EBOOK`
