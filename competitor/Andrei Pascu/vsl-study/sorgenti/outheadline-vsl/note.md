# outheadline-vsl — come e' stato preso

- **Pagina**: https://www.andrei-copy.com/outheadline
- **Flusso**: `https://video.squarespace-cdn.com/content/v1/602126db7a4e4c01fd9babb6/c2dfdc89-bd6c-493b-a967-f88c1996a310/playlist.m3u8`
- **Data**: 2026-09-10

## Cosa e' servito

Unico bersaglio NON su Vimeo: video nativo Squarespace. L'URL non era nella cattura statica, e' stato sniffato in diretta con Playwright ascoltando le richieste di rete. Il manifest e' firmato (Signature+Expires): il link scade, il file mp4 no.

Il flusso e' HLS: yt-dlp ha scaricato traccia video e traccia audio separate e le ha unite in mp4 con ffmpeg. Pagina pubblica, nessun login, nessun pagamento, nessuna protezione aggirata.

## Cosa NON ha funzionato

- Cercare l'URL del flusso dentro il codice catturato non basta per i player nativi (vedi outheadline): li' l'unica strada e' ascoltare la rete con Playwright.
- La pagina non espone un `.mp4` diretto: e' sempre HLS segmentato, quindi il download passa per forza da yt-dlp/ffmpeg.
