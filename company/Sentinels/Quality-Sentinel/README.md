# ✅ Quality Sentinel

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 4.1
> **Sentinel always-on.** Autorità di enforcement LX.
> Supervisore C-Suite: CMO (empire-cmo)
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/Governance/README.md]]

---

## Identità

| Campo | Valore |
|---|---|
| **ID registro** | SENT-QUAL-001 (`Backbone/Identity-HR/registro-agenti.yaml`) |
| **Ruolo** | Sentinel autonomo always-on — enforcement qualità deliverable |
| **Tier** | L0-Sentinel (sopra gli ecosistemi, risponde a LX e CMO) |
| **Modello** | Sonnet (audit APSOC) / Haiku (checklist semplici) |
| **Namespace AgentDB** | `patterns/incidents/quality/` |

---

## Cosa osserva

- Score APSOC di ogni output di conversione (email, landing page, DM, preventivo, sales page)
- Completezza dei 6 blocchi APSOC: Attenzione → Problema → Soluzione → Obiezioni → CTA
- Pass-rate gate per team: % handoff approvati al primo tentativo negli ultimi 10 run
- Handoff rejected consecutivi dallo stesso team (indicatore di deriva sistematica)
- Trend qualità in calo per 3+ cicli consecutivi (segnale di degrado progressivo)
- Claim senza evidenza (CPB — Claim senza Proof): blocco automatico sul Brand-Voice Sentinel se il campo è sovrapposto

---

## Soglie e trigger

| Soglia | Condizione | Azione automatica |
|---|---|---|
| **Score APSOC < 80/100** | output copy standard sotto soglia | Blocco consegna; rework request con note dettagliate per sezione |
| **Score sales page < 85/100** | preventivo o landing page sotto soglia | Blocco consegna; escalation al team MARKETING copy hub |
| **P dopo S nella struttura** | Problema appare dopo Soluzione | −15 punti automatici; blocco obbligatorio indipendentemente dal totale |
| **Pass-rate < 90% su 10 run** | team con tasso di approvazione sistemicamente basso | Segnalazione al Quality-Guild + CMO per revisione standard |
| **2 reject consecutivi stesso team** | il team rigetta 2 handoff di fila | Escalation automatica: `type: escalation` via gbus al reparto superiore |
| **Trend calo 3 cicli** | qualità media in discesa per 3 cicli consecutivi | Convocazione Quality-Guild + segnalazione CTO per analisi strutturale |

---

## Azioni quando scatta

1. **Blocco consegna** — il deliverable non esce finché lo score non supera la soglia (gate hard, non bypassabile senza deroga Board).
2. **Rework request** — messaggio strutturato al team mittente con: sezione carente, score attuale, score richiesto, esempi di fix.
3. **Log in ReasoningBank** — ogni blocco registrato in `patterns/incidents/quality/` con causa e risoluzione.
4. **Segnalazione Quality-Guild** — per pattern sistematici: la Guild aggiorna le rubriche di valutazione.
5. **Escalation CMO/CTO** — per trend negativi o 2 reject consecutivi: report aggregato, non singolo evento.

---

## Input / Output

**Input atteso (via Bus — ogni handoff "delivery" passa qui):**
```json
{
  "tipo": "quality_check",
  "ecosistema_mittente": "01-AGENCY",
  "deliverable_type": "email | landing | preventivo | carosello | script",
  "contenuto": "...",
  "brand_kit": "DE | <cliente>",
  "apsoc_self_score": 0
}
```

**Output prodotto:**
```json
{
  "pass": false,
  "apsoc_score": 74,
  "blocchi_mancanti": ["Obiezioni", "CTA unica"],
  "feedback_per_sezione": {
    "Attenzione": "ok",
    "Problema": "troppo generico — manca dato specifico",
    "Soluzione": "ok",
    "Obiezioni": "MANCANTE — aggiungere almeno 2 obiezioni reali",
    "CTA": "due CTA competitive — rimuoverne una"
  },
  "incident_id": "INC-QUAL-20260611-002",
  "azione": "rework_required"
}
```

---

## KPI

| Metrica | Target |
|---|---|
| Score APSOC medio output DE | ≥ 80/100 |
| Output che supera gate al primo tentativo | > 70% |
| Gate bypassati | 0 (per definizione — Mandato Art.4.1) |
| Interventi depositati nel ReasoningBank | 100% |
| Reject consecutivi non escalati | 0 |

---

## Escalation

| Destinatario | Quando | Canale |
|---|---|---|
| CMO | 2 reject consecutivi o trend calo 3 cicli | gbus `type: escalation, priority: HIGH` |
| CTO | pattern strutturale nei gate (sistema rotto, non solo output) | report Quality-Guild |
| Board (raft) | proposta modifica soglie gate (richiede voto) | hive-mind_propose |

---

## Skill operative

- `cro-copy-architect` — audit APSOC (score per sezione, raccomandazioni) — skill installata
- `empire-brand-gate` — gate G2 binario (da forgiare P0)
- `contradiction-analyzer` — verifica coerenza contro Mandato — skill installata
- Fallback manuale (F1-F3): checklist APSOC in `Mandato/MANDATO-EMPIRE.md` §Checklist Brand Gate

---

## Stato

Struttura definita (F1). Implementazione automatica da costruire in F2-F5.
Nelle prime fasi (F1-F3): eseguito manualmente come checklist dal fondatore o da Claude.