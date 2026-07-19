# 🗺️ V2-INDEX — Mappa della costruzione a scala v2

> Punto unico da cui vedere lo stato dell'intera ricostruzione V2 (ADR-007, direttiva
> `11-PIANO-V2-DIRETTIVA-SCALA.md`). Aggiornato a ogni lotto. Principio Maximilian:
> **visibilità totale — niente conoscenza implicita, tutto navigabile.**
> Aggiornato: 2026-07-19 (Gael, CP-20260719-001 — lotto 3 chiuso).

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
| 05 | `05-ECOSISTEMA-MULTIBUSINESS-V2.md` | 12 | ~72 | — | ✅ lotto 3 | ⬜ V2-6 |
| 06a | `06a-ECOSISTEMA-PLATFORM-V2.md` | 5 | ~45 | 16 | ✅ lotto 3 | ⬜ V2-6 |
| 06b | `06b-ECOSISTEMA-FORGE-V2.md` | 5 | ~40 | 15 | ✅ lotto 3 | ⬜ V2-6 |
| 06c | `06c-ECOSISTEMA-INTELLIGENCE-V2.md` | 5 | ~35 | 20 | ✅ lotto 3 | ⬜ V2-6 |
| 06d | `06d-ECOSISTEMA-OPERATIONS-V2.md` | 5 | ~37 | 17 | ✅ lotto 3 | ⬜ V2-6 |
| 07 | `07-...-V2.md` (BACKBONE-RUFLO-SKILLS) | — | — | — | ⬜ lotto 4 | ⬜ |
| 08 | `08-...-V2.md` (ROADMAP-FASI) | — | — | — | ⬜ lotto 4 | ⬜ |
| 09 | `09-...-V2.md` (ECOSISTEMA-MEMORY) | — | — | — | ⬜ lotto 4 | ⬜ |

**Blueprint completati: 8/9 ecosistemi (01,02,03,04,05,06a,06b,06c,06d — nota: 06 conta come 4
ecosistemi separati dopo lo split) + 2 organi di vertice. Costruiti: 0.**
**Agenti progettati nei v2 finora: ~477 (248 lotto 1-2 + 229 lotto 3: 72+45+40+35+37).
Censiti in `registro-agenti.yaml`: 19.** → gap da colmare, resta in BACKLOG (ADR-005).

## Split 06-CORE — ESEGUITO (CP-20260719-001, Gael)

Il v1 `06-ECOSISTEMI-CORE.md` impacchettava 4 ecosistemi perché in v1 erano "minori". A scala
v2 ("ogni cosa è un'azienda") sono stati splittati in **4 dossier v2 distinti**:
`06a-ECOSISTEMA-PLATFORM-V2.md` · `06b-ECOSISTEMA-FORGE-V2.md` ·
`06c-ECOSISTEMA-INTELLIGENCE-V2.md` · `06d-ECOSISTEMA-OPERATIONS-V2.md`.
**Naming `06a/06b/06c/06d` (non rinumerato 06/07/08/09)** per evitare collisione con i file già
esistenti `07-BACKBONE-RUFLO-SKILLS.md`, `08-ROADMAP-FASI.md`, `09-ECOSISTEMA-MEMORY.md` (che
restano con la loro numerazione, sono dossier trasversali diversi, non ecosistemi core). Il v1
`06-ECOSISTEMI-CORE.md` resta intatto come riferimento (ADR-003) — non archiviato, non toccato.

## Roadmap V2 (da `11-PIANO-V2` §10)

| Fase | Cosa | Stato |
|---|---|---|
| V2-0 | direttiva + ADR-007 + corpus | ✅ |
| V2-1 | F1-bis (base v1) | ✅ |
| V2-2 | dossier v2 (9 ecosistemi + MAXIMILIAN + MANDATO) | 🔄 8/9 (lotto 3 chiuso) + 2/2 organi — resta lotto 4 (07/08/09) |
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
