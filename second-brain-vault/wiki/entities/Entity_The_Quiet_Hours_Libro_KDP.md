---
Type: ENTITY
Status: ✅ Completato — pacchetto pronto al caricamento
Tags: #kdp #libro #publishing #primo-prodotto
Created: 2026-08-23
Last updated: 2026-08-23
---

# "The Quiet Hours" — Primo Libro KDP Completo

## Overview
Primo libro mai completato dall'ecosistema Publishing di Digital Empire: 115
pagine reali (verificate sul PDF impaginato, non stimate) + copertina 1800×2700,
pacchetto pronto al caricamento su Amazon KDP. Prodotto con [[Tool_Pipeline_Libri_KDP]].

## Dettagli
- **Pagine reali**: 115 (contate su PDF impaginato con `conta_pagine_pdf()`, non
  stimate da conteggio parole — la stima precedente su un test aveva sbagliato per
  quasi 10 pagine: 115.5 dichiarate vs 106 reali sul PDF)
- **Copertina**: proporzioni e risoluzione corrette (1800×2700), adattamento
  automatico — bug precedente accettava copertine quadrate perché controllava solo
  il peso del file
- **Pacchetto**: PDF impaginato + copertina, completo (bug precedente: PDF a volte
  assente dal pacchetto finale, ora sempre incluso)
- **Non ancora fatto**: caricamento reale su Amazon KDP (fuori dallo scope della
  sessione che l'ha prodotto)

## Come Impatta DE
Prova che l'ecosistema Publishing (KDP) può produrre un libro reale e verificabile
end-to-end, non solo infrastruttura. Sblocca la ripetibilità: il prossimo libro
riusa la stessa pipeline senza dover ririsolvere gli stessi bug.

## Connessioni
- [[Tool_Pipeline_Libri_KDP]] — il motore che lo ha prodotto
- [[Entity_The_Ninth_Winter_Libro_KDP]] — secondo libro, stessa pipeline, correzione calibrazione 320 parole/pagina
- [[Entity_The_Second_Hand_Spellbook_Libro_KDP]] — terzo libro, stessa pipeline
- [[projects/Piano_Maestro_EMPIRE_OS]]

## Status
- First added: 2026-08-23 (backfill del buco wiki 06→22 agosto — il lavoro reale è del 2026-08-08, checkpoint CP-20260808-002)
- Confidence: Alta — pagine e copertina verificate con controlli reali, non dichiarazioni
