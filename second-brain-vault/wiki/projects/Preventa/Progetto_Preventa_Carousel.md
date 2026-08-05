---
Type: PROJECT
Status: Active
Tags: #preventa #caroselli #arena #playwright #instagram #reparto-produzione
Created: 2026-08-03
Last updated: 2026-08-03
---

# Progetto Preventa — Caroselli Instagram

## Overview
Primo progetto creato sotto [[Reparto_Produzione_Digital_Empire]] (ordine di Max,
Fase 3 del piano [[CP-20260803-004]]). Genera caroselli Instagram promozionali per
Preventa riusando il motore ArenaAI (Playwright su Arena.ai) già costruito e
funzionante per il progetto Agency — non un motore nuovo, un progetto nuovo sullo
stesso motore.

## Perché non è un funnel di vendita
Preventa vende tramite outreach WhatsApp diretto ai concessionari (vedi
[[Preventa_Logica_Completa_Metodo]]), non tramite DM Instagram. Il template
Agency ha una CTA fissa "scrivimi X in DM per una call" — inadatta a Preventa.
Il copywriter Preventa (`Agents/copywriter_agent_preventa.py`) genera invece CTA
di brand awareness/social proof (segui/scopri di più), mai vendita diretta in
slide.

## Percorso
`SKILL & Agenti/Workflow agency creative/caroselli - preventa/`

## Contenuto reale (positioning, non inventato)
Preso da `Crea siti/Preventa/index.html` + `agency-empire/.../03b-preventa.tsx` +
[[Preventa_Logica_Completa_Metodo]]:
- Prodotto: incolli il link di un annuncio auto (anche estero) → PDF preventivo
  brandizzato con prezzi bloccati, pronto per WhatsApp.
- Prezzo: €2.000 una tantum, nessun canone.
- Target: concessionari import (stesso segnale di [[CP-20260803-005]] — filtro
  solo-import dell'outreach).
- Colori brand reali: `#101E3E` (blu fiducia/automotive) primario,
  `#FF4D00` (arancio) solo per CTA/accenti, mai oltre il 10% della slide.

## Come funziona tecnicamente (verificato leggendo il codice, non assunto)
`ArenaAI/arena_generator.py::generate_carousel_visuals()` **non riusa una chat
Arena salvata** — riapre `https://arena.ai/` da zero per ogni slide. La
continuità stilistica tra slide 1→2→3 viene dal ricaricare l'immagine appena
generata come allegato (pattern "Edit" descritto in `REGOLE.md` di Agency), non
da un URL di chat. Quello che isola davvero Preventa da Agency:
- `config_preventa.LOCAL_DOWNLOAD_DIR` → `caroselli - preventa/output_preventa/`
  (mai dentro la cartella Agency)
- `config_preventa.ALLEGATI_DIR` → cartella dedicata Preventa, **vuota al primo
  run** (nessun carosello Preventa esiste ancora — lo stile viene descritto a
  parole nel prompt; la slide 1 del primo run reale diventa reference per i
  successivi)

`orchestrator_preventa.py` sovrascrive questi due attributi sul modulo `config`
condiviso (quello di Agency, l'unico `config.py` sul path — Python lo tratta
come singleton) subito prima di chiamare `generate_carousel_visuals()`, così il
motore condiviso scrive dove deve senza che il suo codice venga toccato.

## Stato al 2026-08-03
- ✅ Scaffold completo: `config_preventa.py`, `Agents/copywriter_agent_preventa.py`,
  `orchestrator_preventa.py`, `REGOLE.md` — tutti `py_compile` puliti.
- ✅ Primo esempio di copy scritto a mano (stesso schema JSON del copywriter):
  `output_preventa/esempio-01-tempo-perso/carousel_plan.json` — 3 slide (hook
  tempo perso → soluzione PDF automatico → CTA brand).
- ❌ **Nessun visual ancora generato** — richiede il run live
  (`python orchestrator_preventa.py`), che apre un browser reale sull'account
  Arena di Max: non lanciato senza conferma esplicita (stesso principio già
  applicato per l'invio WhatsApp reale in questa stessa sessione).
- ❌ Cartella Agency (`caroselli - agency/`) non modificata — solo letta/importata,
  rispettando il suo `REGOLE.md` di confinamento.

## Connessioni
- [[Reparto_Produzione_Digital_Empire]] — il concetto organizzativo che questo progetto inaugura
- [[Preventa_Logica_Completa_Metodo]] — il prodotto/sistema outreach che questi caroselli promuovono
- [[CP-20260803-005]] — filtro solo-import (stesso target audience)
