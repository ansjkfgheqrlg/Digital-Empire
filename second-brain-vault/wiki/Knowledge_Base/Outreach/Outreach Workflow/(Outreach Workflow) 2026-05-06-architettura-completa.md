# ARCHITETTURA_COMPLETA
            
> Path: [[Map - Outreach|Outreach > Outreach Workflow]]

## Content

# Outreach Automatico v2.0 — Architettura Completa
**Digital Empire | 300 email/giorno | $0/giorno (tutto NVIDIA Nemotron gratuito)**

---

## Stack Tecnologico

| Componente | Tecnologia | Costo |
|-----------|-----------|-------|
| Fonte lead | Facebook Ad Library API ufficiale | Gratuita |
| Estrazione email | BeautifulSoup + lxml (scraping siti) | Gratuita |
| AI (tutti gli agenti) | NVIDIA Nemotron via OpenRouter | $0/giorno |
| Database deduplicazione | SQLite locale | Gratuita |
| Invio email | Gmail SMTP | Gratuita |
| **TOTALE** | | **$0/giorno** |

**Modello AI**: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
**Fallback**: `meta-llama/llama-3.3-70b-instruct:free`
**Client Python**: OpenAI SDK con `base_url="https://openrouter.ai/api/v1"`

---

## Struttura File

```
Outreach Workflow/
├── run.py                    # Entry point — lancia tutto
├── test_pipeline.py          # Test email con lead finti (senza FB)
├── 1_SETUP.bat               # Installa dipendenze + test iniziale
├── 2_AVVIA.bat               # Lancio produzione giornaliero
├── 3_TEST_EMAIL.bat          # Test qualita' email
├── .env                      # Credenziali (OpenRouter, FB, Gmail)
├── requirements.txt          # openai, requests, beautifulsoup4, lxml, dotenv
│
├── knowledge/                # BASE DI CONOSCENZA COPY (il "cervello" del sistema)
│   ├── apsoc.py              # Framework APSOC + Templates A/B/C + CPB + DR
│   ├── brand_voice.py        # Tono DE + Andrei Pascu benchmark + vocab
│   └── copy_training.py      # 30+ esempi email, anti-esempi, regole settore
│
├── agents/
│   ├── scraper.py            # Team 1: Facebook Ad Library scraper
│   ├── extractor.py          # Team 1: estrae email dai siti web
│   ├── qualifier.py          # Team 1: score lead 0-100 + template A/B/C
│   ├── copy_knowledge.py     # Team 2: prepara briefing pack copy
│   ├── strategist.py         # Team 3: genera strategy brief
│   ├── writer.py             # Team 4: scrive email APSOC-powered
│   ├── humanizer.py          # Team 5: QA 3-check + revision loop
│   ├── sender.py             # Team 6: invio Gmail SMTP
│   └── orchestrator.py       # Coordinatore: lancia i 6 team in sequenza
│
└── output/
    └── leads.db              # SQLite — storico email inviate (deduplicazione)
```

---

## Flusso Completo End-to-End

```
python run.py --target 300
       │
       ├── [FASE 1] TEAM 1 — INTELLIGENCE
       │    ├── ScraperAgent       → 660 business da Facebook Ads (2× buffer)
       │    ├── ExtractorAgent     → ~400 con email estratta dal sito
       │    └── QualifierAgent     → Score 0-100 + template A/B/C (scarta < 40)
       │
       ├── SQLite dedup           → rimuove email gia' contattate in precedenza
       │
       ├── [FASE 2] TEAM 2 — COPY KNOWLEDGE
       │    └── CopyKnowledgeAgent → briefing pack per ogni lead:
       │                             esempi email approvati per settore
       │                             anti-esempio con spiegazione
       │                             regole specifiche per template+settore
       │                             statistiche di settore credibili
       │                             apertura personalizzata (oggetto + prima riga)
       │
       ├── [FASE 3] TEAM 3 — STRATEGY
       │    └── StrategistAgent    → brief 80 parole per ogni lead:
       │                             hook_angle (come aprire)
       │                             problema_da_amplificare (con impatto)
       │                             angolo_soluzione (come presentare)
       │                             nota_tono (calibrazione settore)
       │
       ├── [FASE 4+5] TEAM 4+5 — COPY + QA (loop per ogni lead)
       │    ├── EmailWriterAgent   → email APSOC completa (max 130 parole)
       │    │                        oggetto + oggetto_b + oggetto_c (A/B/C test)
       │    └── HumanizerAgent     → 3 check in sequenza:
       │         ├── Check 1: HumannessChecker (score 1-10)
       │         ├── Check 2: DirectResponseReviewer — APSOC compliance (score 1-10)
       │         └── Check 3: BrandValidator — tono Andrei Pascu (score 1-10)
       │              Media >= 7 → APPROVATA → coda invio
       │              Media < 7  → feedback specifico → 1 revisione writer
       │                           → secondo QA → se passa: invio
       │                                        → se fallisce: SCARTATA
       │
       ├── [FASE 6] TEAM 6 — DELIVERY
       │    ├── SenderAgent        → max 300 email via Gmail SMTP
       │    └── SQLite tracker     → salva ogni email inviata (deduplicazione)
       │
       └── Report qualita' finale
            % passate al 1° tentativo
            % revisionate e passate
            % scartate (doppio fail QA)
            QA score medio
            distribuzione template A/B/C
```

