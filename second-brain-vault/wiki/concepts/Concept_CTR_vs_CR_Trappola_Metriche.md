---
Type: CONCEPT
Status: Active
Tags: #metriche #email #analytics #ctr #cr #quality-gate
Created: 2026-08-23
Last updated: 2026-08-23
---

# Concept: CTR vs CR — la Trappola di Lettura delle Metriche

## Overview
Due metriche diverse, spesso confuse, che descrivono lo stesso evento (un click) con basi di calcolo diverse — leggerle come intercambiabili porta a decisioni sbagliate. Generalizzabile oltre l'email a qualsiasi funnel con più stadi (sent → opened/seen → clicked).

## Le due metriche

- **CR (Click Rate)** = click / TOTALE inviati (o totale mostrati, nel caso di un ads/post)
- **CTR (Click-Through Rate)** = click / TOTALE aperti (o visualizzati)

Esempio: 100 email inviate → 10 aperture (Open Rate 10%) → 2 click → **CR = 2%**, **CTR = 20%**. Stesso numero assoluto di click, percentuali che differiscono di un ordine di grandezza a seconda della base scelta.

## Il secondo errore: click totali vs click per-destinazione

Anche dentro la CTR corretta, un numero alto può essere fuorviante se il contenuto ha più di un link cliccabile: un link secondario/distrattivo (social, video esterno) può assorbire la maggior parte dei click mentre il CTA che conta davvero (es. la landing page) resta sotto-performante. Serve sempre il breakdown per singolo link/pulsante, non solo il click totale.

## Come si applica

- Prima di commentare "abbiamo un ottimo CTR/CR", verificare quale delle due basi si sta usando e non confrontarla con un benchmark pensato per l'altra.
- Quando un contenuto ha più CTA, guardare SEMPRE il breakdown per link prima di dichiarare vittoria su un numero aggregato.
- Vale per email, ma anche per ads (impression→click vs reach→click), post social, notifiche push: stesso principio, nomi diversi a seconda della piattaforma.

## Perché conta

Un CTR alto scambiato per CR (o viceversa) porta a sovrastimare o sottostimare la reale efficacia di un canale — e un CTA "vincente" sulla carta può in realtà performare male se il click aggregato nasconde un link secondario che sta rubando l'attenzione al vero obiettivo.

## Connessioni

- [[Source_Andrei_Pascu_10_Strategie_Email_Copywriting]] — fonte originale (definizioni + esempio numerico + caveat click-per-link)
- [[Concept_Hook_Anti_Cliche_Checklist]] — altro gate di qualità pre-decisione dallo stesso run, applicato all'hook invece che alle metriche
