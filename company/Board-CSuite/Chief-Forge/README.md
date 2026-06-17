# Chief-Forge — Architettura della Figura

> **Livello:** L0 — Board C-Suite
> **Namespace AgentDB:** `board/chief-forge`
> **Tier conductor:** Opus
> **Blueprint vincolante:** `company/Board-CSuite/_BLUEPRINT/BP-Chief-Forge.md`
> **Base v1:** `company/Board-CSuite/Chief-Forge.md`
> **Versione:** 2.0 CF-grade · Creato: 2026-06-17

---

## Missione

Chief-Forge è la **fabbrica organizzativa della holding**. Siede in C-Suite e governa
la crescita strutturale di EMPIRE OS: smista richieste di nuova capability, presidia il
portfolio skill/agenti, mantiene il registro Identity-HR, garantisce gli eval gate, e
autorizza mandati per interi ecosistemi nuovi. È il committente di alto livello del
Genesi Core (ARCHITETTURA → FORGE): nessun artefatto organizzativo nasce senza
passare per Chief-Forge.

**In una frase:** *"Ogni agente che assumiamo e ogni skill che forgiamo deve risolvere
un problema reale — non riempire uno schema."*

---

## Forma: cartella-workflow CF-grade (pesante)

Chief-Forge NON è un singolo file. È una struttura navigabile con:
- **10 agenti** in `agenti/` — roster completo con schede millimetriche
- **3 workflow CF-grade** in `workflow/` — pipeline operative con gate
- **Principi, regole, skill, scripts, KPI, state** — livelli di governance separati

Questa forma riflette la complessità del mandato: Chief-Forge governa L'INTERA
crescita organizzativa della holding, non un singolo reparto.

---

## Posizione nella gerarchia

```
MANDATO (leggi/regole)
  └─ MAXIMILIAN (standard e visione)
       └─ BOARD C-SUITE
             ├─ CEO — direzione strategica
             ├─ CFO — risorse e budget
             └─ CHIEF-FORGE ← qui (fabbrica organizzativa)
                  ├─ ARCHITETTURA (blueprint per-artefatto)
                  └─ FORGE (build artefatti)
```

Chief-Forge è il ponte tra il Board e il Genesi Core (ARCHITETTURA + FORGE).
Non costruisce artefatti in prima persona: commissiona, valuta, approva, registra.

---

## I 10 agenti del roster (overview)

| Agente | Ruolo | Tier |
|---|---|---|
| `cf-conductor` | Coordina la crescita organizzativa, riporta al CEO | Opus |
| `cf-architettura-liaison` | Contatto con ARCHITETTURA (blueprint) | Sonnet |
| `cf-forge-liaison` | Contatto con FORGE (build artefatti) | Sonnet |
| `cf-intake-router` | Cattura e smista richieste capability | Sonnet |
| `cf-skill-portfolio` | Catalogo skill, gap e duplicati | Haiku |
| `cf-agent-registry` | Registro Identity-HR (100% agenti) | Haiku |
| `cf-eval-warden` | Gate eval prima del rilascio | Sonnet |
| `cf-ecosystem-builder` | Mandato ecosistemi nuovi | Opus |
| `cf-contradiction-warden` | Skill-contradiction-analyzer sui rilasci | Sonnet |
| `cf-memoria` | Storico forgiature, eval, pattern organizzativi | Haiku |

Schede millimetriche in `agenti/` — ogni scheda ≥25 righe, I/O JSON, logica passo-passo.

---

## I 3 workflow CF-grade (overview)

| Workflow | Scopo |
|---|---|
| `WF-CAPABILITY-INTAKE` | Richiesta gap → spec → blueprint → build → eval → registro |
| `WF-ECOSYSTEM-MANDATE` | Board chiede ecosistema → ARCHITETTURA disegna → FORGE costruisce |
| `WF-HR-REGISTRY` | Censimento/aggiornamento Identity-HR, ritiro agenti obsoleti |

Flussi completi in `workflow/`.

---

## Handoff principali

| Direzione | Controparte | Payload |
|---|---|---|
| ← input | Tutti gli ecosistemi | richieste capability `{eco, gap, KPI, budget}` |
| → commissiona | ARCHITETTURA | `{tipo, scopo, vincoli}` → blueprint |
| → commissiona | FORGE | blueprint approvato → build |
| ↑ riporta | CEO | mandati ecosistemi nuovi, budget straordinari |
| ↑ riporta | CFO | costo nuovi agenti, piano budget forgiatura |

---

## KPI presidiati

- Tempo richiesta → artefatto consegnato (da misurare)
- Eval score nuove skill: target ≥85% pass
- Copertura Identity-HR: target 100%
- Skill orfane/duplicate: target 0

---

## Connessioni

- [[BP-Chief-Forge]] — blueprint sorgente
- [[Chief-Forge.md]] — v1 base
- [[14-DOSSIER-ARCHITETTURA]] — organo ARCHITETTURA (controparte)
- [[company/Ecosistemi/07-FORGE/ECOSISTEMA.md]] — organo FORGE (controparte)
- [[12-DOSSIER-MAXIMILIAN]] — standard CF-grade di riferimento
