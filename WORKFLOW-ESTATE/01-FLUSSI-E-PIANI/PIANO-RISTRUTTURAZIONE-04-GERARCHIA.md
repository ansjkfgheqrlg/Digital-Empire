# PIANO 4 — REPARTI E GERARCHIA VERA
> Livello 4 di 7 · **Stato: Proposta** · Owner: Max · Controllore: Claude · Origine: RISTRUTTURAZIONE-03-WORKFLOWS.md

---

## 0. Autocritica di RISTRUTTURAZIONE-03-WORKFLOWS
Il Piano 03 imposta correttamente i workflow operativi dei 6 stream, ma:
1. **Nessun organo gerarchico:** Tratta gli agenti come script isolati, senza stabilire relazioni di comando o di subordinazione.
2. **Escalation non strutturata:** Non indica cosa succede quando un controllo QA fallisce a livello di team operativo.
3. **Mancanza di ruoli dedicati:** Non definisce chi ha la responsabilità ultima della qualità di ciascuna fase.

---

## 1. Dimensione Migliorata
**Struttura Gerarchica e Ruoli Aziendali.**
L'obiettivo è mappare le interazioni tra gli agenti secondo un organigramma aziendale classico (Direttore -> Capo Reparto -> Specialista -> QA Indipendente).

---

## 2. Il Contenuto

### A. Organigramma degli Agenti in Esecuzione

```
             [CEO / Conductor Agent] (Direttore Generale)
                      |
        +-------------+-------------+
        |                           |
[CMO / Marketing Chief]    [CTO / Tech Chief] (Capi Reparto)
        |                           |
  +-----+-----+               +-----+-----+
  |           |               |           |
[Copywriter] [Ingestor]     [Developer] [SysAdmin] (Specialisti)
  |           |               |           |
  +-----+-----+               +-----+-----+
        |                           |
[QA Marketing Gate]        [QA Code Auditor] (Controllori QA)
```

1. **CEO Agent (Direttore):** Coordina il flusso globale, riceve i report dai Capi Reparto e presenta il risultato a Max.
2. **Capi Reparto (CMO, CTO):** Definiscono i piani operativi per la sessione e gestiscono le deviazioni standard.
3. **Specialisti (Copy, Ingestor, Dev, SysAdmin):** Eseguono i task operativi (scrittura script, download video competitor, restyle landing page).
4. **Controllori QA (QA Gate):** Ruoli indipendenti dagli specialisti. Controllano l'output secondo metriche rigide (es. Checklist APSOC, assenza di placeholders).

### B. Matrice di Escalation degli Errori
Quando un errore si verifica (es. Scadenza Stripe rotta o script non allineato a Dose Mentale):
1. **Fase 1 (Specialista):** Tenta una correzione automatica per 1 ciclo (re-generation).
2. **Fase 2 (Capo Reparto):** Se fallisce, il Capo Reparto blocca il flusso, analizza i log di errore e tenta una configurazione di ripiego (Fallback).
3. **Fase 3 (Direttore & Umano):** Se anche il fallback fallisce, il CEO Agent interrompe l'esecuzione del workflow, scrive l'errore nel registro ed invia una spiegazione in linguaggio umano semplice a Max (tramite notifica toast in `EmpireDesk` e log dedicato).

---

## 3. Gate di Passaggio 4→5

Il passaggio al Livello 5 è consentito solo se si soddisfano i seguenti criteri oggettivi:
1. **Separazione dei ruoli dimostrata:** Un output generato dallo specialista (Copy) viene respinto almeno una volta dal QA per violazione delle regole, e lo specialista esegue con successo la seconda revisione automatica.
2. **Interruzione ed Escalation:** Simulando un errore bloccante (es. API offline), il sistema si arresta a livello di CEO Agent senza far andare in crash l'intera pipeline.

*Cosa fare in caso di fallimento:* Se un QA approva un file contenente placeholder (es. "YOUR_STRIPE"), il QA Agent viene disattivato e il sistema solleva un'allerta di conformità bloccante.

---

## 4. Autocritica del Piano 4
- **Cosa ho migliorato:** Ho introdotto una gerarchia rigida che specchia un'azienda reale, eliminando la possibilità che gli specialisti controllino il proprio operato.
- **Cosa manca ancora:** Abbiamo la gerarchia, ma se il server o la sessione viene interrotta (restart, crash di corrente), non abbiamo descritto come recuperare lo stato senza rifare il lavoro (compito del Livello 5).
- **SCORE:** **9.3 / 10** (Struttura gerarchica solida).

---
⛓️ Trace P12: `RISTR-PIANO-04#gerarchia` · fonte: RISTRUTTURAZIONE-03-WORKFLOWS.md · migliorato da: [RISTRUTTURAZIONE-05-DEBUG-RIPRESA.md](RISTRUTTURAZIONE-05-DEBUG-RIPRESA.md)
