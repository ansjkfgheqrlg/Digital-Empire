---
Type: PROJECT
Status: Proposta
Tags: #lanci #ecosistema-15 #prodotto
Created: 2026-09-05
---

# 03 — WF-PRD · IL FLUSSO DEL PRODOTTO

> **Nota di lettura.** Questo dossier copre la **creazione e certificazione del prodotto**.
> I testi di marketing hanno un dossier proprio, il **05**, che è stato riscritto dopo la critica:
> la griglia di punteggio che trovavi qui nella prima stesura è **superata** da quella.
>
> **Tre correzioni valgono anche per questo flusso**, e vengono dai revisori:
> 1. Le sigle dei gate qui usate (`GP-*`) sono sostituite dalla numerazione unica
>    `GATE-PRD-1/2/3` — dossier 00 §5.2.
> 2. Le durate in **giorni** vanno lette come **ore-uomo**: 12-20 giorni pieni non esistono in
>    un'azienda dove si fa anche altro. Il percorso per prodotti già esistenti è **20-30 ore**.
> 3. Il criterio *"100% delle fonti raggiungibili"* è **allineato a ≥90%** (dossier 07 §B.3): due
>    soglie diverse sullo stesso file mandavano il primo lancio in stallo fra due reparti.
>
> **Il percorso per prodotti già esistenti (§5, percorso E) è il cuore di questo dossier:** è
> quello che il Manuale Claude Code attraverserà, e la sua regola è una sola — *salta la
> produzione, non salta mai la certificazione*.

---


> Progettazione dei workflow **WF-1 CREAZIONE PRODOTTO** e **WF-2 MATERIALI MARKETING & COPYWRITING**
> per l'ecosistema **15-LANCI** di Digital Empire.
>
> Fonti lette per intero: `BRIEFING-MAESTRO.md` · `PIANO-MAESTRO/ASSORBIMENTO-LANCI.md`
> (§5, §6, §9, §10 usate direttamente) · `PIANO-MAESTRO/26-ECOSISTEMA-LANCI.md` ·
> `.claude/skills/cro-copy-architect/SKILL.md` (esiste; usata come riferimento di livello).
>
> ⚠️ Nota di numerazione: `26-ECOSISTEMA-LANCI.md` scrive "14-LANCI"; il briefing corregge —
> **il numero è 15** (14 è TESORERIA). Qui si usa sempre `15-LANCI`. L'aggiornamento del file L3
> non è di quest'area (→ SEGNALAZIONI).
>
> Convenzione dei percorsi di lavoro: ogni lancio vive in
> `company/Ecosistemi/15-LANCI/lanci/<lancio_id>/` (namespace BRAIN `lanci/{lancio-id}/` di L3).
> Nessuna cartella viene creata da questo documento: è carta di progetto.

---
---

