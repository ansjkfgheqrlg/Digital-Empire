---
Type: PROJECT
Status: Active
Tags: #preventa #caroselli #arena #playwright #instagram #reparto-produzione
Created: 2026-08-03
Last updated: 2026-08-23
---

# Progetto Preventa — Caroselli Instagram

## Overview
Primo progetto creato sotto [[Reparto_Produzione_Digital_Empire]] (ordine di Max,
Fase 3 del piano [[CP-20260803-004]]). Genera caroselli Instagram promozionali per
Preventa. **Primo carosello reale prodotto e verificato il 2026-08-06** ([[CP-20260805-013]]).

## ⚠️ Correzione importante (2026-08-05/06)
La prima versione di questa pagina descriveva il motore sbagliato. Il motore reale
"perfetto" a cui Max si riferiva **non è** `ArenaAI/arena_generator.py` (Playwright
grezzo, chat Direct+Image, 3 slide, gradiente hardcoded) — è un **Agent workspace
già costruito dentro Arena stessa** (Arena "Agent Mode"), con un file system persistente
(`apex7/agents/memory/orchestrator/playwright_bridge/...`), raggiungibile SOLO tramite
una chat archiviata specifica. Il motore Playwright grezzo resta comunque utile come
infrastruttura condivisa (usato per Agency) ma non è il percorso per Preventa.

## Perché non è un funnel di vendita
Preventa vende tramite outreach WhatsApp diretto ai concessionari (vedi
[[Preventa_Logica_Completa_Metodo]]), non tramite DM Instagram. I caroselli servono
per brand awareness/social proof, non per generare lead diretti dai commenti/DM.

## Percorso
`SKILL & Agenti/Workflow agency creative/caroselli - preventa/`

## Contenuto reale (positioning, non inventato)
Preso da `Crea siti/Preventa/index.html` + `agency-empire/.../03b-preventa.tsx` +
[[Preventa_Logica_Completa_Metodo]]:
- Prodotto: incolli il link di un annuncio auto (anche estero) → PDF preventivo
  brandizzato con prezzi bloccati, pronto per WhatsApp.
- Prezzo: €2.000 una tantum, nessun canone.
- Target: concessionari import (stesso segnale di [[CP-20260803-005]] — filtro
  solo-import dell'outreach).
- Leve psicologiche usate nel copy (stesse validate nell'outreach): perdita
  imminente (cliente scrive AGLI ALTRI concessionari ora), sollievo dal tempo perso
  (20-30 min → 5 sec), vergogna Excel disordinato vs PDF professionale, doppio
  lavoro import (tradurre + ricalcolare).

## Come funziona DAVVERO (verificato con un run reale completo, non assunto)
1. Arena → sidebar **Search** → tab **Archived** → apri la chat
   **"# PROMPT INGEGNERIZZATI PER [ARENA.AI]"**.
2. Scrivi **`/inizio-generazione`** (se la chat non è già attivata).
3. Quando chiede l'argomento: dagli un **contesto ricco** (prodotto, pain point,
   leve, target, prezzo, tono) — un one-liner non basta, la chat non conosce il
   prodotto (correzione di Max dopo il primo tentativo troppo scarno).
4. Genera 8 slide fisse: IL PROBLEMA, LA VERITÀ, LA SOLUZIONE, COME FUNZIONA,
   IL RISULTATO, LA DOMANDA VERA, INIZIA ORA — una alla volta, con immagini 4K
   ultra grain.
5. Può fermarsi su "The AI took too long to respond" — si sblocca scrivendo
   "continua".
6. Chiede conferma finale "Questo compito è riuscito? Sì/No" — confermare "Sì".
7. Il file ZIP appare come un chip inline nel testo — cliccarlo apre un pannello
   con un bottone "Download file" (non confondere con "Download workspace", che
   scarica tutto il progetto).

Script che automatizzano questo flusso via Playwright (riusano l'account Arena già
autenticato, non duplicano il motore): `run_content_factory.py`, `check_status.py`,
`resume_generation.py`, `confirm_and_download.py`, tutti in `caroselli - preventa/`.

## Stato al 2026-08-06
- ✅ **Primo carosello reale generato e scaricato**: 8 PNG (1080×1350, upscalati da
  4K) + `copy.json`, salvato in
  `Arsenale Caroselli/Preventa/2026-08-06_tempo-perso-import/` — libreria dei
  caroselli finiti, separata dal motore (richiesta esplicita di Max: "un'arsenale
  dei caroselli, una cartella per ogni prodotto"). Verificato
  con `unzip -l` (10 file, dimensioni reali) e ispezione visiva (slide 8/8: prezzo,
  target, brand tutti corretti).
- ✅ Scaffold del progetto Preventa completo, `py_compile` pulito su tutti gli script.
- ✅ Cartella Agency (`caroselli - agency/`) non modificata nella sua logica di
  business — solo il motore condiviso `ArenaAI/arena_generator.py` ha ricevuto fix
  di bug reali (vedi [[CP-20260805-013]]) che beneficiano anche Agency.

## Aggiornamento 2026-08-12 — motore di pubblicazione IG, dry-run verificato

Max ha fornito le credenziali reali della pagina `digitalempireagency.e` (già presenti
in `Workflow pubblicazione automatica/Instagram/config.py`, stesso publisher già
esistente e funzionante) e chiesto un motore di pubblicazione + un team copy APSOC.

Scritto `publish_instagram.py` — **wrappa** `Instagram/instagram_publisher.py` via
import (ADR-003, nessuna modifica al motore condiviso). Testato per la prima volta
in **dry-run**: trova le 8 slide del carosello #1 e le compone correttamente, senza
toccare IG. Il "team copy APSOC" richiesto **non va costruito**: esiste già come
skill [[cro-copy-architect]].

**Nota di processo**: questo lavoro (credenziali, wrapper, edit a
`run_content_factory.py`) era esistito solo su disco/in chat per 6 giorni prima di
essere salvato in un checkpoint — recuperato rileggendo la conversazione, non la
Memory. Verificato anche che il "blocco arena.ai" di una sessione precedente non era
specifico al servizio: nello stesso momento anche google.com/github.com erano
irraggiungibili dalla stessa shell → mancanza di rete del sandbox, non outage Arena.

**Prossimo passo (non ancora fatto)**: generare carosello #2, scrivere caption reale
via `cro-copy-architect`, poi solo con ok esplicito di Max lanciare
`publish_instagram.py --live` per il primo post reale.

## Connessioni
- [[Reparto_Produzione_Digital_Empire]] — il concetto organizzativo che questo progetto inaugura
- [[Preventa_Logica_Completa_Metodo]] — il prodotto/sistema outreach che questi caroselli promuovono
- [[CP-20260803-005]] — filtro solo-import (stesso target audience)
- [[CP-20260805-013]] — primo output reale, flusso esatto verificato
