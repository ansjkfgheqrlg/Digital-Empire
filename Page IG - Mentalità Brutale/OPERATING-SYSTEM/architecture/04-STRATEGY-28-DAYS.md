# Strategia 28 giorni — baseline chirurgica

## Obiettivo

Scoprire quali combinazioni **formato × hook × slot** generano attenzione qualificata per Mentalità Brutale senza confondere volume, qualità e causalità.

## Numero preciso

- 4 settimane.
- 7 pubblicazioni/settimana.
- 28 pubblicazioni totali.
- 16 Reel (4/settimana).
- 12 caroselli (3/settimana).
- 2 snapshot per contenuto: +48h e +168h.
- 56 snapshot metrici attesi.

Questa cadenza è un **protocollo di test**, non una promessa algoritmica. Viene fermata se quality first-pass scende o il sistema entra in PAUSED.

## Griglia settimanale

| Giorno | Formato | Pilastro default | Slot alternato | CTA default |
|---|---|---|---|---|
| Lun | Reel | P1 | 13:00/20:30 | salva |
| Mar | Carosello | P2 | 20:30/13:00 | condividi |
| Mer | Reel | P3 | 13:00/20:30 | segui |
| Gio | Carosello | P1/P4 | 20:30/13:00 | salva |
| Ven | Reel | P2 | 13:00/20:30 | condividi |
| Sab | Carosello | P5/P3 | 20:30/13:00 | salva |
| Dom | Reel | P4/P1 | 13:00/20:30 | segui |

La settimana successiva inverte slot e hook per ridurre il bias giorno-orario.

## Struttura Reel v0 — ipotesi da certificare sui video reali

1. **0.0-1.0s — pattern interrupt:** immagine/movimento + tesi leggibile senza audio.
2. **1-4s — costo:** cosa perde chi continua così.
3. **4-10s — meccanismo:** perché succede, una sola idea.
4. **10-16s — standard:** comportamento concreto.
5. **16-20s — payoff/CTA:** frase memorabile + azione.

Questo timing è `[IPOTESI]`, non pattern estratto: va sostituito dopo Empire Studio su un campione reale.

## Struttura carosello

1. Hook: contrasto/domanda, ≤1 tesi.
2. Tensione: costo invisibile.
3. Errore: comportamento specifico.
4. Meccanismo: perché si ripete.
5. Standard 1.
6. Standard 2.
7. Azione oggi.
8-9. prova/esempio solo se serve.
10. CTA coerente.

## Metriche

### Primary per tutti

- reach;
- saved;
- shares;
- total_interactions.

### Reel secondary

- views;
- average watch time;
- total watch time;
- first-3-second skip rate.

### Business

- profile activity/visits dove disponibile;
- bio link click dove disponibile;
- lead e revenue con UTM/CRM, non dedotti da like.

## Score diagnostico interno

```text
quality_actions = 5*shares + 4*saved + 3*comments + likes
quality_action_rate = quality_actions / max(reach, 1) * 100
```

Lo score serve a ordinare post comparabili, non sostituisce le metriche raw e non è una “metrica Meta”.

## Decisioni a fine ciclo

- **KEEP:** n≥3, mediana > baseline stesso formato, qualità stabile.
- **ITERATE:** segnale positivo ma n<3 o trade-off non chiaro.
- **KILL:** mediana sotto baseline in due finestre comparabili o quality gate degradato.
- **NO DECISION:** dato vuoto/ritardato o cella non bilanciata.

## Monetizzazione

Non riattivare la pagina “per postare”. Ogni ciclo deve avere una destinazione esplicita:

1. fase A: follow/save/share e baseline;
2. fase B: lead magnet coerente in bio;
3. fase C: prodotto proprio/affiliate filtrato;
4. fase D: shoutout solo con audience e disclosure adeguate.

Il link in bio e l'offerta non sono inventati da MB-OS: vengono approvati da 05-MB/02-INFO/04-MKT e tracciati.
