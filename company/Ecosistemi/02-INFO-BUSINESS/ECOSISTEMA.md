# 📚 02 — INFO-BUSINESS

> **Livello:** L1 · **Priorità:** ALTA · **Stato:** ATTIVO (lanci episodici)
> Dossier completo: `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md`

## Missione

Produrre e vendere prodotti informativi (corsi, ebook, community) che portano
clienti a Digital Empire e generano revenue scalabile. Ogni prodotto è sia un
asset educativo che un funnel di ingresso per i servizi agency.

## Catalogo prodotti

| Prodotto | Prezzo | Ruolo | Stato |
|---|---|---|---|
| Manuale Claude Code | ❓ DA DECIDERE | corso / lead magnet? | BLOCCANTE (B1) |
| Vendi la Skill (Skill Beast) | da definire | corso | in sviluppo |
| Ebook | vari | lead magnet / vendita | episodico |

> ⚠️ **Blocco critico:** Manuale Claude Code ha prezzo "NON LO SO" e doppio ruolo
> contraddittorio (gratuito vs pagamento). Risoluzione obbligatoria prima di fase B1.

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Prodotto | curriculum, contenuti, piattaforma (Supabase) | `Reparti/Prodotto/` |
| L2.2 | Lanci | T-30→T+7, dry-run, go/no-go, sequenze | `Reparti/Lanci/` |
| L2.3 | Vendite/Funnel | sales page, checkout, evergreen funnel | `Reparti/Vendite-Funnel/` |
| L2.4 | Community&Retention | post-acquisto, engagement, upsell | `Reparti/Community-Retention/` |

## Workflow principali

- `WF-CORSO` — raw → content-forge MKD → curriculum → piattaforma Supabase
- `WF-LANCIO` — T-30 → T+7 con dry-run e go/no-go hive-mind
- `WF-FUNNEL-EVERGREEN` — always-on: ads → landing → checkout → sequenza email

## Come si collega al Backbone

- **BUS:** riceve upsell lead da AGENCY; invia copy brief a MARKETING; richiede contenuti a CONTENT-FACTORY
- **BRAIN:** namespace `infobusiness/*` — stato lancio, metriche funnel
- **GOVERNANCE:** gate lancio (validazione idea ≥60/100, APSOC copy ≥80/100)

## Asset esistenti

- `Formazzione/` — materiale corsi esistente (da mappare in F3)
- `Lancio corso skill beast/` — materiale lancio (da mappare in F3)
- `Lanco ebook/` — workflow ebook (da mappare in F3)
- `InfoBusiness/` — risorse generali

*Fonte: `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md` · Aggiornato: 2026-06-11*
