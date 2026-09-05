# ORIGINE — cosa era stato chiesto davvero sull'ecosistema LANCI

## 1. LA TASK MADRE — cosa chiedeva, alla lettera

Fonte: `company/Memory/tasks/TASK-GAEL-20260831-SETTIMANA-02.md`

Header del documento (righe 1-7):
> Owner: Max (committente) · Esecutore: GAEL · Controllore: Claude (audit + review)
> Origine: audit W1 richiesto da Max 2026-08-31 (verificato eseguendo il codice, non leggendo i checkpoint)
> Governo: ADR-006 (ciclo 9 passi) + REGOLA ZERO memory-first + ADR-003 (wrap, mai riscrittura)
> Emesso: 2026-08-31 · Settimana: W2 (lun 1 set -> dom 7 set 2026)

La task LANCI è la quarta delle quattro task settimanali (riga 39): `🔴 TASK-LANCI-ECO-W2 — il piano dell'ecosistema Lanci (spezzato in L1→L6)`.

Testo di apertura della sezione LANCI (righe 401-403, 452-471):
> "# 🔴 TASK-LANCI-ECO-W2 — Ecosistema LANCI"
> "⚠️ Questa task ha una regola diversa dalle altre due. Leggila tutta prima di toccare un file."
> "Max è stato esplicito: **prima devi consegnare un piano perfetto, estremamente progettato, chirurgico. Poi si costruisce.** Non aprire cartelle, non scrivere agenti, non creare l'ecosistema finché il piano non è approvato da Max. Il piano è il deliverable della settimana; la costruzione è la W3."
> "È una task enorme, quindi è spezzata in 6 sotto-task con gate propri (L1→L6). Si fanno in quest'ordine: ognuna è l'input della successiva. Chiudi e segna ogni L prima di aprire la seguente — se la settimana finisce a L4, hai comunque consegnato qualcosa di completo e riprendibile, non un cantiere aperto."

Tabella delle sotto-task (righe 464-472), testuale:
| # | Sotto-task | Output | Tempo indicativo |
|---|---|---|---|
| L1 | Ricognizione di cosa esiste davvero | `RICOGNIZIONE-LANCI.md` | mezza giornata |
| L2 | Estrazione del contenuto dai progetti vecchi | `ASSORBIMENTO-LANCI.md` | mezza giornata |
| L3 | Architettura: ecosistema + reparti | bozza `26-ECOSISTEMA-LANCI.md` §1-2 | 1 giorno |
| L4 | Il flusso end-to-end di UN lancio + comando ufficiale | §3 dello stesso doc | mezza giornata |
| L5 | Agenti e gate per reparto | §4 dello stesso doc | 1 giorno |
| L6 | ADR proposto + consegna a Max | ADR in `decisions/` | 1 ora |

### L1 — testo esatto (righe 475-503)
> "Max vuole sapere **cosa esiste già** sui lanci prima di decidere. Ti do quello che ho trovato io in questo audit, così non ricominci da zero — **verificalo e completalo, non fidarti**"

Elenco di cosa "esiste ed è vero" (righe 480-486):
> "`company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/` — **1.805 righe** di documentazione: 9 agenti (`IB-COORD-LANCI`, `IB-LANC-PLANNER`, `ASSET`, `COPY-LIAISON`, `DRY`, `QA`, `TRACKER`, `WEBINAR`, `DEBRIEF`), `ARCHITETTURA.md`, `KPI.md`, `PRINCIPI.md`, `REGOLE.md`, `SKILLS.md`, e 2 workflow (`WF-LANCIO` T-30→T+7, `WF-WEBINAR`)."
> "Il workflow WF-LANCIO ha input JSON, gate, sequenza. **È scritto bene.**"

Elenco di cosa "è il problema" (righe 488-494):
> "`scripts/README.md` dice *\"Script pianificati (build in V2)\"* — `launch_calendar.py`, `dry_run_costs.py`, `launch_debrief_diff.py`: **nessuno dei tre esiste.**"
> "`state/README.md`: schema, nessuno stato."
> "`SKILLS.md`: skill *\"da forgiare\"*, nessuna forgiata."
> "**Zero file eseguibili nell'intero reparto.** È un ecosistema di carta: descrive perfettamente un lancio che nessun comando sa avviare."

Gate L1 (riga 500-502): "il documento distingue esplicitamente ciò che è eseguibile da ciò che è solo descritto, con il comando che lo dimostra (`ls`, `python -c \"import ...\"` — qualcosa che prova l'esistenza, non la fiducia)."

### L2 — testo esatto (righe 506-535)
Elenco fonti storiche da assorbire, testuale (righe 510-519):
```
Progetti Claude/Info-Business-HQ_Knowledge/          (Priorità 1/2/3)
InfoBusiness/                                        (catalogo prodotti, Funnel Unico Perfetto.pdf, Webinar/)
System OMEGA/.../CONTESTO - SOLO ESEMPI/Product Creation Lab/
System OMEGA/.../CONTESTO - SOLO ESEMPI/Product Pricing Strategist.skill
System OMEGA/.../CONTESTO - SOLO ESEMPI/Project-Marketing University.md
System OMEGA/.../CONTESTO - SOLO ESEMPI/Project-Strategy Command Center/
System OMEGA/.../CONTESTO - SOLO ESEMPI/VSL Script Builder.skill
System OMEGA/.../CONTESTO - SOLO ESEMPI/Webinar Script Master.skill
Lancio corso skill beast/ · Lanco ebook/ · Formazzione/
```
Citazione diretta di Max (riga 521-522): *"prima facevamo tutto con dei progetti, i classici progetti. Adesso al posto dei progetti del cavolo facciamo workflow, reparti, team di agenti, piccoli ecosistemi."*
Conseguenza dichiarata: "il contenuto di quei progetti si assorbe, la loro forma si butta."

