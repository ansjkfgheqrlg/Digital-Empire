# INVENTARIO SORGENTI VSL — Andrei Pascu

Fase 0 dello studio del montaggio. File veri sul disco, presi da pagine di vendita **pubbliche**,
nessun login e nessuna protezione aggirata. Dati tecnici misurati con `ffprobe`, non stimati.

**Data raccolta:** 2026-09-10

## Presi

| bersaglio | url pagina | flusso trovato | scaricato | durata | peso | note |
|---|---|---|---|---|---|---|
| `armageddon-home` | https://armageddon.bsns.it/ | Vimeo 1224266050 | **SI** | 0:13:28 | 357.1 MB | 1920x1080 @ 25.0fps, h264/aac — — |
| `claude-speedrun-hero` | https://claude-speedrun.com/ | Vimeo 1175138868 | **SI** | 0:01:21 | 34.5 MB | 1920x1080 @ 30.0fps, h264/aac — — |
| `claude-speedrun-sez9` | https://claude-speedrun.com/ | Vimeo 1175159560 | **SI** | 0:04:45 | 120.6 MB | 1920x1080 @ 30.0fps, h264/aac — — |
| `claude-speedrun-sez14` | https://claude-speedrun.com/ | Vimeo 1175270347 | **SI** | 0:05:57 | 133.5 MB | 1920x1080 @ 30.0fps, h264/aac — — |
| `arma-outfunnel-vsl` | https://armageddon.bsns.it/outfunnel | Vimeo 1224257782 | **SI** | 0:01:39 | 58.8 MB | 1920x1080 @ 29.97fps, h264/aac — — |
| `arma-outemail-vsl` | https://armageddon.bsns.it/outemail | Vimeo 1224257842 | **SI** | 0:02:47 | 72.8 MB | 1920x1080 @ 29.97fps, h264/aac — — |
| `arma-outemail-secondo` | https://armageddon.bsns.it/outemail | Vimeo 1072634745 | **SI** | 0:01:46 | 45.7 MB | 1920x1080 @ 29.97fps, h264/aac — riusato su 2 lanci |
| `outfunnel-vsl-1` | https://www.andrei-copy.com/outfunnel | Vimeo 1053413091 | **SI** | 0:02:31 | 81.1 MB | 1920x1080 @ 30.0fps, h264/aac — riusato su 2 lanci |
| `outfunnel-vsl-2` | https://www.andrei-copy.com/outfunnel | Vimeo 1053450256 | **SI** | 0:01:48 | 67.6 MB | 1920x1080 @ 29.97fps, h264/aac — — |
| `outheadline-vsl` | https://www.andrei-copy.com/outheadline | HLS Squarespace | **SI** | 0:00:46 | 17.0 MB | 1920x1080 @ 24.0fps, h264/aac — HLS nativo, url firmato a scadenza |

**Totale: 10 VSL — 00:36:52 di girato — 0.97 GB.**

Ogni cartella contiene `video.mp4`, `sorgente.json` (url pagina, url flusso, data, metodo, durata, risoluzione, fps, bitrate, codec video e audio) e `note.md`.

## Non presi

| bersaglio | url pagina | perche' |
|---|---|---|
| `apsales` | https://apsales.eu/ | **Sito irraggiungibile ora, non un login.** Il DNS risolve (185.158.133.1) ma il server chiude l'handshake TLS con `SSLV3_ALERT_HANDSHAKE_FAILURE` a curl, a Chromium e a Python. Nessun VSL raggiungibile finche' il certificato non torna a posto. Da riprovare. |
| `arma-outheadline` | https://armageddon.bsns.it/outheadline | Pagina caricata in diretta con Playwright, click di play tentato, scroll completo: **nessuna richiesta video emessa**. Quella pagina non ha un VSL, e' solo testo. |
| `arma-outviral` | https://armageddon.bsns.it/outviral | Nessun VSL. Solo due clip di contorno senza audio (`assets/img/outviral/NPC.mp4`, `NPC3.mp4`): sono decorazione, non materiale di montaggio. |

## Da sapere prima di studiare

- **Le catture `07-claude-speedrun` e `12-claude-speedrun-v2` sono la stessa pagina** (`https://claude-speedrun.com/`), catturata due volte. Non sono due prodotti: la v2 e' quella viva. Sulla pagina ci sono tre video, tutti presi.
- **Tutto Vimeo, tranne outHeadline.** Andrei Pascu monta su Vimeo (player `f.vimeocdn.com` 4.46.106, HLS multi-bitrate fino a 1080p25). L'unica eccezione e' `andrei-copy.com/outheadline`, video nativo Squarespace: quello e' un residuo del vecchio sito, non della macchina Armageddon.
- **Due video sono riusati tra i lanci.** `1053413091` sta sia su `andrei-copy.com/outfunnel` sia su `armageddon.bsns.it/outfunnel`; `1072634745` sta sia su `andrei-copy.com/outemail` sia su `armageddon.bsns.it/outemail`. Scaricati una volta sola: e' gia' un dato di studio, riusa il girato invece di rigirarlo.
- **I VSL nuovi di Armageddon hanno ID consecutivi** (`1224257782`, `1224257842`, `1224266050`): girati e caricati tutti nella stessa sessione, poche ore l'uno dall'altro.

## Altri VSL individuati, non scaricati

Fuori dal perimetro di questa Fase 0, ma gli ID sono gia' in mano se servono:

| pagina | vimeo |
|---|---|
| https://www.andrei-copy.com/outemail | 1072650262 |
| https://www.andrei-copy.com/copy | 1099337502 |
| https://www.andrei-copy.com/asa | 1099333295 |
| https://www.andrei-copy.com/define | 1099334931 |
| https://www.andrei-copy.com/vendita | 692784678, 839332808 |

## Come rifarlo

1. Gli ID Vimeo erano **gia' dentro le catture del 07/09** (`site-study/capture/<slug>/scheda.json`, campo degli iframe). Non serviva aprire il browser.
2. Per i player nativi (Squarespace, Wix) l'url non e' nel codice statico: va sniffato in diretta con Playwright ascoltando le richieste di rete e cercando `.m3u8`.
3. Scarico: `python -m yt_dlp --referer <pagina> -f "bv*[height<=1080]+ba/b" --merge-output-format mp4 -o video.%(ext)s <flusso>`.
