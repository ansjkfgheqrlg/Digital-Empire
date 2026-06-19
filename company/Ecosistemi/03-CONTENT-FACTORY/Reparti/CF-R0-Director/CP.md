---
Type: CHECKPOINT
Status: Closed
Tags: #checkpoint #content-factory #cf-r0 #director #step5 #V2-6
Created: 2026-06-19
Last updated: 2026-06-19
---

# CP-20260619-008 — STEP 5: 03-CONTENT-FACTORY CF-R0 Director

> **ID checkpoint:** CP-20260619-008
> **Fase:** STEP 5 — 03-CONTENT-FACTORY CF-R0 Director (reparto leader ecosistema)
> **Eseguito da:** Gael
> **Data:** 2026-06-19
> **Riferimento Memory:** `company/Memory/checkpoints/` (da copiare lì per sync)

---

## Cosa è stato fatto

Build completa della cartella `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R0-Director/`
con standard CF-grade (ADR-007). Il CF-R0 è il livello 0 della gerarchia MEGA-REPARTO
di CF-DE: ingresso unico ordini, validazione contratto multi-tenant, smistamento alle 3 aree.

---

## File creati (14 file, 0 stub)

| File | Tipo | Righe stimate |
|---|---|---|
| `README.md` | Missione + roster + contratto ordine + KPI + escalation | >100 |
| `ARCHITETTURA.md` | Gerarchia 5 livelli MEGA-REPARTO + regola coda + multi-tenant | >100 |
| `agenti/cf-d-lead.md` | Agente opus — leader ecosistema | >150 |
| `agenti/cf-d-qa.md` | Agente sonnet — gate BLOCCANTE ordini | >150 |
| `agenti/cf-d-dispatch.md` | Agente sonnet — creazione struttura e dispatch | >150 |
| `agenti/cf-d-sched.md` | Agente sonnet — capacity planning e batch merging | >150 |
| `agenti/cf-d-budget.md` | Agente haiku — budget sentinel e alert soglia | >130 |
| `agenti/cf-d-status.md` | Agente haiku — dashboard e alert milestone | >130 |
| `agenti/cf-d-learn.md` | Agente sonnet — pattern aggregator e trigger 07-FORGE | >150 |
| `workflow/WF-ORDER-INTAKE.md` | Workflow CF-grade intake + gate BLOCCANTE | >150 |
| `workflow/WF-DIRECTOR-REVIEW.md` | Workflow CF-grade review settimanale + escalation Board | >150 |
| `principi/PRINCIPI.md` | 6 principi operativi CF-R0 | >60 |
| `scripts/README.md` | Wrapper skill cf-order + 2 script target deterministici | >80 |
| `kpi/KPI.md` | KPI globali CF-R0 con [DM] per baseline mancanti | >100 |
| `state/README.md` | Namespace cf/orders + cf/kpi + schemi 4 file + regole integrità | >120 |
| `CP.md` | Questo checkpoint | — |

**Totale: 16 file (incluso questo CP.md)**

---

## Conformità alle regole

- ADR-003: RISPETTATO — skill `cf-order` esistente si WRAPPA, non si riscrive.
  Nessun file v1 in `company/Ecosistemi/03-CONTENT-FACTORY/` è stato toccato.
- ADR-007 (CF-grade): RISPETTATO — ogni scheda agente ha: frontmatter, Identità + "Cosa NON fa",
  Responsabilità numerate, Input/Output JSON con esempio, "Come ragiona (passo-passo)",
  KPI (tabella), Escalation, Esempio operativo, Connessioni [[...]].
- Mandato Art.2 (no metriche inventate): RISPETTATO — tutti i target numerici sono [DM].
- Pattern 11 (brand_kit+icp obbligatori): RISPETTATO — gate BLOCCANTE in WF-ORDER-INTAKE
  e principio P2 nei PRINCIPI.
- Zero stub: CONFERMATO — nessun "TODO", "PLACEHOLDER", "FIXME", "da compilare" nel
  contenuto. I path degli script target sono marcati "campo popolato a runtime".
- Ogni file linka 2-3 pagine [[...]]: CONFERMATO — tutte le sezioni Connessioni completate.
- NON modificati: `STATO-EMPIRE.md`, `INDEX.md`, file v1 dell'ecosistema 03.

---

## Cosa NON è stato fatto (in scope V2-6 successivo)

- Le 3 aree (Pre-Produzione, Produzione, Post-Produzione) e i loro 8 reparti L2 (CF-R1...CF-R8)
  non sono ancora costruiti: verranno nei batch successivi di STEP 5.
- I 4 brand_kit del registry CF-R2 non sono ancora onboardati: task di CF-R2.
- I workflow chiave (WF-CAROSELLO, WF-VIDEO, WF-PUBLISH) non sono ancora costruiti: task CF-R3/R4/R5.
- Gli script `order-validator.py` e `capacity-planner.py` sono target deterministici: verranno
  scritti quando il runtime sarà pronto (fase V2-6 esecuzione).

---

## Ripresa da

Prossimo task STEP 5: costruire uno dei reparti L2 delle 3 aree operative (CF-R1 Strategia & Brief
è il più urgente — nessun ordine può entrare in produzione senza brief). Leggere
`PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §3 CF-R1` prima di iniziare.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §3`
- [[README]] · `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R0-Director/README.md`
- [[ARCHITETTURA]] · `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R0-Director/ARCHITETTURA.md`
