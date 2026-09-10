# armageddon-home — come e' stato preso

- **Pagina**: https://armageddon.bsns.it/
- **Flusso**: `https://player.vimeo.com/video/1224266050?h=146a86b1fa`
- **Data**: 2026-09-10

## Cosa e' servito

VSL principale dell'ultimo lancio Armageddon. Player Vimeo pubblico (f.vimeocdn 4.46.106), HLS multi-bitrate. ID ricavato dalla cattura del 07/09 (site-study/capture/11-armageddon/scheda.json), confermato da yt-dlp senza login.

Il flusso e' HLS: yt-dlp ha scaricato traccia video e traccia audio separate e le ha unite in mp4 con ffmpeg. Pagina pubblica, nessun login, nessun pagamento, nessuna protezione aggirata.

## Cosa NON ha funzionato

- Cercare l'URL del flusso dentro il codice catturato non basta per i player nativi (vedi outheadline): li' l'unica strada e' ascoltare la rete con Playwright.
- La pagina non espone un `.mp4` diretto: e' sempre HLS segmentato, quindi il download passa per forza da yt-dlp/ffmpeg.
