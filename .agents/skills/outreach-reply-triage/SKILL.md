---
name: outreach-reply-triage
description: "Classifica le risposte ai messaggi outreach in 4 categorie e suggerisce la prossima azione. Usa quando hai una risposta da un prospect e devi decidere cosa fare. E' anche un PRODOTTO: la versione parametrizzata viene consegnata ai clienti Outreach Factory."
---

# Skill: outreach-reply-triage

> Reparto: A2-ACQUISIZIONE | Team: T-reply-triage | Tier: haiku
> PRODOTTO: versione parametrizzata inclusa in Outreach Factory delivery.

## Scopo

Classificare ogni risposta ricevuta su email/LinkedIn/Instagram in una delle 4 categorie
e determinare la prossima azione ottimale.

## Categorie di classificazione

### 1. INTERESSATO
Segnali: chiede dettagli, vuole sapere di piu', propone call, risponde positivamente.
Prossima azione: **proponi call** (link calendario o orari disponibili).
Mai fare: non inviare proposta senza call discovery.

### 2. OBIEZIONE
Segnali: ha dubbi specifici (prezzo, tempo, "gia' ci pensiamo", "non e' il momento").
Prossima azione: **rispondi all'obiezione** con prova reale dalla libreria A5.
Regola: max 2 follow-up dopo obiezione. Al 3o silenzio: archivia.

### 3. NO DEFINITIVO
Segnali: "non interessato", "rimuovimi", "per favore non scrivere", "stop".
Prossima azione: **archivia immediatamente**. ZERO follow-up. Segna in leads.db.
Regola ferrea: nessuna risposta a "no" definitivo.

### 4. OUT-OF-OFFICE / FUORI-CONTESTO
Segnali: risposta automatica OOO, risposta irrilevante, persona sbagliata.
Prossima azione: **attendi** (OOO: riprova dopo data rientro) o **archivia** (sbagliato).

## Processo

1. Leggi il testo della risposta
2. Identifica categoria (se ambiguo: scegli la piu' conservativa — meglio OBIEZIONE che INTERESSATO)
3. Cerca obiezione piu' vicina nella libreria T-objection-handler
4. Genera prossima azione specifica con testo suggerito
5. Logga in agency/conversations (DOPO aidefence_has_pii se contiene dati personali)

## Output

```json
{
  "lead_id": "string",
  "canale": "email | linkedin | instagram",
  "categoria": "INTERESSATO | OBIEZIONE | NO | OOF",
  "confidenza": "alta | media | bassa",
  "obiezione_tipo": "string | null",
  "prossima_azione": "PROPONI_CALL | RISPONDI_OBIEZIONE | ARCHIVIA | ATTENDI",
  "testo_risposta_suggerito": "string | null",
  "note": "string"
}
```

## Connessioni

- `company/01-agency/A2-ACQUISIZIONE/BACKBONE.md`
- `company/01-agency/A5-COPY-INTERNO/BACKBONE.md` — libreria obiezioni
- `company/01-agency/A2-ACQUISIZIONE/handoffs/HC-A2-A3-call.json` — attivato su INTERESSATO