Gate L2 (riga 533-534): "ogni riga del documento punta a un file sorgente reale e a un reparto di destinazione. Zero righe 'da approfondire'."

### L3 — testo esatto (righe 538-568)
> "Un ecosistema nuovo, **`company/Ecosistemi/14-LANCI/`** (14 è il primo numero libero: l'ultimo è `13-ARENA-APEX`)."

Tabella reparti nominati da Max esplicitamente + quelli che il flusso richiede (righe 549-558): Strategia, Intelligence & Competitor, Prodotto, Pricing & Offerta, Copy, Siti & Funnel, Marketing & Traffico, Esecuzione Lancio.

Citazione sul sotto-ecosistema Siti (righe 560-564): "deve occuparsi di *organizzare e strutturare perfettamente tutti i siti dove il lancio avviene*. Nel piano specifica quali pagine servono per un lancio (sales page, landing opt-in, pagina webinar, checkout, thank you, upsell/downsell), chi le costruisce, con quale skill, e **come si verifica che siano online e funzionanti** — non 'fatte', *online e funzionanti*."

Gate L3 (righe 566-568): "§1-2 di `26-ECOSISTEMA-LANCI.md` scritte, con per ogni reparto missione in 1 frase, cosa produce, cosa lo blocca. Se un reparto non ha un output verificabile, non è un reparto: o lo motivi o lo togli."

### L4 — testo esatto (righe 572-587)
> "Questo è il cuore, ed è la parte che oggi manca completamente: **dal 'abbiamo un'idea' al 'carrello chiuso e debrief scritto'**, in una sequenza sola, con chi fa cosa e quale gate ferma cosa."
> "Deve avere lo stesso taglio del flusso KDP che hai già costruito e che funziona: un comando ufficiale che parte, legge lo stato, sa a che punto è, e non improvvisa quando manca un input. Stessa filosofia di `/libro-del-giorno`: **un comando, e parte.**"
> "Nel piano scrivi: nome del comando, cosa legge, cosa produce, dove si ferma e perché, e quali passaggi restano necessariamente umani (l'incasso, la pubblicazione, l'invio alla lista: azioni irreversibili verso l'esterno — quelle le fa una persona, sempre)."

Gate L4 (riga 586-587): "§3 scritta — la sequenza completa con i gate bloccanti, il comando ufficiale definito, e i punti di intervento umano dichiarati esplicitamente."

### L5 — testo esatto (righe 591-607)
> "Per ogni reparto il piano deve dire, obbligatoriamente: 1. missione in 1 frase 2. gli agenti (nome, mestiere in 1 riga, input, output) — **stesso formato dei 9 agenti di IB-L2-LANC** 3. il/i workflow con i gate BLOCCANTI 4. **cosa è eseguibile** — quali script/comandi, con nome e firma. 5. le connessioni: cosa riceve da chi, cosa passa a chi"
> "Regola che vale per tutti: **chi produce non approva.**"

Gate L5 (riga 605-607): "§4 scritta — ogni reparto ha i suoi agenti nel formato standard e almeno un gate bloccante con criterio misurabile (non 'qualità alta': un numero, o una condizione verificabile)."

### L6 — testo esatto (righe 610-618)
> "Un ADR **proposto, non applicato**, in `company/Memory/decisions/`: creazione di `14-LANCI`, spostamento di IB-L2-LANC dentro (ADR-003: si sposta, non si riscrive), cosa si assorbe dai progetti vecchi e cosa si archivia. Con le alternative scartate e il perché — un ADR senza alternative scartate è un annuncio, non una decisione."

Gate L6 (riga 617-618): "`26-ECOSISTEMA-LANCI.md` completo + ADR proposto. **Nessuna cartella `14-LANCI/` creata prima dell'ok di Max.**"

### Nota di aggiornamento 2026-09-05 aggiunta in testa alla task (righe 403-437)
Testuale (righe 403-437): Max ha completato personalmente L4, L5, L6 mentre Gael chiudeva i libri KDP. "Il tuo lavoro L1-L2-L3 non è stato sostituito: è la base di tutto ed è citato ovunque, per nome." Il piano finale è in `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/`, comincia da `00-LEGGIMI-GAEL.md`. Contiene: "dodici reparti, sette flussi con l'agente per ogni fase, 50 agenti con il frontmatter già scritto, tredici gate con criteri numerici, ~235 file con il percorso assoluto, 139-187 ore-uomo di costruzione a scaglioni." Tre note esplicite: "Il numero è 15, non 14"; "L'ADR-022 va registrato PRIMA di creare la cartella"; "Il criterio di chiusura del primo scaglione è far uscire davvero il Manuale Claude Code. Se non esce, gli altri reparti non si costruiscono — e il vincolo è tecnico, non morale." Il piano è stato "battuto tre volte" con revisori indipendenti, "dieci difetti gravi trovati e corretti".

### Nota di ordine del 2026-09-04 (righe 443-450), citazione testuale di Max
> "Deve essere tutto ancora più architettato, mi raccomando i miglioramenti - Devi fare l'intera parte di architettatura e struttura tutta completamente con arena Però fatti dare tutto l'intero prompt e contesto da Emperator."
Nota accanto: "L3 (§1-2) è chiusa, ma non basta: prima di L4→L6, apri una chat con Emperator e fatti dare il prompt/contesto completo — non riprendere da solo. E occhio al numero: `14-LANCI` collide con `14-TESORERIA` già esistente — prossimo numero libero in `company/Ecosistemi/REGISTRO-NUMERI.md` (15)."

