> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 4.2

# WF-YT-CALENDAR — Calendario editoriale 30 giorni

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Strategia · **Fase:** 1 — Ricerca/Strategia
**Owner gate:** `mb-yt-strategy-coord` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Pianificare il calendario editoriale per 30 giorni su un canale specifico: titoli provvisori,
keyword target per video, slot di pubblicazione, cadenza rispettosa dei gate. Il calendario è
l'unica fonte di autorità per il reparto YT-Produzione: non si compila un brief senza slot calendario.

## Input

| Campo | Fonte |
|---|---|
| brand_kit canale (output WF-YT-CHANNEL-LAUNCH) | `mb/yt/<canale-slug>/brand_kit.yaml` |
| Keyword map della niche (output WF-YT-NICHE + T-keyword-yt) | `mb/yt/<canale-slug>/keywords.yaml` |
| Pattern editoriali `[da F-MB1]` | wiki `sources/` canali riferimento |
| Analisi retention (WF-YT-ANALYTICS — se canale già avviato) | `mb/yt/<canale-slug>/analytics/` |

## Processo (step interni)

1. `mb-yt-keyword-miner`: espande la keyword map con keyword secondarie, trending e stagionali
2. `mb-yt-calendar-planner`: seleziona 30 topic distinti (similarity check anti-ripetitività)
3. `mb-yt-calendar-planner`: assegna keyword primaria e secondaria a ogni slot
4. `mb-yt-calendar-planner`: distribuisce gli slot rispettando la cadenza di pubblicazione
5. `mb-yt-strategy-coord`: revisione finale calendario → salvataggio

## Schema calendario (un slot per video)

```yaml
slot:
  - data: "YYYY-MM-DD"
    giorno_settimana: ""
    titolo_provvisorio: ""
    keyword_primaria: ""
    keyword_secondarie: []
    formato: "long_form | short | entrambi"
    durata_target_minuti: 0
    angolo: ""           # elemento differenziante rispetto ai precedenti
    priorita: "alta | media | bassa"
    stato: "pianificato | in_produzione | pubblicato | saltato"
```

## Cadenza (regole non negoziabili)

- **Warm-up (settimane 1-4):** 2-3 video/settimana + 1-2 Shorts/giorno
- **Regime (mese 2+):** `[da F-MB1: cadenza reale dei canali riferimento]` — default 3-5/settimana SE gate reggono
- **Regola fondamentale:** la cadenza NON supera mai la capacità dei gate. Qualità > volume.
  Se i gate rallentano → si riduce la cadenza, mai si abbassano i criteri.
- **Anti-ripetitività:** nessun topic simile agli ultimi 5 video pubblicati sullo stesso canale

## Multi-canale

Con N canali attivi, `mb-conductor` gestisce N calendari in parallelo tramite swarm
(`mb-yt-calendar-planner` clonato per canale, namespace `mb/yt/<canale-slug>/calendar/`).
I namespace sono isolati — `mb/yt/patterns` contiene i pattern cross-canale (titoli vincenti,
topic con alta retention) che alimentano tutti i calendari senza cross-contaminazione contenuti.

## Acceptance criteria

- Calendario 30 slot completato (nessun buco non giustificato)
- Nessun titolo/topic duplicato o con similarity > soglia vs ultimi 20 video del canale
- Keyword primaria assegnata a ogni slot
- Salvato in `mb/yt/<canale-slug>/calendar/YYYY-MM.yaml` + log wiki
