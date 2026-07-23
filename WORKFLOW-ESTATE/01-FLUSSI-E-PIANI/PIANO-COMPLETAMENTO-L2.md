---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/PIANO-COMPLETAMENTO-L1.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# PIANO COMPLETAMENTO WORKFLOW-ESTATE — **LIVELLO 2** (separazione, ladder, valore)
> 2026-07-23 · Claude · **Migliora L1** risolvendo i suoi 4 limiti dichiarati.
> A sua volta migliorato da [L3](PIANO-COMPLETAMENTO-L3.md).

## 0. Le 4 correzioni che L2 applica a L1

| Limite di L1 | Correzione L2 |
|---|---|
| Non separa il mio lavoro da quello di Max | **Regola della corsia**: ogni lavoro è `AUTO` (lo chiudo io) o `GATED` (serve Max). Un lavoro GATED non può bloccare un AUTO |
| Non ordina per valore | **Ordinamento per €/h** (regola P7 §7.1): incassa > compounding > vanity |
| "Fatto" non verificabile | Ogni lavoro ha una **DoD con comando**: se il comando non è verde, non è fatto |
| Nessuna ladder | **Ogni blocco ha 3 gradini**: primario → fallback → deferred. Nessun lavoro muore per un blocco esterno |

## 1. REGOLA DELLA CORSIA — chi può chiudere cosa

### 🔴 GATED — impossibili senza Max (NON si tentano, si preparano)
| # | Lavoro | Cosa serve da Max | Cosa preparo io comunque |
|---|---|---|---|
| G1 | Payment Link Stripe reali | 2 link creati su Stripe (base + bump) | tutto il resto del checkout, così che l'incollaggio del link duri 30 secondi |
| G2 | Pubblicazione YouTube | canale designato + credenziali API (M-EST-8) | video renderizzato + SEO pack pronti da caricare |
| G3 | Invio outreach reale | ok all'invio (G-A4) | messaggi generati, coda pronta, invio a `--dry-run` |
| G4 | Conferma Gate-CONTATTI / Gate-S4 / Gate-S5 | conferma umana esplicita | l'evidenza da confermare, calcolata dai dati veri |

**Corollario duro:** il Gate-FUNNEL resta 🔴 finché Max non crea i link Stripe. **Ma il funnel non deve restare morto**: la ladder di checkout va attivata comunque (vedi §3).

### 🟢 AUTO — li chiudo adesso, nessuno può bloccarli
A1 modulo `inspect` · A2 default-plus-veto automatico · A3 evidenza Gate-CONTATTI da `lead.csv` · A4 ladder checkout · A5 case study Novacar · A6 landing Preventa · A7 video YouTube via ladder · A8 S4 E2E carousel · A9 WF-MEM-EOD/RETRO eseguibili · A10 riparazione link + registrazione ADR-008.

## 2. ORDINAMENTO PER VALORE (sostituisce l'elenco piatto di L1)

| Rango | Lavoro | Perché qui | Stream |
|---|---|---|---|
| 🥇 1 | **Checkout che incassa** (A4) | è l'unico pezzo che trasforma traffico in € oggi. Landing senza checkout = zero | S2 |
| 🥈 2 | **Case study Novacar** (A5) | blocco n.1 dichiarato del dossier 23: "serve 1 prova credibile". Sblocca S6 E l'outreach workflow | S6 |
| 🥉 3 | **Landing Preventa** (A6) | destinazione dei 61 lead già scrapati. Senza, l'outreach porta a nulla | S6 |
| 4 | **Follow-up + evidenza contatti** (A3) | i lead esistono, le risposte no: il follow-up è dove sta la conversione | S1 |
| 5 | **Video YouTube E2E** (A7) | compounding, ma va DIMOSTRATO una volta o resta teoria per sempre | S5 |
| 6 | **inspect + EOD/RETRO** (A1, A9) | senza misura, i gate restano opinioni. Costo basso, abilita tutto il resto | MASTER |
| 7 | **default-plus-veto** (A2) | Gate-DEC è rosso per un bug di registrazione, non per un fatto | MASTER |
| 8 | **S4 E2E carousel** (A8) | regola Max: 100% auto o STANDBY. Va deciso, non lasciato ⏳ | S4 |
| 9 | **link + ADR-008** (A10) | igiene, non revenue | tutti |

