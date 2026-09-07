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

## AGGIORNAMENTO — 2026-09-07 pomeriggio (tutto misurato sul disco)

**Onda A: 9/9 catturate. Onda B: 8/8 catturate.** Comando che dice sempre la verità, perché conta
sul disco e non si fida di nessuna riga scritta a mano:

```
python "competitor/Andrei Pascu/site-study/scripts/stato_onde.py"
```

Fatto in questo giro, tutto committato:
- **Pre-mortem dell'esecuzione** (`site-study/PRE-MORTEM-ESECUZIONE.md`) — chiude l'obbligo 5 di
  GOD EMPEROR DOOM. Tre cause di fallimento già vive, non previste: zero teardown di copy su 16
  rapporti, 5 righe assorbite dalla Fabbrica contro ~2.400 di rapporti, tabella di stato che
  dichiarava 0 catture su un'onda che ne aveva 6.
- **`scripts/stato_onde.py`** — la contromisura unica: una pagina è "chiusa" solo con quattro file
  (scheda + rapporto + ATLANTE + COPY), e la sezione STATO di `ECOSISTEMA.md` la riscrive lui.
- **La macchina del funnel** (`reports/24-25-27-28-macchina-del-funnel.md`): quattro pagine di
  Onda B non vendono niente, sono i gradini verso la cassa. Triage corretta in `ECOSISTEMA.md`
  nello stesso turno. `/acquista-v101` è una pre-cassa nuova, non era in elenco: **l'Onda D va
  riaperta più grande di 14 pagine**.
- **ADR-024** — la legge della Fabbrica incassa §11 (la cassa ha un gradino) e §12 (l'accento si
  spende una volta), più due pattern decisi e quattro controlli per `gate_siti.py`.
  Assorbimento della legge: **da 5 righe a 14**.
- Rapporti nuovi: `18-20-apsales-servizi-COPY.md` (3.514 parole) e
  `18-20-apsales-servizi-COSTRUZIONE.md` (4.844 parole).

**✅ CHIUSA la discrepanza `RevealFooter`** (era «da verificare a mano»): letto il codice di
`RevealFooter-B34lvwld.js`, il wordmark blu è un `div` in flusso normale sempre visibile; il
pannello `bg-blue` `fixed` dentro `clipPath: inset(0)` è uno sticky reveal che si scopre con
`a = 1 - top/innerHeight` mentre si scorre. Lo screenshot coglie il fotogramma `a≈0`: **non era un
bug di cattura, era una foto di un'animazione legata allo scroll.**

**Debito aperto e misurato:** teardown di copy mancanti — 6 pagine di Onda A, 8 di Onda B (lo
elenca `stato_onde.py` da solo, sezione DEBITO DI COPY).

---

## LA PRIMA COSA DA FARE ALLA RIPRESA

**Misurare sul disco.** Non fidarsi di questa riga — vale anche per lei.
**Entrambe le sentinelle hanno consegnato prima della chiusura**: i quattro file ci sono e sono
committati (verificati sul disco, non riferiti). Restano da rileggere quando servono:

```
[FATTI E COMMITTATI 2026-09-07 08:28]
competitor/Andrei Pascu/site-study/reports/13-apsales-STACK-E-TOKEN.md   266 righe
competitor/Andrei Pascu/site-study/reports/13-apsales-ATLANTE.md         505 righe

[FATTI E COMMITTATI 2026-09-07 — tutti e quattro consegnati]
competitor/Andrei Pascu/site-study/reports/14-17-famiglia-out-CONFRONTO.md  327 righe
competitor/Andrei Pascu/site-study/reports/14-17-famiglia-out-ATLANTE.md    425 righe
```

**Gia' incassato da apsales.eu** (verificato, non riferito): stack **React + TanStack Start** provato
dalle stringhe `tanstack_router_reload` e dal pattern `createServerFn(...).handler(...)` nel bundle
— un gradino sopra `claude-speedrun.com`, che e' solo client. I sei token `--brand-*` convertiti da
OKLCH: `--brand-void #0a0a0b` · `--brand-pitch #111111` · `--brand-blue #0062ff` ·
`--brand-paper #f9f9f9` · `--brand-ink #1c1c1e` · `--brand-bone #eae8df` (dichiarata e mai usata).
**I due neutri coincidono quasi a cifra col nostro canone**, ma il colore d'azione e' **blu**, non
arancione: qui **nessun rischio di confusione di marca**, al contrario di claude-speedrun.
**Delta alla Fabbrica da lavorare:** il componente `Ascii` (blend `screen` + `contrast/brightness`
per immagini bianco-su-nero) e il **doppio bottone con clip-path animato** — una CTA che si fonde
con la sezione sottostante. **Una discrepanza aperta, non forzata:** `RevealFooter` dichiara
`bg-blue` su un layer `fixed` dentro `clipPath: inset(0)`, ma lo screenshot mostra fondo nero col
solo wordmark blu. Da verificare a mano.

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
