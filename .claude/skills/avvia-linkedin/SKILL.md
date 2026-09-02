---
name: avvia-linkedin
description: Avvia il workflow LinkedIn di Digital Empire (commenti + connessioni + messaggi). Apre una finestra CMD visibile. Usa quando l'utente scrive /avvia-linkedin o vuole avviare LinkedIn, fare commenti su LinkedIn, mandare connessioni LinkedIn.
metadata:
  version: 1.0.0
---

# Avvia LinkedIn Outreach

Apri SUBITO una finestra CMD visibile con il flusso LinkedIn. NESSUNA domanda — esegui direttamente.

## Azione immediata

Esegui questo comando PowerShell che apre una nuova finestra CMD visibile sul desktop:

```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation" && echo. && echo  ===================================================== && echo   LINKEDIN OUTREACH - Digital Empire && echo   20 connessioni + 20 messaggi + 30 commenti/giorno && echo  ===================================================== && echo. && python run_today.py'
```

Dopo aver lanciato il comando, di' all'utente:
- "CMD aperto — flusso LinkedIn avviato"

## Fase 0 (a monte dell'outreach) — Il profilo come sales page

Il profilo LinkedIn non è un curriculum: è la pagina su cui atterra chi ha appena letto un post o ricevuto un messaggio. Se è rotto, tutto il traffico generato dall'outreach sopra evapora in silenzio invece di convertire — "fixing the profile beats improving content: la traffic sta già arrivando, un profilo rotto la fa solo evaporare in silenzio" (fonte: -gq8euRvNR4 — Paolo Trivellato, 12:00). Prima di aumentare il volume di connessioni/messaggi/commenti, verifica il profilo (proprio e, in prospettiva, quello dei clienti CRO) su questi 4 punti, logica errore→correzione:

| Errore | Correzione |
|---|---|
| Headline = job title (es. "CEO at [azienda sconosciuta]" — lo scrive chiunque, non differenzia) | Headline = chi aiuti + il risultato che generi, nient'altro (esempio reale: le prime due parole dell'headline dell'autore sono "Agencies and SaaS" — il suo ICP esatto) |
| Custom button che punta a una homepage generica (o assente) | Custom button = link diretto a un calendario di prenotazione |
| Featured section vuota | Featured section = case study + video-testimonial + breakdown della metodologia |
| Profilo che si legge come uno storico di carriera, non come una pagina di vendita | Ogni riga di About/Experience deve superare lo stesso test di rilevanza per l'ICP dei post |

(fonte: -gq8euRvNR4 — Paolo Trivellato, 09:56-12:00)

## Fase 0b — Segnale profile-view (contatto caldo in entrata)

Chi visita ripetutamente il tuo profilo in una finestra breve di tempo sta facendo ricerca attiva — è un segnale di buying-intent, non rumore. La maggior parte lo ignora. Va controllato quotidianamente e agganciato con UN messaggio genuino, diverso da quello a freddo: nessun pitch, nessun deck, solo una domanda sincera — non stai interrompendo, stai rispondendo a un segnale che l'altra persona ha già dato (fonte: -gq8euRvNR4 — Paolo Trivellato, 15:52).

Script esatto mostrato a schermo ("word for word"):
> "Noticed you have been checking out my profile — curious what caught your attention?"
(fonte: -gq8euRvNR4 — Paolo Trivellato, 17:04)

Tasso di risposta atteso — **discrepanza dichiarata nel video, non risolta a favore dell'una o dell'altra cifra**: 40-50% mostrato a schermo nella grafica, ma 20-50% dichiarato a voce dallo stesso autore poco dopo, come dipendente dalla qualità del profilo e dei contenuti (fonte: -gq8euRvNR4 — Paolo Trivellato, 15:52 a schermo / 16:54 a voce).

## Gate di qualità sui post — "The One-Sentence Post Test"

Prima di pubblicare qualsiasi post LinkedIn (proprio o per un cliente), verificare: **un prospect qualificato che lo legge può dire "sì — è esattamente la mia situazione"? Se no, è il post sbagliato.** (fonte: -gq8euRvNR4 — Paolo Trivellato, 04:28)
