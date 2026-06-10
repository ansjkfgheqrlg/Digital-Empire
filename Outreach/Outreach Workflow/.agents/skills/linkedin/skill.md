# LinkedIn Automation Skill

Skill per gestire il flusso LinkedIn automation di Digital Empire.
Directory principale: `c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation\`

## Comandi disponibili

### `/linkedin status`
Mostra lo stato completo del database LinkedIn:
```bash
python -c "
import json
from collections import Counter
with open(r'c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation\linkedin_leads.json') as f:
    data = json.load(f)
print('Status:', dict(Counter(l['status'] for l in data)))
print('Totale lead:', len(data))
"
```

### `/linkedin scrape [query]`
Scrape nuovi lead dalla ricerca LinkedIn. Esempi:
- `/linkedin scrape` — usa tutte le query in config.py
- `/linkedin scrape "avvocato Milano" 50` — cerca 50 avvocati a Milano

```bash
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"
python 01_scrape_leads.py
# oppure con query custom:
python 01_scrape_leads.py --search "avvocato Milano" --max 50
```

### `/linkedin connect`
Invia richieste di connessione (max 20/giorno, SENZA nota):
```bash
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"
python 02_send_connections.py
```

### `/linkedin check`
Controlla quali richieste sono state accettate:
```bash
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"
python 03_check_accepted.py
```

### `/linkedin message`
Invia il primo messaggio personalizzato ai connessi:
```bash
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"
python 04_send_messages.py
```

### `/linkedin followup`
Invia follow-up (giorno 3-4 no-link, giorno 7 con link):
```bash
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"
python 05_send_followups.py
```

### `/linkedin daily`
Runner giornaliero completo (check + messaggi + followup + connessioni):
```bash
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"
python run_daily.py
```

## Setup iniziale (da fare UNA VOLTA)

1. Crea account LinkedIn con la tua email
2. Modifica `config.py`: inserisci email e password LinkedIn
3. Fai login e salva sessione:
   ```bash
   cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"
   python linkedin_session.py
   ```
4. Scrape i primi lead:
   ```bash
   python 01_scrape_leads.py
   ```
5. Da domani: esegui `python run_daily.py` ogni mattina

## Strategia (da NotebookLM — Oleg Melnikov)

- Connessione SENZA nota → acceptance rate +30%
- Max 20 connessioni/giorno su account nuovo
- Messaggio dopo 24h dall'accettazione
- ZERO link nel primo messaggio
- Follow-up giorno 3-4: nudge (40% response rate)
- Follow-up giorno 7: info dump + link (30% response rate)
- Tasso risposta complessivo atteso: 20-40%
