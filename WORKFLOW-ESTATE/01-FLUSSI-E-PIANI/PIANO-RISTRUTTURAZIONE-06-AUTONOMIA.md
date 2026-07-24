# PIANO 6 — AUTONOMIA SORVEGLIATA
> Livello 6 di 7 · **Stato: Proposta** · Owner: Max · Controllore: Claude · Origine: RISTRUTTURAZIONE-05-DEBUG-RIPRESA.md

---

## 0. Autocritica di RISTRUTTURAZIONE-05-DEBUG-RIPRESA
Il Piano 05 rende il sistema resiliente in grado di riprendere dopo un'interruzione, ma:
1. **Confine d'azione vago:** Non stabilisce una distinzione formale tra le operazioni che l'AI può fare da sola e quelle che necessitano dell'approvazione umana.
2. **Rischio di out-of-control:** Lascia aperta la possibilità teorica che un agente provveda autonomamente alla pubblicazione di video/caroselli non corretti o all'invio di messaggi non validati.

---

## 1. Dimensione Migliorata
**Autonomia di Esecuzione e Confine Gated.**
L'obiettivo è concedere la massima autonomia operativa all'AI nella fase di "fabbrica" (ricerca, scrittura, rendering, test) tenendo però il controllo manuale assoluto sulla "porta d'uscita" verso l'esterno.

---

## 2. Il Contenuto

### A. La Regola d'Oro del Confine Operativo
- **Autonomia AI (100%):** Ingestion, analisi competitor, sintesi script, rendering video, test checkout di prova, scraping lead, preparazione bozze email/messaggi.
- **Approvazione Umana (Max):** Invio messaggi/email reali ai concessionari (outreach), pubblicazione live dei video su YouTube, pubblicazione caroselli su Instagram.

### B. Interfaccia di Approvazione (UI Gate)
Ogni workflow si interrompe prima dello stage finale di rilascio ("Publishing" o "Send"):
1. **Notifica su EmpireDesk:** La System Tray App mostra una notifica toast nativa: `Workflow WF-S5 pronto per il rilascio. In attesa di approvazione.`
2. **File di Validazione:** L'agente genera un file in `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/feedback/ready_<workflow_id>.json` contenente il percorso del video, il testo del post e i lead destinatari.
3. **Sblocco Umano:** Max apre `EmpireDesk`, seleziona il workflow e clicca su "Approva" (che scrive `{"approved": true}` nel file di feedback sbloccando l'ultimo stage dell'agente).

---

## 3. Gate di Passaggio 6→7

Il passaggio al Livello 7 è consentito solo se si soddisfano i seguenti criteri oggettivi:
1. **Nessun invio non autorizzato:** Durante i test offline, nessun video viene effettivamente caricato su YouTube e nessuna email inviata se il file `ready_*.json` non contiene la firma di approvazione di Max.
2. **Sblocco da Tray funzionante:** Lo sblocco del gate di pubblicazione tramite input dell'utente su `EmpireDesk` funziona correttamente e fa avanzare il processo.

*Cosa fare in caso di fallimento:* Se un'azione esterna viene intrapresa senza firma, il sistema viene istantaneamente bloccato, revocando le credenziali API salvate in memoria ed emettendo un allarme di violazione di sicurezza.

---

## 4. Autocritica del Piano 6
- **Cosa ho migliorato:** Ho protetto il brand ed il budget aziendale definendo una barriera invalicabile tra la generazione dei contenuti e la pubblicazione finale.
- **Cosa manca ancora:** Abbiamo un sistema autonomo e sicuro, ma manca il cervello superiore (APEX) in grado di analizzare gli errori commessi nelle sessioni precedenti e auto-migliorare le regole degli agenti (compito del Livello 7).
- **SCORE:** **9.5 / 10** (Equilibrio perfetto tra controllo e velocità).

---
⛓️ Trace P12: `RISTR-PIANO-06#autonomia` · fonte: RISTRUTTURAZIONE-05-DEBUG-RIPRESA.md · migliorato da: [RISTRUTTURAZIONE-07-AUTO-MIGLIORAMENTO.md](RISTRUTTURAZIONE-07-AUTO-MIGLIORAMENTO.md)
