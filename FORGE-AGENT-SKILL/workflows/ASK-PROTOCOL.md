---
intestazione_adr008: { proprietario: FORGE-AGENT-SKILL (06b-FORGE, via fas-conductor), controllore: fas-qa-gate (punto 7 checklist) + METHOD-GUARD, origine: FORGE — MIR-3 dossier 18 (2026-07-20, CP-20260720-009), governo: ADR-002/005/006/008 }
---

# ASK-PROTOCOL — l'ASK formale e obbligatorio dei FORGE-PLAN (MIR-3)

Chiude l'invariante #3 della master-build-architecture (`PLAN → ASK → BUILD → CRITIQUE → ITERATE`)
che nell'impero era applicata in modo informale (audit dossier 18: ⚠️ parziale).
Da oggi **ogni FORGE-PLAN del reparto contiene una sezione `## ASK` compilata SEMPRE** —
anche quando la risposta è \"0 domande necessarie\" (in tal caso: motivarla in una riga).

## 1. Quando l'ASK è obbligatorio (trigger — basta 1)

| # | Trigger | Esempio |
|---|---|---|
| T1 | **Ambiguità ad alto impatto** su nomi/slug, ownership, confini con altri asset, priorità | \"questo agente va sotto 04-MARKETING o 06b-FORGE?\" |
| T2 | **Sorgente insufficiente per atomi critici** (il MKD non raggiunge 95% senza ➕ inventati) | manca il numero reale di lead/mese attuale |
| T3 | **Decisione economica o cliente-facing** (prezzi, contratti, promesse commerciali) | il lead magnet promette un risultato numerico? |
| T4 | **Potenziale conflitto** con asset attivi (ADR-003) o con decisioni Max precedenti | la nuova skill sovrascrive una Script-Factory attiva? |

Nessun trigger ⇒ sezione `## ASK` con una riga: `0 domande — motivo: <perché i requisiti sono completi>`.

## 2. Regole di forma (bloccanti)

1. **MAX 3 domande.** Se ne emergono di più, si tengono le 3 a maggior impatto e il resto va in
   backlog (`memory/INDEX.md` o BACKLOG.md dell'ecosistema) — mai alluvionare Max.
2. **Una domanda = una sola decisione.** Vietate domande ombrello (\"come lo vuoi?\" → FAIL).
3. Ogni domanda dichiara: **contesto in 1 riga · opzioni (A/B/C) · raccomandazione del conductor ·
   default** — il piano non dipende dalla risposta (ADR-005: mai fermare la costruzione).
4. **Default dichiarato:** se Max non risponde entro la sessione, si procede col default marcato
   `[ASSUNZIONE]` nel piano e nella build, da validare a risposta avvenuta.
5. **Replies tracciate:** a risposta ricevuta, si aggiunge `↳ RISPOSTA (<data>): <decisione>` nella
   sezione ASK e si aggiorna il piano/artefatto. Chiudere il cerchio è parte del protocollo.

## 3. Formato canonico (copia-incolla nel PLAN)

```markdown
## ASK (MIR-3 — ASK-PROTOCOL)
| # | Domanda (1 decisione) | Opzioni | Raccomandazione | Default [ASSUNZIONE] | Trigger |
|---|---|---|---|---|---|
| Q1 | ... | A ... / B ... | B (motivo 1 riga) | B | T1 |
```

## 4. Gate

- **Conductor checklist (MIR-3):** la sezione `## ASK` è compilata PRIMA del BUILD; i default
  `[ASSUNZIONE]` sono propagati nel piano e negli artefatti.
- **fas-qa-gate (checklist punto 7 — Memoria):** FAIL se manca la sezione `## ASK` nel piano
  o contiene domande-ombrello/più di 3 domande.
- **Anti-recidiva:** se un difetto di gate nasce da \"requisito ambiguo non chiesto\", il FAIL
  ripetuto 2 volte genera una nuova regola in `rules/` (Ispettorato, dossier 15).

## 5. Perché max 3

Brain-dump di domande = esternalizzare il lavoro del conductor. Il reparto è pagato (in tempo di Max)
per **proporre default sensati e chiedere solo ciò che cambia davvero l'artefatto** — coerente con
ADR-005 (backlog non blocca) e con il principio Hormozi applicato al team: domande ad alto valore,
attrito minimo.
