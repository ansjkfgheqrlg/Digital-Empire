# outfunnel-vsl-1 — come e' stato preso

- **Pagina**: https://www.andrei-copy.com/outfunnel
- **Flusso**: `https://player.vimeo.com/video/1053413091?h=1f9bb5f882`
- **Data**: 2026-09-10

## Cosa e' servito

Primo VSL di outFunnel. Lo stesso ID compare anche su https://armageddon.bsns.it/outfunnel: il video e' riusato tra i due lanci, scaricato una volta sola.

Il flusso e' HLS: yt-dlp ha scaricato traccia video e traccia audio separate e le ha unite in mp4 con ffmpeg. Pagina pubblica, nessun login, nessun pagamento, nessuna protezione aggirata.

## Cosa NON ha funzionato

- Cercare l'URL del flusso dentro il codice catturato non basta per i player nativi (vedi outheadline): li' l'unica strada e' ascoltare la rete con Playwright.
- La pagina non espone un `.mp4` diretto: e' sempre HLS segmentato, quindi il download passa per forza da yt-dlp/ffmpeg.
