# LinkedIn Daily Checklist — Digital Empire

## OGNI MATTINA — Cosa controllare

### 1. Risposte ai COMMENTI
- Apri LinkedIn → Notifiche → filtra "Commenti"
- Per ogni risposta al tuo commento:
  - Se positiva/curiosa → rispondi + manda connection request con nota
  - Se neutra → metti Like alla risposta, non rispondere ancora
  - Log: aggiorna `linkedin_leads.json` con `"comment_replied": true`

### 2. Accettazioni CONNESSIONI
- Apri LinkedIn → La mia rete → Connessioni
- Per ogni nuova connessione accettata:
  - Aspetta 1 giorno → poi manda il DM di benvenuto (generate_message)
  - In `linkedin_leads.json` cerca il profilo → `"connect_accepted": true`
  - Script: `python run_today.py` gestisce già il follow-up automatico (FASE 3)

### 3. Risposte ai DM
- Apri LinkedIn → Messaggi
- Per ogni risposta:
  - Se interessato → porta la conversazione avanti, proponi una call
  - Se "non sono interessato" → risposta educata + rimuovi da sequenza
  - Log: aggiorna `"status": "in_conversation"` in `linkedin_leads.json`

### 4. Avvia gli script del giorno
```bash
cd "LinkedIn Automation"

# 1. Commenti (30/giorno)
python comment_posts.py

# 2. Connessioni + messaggi follow-up
python run_today.py

# 3. DM diretti su Open Profile
python direct_dm.py
```

---

## LOG GIORNALIERO

### 2026-05-12 (OGGI)
| Azione | Numero | Note |
|--------|--------|------|
| Commenti inviati | 11 → target 30 | In corso |
| Connessioni inviate | 0 | Da fare dopo commenti |
| DM diretti inviati | 0 | Da fare dopo connections |
| Connessioni accettate | 0 | Check domani |
| Risposte DM | 0 | Check domani |
| Risposte commenti | 0 | Check domani |

---

## REGOLE ANTI-BAN
- Max 20 connection requests/giorno
- Max 30 commenti/giorno
- Max 25 DM diretti/giorno
- Delay 30-55 sec tra commenti
- Delay 35-65 sec tra DM
- Delay 12-25 sec tra connection requests
- NON superare mai i limiti
- Se LinkedIn mostra captcha → ferma tutto, aspetta 24h
