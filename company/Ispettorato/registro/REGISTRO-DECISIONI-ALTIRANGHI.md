---
Type: REGISTRO
Status: Active (append-only)
Tags: #ispettorato #decisioni #altiranghi #board #maximilian
Created: 2026-07-20
Last updated: 2026-07-20
---

# REGISTRO-DECISIONI-ALTIRANGHI — Decisioni di Ritorno

> Traccia ogni decisione che torna da **Board C-Suite**, **MAXIMILIAN** o **Max** in risposta a un
> report dell'Ispettorato. Append-only: una voce chiusa non si riscrive; se un indirizzo cambia,
> si apre una nuova voce che cita la precedente.
> Agente responsabile (M3): `isp-liaison-altiranghi`. Chiusura solo dopo verifica di `isp-verifier`.

## Come si compila una voce

Per ogni decisione ricevuta dagli alti ranghi:
1. Registrare il testo INTEGRALE della decisione — non una parafrasi addolcita.
2. Legare la decisione al report che l'ha originata (`report/run|daily|escalation/<id>`).
3. Assegnare owner e scadenza; lo stato parte APERTA.
4. Solo `isp-verifier`, verificata l'applicazione reale, può portare lo stato a CHIUSA.

**Formato voce:**

```markdown
## DEC-YYYYMMDD-NNN
**Da:** Board / MAXIMILIAN / Max
**In risposta a:** <report id>
**Decisione:** <testo integrale>
**Assegnata a:** <reparto/agente owner> · **Scadenza:** <data|nessuna>
**Stato:** APERTA / IN ATTUAZIONE / CHIUSA (verificata da isp-verifier il <data>)
```

---

<!-- Nessuna decisione registrata: il registro è operativo da M3.
     Prima voce reale = DEC-YYYYMMDD-001 alla prima decisione di ritorno instradata. -->

## Connessioni
- [[REGISTRO-ERRORI]] · [[REGISTRO-REVISIONI]] · [[REGISTRO-SUCCESSI]]
- [[15-DOSSIER-ISPETTORATO]] · [[ARCHITETTURA]]
- `isp-liaison-altiranghi` (proprietario) · `isp-verifier` (chiude le voci)
