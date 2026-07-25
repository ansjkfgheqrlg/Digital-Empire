# Produzione Spec (Fliki) — RUN-20260723-001 (F4)

> Nota onesta: Fliki (fliki.ai) è uno strumento **web**, non un'API automatica — si usa da browser
> (registrazione email + editor manuale, vedi `references/fliki-produzione.md`). Questo documento
> è l'istruzione precisa per chi lo esegue (Gael/Max in Fliki): il video-producer non rende il
> file, produce le istruzioni ripetibili. Nessuna spesa API è stata fatta per generare questo
> documento.

## Progetto
- **Nome:** CCM-YT-001-installare-claude-code
- **Formato:** 16:9 YouTube (1920x1080)
- **Durata stimata:** ~6-7 minuti

## Voce
- Lingua/accento: italiano neutro, tono da "collega esperto" (coerente brand voice DE — vedi
  `Outreach/Outreach Workflow/knowledge/brand_voice.py`, benchmark Andrei Pascu: diretto, numeri
  reali, peer-to-peer).
- Ritmo: medio-veloce (contenuto tecnico ma per principianti, niente lentezza).
- **Anteprima voce obbligatoria prima di procedere** — scegliere tra 2-3 voci italiane maschili/
  neutre disponibili in Fliki e validare che pronunci correttamente "Claude Code", "terminale",
  "npm install" (termini tecnici a rischio mispronuncia — verificare in anteprima).

## Musica
- Sottofondo tech/minimal, **basso impatto** (è un tutorial, non serve energia da hype).
- Volume: sotto la voce in ogni scena, specialmente durante le sezioni con comandi da leggere a
  schermo.

## Mappa Scene (da script-F3.md, una scena per blocco)

| # | Timecode | Blocco script | Visual | Durata |
|---|---|---|---|---|
| 1 | 0:00-0:15 | Hook | Screencast: terminale vuoto che si apre, testo overlay "5 minuti reali" + cronometro visibile in angolo | 15s |
| 2 | 0:15-0:20 | CTA iniziale | Bubble iscriviti (asset Fliki standard) sovrapposto al terminale | 5s |
| 3 | 0:20-0:55 | Intro | Talking-point su slide semplice (non serve volto): titolo "Cosa vediamo oggi" + 3 bullet | 35s |
| 4 | 0:55-1:40 | Prerequisiti | Screencast terminale: `node --version` | 45s |
| 5 | 1:40-2:30 | Installazione | Screencast terminale: comando + output reale di `npm install -g @anthropic-ai/claude-code` | 50s |
| 6 | 2:30-3:10 | Primo avvio | Screencast: `claude`, flusso login | 40s |
| 7 | 3:10-4:15 | Errore comune | Screencast: PATH/permessi, risoluzione dal vivo, overlay testo "ERRORE #1" | 65s |
| 8 | 4:15-4:30 | CTA metà | Bubble like sovrapposto | 15s |
| 9 | 4:30-5:30 | Verifica funzionamento | Screencast: comando di test + risposta reale | 60s |
| 10 | 5:30-6:00 | CTA finale | Slide con link Manuale + freccia verso descrizione | 30s |

**Transizioni:** taglio secco tra scene screencast (coerente col ritmo tutorial, niente dissolvenze
lente che rallentano); dissolvenza breve (0.3s) solo tra slide/bubble e screencast.

## Materiale sorgente da caricare (NON generato da Fliki, serve schermo reale)
- Registrazione screencast reale dei comandi (blocchi 4-7, 9) — **non può essere stock footage
  generico**: i comandi/output devono essere veri, altrimenti il video mente sul tutorial.
  Chi esegue: registrare con Claude Code reale prima di aprire Fliki (OBS/QuickTime bastano).

## Sottotitoli
**ON** — obbligatorio (accessibilità + SEO indicizzata, invariante skill).

## Export
- Risoluzione: **≥1080p**
- Formato: **MP4**
- Checklist pre-export:
  - [ ] Anteprima completa vista (mai saltare)
  - [ ] Volume musica verificato sotto la voce in tutte le scene
  - [ ] Sottotitoli attivi e sincronizzati
  - [ ] Browser NON chiuso durante il rendering

## Stato di questo run
**NON eseguito** — è una spec pronta da eseguire in Fliki (lavoro umano in browser), non richiede
credenziali/API a pagamento da parte mia. Nessuna violazione della regola "dry-run prima di
spendere": Fliki ha un piano gratuito con limiti (minuti/mese) — verificare con Max/Gael quale
account usare prima del primo export reale.