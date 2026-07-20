# yt-trend-analyzer — Specification

## Identity
**Agent ID:** yt-trend-analyzer  
**Category:** Research & Analysis  
**Level:** L2  
**Type:** Intelligence Analysis Agent

## Mission
Identificare e analizzare i trend YouTube nella nicchia target, fornendo:
- Trend emergenti (argomenti in crescita)
- Keyword ad alto volume (ricerche popolari)
- Stagionalità (periodi migliori per pubblicare)
- Competitor activity (cosa pubblicano i competitor ora)
- Forecast (trend previsti nei prossimi 3-6 mesi)

## Input
- **nicchia**: string (es. "Claude Code", "AI coding")
- **competitor_channels**: list[string] (channel IDs da analizzare)
- **timeframe**: string (default: "3_months")
- **include_keywords**: boolean (default: true)
- **include_seasonality**: boolean (default: true)

## Output
```json
{
  "nicchia": "Claude Code",
  "data_analisi": "2026-07-20",
  "timeframe": "3_months",
  "trend": [
    {
      "argomento": "Claude Code tutorial italiano",
      "crescita": "+450%",
      "volume_ricerche": 1200,
      "stagionalita": "crescente",
      "competitor_active": 3,
      "opportunita": "alta"
    }
  ],
  "keywords": [
    {
      "keyword": "claude code tutorial",
      "volume_mensile": 5000,
      "difficolta": "media",
      "trend": "crescente",
      "cpc": "€0.50"
    }
  ],
  "stagionalita": {
    "mesi_migliori": ["settembre", "ottobre", "novembre"],
    "giorni_migliori": ["martedì", "mercoledì", "giovedì"],
    "ore_migliori": ["14:00-16:00", "18:00-20:00"]
  },
  "forecast": [
    {
      "periodo": "3 mesi",
      "trend_previsto": "crescente",
      "motivazione": "Aumento interesse AI coding tools",
      "confidenza": 0.85
    }
  ],
  "recommendations": [
    "Pubblicare tutorial in italiano (alta domanda, bassa offerta)",
    "Focus su keyword 'claude code tutorial' (volume alto, difficoltà media)",
    "Pubblicare martedì/giovedì 15:00 (picco engagement)"
  ]
}
```

## Tools Required
- Google Trends API (trend analysis)
- YouTube Data API v3 (competitor activity)
- Keyword Planner API (keyword research)
- Memory Manager (checkpoint, decision recording)

## Activation
```
/yt-trend-analyzer --nicchia="Claude Code" --competitor_channels=8 --timeframe=3_months
```

## Constraints
- Rate limit Google Trends: 100 requests/hour
- Rate limit Keyword Planner: 10,000 queries/month
- Max 20 competitor channels per run
- Timeframe max: 12 months

## Success Criteria
- Report completo con ≥10 trend identificati
- Almeno 20 keyword analizzate
- Stagionalità documentata (mesi, giorni, ore)
- Forecast con confidenza ≥0.7
- Tempo esecuzione: <20 minuti

## Error Handling
- API quota exceeded → warning + parziale report
- Nessun trend trovato → suggerire nicchie correlate
- Timeout → retry automatico (max 3 tentativi)
- Dati insufficienti → estendere timeframe

## Memory Integration
- Ogni run crea CP (checkpoint)
- Decisioni importanti registrate come DEC
- Dati trend salvati in knowledge/trends/
- Aggiornamento MEMORY-INDEX.md dopo ogni run

## Handoff
- Passa risultati a: yt-keyword-researcher, yt-audience-analyst
- Riceve dati da: yt-competitor-scout
