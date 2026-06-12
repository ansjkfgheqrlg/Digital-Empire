> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.1 (Reparti L2)

# IB-R1-PRODOTTO — Reparto Prodotto

> Reparto L2 · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

Trasformare materiale raw (registrazioni, PDF, manuali, transcript in `Formazzione/`)
in prodotti finiti e vendibili: ebook, corsi su piattaforma, guide, webinar.
**Nessun prodotto si crea senza validazione idea** (score ≥60/100 dal Product Idea Backlog,
definito in `Lancio corso skill beast/processo lancio.txt`).

---

## Workflow L3

| Workflow | Descrizione |
|---|---|
| `WF-CORSO` | Produzione corso end-to-end: raw → MKD → curriculum → lezioni → piattaforma Supabase |
| `WF-EBOOK` | Raw → MKD → ebook impaginato → sales asset (Manuale Claude Code 203pp è il prototipo) |
| `WF-VALIDAZIONE` | Idea → scoring 5 criteri /100 → test MVP 7 giorni → brief validato (gate d'ingresso) |

---

## Team L4 (Funzioni)

| Team | Responsabilità |
|---|---|
| `T-mkd` | Esegue content-forge: raw → Master Knowledge Document (100% atomi coperti) |
| `T-curriculum` | MKD → struttura moduli/lezioni con obiettivi di apprendimento misurabili |
| `T-piattaforma` | Caricamento su Supabase+Next.js (agenti `formazione-*` esistenti) |
| `T-design-prodotto` | Copertine, slide, workbook (handoff a CONTENT-FACTORY per i video) |

---

## Agenti L5 (roster)

`ib-prodotto-coordinator`, `ib-validator`, `ib-mkd-forger`, `ib-curriculum-architect`,
`ib-lesson-writer`, `formazione-orchestrator`, `formazione-database`, `formazione-admin`,
`formazione-student`, `formazione-design`

---

## KPI

| KPI | Definizione |
|---|---|
| Lead time corso | Giorni da brief validato → corso live su piattaforma |
| Tasso validazione | % idee che superano score ≥60 + MVP test |

---

## Quality Gate

**Gate qualità prodotto:** 100% atomi fonte coperti; ogni lezione ha outcome verificabile;
smoke test studente verde; brand voice conforme al Mandato Empire.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS]] sez. 2.1 + 4a (WF-CORSO)
- [[IB-R2-LANCI]] — destinatario del prodotto finito
- [[03-ECOSISTEMA-CONTENT-FACTORY]] — produce i moduli video su brief di questo reparto
- [[07-FORGE]] — nuove skill: `course-architect`
