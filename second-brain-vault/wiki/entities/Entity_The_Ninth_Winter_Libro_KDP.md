---
Type: ENTITY
Status: ✅ PUBBLICABILE — copertina, PDF, copy pronti
Tags: #kdp #libro #publishing #secondo-prodotto
Created: 2026-08-24
Last updated: 2026-08-24
---

# "The Ninth Winter" — Secondo Libro KDP

## Overview
Secondo libro completato dall'ecosistema Publishing di Digital Empire con
[[Tool_Pipeline_Libri_KDP]] — 24/24 capitoli, **34.897 parole**, dentro il target. Prima
verifica end-to-end reale del modello "lo scrivo io" deciso il 2026-08-15 (Claude scrive in
sessione, il Python diventa attrezzatura di misura/impaginazione, mai un chiamatore di
modelli). Non su un caso ideale: un libro lasciato fermo dal 13 agosto a 8 capitoli su 24,
con un difetto di ritmo dentro.

## Dettagli
- **Genere/nicchia**: amish romance suspense (mediana recensioni 180, prezzo medio $5.95,
  6/16 concorrenti deboli — dati Amazon reali via `niche_finder.py`)
- **Il difetto trovato e corretto scrivendo il capitolo 9**: `riassunti.md` non era mai
  stato aggiornato dal capitolo 8 (solo un segnaposto) — ricostruiti rileggendo tutti gli 8
  capitoli esistenti, e la scaletta riallineata (due snodi di trama erano già avvenuti
  prima di dove l'outline li metteva).
- **Bug di calibrazione pagine scoperto qui** (2026-08-17): a 24/24 capitoli il libro era a
  34.347 parole, 153 sotto il minimo di 34.500 — invece di gonfiare, chiuso un arco narrativo
  rimasto davvero aperto (il personaggio Efrain). Risultato: 34.897 parole. La stessa
  richiesta "dammelo sempre in PDF" ha poi rivelato che la costante words-per-page era
  tarata a 300 invece delle 320 reali misurate su due libri veri impaginati — il libro era
  di fatto **111 pagine reali, sotto il minimo di 115** nonostante il conteggio parole
  sembrasse a posto. Corretto aggiungendo tre scene non-riempitive (consegna prove,
  chiusura di una sottotrama, restituzione ai truffati) fino a 115 pagine reali contate sul
  PDF.
- **Regola "niente lineette lunghe" applicata qui per la prima volta** (2026-08-18, regola
  di Gael: le lineette `—`/`–`/`--` sono la firma più riconoscibile della scrittura
  automatica): 193 righe riscritte a mano su entrambi i libri già pronti, distinguendo i
  trattini di parole composte inglesi (`twenty-nine`, da tenere) e le lineette nel discorso
  diretto per parole tagliate a metà (da tenere) dalle lineette narrative (da riscrivere).
  Togliere le lineette ha accorciato il libro sotto il minimo una seconda volta —
  richiuso con la scena di Emma Stoltzfus, un filo narrativo lasciato davvero aperto.
- **Scelta narrativa deliberata**: nessuno viene mai incriminato per la morte di Sarah — le
  prove non ci sono nella storia, e fabbricarle sarebbe stato disonesto verso la trama.

## Come Impatta DE
Prova che la pipeline KDP regge su un caso reale e imperfetto, non solo su un libro scritto
di fresco — e ha prodotto due correzioni di calibrazione (320 parole/pagina, regola
lineette) che si applicano a ogni libro successivo, incluso [[Entity_The_Second_Hand_Spellbook_Libro_KDP]].

## Connessioni
- [[Tool_Pipeline_Libri_KDP]] — il motore/metodo che lo ha prodotto
- [[Entity_The_Quiet_Hours_Libro_KDP]] — primo libro, stesso rapporto parole/pagina misurato
- [[Entity_The_Second_Hand_Spellbook_Libro_KDP]] — terzo libro, stessa pipeline

## Status
- First added: 2026-08-24 (backfill wiki storico 06→08/2026, permesso esplicito Max)
- Confidence: Alta — pagine, parole e regole verificate con controlli reali (conteggio su
  PDF impaginato, non stime), checkpoint CP-20260817-001, CP-20260817-002, CP-20260818-002
