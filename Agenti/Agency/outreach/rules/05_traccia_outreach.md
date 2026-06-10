# REGOLA 05 — Traccia Outreach e Gestione Pipeline

## OBIETTIVO
Mantenere aggiornato lo stato di ogni lead attraverso il ciclo di outreach, dalla bozza email fino alla chiusura del deal o all'archiviazione, garantendo che nessun contatto venga perso o contattato due volte.

## TRIGGER
- Manuale: operatore aggiorna lo stato di un lead dopo ogni azione
- Semi-automatico: lo script legge le risposte email e aggiorna automaticamente

## INPUT

| Campo | Obbligatorio | Tipo | Descrizione |
|-------|-------------|------|-------------|
| `id_lead` | Sì | stringa | ID del lead da aggiornare |
| `nuovo_stato` | Sì | stringa | Nuovo stato (vedi tabella stati) |
| `note` | No | stringa | Note libere |
| `data_followup` | No | data | Data per reminder follow-up |

## OUTPUT
- Riga aggiornata in Google Sheets
- Log in `logs/YYYY-MM-DD_WF-E_tracking.log`

---

## STATI DELLA PIPELINE

| Stato | Codice | Descrizione | Prossima azione |
|-------|--------|-------------|-----------------|
| Nuovo | `nuovo` | Lead trovato, non ancora contattato | Generare bozza email |
| Bozza pronta | `bozza_pronta` | Email generata, in attesa di revisione | Revisionare e approvare |
| Inviato | `inviato` | Email inviata | Attendere risposta (7 giorni) |
| Follow-up 1 | `followup_1` | Primo follow-up inviato | Attendere risposta (7 giorni) |
| Follow-up 2 | `followup_2` | Secondo follow-up inviato | Attendere risposta (7 giorni) |
| Risposto | `risposto` | Lead ha risposto | Gestire manualmente la conversazione |
| Call fissata | `call_fissata` | Appuntamento fissato | Preparare la call |
| Proposta inviata | `proposta_inviata` | Preventivo/proposta inviata | Attendere decisione |
| Cliente | `cliente` | Deal chiuso positivamente | Onboarding |
| Non interessato | `non_interessato` | Rifiuto esplicito | Archivia |
| Nessuna risposta | `nessuna_risposta` | Dopo 2 follow-up senza risposta | Archivia per 6 mesi |
| Archiviato | `archiviato` | Non più attivo | Nessuna |

---

## STEP-BY-STEP

### Step 1 — Leggi stato attuale
1. Cerca lead per `ID_LEAD` in Google Sheets (cerca in tutti i tab)
2. Mostra stato attuale: `"[NOME_BUSINESS] — stato corrente: [STATO]"`
3. Verifica che la transizione di stato sia valida (vedi matrice transizioni)

### Step 2 — Valida transizione di stato

#### Matrice transizioni valide:
```
nuovo → bozza_pronta
bozza_pronta → inviato
inviato → risposto | followup_1 | non_interessato
followup_1 → risposto | followup_2 | non_interessato
followup_2 → risposto | nessuna_risposta | non_interessato
risposto → call_fissata | non_interessato | archiviato
call_fissata → proposta_inviata | non_interessato | archiviato
proposta_inviata → cliente | non_interessato | archiviato
* → archiviato (qualsiasi stato può essere archiviato)
```

Se la transizione non è valida: log warning, chiedi conferma all'operatore.

### Step 3 — Aggiorna Google Sheets
Aggiorna le seguenti colonne:
- `STATO_OUTREACH` → nuovo stato
- `DATA_ULTIMO_CONTATTO` → oggi (se stato = inviato, followup_1, followup_2)
- `DATA_RISPOSTA` → oggi (se stato = risposto)
- `DATA_FOLLOWUP_SCHEDULATO` → data fornita dall'operatore
- `NOTE` → aggiungi nota con timestamp (non sovrascrivere, appendi)
- `STORICO_STATI` → aggiungi entry: `[timestamp]: [vecchio_stato] → [nuovo_stato]`

### Step 4 — Genera reminder follow-up
Se nuovo stato = `inviato` e nessuna `data_followup` specificata:
- Calcola automaticamente: oggi + 7 giorni
- Aggiorna `DATA_FOLLOWUP_SCHEDULATO`
- Log: `"Follow-up schedulato per [data] per [NOME_BUSINESS]"`

### Step 5 — Alert e notifiche
Se nuovo stato = `risposto`:
- Log prominente: `"🎯 RISPOSTA RICEVUTA: [NOME_BUSINESS] ha risposto!"`
- (opzionale) Invia notifica email all'operatore tramite Gmail

---

## REPORT SETTIMANALE PIPELINE

Il sistema genera automaticamente ogni lunedì un report con:
- N lead totali per stato
- N lead in attesa di azione
- N follow-up scaduti (data schedulata passata)
- Tasso di risposta: risposte / email inviate
- Lead più vecchi ancora in pipeline

Formato output: sezione aggiunta al log + email di riepilogo all'operatore

---

## REGOLE ANTI-SPAM

1. **Mai contattare lo stesso lead più di 3 volte** (1 email + 2 follow-up)
2. **Pausa minima tra email allo stesso lead**: 7 giorni
3. **Mai inviare email nei weekend** (sabato/domenica)
4. **Se un lead risponde "non interessato"**: aggiorna stato immediatamente, non inviare follow-up
5. **Limite giornaliero email**: max 20 email inviate per giorno dalla stessa casella mittente

---

## GESTIONE ERRORI

| Errore | Causa | Azione |
|--------|-------|--------|
| `ID lead non trovato` | ID errato o lead cancellato | Log errore, chiedi conferma |
| `Transizione non valida` | Stato non compatibile | Log warning, chiedi conferma esplicita |
| `Google Sheets: errore scrittura` | Connessione o permessi | Salva modifica in coda locale, riprova |
| `Data follow-up nel passato` | Data errata | Log warning, correggi a oggi + 7 giorni |

---

## CASI LIMITE

- **Lead risponde ma non è interessato**: stato `non_interessato`, non `risposto`
- **Lead risponde con richiesta di rimandare**: stato `risposto`, note "interesse futuro", follow-up tra 30 giorni
- **Lead contatta direttamente** (non risponde all'email): crea manualmente il lead se non esiste, salta gli step email
- **Stesso contatto in più lead** (es. stesso proprietario con due business): trattare ogni lead indipendentemente

---

## LOG

File: `logs/YYYY-MM-DD_WF-E_tracking.log`

```
[2025-01-15 17:00:00] UPDATE — NS-MI-xxx [Ristorante Bella Italia]: bozza_pronta → inviato
[2025-01-15 17:00:01] Follow-up schedulato: 2025-01-22
[2025-01-15 17:00:05] UPDATE — AF-RM-xxx [Studio Dentistico Bianchi]: nuovo → bozza_pronta
[2025-01-15 17:05:00] 🎯 RISPOSTA — NS-MI-yyy [Parrucchiere Rossella]: inviato → risposto
```
