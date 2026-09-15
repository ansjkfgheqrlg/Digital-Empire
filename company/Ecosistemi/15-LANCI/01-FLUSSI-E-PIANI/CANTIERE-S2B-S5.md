# CANTIERE — S2b → S5, la struttura completa (2026-09-15, Emperator per Gael)

Ordine di Gael: «concludi con i lanci, con la struttura completa e tutto». Assetto GOD EMPEROR DOOM.
Questo file è il piano battuto (§6.8/§6.20 della dottrina) e il pre-mortem (ADR-006). Si legge
prima del checkpoint di chiusura; i giri restano scritti perché si veda cosa è stato scartato.

## 1. Il piano — tre giri

**P0 (prima idea).** Un solo costruttore che fa in sequenza MT-3XWC → MT-4GNU → MT-GHZ6 → MT-GEKH →
MT-69CE → MT-RGZ6, come la numerazione delle micro-task suggerisce.
*Obiezione più forte:* 6 scaglioni in fila su una sessione sola = 60-90 ore-uomo di stima (documento
04 §2) in un turno; e S2c/S2d/S3/S4 sono aree di scrittura **disgiunte** dal motore — ADR-006 impone
lo swarm sopra le due aree. P0 è pigrizia travestita da ordine.

**P1.** Cinque forze in parallelo: motore (S2b + ponte), gate S2 (rossi prima), gate S3+S4+governo,
agenti, piano automazione. *Obiezione:* tre mani scrivono sugli stessi oggetti — `stato.json`, i
verdetti, `lancio.py` — senza un contratto: la collisione è certa, e i test di una mano dipendono dal
codice di un'altra che non esiste ancora.
*Assorbito:* prima di lanciare chiunque ho scritto **io** `scripts/gates/_comune.py` (Verdetto,
Rete/ReteFinta, esegui_gate, trova_gate) e `CONTRATTO-STATO.md` (campi di stato.json, verbali con
chiave (controllo, tentativo), registro-chiamate, tabella gate↔transizione). Ogni prompt cita solo
quei due file come legge e un perimetro di scrittura che non si sovrappone a nessun altro. I
comandi S5 (`blocchi`, `costi`) vivono in `governo.py` — modulo a parte — e il cablaggio dentro
`lancio.py` lo faccio io dopo, unica mano.

**P2.** *Obiezione a P1:* la condizione di sblocco di S2 («`crea prova-vuota` + `avanza` si ferma
al controllo dell'offerta, codice 1») è **contraddittoria** letta alla lettera: un lancio vuoto si
ferma al primo gate (PUB), non all'offerta. E i gate che aprono link (PRD, INT, FNL) o «passano»
finto nei test — Legge Suprema violata — o richiedono la rete vera in `pytest`.
*Assorbito:* (a) `Rete` è un'interfaccia iniettata: `ReteFinta` solo nei test, `ReteVera` nel CLI,
mai un gate che finge da solo; (b) `lancio crea X --con-esempio` copia `05-TEMPLATES-E-KIT/esempio/`
(artefatti validi PUB..PRV, offerta solo PROPOSTA) → con la rete vera `avanza` arriva **davvero**
a GATE-OFF-1 e blocca con codice 1 perché non c'è firma; il lancio letteralmente vuoto blocca a
GATE-PUB-1 con lo stesso codice 1 — entrambi verbale scritto, stato invariato. Dichiarato, non
aggirato.

**P3 (taglio dell'ambizione).** *Obiezione a P2:* il ponte ADR-014 con chiamate vere a `claude -p`
in questo turno costa denaro e non è verificabile in un test; il promemoria giornaliero come task di
Windows registrato sulla macchina di Gael senza chiederglielo è un'invasione; la registrazione
(REGISTRO-IMPRESA, skills-map, wiki) da cinque mani è un conflitto sicuro.
*Assorbito:* il ponte ha un `esecutore` iniettabile e i test non lanciano mai `claude`; nessuna
chiamata vera in questo turno (dichiarato nel checkpoint: il ponte è **provato con un esecutore
finto**, non in produzione); il promemoria è uno script + istruzioni `schtasks`, non un task
installato; la registrazione la faccio io, alla fine, in un solo commit.

**Cosa resta fuori per infattibilità o perché è di Max (ADR-028: non ferma il resto):** S0 gesti
5-6 (MT-F37C: evento d'acquisto e commissioni **sulla transazione vera**) e MT-32RU/MT-CV7N
(pagamento vero con carta vera) — servono i Payment Link Stripe e la carta di Max; la rotazione
della chiave Brevo sul pannello (MT-FJF6 metà umana); la firma su prezzo e data del Manuale.
Il lancio del Manuale **non si apre** comunque: pubblico verificato zero (CP-20260910-UNUE).

## 2. Pre-mortem — è il 16 settembre e questa costruzione è fallita. Perché?

| # | Causa | Segnale che la vede | Contromisura in vigore |
|---|---|---|---|
| 1 | Le cinque mani hanno scritto codice che non si incastra: i gate ritornano una cosa, il motore ne aspetta un'altra | `pytest tests` rosso dopo l'integrazione; `avanza` esce 3 «controllo non costruito» anche coi moduli presenti | contratto scritto **prima**, perimetri disgiunti, integrazione fatta da una sola mano con i test di tutti eseguiti insieme |
| 2 | Un gate «passa» perché finge (rete finta dentro il gate, campo `valido` letto dal file) — il PASS finto di `push_social.py` sotto altro nome | un test verde che non tocca mai `Rete`; un gate che legge `stato.json` | `Rete` iniettata, `ReteFinta` solo in `tests/`; review indipendente mia con `grep -n "urllib\|stato.json" scripts/gates/` prima del commit |
| 3 | La forma è completa e la sostanza no: 14 gate, 15 agenti, 0 lanci che avanzano davvero | `lancio avanza manuale-claude-code` esce 3 o solleva | la definizione di FATTO di ogni forza è un **comando eseguito**, e la mia verifica finale rilancia tutto: `pytest`, `valida_registro.py`, `verifica_agenti.py`, `avanza` sul lancio vero, `governo blocchi` |

## 3. Le verifiche di chiusura (le eseguo io, non le credo)

```
cd company/Ecosistemi/15-LANCI/02-AUTOMAZIONI-E-SCRIPTS
PYTHONIOENCODING=utf-8 python -m pytest tests -q                       # tutto verde
PYTHONIOENCODING=utf-8 python -m scripts.lancio crea prova-s2 --prodotto Prova --con-esempio
PYTHONIOENCODING=utf-8 python -m scripts.lancio avanza prova-s2         # codice 1 a GATE-OFF-1
PYTHONIOENCODING=utf-8 python -m scripts.lancio avanza manuale-claude-code  # il lancio vero: codice e causa
PYTHONIOENCODING=utf-8 python -m scripts.governo blocchi
PYTHONIOENCODING=utf-8 python scripts/verifica_agenti.py               # 15/15
cd ../../../../PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati && PYTHONIOENCODING=utf-8 python valida_registro.py  # 0
```
