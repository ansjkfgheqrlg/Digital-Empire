# 03_qualifica_lead
            
> Path: [[Map - Agenti|Agenti > Agency > outreach > rules]]

## Content

# REGOLA 03 — Qualifica e Scoring Lead

## OBIETTIVO
Analizzare i lead grezzi trovati da WF-A e WF-B, arricchirli con dati aggiuntivi, calcolare un punteggio di priorità finale e ordinarli per massimizzare il tasso di conversione dell'outreach.

## TRIGGER
- Automatico: eseguito al termine di WF-A o WF-B
- Manuale: quando si vuole riqualificare lead già presenti nel foglio

## INPUT

| Campo | Obbligatorio | Tipo | Descrizione |
|-------|-------------|------|-------------|
| `source` | Sì | stringa | `"no_sito"`, `"funnel_scarso"` o `"ai_prospect"` |
| `sheet_tab` | No | stringa | Tab Google Sheets da processare (default: tutti i nuovi) |
| `solo_nuovi` | No (default: True) | bool | Se True, processa solo lead con `STATO_OUTREACH = "nuovo"` |

## OUTPUT
- Colonne aggiornate nel foglio Google Sheets: `SCORE_PRIORITÀ`, `FASCIA`, `PRONTO_OUTREACH`
- Log in `logs/YYYY-MM-DD_WF-C_qualifica.log`

### Colonne aggiunte/aggiornate:

| Colonna | Descrizione | Valori |
|---------|-------------|--------|
| `SCORE_PRIORITÀ` | Punteggio finale 0-100 | intero |
| `FASCIA` | Classificazione | `A` / `B` / `C` |
| `PRONTO_OUTREACH` | Pronto per email? | `Sì` / `No` |
| `MOTIVO_ESCLUSIONE` | Perché non è pronto | stringa o vuoto |

---

## STEP-BY-STEP

### Step 1 — Leggi lead da Google Sheets
1. Apri tab appropriato (`Lead_NoSito` o `Lead_FunnelScarso`)
2. Carica righe con `STATO_OUTREACH = "nuovo"` (o tutte se `solo_nuovi=False`)
3. Log: `"N lead da qualificare"`

### Step 2 — Arricchimento dati (se mancanti)
Per ogni lead senza email:
1. Prova Hunter.io domain search con il dominio del sito (se esiste) o `nome+città`
2. Se trovata → aggiorna colonna EMAIL nel foglio
3. Log: `"Email trovata per [nome]: [email]"` o `"Nessuna email per [nome]"`

### Step 3 — Calcolo Score Priorità Finale

#### Per lead "no sito" (fonte: WF-A)
Il punteggio è già calcolato da WF-A. In questo step lo raffina:

| Bonus | Punti |
|-------|-------|
| Email trovata nel passo arricchimento | +15 |
| Settore ad alta domanda* | +10 |
| Nessun competitor ovvio nella stessa zona | +5 |

*Settori ad alta domanda: dentista, avvocato, commercialista, ristorante gourmet, palestra, centro estetico, idraulico, elettricista

#### Per lead "funnel scarso" (fonte: WF-B)
Score finale = (100 − Score_Funnel) + bonus:

| Bonus | Punti |
|-------|-------|
| Almeno 3 ads attivi (investono di più) | +15 |
| Email trovata | +15 |
| Telefono trovato | +10 |
| Settore ad alta domanda | +10 |

Score massimo possibile: 150 → normalizzato su 100

### Step 4 — Classificazione in Fasce

| Fascia | Score | Priorità | Descrizione |
|--------|-------|----------|-------------|
| A | 70-100 | Alta | Lead caldissimo, contatta subito |
| B | 40-69 | Media | Lead valido, includi nel prossimo batch |
| C | 0-39 | Bassa | Lead debole, archivio futuro |

### Step 5 — Verifica idoneità outreach
Un lead è `PRONTO_OUTREACH = "Sì"` solo se:
- [ ] Ha email O telefono
- [ ] Fascia A o B
- [ ] Non è già stato contattato (`STATO_OUTREACH = "nuovo"`)

Altrimenti: `PRONTO_OUTREACH = "No"` con `MOTIVO_ESCLUSIONE` compilato.

#### Per lead "ai_prospect" (fonte: WF-F)
Score finale basato su indicatori di opportunità AI e contattabilità:

| Criterio | Punti |
|----------|-------|
| SCORE_AI_POTENZIALE >= 60 | +30 |
| SCORE_AI_POTENZIALE 40-59 | +15 |
| Offerte lavoro trovate per ruoli manuali | +20 |
| Referente decisionale trovato | +20 |
| Email trovata | +15 |
| Telefono trovato | +10 |
| Dimensione 20-50 dipendenti (sweet spot) | +10 |
| Dimensione 50-200 dipendenti | +5 |
| Settore ad alta priorità AI* | +10 |

*Settori ad alta priorità AI: logistica, studi legali, commercialisti, agenzie immobiliari, e-commerce, cliniche, agenzie marketing

Score massimo possibile: 115 → normalizzato su 100

### Step 6 — Aggiorna Google Sheets
1. Batch update di tutte le righe processate
2. Ordina il foglio per `SCORE_PRIORITÀ` decrescente
3. Log: `"Qualificati N lead: X fascia A, Y fascia B, Z fascia C"`

---

## GESTIONE ERRORI

| Errore | Causa | Azione |
|--------|-------|--------|
| `Hunter.io: 429 rate limit` | Troppe richieste | Pausa 30s, riprova, poi salta email search |
| `Foglio vuoto` | Nessun lead nuovo | Log info, exit 0 |
| `Errore update Sheets` | Connessione o permessi | Salva modifiche su CSV locale, riprova poi |

---

## CASI LIMITE

- **Lead con score identico**: ordina alfabeticamente come tiebreaker
- **Email personale trovata** (es. mario.rossi@gmail.com): segnala in NOTE come "email personale", usa ugualmente
- **Lead duplicato tra i due tab** (stesso business trovato sia senza sito che con ads): mantieni il record con score più alto, archiviate l'altro
- **Lead AI prospect che ha anche funnel scarso**: trattare come due opportunità distinte — potrebbe ricevere sia servizio funnel che servizio AI
- **Azienda AI prospect senza email o referente**: `PRONTO_OUTREACH = "No"` — per il Servizio 2 è fondamentale contattare la persona giusta, non un'email generica `info@`

---

## LOG

File: `logs/YYYY-MM-DD_WF-C_qualifica.log`

```
[2025-01-15 15:05:00] START — Qualifica 35 lead nuovi
[2025-01-15 15:05:10] Arricchimento: 8 email trovate su 35 lead
[2025-01-15 15:05:30] Scoring completato
[2025-01-15 15:05:30] Fasce: A=12, B=18, C=5
[2025-01-15 15:05:30] Pronti per outreach: 27 (no email/tel: 3, fascia C: 5)
[2025-01-15 15:05:35] Google Sheets aggiornato
[2025-01-15 15:05:35] END — Durata: 35s
```

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Outreach|Outreach Area]]
