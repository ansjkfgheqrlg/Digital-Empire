---
Type: PROJECT
Status: Active
Tags: #outreach #email #copy #audit #dentista
Created: 2026-05-07
Last updated: 2026-05-07
---

# Email Audit — Template Dentisti v1 → v2

## Overview
Analisi critica del template email usato nel primo batch da 30 email a studi dentistici (inviato 2026-05-06). Identificati 8 errori e prodotto template v2 migliorato con valore educativo, identità mittente, e rimozione di frasi difensive.

---

## Batch v1 — Dati
- **Data invio**: 2026-05-06, ore 21:41-21:44
- **Destinatari**: 30 studi dentistici (Milano, Roma, Napoli, altre città IT)
- **Tasso apertura**: da rilevare
- **Risposta ricevuta**: 1 — `assistenza.pazienti@studiobittante.com` → "BASTA MAIL!!!" (BLACKLIST)

---

## Errori Identificati (8)

### ERRORE 1 — IDENTITÀ ASSENTE ⚠ (alta priorità)
L'email non dice chi è Max né cosa fa Digital Empire. Senza identità, suona come spam anonimo.
**Fix**: aggiunta riga "Sono Max — lavoro con studi medici e dentistici in Italia per..."

### ERRORE 2 — ZERO VALORE EDUCATIVO ⚠ (alta priorità)
L'email descrive il problema ma non insegna nulla di nuovo al destinatario.
**Fix**: aggiunto dato educativo: "Il 62% delle ricerche mediche avviene tra le 18 e le 22" + meccanismo concreto del reminder SMS.

### ERRORE 3 — FRASE DIFENSIVA: "Non ti chiedo di fidarti"
Viene da un posto di insicurezza. Un consulente esperto non si giustifica preventivamente.
**Fix**: rimossa completamente.

### ERRORE 4 — AUTO-SABOTAGGIO: "Il 90% puoi applicarlo da solo"
Undermines il valore della call. Contraddittorio con l'obiettivo.
**Fix**: sostituita con "Ti chiedo 20 minuti per mostrarti quello che ho trovato nel vostro caso specifico."

### ERRORE 5 — CPB INCOMPLETO (PROOF mancante)
CLAIM: "prenotazioni solo per telefono" ✓ | PROOF: non dimostrata ✗ | BENEFIT ✓
**Fix**: l'opener è stato rafforzato per specificare l'osservazione ("L'unico modo per prenotare: solo telefono").

### ERRORE 6 — SOCIAL PROOF ASSENTE
Nessun riferimento ad altri studi dentistici o al settore.
**Fix**: aggiunto "Gli studi dentistici che usano questo sistema..."

### ERRORE 7 — OGGETTO NON CREA CURIOSITY GAP
`"{nome} — pazienti che non riuscite a raggiungere"` dice già tutto.
**Fix**: nuovo oggetto → `"{nome} — quanti pazienti vi cercano la sera e non riescono a contattarvi?"`

### ERRORE 8 — LUNGHEZZA ECCESSIVA
~155 parole vs max 130 del framework. Aggiustato con restructuring denso.

---

## Template v2 (attivo in send_now.py)

```
OGGETTO: {nome} — quanti pazienti vi cercano la sera e non riescono a contattarvi?

CORPO:
Ho cercato studi dentistici a {citta} e ho trovato {nome}. Per prenotare: solo telefono.

Il 62% delle ricerche mediche avviene tra le 18 e le 22, quando gli studi sono chiusi. Senza
prenotazione online, quei pazienti finiscono dove trovano il pulsante "prenota adesso". Stima
concreta: 15-20 pazienti al mese che non tornano. Il reminder automatico SMS riduce i no-show
del 30-35% — ogni appuntamento saltato vale mediamente €120-150 di agenda persa.

Ecco come funziona: il paziente sceglie uno slot disponibile, conferma in 30 secondi, riceve
un reminder 48h prima. Gli studi dentistici che usano questo sistema lo impostano una volta
e smettono di pensarci.

Sono Max — lavoro con studi medici e dentistici in Italia per chiudere questo tipo di gap.
Prima analizzo ogni caso, poi (e solo allora) propongo qualcosa.

Ti chiedo 20 minuti per mostrarti quello che ho trovato nel vostro caso specifico.

Ha senso fare quella chiamata?

Max | Digital Empire
```

---

## Principi Applicati (dal framework wiki)

| Principio | Applicato in v2? |
|-----------|-----------------|
| APSOC: ATTENZIONE specifica | ✓ opener diretto |
| APSOC: PROBLEMA amplificato | ✓ con numeri |
| APSOC: SOLUZIONE risultato | ✓ sistema concreto |
| APSOC: SOCIAL PROOF settoriale | ✓ "studi dentistici che..." |
| APSOC: OBIEZIONE anticipata | ✓ "prima analizzo, poi propongo" |
| APSOC: CTA morbida | ✓ domanda sì/no |
| DR: Loss aversion | ✓ |
| DR: Specificità numerica | ✓ 62%, 15-20, 30-35%, €120-150 |
| CPB completo | ✓ claim+proof+benefit |
| Identità mittente | ✓ (mancava in v1) |
| Valore educativo | ✓ (mancava in v1) |

---

## Piano Follow-up

### Email 2 — Follow-up breve (giorno 3-5) ✅ IMPLEMENTATO
- **Script**: `send_followup_b1.py` (batch 1) / `send_followup_b2.py` (batch 2)
- **Strategia**: pattern interrupt — <60 parole, zero stats, domanda binaria
- **Killer line**: "poi smetto di scrivere se la risposta è no"
- **Oggetto**: identico all'email 1 → Gmail threada automaticamente
- **Timing B1**: 2026-05-09/10/11 | **Timing B2**: 2026-05-11/12

### Email 3 — Chiusura definitiva (giorno 10-14) ⏳ DA FARE
- **Tono**: definitivo, si chiude il ciclo ("ultima email")
- **Angolo**: costo concreto dell'inazione in €/mese, o passaggio a WhatsApp

### Response Management
- **Blacklist**: `studiobittante.com` → MAI più contattare
- **Interessati**: risposta manuale immediata → call entro 24h
- **Response Analyzer**: classificare risposte (interessato / negativo / rimbalzo)

---

## Connessioni
- [[Outreach_Workflow_Sistema]] — sistema principale di outreach
- [[Concept_Email_APSOC]] — framework copy utilizzato
- [[Outreach_Batch_Dentisti_2026-05]] — dati del batch