### Regole valide per tutte e 3 le task della settimana (righe 636-654), rilevanti per LANCI
1. "Prova, non dichiarazione — comando + output reale incollato nel checkpoint."
2. "Task chiusa → checkpoint ... + stato aggiornato in `EmpireDesk/state/taskboard.json`."
3. "ADR-003 vale ovunque: il workflow KDP funziona — si estende, non si riscrive. IB-L2-LANC è scritto bene — si sposta, non si rifà."
4. "Ordine di priorità, non negoziabile: FIX → PIANO → 5 LIBRI → LANCI." — LANCI è ultima priorità della settimana, esplicitamente sacrificabile se il tempo si stringe ("si stringe sull'ultima").
5. "Item minori → `company/Memory/BACKLOG.md`. Non fermano la settimana."
6. "Se ti blocchi più di una sessione sullo stesso punto → blocco ⚠️ COORDINAMENTO in `STATO-EMPIRE.md`."

Sezione "Costruzione: NON questa settimana" (righe 622-627): "Il piano lo approva Max. Poi si costruisce (W3). Se avanza tempo dopo aver chiuso le prime task, puoi costruire **un solo pezzo pilota** — il più piccolo che dimostra che il piano regge (es. `launch_calendar.py` ...). Nient'altro."

## 2. VINCOLI ESPLICITI POSTI DA MAX

- **V-01 — Piano prima, costruzione dopo, ordine tassativo.** File: `TASK-GAEL-20260831-SETTIMANA-02.md`, righe 454-457: "Max è stato esplicito: prima devi consegnare un piano perfetto, estremamente progettato, chirurgico. Poi si costruisce. Non aprire cartelle, non scrivere agenti, non creare l'ecosistema finché il piano non è approvato da Max."
- **V-02 — Zero cartelle create senza ok.** Righe 617-618 e ripetuto in `26-ECOSISTEMA-LANCI.md` riga 184: "La cartella non esiste e non va creata fino all'ok di Max."
- **V-03 — LANCI è la priorità più bassa della settimana, sacrificabile.** Righe 646-650: "FIX → PIANO → 5 LIBRI → LANCI ... Le prime tre producono libri e pubblicazioni (revenue); la quarta produce un piano (impianto). Se la settimana si stringe, si stringe sull'ultima."
- **V-04 — Wrap, mai riscrittura (ADR-003), citato esplicitamente per IB-L2-LANC.** Riga 643-644: "IB-L2-LANC è scritto bene — si sposta, non si rifà."
- **V-05 — Reparti nominati esplicitamente da Max + sotto-ecosistema Siti nominato per nome.** Righe 545, 560-564 (vedi sopra, sezione 1/L3).
- **V-06 — Verifica "online e funzionanti", non "fatte".** Riga 564: le pagine dei siti vanno verificate come "online e funzionanti", non semplicemente costruite.
- **V-07 — Azioni irreversibili verso l'esterno le fa sempre una persona.** Riga 584: "quali passaggi restano necessariamente umani (l'incasso, la pubblicazione, l'invio alla lista): azioni irreversibili verso l'esterno — quelle le fa una persona, sempre." (stesso principio ripetuto per KDP: FIX-1, riga 77-79 "l'upload è manuale e lo fa una persona").
- **V-08 — Chi produce non approva.** Riga 602: "Regola che vale per tutti: chi produce non approva. È la lezione di `kdp blocco`."
- **V-09 — Ordine del 2026-09-04: architettare di più, passare da Emperator per il contesto completo.** Citazione testuale di Max riportata sopra (sezione 1): "Deve essere tutto ancora più architettato, mi raccomando i miglioramenti..."
- **V-10 — Numerazione: 14 collide con Tesoreria, il numero corretto è 15.** `TASK-GAEL...` riga 449-450 e confermato in `CP-20260905-015.md` riga 36-37: "Il numero dell'ecosistema è 15, non 14 — il 14 è TESORERIA. Riservato in REGISTRO-NUMERI.md."
- **V-11 — Piano da consegnare "chirurgico", con 3 giri e revisione indipendente ("chi produce non approva" esteso al piano stesso).** Confermato in `26-ECOSISTEMA-LANCI.md` §0 (tre giri) e in `CP-20260905-015.md` (tre revisori indipendenti, 106 rilievi).
- **V-12 — L'ADR (ADR-022) va registrato PRIMA di creare la cartella dell'ecosistema.** `TASK-GAEL...` riga 426; confermato in `CP-20260905-015.md` riga 45 e `EMP-ECGA.md` riga 42-43 (lo impone ADR-009, verificato da `empire/conform.py`).
- **V-13 — Il criterio di chiusura del primo scaglione di costruzione è "far uscire davvero il Manuale Claude Code".** `TASK-GAEL...` riga 427-428: "Se non esce, gli altri reparti non si costruiscono — e il vincolo è tecnico, non morale."

## 3. L'ARCHITETTURA DI PARTENZA (L3, gli 8 reparti di Gael)

Fonte: `PIANO-MAESTRO/26-ECOSISTEMA-LANCI.md` (marcato "superato" dal 2026-09-05, ma è il documento L3 originale di Gael, citato come base da tutto il resto).

**Metodo dichiarato (§0, righe 37-111):** tre giri.
- Giro 1 ("otto reparti nuovi in un ecosistema nuovo") — scartato perché 4 degli 8 reparti esistono già altrove come specifica scritta (94 file, 12.027 righe in 02-INFO-BUSINESS + 16.226 righe in 04-MARKETING, zero eseguibili, zero agenti ufficiali su 42 schede: `ls .claude/agents/ | grep -icE "^ib-"` → 0).
- Giro 2 ("14-LANCI è solo un orchestratore trasversale senza reparti propri") — scartato perché Max ha chiesto esplicitamente un ecosistema con reparti e per nome il sotto-ecosistema Siti.
- Giro 3 (adottato): "14-LANCI esiste come ecosistema, e ogni suo reparto porta un'etichetta dichiarata: NUOVO o WRAP." NUOVO = non esiste da nessuna parte nell'Impero, si costruisce. WRAP = esiste già altrove, 14-LANCI lo usa via handoff senza riscriverlo (ADR-003).

