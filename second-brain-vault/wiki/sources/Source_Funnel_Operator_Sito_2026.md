---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #funneloperator #sito #design-system #fabbrica-siti
Created: 2026-09-13
Last updated: 2026-09-13
---

# funneloperator.it — il sito nuovo del corso di Andrei Pascu (studio 13/09/2026)

## Overview
Il sito che Max indica come **il migliore di Andrei Pascu**: dominio proprio, non più una pagina di andrei-copy.com. Studiato in quattro
rapporti paralleli sulla cattura forense (30 sezioni, 32.807 px, 26 CTA, 68 immagini originali, 44 file sorgente): struttura e strategia,
stile, atlante visivo degli elementi, costruzione. Sintesi e **strategie classificate** (FO-S/C/I/E/T) in
`competitor/Andrei Pascu/site-study/reports/66-funneloperator-SINTESI-STRATEGIE.md`.

## Dettagli
- **Struttura**: primo volto all'8,5%, numeri al 9,6%, storia personale = 14% della pagina (7 foto), **primo bottone di acquisto al 64%**;
  un solo bottone flottante a tre sentinelle; 3 micro-CTA «↓»; urgenza vera nel codice (`434 → 560 € dal 2026-10-12`).
- **Stile**: colonna 832 px; fondi `#111111`/`#ededed` mai puri; un accento in 4 luci speso in testo 16 : decorazione 9 : bottoni 3;
  0 ombre; raggi 8/12/24; 4 famiglie a ruolo fisso (Plus Jakarta Sans titoli, Inter Tight corpo, DM Mono metadati, Curseyt solo h1); 6 corpi;
  grana CSS presente ma spenta (la materia è nelle WebP); nessun reveal on scroll; reduced-motion in tre strati.
- **Immagini**: 15 foto vere del fondatore con luce = accento, 10 xilografie di una sola mano, oggetti costruiti (tessera SEC, badge con QR,
  carte, insegna, cartella in `clip-path`); **40 raster su 60 a 2× esatto, 1 sola ritagliata dal CSS, width/height ovunque, lazy tranne l'hero**.
- **Costruzione**: React 19 + TanStack Start + Tailwind v4 + Supabase su Vercel; design system `fo-` in italiano (59 token OKLCH); prezzo come
  dato unico → cifra, countdown, FAQ, JSON-LD; placeholder autodichiarati; consenso onesto; difetti: bundle 589 KB che espone l'ambiente,
  numeri magici, 7 colori fuori token, testo giustificato, portfolio di 3 pezzi ripetuti.
- **Ufficializzato in DE**: ADR-031 → CLAUDE-SITI **§14 «L'immagine si vede intera»** e **§15 «Il volto prima, la richiesta dopo»**;
  14 pattern candidati; B-083…B-088; 12 candidati in MIGLIORAMENTI; Dossier 38 v2 del sito agency riscritto su queste strategie.

## Connessioni
- [[Tool_Fabbrica_Siti]] — §14 e §15 nascono qui
- [[Progetto_Sito_Agency_Vivo]] — il piano solo-aggiunte riscritto (Dossier 38 v2)
- [[Synthesis_Sistema_Visivo_Andrei_Pascu]] — le 52 pagine precedenti; questa è la prima «app React» dell'ecosistema
- [[Source_Andrei_Pascu_Armageddon_Landing_Lancio]] — il primo sito costruito con Claude Code; qui il metodo è maturo
