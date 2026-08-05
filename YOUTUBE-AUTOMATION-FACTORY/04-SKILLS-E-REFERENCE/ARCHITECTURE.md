# ARCHITECTURE — `youtube-automation-factory`

> Mappa navigabile dell'intera fabbrica. Costruita con **master-build-architecture** (topologia a 3
> livelli: Kernel + Specialisti + Tool; memoria dal passo zero; 7 sezioni canoniche per agente) e
> **content-forge 2.0** (MKD come base canonica, espansione mai riassunto).
> Chi entra qui (umano o LLM) si orienta in un colpo solo.

---

## Topologia (3 livelli, MBA)

```
L1 — KERNEL / CONDUCTOR
      SKILL.md + agents/conductor.md
      orchestrazione, stato del run, applicazione invarianti+gate
        │
        ├── L2 — SPECIALISTI (subagenti)
        │     operatori/   → chi OPERA (produce artefatti: script, specs, brief, metadati)
        │     controllo/   → chi CONTROLLA (gate + audit bloccanti)
        │     supporto/    → chi MANTIENE (memoria, auto-miglioramento)
        │
        └── L3 — TOOL DETERMINISTICI
              scripts/seo_score.py       (punteggio SEO ripetibile)
              scripts/cashcow_check.py   (euristica cash cow / views-ora)
              scripts/self_improve.py    (motore di auto-miglioramento)
              references/*               (conoscenza on-demand)
              memory/*                   (checkpoint, decisioni, log e regole)
```

**Perché operatori vs controllo separati:** chi produce non si auto-approva. Un gate (`niche-gate`,
`qa-audio-video`, `seo-gate`) è un agente diverso da chi ha costruito l'artefatto → controllo indipendente (MBA
invariante #6: failure-modes e verifica come first-class).

---



## Pipeline a 6 fasi + feedback

```
                 ┌──────────────────────────────────────────────────────────  ─┐
                 │                     FEEDBACK LOOP (Auto-miglioramento)      │
                 ▼                                                             │
[F1] SCOUTING ──► niche-scout ──► ⟨niche-gate⟩ ──► [F2] SELEZIONE VIDEO         │
                                                     video-hunter              │
                                                     seo-analyst               │
                                                     └─► DECISIONE A/B         │
                                                            │                  │
                                                            ▼                  │
[F3] SCRIPT ◄──────────────────────────────────── script-writer                │
   │                                                                           │
   ▼                                                                           │
[F4] PRODUZIONE ──► video-producer ──► ⟨qa-audio-video⟩ ──► ⟨niche-gate⟩        │
   │                                                                           │
   ▼                                                                           │
[F5] PUBBLICAZIONE ──► thumbnail-designer ──► metadata-optimizer ──► ⟨seo-gate⟩ ➔ PUBBLICA
   │                                                                           │
   ▼                                                                           │
[F6] AUDIT ──► performance-auditor ──► self-improver ──► diagnosi & regole ────┘
```

Gate `⟨...⟩` = bloccanti. Se rossi, il flusso torna all'operatore competente, non prosegue.
*Nota sulla mappatura:* Le 6 fasi della pipeline reale sono mappate su 5 file workflow in `workflows/` poiché la Fase 3 (Script) e la Fase 4 (Produzione) sono accorpate in `WF3-production.md` per coerenza di sviluppo.

---



## Gerarchia file

```
youtube-automation-factory/
├── SKILL.md                         # kernel: invocazione, invarianti, pipeline, roster, routing
├── ARCHITECTURE.md                  # questo file — mappa navigabile
├── MKD.md                           # Master Knowledge Document (metodo completo, espanso)
│
├── agents/                          # conductor + 13 agenti (ognuno = 1 file, 7 sezioni canoniche)
│   ├── conductor.md                 # L1 — orchestratore
│   ├── operatori/                   # chi OPERA
│   │   ├── niche-scout.md
│   │   ├── video-hunter.md
│   │   ├── seo-analyst.md
│   │   ├── script-writer.md
│   │   ├── video-producer.md
│   │   ├── thumbnail-designer.md
│   │   └── metadata-optimizer.md
│   ├── controllo/                   # chi CONTROLLA (gate + audit)
│   │   ├── niche-gate.md
│   │   ├── qa-audio-video.md
│   │   ├── seo-gate.md
│   │   └── performance-auditor.md
│   └── supporto/                    # chi MANTIENE
│       ├── memory-keeper.md
│       └── self-improver.md
│
├── workflows/                       # DAG eseguibili, uno per fase (dual formato MD + JSON)
│   ├── WF1-niche-discovery.md
│   ├── WF2-video-selection.md
│   ├── WF3-production.md
│   ├── WF4-publish-seo.md
│   └── WF5-performance-audit.md
│
├── references/                      # conoscenza on-demand (progressive disclosure)
│   ├── video-iq-analisi.md
│   ├── seo-certificazione.md
│   ├── teoria-script.md
│   ├── fliki-produzione.md
│   ├── fliki-avanzato.md
│   └── monetizzazione-compliance.md
│
├── scripts/                         # tool deterministici (L3)
│   ├── seo_score.py
│   ├── cashcow_check.py
│   └── self_improve.py
│
├── memory/                          # ecosistema memoria (dal passo zero)
│   ├── MEMORY-INDEX.md
│   ├── checkpoints/CP-000.md
│   ├── decisions/DEC-000.md
│   ├── performance_logs.json        # log storico delle metriche reali (input per auto-miglioramento)
│   └── learned_rules.json           # regole e blacklist apprese dal sistema (auto-migliorato)
│
└── evals/
    └── evals.md                     # criteri di accettazione della fabbrica
```

---



## Le 7 sezioni canoniche per agente (MBA invariante #5, forma compatta)

Ogni file agente contiene, in un unico documento navigabile:

1. **Spec** — id, ruolo, input, output, quando si attiva.
2. **System prompt** — istruzioni operative.
3. **Tools** — cosa usa (script, reference, Agent tool).
4. **Playbook** — passi concreti.
5. **Evals** — come si misura se ha fatto bene.
6. **Failure modes** — errore | sintomo | prevenzione | recupero.
7. **Memory** — cosa scrive in `memory/`.

> Scelta di design: 7 **sezioni** in 1 file invece di 7 file separati per agente. Motivo: la
> critica-guida di master-build-architecture è "niente stub, profondità reale e struttura visibile".
> Un file ricco per agente dà profondità + navigabilità senza generare decine di stub. Decisione
> tracciata in [memory/decisions/DEC-000.md](memory/decisions/DEC-000.md).

---



## Traceability

Ogni artefatto risale al [MKD.md](MKD.md): F1↔MKD §1-2, F2↔MKD §2, F3↔MKD §4, F4↔MKD §3,
F5↔MKD §2.4/§3.4, F6↔MKD §2.2/§5. Coverage degli atomi sorgente: 100% nel MKD.