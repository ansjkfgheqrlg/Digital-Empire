# PreventivoForge

Workflow multi-agente: **annuncio mobile.de (DE) → preventivo italiano (PDF)**, prezzo finale
nel titolo, **multi-concessionaria**. Cliente: Prof Autocad.

## Setup (una volta)
```bash
cd "Clienti/Prof Autocad/preventivo-forge"
python -m venv .venv && . .venv/Scripts/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env                                   # poi compila .env
```

## Uso
```bash
python run.py "https://suchen.mobile.de/auto-inserat/.../456259857.html"
python run.py "<url>" --dealer prof-autocad
python run.py --list-dealers
# fallback senza scraping (se mobile.de blocca):
python run.py --manual annuncio.html --foto ./foto --dealer prof-autocad
```
Output in `runs/<id>/`: `listing.json`, `listing_it.json`, (con Half B) `preventivo_*.pdf`.

## Stato
- **Half A (Max):** scraping (S1), parsing (S2), pricing (S4), regia `run.py`, multi-tenant. ✅ runnable & testato.
- **Half B (Gael):** traduzione+copy (S3), PDF (S5), gate QA. → `HANDOFF-GAEL.md`.

## Documenti
- Architettura/SPEC: `00-ARCHITETTURA-WORKFLOW.md`
- Brain (RBI): `CLAUDE.md`
- Contratto dati: `schema/listing.schema.json`, `schema/listing_it.schema.json`
- Handoff Gael: `HANDOFF-GAEL.md`

## Nuova concessionaria
Crea `concessionarie/<id>/config.json` (copia da `prof-autocad`), imposta prezzo/logo/contatti,
poi `python run.py "<url>" --dealer <id>`.
