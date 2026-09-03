# 14 — TESORERIA

> **L'organo che conta i soldi di Digital Empire.**
> Nato il 2026-09-03 su ordine di Max. Decisione: [ADR-020](../../Memory/decisions/ADR-020-reparto-tesoreria.md).

---

## Perché esiste

Misurato il 2026-09-03: **Digital Empire non misurava un solo euro.** Né incassi, né costi
effettivi, né una metrica del percorso di vendita.

Il direttore finanziario sorvegliava le spese di un'azienda che non aveva mai contato un
ricavo. Lo stato della pipeline commerciale era un'opinione. **Ed è per questo che nessuno
si era accorto che il magazzino era pieno**: 25 pezzi di lavoro finito mai pubblicati, il
più vecchio fermo da 135 giorni, zero vendite documentate ([ADR-016](../../Memory/decisions/ADR-016-ultimo-metro.md)).

Chiude la voce di backlog **B-043**.

---

## Come si usa — cinque comandi

```bash
# un euro che entra
python scripts/tesoreria.py entrata --importo 1500 --da "Cliente" \
    --per agency --stato incassato --nota "sprint CRO settembre"

# un euro che esce
python scripts/tesoreria.py spesa --importo 20 --a "Anthropic" \
    --categoria strumenti --ricorrente

# un previsto che e' arrivato davvero
python scripts/tesoreria.py incassa --id E-20260903-001

# il quadro
python scripts/tesoreria.py report
python scripts/tesoreria.py report --mese 2026-09
python scripts/tesoreria.py report --scrivi
```

---

## Gli organi

| Organo | Dove | Mestiere |
|---|---|---|
| Motore | `scripts/tesoreria.py` | registra, calcola, riferisce |
| Comando | `.claude/skills/tesoreria/` | come si usa |
| Capo | `.claude/agents/tesoreria-conductor.md` | qualunque domanda sui soldi |
| Entrate | `.claude/agents/tesoreria-entrate.md` | ogni euro che entra, e quelli che non arrivano |
| Spese | `.claude/agents/tesoreria-spese.md` | ogni euro che esce, e gli sprechi che nessuno vede |
| Rapporto | `.claude/agents/tesoreria-report.md` | il quadro, pronto sempre |
| Previsione | `.claude/agents/tesoreria-previsione.md` | quanto durano i soldi |

**I dati veri:** `company/Memory/tesoreria/` — due file di testo, una riga per movimento.
**Il rapporto:** `company/Memory/TESORERIA.md`, rigenerato a ogni esecuzione.

---

## Le tre leggi

1. **Previsto non è incassato. Mai.** I due numeri restano separati, anche quando la somma
   farebbe più bella figura.
2. **Un numero che non esiste si dichiara, non si stima.** Una stima presentata come misura
   è il male che questo reparto esiste per curare.
3. **La storia dei soldi non si riscrive, si annota.** Un errore si corregge accodando la
   rettifica. Chi cancella una riga sta cancellando una prova.

---

## Il vincolo di sopravvivenza

Una tesoreria vive o muore su una cosa sola: **che qualcuno registri i movimenti.**

Un movimento annotato tre giorni dopo è un movimento perso. Un mese saltato rende
inservibile il confronto. **Il primo movimento va registrato oggi** — anche uno solo,
anche piccolo: un registro vuoto e un registro che non esiste si assomigliano troppo.

---

## Cosa NON copre

- **il percorso di vendita** (contatti, chiamate, preventivi, chiusure) → voce B-049,
  è il prossimo buco da chiudere
- **tasse e commercialista** — la soglia SRL è un numero che si consegna al CFO
- **l'autorizzazione delle spese**, che resta del `cfo-empire`
- **⚠️ non esiste ancora un tetto di spesa in euro**: le soglie del CFO sono percentuali
  di un denominatore mai fissato (B-048)

---

*Supervisore: `cfo-empire` · Ordine: Max, 2026-09-03 · Decisione: ADR-020*
