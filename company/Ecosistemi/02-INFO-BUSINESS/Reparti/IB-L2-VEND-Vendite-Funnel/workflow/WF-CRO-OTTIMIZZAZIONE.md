---
Type: CONCEPT
Status: Active
Tags: #workflow #vendite #funnel #cro #ab-testing #IB-L2-VEND
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-CRO-OTTIMIZZAZIONE — Ciclo Continuo di Ottimizzazione del Funnel

> **Workflow:** WF-CRO-OTTIMIZZAZIONE · **Reparto:** IB-L2-VEND Vendite & Funnel
> **Trigger:** loop settimanale evergreen o anomalia metrica rilevata da IB-VEND-TRACK
> **Output:** variante adottata (o scartata con rationale) in `infobusiness/vendite/funnel/tests/`
> **Gate di uscita:** nessun test "conclusivo" prima del campione minimo; risultato documentato

---

## Scopo

Ciclo continuativo di ottimizzazione del funnel basato su dati reali. **Un test A/B alla volta**,
nessuna conclusione su campione sotto il minimo statistico (calcolato da IB-VEND-CRO), un solo
elemento cambiato per esperimento. L'obiettivo è migliorare la conversione in modo difendibile,
non inseguire variazioni da rumore statistico. Framework di riferimento: ICRO
(`Lancio corso skill beast/Framework_ICRO_Digital_Empire.pdf`).

---

## Trigger

```json
{
  "evento": "loop_settimanale | anomalia_metrica",
  "prodotto_id": "...",
  "step_critico": "step con conversione più bassa (da IB-VEND-TRACK)",
  "traffico_giornaliero": 200
}
```

---

## Input JSON

```json
{
  "prodotto_id": "...",
  "metriche_step": {"opt_in": 0.30, "salespage_ctr": 0.18, "checkout": 0.04},
  "baseline_step_target": 0.04,
  "delta_minimo_rilevabile": 0.01,
  "vincoli": ["1 solo elemento per test", "no scarcity falsa", "rollout su % traffico"]
}
```

---

## Pipeline (step + owner)

```
[1] IB-VEND-TRACK — analisi settimanale
  → aggrega metriche per step → identifica lo step con conversione più bassa (collo di bottiglia)
  → output: report con step critico + baseline

[2] IB-VEND-CRO — formula ipotesi falsificabile
  → NON "proviamo a vedere" ma "se cambio X, mi aspetto +Y perché Z"
  → seleziona 1 SOLO elemento da cambiare
  → calcola il campione minimo statistico (baseline + delta minimo rilevabile)

[3] IB-COORD-VENDITE — approvazione
  → verifica: ipotesi chiara? 1 solo elemento? campione calcolato? no manipolazione?
  → se ok: autorizza rollout su % traffico (NON su tutto)

[4] Rollout — variante su % traffico
  → split definito (es. 50/50); attesa dati fino al campione minimo
  GATE: il test resta "in_corso" finché il campione minimo non è raggiunto

[5] IB-VEND-CRO — analisi e decisione
  → campione minimo raggiunto → delta significativo?
     → vincitore variante → ADOTTA + documenta
     → vince il controllo → SCARTA variante + documenta
     → inconcludente → RIPETI o cambia ipotesi
  → documenta SEMPRE (anche se scartato) in funnel/tests/{test_id}.json
```

---

## Gate

| Gate | Owner | Criteri |
|---|---|---|
| G-IPOTESI | IB-COORD-VENDITE | Ipotesi falsificabile + 1 solo elemento + campione calcolato + no manipolazione |
| G-CAMPIONE | IB-VEND-CRO | Nessuna conclusione prima del campione minimo statistico |
| G-DOC | IB-VEND-CRO | Ogni test (adottato o scartato) documentato con rationale |

---

## Output JSON

```json
{
  "test_id": "vend-cro-2026XXXX-NN",
  "prodotto_id": "...",
  "step_target": "checkout",
  "ipotesi": "prezzo+garanzia sopra la piega → +1pp conversione checkout",
  "elemento_cambiato": "posizione blocco prezzo+garanzia",
  "campione_minimo": 1200,
  "split": "50/50",
  "esito": {"vincitore": "variante | controllo | inconcludente", "delta": "+1.4pp", "significativo": true},
  "decisione": "adotta | scarta | ripeti",
  "rationale": "..."
}
```

---

## Handoff

| Direzione | A | Payload | Quando |
|---|---|---|---|
| ← IB-VEND-TRACK | interno | metriche_step + step critico | inizio ciclo (step 1) |
| → IB-VEND-SALESPAGE / CHECKOUT | interno | variante da implementare | dopo adozione (step 5) |
| → IB-VEND-OFFER | interno | flag "problema offerta, non copy" | se conversione < 1% dopo 500 visite |
| → ib-director | escalation | revisione offerta | conversione sistematicamente bassa |

---

## Dry-run (esempio)

**Trigger:** loop settimanale "Vendi la Skill". IB-VEND-TRACK: opt-in 30%, salespage CTR 18%,
checkout 4% (collo di bottiglia).

1. IB-VEND-TRACK: step critico = checkout (4%), baseline confermata su 1.000 sessioni/settimana.
2. IB-VEND-CRO: ipotesi = "mostrare la garanzia 30gg accanto al bottone di pagamento riduce
   l'ansia da acquisto → +1pp". Elemento cambiato: SOLO il badge garanzia nel checkout.
   Campione minimo calcolato: 1.200 sessioni per ramo.
3. IB-COORD-VENDITE: ipotesi chiara, 1 elemento, campione calcolato → approva rollout 50/50.
4. Rollout: 11 giorni per raggiungere il campione. A giorno 6 la variante "sembra" vincere
   (+2pp) ma il campione non è raggiunto → IB-VEND-CRO NON conclude (G-CAMPIONE).
5. Giorno 12: campione raggiunto. Delta = +1.3pp, significativo → ADOTTA. Documentato in
   `funnel/tests/vend-cro-20260630-01.json` con rationale. Variante implementata nel checkout.

**Esito:** +1.3pp conversione checkout, test documentato, ciclo pronto a ripartire sul prossimo collo.

---

## Connessioni

- [[ib-vend-cro]] · `agenti/ib-vend-cro.md`
- [[ib-vend-track]] · `agenti/ib-vend-track.md`
- [[ib-coord-vendite]] · `agenti/ib-coord-vendite.md`
- [[WF-FUNNEL-EVERGREEN]] · `workflow/WF-FUNNEL-EVERGREEN.md`
- [[KPI]] · `kpi/KPI.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — test onesti)
