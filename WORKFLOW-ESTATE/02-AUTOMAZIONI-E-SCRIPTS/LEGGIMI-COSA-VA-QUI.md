# 🧠 02-AUTOMAZIONI-E-SCRIPTS — cosa va qui, cosa NO

> Deciso da Max il 2026-07-27. Regola dell'architettura del Workflow Estate.

## Il Workflow Estate è CERVELLO, non muscolo

Questo workflow **decide, orchestra, misura, ricorda**. Non manda email, non scrapa lead,
non renderizza video. Dice *cosa* va fatto e *verifica* che sia fatto bene.

## ✅ Cosa VA in questa cartella
Script **di supporto alla decisione e alla memoria**:
- `memory_manager.py` — gestione della memoria del workflow
- eventuali script di misura, telemetria, controllo gate, checkpoint

## ❌ Cosa NON va qui
Script **operativi** — quelli che agiscono verso l'esterno. Vivono nei workflow operativi:

| Script operativo | Va in |
|---|---|
| invio email / WhatsApp / outreach | `Outreach/Outreach Workflow/` |
| scraping lead | `Outreach/preventa-maps-scraper/` |
| rendering / test API video (Fliki) | `YOUTUBE-AUTOMATION-FACTORY/` |
| bot NFT/memecoin | `company/Ecosistemi/12-STREAM-S7-BOT/` |

## Spostati il 2026-07-27 (opzione A di Max)
Erano qui per comodità, ma sono operativi. Riportati al loro posto (con storia git preservata):
- `send_s1_whatsapp_auto.py` → `Outreach/Outreach Workflow/`
- `prepare_outreach_emails.py` → `Outreach/Outreach Workflow/`
- `send_outreach_ready.py` → `Outreach/Outreach Workflow/`
- `fliki_youtube_test.py` → `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/`

## Le 11 sottocartelle (i sensori)
`decisions · errors · performances · reasoning-bank · sessions` si riempiono da sole quando
si lavora (`empire trace`). `architectures · brainstorms · checkpoints · feedback · metrics · plans`
raccolgono gli artefatti decisionali. **Sono cervello: qui la traccia del pensiero, non l'azione.**