---

## TEAM 1 — INTELLIGENCE

### ScraperAgent (`agents/scraper.py`)
**Fonte**: Facebook Ad Library API v21.0 (gratuita, ufficiale)
**Logica**: itera su 20 settori × 25 città italiane
**Output**: `{page_id, page_name, website, settore, citta}`

**Settori cercati**: dentista, palestra, ristorante, avvocato, fisioterapista, parrucchiere, estetista, agenzie immobiliari, meccanico, hotel, psicologo, nutrizionista, centro estetico, consulente finanziario, personal trainer, fotografo, architetto, commercialista, assicurazioni, clinica veterinaria

**Città**: Milano, Roma, Napoli, Torino, Bologna, Firenze, Palermo, Bari, Venezia, Catania, Genova, Verona, Padova, Brescia, Bergamo, Parma, Modena, Reggio Emilia, Perugia, Trieste, Taranto, Messina, Prato, Reggio Calabria, Cagliari

**Rate limit**: delay 1.5s tra query, 0.4s tra richieste pagina
**Gestione errori**: token scaduto (codice FB 190), rate limit (codice 429 → sleep 60s)

**IMPORTANTE**: Il token FB scade ogni 60 giorni. Rinnovalo su:
`developers.facebook.com/tools/explorer` → permesso `ads_read` → "Extend Access Token"

---

### ExtractorAgent (`agents/extractor.py`)
**Fonte**: scraping siti web (BeautifulSoup + lxml)
**Input**: lista business con website
**Output**: lead con campo `email` aggiunto
**Logica**: cerca email nel HTML della homepage + pagina `/contatti` + footer
**Timeout**: 10s per sito

---

### QualifierAgent (`agents/qualifier.py`)
**Modello**: NVIDIA Nemotron
**Input**: lead con nome, settore, citta, website, email
**Output**: lead con score(0-100) + template(A/B/C) + pain_point + key_observation + settore_calibrato

**Sistema di scoring**:
- 80-100 (Hot): lead ideale, problema identificabile, alto potenziale → 3 tentativi di invio
- 60-79 (Warm): buon lead, problema probabile
- 40-59 (Tiepido): lead mediocre, contattare se non di meglio
- 0-39 (Cold): scartato → non viene processato

**Logica template**:
- **Template A**: business senza sito (perde clienti su Google)
- **Template B**: business con FB Ads ma funnel/landing page scarsa
- **Template C**: azienda strutturata con processi manuali da automatizzare

**Boost score**: dentista, legale, immobiliare, e-commerce, SaaS, chi fa ads
**Penalità**: pubblica amministrazione, multinazionali, solo 1 persona

---

## TEAM 2 — COPY KNOWLEDGE (`agents/copy_knowledge.py`)

**Modello**: NVIDIA Nemotron (parte deterministica: Python puro)
**Scopo**: compensare la minore qualità creativa di NVIDIA rispetto a Sonnet con una knowledge base estesa

**Output `copy_briefing_pack`**:
```
{
  esempi_approvati:   2 email approvate rilevanti per template+settore
  anti_esempio:       1 email sbagliata con spiegazione dettagliata
  regole_settore:     5 regole specifiche per questo settore
  statistiche:        2 statistiche credibili da usare nell'email
  apertura_suggerita: {oggetto, prima_riga} personalizzata per questo lead
  tono_settore:       calibrazione tono specifica per il settore
  template_structure: struttura completa del template A/B/C
  checklist_qualita:  10 domande di verifica qualita'
}
```

**Selezione esempi**: prima cerca per settore specifico, poi template generico
**Personalizzazione apertura**: NVIDIA genera oggetto + prima riga specifica per il lead

---

## KNOWLEDGE BASE (`knowledge/`)

