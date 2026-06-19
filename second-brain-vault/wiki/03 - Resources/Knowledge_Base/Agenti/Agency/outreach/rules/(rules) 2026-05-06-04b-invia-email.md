# 04b_invia_email
            
> Path: [[Map - Agenti|Agenti > Agency > outreach > rules]]

## Content

# REGOLA 04b — Invio Email Approvata

## OBIETTIVO
Inviare via Gmail un'email di outreach precedentemente generata e approvata manualmente dall'operatore. Aggiorna automaticamente lo stato del lead nel Google Sheets dopo l'invio.

**REGOLA ASSOLUTA**: Non inviare mai un'email senza averla prima letta e approvata. Lo script chiede sempre conferma esplicita prima di inviare.

## TRIGGER
- Manuale: operatore ha rivisto e approvato la bozza in `bozze_email/`
- Dipendenza obbligatoria: WF-D deve aver già generato la bozza

## INPUT

| Campo | Obbligatorio | Tipo | Descrizione |
|-------|-------------|------|-------------|
| `--id` | Sì | stringa | ID lead (es. `NS-MI-20250115143022`) |
| `--oggetto` | No | stringa | Oggetto personalizzato (sovrascrive quello della bozza) |
| `--anteprima` | No | flag | Mostra anteprima senza inviare |

## PRE-REQUISITI
- Lead con `BOZZA_GENERATA = Sì` e file bozza presente in `bozze_email/`
- Lead con `EMAIL` compilata nel foglio Google Sheets
- `MITTENTE_EMAIL` e `MITTENTE_EMAIL_PASSWORD` configurati nel `.env`
- Gmail con 2FA attiva e password per le app generata

## OUTPUT
- Email inviata al destinatario
- Colonne aggiornate in Google Sheets:
  - `STATO_OUTREACH` → `inviato`
  - `DATA_ULTIMO_CONTATTO` → timestamp invio
  - `DATA_FOLLOWUP_SCHEDULATO` → oggi + 7 giorni
  - `STORICO_STATI` → voce aggiunta

---

## STEP-BY-STEP

### Step 1 — Verifica pre-invio
1. Carica dati lead da Google Sheets (cerca in Lead_NoSito e Lead_FunnelScarso)
2. Verifica che `EMAIL` sia presente
3. Verifica che una bozza esista in `bozze_email/`
4. Se stato è già `inviato`: chiedi conferma esplicita prima di procedere

### Step 2 — Mostra anteprima
1. Estrai oggetto (primo suggerito o personalizzato) e corpo dalla bozza
2. Stampa anteprima completa a schermo
3. Chiedi conferma: **l'operatore deve digitare "s" per procedere**

### Step 3 — Invio
1. Crea messaggio MIME con oggetto, corpo testo plain, mittente e destinatario
2. Connetti a Gmail SMTP (`smtp.gmail.com:587`) con TLS
3. Autenticazione con email e password app
4. Invia email
5. Log: `"Email inviata a [email] ([nome_business])"`

### Step 4 — Aggiorna Google Sheets
1. `STATO_OUTREACH` → `inviato`
2. `DATA_ULTIMO_CONTATTO` → timestamp corrente
3. `DATA_FOLLOWUP_SCHEDULATO` → oggi + 7 giorni
4. `STORICO_STATI` → aggiungi `[timestamp]: [vecchio_stato] → inviato`

---

## GESTIONE ERRORI

| Errore | Causa probabile | Azione |
|--------|----------------|--------|
| `SMTPAuthenticationError` | Password app errata o non configurata | Interrompi, log errore con istruzioni per creare password app Gmail |
| `Bozza non trovata` | WF-D non eseguito o ID sbagliato | Interrompi, suggerisci di eseguire draft_emails.py |
| `EMAIL mancante nel lead` | Contatto non trovato in WF-A/B | Interrompi, suggerisci aggiornamento manuale |
| `Google Sheets: errore update` | Connessione o permessi | Log warning, email è comunque inviata — aggiorna manualmente |
| `Operatore ha rifiutato l'invio` | Input "N" alla conferma | Exit 0 normale, nessun log errore |

---

## FORMATO FILE BOZZA ATTESO

```
# BOZZA EMAIL — [ID_LEAD]
# ...metadati...

OGGETTO 1: [oggetto principale]
OGGETTO 2: [alternativa]
OGGETTO 3: [alternativa]
---
CORPO EMAIL:
[testo email]

# ISTRUZIONI...
```

Lo script estrae automaticamente oggetto e corpo da questo formato.

---

## SICUREZZA ANTI-SPAM

- Massimo 1 email inviata per run (script non supporta batch)
- Se il lead è già in stato `inviato`: avviso e conferma esplicita
- Le bozze non vengono mai eliminate dopo l'invio (archivio storico)
- La firma viene letta da `.env`, non hardcoded

---

## LOG

Aggiunto al file log del run corrente + log di WF-E tracking:
```
[2025-01-15 17:30:00] Invio email a info@rosi.it (Ristorante Bella Italia)
[2025-01-15 17:30:02] Email inviata con successo
[2025-01-15 17:30:03] Google Sheets aggiornato: NS-MI-xxx → inviato
[2025-01-15 17:30:03] Follow-up schedulato: 2025-01-22
```

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Outreach|Outreach Area]]
