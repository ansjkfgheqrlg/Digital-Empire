---
name: proposal-gate
description: "Gate Preventivo: checklist eseguibile che BLOCCA l'invio di un preventivo se non soddisfa i criteri. Usa questa skill prima di inviare qualsiasi preventivo a un prospect. BLOCCA, non suggerisce. Output: PASS (ok inviare) o FAIL (lista punti bloccanti da correggere)."
---

# Skill: proposal-gate

> Reparto: A3-PREVENTIVI | Team: T-proposal-qa | Tier: opus
> Kernel <=500 righe. Per il dettaglio tecnico: references/proposal-gate/

## Scopo

Checklist BLOCCANTE del Gate Preventivo (PIANO-MAESTRO/01 sez. 8).
Nessun preventivo viene inviato senza PASS su tutti i punti.

## Input atteso

Il documento preventivo completo (testo o markdown) + brief discovery call.

## Checklist (tutti i punti DEVONO essere PASS)

### 1. Problem-first [BLOCCA]
- Il documento APRE con il problema del cliente (non con chi siamo, non con i prezzi)
- Il problema e' descritto con le parole/dati del cliente (non marketing generico)

### 2. Awareness level corretto [BLOCCA]
- Se cliente AWARE: documento parla di implementazione concreta, non di concetti base
- Se cliente UNAWARE: documento educa prima di vendere, poi propone

### 3. Pricing a catalogo [BLOCCA]
- Prezzo = uno di: EUR 4.000 (Outreach Factory) / EUR 3.500 (Content Factory) / EUR 2.500 (Second Brain) / EUR 8.000 (Engine Room)
- NESSUN sconto improvvisato, nessun prezzo personalizzato
- "Vedremo come finisce" o prezzi vaghi = FAIL automatico

### 4. Prove verificabili [BLOCCA]
- Ogni claim di risultato e' accompagnato da: dati nostri reali OPPURE dati del cliente dalla call
- Nessuna promessa senza prova (Mandato Empire: "prove non promesse")
- Frasi tipo "potrai aumentare le vendite del 300%" senza fonte = FAIL automatico

### 5. Scope delivery 7gg [BLOCCA]
- Il documento specifica che il setup avviene in 7 giorni SUL SERVER DEL CLIENTE
- Il countdown parte da ambiente conforme (non da firma)

### 6. Proprieta' codice + EUR 0 canoni [BLOCCA]
- Esplicitamente scritto: il codice e' di proprieta' del cliente
- Esplicitamente scritto: EUR 0 canoni mensili (one-time)

### 7. Supporto 90gg definito [BLOCCA]
- Supporto 90 giorni post-delivery menzionato con scope chiaro

### 8. Brand voice [WARN — non blocca, ma segnala]
- Tono diretto, provocatorio, trasparente
- No gergo tecnico senza spiegazione
- No promesse eccessivamente entusiastiche

### 9. Timing [BLOCCA se scaduto]
- Il preventivo viene inviato entro 48h dalla discovery call

### 10. Soglia ticket alto — gate umano [WARN — riferimento di mercato]
- Se il prezzo del preventivo è **sopra 3.000 €**: verifica che il percorso del prospect sia passato
  da una vera sales call (non solo da un checkout/form automatico) — sopra questa soglia non basta
  l'automazione, serve un gate umano prima dell'invio. Il catalogo prezzi DE (EUR 2.500-8.000) è
  quasi sempre sopra soglia: questo punto conferma che il Gate Preventivo stesso, con la discovery
  call obbligatoria a monte, è già allineato al riferimento di mercato. Fonte: studio Andrei Pascu,
  outFunnel Lezione 19 (KA-01/02).

## Output

```
GATE PREVENTIVO: PASS | FAIL

Punti PASS: [lista]
Punti FAIL: [lista con punto specifico e testo da correggere]
Warnings: [lista]

Prossima azione: INVIA | REWORK (punti: X, Y, Z)
```

## Connessioni

- `company/01-agency/A3-PREVENTIVI/BACKBONE.md`
- Skill `discovery-call-brief` — fornisce il brief di input
- Skill `beast-preventivi` — genera il documento da gateare
- `company/Mandato/MANDATO-EMPIRE.md` — "prove non promesse"
