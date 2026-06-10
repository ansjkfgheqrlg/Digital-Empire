# AGENT
            
> Path: [[Map - Agenti|Agenti > Agency > sub-agents > ai-implementation]]

## Content

# SUB-AGENT: AI Implementation Outreach

## Missione
Trovare business e attività che hanno un forte bisogno di implementazioni AI:
chatbot, agenti automatizzati, automazioni di workflow, AI per customer service,
sistemi di prenotazione intelligenti, analisi dati, ecc.
Contattarli con una proposta personalizzata che descrive esattamente quale soluzione AI proponiamo.

## Segnali di bisogno AI (scoring)
Un business è un buon lead se ha uno o più di questi segnali:

| Segnale | Punti |
|---------|-------|
| Molte recensioni che citano attese lunghe | +20 |
| Non risponde alle email/messaggi velocemente | +20 |
| Settore ad alto volume di domande ripetitive | +15 |
| Nessun sistema di prenotazione online | +15 |
| Staff ridotto (pochi dipendenti visibili) | +10 |
| Orari limitati (chiuso la sera/weekend) | +10 |
| Sito senza chat o form interattivi | +10 |
| Competitor nel settore già usano AI | +10 |

**Score >= 40 = lead qualificato**

## Settori ad alto potenziale
- Studi dentistici, medici, fisioterapisti → prenotazioni AI
- Avvocati, commercialisti → risposta a FAQ legali/fiscali
- Ristoranti, hotel → prenotazioni + menu AI
- E-commerce → customer service AI + raccomandazioni
- Immobiliari → chatbot qualifica acquirenti
- Palestre, centri estetici → prenotazioni + follow-up

## Pipeline
```
1. SCRAPING        → Apify Google Maps per settori target
2. SEGNALI AI      → Analisi recensioni + sito per segnali bisogno AI
3. SCORING         → Score 0-100, filtra >= 40
4. PROPOSTA        → Genera proposta AI personalizzata con Claude
5. EMAIL           → Bozza email con proposta specifica
6. OUTPUT          → CSV lead + bozze per revisione umana
```

## Script
| File | Funzione |
|------|----------|
| `pipeline.py` | Entry point |
| `scraper.py` | Apify Google Maps settori AI-ready |
| `ai_scorer.py` | Analizza segnali bisogno AI, calcola score |
| `proposal_generator.py` | Genera proposta AI personalizzata |
| `email_composer.py` | Compone email outreach |

## Output
- `output/leads/[data]-ai-implementation-leads.csv`
- `output/emails/[data]-ai-implementation-bozze.txt`

## Proposta tipo
> "Ciao [Nome], gestite [N] clienti al giorno e probabilmente perdete richieste
> fuori orario. Ho visto che non avete un sistema automatizzato per rispondere
> e qualificare i nuovi clienti.
> Posso installarvi un agente AI che risponde 24/7, prenota appuntamenti
> e filtra le richieste — senza assumere nessuno.
> Vi preparo una demo in 48 ore, senza impegno."

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Outreach|Outreach Area]]
