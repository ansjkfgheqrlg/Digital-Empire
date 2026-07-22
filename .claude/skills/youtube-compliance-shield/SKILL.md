---
name: youtube-compliance-shield
description: >-
  Scudo di conformità per canali YouTube Automation. Verifica PRIMA della pubblicazione che un
  video replicato sia sufficientemente TRASFORMATO (non un re-upload), che non violi copyright su
  clip/musica/immagini, e che rispetti le policy YouTube su contenuto riutilizzato, monetizzazione
  e argomenti sensibili. Contiene il compliance-gate BLOCCANTE: se il video è un re-upload mascherato
  o ha materiale a rischio, la pubblicazione si ferma. Usa questa skill prima di ogni pubblicazione,
  quando un canale riceve un avvertimento/strike, quando la monetizzazione viene negata per
  "contenuto riutilizzato", o quando vuoi valutare il rischio di una nicchia. Comando:
  /yt-compliance <video|canale>. NON usarla per consulenza legale vincolante: è una checklist di
  rischio operativa, non un parere legale.
type: gate
theme: youtube-automation
version: "1.0"
---

# `youtube-compliance-shield` — Skill kernel

> **"Il canale che incassa è quello che sopravvive. Un re-upload ti fa guadagnare una settimana e
> ti costa il canale."**
>
> **Invocazione:** `/yt-compliance <video|canale> [--fonte=<url-originale>]`
> **Trigger naturali:** "posso pubblicare questo?", "rischio strike?", "mi hanno rifiutato la
> monetizzazione per contenuto riutilizzato", "questa nicchia è rischiosa?".

---

## ⚠️ Perché questa skill esiste (leggi prima di tutto)

Il metodo YouTube Automation replica video già validati — anche in altre lingue. È legittimo **solo
se il risultato è trasformato**: YouTube monetizza il contenuto **originale o significativamente
trasformato**, e penalizza il **"contenuto riutilizzato"** (re-upload, compilation senza apporto,
voce sintetica sopra il video di un altro).

**La differenza pratica:**
| ❌ Re-upload (rischio strike/demonetizzazione) | ✅ Trasformazione (accettabile) |
|---|---|
| Scarichi il video e lo ricarichi | Prendi **l'idea/struttura**, rifai da zero |
| Traduci l'audio e tieni il video originale | **Nuovo** script, **nuova** voce, **nuove** immagini |
| Usi le clip dell'originale | Immagini/clip da **archivio con licenza** (Fliki) o tue |
| Copi la miniatura | Miniatura **tua** |

La fabbrica Digital Empire produce con **Fliki** (voce nuova + immagini d'archivio + script
riscritto) → **è nel lato giusto**, ma solo se il `compliance-gate` lo verifica ogni volta.

---

## ⚠️ Invarianti non negoziabili

1. **Il gate BLOCCA, non suggerisce.** Se il punteggio di originalità è sotto soglia, non si pubblica.
2. **Si copia l'IDEA, mai i FILE.** Nessun asset (video, audio, miniatura) preso dall'originale.
3. **Ogni asset ha una provenienza dichiarata.** Se non sai da dove viene un'immagine, non entra.
4. **Nessun parere legale.** Questa è una checklist di rischio operativa. Per casi seri (diffida,
   strike ripetuti) serve un avvocato: la skill lo dice esplicitamente e si ferma.
5. **Nicchie sensibili = regole extra.** Salute, finanza, minori, notizie, contenuti scioccanti hanno
   requisiti più severi (monetizzazione limitata). Il `policy-checker` le segnala.

---

## 🔄 Pipeline (3 controlli + gate)

```
/yt-compliance <video> --fonte=<originale>
    │
    ├─► [C1] originality-auditor   → quanto hai TRASFORMATO? (script/voce/immagini/struttura)
    │                                 scripts/originality_score.py → 0-100
    ├─► [C2] copyright-scanner     → asset a rischio (musica, clip, loghi, immagini)
    ├─► [C3] policy-checker        → nicchia sensibile? monetizzazione? disclaimer necessari?
    │
    └─► ⟨compliance-gate⟩  VERDE = pubblica · GIALLO = correggi · ROSSO = BLOCCA
```

---

## 🤖 Squadra (3 operativi + 1 controllo)

| Classe | Agente | Fa | File |
|---|---|---|---|
| **Operativo** | `originality-auditor` | misura la trasformazione vs originale | [agents/operatori/originality-auditor.md](agents/operatori/originality-auditor.md) |
| **Operativo** | `copyright-scanner` | caccia asset a rischio (musica/clip/immagini/loghi) | [agents/operatori/copyright-scanner.md](agents/operatori/copyright-scanner.md) |
| **Operativo** | `policy-checker` | policy YouTube, nicchie sensibili, monetizzazione | [agents/operatori/policy-checker.md](agents/operatori/policy-checker.md) |
| **Controllo** | `compliance-gate` | verdetto BLOCCANTE verde/giallo/rosso | [agents/controllo/compliance-gate.md](agents/controllo/compliance-gate.md) |

---

## 🗺 Routing
| Sei a | Vai a |
|---|---|
| Regole YouTube in dettaglio | [references/policy-youtube.md](references/policy-youtube.md) |
| Eseguire il controllo completo | [workflows/WF-compliance-check.md](workflows/WF-compliance-check.md) |
| Punteggio originalità | `scripts/originality_score.py` |

## 🔗 Integrazione
Chiamata **obbligatoria** dalla Fase 5 di `youtube-automation-factory` (prima del `seo-gate`) e
dalla Fase di pubblicazione di `youtube-scale-ops` (batch). Orchestratore: `youtube-empire`.
