---
Type: TOOL
Status: Active
Tags: #kdp #libri #publishing #pipeline #arena #niche-finder
Created: 2026-08-23
Last updated: 2026-08-23
---

# Tool: Pipeline Produzione Libri KDP

## Overview
Motore reale (non simulato) che porta un libro da idea a pacchetto KDP pronto al
caricamento: ricerca nicchia → capitoli scritti in sessione → assemblaggio →
copertina → conteggio pagine verificato sul PDF impaginato. Nato dal fallimento
del vecchio "PIANO KDP 67" (LM Arena bloccato dai captcha sul testo lungo) — il
pezzo mancante non era un generatore automatico di testo, ma il ponte tra
capitoli scritti a mano in sessione e un motore di assemblaggio reale.

## Dettagli

**Percorso**: `engine/book_project.py` (un progetto = una cartella, capitoli come
file) + `SOP-SCRIVERE-UN-LIBRO.md` (7 step) + `niche_finder.py` (ricerca nicchie
Amazon reali: recensioni mediane, concorrenti deboli, prezzo medio, punteggio
motivato).

**Perché non usa LM Arena per il testo**: il captcha di Arena non è aggirabile
oltre il primo messaggio — un libro ne richiede 24+. Le copertine invece restano
su LM Arena (funzionano, nessun blocco lì). Il testo si scrive con Claude in
sessione diretta.

**3 bug reali dello stesso tipo trovati sul primo libro** (numeri dichiarati mai
verificati): copertina quadrata accettata perché si controllava solo il peso del
file (fix: proporzioni + risoluzione + adattamento automatico a 1800×2700); pagine
STIMATE (parole/300) invece che contate — dichiarava 115.5 pagine, il PDF reale ne
aveva 106 (fix: `conta_pagine_pdf()` sul PDF impaginato, quello che impagina KDP,
non una stima); PDF assente dal pacchetto finale (aggiunto).

**Sbloccato da**: cambio di approccio chiesto da Gael — "crea i flussi, dei SOP,
dividi in step" invece di inseguire l'automazione end-to-end del testo.

## Primo output reale
[[Entity_The_Quiet_Hours_Libro_KDP]] — primo libro completato con questa pipeline,
115 pagine reali verificate + copertina, pacchetto pronto al caricamento
(2026-08-08).

## Come Impatta DE
Sblocca l'ecosistema Publishing (KDP) come revenue stream ripetibile: ogni nuovo
libro riusa la stessa pipeline (cartella progetto → capitoli → assemblaggio →
copertina → verifica pagine reali), non si riparte da zero.

## Connessioni
- [[Entity_The_Quiet_Hours_Libro_KDP]]
- [[projects/Piano_Maestro_EMPIRE_OS]]
- [[Reparto_Produzione_Digital_Empire]]

## Status
- First added: 2026-08-23 (backfill del buco wiki 06→22 agosto, lavoro reale del 2026-08-05/08)
- Confidence: Alta — verificato con esecuzione reale, checkpoint CP-20260805-001, CP-20260806-004, CP-20260808-002
