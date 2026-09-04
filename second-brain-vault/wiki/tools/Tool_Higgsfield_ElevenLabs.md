---
Type: TOOL
Status: Experimental
Tags: #tool #video #voce #acquisto #higgsfield #elevenlabs #ai-generativa
Created: 2026-09-04
Last updated: 2026-09-04
---

# Higgsfield + ElevenLabs — valutazione d'acquisto

## Overview

Due strumenti valutati a fondo il 2026-09-04 su richiesta di Max, entrando sui siti veri
(Playwright su DOM renderizzato, perche' entrambe le pagine prezzi sono SPA e il fetch
semplice le vede vuote). **Higgsfield** e' un negozio con oltre 30 modelli video e immagine
sotto un solo abbonamento; **ElevenLabs** e' voce sintetica, clonazione e agenti vocali.
Dossier completo con tutti i numeri: `PIANO-MAESTRO/28-DOSSIER-HIGGSFIELD-ELEVENLABS.md`.

## I tre fatti che cambiano le decisioni

1. **Higgsfield non sostituisce Fliki.** Tetto di 15 secondi per clip: fa il girato, non il
   film. E il blocco della fabbrica YouTube non viene da Fliki ma da un nostro gate,
   `quality_gate.py:93`, con 21 fallimenti identici in memoria.
2. **L'unlimited di Higgsfield non e' automatizzabile.** I Termini vietano scripting e uso
   automatizzato, e l'unlimited non esiste su MCP, CLI, Canvas o Supercomputer. Si usa a mano,
   in sprint. L'automazione legittima passa da MCP e API, a crediti.
3. **Le chiamate a freddo automatiche in Italia oggi non si possono fare.** Legge 49/2026
   (opt-in dal 19 giugno) e AI Act articolo 50 (operativo dal 2 agosto, obbligo di dichiarare
   l'AI dentro la conversazione). Il flusso vocale si costruisce sul lead caldo che ha gia'
   risposto, non a freddo.

## Numeri chiave

| | Higgsfield Plus | ElevenLabs Creator |
|---|---|---|
| Prezzo | €59 mensile, €47 annuale | $22 mensile, $18,33 annuale |
| Quota | 1.200 crediti/mese | 121.000 crediti/mese |
| Unita' | Kling 3.0 1080p 8 cr/5s, Nano Banana Pro 2 cr/img, Soul 2.0 0,12 cr/img | 1 credito per carattere, Voice Changer 1.000 cr/minuto |
| Un promo 30s con retake | €5,65 | — |
| Un carosello da 10 slide | €0,78 | — |
| Una chiamata vocale da 2 minuti | — | circa €0,21 tutto compreso |

Sbarramento: **Starter non accede a Seedance**, quindi il piano minimo utile e' Plus.

## Integrazione con Claude Code

Higgsfield espone un server MCP ufficiale, quindi Emperator genera immagini e video
direttamente dal flusso di lavoro:

```
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

Nessun tetto di spesa nativo: il freno e' la regola nostra (mai sopra 50 crediti senza via
libera di Max).

## Rapporto con Arena

Arena resta viva per l'esplorazione gratuita e va comunque riparata. Ma la produzione dei
caroselli conviene su Nano Banana Pro via MCP, dove **le reference sono un parametro** e non un
upload manuale fragile: €0,78 a carosello contro il debito di tempo accumulato in
`caroselli - agency` (oltre 40 script di debug e 60 screenshot di tentativi).

## Connessioni
- [[Tool_Arena_Workflow_Caroselli]]
- [[Digital_Empire_YouTube_Automation_Factory]]
- [[Preventa_Outreach_Automation]]
- [[Concept_CCM_Brand_Guidelines]]
