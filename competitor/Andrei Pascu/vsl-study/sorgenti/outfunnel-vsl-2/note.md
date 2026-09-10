# outfunnel-vsl-2 — come e' stato preso

- **Pagina**: https://www.andrei-copy.com/outfunnel
- **Flusso**: `https://player.vimeo.com/video/1053450256?h=ba0c8f3d0c`
- **Data**: 2026-09-10

## Cosa e' servito

Secondo VSL di outFunnel.

Il flusso e' HLS: yt-dlp ha scaricato traccia video e traccia audio separate e le ha unite in mp4 con ffmpeg. Pagina pubblica, nessun login, nessun pagamento, nessuna protezione aggirata.

## Cosa NON ha funzionato

- Cercare l'URL del flusso dentro il codice catturato non basta per i player nativi (vedi outheadline): li' l'unica strada e' ascoltare la rete con Playwright.
- La pagina non espone un `.mp4` diretto: e' sempre HLS segmentato, quindi il download passa per forza da yt-dlp/ffmpeg.
