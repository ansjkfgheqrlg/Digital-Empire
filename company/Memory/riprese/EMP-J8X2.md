# EMP-J8X2 — STUDIO TOTALE ANDREI PASCU + FABBRICA SITI

- **Aperto:** 2026-09-07
- **Stato:** APERTA
- **Task:** Onde B-G del dossier 33, poi fusione `empire-premium-style` nella Fabbrica e canone v2
- **Checkpoint di origine:** [CP-20260907-ECX7](../checkpoints/CP-20260907-ECX7.md) — leggilo per primo

---

## Dove siamo

**Fabbrica Siti** (`.claude/skills/fabbrica-siti/`): Fase 1 chiusa (legge `CLAUDE-SITI.md` a 10
articoli + canone + ADR-023 due corsie), Fase 2 chiusa (8 pattern che girano + galleria generata).
Restano Fase 3 (flusso a 9 passi + `SKILL.md`), Fase 4 (`gate_siti.py` + `qa_sito.py`), Fase 5 (collaudo).

**Studio totale** (`PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`): l'ecosistema ha
**187 URL su 7 domini**, non 11. Triage e stato in
`competitor/Andrei Pascu/site-study/ECOSISTEMA.md` — **58 pagine da aprire**.
Onda A catturata (6 pagine), 1 rapporto scritto su 9.

---

## LA PRIMA COSA DA FARE ALLA RIPRESA

**Misurare sul disco.** Non fidarsi di questa riga — vale anche per lei.
Due sentinelle erano in corso alla chiusura della chat precedente e la loro notifica è andata persa.
Cercare questi quattro file:

```
competitor/Andrei Pascu/site-study/reports/13-apsales-STACK-E-TOKEN.md
competitor/Andrei Pascu/site-study/reports/13-apsales-ATLANTE.md
competitor/Andrei Pascu/site-study/reports/14-17-famiglia-out-CONFRONTO.md
competitor/Andrei Pascu/site-study/reports/14-17-famiglia-out-ATLANTE.md
```

Se ci sono: verificarli (i numeri devono essere **misurati**, non stimati) e committare.
Se mancano o sono a metà: rifarli. **I dati sono già tutti su disco**, non serve ricatturare niente.

---

## Poi, in ordine

1. **Pre-mortem formale** dell'esecuzione (obbligo 5 di GOD EMPEROR DOOM, rimasto aperto).
2. **Onda B** — le 8 pagine T2 mai viste. Comando pronto:
   `python scripts/site_capture2.py "<url>" --slug "<NN-nome>"`
   per `/outemail` · `/outviral` · `/vendita` · `/asa` · `/define` · `/mpo2` · `/armadeggon-strp` ·
   `/outfunnel-1` (tutte su `https://www.andrei-copy.com`).
3. **Onda C** (integrazione delle 7 catture vecchie), **Onda D** (la macchina del funnel: 14 pagine
   `-pre` e `pre-checkout` — **è la scoperta grossa**), **Onda E**, **Onda F** (corpus di 105 articoli).
4. Le tre sintesi: sistema visivo, sistema di copy, **metodo**.
5. **Fusione di `empire-premium-style`** dentro la Fabbrica (perimetro già scritto nel dossier 33 §5).
6. **Canone v2** + pattern nuovi.

---

## Trappole già pagate

- **Non fidarsi di una riga "RIPRESA DA": misurare sul disco.**
- **Niente batch di agenti paralleli oltre 2-3.** Sul run dei video il limite di spesa è stato
  colpito **due volte in meno di 24 ore**, sempre dentro batch paralleli.
- **`site_capture2.py` è idempotente:** se `scheda.json` esiste non rifà nulla. Serve `--force`.
- **Il rilevatore di costruzione non conosce ancora Vite/TanStack**: li chiama "artigianale".
  Verificare a mano dai nomi dei file in `src/_INDICE.json`.
- **La chat muore col contesto pieno:** chiudere e committare spesso.

---

## I file da riaprire

| File | Cosa |
|---|---|
| `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` | il piano, coi 7 giri di critica |
| `competitor/Andrei Pascu/site-study/ECOSISTEMA.md` | l'elenco vero e lo stato delle onde |
| `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` | dove deve finire tutto |
| `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` | la legge che riceve i delta |
| `reports/12-claude-speedrun-STACK-E-TOKEN.md` | il modello di profondità da imitare |
| `emperator.md` §6.20 · §6.22 · §6.23 | i principi imparati il 2026-09-07 |
