---
Type: TOOL
Status: Experimental
Tags: #tool #video #voce #acquisto #higgsfield #elevenlabs #ai-generativa #produzione-contenuti
Created: 2026-09-04
Last updated: 2026-09-04 (revisione 2 — scansione completa del sito)
---

# Higgsfield + ElevenLabs — valutazione d'acquisto

## Overview

Due strumenti valutati il 2026-09-04 su richiesta di Max. La prima stesura si era fermata al
listino e a tre pagine, e aveva prodotto due verdetti sbagliati; Max ha chiesto di entrare
davvero. **Revisione 2: 60 pagine di higgsfield.ai lette con Playwright sul DOM renderizzato**,
piu' documentazione API, help center, Termini d'uso e normativa.
Dossier completo: `PIANO-MAESTRO/28-DOSSIER-HIGGSFIELD-ELEVENLABS.md`.
Report professionale: https://claude.ai/code/artifact/24fb95f3-f393-4566-b014-2b8e307d2335

## Cos'e' Higgsfield davvero

Non un generatore di video: un **sistema operativo di produzione contenuti**. Oltre 30 modelli
(Sora 2, Veo 3.1, Kling 3.0, Seedance 2.0 e 2.5, Wan 3.0, Nano Banana Pro, FLUX.2, Soul) sotto
un solo abbonamento e un solo sistema di crediti, piu' un livello di automazione che e' il vero
valore.

| Modulo | Cosa fa |
|---|---|
| **AI Long Video Generator** | Script -> video multi-scena da minuti. Storyboard mode, character lock, scene extension, **fino a 12 reference per scena**, audio nativo (dialoghi, SFX, musica), lipsync e doppiaggio in 74+ lingue, upscale 4K, export MP4 in 16:9, 9:16, 1:1 |
| **Supercomputer** | Agente che gira tutta la piattaforma da una chat. AI Employees con skill preinstallate, Orchestrator, ragionamento su Claude Opus/Sonnet 4.6, **30+ connettori** (Slack, Drive, Notion), workflow ricorrenti programmabili |
| **Canvas** | Editor a nodi, piu' modelli nello stesso grafo, template riutilizzabili tra campagne |
| **Marketing Studio** | 6 formati. Incolli la URL e il prodotto si carica da solo con logo, colori e copy. 100+ avatar. Layer modificabili |
| **AI Ad Generator** | URL -> annuncio finito in 2 minuti, 9 modalita' |
| **Layers** | Immagine piatta -> **livelli modificabili, testo compreso**. Relight, inpaint, decomposizione |
| **Audio** | TTS, Voice Change, Translate. **ElevenLabs v3 come modello di default**, piu' MiniMax, Seed Speech, Vibe Voice |
| **Soul ID / Character** | Personaggio costante fra luci, angoli e stile. Soul 2.0 a 0,12 crediti a immagine |
| **MCP e CLI** | `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp` |
| **Plugin** | Photoshop, After Effects, Premiere Pro, DaVinci Resolve, **Figma**, Blender |

Altri: Popcorn (storyboard 8 scene), Genjutsu (ricasta video esistenti), Mixed Media, Fashion
Factory, Lipsync Studio, Photodump Studio, AI Influencer Studio, Games con deploy, Collab.

**Lacune reali:** nessun generatore di sottotitoli nativo (`/subtitles` e' 404) e costo in
crediti del Text-to-Speech non pubblicato — unico numero non verificabile dall'esterno.

## I tre fatti che decidono

1. **Higgsfield sostituisce Fliki.** Il Long Video Generator dichiara alla lettera il nostro caso
   d'uso: *"Build YouTube and long-form content, faceless channels, full episodes"*. Un video da
   10 minuti in modello misto (8 clip Kling 3.0 1080p + 60 immagini Soul 2.0) costa **~71 crediti
   = €2,78**, cioe' **~16 video al mese** col piano Plus.
2. **L'unlimited non e' automatizzabile.** I Termini vietano lo scripting e l'unlimited non
   esiste su MCP, CLI, Canvas o Supercomputer. Si usa a mano in sprint di 7 giorni a inizio mese;
   l'automazione passa da MCP e API, a crediti.
3. **Le chiamate a freddo automatiche in Italia sono bloccate.** Legge 49/2026 (opt-in dal 19
   giugno) e AI Act articolo 50 (dal 2 agosto, obbligo di dichiarare l'AI dentro la
   conversazione). Il flusso vocale va costruito sul lead caldo che ha gia' risposto in Preventa.

## Numeri chiave

| | Higgsfield Plus | ElevenLabs Creator |
|---|---|---|
| Prezzo | €59 mensile, **€47 annuale** | $22 mensile, $18,33 annuale |
| Quota | 1.200 crediti/mese (€0,039 l'uno) | 121.000 crediti/mese |
| Video | Kling 3.0 1080p 8 cr/5s · Seedance 2.0 1080p 45 cr/5s · Veo 3.1 1080p 29 cr/4s | — |
| Immagini | Soul 2.0 0,12 cr · Nano Banana Pro 2 cr | — |
| Voce | TTS incluso (ElevenLabs v3), costo da misurare | 1 credito per carattere, Voice Changer 1.000 cr/min |
| Chiamate | non le fa | ~€0,21 per chiamata da 2 minuti |

**Starter non accede a Seedance**: il piano minimo utile e' Plus.

## Rapporto con Arena — verdetto corretto

La revisione 1 proponeva di spostare i caroselli su Nano Banana Pro a €0,78 l'uno. **Ritirato.**
Le slide che Max produce in Arena sono un sistema di design coerente allineato alle
[[Concept_CCM_Brand_Guidelines]]: Nano Banana Pro genera la fotografia di una slide, non un
layout. Il confronto sul prezzo era l'asse sbagliato.

**I caroselli restano su Arena**, e il lavoro li' e' rendere affidabile l'automazione (captcha,
modale Terms of Use, bottoni che cambiano, sessioni che scadono — oltre 40 script di debug in
`caroselli - agency` lo raccontano). L'unica cosa di Higgsfield che entra qui e' **Layers**:
prendere una slide gia' perfetta e rigenerarne solo il testo, invece di ritirare i dadi sul
layout.

## Connessioni
- [[Tool_Arena_Workflow_Caroselli]]
- [[Digital_Empire_YouTube_Automation_Factory]]
- [[Preventa_Outreach_Automation]]
- [[Concept_CCM_Brand_Guidelines]]
