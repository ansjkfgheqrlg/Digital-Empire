# arma-outfunnel-vsl — come e' stato preso

- **Pagina**: https://armageddon.bsns.it/outfunnel
- **Flusso**: `https://player.vimeo.com/video/1224257782?h=306ceb39fa`
- **Data**: 2026-09-10

## Cosa e' servito

VSL nuovo di outFunnel dentro Armageddon. Confermato in diretta via Playwright: iframe Vimeo emesso al caricamento della pagina.

Il flusso e' HLS: yt-dlp ha scaricato traccia video e traccia audio separate e le ha unite in mp4 con ffmpeg. Pagina pubblica, nessun login, nessun pagamento, nessuna protezione aggirata.

## Cosa NON ha funzionato

- Cercare l'URL del flusso dentro il codice catturato non basta per i player nativi (vedi outheadline): li' l'unica strada e' ascoltare la rete con Playwright.
- La pagina non espone un `.mp4` diretto: e' sempre HLS segmentato, quindi il download passa per forza da yt-dlp/ffmpeg.
