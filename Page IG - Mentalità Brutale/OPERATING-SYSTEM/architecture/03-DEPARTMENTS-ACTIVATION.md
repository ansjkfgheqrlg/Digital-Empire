# SOCIAL EMPIRE — attivazione reparti per Mentalità Brutale

## Principio

“Attivare tutti i reparti” non significa duplicare decine di agenti in una cartella nuova. Significa assegnare owner, controllore, input, output, SLA e gate alle capability già costruite in EMPIRE OS.

## Catena di comando

```text
MAX / Board
  └─ Social Empire Director (tenant MB, 05-MB)
      ├─ D1 Intelligence & Competitor Research
      ├─ D2 Strategy & Growth
      ├─ D3 Editorial Planning
      ├─ D4 Copy & Reel Scripts
      ├─ D5 Carousel & Visual
      ├─ D6 Video Production
      ├─ D7 QA & Compliance (indipendente)
      ├─ D8 Authorization, Publishing & SRE
      ├─ D9 Analytics & Learning
      ├─ D10 Community & Reputation
      └─ D11 Revenue & Funnel

Capability gap → Chief-Forge → ARCHITETTURA → FORGE → eval → registro → reparto
```

## Roster operativo/RACI

| ID | Reparto | Owner Empire esistente | Output contrattuale | Controllore |
|---|---|---|---|---|
| D0 | Social Director | 05-MB + CF-R0 | ordine, priorità, P&L, stop/go | CEO/CFO |
| D1 | Intelligence | 08-INTELLIGENCE / Empire Studio | evidence pack, competitor matrix, transcript+frame refs | Verification & Control |
| D2 | Strategy & Growth | CF-R1 + 04-MKT Strategia | ipotesi, pilastri, experiment id | CMO/Analytics |
| D3 | Editorial | CF-R1 Calendar | calendario 28d bilanciato | Social Director |
| D4 | Copy & Script | CF-R4 + 04-MKT Copy | caption/script con claim ledger | CF-R6 Copy |
| D5 | Visual/Carousel | CF-R5 / `carousel-factory` | slide + manifest | CF-R6 Format/Brand |
| D6 | Video | CF-R3 | master Reel + subtitles + rights | CF-R6 Format/Safety |
| D7 | QA & Compliance | **CF-R6 indipendente** | 5 verdict PASS/FAIL | L1 Post-Production |
| D8 | Auth/Publish/SRE | CF-R7 + 09-OPERATIONS | token health, staging, publish, permalink, alert | Security + CF-R7-QA |
| D9 | Analytics/Learning | CF-R8 + 04-MKT Analytics | snapshot 48h/7d, pattern n≥3 | CF-R8-QA |
| D10 | Community | 04-MKT Community (fase 2) | triage commenti/DM, escalation reputazione | Safety/Human for sensitive cases |
| D11 | Revenue/Funnel | 05-MB + 02-INFO/04-MKT | CTA, UTM, lead/revenue attribution | CRO/CFO |

## Handoff standard

Ogni handoff contiene:

```json
{
  "run_id": "MB-RUN-...",
  "content_id": "MB-...",
  "from": "D4",
  "to": "D7",
  "input_refs": ["path/immutabile"],
  "output_ref": "path/immutabile",
  "gate": "PASS|FAIL|PENDING",
  "evidence": [{"source": "...", "locator": "timestamp/frame/line"}],
  "ts": "ISO-8601 UTC"
}
```

## Quando Chief-Forge costruisce qualcosa

Chief-Forge riceve un capability gap solo se almeno una condizione è vera:

1. lo stesso failure si ripete ≥3 volte;
2. un workflow non ha owner o gate;
3. un compito manuale ricorrente supera 30 minuti/settimana;
4. un nuovo formato/canale non è coperto;
5. l'eval della skill scende sotto soglia;
6. una fonte integrale contiene regole riusabili non presenti nel portfolio.

Prima cerca nel portfolio. Se esiste, **migliora/estende**; non crea un duplicato.

## Coda FORGE iniziale

| Priorità | Capability | Forma minima | Trigger build |
|---|---|---|---|
| P0 | `mentalita-brutale-operator` | skill project-level | costruita in questa fase |
| P0 | Meta API publisher | runtime deterministico | costruito in questa fase |
| P1 | Reel Pattern Extractor | skill + evidence schema | dopo ingestione di almeno 10 Reel veri |
| P1 | Reel Script Engine | skill | dopo Pattern Extractor + 3 pattern validati |
| P1 | Visual QA OCR/contrast | tool | quando il gate manuale produce ≥3 rework |
| P2 | Community Triage | workflow | dopo permission comments/messages + policy escalation |
| P2 | Funnel Attribution | workflow | quando esiste una destinazione link-in-bio approvata |

## Ritmo operativo

- **Settimanale:** lunedì batch planning; produzione in parallelo; QA entro venerdì; scheduler 7 giorni.
- **Giornaliero:** 09:00 token/scheduler health; publish slot; post-check; alert solo per eccezioni.
- **+48h/+7d:** metric snapshots (Meta può ritardare fino a 48h).
- **Domenica:** CF-R8 distilla pattern; D2 modifica una sola variabile primaria per il ciclo seguente.
- **Mensile:** Chief-Forge capability audit + Security secret/token audit + P&L review.
