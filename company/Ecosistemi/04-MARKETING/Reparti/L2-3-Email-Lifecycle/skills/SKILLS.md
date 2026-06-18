---
Type: SKILLS
Status: Active
Tags: #skills #email #lifecycle #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# Skills — L2.3 Email & Lifecycle

> Mappa delle skill proprie del reparto e delle skill esistenti mappate a L2.3.
> Skill proprie da forgiarsi via 07-FORGE (standard §8 piano V2): PRD + architettura + build.

---

## Skill propria L2.3 (da forgiarsi)

### `email-lifecycle-architect` — P2

**Priorità:** P2 (critica per l'autonomia del reparto — da forgiarsi nella fase V2-5)
**Scopo:** skill che guida la progettazione di una sequenza email lifecycle completa, dalla
scelta del tipo (lancio/nurture/onboarding/winback) all'architettura dei trigger e branch,
fino al contratto di richiesta copy per L2.1.
**Processo di forge:** PRD → architettura SPARC → build → test su caso reale → gate E-QA.
**Owner:** E1 (l'architettura della skill rispecchia il ragionamento di E1).
**Namespace output:** `marketing/email/sequences/{tipo}/{sequence_id}/`.

---

## Skill esistenti mappate a L2.3

| Skill | Fonte | Mappata a | Note operative |
|---|---|---|---|
| `emails` | esistente in `.claude/skills/` | L2.3 (standard compositivo) | Standard compositivo email con APSOC; usata da L2.1 WF-COPY-EMAIL su richiesta L2.3 |
| `cold-email` | esistente | L2.3 (QA standard) + 01-AGENCY (runtime) | L2.3 possiede lo standard; il runtime è in 01-AGENCY (ADR-003 — non toccare) |
| `churn-prevention` | esistente | L2.3 (E5 — asse win-back) | Skill principale per WF-EMAIL-WINBACK; E5 la usa per strutturare sequenze e CPB |
| `sms` | esistente | L2.3 (canale complementare) | Touchpoint SMS come complemento alle sequenze email (es. reminder last-call lancio) |
| `popups` | esistente | L2.3 (input lista) | Popups come touchpoint di acquisizione opt-in; L2.3 ne riceve l'output (lista) ma non li gestisce |

---

## Regole skill

1. Nessuna skill viene forgiata senza PRD approvato da EMAIL-LEAD e review MAXIMILIAN (standard V2 §8).
2. Le skill esistenti mappate NON si riscrivono senza ADR (wrap, non riscrittura — ADR-003).
3. La skill `cold-email` ha doppia ownership: L2.3 possiede lo standard qualitativo;
   01-AGENCY possiede il runtime. Qualsiasi modifica allo standard → coordinamento esplicito.

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.3 §5`
- [[e1-lifecycle-architect]] · `agenti/e1-lifecycle-architect.md` — owner della skill propria
- [[e5-winback-specialist]] · `agenti/e5-winback-specialist.md` — usa `churn-prevention`