# WF-1 — CREAZIONE PRODOTTO

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-PROD` |
| **Nome** | Workflow Creazione e Certificazione Prodotto |
| **Missione** | Trasforma un'idea validata (o un prodotto già esistente) in un **prodotto certificato pronto da vendere**: architettura didattica provata, 6 red flag a zero, beta test fatto se dovuto, pacchetto consegnabile. |
| **Proprietario** | Reparto **LAN-PRODOTTO** (WRAP di `IB-L2-PROD`, 02-INFO-BUSINESS) |
| **Durata tipica** | **Percorso N (prodotto nuovo): 12-20 giorni lavorativi.** **Percorso E (prodotto esistente): 3-5 giorni lavorativi** — salta la produzione, non la certificazione. |

Rispetto della regola §1.5 di L3 (un reparto WRAP ha solo agenti di interfaccia e di gate): gli
agenti di produzione qui nominati **ufficializzano** le schede agente già progettate in
`IB-L2-PROD` (10 schede, 2.703 righe, zero agenti invocabili). Non sono duplicati: sono
l'**incarnazione ufficiale unica** di quelle specifiche (ADR-003 + ADR-008 + "niente si scarta").
La conoscenza resta di IB-L2-PROD; l'esecuzione diventa invocabile qui.

## 2. Trigger

| Tipo | Dettaglio |
|---|---|
| **Handoff in ingresso** | LAN-STRATEGIA deposita `lanci/<lancio_id>/decisione.json` con `verdetto: "GO"` (filtro anti-ADD passato, G1). Questo **abilita** il workflow, non lo avvia. |
| **Comando esatto** | `/lancio-prodotto <lancio_id>` — lo lancia Max o Gael. Nessun avvio automatico: un prodotto entra in produzione solo per ordine umano esplicito. |
| **Evento equivalente** | Nessuno. Il deposito di `decisione.json` senza comando non fa partire nulla (anti-pre-mortem #2: il sistema non deve girare a vuoto). |

## 3. Input tipizzato

File atteso: `company/Ecosistemi/15-LANCI/lanci/<lancio_id>/input-prodotto.json`

```json
{
  "lancio_id": "string",
  "percorso": "N | E",
  "decisione_path": "string (path a decisione.json)",
  "brief": {
    "idea": "string",
    "score": "number (0-100)",
    "mvp_conferme": ["string — nome o identificativo di chi ha detto 'lo comprerei'"],
    "target": "string — mai 'chiunque voglia imparare X'",
    "formato": "PDF | Ebook | Mini-corso | Corso | Percorso",
    "fascia_prezzo_ipotizzata": "string — livello Product Ladder 0-4"
  },
  "ricerca_path": "string (path a ricerca.json prodotto dal WF Intelligence)",
  "offerta_path": "string | null (path a offerta.json di LAN-PRICING, se già esiste)",
  "prodotto_esistente": {
    "percorso_asset": "string — cartella del prodotto già fatto",
    "formato": "string",
    "dichiarato_pronto_da": "string (data ISO)"
  }
}
```

| Campo | Tipo | Obbligatorio | Se manca |
|---|---|---|---|
| `lancio_id` | string | ✅ sempre | **STOP exit 2** — niente parte senza identità del lancio |
| `percorso` | enum N/E | ✅ sempre | **STOP exit 2** — il workflow non indovina il percorso |
| `decisione_path` | string | ✅ sempre | **STOP exit 2** — senza GO di Strategia non si entra |
| `brief.idea` | string | ✅ sempre | **STOP exit 2** |
| `brief.score` | number | ✅ percorso N | **BLOCK exit 1** al gate GP-1 (percorso E: facoltativo, il prodotto esiste già — la validazione è il mercato che sta per testarlo, ma la sua assenza va scritta nel certificato come "score: non misurato") |
| `brief.mvp_conferme` | array ≥5 | ✅ percorso N | **BLOCK exit 1** a GP-1 |
| `brief.target` | string | ✅ sempre | **STOP exit 2** — senza target non c'è architettura né copy a valle |
| `brief.formato` | enum | ✅ sempre | **STOP exit 2** |
| `brief.fascia_prezzo_ipotizzata` | string | ✅ sempre | **STOP exit 2** — serve alla regola beta test (≥€97) |
| `ricerca_path` | string | ✅ sempre | **STOP exit 2** — la ricerca è bloccante per definizione (fonte: *"Non si procede senza aver completato questo step"*) |
| `offerta_path` | string\|null | ⬜ | Se `null`, la regola beta test assume il **caso peggiore** (≥€97 → beta obbligatorio). Mai il contrario. |
| `prodotto_esistente.*` | object | ✅ se percorso E | **STOP exit 2** — percorso E senza asset non ha senso |

## 4. Precondizioni

Ognuna verificabile con un comando, nessuna "di fiducia":

| # | Precondizione | Verifica |
|---|---|---|
| P1 | `decisione.json` esiste e `verdetto == "GO"` | `python prodotto_intake.py --check-decisione <path>` → exit 0 |
| P2 | `ricerca.json` esiste ed è JSON valido conforme allo schema del WF Intelligence | `python verifica_ricerca.py <path> --solo-schema` → exit 0 |
| P3 | Il registro lanci non contiene già un `certificato-prodotto.json` per questo `lancio_id` (idempotenza: se c'è, il comando lo dice e chiede `--rifai` esplicito) | check esistenza file |
| P4 | Percorso E: la cartella `prodotto_esistente.percorso_asset` esiste e contiene ≥1 file | check filesystem |
| P5 | Blocco ⚠️ COORDINAMENTO scritto in `company/Memory/STATO-EMPIRE.md` se il lavoro supera 1 giornata (ADR-006) | presenza della riga, verificata a mano da chi lancia |

## 5. Le fasi

### Percorso N — prodotto nuovo

| # | Fase | Cosa fa | Agente | Input | Output (file) | Durata | Parallelo | Umano |
|---|---|---|---|---|---|---|---|---|
| **N0** | Intake e smistamento | Valida `input-prodotto.json` contro lo schema, verifica P1-P5, smista N/E | `lan-prod-intake` | `input-prodotto.json` | `lanci/<id>/prodotto/00-intake.json` (esiti campo per campo) | 0,5 h | no | no |
| **N1** | Verifica validazione idea | Controlla score ≥60/100 e ≥5 conferme MVP **nominali** (non "5 persone": 5 identificativi) | `lan-prod-intake` | `brief` | `prodotto/01-validazione.json` | 0,5 h | no | no |
| **N2** | Verifica ricerca in ingresso | Conta 15/5/3/3, verifica che il 100% delle URL risponda, spot-check di contenuto su 3 frasi a campione (la frase citata deve comparire nella pagina) | `lan-prod-verificatore-ricerca` | `ricerca.json` | `prodotto/02-verifica-ricerca.json` | 1-2 h | no | no |
| **N3** | Architettura didattica | Progetta i moduli: **max 7, ideale 5**, 1 modulo = 1 trasformazione "da [prima] a [dopo]", ogni modulo con output pratico dichiarato. Regola dura dalla fonte: *"se non sai dire da [prima] a [dopo], il modulo non è pronto"* | `lan-prod-architetto` (ufficializza la scheda Learning-Path di IB-L2-PROD, fonte `KB_03_LEARNING_PATH_ENGINE.md`) | brief + ricerca verificata | `prodotto/03-architettura.json` | 0,5-1 g | no | **Sì, 15 min**: Max o Gael approva la lista moduli prima della produzione — è il punto più economico per cambiare rotta; dopo, ogni modifica costa giorni |
| **N4** | Produzione contenuti | Produce i contenuti modulo per modulo secondo gli standard per tipo (fonte `KB_04_PRODUZIONE_CONTENUTI.md` + `KB_07_STANDARD_PER_TIPO.md`): testo, template CON esempio compilato, esercizi, asset | `lan-prod-produttore` (ufficializza le schede di produzione di IB-L2-PROD) | `03-architettura.json` approvata | `prodotto/contenuti/` (un sottofolder per modulo: `M01/`, `M02/`…) + `prodotto/04-produzione.json` (indice: modulo → file → stato) | 5-12 g | **Sì**: i moduli si producono in parallelo (1 istanza agente per modulo, prompt idempotenti, ADR-006) | no |
| **N5** | Collaudo — 6 red flag | Esegue i 6 test dei red flag (tabella al §6) su TUTTO il prodotto. Non si fida di `04-produzione.json`: rilegge i file | `lan-prod-collaudatore` — **mai** lo stesso di N4 | `prodotto/contenuti/` | `prodotto/05-collaudo.json` (per red flag: esito, evidenza, file incriminati) | 0,5-1 g | no | no |
| **N6** | Beta test | Se prezzo (da `offerta.json`, o caso peggiore se assente) **≥€97**: recluta ≥5 beta tester, raccoglie feedback strutturato, impone fix per ogni problema segnalato da ≥2 tester (fonte `KB_05`), poi ri-passa N5 sui moduli toccati | `lan-prod-beta-coordinatore` | prodotto collaudato | `prodotto/06-beta.json` (tester, feedback, fix applicati) | 5-7 g (cap: 7) | **Sì**: gira in parallelo con l'avvio di WF-2 (il copy non aspetta il beta; aspetta il certificato solo per la consegna finale) | **Sì, per natura**: i beta tester sono umani; il reclutamento lo approva Max |
| **N7** | Packaging | Impagina/assembla il consegnabile finale (PDF, area corso, zip template), naming e struttura da `KB_06_PACKAGING_HANDOFF.md` | `lan-prod-packager` | contenuti post-beta | `prodotto/pacchetto/` + `prodotto/07-packaging.json` | 0,5-1 g | no | no |
| **N8** | Certificazione e handoff | **Ricalcola tutto dai file** (non dai JSON di stato dichiarati): red flag, beta, packaging. Emette il certificato. Firma umana se ≥€97 | `lan-prod-certificatore` — indipendente da N4-N7 | tutti gli output precedenti | `lanci/<id>/certificato-prodotto.json` | 2 h | no | **Sì se ≥€97**: firma di Max o Gael nel campo `firma_umana` — un prodotto caro non esce con sola firma di macchina |

### Percorso E — prodotto già esistente (il caso Manuale Claude Code, 203 pagine)

**Principio esplicito: il percorso E salta la PRODUZIONE, non salta MAI la CERTIFICAZIONE.**
Il Manuale è "Pronto" dal 07/03/2026 secondo un file che nessuno ha mai collaudato: "pronto
dichiarato" e "pronto certificato" sono due stati diversi, e questo percorso esiste per
trasformare il primo nel secondo.

| # | Fase | Cosa fa | Agente | Input | Output (file) | Durata | Parallelo | Umano |
|---|---|---|---|---|---|---|---|---|
| **E0** | = N0 | Intake, smistamento su E | `lan-prod-intake` | `input-prodotto.json` | `prodotto/00-intake.json` | 0,5 h | no | no |
| **E1** | Inventario asset | Censisce ogni file del prodotto: pagine, capitoli, template, link contenuti, media. Nessun giudizio, solo conteggio | `lan-prod-inventariante` | `percorso_asset` | `prodotto/E1-inventario.json` | 2-4 h | no | no |
| **E2** | Retro-architettura | Mappa i capitoli esistenti sulle trasformazioni "da [prima] a [dopo]". Serve a due cose: certificare la tenuta didattica E dare a WF-2 le trasformazioni per i bullet della sales page. Soglia (proposta nuova, dichiarata): **≥80% dei capitoli mappati a una trasformazione, 100% dei moduli che compariranno in sales page**. Capitoli non mappabili → etichettati "supporto" nel file | `lan-prod-architetto` | `E1-inventario.json` + il prodotto | `prodotto/03-architettura.json` (stesso schema di N3, con campo `retro: true`) | 0,5-1 g | no | no |
| **E3** | = N5 | Collaudo 6 red flag **integrale** — sul Manuale significa: ogni link delle 203 pagine testato in incognito, ogni template con esempio compilato, ecc. | `lan-prod-collaudatore` | prodotto + inventario | `prodotto/05-collaudo.json` | 0,5-1 g | no | no |
| **E4** | = N6 | Beta test. Per il Manuale: prezzo oggi = "NON LO SO" → `offerta.json` assente o non valida → **caso peggiore → beta obbligatorio** (≥5 tester sul prodotto vero). Se LAN-PRICING nel frattempo fissa un prezzo <€97, il gate si rilegge e il beta decade | `lan-prod-beta-coordinatore` | prodotto collaudato | `prodotto/06-beta.json` | 5-7 g | **Sì** con WF-2 | **Sì** (tester + ok Max al reclutamento) |
| **E5** | = N7 + N8 | Packaging (spesso già fatto: si verifica, non si rifà) + certificazione con ricalcolo integrale | `lan-prod-packager` poi `lan-prod-certificatore` | tutto | `certificato-prodotto.json` | 0,5 g | no | **Sì se ≥€97** |

Nota sul primo giro reale: il doppio ruolo del Manuale (Premium a pagamento vs lead magnet
gratuito, conflitto aperto dall'11 giugno) **non è di questo workflow** — è di LAN-PRICING/Max.
WF-PROD lo tratta così: finché `offerta.json` non esiste, certifica col caso peggiore (beta
incluso). Il certificato non aspetta il prezzo; la vendita sì.

## 6. I gate

Regola trasversale: **chi produce non approva** — ogni gate è eseguito da un agente diverso da
chi ha prodotto l'output. Ogni gate scrive un verbale-file; un gate senza verbale **non è stato
eseguito** (la dichiarazione verbale non esiste).

| Sigla | Dove | Criterio (numerico o binario) | Chi lo esegue | Se BLOCCA | Come si sblocca |
|---|---|---|---|---|---|
| **GP-0** | prima di N0/E0 | `decisione.json` presente ∧ `verdetto == "GO"` (binario) | `lan-prod-intake` via `prodotto_intake.py` | Il comando esce 1, nessun file di lavoro creato | LAN-STRATEGIA emette il GO (fuori da quest'area) |
| **GP-1** | dopo N1 | `brief.score ≥ 60` ∧ `len(mvp_conferme) ≥ 5` (fonte `KB_01`) | `lan-prod-intake` (il brief l'ha prodotto Strategia/Prodotto a monte, quindi qui è terza parte) | Verbale con i campi mancanti; il lancio torna a chi ha fatto il brief | Nuovo brief con score e conferme reali; **le conferme sono identificativi, non un numero** |
| **GP-2** | dopo N2 | `frasi ≥ 15` ∧ ogni frase con `url` ∧ `pain_point ≥ 5` ∧ `competitor ≥ 3` ∧ `gap ≥ 3` ∧ 100% URL con HTTP 200/301 ∧ 3/3 spot-check di contenuto positivi | `lan-prod-verificatore-ricerca` via `verifica_ricerca.py` (la ricerca l'ha prodotta il WF Intelligence: terzietà garantita) | Verbale con il conteggio esatto (es. "frasi: 12/15, url morte: 2"); handoff respinto al WF Intelligence | Il WF Intelligence completa/corregge e rideposita; si riesegue solo GP-2, non tutto |
| **GP-3** | dopo N3/E2 | `1 ≤ n_moduli ≤ 7` ∧ 100% dei moduli con `da`/`a` non vuoti e diversi tra loro ∧ 100% dei moduli con `output_pratico` non vuoto ∧ (percorso E: copertura capitoli ≥80%) | `lan-prod-collaudatore` via `gate_architettura.py` (l'architetto non si autoapprova) | L'elenco dei moduli non pronti, verbatim: *"se non sai dire da [prima] a [dopo], il modulo non è pronto"* | L'architetto riformula SOLO i moduli bocciati; max 2 giri, poi escalation a Max |
| **GP-4** | dopo N5/E3 | **6/6 red flag assenti** — uno solo presente → BLOCK (fonte `KB_05`). Test scritto di ciascuno: **RF1** lezione senza output pratico → per ogni modulo, il file dell'output pratico esiste ed è >0 byte, e il collaudatore lo esegue/compila davvero · **RF2** template senza esempio compilato → per ogni template, esiste il gemello `-ESEMPIO` compilato con dati realistici · **RF3** concetto chiave non spiegato → ogni termine della lista `concetti_chiave` dell'architettura compare spiegato PRIMA del primo uso (ricerca testuale + lettura del passaggio) · **RF4** audio/video incomprensibile → ascolto dei primi e ultimi 2 min di ogni media + 1 punto casuale; giudizio binario "si capisce senza riavvolgere?" registrato per file · **RF5** link o file non funzionante → *"testa ogni link in modalità incognito, come lo studente non loggato"*: 100% dei link con esito registrato · **RF6** salto logico tra moduli → per ogni coppia (Mn, Mn+1): lo stato "dopo" di Mn è compatibile con lo stato "prima" di Mn+1, verdetto per coppia | `lan-prod-collaudatore` via `collaudo_red_flag.py` (RF1-2-5 automatici; RF3-4-6 semi-automatici con giudizio registrato per item) | Verbale con red flag, evidenza e file; il prodotto torna in N4 (o al proprietario dell'asset in percorso E) SOLO sui punti bocciati | Fix mirati, ri-collaudo dei soli item bocciati + RF6 sempre integrale |
| **GP-5** | dopo N6/E4 | Se prezzo ≥€97 (o ignoto): `n_tester_invitati ≥ 5` ∧ `n_tester_completato ≥ 3` (soglia proposta, dichiarata nuova) ∧ 100% dei problemi segnalati da ≥2 tester marcati `risolto` con link al fix ∧ ri-collaudo GP-4 sui moduli toccati = PASS. Se prezzo certo <€97: gate AUTO-PASS con motivo scritto | `lan-prod-certificatore` (il beta l'ha coordinato un altro agente) | Il lancio slitta: **il beta non si salta, si aspetta**. Verbale con cosa manca | Tester reclutati / fix completati; nessuna deroga di macchina — la deroga può firmarla solo Max, e resta scritta nel certificato |
| **GP-6** | in N8/E5 | Certificazione = ricalcolo indipendente: GP-1…GP-5 tutti PASS **ricontrollando i file su disco, non i JSON di stato** ∧ `prodotto/pacchetto/` esiste, non vuoto ∧ per prezzo ≥€97: campo `firma_umana` valorizzato da Max o Gael | `lan-prod-certificatore` via `certifica_prodotto.py` | Nessun certificato emesso; il verbale dice quale ricalcolo diverge dallo stato dichiarato — e la divergenza finisce in `REGISTRO-ERRORI` (Ispettorato) | Si sana la divergenza reale; il certificato si emette solo quando dichiarato e ricostruito coincidono |

## 7. Output tipizzato

File: `company/Ecosistemi/15-LANCI/lanci/<lancio_id>/certificato-prodotto.json`

```json
{
  "lancio_id": "string",
  "percorso": "N | E",
  "prodotto": {
    "nome": "string",
    "formato": "string",
    "percorso_pacchetto": "string",
    "n_moduli": "number",
    "trasformazioni": [{"modulo": "M01", "da": "string", "a": "string", "output_pratico": "string"}]
  },
  "gate": {
    "GP-1": {"esito": "PASS", "score": 74, "mvp_conferme": 6},
    "GP-2": {"esito": "PASS", "frasi": 17, "pain": 6, "competitor": 3, "gap": 4, "url_ok": "17/17"},
    "GP-3": {"esito": "PASS", "n_moduli": 5},
    "GP-4": {"esito": "PASS", "red_flag": [0,0,0,0,0,0]},
    "GP-5": {"esito": "PASS | AUTO-PASS", "motivo": "string", "tester": 5, "completati": 3, "fix": 4},
    "GP-6": {"esito": "PASS", "firma_umana": "Max | Gael | null", "data": "ISO"}
  },
  "non_misurato": ["string — ogni dato assente dichiarato, mai stimato"],
  "emesso_da": "lan-prod-certificatore",
  "data_certificazione": "ISO"
}
```

File prodotti dal workflow (tutti sotto `company/Ecosistemi/15-LANCI/lanci/<lancio_id>/`):

| File | Fase |
|---|---|
| `prodotto/00-intake.json` · `prodotto/01-validazione.json` · `prodotto/02-verifica-ricerca.json` | N0-N2 |
| `prodotto/03-architettura.json` | N3/E2 |
| `prodotto/contenuti/M*/` + `prodotto/04-produzione.json` | N4 |
| `prodotto/05-collaudo.json` · `prodotto/06-beta.json` · `prodotto/07-packaging.json` | N5-N7 |
| `prodotto/E1-inventario.json` | E1 |
| `prodotto/pacchetto/` | N7/E5 |
| `certificato-prodotto.json` | N8/E5 |

## 8. Handoff in uscita

| A chi | Cosa | Criterio di accettazione (lo verifica chi riceve) |
|---|---|---|
| **WF-2 (LAN-COPY)** | `certificato-prodotto.json` + `03-architettura.json` (le trasformazioni sono la materia prima dei bullet e della promessa) | Certificato con GP-4 = 6/6 PASS e schema valido; architettura con 100% trasformazioni compilate |
| **LAN-PRICING** | `03-architettura.json` + `01-validazione.json` (fascia ipotizzata + valore percepito per lo stack) | Schema valido; può partire già dopo GP-3, non serve il certificato |
| **LAN-SITI** | `prodotto/pacchetto/` (il consegnabile da collegare a thank you page / area riservata) | Pacchetto non vuoto; ogni file del pacchetto aperto con successo una volta |
| **LAN-ESECUZIONE** | `certificato-prodotto.json` (precondizione per il calendario: senza certificato il carrello non si apre) | GP-6 PASS con firma umana se dovuta |
| **10-MEMORY** | Checkpoint di chiusura + eventuali pattern (es. red flag ricorrenti) | Regola ADR-002: nessun task è fatto finché non è in Memory |

## 9. Fallimenti

| Modo di fallimento | Sintomo | Cosa fa il sistema |
|---|---|---|
| **Un agente dichiara fatto senza averlo fatto** (la malattia documentata: `push_social.py` che stampa "successo (SIMULATA)" ed esce 0) | `04-produzione.json` dice "completo" ma i file mancano, sono vuoti o placeholder | GP-6 **ricalcola dai file, mai dai JSON di stato**: divergenza → BLOCK + voce in `REGISTRO-ERRORI` dell'Ispettorato + il modulo torna in produzione. Il collaudatore (N5) intercetta prima: rilegge i file, non l'indice |
| Ricerca fasulla (frasi inventate, URL di facciata) | Spot-check GP-2: la frase citata non compare nella pagina | BLOCK, verbale con le 3 frasi campionate, handoff respinto al WF Intelligence. Al secondo respingimento sullo stesso lancio → escalation a Max |
| Link morti / file rotti nel prodotto | RF5 in collaudo | Fix obbligatorio + ri-test in incognito dei soli link toccati; il gate non passa "con riserva" |
| Beta tester non reclutati | 7 giorni dal via di N6 senza ≥5 inviti accettati | Escalation a Max con tre opzioni scritte: allunga, recluta lui, o (solo lui) deroga firmata nel certificato. La macchina non deroga |
| Prodotto esistente non certificabile (percorso E) | E2 < 80% capitoli mappabili, o GP-4 con red flag strutturali | Il prodotto esce dal percorso E e rientra come percorso N parziale (si riproducono solo i moduli bocciati). Verbale del perché |
| Input malformato | Schema JSON non valido | Exit 2 immediato, stampa dei campi rotti, **zero file scritti** (idempotenza) |
| Loop di rework infinito | Stesso gate bocciato 2 volte | Al terzo tentativo il workflow si ferma da solo ed emette verbale di escalation a Max — un gate che bocca tre volte segnala un problema di monte, non di valle |
| Timeout di fase | Una fase supera 2× la durata stimata senza output | Recap forzato a Max (regola recap 10 minuti già attiva) con percentuale e blocco dichiarato |

## 10. Gli eseguibili

Tutti sotto `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\15-LANCI\scripts\`.
Convenzione exit code comune: **0** = PASS · **1** = BLOCK (gate fallito, verbale scritto) ·
**2** = input/schema non valido (nessun file di lavoro scritto) · **3** = errore d'ambiente
(rete, filesystem — riprovabile).

### `prodotto_intake.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `carica_input` | `carica_input(path: str) -> dict` | l'input validato contro lo schema; solleva `SchemaError` (→ exit 2) |
| `verifica_decisione` | `verifica_decisione(decisione_path: str) -> bool` | `True` solo se `verdetto == "GO"` |
| `verifica_brief` | `verifica_brief(brief: dict, percorso: str) -> tuple[bool, list[str]]` | (esito GP-1, elenco mancanze) |
| `smista_percorso` | `smista_percorso(input_lancio: dict) -> str` | `"N"` o `"E"`; scrive `00-intake.json` |

