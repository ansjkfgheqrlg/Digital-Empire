# 📏 Regole fisse — Fabbrica Video "Dose Mentale"

> Regole date da Gael più volte (2026-07-29), non richiederle di nuovo. Riferimento tecnico
> completo: [CP-20260729-009](checkpoints/CP-20260729-009.md), [CP-20260729-010](checkpoints/CP-20260729-010.md).
> *(rinumerati da CP-20260729-001/002 nel merge del 2026-07-30 per collisione con due checkpoint
> diversi creati in parallelo da un'altra sessione.)*

## Cosa NON è questo progetto
Il "Manuale Claude Code" è un progetto **morto, non più attivo**. Non nominarlo mai più in
relazione a questo lavoro. Questo NON è un funnel verso un info-prodotto.

## Cosa È questo progetto
Un canale YouTube (comprato già monetizzato, gestito da Gael/Max — non compito di Claude)
il cui unico obiettivo è **guadagnare dalle visualizzazioni**, copiando/adattando i video reali
del canale **@dosementale** (`https://www.youtube.com/@dosementale`) — contenuto reale:
spiritualità, psicologia, saggezza biblica/buddista, motivazione/storie di vita, salute e
benessere per un pubblico adulto/anziano.

## Flusso obbligatorio per ogni video
1. Scegliere un video reale da `@dosementale` per velocity (views/età, soglia maturità 24h) —
   stesso criterio già usato in F2 di `apex7_orchestrator.py`, applicato però su questo canale,
   non sui 20 canali AI del vecchio niche-scout.
2. Scaricare il transcript reale (yt-dlp `--write-auto-sub`) e riscrivere (non copiare verbatim)
   uno script adattato sullo stesso argomento reale, formato HOOK/INTRO/CORPO/CTA.
3. Copertina: `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/arena_thumbnail.py` (Arena.ai
   via Playwright, profilo persistente `chrome-profile-arena/` — sessione già loggata, non
   richiedere login di nuovo salvo scadenza).
4. Video: `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py` (API Fliki reale).

## Standard qualità obbligatori (verificare sempre col file reale, non fidarsi della sola risposta API)
- **Durata ≥ 12 minuti** — `duration` nell'API Fliki è in **MINUTI**, non secondi. Per
  `workflowType: "script"`, il valore **0** è documentato come "usa il contenuto COSÌ COM'È,
  senza riscriverlo" — senza `duration: 0`, Fliki riscrive/condensa il testo in un video breve
  a lunghezza fissa (verificato: due run con script diversi sono uscite entrambe a 230.592s
  identici, segno di riscrittura automatica indipendente dal contenuto). Con `duration: 0` la
  durata finale dipende dalla lunghezza reale dello script. Verificare comunque sempre con
  `ffprobe -show_entries format=duration` sul file scaricato.
  - **Valori già provati, NON riprovarli** (storico reale, per non ripetere esperimenti a vuoto):
    campo assente → 230.6s · `720` (creduto secondi, in realtà 720 MINUTI) → 230.6s **identico** ·
    `0` con 4 scene → 230.6s identico · `0` con 18 scene (frase per frase) → 181.1s (diverso ma
    più corto). Il valore reale in minuti (es. `15`) è l'unica combinazione sensata rimasta.
- **Voce di alta qualità** — non il primo risultato di un filtro genere andato in fallback.
- **Sottotitoli sempre presenti, precisi, senza errori** — richiede un `subtitlePresetId` REALE
  (es. `builtin-legacy-bold`), ottenibile solo cliccando "Copy subtitle preset ID" su
  `fliki.ai/info/subtitle` via Playwright (non è nell'HTML statico né in chiamate di rete
  intercettabili). Verificare con un fotogramma ffmpeg a metà video che siano visibili davvero.

## Limite noto — velocità Fliki (non un bug da rincorrere in loop)
Verificato a fondo (documentazione ufficiale + test reali ripetuti): l'API Fliki non espone
nessun parametro di priorità/velocità/tier. Il tempo "queued" (~860-970s, ~14-16 min) osservato
è lato server, praticamente costante indipendentemente da contenuto/durata richiesta — non
riducibile lato client. Se serve sotto i 10 minuti totali, l'unica leva è un eventuale tier a
pagamento più alto sull'account Fliki (da verificare sul loro dashboard, non nel codice).