### `knowledge/apsoc.py` — Framework Copy
- **APSOC_FULL_FRAMEWORK**: A(Attenzione) P(Problema) S(Soluzione) P(Proof) O(Obiezione) C(CTA) — regole complete
- **TEMPLATE_A**: struttura per business senza sito — angolo loss aversion
- **TEMPLATE_B**: struttura per business con ads + funnel scarso — angolo ROI
- **TEMPLATE_C**: struttura per AI implementation — angolo efficienza operativa
- **CPB_FRAMEWORK**: Claim→Proof→Benefit — ogni affermazione va ancorata
- **DR_PRINCIPLES**: Loss aversion > Gain framing, Specificity, Curiosity gap, One CTA
- **PROHIBITED_PHRASES**: 30+ frasi vietate (es: "Spero che stia bene", "soluzioni innovative")
- **APPROVED_OPENERS**: pattern di apertura approvati (osservazione specifica)

### `knowledge/brand_voice.py` — Tono e Voce
- **SENDER_IDENTITY**: "Max Ricci, consulente DE" — persona del mittente
- **ANDREI_PASCU_BENCHMARK**: benchmark tono (diretto, numeri reali, peer-to-peer, brevità densa)
- **BRAND_VOICE_GUIDELINES**: regole de brand voice DE
- **APPROVED_VOCABULARY**: parole approvate per settore
- **BANNED_VOCABULARY**: 30+ termini vietati (eccellente, garantito, sinergie, ROI...)
- **QUALITY_CHECKLIST**: 10 domande pre-approvazione email
- **SECTOR_TONE_CALIBRATION**: calibrazione tono per 8 settori:
  - ristorante_bar_cafe, palestra_fitness, dentista_medico, e-commerce
  - avvocato_notaio, agenzia_immobiliare, artigiano_idraulico_elettricista, consulente_coach