### `verifica_ricerca.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `conta_requisiti` | `conta_requisiti(ricerca: dict) -> dict` | `{"frasi": int, "pain": int, "competitor": int, "gap": int}` |
| `verifica_url` | `verifica_url(frasi: list[dict], timeout_s: int = 10) -> list[dict]` | per URL: `{"url": str, "status": int, "ok": bool}` |
| `spot_check` | `spot_check(frasi: list[dict], campione: int = 3, seed: int | None = None) -> list[dict]` | per frase campionata: la frase compare nella pagina? |
| `esito` | `esito(ricerca_path: str, out_path: str) -> int` | scrive `02-verifica-ricerca.json`, ritorna l'exit code |

### `gate_architettura.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `valida_moduli` | `valida_moduli(architettura: dict) -> list[str]` | elenco violazioni (vuoto = PASS): n>7, `da`/`a` vuoti o uguali, output pratico mancante |
| `copertura_capitoli` | `copertura_capitoli(architettura: dict, inventario: dict) -> float` | frazione 0-1 di capitoli mappati (solo percorso E) |
| `esito` | `esito(architettura_path: str, inventario_path: str | None) -> int` | exit code + verbale |

### `collaudo_red_flag.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `testa_link` | `testa_link(percorso_prodotto: str, timeout_s: int = 15) -> list[dict]` | ogni link trovato nei file: `{"link": str, "status": int, "ok": bool}` — RF5 |
| `verifica_output_pratici` | `verifica_output_pratici(architettura: dict, contenuti_dir: str) -> list[str]` | moduli senza file di output pratico >0 byte — RF1 |
| `verifica_template` | `verifica_template(contenuti_dir: str) -> list[str]` | template senza gemello `-ESEMPIO` — RF2 |
| `registra_giudizio` | `registra_giudizio(red_flag: int, item: str, esito: bool, nota: str) -> None` | appende il giudizio umano/agente su RF3-4-6 al verbale (un giudizio non registrato non esiste) |
| `report` | `report(lancio_dir: str) -> dict` | il verbale completo `05-collaudo.json`; exit 1 se ≥1 red flag |