### ❌ TAGLIATO da L2 (era in L1)
**S3 pubblicazione caroselli su `crea.illtuo_impero`.** Max ha misurato: pagina a ZERO (D-EST-006 risolto → Opzione B outbound freddo). Pubblicare 7 caroselli a zero follower è lavoro che *sembra* produttivo e non lo è.
→ **La fabbrica di caroselli si costruisce lo stesso (A8), la pubblicazione no.** L'asset resta pronto per quando ci sarà pubblico. Questo chiude anche Gate-S4 onestamente: E2E dimostrato = 🟢, pubblicazione = decisione separata.

## 3. LADDER — nessun lavoro muore per un blocco esterno

### L-CHECKOUT (sblocca il Gate-FUNNEL bloccato da G1)
1. **Stripe Payment Link** — appena Max li crea.
2. **Fallback attivo SUBITO**: pagina di pagamento con PayPal.me + bonifico + form ordine. Il visitatore può pagare **oggi**, non quando Max apre Stripe.
3. **Deferred**: mai. Un funnel senza modo di pagare non è un funnel.

> Design obbligatorio: **un solo file di configurazione** (`checkout.config.json`) con i link, e uno script che li inietta in tutte le pagine. Max incolla 2 link in un JSON → tutto il sito si aggiorna. Zero HTML modificato a mano.

### L-VIDEO (sblocca S5 con `FLIKI_API_KEY` vuota)
1. Fliki API — **morta oggi** (chiave vuota, verificato).
2. **Fallback**: script IT + stock/screen + TTS + montaggio `ffmpeg`.
3. **Deferred**: se manca anche ffmpeg → si consegna **pacchetto-video pronto al render** (script a scene, testo TTS, lista shot, SEO pack) e si dichiara `error --wf WF-YT-RENDER`. Non si finge un video.

### L-INVIO (sblocca S1 con G3 chiuso)
1. Invio reale — gated.
2. **Fallback**: coda generata + `--dry-run` verificato + messaggi pronti nominalmente. Max preme un tasto.
3. Deferred: mai.

## 4. DoD CON COMANDO (sostituisce i "fatto/non fatto" di L1)

| Lavoro | È finito SOLO se |
|---|---|
| A1 inspect | `python -m empire dash build` non stampa più `n/d (modulo inspect...)` su nessun KPI |
| A2 default-veto | `python -m empire flow gates` → Gate-DEC 🟢 |
| A3 contatti | `python -m empire flow gate Gate-CONTATTI` mostra l'evidenza reale contata da `lead.csv` |
| A4 checkout | `grep -r YOUR_STRIPE "Crea siti/"` → 0 risultati **e** la pagina ha un modo di pagare attivo |
| A5 case study | il PDF esiste su disco e contiene i numeri veri di Novacar (non lorem) |
| A6 landing Preventa | la pagina apre nel browser e ha CTA che punta a un contatto reale |
| A7 video | il file video esiste **oppure** esiste il pacchetto-render + `error` registrato |
| A8 S4 | un comando solo fa batch→QA→report e finisce con exit 0 |
| A9 EOD/RETRO | `python -m empire flow eod` scrive checkpoint e aggiorna dashboard |
| A10 igiene | `python -m empire conform WORKFLOW-ESTATE` → 0 block, 0 warn |

## 5. Limiti dichiarati di L2
- Dice *cosa* fare e *in che ordine*, ma non *chi lo esegue in parallelo*: non c'è disegno di swarm né perimetri disgiunti → **rischio collisione** (già successo: CP-20260719-008, Gael e Max sullo stesso file).
- Le DoD sono comandi, ma non c'è **un unico comando che dica "il Workflow Estate è finito"**.
- Nessun pre-mortem: non elenca cosa può andare storto durante la costruzione.
- Non dice cosa fare quando due lavori toccano lo stesso file (es. A1 e A9 toccano entrambi la dashboard).

➡️ **Questi 4 limiti sono l'input di L3.**

---
⛓️ P12: `PIANO-COMPL-L2#estate-2026` · migliora: L1 · migliorato da: [L3](PIANO-COMPLETAMENTO-L3.md)
