# AGENT
            
> Path: [[Map - Agenti|Agenti > Agency > sub-agents > no-website]]

## Content

# SUB-AGENT: No-Website Outreach

## Missione
Trovare business locali che NON hanno un sito web, qualificarli e contattarli via email o SMS con una proposta personalizzata per creare la loro presenza online.

## Pipeline

```
1. SCRAPING        → Apify Google Maps → lista business
2. FILTRAGGIO      → tieni solo quelli senza sito web
3. QUALIFICA       → score 0-100 (rating, recensioni, contatto)
4. ESTRAZIONE      → cerca email/telefono dal web
5. GENERAZIONE     → bozza email/SMS personalizzata con Claude
6. OUTPUT          → CSV lead + bozze per revisione umana
```

## Script
| File | Funzione |
|------|----------|
| `pipeline.py` | Entry point, coordina tutti gli step |
| `scraper.py` | Apify Google Maps, filtra no-website |
| `qualifier.py` | Score lead, fascia A/B/C |
| `contact_finder.py` | Cerca email e telefono |
| `message_generator.py` | Genera email + SMS con Claude API |

## Regole
- Lead salvato SOLO se ha email valida
- SMS generato solo se c'è numero di telefono
- Mai inviare automaticamente — sempre revisione umana
- Max 20 messaggi per run

## Output
- `output/leads/[data]-no-website-leads.csv`
- `output/emails/[data]-no-website-bozze.txt`

## Proposta tipo (no-website)
> "Ciao [Nome], ho notato che [Business] non ha un sito web.
> I tuoi competitor [X] e [Y] ne hanno uno e ricevono clienti ogni giorno da Google.
> Posso crearti un sito professionale in 7 giorni, ottimizzato per la tua zona.
> Possiamo parlarne 10 minuti questa settimana?"

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - Outreach|Outreach Area]]