### `certifica_prodotto.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `ricalcola_gate` | `ricalcola_gate(lancio_dir: str) -> dict` | riesegue le verifiche GP-1…GP-5 **dai file**, ritorna esiti indipendenti |
| `confronta_stati` | `confronta_stati(dichiarato: dict, ricostruito: dict) -> list[str]` | elenco divergenze (vuoto = coerente); ogni divergenza → `REGISTRO-ERRORI` |
| `emetti` | `emetti(lancio_dir: str, firma_umana: str | None) -> int` | scrive `certificato-prodotto.json` solo se tutto PASS; exit 1 se manca la firma dovuta |

## 11. La skill e il comando

| Campo | Valore |
|---|---|
| **Skill ufficiale** | `.claude/skills/lancio-prodotto/SKILL.md` — nome `lancio-prodotto`, description con trigger espliciti ("certifica il prodotto", "prepara il prodotto per il lancio", "percorso prodotto esistente", "/lancio-prodotto") |
| **Comando** | `/lancio-prodotto <lancio_id>` (+ flag `--rifai` per rieseguire su un lancio già certificato) |
| **Se manca l'input** | La skill NON improvvisa: stampa lo schema atteso di `input-prodotto.json`, l'elenco esatto dei campi mancanti e dove recuperarli (decisione → LAN-STRATEGIA, ricerca → WF Intelligence), ed esce con codice 2 **senza scrivere alcun file**. Se manca solo `lancio_id` lo chiede interattivamente, ed è l'unica domanda che fa |