**Missione dell'ecosistema (§1.1, riga 118-120):** "14-LANCI porta un prodotto finito sul mercato e ne misura l'esito. Non lo crea, non lo scrive, non lo disegna: lo lancia. È l'organo che trasforma 'è pronto' in 'è in vendita, e so quanto ha reso'."

**DONE WHEN (§1.2, righe 124-131):** un lancio è chiuso quando tutte e cinque sono vere: (1) prezzo e data decisi, scritti in un file; (2) pagine del funnel online e misurate; (3) carrello aperto e chiuso alle date del calendario; (4) metriche reali confrontate coi benchmark, ogni scarto ≥10% con causa scritta; (5) debrief in Memory con almeno 3 pattern distillati.

**Gli 8 reparti L2 (§2, tabella riassuntiva §3, righe 442-451):**
1. **LAN-STRATEGIA** — WRAP (wrappa `IB-L2-STRA`). Produce `decisione.json` (GO/BACKLOG/SCARTA). Gate G1 (filtro anti-ADD, 5 domande).
2. **LAN-INTELLIGENCE** — WRAP (wrappa `IB-L2-STRA` + `08-INTELLIGENCE`). Produce `ricerca.json` (≥15 frasi con URL, ≥5 pain point, ≥3 competitor, ≥3 gap).
3. **LAN-PRODOTTO** — WRAP (wrappa `IB-L2-PROD`). Produce `certificato-prodotto.json`. Gate G2 (score ≥60/100 + MVP ≥5 persone) e G3 (6 red flag a zero).
4. **LAN-PRICING** — 🟢 **NUOVO, l'unico dei giro-1 originari.** Produce `offerta.json` (prezzo, data apertura carrello, durata, stack valore, anchor, bonus, garanzia, livello Product Ladder). Gate G4 (prezzo o data vuoti/"NON LO SO"/"presto" → BLOCK).
5. **LAN-COPY** — WRAP (wrappa `04-MARKETING/L2-1-Copywriting` + `L2-3-Email-Lifecycle` + skill `cro-copy-architect`). Produce `copy/`. Gate G5 (APSOC ≥80/100).
6. **LAN-SITI** — WRAP + estensione (wrappa `IB-L2-VEND` + skill `site-build`/`site-copy`/`site-deploy`/`signup`/`empire-premium-style`). Produce `funnel.json` con URL, codice HTTP, tag, evento conversione. Gate G7 (pagina che non risponde 200 o non registra conversione = non online).
7. **LAN-TRAFFICO** — WRAP (wrappa `04-MARKETING/L2-2-Advertising` + `L2-4-Analytics`). Produce `traffico.json` (per canale: volume, costo, opt-in, CAC). Gate G6 (delta budget >10% → BLOCK).
8. **LAN-ESECUZIONE** — WRAP (wrappa `IB-L2-LANC`, 19 file/2.377 righe/9 agenti). Produce `calendario.md` + `state.json` + `dry-run.md` + verbale go/no-go + `debrief.md` (≥3 pattern). Gate G6.

**Promessa/motivo dichiarato per l'esistenza dell'ecosistema (§1.3, righe 133-150):** il Manuale Claude Code è "Pronto" dal 07/03/2026, 203 pagine, con lead magnet, landing, funnel, copy, script webinar e sequenze email già pronti, ma "Prezzo: '€ NON LO SO'. Data: 'Presto spero'. Metriche: 0." Citato come blocco dichiarato in `02-INFO-BUSINESS/ECOSISTEMA.md` come "BLOCCANTE (B1)" dall'11 giugno, mai risolto in tre mesi.

**Confini (§1.4):** 14-LANCI NON crea il prodotto (fa `IB-L2-PROD`), non scrive il copy da zero (fa `L2-1-Copywriting`), non acquisisce clienti agenzia (01-AGENCY), non gestisce community post-acquisto (`IB-L2-COMM`), non studia video/corsi (Empire Studio). "La linea: se un'attività continua dopo la chiusura del carrello, non è di 14-LANCI."

**Invariante (§1.5, riga 166-172):** "Nessun reparto di 14-LANCI duplica un reparto esistente ... un reparto WRAP non può avere agenti propri che rifanno il lavoro del proprietario. Può avere solo agenti di interfaccia (prepara l'input, verifica l'output, gestisce il gate)."

**Le tre decisioni che 14-LANCI non può prendere da solo (§4, righe 458-468):**
1. Manuale Claude Code a pagamento o lead magnet gratuito — decide Max.
2. APP-SOC o APSOC come standard di copy — decide il CMO.
3. `Gemini.md` o `empire-premium-style` come sistema visivo — decide la guild Design.

Questo documento è dichiarato SUPERATO dal 2026-09-05 (riquadro iniziale, righe 14-26): il numero passa da 14 a 15, i reparti da 8 a 12 (aggiunti offerta, editoriale, tesoro, memoria), e il piano completo di L4-L5-L6 vive ora in `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/`.

## 4. COSA HANNO MISURATO L1 e L2

Fonte L1: `PIANO-MAESTRO/RICOGNIZIONE-LANCI.md`
Fonte L2: `PIANO-MAESTRO/ASSORBIMENTO-LANCI.md`

