---
Type: PROJECT
Status: Active
Tags: #saas #app #mobile #ai #funnel #marketmind #vibecoding
Created: 2026-05-02
Last updated: 2026-05-02
---

# MarketMind — App AI Funnel Builder Vocale

## Overview
App mobile (Android) + web che genera funnel di marketing completi tramite chat vocale guidata in 3 fasi. Formula core: **Più contesto = Funnel migliore**. Differenziatore: trasparenza radicale + "prompt di emergenza" che consiglia anche altri tool AI.

## Dettagli

### Problema Risolto
I marketer AI-native perdono ore a costruire funnel perché danno troppo poco contesto all'AI → risultati generici. MarketMind guida vocalmente l'utente a fornire contesto massimo strutturato.

### Target
Marketer digitali / digital entrepreneur, 24-38 anni, alto livello di consapevolezza AI, usano Claude/ChatGPT ogni giorno, budget €10-20/mese per tool.

### Core Feature: La Chiamata in 3 Fasi
1. **Fase 1 — Contesto**: AI raccoglie business, prodotto, avatar, competitor, pricing, obiezioni
2. **Fase 2 — Architettura**: AI propone struttura funnel, utente conferma/modifica
3. **Fase 3 — Formazione**: AI raccoglie dati finali, poi Claude API genera funnel completo

### Monetizzazione
- Crediti settimanali per piano
- Base €5/mese | Pro €10/mese | Empire €15/mese | Agency custom
- Early adopter (primi 100): settimana 1 gratis + 20% sconto forever

### Tech Stack
- Mobile: Expo (React Native) + TypeScript
- Web: Next.js 14 + Tailwind
- Backend: Supabase (Auth + DB + Edge Functions)
- Voice: Vapi SDK (Web Call mode)
- AI: Claude API (claude-sonnet-4-6)
- Payments: Stripe (web) + RevenueCat (mobile)
- Analytics: PostHog

### Status PRD
**Score**: 87/100 — Pronto per sviluppo
**PRD file**: `/MarketMind/docs/PRD.md`
**Fasi**: 4 fasi, ~24 giorni di sviluppo vibecoding
**Open Questions critiche**: crediti per piano, Vapi mode (da decidere prima di iniziare)

## Connessioni
- [[Vendi_la_Skill_Course]] — target audience simile
- [[Concept_Copywriting_Framework]] — knowledge base per l'AI interna
- [[Concept_Conversion_Rate_Optimization]] — dominio core del prodotto
- [[Project_Outreach_Automation_Implementation]] — canale acquisizione (Reddit, X)
- [[Manuale_Claude_Code_Product]] — possibile cross-sell
