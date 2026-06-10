# ADR-001 — EMPIRE OS: holding di 10 ecosistemi su modello AION GROUP

- **Data:** 2026-06-10
- **Stato:** ATTIVO
- **Decisori:** Max + sessione di pianificazione (swarm 7 agenti + conductor)

## Contesto
Digital Empire opera su molti fronti (agency, outreach, info products, KDP, siti, SaaS)
in modo frammentato: decine di workflow e 100+ skill senza gerarchia né memoria condivisa.
AION GROUP (Content Factory Exponium) ha dimostrato che il modello holding di ecosistemi
di agenti funziona, ma è mono-scopo.

## Decisione
Digital Empire diventa **EMPIRE OS**: holding di **10 ecosistemi** indipendenti ma connessi
(01 AGENCY, 02 INFO-BUSINESS, 03 CONTENT-FACTORY, 04 MARKETING, 05 MULTI-BUSINESS,
06 PLATFORM, 07 FORGE, 08 INTELLIGENCE, 09 OPERATIONS, 10 MEMORY) su Corporate Backbone
condiviso, gerarchia LX→L5 (Mandato Empire → Board/C-Suite → Ecosistemi → Reparti →
Workflow → Funzioni → Agenti) + Guilds e Sentinels trasversali. Piano completo in
`Digital Empire/PIANO-MAESTRO/` (10 dossier).

## Alternative scartate
- Un solo mega-ecosistema piatto — non scala, drift garantito.
- Replicare CF Exponium 1:1 — mono-scopo, mancano Agency/Sales/Product/Memory.
- Tool esterni di orchestrazione (n8n/CrewAI) come spina dorsale — Ruflo+Claude Code
  già installati, pattern CF validati.

## Conseguenze
- Ogni nuovo lavoro si colloca in un ecosistema/reparto preciso (zero orfani).
- Costruzione a fasi F1→F12 con gate (08-ROADMAP-FASI.md).
- Il piano è la micro-base: la FORGE potrà creare nuovi ecosistemi senza toccare l'architettura.

## Contradiction-check
Nessun ADR precedente. Coerente col Mandato Empire (da formalizzare in F1.2).
