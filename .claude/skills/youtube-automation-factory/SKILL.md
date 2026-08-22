---
name: youtube-automation-factory
description: >-
  Fabbrica operativa per YouTube Automation / Cash Cow Channels. Trasforma il metodo Digital
  Empire (analisi Video IQ → nicchia + certificazione SEO → produzione Fliki → script hook/intro/CTA
  → pubblicazione ottimizzata → audit performance) in un workflow multi-agente con agenti che
  OPERANO, agenti che CONTROLLANO/verificano, sub-agenti di supporto e gate bloccanti. Usa questa
  skill quando devi: trovare/validare una nicchia, individuare un canale cash cow, scegliere quale
  video replicare, scrivere uno script, produrre un video in Fliki, ottimizzare i metadati SEO, o
  fare l'audit di un video pubblicato. Comando: /yt-factory <fase|obiettivo>. Costruita con la
  metodologia master-build-architecture (6 fasi, memoria dal passo zero, 7 sezioni canoniche per
  agente) + content-forge 2.0 (espansione, mai riassunto). NON usarla per editing video manuale
  frame-by-frame o per canali non-automation (vlog personali): è pensata per format ripetibili.
type: interactive
theme: youtube-automation
version: "1.0"
---

# `youtube-automation-factory` — Skill kernel

> **"Da nicchia a canale che incassa: analizza coi dati, certifica con la SEO, produci con Fliki,
> migliora coi feedback — in un flusso ripetibile con agenti che operano e agenti che controllano."**
>
> **Invocazione:** `/yt-factory <fase|obiettivo> [--nicchia=<slug>] [--canale=<id>] [--video=<url>]`
> **Trigger naturali:** "trova una nicchia YouTube", "questo canale è un cash cow?", "quale di questi
> due video conviene copiare?", "scrivimi lo script per…", "produci il video in Fliki", "ottimizza i
> metadati SEO", "com'è andato questo video pubblicato?".
>
> Base di conoscenza canonica: **[MKD.md](MKD.md)**. Mappa navigabile: **[ARCHITECTURE.md](ARCHITECTURE.md)**.

---

## ⚠️ Invarianti non negoziabili

1. **Account neutro per l'analisi.** Ogni analisi (Video IQ, nicchie, canali) va fatta da un profilo
   YouTube vergine/dedicato. Un profilo con cronologia distorce i dati → il `niche-scout` e il
   `video-hunter` lo verificano prima di produrre dati. *(fonte: regola Captain Hook)*
2. **Coerenza di nicchia = legge.** Un canale resta sulla sua nicchia. Il gate `niche-gate` blocca
   qualsiasi video che esca dalla nicchia certificata.
3. **Copi il successo, non gli errori.** Prima di replicare un video vincente, `seo-analyst` isola
   i suoi errori SEO; `script-writer`/`metadata-optimizer` li correggono.
4. **Gate prima di produrre e prima di pubblicare.** Nessuna produzione senza `niche-gate` VERDE;
   nessuna pubblicazione senza `seo-gate` VERDE. I gate BLOCCANO, non suggeriscono.
5. **Decisione su dati, mai su intuizione.** Ogni scelta (nicchia, canale, quale video copiare)
   cita metriche reali (views/ora, CTR, retention, punteggio SEO). Niente numeri inventati → se un
   dato non c'è, l'agente lo dichiara mancante.
