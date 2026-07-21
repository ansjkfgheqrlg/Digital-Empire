# 🚦 STATO SITUAZIONE — 2026-06-30

> File-cruscotto. Lo leggono **Max e Gael** per sapere cosa succede ORA.
> Fonte di verità dettagliata: `company/Memory/STATO-EMPIRE.md` (blocco 🛑 in cima).

## ⏸️ DECISIONE: Digital Empire IN PAUSA
Stop temporaneo alla costruzione dell'impero (ecosistemi 01-AGENCY, 05, 06-CORE, ecc.).
**Priorità unica ORA = primo cliente ufficiale: Prof Autocad.** Si riprende l'impero dopo.

- **Gael:** NON scegliere l'ecosistema, NON costruire l'impero. → vai a Half B (sotto).
- **Max:** completa Half A (agenti CF-grade + regole) quando riprende.

---

## 🎯 IL LAVORO: PreventivoForge (cliente Prof Autocad)
Workflow: **annuncio mobile.de (tedesco) → PREVENTIVO italiano (PDF)**, copy migliorato,
**prezzo finale nel titolo** (`esposto ×1.03 +1500 +1500`), **multi-concessionaria**.
Cartella: `Clienti/Prof Autocad/preventivo-forge/`. Riferimento formato: `Clienti/Prof Autocad/Preventivo BMW Z4 2003 FR 3.0i.pdf` ✅ (già presente).

### Split 50/50
| Metà | Chi | Cosa | Stato |
|---|---|---|---|
| **Half A** | **Max** | scraper S1, parser S2, pricer S4, regia `run.py`, multi-tenant, schema, skill `/preventivo-auto` | ✅ **FATTO + testato** (18.000→21.540) |
| **Half B** | **Gael** | traduzione+copy S3, PDF preventivo S5, 4 agenti QA + gate, template, regole R3/R5/R6 | ⬜ **DA FARE — inizia ora** |

Cucitura congelata tra le due metà: `preventivo-forge/schema/listing.schema.json`.

---

## ▶️ GAEL — INIZIA QUI (Half B)
```
1. git pull --rebase                      # ricevi il codice di Max
2. apri:  Clienti/Prof Autocad/preventivo-forge/HANDOFF-GAEL.md   # spec completa
3. costruisci (in ordine):
   - implementation/translate_copy.py   (S3)  -> firma: translate(ctx, dealer)
   - implementation/render_pdf.py + templates/preventivo.html  (S5) -> render(ctx, dealer) -> Path
   - implementation/qa_gate.py          (gate B/C/D)
   - agenti CF-grade (7 file): op-translator-copy, op-pdf-renderer, 4x qa-*
   - rules/R3-translation-copy.md, R5-pdf-render.md, R6-qa-gate.md
4. NON toccare Half A (scraper/parser/pricer/run.py) né schema/listing.schema.json (CONGELATO)
5. Test:  python run.py "<url-mobile.de>"   deve produrre  preventivo_*.pdf  con gate verdi
6. Chiudi: CP in company/Memory/checkpoints/ + aggiorna STATO-EMPIRE + push
```
Skill motore consigliate: `content-forge`, `copywriting`, `cro-copy-architect`, `verification-quality`.

---

## ▶️ MAX — riprende qui (completa Half A)
Agenti CF-grade 7-file (conductor, op-scraper, op-parser, op-pricer) + `agents/CATALOG.md`
+ regole R1/R2/R4 + `orchestration/`. Poi: dati dealer (logo/contatti) in `concessionarie/prof-autocad/config.json`.

---

## ⚠️ NOTE
- **Sync/git:** lo Stop-hook di auto-sync NON stava committando/pushando → il coordinamento era saltato.
  Ora si committa/pusha A MANO finché non si sistema l'hook. **Max: dopo il commit → `git push origin main`.**
- **Scraping mobile.de:** anti-bot forte. Path automatico Playwright + fallback `--manual` pronti;
  il test live va fatto nell'ambiente del cliente.

---

## 📅 CHECKPOINT - 2026-07-21 (YouTube Automation)
- **Gael:** Creato asset `KB_06_youtube_automation_vidiq_fliki.md` in YouTube Lead Engine, strutturando i raw log sulle logiche di YouTube Automation, VidIQ e Fliki. Inserito in `STATO-SITUAZIONE` come previsto dal Ciclo di Fase (passo 7).

## 📅 CHECKPOINT - 2026-07-21 (YouTube Automation Engine Architettura)
- **Gael:** Creato l'ecosistema `YouTube-Automation-Engine` applicando le skill `master-build-architecture` (per l'albero di directory e memorie) e `content-forge2.0` (per trasformare KB_06 in flussi di lavoro `flow.md`). Creati 3 workflow: VidIQ SEO, Scripting, Fliki. Aggiornato INDEX di memoria interno.
- **Gael:** Creato il team di agenti (`vidiq-seo-analyst`, `script-engineer`, `fliki-operator`) con file canonici (spec + system_prompt) sotto `YouTube-Automation-Engine/agents/`. Piena implementazione dei Modelli Mentali di Content Forge.
- **Gael:** Aggiunto il target project `Dose-Mentale-Remake` nell'engine. Creati gli agenti di Ingestion e Publishing, chiudendo il loop end-to-end (dal canale target al canale proprietario clonato) includendo le contromisure anti-copyright.
