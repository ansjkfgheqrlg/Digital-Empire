---
Type: REGISTRO
Status: Active (append-only)
Tags: #ispettorato #successi #pattern-vincenti
Created: 2026-07-20
Last updated: 2026-07-20
---

# REGISTRO-SUCCESSI — Pattern Vincenti (non solo gli errori)

> **Direttiva Max (2026-07-20):** studiare anche quando qualcosa esce bene, non solo quando
> esce male — e studiare cosa succede quando un output passa MOLTE verifiche prima di essere
> confermato buono. Append-only. Agente responsabile (M3): `isp-revision-analyst` (§ successi).

## Come si compila una voce
Per ogni caso di **0 correzioni** (accettato al primo output) o di **verifica multipla superata
senza difetti**: cosa ha reso possibile il risultato pulito, per ripeterlo deliberatamente.

---

## SUC-20260711-001 — Il gate ha trovato 2 difetti PRIMA della consegna (01-AGENCY)

**Cosa è successo:** al gate di chiusura 01-AGENCY (batch-3), il test di integrità automatico
ha trovato 2 difetti reali (namespace divergente 87 occorrenze, 6 README v1 stantii) che una
chiusura frettolosa avrebbe sepolto — l'ecosistema è stato dichiarato completo SOLO dopo averli
corretti e ri-verificati a zero.
**Perché ha funzionato:** il gate non era un check estetico ("i file ci sono?") ma un test di
COERENZA funzionale (link agenti↔citazioni, namespace↔chiavi di stato) — l'unico tipo di gate
capace di trovare un difetto che "sembra" tutto a posto ma si romperebbe a runtime.
**Pattern da ripetere:** ogni chiusura di reparto/ecosistema deve avere un test di integrità
delle CITAZIONI/RIFERIMENTI incrociati, non solo un conteggio di file e righe.

## SUC-20260719-001 — Bug trovato in autorevisione, zero lanci reali (EmpireDesk B1)

**Cosa è successo:** Gael, costruendo il loader `modules/*.py`, ha trovato in autorevisione
(EDE-7) che un modulo con schema sbagliato avrebbe fatto crashare la lettura di TUTTE le tile
— corretto PRIMA di lanciare qualsiasi cosa, zero run reali necessarie per scoprirlo.
**Perché ha funzionato:** il pattern "isolare e validare ogni pezzo che un componente esterno
può fornire, non solo l'import" era già una regola scritta (ereditata da errori precedenti) —
applicata per riflesso, non riscoperta da zero.
**Pattern da ripetere:** le regole permanenti scritte nei REGISTRO-ERRORI locali funzionano
quando vengono lette PRIMA di scrivere codice nuovo dello stesso tipo, non solo dopo un crash.

## SUC-20260719-002 — Tile Caroselli: difetto trovato per lettura del codice, non per crash

**Cosa è successo:** EDE-5 (bottone che sarebbe fallito sempre per argomento mancante) è stato
trovato leggendo COSA si aspettava `generate.js` come input, non lanciandolo e vedendo l'errore.
**Perché ha funzionato:** la regola "selftest statico non basta, va letto il codice del target"
era già scritta da un errore precedente sullo stesso reparto (EDE-4) — applicata nello stesso
ciclo di lavoro invece che in uno successivo.
**Pattern da ripetere:** quando si trova un difetto, controllare SUBITO se lo stesso file ha
altri difetti della stessa classe (qui: altre tile con lo stesso problema di argomenti mancanti),
invece di chiudere al primo trovato.

## Connessioni
- [[REGISTRO-ERRORI]] · [[REGISTRO-REVISIONI]] · [[15-DOSSIER-ISPETTORATO]] · [[ARCHITETTURA]]
