# department-lead - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Paywall/login | contenuto inaccessibile | rileva il blocco | redirect login | salta, segnala, usa fonti aperte |
| Robots/anti-bot | blocco crawler | rispetta robots, rate sobrio | 403/captcha | passa a fonte alternativa |
| Contenuto dinamico | pagina vuota senza JS | Playwright (render JS) | DOM vuoto | attendi il render, riprova |
| Troppe pagine | crawl infinito | cap profondita'/pagine | coda enorme | limita lo scope alle pagine pertinenti |
| Fonte inaffidabile | contenuto di bassa qualita' | valuta autorevolezza | segnali spam | declassa o scarta |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
