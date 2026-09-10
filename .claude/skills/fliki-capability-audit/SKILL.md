---
name: fliki-capability-audit
description: "Confronta i campi del payload che la fabbrica YouTube manda davvero a Fliki con la superficie reale dell'API del fornitore, e produce la lista delle leve che paghiamo e non usiamo. Usala prima di un gate di categoria dello studio AI TUBE PRO, quando qualcuno dice che una cosa con Fliki non si puo' fare via API, quando si sospetta che il fornitore abbia aggiunto funzioni dopo l'ultima verifica, o quando un agente chiede se un campo esiste davvero prima di ordinarne l'uso. E' il braccio operativo dell'agente regolatore-capacita-fliki."
---

# FLIKI CAPABILITY AUDIT

> **Il problema che questa skill esiste per risolvere.**
> Fliki e' lo strumento che la fabbrica usa **in produzione**, e paghiamo l'abbonamento
> intero. Ma nessuno, di mestiere, confronta cio' che il fornitore offre con cio' che il
> nostro client manda davvero. Le due leve trovate finora — `bgMusicVolume` e
> `generateSfx` — sono state scoperte **una volta sola, il 2026-09-07, per caso**, mentre
> si cercava altro. Prima di quel giorno, per mesi, `qa-audio-video` — un gate bloccante —
> bocciava video sul volume di una musica che nel nostro payload **non esiste**, e
> `video-producer` ordinava un montaggio a mano abbandonato da mesi.
>
> Il difetto non e' che ci sfuggisse un campo. E' che **non esisteva il lavoro** di
> cercarli. Questa skill e' quel lavoro, reso ripetibile in minuti invece che in una
> sessione di ricerca dedicata.

## 1. COSA FA

Tre passi, in quest'ordine, e nessuno dei tre si salta.

1. **Legge cosa mandiamo.** Apre
   `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py` ed estrae l'elenco
   dei campi del payload **effettivamente costruiti** — non quelli nominati nei commenti,
   non quelli citati nei documenti degli agenti: quelli che finiscono nella richiesta.
2. **Legge cosa offre il fornitore.** Prende lo schema pubblicato su `developer.fliki.ai`.
3. **Sottrae.** Produce la tabella campo-per-campo con quattro colonne — campo, usato da
   noi si/no, cosa fa secondo la documentazione, dove l'ha letto — e in fondo l'elenco
   secco delle **leve mai usate**.

## 2. COME SI USA

```
/fliki-capability-audit
```

Nessun argomento. Il rapporto viene scritto in
`company/Memory/studi/aitubepro/CAPACITA-FLIKI-<AAAAMMGG>.md`, con la data nel nome: i
rapporti vecchi **non si sovrascrivono**, perche' il confronto fra due date e' esattamente
cio' che dice se il fornitore ha aggiunto qualcosa.

## 3. IL METODO DELLA DOPPIA LETTURA — non e' un vezzo

Il metodo non va inventato ogni volta: e' gia' scritto e collaudato in
`company/Memory/studi/aitubepro/A4-metodo-ai-tube/VERIFICA-PAYLOAD-L20-GATE-A4.md`.

**Ogni campo si legge due volte, con due domande diverse, su due pagine diverse della
documentazione.** Un campo confermato una volta sola resta marcato `da riconfermare`, non
diventa un fatto. La ragione e' misurata, non teorica: la verifica del 2026-09-07 ha
prodotto tre risposte, e la terza — il tetto delle 50 scene — **non era decidibile dallo
schema**. Averlo dichiarato non-decidibile invece di indovinarlo e' cio' che ha reso utili
le altre due.

**Tre esiti ammessi per ogni campo, e sono tre, non due:**

| Esito | Quando | Cosa comporta |
|---|---|---|
| `raggiungibile` | la documentazione lo descrive e il nostro client potrebbe mandarlo | candidato binario B, va al gate |
| `solo interfaccia` | esiste in Fliki ma non ha endpoint | si dichiara e si smette di ordinarlo agli agenti |
| `non decidibile` | lo schema non basta a dirlo | serve una chiamata reale, si scrive che serve |

## 4. IL PRIMO CASO DI PROVA — se non lo trova, la skill e' rotta

`bgMusicVolume` e `generateSfx` sono raggiungibili e **non sono nel nostro payload**,
verificato il 2026-09-07 e riverificato il 2026-09-10. Un'esecuzione che non li ritrova non
sta guardando nel posto giusto, e il rapporto va buttato invece che creduto.

## 5. QUANDO LA FONTE NON RISPONDE

La documentazione del fornitore e' fuori casa nostra e puo' non rispondere. In quel caso il
rapporto **si scrive lo stesso**, dichiarando cosa manca — mai una tabella muta che sembra
dire "nessuna leva nuova".

- **Documentazione irraggiungibile** — si scrive il rapporto con la sola colonna "usato da
  noi", si marca l'intera colonna fornitore come `non letta oggi`, e si dice esplicitamente
  che l'audit **non e' valido** come confronto. Un audit a meta' dichiarato vale; un audit a
  meta' taciuto e' peggio di nessun audit.
- **Documentazione cambiata di struttura** — si registra la data e cosa non si e' trovato
  dove ci si aspettava. Un campo sparito dalla documentazione **non e' un campo rimosso**
  finche' non lo si e' verificato: si marca `da riconfermare`.
- **Nostro client illeggibile** (refactor in corso, file spostato) — ci si ferma e lo si
  dice. Non si deduce il payload dai documenti degli agenti: e' esattamente l'errore che
  aveva fatto credere per mesi che mandassimo la musica.

## 6. COSA QUESTA SKILL NON FA

**Non applica niente.** Produce un elenco; l'uso di una leva nuova tocca
`02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py`, che e' il motore in produzione, e per
[ADR-029](../../../company/Memory/decisions/ADR-029-doppio-binario-studio-fabbrica.md) si
tocca solo a gate di categoria superato, con test verdi e un video di prova.

**Non giudica se una leva convenga.** Dice che c'e' e che non la usiamo. Se convenga
accenderla lo decide il gate, coi costi davanti.

## 7. LEGAMI

- `03-AGENTI-E-RUOLI/regolatori/regolatore-capacita-fliki.md` — l'agente che la invoca a
  cadenza dichiarata. Questa skill e' il suo braccio, non il suo sostituto.
- `04-SKILLS-E-REFERENCE/references/fliki-avanzato.md` e `fliki-produzione.md` — dove
  finiscono le leve confermate.
- `company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/RIPASSO_COSTRUTTIVO.py` —
  regole `A4-RC-16` (l'agente) e `A4-RC-17` (questa skill).
