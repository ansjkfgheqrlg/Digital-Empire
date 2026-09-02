---
Type: SOURCE
Status: Active
Tags: #corso #andrei-pascu #cs2online #vibe-coding #web-development #claude #html #css #javascript
Created: 2026-09-01
Last updated: 2026-09-01
---

# CS2 Lezione 17 — Introduzione al vibe coding

## Overview
Prima lezione della sezione "AI - per coding e simili" del corso Claude Speedrun 2. Andrei definisce il vibe coding (generare codice con AI senza saper programmare) e dimostra il workflow completo: installare VS Code, scrivere HTML/CSS/JS base, usare Live Server, generare codice con Claude via prompt JSON, caricare su GitHub, gestire immagini con Imgur. 14 workflow pratici dimostrati.

## Fonte
- **Tipo**: Corso a pagamento (membership)
- **Autore**: Andrei Pascu
- **Piattaforma**: andrei-copy.com/cs2online
- **Sezione**: AI - per coding e simili (lezione 1 di 7)
- **Rilevanza per DE**: Bassa (entry-level rispetto allo stack DE) — valore pedagogico

## Core Takeaway
Il vibe coding non e' "zero conoscenza" — serve capire le basi (HTML/CSS/JS) per comunicare efficacemente con l'AI. Il formato JSON e' superiore al linguaggio naturale per brief strutturati. Nella realta' professionale si usa un approccio ibrido: website builder per la struttura, codice AI-generated per personalizzazioni.

## Key Insights

### Stack minimo
VS Code + Live Server + Claude + GitHub + Imgur. Alternativa: Cursor (VS Code fork con AI nativa).

### 3 file sempre separati
`index.html`, `style.css`, `main.js` — mai in un unico file. Leggibilita', modifiche AI-friendly, meno errori server.

### Prompt JSON > linguaggio naturale
Per progetti strutturati, Claude capisce JSON molto meglio. Workflow: descrivere in naturale → Claude converte in JSON → iterare ("E' il miglior prompt che puoi darmi?") → usare JSON in chat nuova per generare codice.

### 2 fasi distinte
Fase 1 (prompt engineering): chat dedicata per raffinare il brief JSON.
Fase 2 (code generation): chat nuova, solo il prompt JSON, generazione pulita.

### Approccio ibrido reale
Builder (Squarespace/WordPress) per struttura + code block custom generati dall'AI per personalizzazioni specifiche. Non tutto da zero.

### Multi-chat per dominio
Una chat per il copy, una per il branding, una per la struttura, una per le immagini. Contesto giusto per ogni dominio.

### Gestione errori
Copiare l'errore dalla console del browser → incollarlo direttamente a Claude. Non spiegare, non interpretare.

### Elementi semantici
`<header>`, `<main>`, `<footer>` non sono decorazione — servono per accessibilita' (screen reader) e SEO.

## Connessioni a DE
- [[Source_CS2_Lezione_06_Cucinando_Contesto]] — stessa sessione di corso, contesto come ingrediente fondamentale
- [[Source_CS2_Bonus_04_Claude_Skills]] — Claude Skills come evoluzione naturale del vibe coding base
- Skill `site-build` — DE automatizza gia' questo workflow a livello industriale con agenti dedicati
- Skill `site-premium-stack` — lo stack DE (Next.js/Tailwind/shadcn/GSAP) e' molto piu' avanzato del vanilla HTML/CSS/JS insegnato qui
- Skill `site-copy` — il pattern "multi-chat per dominio" e' esattamente cosa fanno `site-copy-hero`, `site-copy-body`, `site-copy-meta`

## Azioni Proposte
- Nessuna patch tecnica — contenuto entry-level rispetto a DE
- Valore pedagogico: utile come riferimento per spiegare concetti base a Neri o clienti non tecnici

## Status
- Added: 2026-09-01
- Last reviewed: 2026-09-01
- Action taken: No (nessuna patch necessaria, entry-level)
