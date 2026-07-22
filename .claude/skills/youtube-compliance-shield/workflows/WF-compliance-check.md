# WF-COMPLIANCE-CHECK — controllo conformità pre-pubblicazione

> **Quando:** obbligatorio prima di ogni pubblicazione (Fase 5 della factory, o batch di scale-ops).
> **Esito:** verdetto VERDE / GIALLO / ROSSO. Solo il VERDE consente di pubblicare.

---

## DAG

```
INPUT: video prodotto (script + spec produzione + metadati + miniatura)
       + video originale replicato (url/struttura)
   │
   ├──────────────┬──────────────────┐        ← i 3 controlli girano IN PARALLELO
   ▼              ▼                  ▼
[C1]            [C2]               [C3]
originality-    copyright-         policy-
auditor         scanner            checker
   │              │                  │
   └──────────────┴──────────────────┘
                  ▼
          ⟨compliance-gate⟩          ← controllo indipendente, BLOCCANTE
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
   🟢 VERDE    🟡 GIALLO    🔴 ROSSO
   pubblica    correggi     NON pubblicare
               e ripassa    (rifai o scarta)
```

---

## Passi

| # | Chi | Fa | Output |
|---|---|---|---|
| 1 | conductor | raccoglie video prodotto + riferimento all'originale | input completo |
| 2 | `originality-auditor` | vota le 5 dimensioni, lancia `originality_score.py` | `originality-report.md` |
| 3 | `copyright-scanner` | inventario asset + provenienza + licenza | `copyright-report.md` |
| 4 | `policy-checker` | policy generali + nicchia sensibile + monetizzazione | `policy-report.md` |
| 5 | `compliance-gate` | applica la tabella di verdetto | `compliance-verdict.md` |
| 6 | conductor | VERDE → prosegui al `seo-gate`; GIALLO → torna all'operatore; ROSSO → stop | decisione |

**I passi 2-3-4 sono paralleli** (aree disgiunte → swarm, prompt idempotenti).

---

## Precondizioni (bloccanti)
- Esiste la spec di produzione con **l'elenco asset** (senza, il `copyright-scanner` non può lavorare).
- È noto **quale video** è stato replicato (senza, l'`originality-auditor` non ha il riferimento).

## Criteri di uscita
- Verdetto scritto e firmato.
- Se GIALLO: azioni assegnate a un operatore preciso + secondo passaggio pianificato.
- Verdetto registrato in memoria (anti-recidiva).

## Errori tipici
| Errore | Conseguenza | Prevenzione |
|---|---|---|
| Saltare il check "tanto è come gli altri" | strike/demonetizzazione a sorpresa | gate obbligatorio nel routing |
| Fare il check dopo la pubblicazione | danno già fatto | il gate è PRIMA del `seo-gate` |
| Far valutare il video a chi l'ha prodotto | auto-assoluzione | gate = agente indipendente |
