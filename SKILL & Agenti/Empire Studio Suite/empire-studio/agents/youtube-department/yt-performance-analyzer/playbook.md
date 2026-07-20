# yt-performance-analyzer - Playbook

## Flusso operativo

1. Ricevi YouTube URL dal yt-seo-publisher
2. Chiama YouTube Analytics API per CTR, retention, views, engagement
3. Analizza pattern (titolo, thumbnail, hook, durata)
4. Confronta con benchmark del canale
5. Aggiorna ReasoningBank con insight
6. Genera `performance-report.json`
7. Memory checkpoint
8. Handoff al department-lead

## Esempi
- Happy: video con CTR > 8% → pattern salvato nel ReasoningBank
- Edge: retention bassa al minuto 3 → proposta di migliorare hook

## Handoff
Al department-lead con report + ReasoningBank update.