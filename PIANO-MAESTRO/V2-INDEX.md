# 🗺️ V2-INDEX — Mappa della costruzione a scala v2

> Punto unico da cui vedere lo stato dell'intera ricostruzione V2 (ADR-007, direttiva
> `11-PIANO-V2-DIRETTIVA-SCALA.md`). Aggiornato a ogni lotto. Principio Maximilian:
> **visibilità totale — niente conoscenza implicita, tutto navigabile.**
> Aggiornato: 2026-06-16.

---

## ⚠️ Verità da tenere a mente (principio Maximilian: standard chirurgico)

**Un dossier NON è una struttura.** I file qui sotto sono BLUEPRINT (markdown di progetto).
La direttiva §0 è esplicita: "vietato consegnare un ruolo in un markdown e chiamarlo agente".
Un dossier che descrive 76 agenti resta markdown finché V2-3+ non costruisce gli agenti veri
(con script, skill, state). **Non scambiare il progetto per l'edificio.** Colonna "Costruito?".

---

## Dossier di vertice (nuovi, V2-2)

| Dossier | Cosa | Blueprint | Costruito (fase) |
|---|---|---|---|
| `12-DOSSIER-MAXIMILIAN.md` | organo LX che incarna Max + review-gate 5-bis | ✅ | ⬜ V2-3 |
| `13-DOSSIER-MANDATO-ECOSISTEMA.md` | Mandato → ecosistema di governo | ✅ | ⬜ V2-5 |

## Dossier ecosistemi v2 (riscrittura 01-09)

| # | Dossier v2 | Reparti | Agenti | Workflow | Blueprint | Costruito |
|---|---|---|---|---|---|---|
| 01 | `01-ECOSISTEMA-AGENCY-V2.md` | 10 | ~75 | 25 | ✅ lotto 1 | ⬜ V2-6 |
| 04 | `04-ECOSISTEMA-MARKETING-V2.md` | 6 | ~49 | 22 | ✅ lotto 1 | ⬜ V2-6 |
| 03 | `03-ECOSISTEMA-CONTENT-FACTORY-V2.md` (mega) | 3 aree+8 | ~76 | 23 | ✅ lotto 2 | ⬜ V2-6 |
| 02 | `02-ECOSISTEMA-INFOBUSINESS-V2.md` (mega) | 5 aree | ~48 | 15 | ✅ lotto 2 | ⬜ V2-6 |
| 05 | `05-...-V2.md` | — | — | — | ⬜ lotto 3 | ⬜ V2-6 |
| 06 | `06-CORE` → **proposta split in 4** (vedi sotto) | — | — | — | ⬜ lotto 3-4 | ⬜ V2-6 |
| 07 | `07-...-V2.md` | — | — | — | ⬜ lotto 4 | ⬜ |
| 08 | `08-...-V2.md` | — | — | — | ⬜ lotto 4 | ⬜ |
| 09 | `09-...-V2.md` | — | — | — | ⬜ lotto 4 | ⬜ |

**Blueprint completati: 4/9 ecosistemi + 2 organi di vertice. Costruiti: 0.**
**Agenti progettati nei v2 finora: ~248. Censiti in `registro-agenti.yaml`: 19.** → gap da colmare.

## Proposta split 06-CORE (decisione per Max — default proposto)

Il v1 `06-ECOSISTEMI-CORE.md` impacchetta 4 ecosistemi perché in v1 erano "minori". A scala v2
("ogni cosa è un'azienda") il default proposto è **4 dossier v2 distinti**:
`06-PLATFORM-V2` · `07-FORGE-V2` · `08-INTELLIGENCE-V2` · `09-OPERATIONS-V2`
(con rinumerazione coerente da concordare). Razionale: Forge (crea agenti/skill) e Operations
(runtime/costi) sono critici e meritano dossier propri come gli altri ecosistemi.
**Max approva/cambia.** Finché non deciso, il lotto resta a slot pronto (ADR-005).

## Roadmap V2 (da `11-PIANO-V2` §10)

| Fase | Cosa | Stato |
|---|---|---|
| V2-0 | direttiva + ADR-007 + corpus | ✅ |
| V2-1 | F1-bis (base v1) | ✅ |
| V2-2 | dossier v2 (9 ecosistemi + MAXIMILIAN + MANDATO) | 🔄 4/9 + 2/2 organi |
| V2-3 | **build** organo MAXIMILIAN (attiva review-gate 5-bis) | ⬜ priorità alta |
| V2-4 | build Board v2 (7 figure ~70 agenti) | ⬜ |
| V2-5 | build Mandato-ecosistema + Sentinelle + Guilds v2 | ⬜ |
| V2-6 | build reparti v2 ecosistema per ecosistema (01→04→03→02→05) | ⬜ il grosso |
| V2-7 | knowledge ingestion (formazione → organi) | ⬜ |
| V2-8+ | riaggancio F5-F12: produzione reale | ⬜ traguardo operativo |

## Debiti aperti (anticipazione — cose che serviranno PRIMA di quanto sembri)

1. **Registro agenti disallineato:** ~248 agenti progettati, 19 censiti. Va riconciliato
   man mano (o a fine V2-2) — altrimenti il registro mente.
2. **Skill da forgiare non consolidate:** ogni dossier v2 ordina skill nuove alla FORGE
   (10+ per ecosistema). Serve un backlog unico "skill-to-forge V2" prima di V2-3.
3. **v1 vs v2 nell'Explorer:** i v1 restano come riferimento; a fine V2-2 decidere se
   archiviarli in `PIANO-MAESTRO/_v1-archivio/` per pulizia (Max: visibilità).

## Connessioni
- `11-PIANO-V2-DIRETTIVA-SCALA.md` (la direttiva) · `12`/`13` (organi di vertice)
- `company/Memory/STATO-EMPIRE.md` (stato corrente) · `company/Memory/INDEX.md` (checkpoint)
- `10-METODO-CICLO-FASE.md` (ciclo 9 passi + review 5-bis Maximilian)
