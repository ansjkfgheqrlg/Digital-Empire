# Instagram Automation — Daily Checklist

## Prima di avviare (1 volta ogni 7-10 giorni)

- [ ] Sessione valida?
  ```
  python "Instagram Automation\refresh_session.py"
  ```
  Se scaduta: fai login manuale nel browser che si apre, poi premi INVIO.

---

## Avvio giornaliero (tramite run_parallel.py)

```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach"
python run_parallel.py
```

Il sistema esegue automaticamente:
1. **IG-DM** (`run_today.py`) — scraping hashtag + invio DM nuovi + follow-up
2. **IG-REPLIES** (`check_replies.py`) — controlla risposte lead esistenti

### Oppure: avvio standalone Instagram

```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Instagram Automation"
python run_today.py
python check_replies.py
```

Per inviare le risposte automaticamente:
```
python check_replies.py --autoinvia
```

---

## Limiti giornalieri (config.py)

| Azione        | Limite |
|---------------|--------|
| DM nuovi/gg   | 15     |
| Follow-up/gg  | 20     |
| Delay tra DM  | 15–45s |
| Reply check   | 20 profili/sessione |

---

## Stato lead (instagram_leads.json)

| Status         | Significato                              |
|----------------|------------------------------------------|
| `scraped`      | Profilo trovato, nessun DM ancora        |
| `dm_sent`      | Primo DM inviato                         |
| `f1_sent`      | Follow-up 1 inviato (dopo 3gg senza rsp) |
| `f2_sent`      | Follow-up 2 inviato (dopo 5gg senza rsp) |
| `replied`      | Ha risposto — risposta AI generata       |
| `reply_gestita`| Risposta inviata in auto-invia mode      |
| `private`      | Profilo privato — skip                   |
| `error`        | Errore tecnico nell'invio                |

---

## Log e debug

- Log principale: `instagram_replies_log.txt`
- Screenshot debug (su errori): `debug_screenshots/`
- In caso di rate limit: attendi 30-60 min prima di riprovare

---

## Segnali di rate limit

Instagram mostra blocchi temporanei con frasi come:
- "We restrict certain activity" / "Limitiamo alcune attività"
- "Try again later" / "Riprova più tardi"
- "Action Blocked" / "Azione bloccata"

→ Il sistema si ferma automaticamente. Attendi e riprova.

---

## Troubleshooting rapido

| Problema                        | Soluzione                                              |
|---------------------------------|--------------------------------------------------------|
| `Sessione scaduta`              | `python refresh_session.py`                            |
| Browser non si apre             | Verifica che Playwright sia installato: `playwright install chromium` |
| Nessun lead trovato             | Controlla `TARGET_HASHTAGS` in `config.py`             |
| DM non inviati (0/15)           | Possibile rate limit — attendi 1h e riprova            |
| `classify_and_reply` lento      | API Groq ok; timeout alto = OpenRouter fallback attivo |
| Thread DM non si apre           | Profilo potrebbe aver disabilitato i DM da non-follower|
