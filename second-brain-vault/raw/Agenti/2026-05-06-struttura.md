# struttura

> Source: File system (`Agenti\struttura.md`)
> Collected: 2026-05-06
> Published: Unknown

Struttura finale Agency/

Agency/
├── orchestrator/              ← PUNTO DI INGRESSO
│   ├── AGENT.md               Logica decisionale
│   └── run.py                 CLI: python run.py --pipeline [tipo]
│
├── sub-agents/                ← 3 NUOVI SUB-AGENTI
│   ├── no-website/            Siti web → email/SMS
│   │   ├── AGENT.md, pipeline.py, scraper.py
│   │   ├── qualifier.py, contact_finder.py
│   │   └── message_generator.py
│   │
│   ├── cro-funnel/            Audit completo → PDF → email
│   │   ├── AGENT.md, pipeline.py, scraper.py
│   │   ├── site_analyzer.py, market_runner.py
│   │   ├── pdf_generator.py, email_composer.py
│   │
│   └── ai-implementation/     Trova bisogno AI → proposta
│       ├── AGENT.md, pipeline.py, scraper.py
│       ├── ai_scorer.py, proposal_generator.py
│
├── outreach/                  ← Agente esistente importato
├── agents/                    ← 5 market agents
├── skills/                    ← 15 market skills
├── templates/                 ← Template email/content
├── requirements.txt
└── .env.example

## Come usarlo

# Installa dipendenze
pip install -r Agency/requirements.txt

# Pipeline singola
python Agency/orchestrator/run.py --pipeline no-website --citta "Milano" --settore "ristoranti"
python Agency/orchestrator/run.py --pipeline cro-funnel --citta "Roma" --settore "dentisti"
python Agency/orchestrator/run.py --pipeline ai-implementation --citta "Napoli" --settore "avvocati"

# Tutte e 3 in sequenza
python Agency/orchestrator/run.py --pipeline full --citta "Torino" --settore "commercialisti"







Comando + Url = Task 
/market audit <url>	= Full marketing audit with 5 parallel agents
/market quick <url>	= 60-second marketing snapshot
/market copy <url>	= Generate optimized copy with before/after examples
/market emails <topic>	= Generate complete email sequences
/market social <topic>	= 30-day social media content calendar
/market ads <url>	= Ad creative and copy for all platforms
/market funnel <url>	= Sales funnel analysis and optimization
/market competitors <url>	= Competitive intelligence report
/market landing <url>	= Landing page CRO analysis
/market launch <product>	= Product launch playbook
/market proposal <client>	= Client proposal generator
/market report <url>	= Full marketing report (Markdown)
/market report-pdf <url>	= Professional marketing report (PDF)
/market seo <url>	= SEO content audit
/market brand <url>	= Brand voice analysis and guidelines
