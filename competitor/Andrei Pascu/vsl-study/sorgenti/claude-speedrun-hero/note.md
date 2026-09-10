# claude-speedrun-hero — come e' stato preso

- **Pagina**: https://claude-speedrun.com/
- **Flusso**: `https://player.vimeo.com/video/1175138868`
- **Data**: 2026-09-10

## Cosa e' servito

VSL in cima alla pagina Claude Speedrun v2. ID da src/32-index-hunxel6D.js della cattura 12-claude-speedrun-v2. NB: le catture 07 e 12 sono la stessa pagina (claude-speedrun.com), non due prodotti diversi.

Il flusso e' HLS: yt-dlp ha scaricato traccia video e traccia audio separate e le ha unite in mp4 con ffmpeg. Pagina pubblica, nessun login, nessun pagamento, nessuna protezione aggirata.

## Cosa NON ha funzionato

- Cercare l'URL del flusso dentro il codice catturato non basta per i player nativi (vedi outheadline): li' l'unica strada e' ascoltare la rete con Playwright.
- La pagina non espone un `.mp4` diretto: e' sempre HLS segmentato, quindi il download passa per forza da yt-dlp/ffmpeg.
