---
Type: TOOL
Status: Active
Tags: #lanci #adr-025 #ecosistema-15 #macchina-a-stati #artefatti #gate #manuale-claude-code
Created: 2026-09-10
Last updated: 2026-09-11
---

# LANCI — l'ecosistema che porta un prodotto da pubblicato a venduto

## Overview
Quindicesimo ecosistema di Digital Empire ([ADR-025](../../../company/Memory/decisions/ADR-025-ecosistema-lanci.md), firmato da Max l'08/09/2026, cartella creata il 10/09). Mandato in una riga: **porta un prodotto già pubblicabile da pubblicato a venduto e misurato.** È l'anello mancante fra ULTIMO METRO (ADR-016, che porta da finito a pubblicato) e TESORERIA (ADR-020, che conta l'euro una volta nei conti): quel tratto in mezzo non lo copriva nessuno, e si vedeva nei numeri — al 05/09/2026 l'azienda **non poteva incassare un euro**, il bottone d'acquisto era un indirizzo di posta.

Motore: `company/Ecosistemi/15-LANCI/02-AUTOMAZIONI-E-SCRIPTS/scripts/` (`stato_lancio.py` + comando `lancio`). Fonte di verità: `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml`, validato da `valida_registro.py` (**832 controlli**, deve uscire 0 **prima** di ogni build).

## Dettagli

**Il centro è l'artefatto, non il reparto.** Tredici artefatti tipizzati (`ART-PUB`, `ART-DEC`, `ART-CRT`, `ART-RIC`, `ART-PRV`, `ART-OFF`, `ART-CPY`, `ART-FNL`, `ART-EDT`, `ART-BDG`, `ART-APE`, `ART-CNS`, `ART-DBR`), ognuno con uno schema che lo valida, un produttore unico, **un giudice diverso dal produttore** (INV-01), un gate che lo blocca e un ramo di fallimento mai vuoto. Un organigramma di reparti non è più l'unità con cui si progetta.

**Non è un motore di orchestrazione, ed è una scelta registrata** (decisione 5 di ADR-025). Verificato sul codice il 05/09: il motore canonico `orchestration-layer` ha un tetto rigido di sei attività per piano, cinque nomi di ruolo e non sa chiamare nessun modello. Qui serve una macchina a stati con dei controlli — *leggere un file, validarlo contro il suo schema, decidere se si passa, scrivere un verbale* — circa 400 righe, non 133 file.

**Il giudice non scrive.** L'agente `lan-gate` ha `tools: ["Read", "Bash", "Glob", "Grep"]`: niente `Write`, niente `Edit` (INV-09). I verbali dei gate li scrive lo script che lo invoca. Un giudice che può riscrivere il fascicolo non è un giudice.

**Dodici stati, diciassette transizioni**, da `IDEA` ad `APPRESO` (l'unico finale buono: debrief completo con gli scarti spiegati). `PRONTO → APERTO` richiede una firma umana e **`PU-APERTURA` non ha un valore predefinito e non ce l'avrà mai.**

**Tetto di spesa 15,00 $ per lancio.** Al raggiungimento il lancio si ferma dov'è, salvato, e riprende — non ricomincia. Ogni invocazione di agente costa 0,08-0,11 $ di tassa fissa di harness (ADR-014): il numero di agenti è un moltiplicatore di costo, non un indicatore di capacità.

**Il comando che giustifica l'ecosistema** è `lancio blocchi`: tutti i punti umani aperti dell'azienda in una schermata, ordinati per giorni di attesa. *Se quel comando fosse esistito, il Manuale non sarebbe stato fermo sei mesi in silenzio.* Non è ancora costruito — è lo scaglione S5.

**Costruzione a sei scaglioni**, e i primi due non contengono una riga di codice per scelta: prima si incassa un euro vero e lo si rimborsa (S0), poi si porta un lancio a mano fino alla firma di un prezzo (S1). Il software nasce dopo, dai difetti misurati.

## Stato reale al 2026-09-11

**S0 aperto** — la catena dell'incasso non è chiusa. Tre dei sei gesti sono mani umane (pannello del servizio di posta, conto su un fornitore di pagamento, carta vera) e nessuna sessione può farli.

**S1 compilato, e ha bocciato il primo lancio.** I quattro artefatti del Manuale Claude Code sono stati scritti a mano: tre passano i propri schemi, il quarto (`offerta.PROPOSTA.json`) fallisce su `firma` — ed è il comportamento corretto, perché nessun agente può scrivere quel campo. Risultato del collaudo: **pubblico raggiungibile verificato 0** (nessuno dei tre canali ha una prova), **ricavo atteso 0 € in tutti e tre gli scenari**, **certificato non-consegnabile con 4 bandiere rosse su 6**.

**S2a chiuso** — `lancio crea/stato/elenco/valida` girano, 17 prove verdi. La prova che conta: un artefatto che contiene `{"valido": true}` **fallisce lo stesso**, perché la validità è ricalcolata contro lo schema e non letta da un campo.

## Come Impatta DE

È il primo organo che rende **falsificabile** l'affermazione "siamo pronti a lanciare". Prima di LANCI quella frase era un'opinione; adesso è un comando che esce 0 o 1. E al primo uso reale ha risposto 1, per tre motivi che nessun codice risolve: **non sappiamo a chi parlare, non abbiamo mai provato a consegnare, e nel prodotto ci sono tre righe che mostrano il deploy personale di un terzo.**

## Connessioni
- [[Tool_Tesoreria_Digital_Empire]] — l'ecosistema a valle (ADR-020): LANCI porta l'euro fino alla cassa, Tesoreria lo conta da lì in poi. Stessa legge condivisa: un numero che non esiste si dichiara, non si stima.
- [[Source_Giovanni_Beggiato_Claude_Cowork_Corso]] — fonte terza che DE studia, e che il collaudo del Manuale ha fatto riemergere: tre righe del manuale mostrano una distribuzione personale sotto il suo account. È la bandiera rossa RF4, e viene prima del prezzo.
- [[Tool_Conoscenza_Empire_Agente]] — la biblioteca che alimenta gli agenti `lan-*` quando devono sapere cosa l'Impero ha già imparato su lanci, funnel e offerte.
