---
name: upsell-mapper
description: "Mappa cliente -> offerta successiva ottimale. Attivare SOLO dopo Gate Delivery PASS + segnale positivo a fine 90gg. NON durante il supporto attivo. Output: proposta upsell personalizzata o identificazione referral."
---

# Skill: upsell-mapper

> Reparto: A6-MARKETING-INTERNO | Team: T-upsell-mapper | Tier: sonnet

## Regola di attivazione

QUESTA SKILL SI ATTIVA SOLO SE:
1. `gate_delivery_passed = true`
2. `segnale_positivo = true` (a fine 90gg, non prima)
3. Il cliente NON sta attraversando un problema aperto con DE

Se una di queste condizioni non e' soddisfatta: NON generare proposta upsell.

## Matrice upsell

| Prodotto attuale | Upsell naturale | Rationale |
|---|---|---|
| Outreach Factory (EUR 4.000) | Engine Room (EUR 8.000) | ha gia' outreach, manca content + brain |
| Content Factory (EUR 3.500) | Engine Room (EUR 8.000) | ha gia' content, manca outreach + brain |
| Second Brain (EUR 2.500) | Engine Room (EUR 8.000) | ha gia' brain, manca outreach + content |
| Engine Room (EUR 8.000) | Referral program | ha tutto il bundle |
| qualsiasi | Referral | conosce qualcuno con lo stesso problema? |

## Come calcolare il delta upsell

- Cliente ha Outreach Factory (EUR 4.000) -> Engine Room (EUR 8.000) = EUR 4.000 aggiuntivi
- Cliente ha Content Factory (EUR 3.500) -> Engine Room = EUR 4.500 aggiuntivi
- Cliente ha Second Brain (EUR 2.500) -> Engine Room = EUR 5.500 aggiuntivi

Il prezzo presentato e' SEMPRE il prezzo Engine Room meno quanto gia' pagato.
Logica: "hai gia' X — ti mancano Y e Z per avere il sistema completo".

## Vincolo bloccante: il primo acquisto deve restare percepito come completo

Da verificare PRIMA di scrivere il pitch. Se non e' soddisfatto, l'upsell non si manda: si
riprogetta.

**La regola.** Un upsell non deve mai far sembrare il primo acquisto incompleto o mutilato. Se il
cliente percepisce che gli e' stata "tolta" una parte del prodotto originale per poi rivendergliela,
si sente ingannato — e la fiducia costruita in 90 giorni di delivery si perde in una frase.

**I due errori nominati dalla fonte:**
1. Vendere lo stesso prodotto con variazioni cosmetiche minime (non converte).
2. Svalutare il primo acquisto con un secondo prodotto che conteneva informazioni gia' "dovute" nel
   primo.

**Attenzione specifica a questa skill.** Il pitch canonico qui e' *"hai gia' X — ti mancano Y e Z per
avere il sistema completo"* (vedi §Come calcolare il delta upsell). E' una frase a un passo dal
violare la regola: detta male, dichiara al cliente che quello che ha comprato non era completo. Il
taglio corretto e' **additivo, non sottrattivo** — X ha fatto quello che aveva promesso e continua a
farlo; Y e Z risolvono un problema DIVERSO che il cliente ha adesso, non un buco lasciato aperto da X.

**Check da superare prima di emettere `pitch_personalizzato`:** rileggi il pitch e chiediti — un
cliente che lo legge puo' concludere "quindi mi avevate venduto meta' prodotto"? Se si', si riscrive.

Fonte: studio Andrei Pascu, outFunnel Lezione 11 (KA-05 e KA-07 punto 2 — la stessa regola
vista da due angoli, il vincolo piu' insistito della lezione) — candidato AP-017, innestato 2026-09-10.

## Struttura proposta upsell

1. **Riconosci il risultato** (usa metrica reale del case study)
2. **Identifica il gap** (cosa manca per avere il sistema completo)
3. **Presenta il delta** (non il prezzo pieno — il delta)
4. **Prova** (usa il case study appena prodotto da case-study-forge)
5. **CTA** (nuova call discovery per capire se il gap e' prioritario per loro ORA)

## Output

```json
{
  "client_id": "string",
  "prodotto_attuale": "string",
  "upsell_target": "engine_room | referral",
  "delta_eur": 0,
  "pitch_personalizzato": "string (2-3 righe, APSOC compresso)",
  "prova_da_usare": "metrica reale dal case study",
  "timing": "fine_90gg | post_segnale_positivo"
}
```

## Connessioni

- `company/01-agency/A6-MARKETING-INTERNO/BACKBONE.md`
- Skill `case-study-forge` — le prove da usare vengono da qui
- Skill `support-90` — attiva questa skill solo a fine supporto
