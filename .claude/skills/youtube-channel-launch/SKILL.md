---
name: youtube-channel-launch
description: >-
  Porta un canale YouTube da zero a "pronto a pubblicare": naming e posizionamento nella nicchia,
  identità visiva (logo, banner, palette), SEO di CANALE (descrizione, keyword, playlist, trailer,
  handle), format ripetibile, e roadmap di monetizzazione verso i requisiti YPP (1000 iscritti /
  4000 ore). Contiene il launch-gate che BLOCCA il lancio se il canale non è coerente o non è
  pronto. Usa questa skill quando apri un nuovo canale, quando riposizioni un canale esistente,
  quando un canale non cresce per incoerenza di nicchia, o quando pianifichi la monetizzazione.
  Comando: /yt-launch <nicchia>. NON usarla per il singolo video (quello è
  youtube-automation-factory) né per la gestione multi-canale (youtube-scale-ops).
type: interactive
theme: youtube-automation
version: "1.0"
---

# `youtube-channel-launch` — Skill kernel

> **"Un canale è una promessa fatta all'algoritmo: 'ogni volta che apro bocca, parlo di questo'.
> La coerenza è ciò che ti fa certificare."**
>
> **Invocazione:** `/yt-launch <nicchia> [--nome=<slug>] [--lingua=it]`
> **Trigger naturali:** "apro un canale nuovo su…", "come chiamo il canale?", "il canale non cresce",
> "quanto manca alla monetizzazione?", "devo riposizionare questo canale".

---

## ⚠️ Invarianti

1. **Un canale = una nicchia.** La coerenza è il meccanismo con cui YouTube capisce a chi mostrarti
   (certificazione SEO, MKD §2.1). Un canale "un po' di tutto" non si certifica mai.
2. **Format ripetibile prima del primo video.** Se non sai descrivere il tuo format in una riga,
   non sei pronto a lanciare (e non potrai scalare né delegare).
3. **Identità visiva coerente** tra logo, banner e miniature: le miniature sono l'identità vera del
   canale (è lì che l'utente ti riconosce nel feed).
4. **Monetizzazione = conseguenza, non obiettivo iniziale.** Prima il format che trattiene, poi i
   requisiti YPP arrivano. Un canale costruito per "arrivare a 1000 iscritti" produce contenuto povero.
5. **Il gate BLOCCA.** Niente primo video finché il `launch-gate` non è verde.

---

## 🔄 Pipeline (4 operativi + gate)

```
/yt-launch <nicchia>
   │
   ├─► [L1] channel-architect     → nome, handle, posizionamento, FORMAT ripetibile
   ├─► [L2] brand-designer        → logo, banner, palette, template miniature
   ├─► [L3] channel-seo           → descrizione canale, keyword, playlist, trailer
   ├─► [L4] monetization-planner  → roadmap YPP + stima RPM di nicchia
   │
   └─► ⟨launch-gate⟩   VERDE = puoi pubblicare il primo video · ROSSO = manca qualcosa
                         └──► handoff a youtube-automation-factory (Fase 1)
```

---

## 🤖 Squadra (4 operativi + 1 controllo)

| Classe | Agente | Fa | File |
|---|---|---|---|
| **Operativo** | `channel-architect` | nome, handle, posizionamento, format ripetibile | [agents/operatori/channel-architect.md](agents/operatori/channel-architect.md) |
| **Operativo** | `brand-designer` | logo, banner, palette, template miniature | [agents/operatori/brand-designer.md](agents/operatori/brand-designer.md) |
| **Operativo** | `channel-seo` | descrizione, keyword, playlist, trailer | [agents/operatori/channel-seo.md](agents/operatori/channel-seo.md) |
| **Operativo** | `monetization-planner` | roadmap YPP, RPM di nicchia, break-even | [agents/operatori/monetization-planner.md](agents/operatori/monetization-planner.md) |
| **Controllo** | `launch-gate` | BLOCCA il lancio se il canale non è pronto | [agents/controllo/launch-gate.md](agents/controllo/launch-gate.md) |

---

## 🗺 Routing
| Sei a | Vai a |
|---|---|
| Eseguire il lancio completo | [workflows/WF-channel-launch.md](workflows/WF-channel-launch.md) |
| Requisiti e conti di monetizzazione | [references/monetizzazione.md](references/monetizzazione.md) |
| Calcolo progresso YPP | `scripts/monetization_check.py` |

## 🔗 Integrazione
Precede `youtube-automation-factory` (che produce i video del canale lanciato). La nicchia validata
qui alimenta il `niche-gate` della factory. Portfolio multi-canale: `youtube-scale-ops`.
