> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A2 + sez. 5 (run_followup.py, followup_writer)

# T-FOLLOWUP — Sequenze Follow-Up Multi-Touch

> Funzione L4 di A2-ACQUISIZIONE · Worker · Agente: `AG-A2-FUP-W` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A2

## Cosa fa

Gestisce le sequenze follow-up per lead che non hanno risposto (cold follow-up) e per lead con
obiezioni (warm follow-up). Skill: `cold-email`. Script: `run_followup.py`, `followup_writer.py`.

## Tipologie di follow-up

### Cold Follow-Up (nessuna risposta)

Sequenza multi-touch schedulata:
- FUP-1: +3 giorni → angolo diverso, riferimento al precedente (breve)
- FUP-2: +7 giorni → cambio approccio: evidenza/caso d'uso
- FUP-3: +14 giorni → "break-up email": se non interessa, dimmelo (rispetta il tempo)
- Dopo FUP-3 senza risposta → lead taggato "cold-archive"; NON contattato di nuovo per 60 giorni

### Warm Follow-Up (obiezione classificata da T-TRIAGE)

- OBIEZIONE "troppo costoso" → follow-up con ROI breakdown (quanto costa NON farlo)
- OBIEZIONE "lo facciamo già" → follow-up con audit gratuito (sfida l'assunzione)
- OBIEZIONE "non è il momento" → follow-up in 30 giorni (rispetta il timing)
- Ogni risposta a obiezione viene dalla **libreria T-OBJECTION-HANDLER** (solo prove reali)

## Regole operative

- MAI più di 3 follow-up cold senza risposta → regola anti-spam protezione account
- Follow-up APSOC: anche il follow-up rispetta la struttura (hook, valore, CTA)
- CTA invariata: `presentazione-empire.vercel.app`
- `agency/conversations`: ogni follow-up loggato con thread completo; PII-scan prima dello store

## Output

Messaggio follow-up → T-BIBBIA-QA → (se PASS) → T-SENDER. Il Gate Bibbia si applica ANCHE
ai follow-up (non solo al primo messaggio).

## Failure

| Evento | Risposta |
|---|---|
| Libreria obiezioni vuota per quel tipo | follow-up generico (valore, non risposta a obiezione); segnala gap ad A5 |
| Lead risponde con NO durante follow-up | stop immediato: T-TRIAGE riclassifica come NO → do-not-contact |

## Connessioni

- [`./T-reply-triage.md`](./T-reply-triage.md) (trigger per warm follow-up) · [`./T-bibbia-qa.md`](./T-bibbia-qa.md) (gate obbligatorio)
- [`../Funzioni/T-objection-handler.md`](./T-objection-handler.md) (fonte risposte obiezioni)
- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