Registrazione (ADR-008): la skill e gli 8 agenti (`lan-prod-intake`, `lan-prod-verificatore-ricerca`,
`lan-prod-architetto`, `lan-prod-produttore`, `lan-prod-collaudatore`, `lan-prod-beta-coordinatore`,
`lan-prod-packager`, `lan-prod-certificatore`, più `lan-prod-inventariante` per il percorso E)
vanno in `.claude/agents/*.md` con frontmatter minimo valido (`name`, `description` su una riga,
`model`, `color` — nessun campo inventato) + `company/REGISTRO-IMPRESA.md` + `skills-map.yaml` + wiki.

## 12. Come si misura che ha funzionato

| Metrica | Target | Fonte della soglia |
|---|---|---|
| Tempo ciclo percorso E (Manuale Claude Code, primo giro) | ≤5 giorni lavorativi dall'intake al certificato | proposta (dichiarata) |
| Prodotti che passano GP-4 al primo collaudo | ≥70% | proposta (dichiarata) |
| Red flag scoperti DOPO il lancio | **0** | il senso stesso del collaudo |
| Refund rate post-vendita | <5% (critico >10%) | `KB_08_METRICHE_KPI.md` |
| Completion rate | >40% (critico <20%) | `KB_08_METRICHE_KPI.md` |
| Testimonial entro 30 giorni | ≥3 | `KB_08_METRICHE_KPI.md` |
| Beta test eseguito su prodotti ≥€97 | 100%, *"nessuna eccezione — processo rotto"* | `KB_08_METRICHE_KPI.md` |
| Certificati con divergenza dichiarato/ricostruito | 0 (ogni divergenza è una voce in REGISTRO-ERRORI) | Mandato Art. 2 |

Refund, completion e testimonial si misurano a valle (li raccoglie LAN-ESECUZIONE nel debrief),
ma **si attribuiscono a questo workflow**: se il refund supera il 5%, il primo indiziato è la
certificazione, non il traffico.

---
---