### `knowledge/copy_training.py` — Esempi e Formazione
- **TEMPLATE_A_APPROVED_EXAMPLES**: 5 email approvate per business senza sito
- **TEMPLATE_B_APPROVED_EXAMPLES**: 5 email approvate per business con ads scarsi
- **TEMPLATE_C_APPROVED_EXAMPLES**: 4 email approvate per AI implementation
- **ANTI_EXAMPLES**: 6 email sbagliate con spiegazione del problema
- **SECTOR_MICRO_RULES**: regole specifiche per 8 settori + default
- **SUBJECT_LINE_FORMULAS**: formule oggetto per template A/B/C
- **REVISION_PRINCIPLES**: come correggere email rifiutate dal QA
- **SECTOR_STATISTICS**: statistiche credibili da usare (conversioni mobile, velocita' pagina, ecc.)

---

## TEAM 3 — STRATEGY (`agents/strategist.py`)

**Modello**: NVIDIA Nemotron
**Input**: lead qualificato con template + pain_point + key_observation
**Output `strategy_brief`** (max 80 parole totali):
```
{
  hook_angle:              "come aprire — osservazione specifica (max 25 parole)"
  problema_da_amplificare: "problema con impatto quantificato (max 25 parole)"
  angolo_soluzione:        "come presentare la soluzione (max 20 parole)"
  nota_tono:               "calibrazione specifica per settore (max 15 parole)"
}
```

**Scopo**: fornire al writer esattamente cosa fare — il writer non ragiona, esegue il brief

---

## TEAM 4 — COPY (`agents/writer.py`)

**Modello**: NVIDIA Nemotron
**Input**: lead + copy_briefing_pack + strategy_brief (+ feedback_revisione se revisione)

**System prompt include** (costruito dinamicamente da knowledge base):
- Identita' Max Ricci
- Framework APSOC completo
- CPB framework
- Direct Response principles
- Andrei Pascu benchmark
- Brand voice guidelines
- 20 frasi vietate
- 6 pattern apertura approvati
- 10 domande checklist qualita'
- Il template specifico (A o B o C)
- Gli esempi approvati per questo settore
- L'anti-esempio con spiegazione
- Le regole specifiche del settore

**Output JSON**:
```json
{
  "oggetto":   "oggetto principale (max 8 parole)",
  "oggetto_b": "variante B oggetto (A/B test)",
  "oggetto_c": "variante C oggetto (A/B test)",
  "corpo":     "email completa APSOC (max 130 parole)"
}
```

**Revision mode**: se QA rifiuta, il writer riceve `feedback_revisione` (stringa con i problemi specifici) e riscrive — max 1 tentativo

---

## TEAM 5 — HUMAN VOICE QA (`agents/humanizer.py`)

**Modello**: NVIDIA Nemotron
**Input**: lead con email_bozza
**Output**: lead con qa_approved(bool) + qa_score_media(float) + qa_feedback(str)

### Check 1 — HumannessChecker (score 1-10)
Pattern che abbassano:
- Frasi formali: "Spero che stia bene", "Mi permetto di contattarla"
- Autodescrizionali: "Mi chiamo X e lavoro in Y"
- Corporate jargon: "sinergie", "trasformazione digitale"
- Aggettivi vuoti: "eccellente", "straordinario", "leader"
- Struttura rigida template

Pattern che alzano:
- Apertura con osservazione specifica e concreta
- Uso naturale del "tu/voi" diretto
- Frasi brevi e dirette
- Tono da collega esperto
- Specificità con numeri credibili
- Una sola domanda finale

### Check 2 — DirectResponseReviewer (score 1-10)
Verifica compliance APSOC:
- A: prima riga specifica al business?
- P: problema quantificato?
- S: soluzione credibile e collegata al problema?
- P: riferimento settoriale come social proof?
- O: obiezione anticipata?
- C: UNA SOLA CTA morbida?

Penalita' automatiche: >1 CTA (-3), nessuna specificita' prima riga (-2), corpo >150 parole (-2)

### Check 3 — BrandValidator (score 1-10)
Confronto con Andrei Pascu:
- Arriva al punto nella prima riga? (+2)
- Usa numeri reali? (+2)
- Tono confident senza arroganza? (+2)
- Brevita' densa, zero filler? (+2)
- Peer-to-peer? (+2)

### Pre-check deterministici (Python puro, gratuito)
Prima dei check AI:
- Lista 30+ frasi vietate → ricerca esatta nel testo
- Lista termini corporate banditi
- Conteggio parole (soglia: 150 parole)

### Decisione finale
```
Media >= 7.0 → APPROVATA → passa al sender
Media < 7.0  → RIFIUTATA → feedback al writer → 1 revisione
               → secondo check → se >= 7: APPROVATA
                               → se < 7:  SCARTATA (non inviare)
```
**Tasso di scarto atteso**: < 5%

---

## TEAM 6 — DELIVERY (`agents/sender.py`)

**Protocollo**: Gmail SMTP (porta 587, TLS)
**Max per batch**: 300 email/giorno (limite sicuro Gmail free)
**Delay**: 2-4 secondi tra email (evita spam detection)
**Tracking**: salva ogni email inviata su SQLite

---

## ORCHESTRATORE (`agents/orchestrator.py`)

Coordina i 6 team. Stampa header visivi per ogni fase:
```
╔══ FASE 1/6 — INTELLIGENCE ══════════════════════════════════╗
```

Traccia metriche di qualita' durante il run:
- qa_passed_first, qa_passed_after_revision, qa_rejected
- qa_score_medio, template_distribution

Report finale con % per ogni metrica.

---

## SQLite — Deduplicazione

File: `output/leads.db`
Tabella: `leads_contattati`
Campi: page_id, email(UNIQUE), page_name, settore, citta, website, template, score, oggetto, qa_score, stato, data

**Logica**: prima di processare ogni lead, controlla se l'email esiste gia' nel DB.
Se esiste → salta. Se non esiste → processa.
Questo garantisce che lo stesso business non venga mai contattato due volte.

---

## Configurazione `.env`

```
OPENROUTER_API_KEY=sk-or-v1-...   # OpenRouter (NVIDIA free) — gia' configurata
FB_ACCESS_TOKEN=EAANx...          # Token Facebook — SCADE OGNI 60 GIORNI
GMAIL_USER=max.infoproducer@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx   # App Password 16 caratteri
```

---

## Come Usare

| Azione | Comando |
|--------|---------|
| Setup iniziale (una volta) | Doppio click su `1_SETUP.bat` |
| Lancio giornaliero produzione | Doppio click su `2_AVVIA.bat` |
| Test qualita' email | Doppio click su `3_TEST_EMAIL.bat` |
| Test 10 email senza invio | `python run.py --target 10 --anteprima` |
| Produzione 300 email | `python run.py` |

---

## Decisioni Architetturali Chiave

1. **NVIDIA invece di Sonnet**: Claude Pro (web) non copre le API Python. NVIDIA Nemotron via OpenRouter e' gratuito.
2. **Knowledge base come compensazione**: 3 file knowledge (apsoc.py, brand_voice.py, copy_training.py) compensano la minore qualita' creativa di NVIDIA rispetto a Sonnet.
3. **6 team invece di 1 agente**: ogni team ha un ruolo specializzato. Il feedback specifico (humanizer→writer) e' possibile solo con team separati.
4. **Max 300 email/giorno**: Gmail free limit e' 500, ma 300 e' il sweet spot sicuro per la reputazione del dominio.
5. **Andrei Pascu benchmark**: tono di riferimento — diretto, numeri reali, peer-to-peer, breve.
6. **3 template fissi**: A (no sito), B (ads+funnel scarso), C (AI implementation) — coprono 95% dei business italiani raggiungibili.
7. **FB Ad Library API**: sostituisce Apify ($50-200/mese) con l'API ufficiale gratuita.

*Documento generato automaticamente — Ultima versione: 2026-05-04*

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Prove|Prove Area]]
- [[Map - Saas|Saas Area]]