6. **Memoria dal passo zero** (MBA invariante #1). Ogni run scrive checkpoint/decisioni in
   `memory/`. Nessun run è "fatto" finché non è salvato.
7. **Espansione, mai riassunto** (CF2 invariante #1) per gli artefatti di conoscenza (script, MKD,
   reference): si arricchisce, non si comprime.
8. **Canale attivo esclusivo: Legami d'Amore.** Dose Mentale è in pausa (richiesta Max,
   2026-08-13) — nessun agente ne tocca la configurazione o lo sceglie come target senza un nuovo
   ordine esplicito. Regole permanenti per Legami d'Amore: voce Fliki sempre femminile e
   realistica, sottotitoli presenti ma non troppo grandi, step miniatura skippabile
   temporaneamente (flag `--skip-thumbnail`), pubblicazione sempre PRIVATA (flag opt-in
   `--upload` per l'upload reale via Playwright) finché non arriva ordine esplicito di rendere
   pubblico. Vedi
   [WORKFLOW-LEGAMI-DAMORE-MASTER.md](../../../YOUTUBE-AUTOMATION-FACTORY/01-FLUSSI-E-PIANI/WORKFLOW-LEGAMI-DAMORE-MASTER.md).

---

## 🔄 Pipeline a 6 fasi (con feedback loop)

```
/yt-factory <obiettivo>
    │
    ▼
[Fase 1] SCOUTING          → niche-scout        (nicchia + cash cow, account neutro)
                             GATE: niche-gate    (coerenza + potenziale)
[Fase 2] SELEZIONE VIDEO   → video-hunter        (trova candidati, views/ora)
                           → seo-analyst          (punteggio SEO + errori del target)
                             DECISIONE: A upside / B sicurezza  (momento chiave)
[Fase 3] SCRIPT            → script-writer        (hook→intro→corpo→CTA, corregge errori)
[Fase 4] PRODUZIONE        → video-producer       (spec Fliki: voce/musica/transizioni/export)
                             GATE: niche-gate      (il video resta in nicchia?)
[Fase 5] PUBBLICAZIONE     → metadata-optimizer   (titolo/descr/tag/thumb/sottotitoli)
                             GATE: seo-gate        (metadati a norma? BLOCCA se no)
[Fase 6] AUDIT             → performance-auditor   (views/ora, CTR, retention → diagnosi)
                             └──► feedback a Fase 1/2 (miglioramento continuo)
```

Contratto di ogni fase e handoff: [ARCHITECTURE.md](ARCHITECTURE.md).

---

## 🤖 Roster agenti (conductor + 7 operatori + 4 controllori + 2 supporto)

| Classe | Agente | Fa | File |
|---|---|---|---|
| **L1** | `conductor` | orchestra tutto, unico che parla all'utente | [agents/conductor.md](agents/conductor.md) |
| **Operatore** | `niche-scout` | trova/valida nicchia + cash cow (Video IQ) | [agents/operatori/niche-scout.md](agents/operatori/niche-scout.md) |
| **Operatore** | `video-hunter` | trova video da replicare (views/ora, cross-lingua) | [agents/operatori/video-hunter.md](agents/operatori/video-hunter.md) |
| **Operatore** | `seo-analyst` | punteggio SEO + errori del video target | [agents/operatori/seo-analyst.md](agents/operatori/seo-analyst.md) |
| **Operatore** | `script-writer` | script hook→intro→corpo→CTA (corregge errori) | [agents/operatori/script-writer.md](agents/operatori/script-writer.md) |
| **Operatore** | `video-producer` | spec di produzione Fliki + export | [agents/operatori/video-producer.md](agents/operatori/video-producer.md) |
| **Operatore** | `thumbnail-designer` | genera prompt AI e layout grafico miniatura | [agents/operatori/thumbnail-designer.md](agents/operatori/thumbnail-designer.md) |
| **Operatore** | `metadata-optimizer` | metadati SEO pre-pubblicazione | [agents/operatori/metadata-optimizer.md](agents/operatori/metadata-optimizer.md) |
| **Controllo** | `niche-gate` | BLOCCA video fuori nicchia / a basso potenziale | [agents/controllo/niche-gate.md](agents/controllo/niche-gate.md) |
| **Controllo** | `qa-audio-video` | BLOCCA video con audio/video o pronunce difettose | [agents/controllo/qa-audio-video.md](agents/controllo/qa-audio-video.md) |
| **Controllo** | `seo-gate` | BLOCCA pubblicazione se metadati non a norma | [agents/controllo/seo-gate.md](agents/controllo/seo-gate.md) |
| **Controllo** | `performance-auditor` | audit post-pubblicazione + diagnosi errori | [agents/controllo/performance-auditor.md](agents/controllo/performance-auditor.md) |
| **Supporto** | `memory-keeper` | checkpoint/decisioni, coerenza memoria | [agents/supporto/memory-keeper.md](agents/supporto/memory-keeper.md) |
| **Supporto** | `self-improver` | ricalcola learned_rules.json dalle metriche | [agents/supporto/self-improver.md](agents/supporto/self-improver.md) |

Il conductor **sei tu** (l'istanza che invoca la skill). Gli altri sono subagenti spawnati via Agent
tool quando la fase lo richiede, oppure — per run leggeri — eseguiti inline seguendo il loro spec.

---

## 🗺 Routing rapido

| Sei a | Vai a |
|---|---|
| Capire il metodo completo | [MKD.md](MKD.md) |
| Come si concatenano le fasi | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Eseguire una fase | `workflows/WF*-*.md` |
| Leggere le metriche Video IQ | [references/video-iq-analisi.md](references/video-iq-analisi.md) |
| Certificare la SEO di nicchia | [references/seo-certificazione.md](references/seo-certificazione.md) |
| Teoria hook/intro/CTA | [references/teoria-script.md](references/teoria-script.md) |
| Produrre in Fliki | [references/fliki-produzione.md](references/fliki-produzione.md) |
| Punteggio SEO deterministico | `scripts/seo_score.py` |
| Check cash cow / views-ora | `scripts/cashcow_check.py` |
| Auto-miglioramento | `scripts/self_improve.py` |
| Conformità Monetizzazione | [references/monetizzazione-compliance.md](references/monetizzazione-compliance.md) |
| SSML e Dizionario Fliki | [references/fliki-avanzato.md](references/fliki-avanzato.md) |
| APEX-7 Orchestrator | `scripts/apex7_orchestrator.py` |

---

## 🚦 Quando NON usare questa skill
- Editing video manuale frame-by-frame (usa un editor, non la fabbrica).
- Canali non-automation (vlog personali, personal brand con volto): il metodo assume format
  ripetibile e produzione AI.
- Richiesta di far crescere follow in modo non organico / acquisto view: fuori scope e non supportato.

## 📖 Per il conductor
Prima di procedere leggi il tuo system prompt completo in [agents/conductor.md](agents/conductor.md):
lì trovi come parlare all'utente, come gestire lo stato del run, quando spawnare cosa e come
applicare gli invarianti e i gate.
