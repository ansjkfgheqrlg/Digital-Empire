---
name: UI Dark-On-Dark Fix
description: Correzione UI per eliminare componenti dark-on-dark nella piattaforma Formazione Empire
type: CONCEPT
---

# UI Dark-On-Dark Fix

## Overview
Correzione mirata a rimuovere le violazioni di design *dark‑on‑dark* individuate durante l'audit UI del progetto **Formazione Empire**. Sono state apportate due modifiche principali:

1. **LessonDrawer** – sostituzione del background scuro `#0f0f0f` con la classe utility `card-fill-silver`, garantendo contrasto adeguato su sfondo scuro.
2. **VideoPlayer** – aggiunta di `background: '#0a0a0a'` al wrapper dell'iframe YouTube per evitare il flash bianco durante il caricamento.

## Dettagli tecnici
- Il wrapper del drawer ora utilizza `className="card-fill-silver"` mantenendo bordi e shadow originali.
- Il componente `VideoPlayer` aggiunge `style={{ background: '#0a0a0a' }}` al `div` relativo al `iframe`.
- Entrambe le modifiche rispettano la **Regola UI NON NEGOZIABILE**: nessuna `.card-dark` su sfondo scuro; uso obbligatorio di `.card-fill-silver` o `.card-fill-silver-orange`.

## Connessioni
- [[Formazione_Empire_Stato_UI]] – stato UI aggiornato con queste correzioni.
- [[Concept_Dark_On_Dark_Audit]] – audit originale che ha identificato i problemi.

## Why
Garantire leggibilità e coerenza visuale su tutti i componenti UI, evitando problemi di accessibilità e rispettando le linee guida di design premium di Digital Empire.
