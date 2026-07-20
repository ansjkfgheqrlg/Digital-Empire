# yt-competitor-scout — Specification

## Identity
**Agent ID:** yt-competitor-scout  
**Category:** Research & Analysis  
**Level:** L2  
**Type:** Intelligence Gathering Agent

## Mission
Scovare e analizzare i competitor YouTube nella nicchia target, identificando:
- Canali competitor (subscriber count, upload frequency, engagement rate)
- Video top-performing (views, retention, comments)
- Strategie di contenuto (formati, durata, hook, CTA)
- Gap di mercato (opportunità non coperte)
- Best practices del settore

## Input
- **nicchia**: string (es. "Claude Code", "AI coding", "programming tutorials")
- **keyword_opzionale**: string (es. "tutorial italiano", "beginner guide")
- **numero_canali**: int (default: 10)
- **numero_video**: int per canale (default: 5)

## Output
```json
{
  "nicchia": "Claude Code",
  "data_analisi": "2026-07-20",
  "competitor": [
    {
      "canale": "Nome Canale",
      "subscriber": 50000,
      "video_totali": 200,
      "upload_frequency": "2/settimana",
      "engagement_rate": 0.05,
      "top_video": [
        {
          "titolo": "Titolo Video",
          "views": 100000,
          "durata": "10:30",
          "published": "2026-06-15",
          "hook": "In questo video ti mostro...",
          "cta": "Iscriviti per altri tutorial",
          "keywords": ["claude code", "ai coding"]
        }
      ],
      "strategie": ["tutorial step-by-step", "code-along", "project-based"],
      "punti_debolezza": ["audio basso", "niente sottotitoli"]
    }
  ],
  "gap_mercato": [
    "Tutorial in italiano per beginner",
    "Confronto Claude Code vs GitHub Copilot",
    "Project-based learning"
  ],
  "best_practices": [
    "Hook nei primi 15 secondi",
    "CTA chiara alla fine",
    "Thumbnail con testo grande",
    "Durata ottimale 8-12 minuti"
  ],
  "opportunita": [
    "Primo canale italiano su Claude Code",
    "Serie 'Zero to Hero'",
    "Confronti diretti con competitor"
  ]
}
```

## Tools Required
- YouTube Data API v3 (search, channels, videos)
- Web scraping (opzionale per dati extra)
- Memory Manager (checkpoint, decision recording)

## Activation
```
/yt-competitor-scout --nicchia="Claude Code" --canali=10 --video=5
```

## Constraints
- Rate limit YouTube API: 10,000 units/day
- Max 10 canali per run (evitare timeout)
- Solo canali con >1000 subscriber (qualità)
- Solo video con >1000 views (relevance)

## Success Criteria
- Report completo con ≥5 competitor analizzati
- Almeno 3 gap di mercato identificati
- Almeno 5 best practices documentate
- Almeno 3 opportunità concrete suggerite
- Tempo esecuzione: <15 minuti

## Error Handling
- API quota exceeded → warning + parziale report
- Nessun competitor trovato → suggerire nicchie alternative
- Timeout → retry automatico (max 3 tentativi)

## Memory Integration
- Ogni run crea CP (checkpoint)
- Decisioni importanti registrate come DEC
- Dati competitor salvati in knowledge/competitors/
- Aggiornamento MEMORY-INDEX.md dopo ogni run
