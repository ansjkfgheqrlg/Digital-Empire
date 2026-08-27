---
Type: TOOL
Status: Active
Tags: #pubblicazione #instagram #social #automazione #caroselli #playwright
Created: 2026-08-27
Last updated: 2026-08-27
---

# Tool — Workflow Pubblicazione Automatica

## Overview
Il braccio di **pubblicazione** di Digital Empire: prende contenuti già pronti (caroselli,
reel) e li porta sui canali social senza passaggi manuali. Vive in
`SKILL & Agenti/Workflow pubblicazione automatica/` e ha un `REGOLE.md` di confinamento —
si lavora **solo** dentro quella cartella, si esce solo per leggere.

Dal 2026-08-27 (TASK-PUBLISHER-W1) ha **un solo ingresso**: `pubblica.py`. Prende una
cartella di output già pronta e la pubblica sul canale giusto, oppure fa un dry-run
verificato. È il pezzo che chiude la catena iniziata da
[[Progetto_Preventa_Carousel]]: prima i caroselli venivano generati e poi restavano lì.

## Il comando

```bash
cd "SKILL & Agenti/Workflow pubblicazione automatica"
python pubblica.py "<cartella>"          # dry-run VERIFICATO (default, sicuro)
python pubblica.py "<cartella>" --live   # pubblica davvero
```

Input: una cartella con `slide_01.png … slide_NN.png` + `caption.txt` — esattamente il
formato che produce l'Arsenale Caroselli. Quattro passi, tutti con esito reale:

1. **Contenuto** — legge gli header dei PNG: dimensioni, aspect ratio nel range IG
   0.80–1.91, peso ≤8MB, ≤10 slide, caption ≤2200 caratteri, ≤30 hashtag, dedup su
   `published.json`.
2. **Canale** — dedotto dal percorso; pubblica solo su canali con un motore reale,
   gli altri li **blocca dicendo perché**.
3. **Sessione** — apre il **browser vero**, va sul social, salva uno screenshot in
   `_diagnostica/`. Non è una stampa: è una verifica.
4. **Esito** — `0` PASS · `1` FAIL · `2` PASS PARZIALE (contenuto pronto, sessione no).

Il `--live` **si auto-rifiuta** se la sessione non è autenticata.

## Stato reale dei canali (2026-08-27, verificato eseguendo)

| Canale | Account | Stato |
|---|---|---|
| Instagram Agency | @digitalempireagency.e | ✅ motore reale, manca solo il login una tantum |
| LinkedIn | Digital Empire | ⚠️ il publisher importa, **mai** eseguito end-to-end |
| Instagram Mentalità | @mentalita.brutale | ⚠️ publisher Reel presente, mai testato |
| TikTok | Codice dei Potenti | ❌ non importa (`import config` rotto) → B-026 |

**Nessun canale ha una `session_data/` salvata**: è il vero blocco al live, non il codice.

## Il principio: niente PASS finti
Il folder conteneva tre pezzi che dichiaravano successo senza averne titolo — un
publisher "ufficiale" che era una simulazione con `requests.post` commentata, un
orchestratore che stampava "COMPLETATO CON SUCCESSO" incondizionatamente, e un
`publish()` che ingoiava ogni eccezione. Per questo `pubblica.py` ha **tre** esiti e non
due: così "contenuto pronto ma sessione mancante" non può travestirsi da successo.
Diagnosi completa e onesta in `DIAGNOSI-PUBLISHER.md` dentro la cartella.

Stesso principio già applicato altrove nell'Impero: il gate KDP che distingue COMPLETO da
CARICABILE ([[Tool_Pipeline_Libri_KDP]]), e l'audit YouTube che si rifiuta di scrivere
metriche su video mai pubblicati.

## Architettura — wrapping, non riscrittura
`pubblica.py` non riscrive nessun motore (ADR-003): wrappa
`scripts/ig_carousel_publish.py`, l'unico publisher del folder con login, carosello
multi-slide ed esito onesto `bool`. Quel motore era già buono: era **l'ingresso** a
essere morto (puntava alla cartella di un'altra macchina). La task diceva "portarlo a uno
stato usabile da un comando, non ricostruirlo" — era letteralmente vero.

## Prossimo passo
1. Chiudere **B-023** (password Instagram in chiaro sul repo pubblico) — va cambiata
   **prima** del login, o invalida la sessione appena creata.
2. `python Instagram/setup_session.py` — login manuale una tantum (lo fa un umano).
3. Primo `--live` reale, solo con ok esplicito di Max.

## Connessioni
- [[Progetto_Preventa_Carousel]] — produce le cartelle che questo tool pubblica
- [[Tool_Pipeline_Libri_KDP]] — stesso principio di gate onesto; futuro consumatore (promo libri)
- [[Tool_APEX7_Core_Motore_Condiviso]] — il motore di orchestrazione canonico dell'Impero
- [[Digital_Empire_6_Phase_Process]] — dove la pubblicazione si colloca nel processo