### Numeri misurati da L1 (RICOGNIZIONE-LANCI.md)
- Reparto `IB-L2-LANC-Lanci-Campagne`: **2.377 righe** (correzione rispetto alle 1.805 stimate nell'audit di partenza — "il numero non cambia il verdetto: lo peggiora"), **19 file**, **0 file eseguibili**, **0 agenti ufficiali su 9** (`ls .claude/agents/ | grep -iE "ib-|lanc"` → nessun risultato, su 124 agenti ufficiali totali), **0 stato mai scritto** (`find . -maxdepth 6 -type d -path "*infobusiness/lanci*"` → nessun risultato).
- 3 script dichiarati "pianificati (build in V2)" in `scripts/README.md`: `launch_calendar.py`, `dry_run_costs.py`, `launch_debrief_diff.py` — **nessuno dei tre esiste** (0 su 3).
- 1 skill P0 dichiarata (`launch-runbook`, "da forgiare", priorità dichiarata dal 2026-06-21) — **non forgiata**, 0 su 1 (esistono solo skill omonime diverse: `launch`, `market-launch`, `script-video-lancio-ccm`, `youtube-channel-launch`).
- Bilancio finale (§5, tabella): File totali 19, righe doc 2.377, file eseguibili 0, agenti ufficiali 0/9, script esistenti 0/3, skill forgiate 0/1, namespace stato creati 0/4, lanci mai tracciati 0, **skill esterne pronte all'uso: 11 su 11** (`launch`, `ads`, `ad-creative`, `cro-copy-architect`, `empire-premium-style`, `site-build`, `site-copy`, `site-deploy`, `pricing`, `signup`, `paywalls`).
- Conclusione L1 (§3, riga 192-195): "l'ecosistema 14-LANCI non deve costruire da zero sei reparti su otto. Deve cablare skill che esistono già dentro un flusso che oggi non c'è. Il buco non è la capacità — è l'orchestrazione."
- WF-LANCIO.md (152 righe) e WF-WEBINAR.md (144 righe) giudicati "carta, ma di qualità" — si salvano quasi interi, hanno "la stessa anatomia del flusso KDP che funziona", manca solo il comando che li esegue.

### Numeri misurati da L2 (ASSORBIMENTO-LANCI.md)
- **10 fonti aperte su 10**, ~26.300 righe lette + ~52 pagine PDF estratte.
- **58 framework concreti mappati a un reparto** di destinazione.
- **4 gate bloccanti individuati già scritti**: filtro anti-ADD (5 domande), brief ≥60/100 + MVP 5 persone, 6 red flag qualità, quality validation Marketing University.
- **26 soglie numeriche recuperate**: 6 allarmi (`SOGLIE_ALLARME.md`), 6 benchmark funnel, 6 KPI prodotto, 3 soglie funnel diagnostiche, 5 fasce prezzo (`PRODUCT_LADDER.md`).
- **3 coppie di duplicati** verificate e neutralizzate (md5/diff identici): `InfoBusiness/` = `Info-Business-HQ_Knowledge/Priorità 1/`; `Formazzione/` ⊃ `Priorità 2/`; `Product Creation Lab/` = `Product Creation Lab - Copia/`.
- **3 skill dichiarate dalla task come da assorbire, NESSUNA esiste sul disco**: `Product Pricing Strategist.skill`, `VSL Script Builder.skill`, `Webinar Script Master.skill` (verificato con `find . -iname "*.skill*"` → nessun risultato in tutto il repo). Attenuante: per Pricing Strategist esiste fonte sostitutiva (`PRODUCT_LADDER.md`), per Webinar Script Master esiste fonte sostitutiva (i 3 PDF "Webinar Milionario"); **solo VSL Script Builder resta senza nessuna fonte, va scritta da zero.**
- **Scoperta fuori-lista più importante (§8):** il "Processo lanci - CONTESTO.md" (172 righe, non citato nella task) contiene FASE 0→10 (non 0→3 come pensava la task), e mappa esattamente sugli 8 reparti nominati — "nessun reparto va aggiunto, nessuno va tolto."
- **Scoperta §8 sul prodotto pilota** (vedi sezione 5 sotto): il Manuale Claude Code ha quasi tutto pronto tranne prezzo e data.
- **3 conflitti da risolvere prima di L5** (citati anche in §14 e ripresi in 26-ECOSISTEMA-LANCI.md §4): APP-SOC (KB_07_app-soc-framework.md) vs APSOC (standard Impero, owner CMO); `Gemini.md` (design system landing ebook) vs skill `empire-premium-style`; `KB_08_FRAMEWORKS_REGISTRY.md` vs agente `conoscenza-empire` (rischio due biblioteche).
- **6 fonti scartate con motivazione esplicita (§12)**: 9 PDF di `Priorità 2/` (materiale acquisizione clienti agenzia, va a 01-AGENCY, non a LANCI); 2 file `.txt` con solo URL YouTube (code di ingestione, vanno a Empire Studio); `Formazzione/Claude code/` (è il prodotto stesso, non materiale sul lanciarlo — va a Prodotto); duplicati già coperti al punto precedente.

## 5. IL PRODOTTO PILOTA — tutto quello che si sa

**Nome:** "Manuale Claude Code - Da zero a Senior" (talvolta citato come "Claude Code Mastery" / CCM negli asset di codice, es. skill `script-video-lancio-ccm`, cartella `Lancio corso skill beast/Leanding Page CCM/`).

**Fonte primaria del dato di stato:** `Info-Business-HQ_Knowledge/Priorità 1/CATALOGO PRODOTTI ATTUALE — Info-Bu.md` (32 righe, ultimo aggiornamento dichiarato **07/03/2026**), citata in `ASSORBIMENTO-LANCI.md` §8.1:

| Campo | Valore testuale nel file |
|---|---|
| Status | "Pronto" |
| Tipo | Ebook Premium |
| Formato | 203 pagine |
| Prezzo | "€ NON LO SO" |
| Data lancio | "Presto spero" |
| Metriche | 0 |
| Lead magnet collegato | Community WhatsApp (da fare) |
| Funnel tipo | Social → community → sales page → acquisto |

Nota nel file stesso, citata testualmente: "DEVE ANCORA ESSERE TUTTO MIGLIORATO TUTTO."

**CONTRADDIZIONE PRINCIPALE, dichiarata sia in ASSORBIMENTO-LANCI.md §8.1 sia in 26-ECOSISTEMA-LANCI.md §2.4 e §4:** doppio ruolo contraddittorio.
- Nel catalogo prodotti è "Ebook Premium" a pagamento.
- Nella scheda del corso "Vendi la Skill" è descritto come lead magnet gratuito — citazione testuale dal file: "ho un forte lead magnet: Ebook Manuale Claude Code GRATUITO."
- `26-ECOSISTEMA-LANCI.md` riga 144-148 conferma: questo blocco è dichiarato "BLOCCANTE (B1)" in `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md` fin dall'**11 giugno**, con le parole testuali *"prezzo NON LO SO e doppio ruolo contraddittorio (gratuito vs pagamento)"*, e mai risolto in tre mesi.
- `CP-20260905-015.md` e `EMP-ECGA.md` confermano che questa è la prima delle "3 decisioni che aspettano Max" e che senza risolverla "il primo lancio non parte": è nel dossier `04-WF-OFFERTA.md` §5 del nuovo piano `29-ECOSISTEMA-LANCI/`.

**Asset già pronti attorno al prodotto, elencati in ASSORBIMENTO-LANCI.md §8.2 con percorso:**
| Pezzo | Esiste? | Percorso |
|---|---|---|
| Prodotto | Sì, 203 pagine, "Pronto" da marzo | catalogo prodotti |
| Lead magnet | Sì, Framework I.C.R.O., 12 pagine | `Lancio corso skill beast/Framework_ICRO_Digital_Empire.pdf` |
| Landing page | Sì, costruita, 299 righe | `Lanco ebook/Sito- Leanding page/index.html` |
| Design system della landing | Sì, 54 righe di regole | `Lanco ebook/Sito- Leanding page/Gemini.md` |
| Libreria componenti | Sì, Next.js ~30 sezioni, 798 file | `Lancio corso skill beast/Leanding Page CCM/` |
| Struttura funnel | Sì | `KB_04_funnel-unico-perfetto.md` |
| Framework copy | Sì (ma APP-SOC, da riconciliare con APSOC) | `KB_07_app-soc-framework.md` |
| Script webinar | Sì | `WEBINAR_EVENTO.pdf` (+ variante applicata) |
| Sequenze email | Sì | `KB_08_email-sequence-master.md` |
| Prezzo | NO | "NON LO SO" |
| Data | NO | "Presto spero" |
| Lancio | NO | mai avvenuto |

**Nota di coerenza interna trovata in L2 (§10, riga 546-549):** il Framework I.C.R.O. (il lead magnet) insegna a scrivere un CLAUDE.md secondo il metodo I.C.R.O., ma "il CLAUDE.md di questo monorepo non segue I.C.R.O. ... vendiamo un metodo che in casa non applichiamo con quel nome."

**Stato a valle (CP-20260905-015.md e EMP-ECGA.md, 2026-09-05):** il piano completo (L4-L5-L6, 12 reparti, 50 agenti, 13 gate) è stato consegnato in `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` (verificato su disco — 11 file: `00-LEGGIMI-GAEL.md` … `10-ADR-PROPOSTO-E-I-TRE-GIRI.md`). Il ruolo del Manuale (pagamento vs gratuito) resta la prima delle 4 decisioni ancora aperte in attesa di Max, insieme all'approvazione dell'ADR-022, lo standard dei testi (APP-SOC vs APSOC) e il sistema visivo (Gemini.md vs empire-premium-style). Nessuna cartella `15-LANCI/` è stata creata. Nessuna data di lancio o prezzo risultano ancora decisi in nessuna delle fonti lette finora. **Verificato ora**: `company/Memory/decisions/` si ferma ad `ADR-021-pivot-piano-legamidiamore.md` — **ADR-022 non è ancora stato registrato**, coerente con quanto dichiarato (è "proposto", non applicato).

### Dati aggiuntivi trovati nella wiki (non citati nei checkpoint sopra) e CONTRADDIZIONI

Fonte: `second-brain-vault/wiki/09 - Archives/legacy/entities/Manuale_Claude_Code_Product.md` (Created 2026-04-29):
- **Prezzo suggerito qui: "TBD (€297-€497 recommended)"** — un terzo valore, diverso sia da "NON LO SO" (catalogo prodotti) sia da qualunque cifra del `PRODUCT_LADDER.md` a fasce (€97-297 o €497-997). **CONTRADDIZIONE**: tre fonti, tre modi diversi di trattare il prezzo, mai riconciliati.
- **Formato dichiarato qui: 38 capitoli** in 10 parti (Foundations, Installation & Setup, Core Architecture, Building Projects, Permission Modes, Context Management, Sub-Agents & Teams, Skill System, MCP Protocol, Advanced & Deployment) — il catalogo prodotti parla di "203 pagine" senza contare i capitoli: numeri compatibili ma mai incrociati nella stessa fonte.
- **Funnel di vendita descritto qui (§ Sales Funnel), testuale**: `YouTube Content (Free) → WhatsApp Community (Free) → Manuale Claude Code (€297-€497) → Vendi la Skill Video Course (€197-€397) → Premium Membership (€97-€197/month)`. Diverso e più articolato del funnel a due tappe ("Social → community → sales page → acquisto") descritto nel catalogo prodotti citato da ASSORBIMENTO-LANCI.md.
- **Metriche dichiarate qui**: "Sales: 0 (not yet launched)" — coerente con "Metriche: 0" del catalogo.
- Checklist "Before Launch" qui presente elenca esplicitamente come non fatto: decisione prezzo, sales page con narrativa, lead magnet (sequenza email o capitoli 1-3), funnel email, community WhatsApp, calendario YouTube — sostanzialmente lo stesso quadro di L2 ma da una fonte diversa e con data precedente (29 aprile) a quella del catalogo (7 marzo risulta antecedente: **discrepanza di date** — il catalogo è datato "ultimo aggiornamento 07/03/2026" ma descrive lo stesso stato "Pronto" che questa pagina, di quasi due mesi dopo, tratta ancora come da lanciare).

Fonte: `second-brain-vault/wiki/09 - Archives/legacy/projects/Claude_Code_Mastery_Launch.md` (Created 2026-04-29):
- Documento di **piano di lancio** con timeline esplicita: "START (2026-04-29) → TARGET SHIP (2026-05-30)", Status "🟡 Planning". **Questa data-obiettivo (30 maggio 2026) è passata da oltre 3 mesi rispetto a oggi (5 settembre 2026) senza che il lancio sia avvenuto** — nessuna fonte letta finora dichiara esplicitamente questo mancato rispetto della scadenza, è una deduzione diretta dalle date nei documenti.
- Owner dichiarato: Max. Scope include VSL 8-12 min, landing page, strategia YouTube, funnel email; esclude esplicitamente "Produzione corso completo" e "Community platform setup".
- Milestone 2026-05-07: VSL script + competitor analysis + wireframe landing. Milestone 2026-05-15: VSL prodotto, landing live, 2-3 video YouTube pubblicati. Milestone 2026-05-30: funnel completo live, calendario YouTube pubblico, "primi 50 beta testers iscritti". **Nessuna fonte in questa ricerca conferma che una di queste milestone sia stata raggiunta.**

Fonte: `second-brain-vault/wiki/log.md`, righe 1047-1063 (2026-07-29 e 2026-07-31):
- Riga 1054-1057: *"CORREZIONE: il primo contenuto YouTube reale generato era ancora sul funnel morto 'Manuale Claude Code' — pivot deciso da Gael a @dosementale come canale sorgente (replica per un canale da vendere già monetizzato, zero funnel)."*
- Riga 1060-1063: *"apex7_orchestrator.py (F1-F5) riscritto per intero su @dosementale — prima era solo il contenuto ad essere cambiato, il motore restava cablato sul Manuale Claude Code (rischio concreto di sovrascrittura)."*
- **CONTRADDIZIONE RILEVANTE**: il 2026-07-29/31 il canale YouTube pensato per alimentare il lancio del Manuale Claude Code viene definito **"funnel morto"** e abbandonato in favore di un canale diverso (@dosementale). Le fonti L1/L2/L3 di settembre (26-ECOSISTEMA-LANCI.md, ASSORBIMENTO-LANCI.md) non menzionano questo abbandono: continuano a trattare il Manuale Claude Code come "pronto da marzo, manca solo prezzo e data", senza notare che il canale YouTube che avrebbe dovuto fargli da traffico è stato dirottato altrove a fine luglio. Non è chiaro dalle fonti se esista oggi un canale/motore di traffico dedicato al Manuale Claude Code diverso da quello dirottato.

## 6. CAPACITA' GIA' ESISTENTI NELL'IMPERO CHE UN ECOSISTEMA LANCI DOVREBBE USARE

Fonte primaria: `PIANO-MAESTRO/RICOGNIZIONE-LANCI.md` §3 (11 skill esterne verificate con `ls .claude/skills/<nome>/SKILL.md`, riconfermate ora con lo stesso comando):

| Skill | Percorso assoluto | Destinazione (reparto L3) |
|---|---|---|
| `launch` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\launch\SKILL.md` | Esecuzione Lancio |
| `ads` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\ads\SKILL.md` | Marketing & Traffico |
| `ad-creative` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\ad-creative\SKILL.md` | Marketing & Traffico |
| `cro-copy-architect` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\cro-copy-architect\SKILL.md` | Copy |
| `empire-premium-style` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\empire-premium-style\SKILL.md` | Siti & Funnel |
| `site-build` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\site-build\SKILL.md` | Siti & Funnel |
| `site-copy` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\site-copy\SKILL.md` | Siti & Funnel |
| `site-deploy` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\site-deploy\SKILL.md` | Siti & Funnel |
| `pricing` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\pricing\SKILL.md` | Pricing & Offerta |
| `signup` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\signup\SKILL.md` | Siti & Funnel |
| `paywalls` | `C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\paywalls\SKILL.md` | Pricing & Offerta |

Tutte e 11 riconfermate esistenti in questa sessione (`ls .claude/skills/<nome>/SKILL.md` → OK per tutte).

**Reparti esistenti (specifica scritta, zero eseguibili) che l'ecosistema LANCI dovrebbe wrappare, non riscrivere** (percorsi assoluti confermati con `find` in questa sessione):
- `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\02-INFO-BUSINESS\Reparti\IB-L2-LANC-Lanci-Campagne\` — 2.377 righe, 9 agenti-scheda, workflow `WF-LANCIO.md` e `WF-WEBINAR.md` (giudicati "carta ma di qualità")
- `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\02-INFO-BUSINESS\Reparti\IB-L2-PROD-Produzione-Prodotti\` — 2.703 righe, 10 agenti-scheda
- `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\02-INFO-BUSINESS\Reparti\IB-L2-STRA-Strategia-Intelligence\` — 2.413 righe, 7 agenti-scheda
- `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\02-INFO-BUSINESS\Reparti\IB-L2-VEND-Vendite-Funnel\` — 2.353 righe, 8 agenti-scheda
- `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\02-INFO-BUSINESS\Reparti\IB-L2-COMM-Community-Retention\` — 2.181 righe (destinatario dell'handoff in uscita post-vendita, non wrappato dentro LANCI)
- `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\04-MARKETING\Reparti\L2-1-Copywriting\` — 2.934 righe
- `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\04-MARKETING\Reparti\L2-2-Advertising\` — 2.906 righe
- `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\04-MARKETING\Reparti\L2-3-Email-Lifecycle\` — 2.611 righe

**Asset di codice/contenuto già pronti (non skill/agenti, ma materiale finito) individuati da L2 (ASSORBIMENTO-LANCI.md), percorso originale come citato nelle fonti (relativo alla root del monorepo, non ancora verificato assoluto in questa sessione):**
- `Lancio corso skill beast/Framework_ICRO_Digital_Empire.pdf` — lead magnet finito, 12 pagine
- `Lanco ebook/Sito- Leanding page/index.html` — landing page costruita, 299 righe
- `Lanco ebook/Sito- Leanding page/Gemini.md` — design system, 54 righe
- `Lancio corso skill beast/Leanding Page CCM/` — libreria componenti Next.js, 798 file, ~30 sezioni (incluso gruppo `ObjectionCPB_*`, con l'avvertenza da `CP-20260905-015.md` che questi componenti **non accettano props** ed erano stati citati come pronti per errore nella prima versione del piano 29-ECOSISTEMA-LANCI, poi corretta)

**Piano di costruzione già scritto che usa/estende queste capacità:** `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` (11 dossier, verificati presenti su disco in questa sessione: `00-LEGGIMI-GAEL.md`, `01-GERARCHIA-E-REPARTI.md`, `02-MEMORIA-E-HANDOFF.md`, `03-WF-PRODOTTO.md`, `04-WF-OFFERTA.md`, `05-WF-COPY.md`, `06-WF-FUNNEL-E-EDITORIALE.md`, `07-WF-TESORO-MERCATO-REGIA.md`, `08-AGENTI-SKILL-COMANDI.md`, `09-COSTRUZIONE-E-PILOTA.md`, `10-ADR-PROPOSTO-E-I-TRE-GIRI.md`) — non letto in dettaglio in questa ricognizione (fuori dal perimetro delle 8 fonti assegnate), ma è il documento che dovrebbe già rispondere a "come si usano le capacità esistenti".

**BACKLOG collegato (`company/Memory/BACKLOG.md`):**
- **B-002** (riga 10): "Prezzo 'Manuale Claude Code' + ruolo (prodotto vs lead magnet) — NON si decide a mano: lo proporrà il team prezzi (B-003) — gate F6 (lancio reale)". Stato: ⬜ (aperto).
- **B-003** (riga 11): "Team agenti PREZZI — skill `pricing` (installata) come motore + `beast-preventivi`; team L4 in 04-MARKETING/Analytics o 02-INFO-BUSINESS/Vendite; propone prezzi data-driven, Max approva — fase F5/F6". Stato: ⬜ (aperto). Questo è lo stesso "team-prezzi" che `26-ECOSISTEMA-LANCI.md` (riga 316) definisce ancora "solo una promessa in ADR-005", cioè mai costruito.

## 7. FONTI CHE NON HO TROVATO

- **Nessuna fonte non trovata fra le 8 elencate nel compito**: tutti gli 8 punti richiesti sono stati aperti con successo, inclusi i due (RICOGNIZIONE-LANCI.md e ASSORBIMENTO-LANCI.md) che andavano cercati per nome perché il percorso non era dato — trovati entrambi in `PIANO-MAESTRO/` con `find`, non serviva cercare altrove.
- **Skill/asset dichiarati nella task o nelle fonti L1/L2 che risultano NON esistenti sul disco** (dichiarato esplicitamente dalle fonti stesse, non una mia ricerca fallita, ma lo riporto perché rilevante per "cosa non c'è"):
  - `System OMEGA/.../CONTESTO - SOLO ESEMPI/Product Pricing Strategist.skill` — non esiste (verificato in ASSORBIMENTO-LANCI.md con `find . -iname "*.skill*"` → nessun risultato in tutto il repo)
  - `System OMEGA/.../CONTESTO - SOLO ESEMPI/VSL Script Builder.skill` — non esiste, e a differenza delle altre due non ha nemmeno una fonte sostitutiva
  - `System OMEGA/.../CONTESTO - SOLO ESEMPI/Webinar Script Master.skill` — non esiste (fonte sostitutiva trovata nei PDF "Webinar Milionario")
  - `.claude/skills/launch-runbook/` — dichiarata P0 dal 2026-06-21 in `SKILLS.md` del reparto IB-L2-LANC, mai forgiata
  - I 3 script `launch_calendar.py`, `dry_run_costs.py`, `launch_debrief_diff.py` dichiarati in `scripts/README.md` del reparto IB-L2-LANC come "pianificati (build in V2)" — nessuno dei tre esiste sul disco
- **Non ho trovato, e non è stato possibile determinare dalle 8 fonti assegnate**, se esista oggi (5 settembre 2026) un canale YouTube o un motore di traffico attivo e dedicato specificamente al Manuale Claude Code, dato che il log wiki (2026-07-29/31) documenta il dirottamento del motore YouTube da questo prodotto a @dosementale. Nessuna delle fonti L1/L2/L3/CP-20260905-015/EMP-ECGA affronta questo punto: sarebbe da verificare con una ricerca dedicata, fuori dal perimetro di questo incarico.
- **Non ho letto in dettaglio** i contenuti dei dossier `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/01` … `09` (solo verificata la loro esistenza su disco): il compito assegnato indicava come fonte solo `CP-20260905-015.md` e `EMP-ECGA.md` come riassunto di quel piano, non i dossier stessi. Se serve la ricognizione riga-per-riga dei 12 reparti/50 agenti/13 gate del piano definitivo, va fatta come task separata.
- **Non ho cercato** oltre le 8 fonti indicate un'eventuale versione più recente o "ufficiale" del catalogo prodotti (`CATALOGO PRODOTTI ATTUALE — Info-Bu.md`, datata 07/03/2026) che possa aver aggiornato prezzo/data dopo tale data: le fonti assegnate non la richiedevano e non modifico né apro file extra oltre a quanto necessario per completare le sezioni richieste.
