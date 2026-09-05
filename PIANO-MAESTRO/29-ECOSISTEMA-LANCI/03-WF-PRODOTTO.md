# V1 — WORKFLOW CREAZIONE PRODOTTO E MATERIALI MARKETING

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

# WF-2 — MATERIALI MARKETING & COPYWRITING

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-COPY` |
| **Nome** | Workflow Materiali Marketing & Copywriting |
| **Missione** | Produce **tutto il materiale testuale e creativo del lancio nell'ordine giusto** — la sales page come documento madre, e da lei ogni altro pezzo — con ogni pezzo passato dal gate ≥80/100 prima di uscire. |
| **Proprietario** | Reparto **LAN-COPY** (WRAP di `04-MARKETING/L2-1-Copywriting` + `L2-3-Email-Lifecycle` + skill `cro-copy-architect` + guild `guild-copy-apsoc`) |
| **Durata tipica** | **5-8 giorni lavorativi** (di cui 3-4 in sprint parallelo dopo l'approvazione della sales page) |

Rispetto §1.5 di L3: gli agenti di scrittura **wrappano** la skill `cro-copy-architect` (che
esiste, funziona e ha già checklist e reference: la si invoca, non la si riscrive — ADR-003);
il giudice wrappa la rubrica di questo documento; la verifica brand voice wrappa l'agente
**già ufficiale** `sentinel-brandvoice` (nessun nuovo agente per quel compito).

## 2. Trigger

| Tipo | Dettaglio |
|---|---|
| **Handoff in ingresso** | Due file devono esistere: `certificato-prodotto.json` (da WF-PROD — basta GP-3 PASS + architettura per INIZIARE, certificato pieno per CONSEGNARE) e `offerta.json` con prezzo e data validi (da LAN-PRICING, gate G4 dell'ecosistema). |
| **Comando esatto** | `/lancio-copy <lancio_id>` — lo lancia Max o Gael. |
| **Evento equivalente** | Nessun avvio automatico. |

Perché il prezzo è precondizione e non "arriva dopo": sales page, checkout, VSL e webinar
contengono lo stack di valore, l'anchoring e la CTA — **senza prezzo sono scrivibili solo a
metà**, e la metà mancante è quella che vende. Il Manuale fermo 6 mesi è la prova di cosa
succede quando il copy aspetta un prezzo che non arriva: qui il vincolo è esplicito e sta
all'ingresso, non scoperto a metà lavoro.

## 3. Input tipizzato

File atteso: `company/Ecosistemi/15-LANCI/lanci/<lancio_id>/input-copy.json`

```json
{
  "lancio_id": "string",
  "certificato_path": "string",
  "architettura_path": "string",
  "ricerca_path": "string",
  "offerta_path": "string",
  "brand_voice_path": "string | null",
  "funnel_tipo": "webinar | vsl-diretto | solo-sales-page",
  "canali_ads": ["facebook | google | youtube | linkedin | tiktok"],
  "corpus_competitor_dir": "string | null",
  "deadline_consegna": "string (ISO)"
}
```

| Campo | Tipo | Obbligatorio | Se manca |
|---|---|---|---|
| `lancio_id` | string | ✅ | **STOP exit 2** |
| `certificato_path` | string | ✅ | **STOP exit 2** — si accetta anche un certificato parziale con `GP-3: PASS` (fase F0 lo dichiara: "avvio su architettura, consegna solo a certificato pieno") |
| `architettura_path` | string | ✅ | **STOP exit 2** — senza trasformazioni non esistono bullet né promessa onesta |
| `ricerca_path` | string | ✅ | **STOP exit 2** — principio 1 della skill: *"senza dati stai tirando a indovinare"*. Questo workflow non scrive mai copy senza ricerca |
| `offerta_path` | string | ✅ | **STOP exit 2** — vedi §2. Il verbale dice esattamente: "manca offerta.json: il blocco è di LAN-PRICING (G4), non di LAN-COPY" |
| `brand_voice_path` | string\|null | ⬜ | Se `null`: si usa il TOV estratto dalla ricerca (priorità 1 della skill) + default Digital Empire, e il fatto è scritto nel manifest come `brand_voice: "default+ricerca"` |
| `funnel_tipo` | enum | ✅ | **STOP exit 2** — decide quali pezzi della lista chiusa vanno prodotti |
| `canali_ads` | array | ⬜ | Vuoto = niente copy ads; il manifest lo dichiara (LAN-TRAFFICO riceverà un handoff vuoto esplicito, non un buco) |
| `corpus_competitor_dir` | string\|null | ⬜ | Se `null`: il gate anti-plagio gira solo contro la blacklist generica e il manifest marca `anti_plagio: "parziale — corpus competitor assente"` (mai un PASS finto) |
| `deadline_consegna` | string | ✅ | **STOP exit 2** — senza data il calendario T-30 di LAN-ESECUZIONE non può agganciare i pezzi |

## 4. Precondizioni

| # | Precondizione | Verifica |
|---|---|---|
| P1 | `offerta.json`: `prezzo` è numero >0 ∧ `data_apertura` è data ISO futura ∧ nessuno dei due è una stringa vietata (`"NON LO SO"`, `"presto"`, `""`) | `python copy_intake.py --check-offerta <path>` → exit 0 |
| P2 | `ricerca.json` passa lo stesso controllo GP-2 di WF-PROD (15/5/3/3 + URL) — si riusa `verifica_ricerca.py`, non si riscrive | exit 0 |
| P3 | `architettura.json`: 100% trasformazioni compilate | `gate_architettura.py` → exit 0 |
| P4 | La skill `cro-copy-architect` è presente in `.claude/skills/` (è il motore di scrittura wrappato) | check esistenza `SKILL.md` |
| P5 | Nessun `copy/manifest.json` già presente per questo lancio (idempotenza: `--rifai` per sovrascrivere) | check filesystem |

## 5. Le fasi

**La gerarchia di scrittura — e il suo perché.** Prima si scrive il **fondamento** (grande
promessa + mappa obiezioni), poi la **sales page**, e solo dopo tutto il resto. La sales page
viene prima perché è il **documento madre**: contiene per intero l'argomentazione di vendita —
promessa, meccanismo, prove, obiezioni, offerta. Ogni altro pezzo è una **derivazione** di quel
documento: la landing opt-in è la sua promessa compressa, le VSL sono la sua versione parlata,
le email ne distribuiscono le sezioni nel tempo, gli annunci ne sono l'aggancio. Scrivere i
pezzi derivati prima della madre produce incoerenza di messaggio (message match rotto) e rework
a catena: ogni modifica alla madre a valle costa N riscritture. Con quest'ordine, costa zero.

| # | Fase | Cosa fa | Agente | Input | Output (file) | Durata | Parallelo | Umano |
|---|---|---|---|---|---|---|---|---|
| **C0** | Intake | Valida `input-copy.json`, P1-P5, congela la lista pezzi in base a `funnel_tipo` | `lan-copy-intake` | `input-copy.json` | `copy/00-intake.json` | 0,5 h | no | no |
| **C1** | Fondamenta | Produce il documento fondativo: **grande promessa unica** (fonte Webinar Milionario: *"l'unica idea che, se il pubblico la percepisce raggiungibile, rende tutte le altre obiezioni irrilevanti"*), posizionamento contro i ≥3 gap competitor, **mappa obiezioni top 10** ordinata per importanza (frequenza × intensità, dalla ricerca), TOV estratto (le 15+ frasi del target), lessico da usare e da vietare | `lan-copy-stratega` | ricerca + architettura + offerta | `copy/01-fondamenta.md` + `copy/01-obiezioni.json` | 0,5-1 g | no | **Sì, 30 min: Max approva la grande promessa.** Motivo: da quella frase discendono titolo, apertura, segreti, pitch e sales page — è la decisione a più alto effetto-leva dell'intero lancio, e costa mezz'ora contro giorni di rework. Timer: se non approvata in 48h, recap di sollecito automatico |
| **C2** | Sales page (madre) | Scrive la sales page con APSOC-L completo (§ sotto), CPB per le obiezioni, stack di valore da `offerta.json`, ≥3 varianti headline + ≥2 varianti CTA. Motore: skill `cro-copy-architect` (STEP 0-8 della skill, integralmente) | `lan-copy-salespage` | `01-fondamenta.md` + tutti gli input | `copy/10-sales-page.md` | 1-1,5 g | no | no |
| **GC-1** | → gate rubrica sulla sales page (§6) — la madre non genera figli finché non passa | `lan-copy-giudice` | — | `copy/gate/10-sales-page-score.json` | 2-3 h | — | — |
| **C3a** | Pagine funnel | Landing opt-in (APSOC compresso: A+P+Promessa+CTA) · thank you page (conferma + primo passo + seeding upsell) · copy del checkout (O+C di APSOC + micro-copy anti-attrito: garanzia, sicurezza, riepilogo stack) — il checkout monta anche l'obiezione `Checkout` dei componenti CPB (§ obiezioni) | `lan-copy-funnelpagine` | sales page approvata | `copy/20-optin.md` · `copy/21-thankyou.md` · `copy/22-checkout.md` | 0,5-1 g | **Sì** (sprint: C3a-C3e insieme — è lo "Sprint produzione" delle FASI 6-7 del Processo lanci) | no |
| **C3b** | VSL | **VSL breve 3-5 min** (per l'upsell €15: APSOC parlato compresso, dalla fonte KB_07 "declinazione VSL upsell") · **VSL evento 8-12 min** (porta all'iscrizione webinar: A+P estesi, promessa, prova, CTA unica = iscriviti). Ogni script con timecode indicativi e indicazioni di ritmo | `lan-copy-vsl` | sales page + fondamenta | `copy/30-vsl-breve.md` · `copy/31-vsl-evento.md` | 1 g | **Sì** | no |
| **C3c** | Script webinar | Applica il framework Webinar Milionario per **derivazione dalla grande promessa**: (1) **titolo** = la promessa in forma di beneficio specifico; (2) **apertura** col modello storytelling della fonte: caso reale → domanda scomoda → verità che riformula il problema; (3) **i 3 segreti** = ciascuno demolisce una macro-obiezione della mappa (le 3 più forti), riconducendo ogni segreto alla promessa; (4) **pitch** = il percorso che rende la promessa raggiungibile, con stack e Reason Now. Non quattro pezzi: quattro derivazioni della stessa frase — e il gate lo verifica | `lan-copy-webinar` | fondamenta + sales page + offerta | `copy/40-script-webinar.md` | 1 g | **Sì** | no |
| **C3d** | Le 4 sequenze email | (1) **Pre-lancio** (T-14→T-1: nurture, seeding, storia, apertura loop) · (2) **Carrello aperto** (giorno 1 → chiusura: urgenza crescente, un'obiezione demolita per email, ultima chiamata ×2) · (3) **Follow-up non acquirenti** (T+1→T+5: recupero, downsell se previsto, ritorno al nurture — regola ereditata: *il nurture non si interrompe mai, cambia la frequenza non la lista*) · (4) **Onboarding acquirenti** (T+0→T+7: consegna, primo output pratico entro 48h, richiesta testimonial al giorno 7). Struttura AIDA di sequenza + PAS per singola email (matrice della skill) | `lan-copy-email` | sales page + fondamenta + calendario date da `offerta.json` | `copy/50-seq-prelancio.md` · `copy/51-seq-carrello.md` · `copy/52-seq-followup.md` · `copy/53-seq-onboarding.md` | 1-1,5 g | **Sì** | no |
| **C3e** | Copy annunci | Per ogni canale in `canali_ads`: 3 varianti con angoli diversi (PAS base, formato per piattaforma), message match dichiarato con la pagina di destinazione (quale headline riprende quale promessa) | `lan-copy-ads` (wrappa anche skill `ad-creative`) | sales page + fondamenta | `copy/60-ads-<canale>.md` | 0,5-1 g | **Sì** | no |
| **GC-2** | → gate rubrica su OGNI pezzo di C3 (§6), in coda man mano che i pezzi escono | `lan-copy-giudice` | — | `copy/gate/<pezzo>-score.json` | 0,5 g totale | in coda allo sprint | — |
| **C4** | Coerenza trasversale | Verifica sull'intero pacchetto: message match tra step consecutivi del funnel; copertura obiezioni (le top 10 tutte gestite da qualche parte, le top 5 in sales page); **brand voice** (verdetto di `sentinel-brandvoice`, agente già ufficiale: claim senza prova, tono passivo, frasi Barnum); anti-plagio e anti-generico (§6, GC-3/GC-4); nessuna promessa presente in un pezzo e smentita in un altro | `lan-copy-giudice` + `sentinel-brandvoice` | tutti i pezzi passati | `copy/70-coerenza.json` | 0,5 g | no | no |
| **C5** | Manifest e consegna | Assembla `copy/manifest.json`: elenco pezzi, score, esiti gate, mappa obiezioni→pezzo, formato dati CPB per LAN-SITI. Verifica esistenza e dimensione minima di ogni file dichiarato | `lan-copy-bibliotecario` | tutto | `copy/manifest.json` | 2 h | no | **Sì, 30 min**: Max legge sales page e script webinar (i due pezzi che parlano al pubblico più a lungo) e dà l'ok finale di consegna. Non rivaluta la rubrica: decide se quella è la voce con cui vuole parlare |

### Il framework: APSOC-L (risoluzione del conflitto APP-SOC vs APSOC)

**Il conflitto.** La fonte storica (`KB_07_app-soc-framework.md`) scrive **APP-SOC**:
Attention · Problem · Promise · **Solution** (meccanismo unico) · **Offer** (dettaglio) ·
**Close** (Reason Now). Lo standard dell'Impero è **APSOC**: Attenzione · Problema · Promessa ·
**Social Proof** · **Obiezioni** · **CTA** — owner il CMO, sorvegliato da `guild-copy-apsoc`,
incarnato nella skill `cro-copy-architect` installata e funzionante. Non sono lo stesso
framework con due nomi: **condividono i primi 3 slot e divergono sugli ultimi 3.** APP-SOC ha
due pezzi che APSOC non nomina (meccanismo unico, dettaglio offerta); APSOC ha due pezzi che
APP-SOC lascia impliciti (prova sociale, gestione obiezioni) — e sono proprio i due più
misurabili in un gate.

**Risoluzione proposta (motivata, non lasciata in sospeso): lo standard è APSOC, esteso —
"APSOC-L" per l'area lanci.** Le sei parti:

| Parte | Cosa contiene | Come si valuta (voce di rubrica) |
|---|---|---|
| **A — Attenzione** | Headline + apertura: aggancio specifico dalla ricerca (numero, frase del target), promessa implicita, zero clickbait indimostrabile | A1 |
| **P — Problema** | Amplificazione del pain point PRIMA di ogni soluzione (l'unica regola rigida di APSOC); show don't tell: la scena, non l'aggettivo | A2 |
| **S — Promessa & Meccanismo** *(assorbe "Solution" di APP-SOC)* | La trasformazione "da [prima] a [dopo]" (presa dall'architettura di WF-PROD, non inventata) + il **meccanismo unico nominato** che la rende credibile e diversa dai ≥3 gap competitor | A3 |
| **O — Social Proof** | ≥3 prove di categorie diverse (numero, testimonianza, dimostrazione); una prova non verificabile azzera la voce | A4 |
| **C — Obiezioni** | Le top 5 della mappa, in ordine di importanza, ognuna in formato **CPB** (Claim-Proof-Benefit) | A5 |
| **+ Chiusura — Offerta & CTA** *(assorbe "Offer"+"Close" di APP-SOC)* | Stack di valore esplicito (rapporto valore/prezzo ≥3×, da `offerta.json`), anchor, garanzia, **una sola azione**, Reason Now reale e verificabile | A6 |

**Perché APSOC e non APP-SOC:** (1) ADR-003 — APSOC è già installato come skill funzionante con
5 reference file e checklist: si avvolge, non si riscrive; (2) ha già owner (CMO) e guild di
sorveglianza — APP-SOC non ha nessuno dei due; (3) Social Proof e Obiezioni espliciti sono
gate-abili con numeri, "Close" no. **Perché "esteso" e non "puro":** la direttiva *niente si
scarta* — i due slot forti di APP-SOC (meccanismo, dettaglio offerta) sono troppo preziosi per
perderli e diventano contenuto obbligatorio di A3 e A6. **Ratifica:** la decisione formale
spetta al CMO (L3 §4.2); questa è la proposta operativa, reversibile a costo quasi zero (si
spostano due voci di rubrica, non si riscrive il sistema), e il workflow **non resta bloccato**
in attesa della ratifica.

### Le obiezioni: dove nascono, come entrano, cosa si riusa

1. **Nascono dalla ricerca**: `ricerca.json` porta le obiezioni reali (frasi con URL); C1 le
   ordina per importanza (frequenza × intensità) in `copy/01-obiezioni.json`.
2. **Entrano nel copy** così: top 5 → sezione Obiezioni della sales page in CPB · le 3 più
   forti → i 3 segreti del webinar (un segreto = una macro-obiezione demolita) · una per email
   nella sequenza carrello · obiezione "prezzo" → checkout · **regola 9 della skill**: ogni
   frase di qualunque pezzo che genera un dubbio nuovo lo gestisce subito dopo o si riscrive.
3. **Si riusano i 4 componenti già in codice** — `ObjectionCPB_Checkout`, `ObjectionCPB_Time`,
   `ObjectionCPB_Website`, `ObjectionCPB_WordOfMouth` (in `Lancio corso skill beast/Leanding
   Page CCM/`, ~30 componenti Next.js): LAN-COPY **non scrive HTML** — consegna il contenuto di
   ogni obiezione in `copy/obiezioni-cpb.json`, tipizzato sulle props dei componenti
   (`{"componente": "ObjectionCPB_Time", "claim": "...", "proof": "...", "benefit": "..."}`),
   e LAN-SITI li monta. Se un'obiezione top 5 non ha componente corrispondente, il manifest lo
   dichiara e LAN-SITI decide se estendere la libreria (loro area, non nostra).

### La brand voice: chi la possiede, come si verifica

- **Owner: il CMO** (agente `cmo-empire`), come per tutto lo standard copy dell'Impero. Il file
  canonico di brand voice per i lanci oggi **non esiste come percorso verificato** — il campo
  `brand_voice_path` dell'input resta nullable finché il CMO non lo pubblica (→ SEGNALAZIONI).
- **Ordine di priorità** (dalla skill, si eredita tale e quale): 1° il TOV del target dalla
  ricerca · 2° le brand guidelines · 3° il default Digital Empire ("professionale ma
  accessibile, dati non fuffa, diretto, empatico non servile").
- **Verifica in due punti**: voce E2 della rubrica (giudizio ancorato) + verdetto
  dell'agente ufficiale **`sentinel-brandvoice`** in fase C4 (claim senza prova, tono passivo,
  frasi Barnum) — si usa l'organo che esiste, non se ne crea un secondo (ADR-003). Un verdetto
  "grave" di sentinel azzera E2 e blocca il pezzo a prescindere dal totale.

## 6. I gate

### GC-1 / GC-2 — Il gate di copy: RUBRICA COPY-LANCI v1, 100 punti, soglia ≥80

Il "copy ≥80/100" smette di essere una stretta di mano: **100 punti distribuiti su 6 blocchi e
17 voci, ognuna con peso e ancore di punteggio.** La valuta `lan-copy-giudice` (mai chi ha
scritto il pezzo) con `punteggio_copy.py`: **~60 punti sono calcolabili o verificabili a
macchina** (conteggi, presenze, blacklist), il resto è giudizio ancorato con motivazione
scritta obbligatoria per ogni voce sotto il massimo.

**Blocco A — Struttura APSOC-L (30 punti, 5 per sezione).** Ancore comuni: 5 = criterio pieno ·
3 = presente ma debole · 0 = assente o fuori posto.

| Voce | Peso | Criterio |
|---|---:|---|
| A1 Attenzione | 5 | Headline con elemento specifico della ricerca (numero o frase target); promessa implicita chiara; zero claim indimostrabili in apertura |
| A2 Problema | 5 | Pain point preso dalla ricerca (citabile); scena mostrata, non aggettivo dichiarato; **regola rigida: se la soluzione appare prima del problema → A2 = 0** |
| A3 Promessa & Meccanismo | 5 | Trasformazione "da→a" coerente con l'architettura del prodotto (non inventata) + meccanismo unico nominato e distintivo rispetto ai gap competitor |
| A4 Social Proof | 5 | ≥3 prove di ≥2 categorie diverse; **una sola prova non verificabile → A4 = 0** (Mandato Art. 2) |
| A5 Obiezioni | 5 | Top 5 della mappa, in ordine di importanza, ognuna CPB completo |
| A6 Offerta & CTA | 5 | Stack esplicito con rapporto valore/prezzo ≥3×; una sola azione; Reason Now reale (una scadenza vera, non "affrettati") |

**Blocco B — Aderenza alla ricerca (20 punti).**

| Voce | Peso | Criterio (automatico) |
|---|---:|---|
| B1 Frasi del target | 8 | ≥10 frasi della ricerca usate (verbatim o parafrasi stretta, similarità ≥0,8) → 8 · 6-9 → 4 · <6 → 0 |
| B2 Pain point coperti | 6 | 5/5 → 6 · 4/5 → 3 · ≤3/5 → 0 |
| B3 Gap competitor usati | 6 | ≥3 gap trasformati in argomenti di differenziazione → 6 · 2 → 3 · ≤1 → 0 |

**Blocco C — Gestione obiezioni (15 punti).**

| Voce | Peso | Criterio |
|---|---:|---|
| C1 CPB completi | 9 | 5/5 obiezioni top con Claim+Proof+Benefit → 9; −2 per obiezione mancante o CPB monco (min 0) |
| C2 Obiezioni generate non gestite | 6 | Rilettura integrale (STEP 7 della skill): zero → 6 · una → 3 · ≥2 → 0 |

**Blocco D — Specificità e prova (15 punti).**

| Voce | Peso | Criterio |
|---|---:|---|
| D1 Claim con prova | 6 | 100% dei claim provati o riformulati → 6 · 1 claim nudo → 3 · ≥2 → 0 |
| D2 Densità di specificità | 5 | ≥5 numeri concreti / 1.000 parole → 5 · 3-4 → 3 · <3 → 0 (automatico) |
| **D3 Promesse indimostrabili — VOCE KILLER** | 4 | Zero → 4. **Una sola promessa indimostrabile → D3 = 0 E il pezzo è BOCCIATO a prescindere dal totale.** ("Risultati garantiti" a 96/100 resta bocciato) |

**Blocco E — Voce e anti-generico (10 punti).**

| Voce | Peso | Criterio |
|---|---:|---|
| E1 Test di sostituzione | 5 | Sostituisci brand/prodotto col competitor principale: il testo deve **rompersi** (riferimenti a meccanismo, dati, storia che il competitor non può dire). Si rompe in ≥5 punti → 5 · 2-4 → 3 · ≤1 → 0. **È il test anti-"copy che potrebbe essere di chiunque"** |
| E2 Brand voice | 5 | Verdetto `sentinel-brandvoice` + lessico di `01-fondamenta.md`: zero violazioni → 5 · 1-2 minori → 3 · ≥1 grave (claim senza prova, tono passivo, frase Barnum) → 0 e blocco |

**Blocco F — Meccanica di conversione (10 punti).**

| Voce | Peso | Criterio |
|---|---:|---|
| F1 Una sola azione | 4 | Binario: CTA multiple = stessa azione con framing diverso → 4; azioni diverse nello stesso pezzo → 0 |
| F2 Message match | 3 | La headline riprende la promessa dello step precedente del funnel (dichiarato nel pezzo: "arriva da X") → 3/0 |
| F3 Dotazione test | 3 | ≥3 varianti headline + ≥2 varianti CTA + ≥2 proposte A/B con ipotesi e metrica → 3 · parziale → 1 · assente → 0 (automatico) |

**Regole di soglia:**

1. **PASS = totale ≥80/100** ∧ **nessun blocco sotto il 50% dei suoi punti** (A ≥15, B ≥10,
   C ≥8, D ≥8, E ≥5, F ≥5). Un 82 con le obiezioni a zero non è un copy da 82: è un copy rotto
   con buona grafia — il vincolo per blocco lo intercetta.
2. **D3 è killer**: azzera il PASS da solo.
3. Verdetto "grave" di `sentinel-brandvoice` = blocco a prescindere.
4. Ogni voce sotto il massimo ha **motivazione scritta** nel file score: il rework lavora su
   voci nominate, non su "migliorala un po'".
5. Se BLOCCA: il pezzo torna al suo autore con lo score file; **max 2 giri di rework**, al
   terzo esito <80 → escalation al CMO (`cmo-empire`) con verbale delle 3 voci più basse.
6. Come si sblocca: nuovo giro del giudice sul pezzo rivisto — si rivalutano tutte le voci,
   non solo quelle bocciate (un fix può rompere altro).

### GC-3 — Anti-plagio (binario)

| Campo | Valore |
|---|---|
| Dove | In C4, su ogni pezzo, prima della consegna |
| Criterio | **Zero shingle di 8 parole consecutive in comune** con il corpus competitor (le pagine raccolte dal WF Intelligence in `corpus_competitor_dir`). ≥1 shingle coincidente → BLOCK del pezzo |
| Chi | `lan-copy-giudice` via `anti_plagio.py` (automatico) |
| Se BLOCCA | Il verbale elenca i passaggi coincidenti con la fonte; riscrittura obbligatoria dei soli passaggi; ri-check integrale del pezzo |
| Se il corpus manca | Il gate NON dichiara PASS: dichiara `parziale — corpus assente` nel manifest (verità, mai PASS finto) |

### GC-4 — Anti-generico (già dentro la rubrica, con enforcement automatico)

Tre presìdi, due automatici e uno di giudizio: (1) **blacklist frasi generiche/Barnum**
(`scripts/blacklist-frasi.txt`, seed iniziale ~50 frasi tipo "porta il tuo business al livello
successivo", proprietà `guild-copy-apsoc`): >2 occorrenze per 1.000 parole → −5 su E1
automatico; (2) **B1**: senza ≥10 frasi vere del target il pezzo non arriva a 80; (3) **E1
test di sostituzione**: il giudizio finale. Un copy che potrebbe essere di chiunque non passa
da tre porte diverse.

### GC-5 — Gate di derivazione webinar (binario)

| Campo | Valore |
|---|---|
| Dove | Su `40-script-webinar.md`, insieme a GC-2 |
| Criterio | 4/4 derivazioni verificate: titolo, apertura, ciascun segreto e pitch **citano o parafrasano la grande promessa approvata** (similarità ≥0,7 con la frase di `01-fondamenta.md`) ∧ ogni segreto dichiara quale macro-obiezione demolisce (campo esplicito nello script) |
| Chi | `lan-copy-giudice` via `deriva_webinar.py` |
| Se BLOCCA | Il pezzo non è "un webinar scritto male": è un webinar **staccato dalla promessa** — torna a C3c con l'elenco delle derivazioni mancanti |
| Sblocco | Ri-derivazione e ri-check dei 4 punti |

## 7. Output tipizzato

File: `company/Ecosistemi/15-LANCI/lanci/<lancio_id>/copy/manifest.json`

```json
{
  "lancio_id": "string",
  "grande_promessa": "string (la frase approvata da Max)",
  "framework": "APSOC-L v1",
  "pezzi": [
    {
      "id": "10-sales-page",
      "file": "copy/10-sales-page.md",
      "score": 87,
      "score_file": "copy/gate/10-sales-page-score.json",
      "gate": {"rubrica": "PASS", "anti_plagio": "PASS | parziale", "derivazione": "n/a"},
      "varianti": {"headline": 3, "cta": 2, "ab_test": 2},
      "autore": "lan-copy-salespage",
      "giudice": "lan-copy-giudice",
      "giri_rework": 1
    }
  ],
  "obiezioni": {
    "mappa": "copy/01-obiezioni.json",
    "cpb_componenti": "copy/obiezioni-cpb.json",
    "copertura_top10": "10/10",
    "non_mappate_a_componente": ["string"]
  },
  "brand_voice": "file | default+ricerca",
  "coerenza": "copy/70-coerenza.json",
  "ok_umano": {"chi": "Max", "data": "ISO", "pezzi_letti": ["10-sales-page", "40-script-webinar"]},
  "consegnato_a": ["LAN-SITI", "LAN-TRAFFICO", "LAN-ESECUZIONE"]
}
```

File prodotti (lista chiusa, tutti sotto `lanci/<lancio_id>/copy/`): `00-intake.json` ·
`01-fondamenta.md` · `01-obiezioni.json` · `10-sales-page.md` · `20-optin.md` ·
`21-thankyou.md` · `22-checkout.md` · `30-vsl-breve.md` · `31-vsl-evento.md` ·
`40-script-webinar.md` · `50-seq-prelancio.md` · `51-seq-carrello.md` · `52-seq-followup.md` ·
`53-seq-onboarding.md` · `60-ads-<canale>.md` (uno per canale) · `obiezioni-cpb.json` ·
`70-coerenza.json` · `gate/<pezzo>-score.json` (uno per pezzo) · `manifest.json`.

## 8. Handoff in uscita

| A chi | Cosa | Criterio di accettazione (lo verifica chi riceve) |
|---|---|---|
| **LAN-SITI** | Copy di tutte le pagine (`10`, `20`, `21`, `22`, `31` per la pagina evento) + `obiezioni-cpb.json` tipizzato sulle props dei componenti `ObjectionCPB_*` | Manifest con score ≥80 su ogni pezzo pagina; `obiezioni-cpb.json` con schema valido — un CPB monco viene respinto, non montato |
| **LAN-TRAFFICO** | `60-ads-*.md` + `30-vsl-breve.md` + il message match dichiarato (quale annuncio → quale pagina) | 3 varianti per canale; message match presente per ogni annuncio; se `canali_ads` era vuoto, handoff vuoto **esplicito** nel manifest |
| **LAN-ESECUZIONE** | Le 4 sequenze email (`50-53`) + `40-script-webinar.md`, agganciati alle date di `offerta.json` | Ogni email con giorno relativo (T-x/T+x) e subject in 3 varianti; il calendario T-30→T+7 deve poter piazzare ogni pezzo senza chiedere nulla |
| **10-MEMORY** | Checkpoint + pattern (es. voci di rubrica sistematicamente basse → segnale di formazione) | ADR-002 |

## 9. Fallimenti

| Modo di fallimento | Sintomo | Cosa fa il sistema |
|---|---|---|
| **Un agente dichiara fatto senza averlo fatto** | Il manifest elenca un pezzo ma il file manca, è vuoto o sotto la dimensione minima del suo tipo (es. sales page <8.000 caratteri) | `assembla_copy.py` verifica esistenza + dimensione minima + presenza dello score file **per ogni pezzo**: manifest non emesso, exit 1, voce in REGISTRO-ERRORI. Un pezzo senza score file = mai giudicato = non esiste |
| Giudice = autore (violazione "chi produce non approva") | Nel manifest `autore == giudice` per un pezzo | `punteggio_copy.py` rifiuta di emettere lo score (exit 1). Il controllo è nel codice, non nella buona volontà |
| Score <80 per due giri | Terzo esito sotto soglia | Escalation automatica al CMO con le 3 voci più basse e le motivazioni scritte; il pezzo esce dallo sprint per non bloccare gli altri |
| Grande promessa non approvata | 48h senza ok di Max su C1 | Il workflow resta in C1 (nessun pezzo derivato si scrive su una promessa non approvata); recap di sollecito con timer visibile |
| Plagio rilevato | GC-3 trova shingle coincidenti | Pezzo bloccato, passaggi elencati, riscrittura mirata, ri-check integrale |
| Prezzo/data spariti o cambiati in corsa | `offerta.json` modificato dopo C0 (hash diverso) | `copy_intake.py --ricontrolla` rileva il cambio: tutti i pezzi che citano prezzo/date (sales, checkout, email carrello, webinar pitch) tornano in revisione mirata; gli altri no |
| Obiezione top 5 senza gestione | C4 trova un buco di copertura | BLOCK di consegna: la mappa obiezioni → pezzo deve essere 10/10 (top 5 in sales page) |
| Ricerca povera che rende B1 impossibile | <10 frasi utilizzabili in tutta la ricerca | Non si abbassa la soglia: handoff respinto al WF Intelligence con verbale (il difetto è dell'input, e si dichiara — mai compensare in silenzio scrivendo frasi finte) |
| Sprint sbilanciato | Un agente dello sprint C3 è a 2× la durata stimata | Recap forzato + il bibliotecario segnala quali handoff a valle slittano |

## 10. Gli eseguibili

Tutti sotto `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\15-LANCI\scripts\`.
Stessa convenzione exit code di WF-PROD (0 PASS · 1 BLOCK · 2 schema · 3 ambiente).

### `copy_intake.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `verifica_input` | `verifica_input(path: str) -> dict` | esito campo per campo; `SchemaError` → exit 2 |
| `verifica_offerta` | `verifica_offerta(offerta_path: str, vietate: tuple[str, ...] = ("NON LO SO", "presto", "")) -> bool` | `True` solo se `prezzo` float >0 ∧ `data_apertura` ISO futura ∧ nessuna stringa vietata |
| `congela_lista_pezzi` | `congela_lista_pezzi(funnel_tipo: str, canali_ads: list[str]) -> list[dict]` | la lista chiusa dei pezzi attesi per questo lancio (id, file, dimensione minima) |
| `ricontrolla` | `ricontrolla(lancio_dir: str) -> list[str]` | pezzi da rivedere se gli input a monte sono cambiati (confronto hash) |

### `punteggio_copy.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `conta_frasi_ricerca` | `conta_frasi_ricerca(testo: str, frasi: list[str], soglia_similarita: float = 0.8) -> int` | quante frasi del target sono usate (B1) |
| `densita_numeri` | `densita_numeri(testo: str) -> float` | numeri concreti per 1.000 parole (D2) |
| `frasi_generiche` | `frasi_generiche(testo: str, blacklist_path: str) -> list[str]` | occorrenze dalla blacklist (GC-4) |
| `verifica_varianti` | `verifica_varianti(testo: str) -> dict` | `{"headline": int, "cta": int, "ab_test": int}` (F3) |
| `calcola` | `calcola(pezzo_path: str, ricerca_path: str, giudizi_path: str, autore: str, giudice: str) -> dict` | lo score completo per blocco e voce (auto + giudizi ancorati); **solleva `ConflittoRuoli` se `autore == giudice`** |
| `esito` | `esito(score: dict) -> int` | 0 se totale ≥80 ∧ ogni blocco ≥50% ∧ D3 = 4 ∧ E2 senza "grave"; altrimenti 1 |

### `anti_plagio.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `shingles` | `shingles(testo: str, n: int = 8) -> set[str]` | gli n-grammi normalizzati del testo |
| `sovrapposizione` | `sovrapposizione(pezzo_path: str, corpus_dir: str, n: int = 8) -> list[dict]` | per coincidenza: `{"shingle": str, "fonte": str}`; exit 1 se ≥1 |

### `deriva_webinar.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `estrai_promessa` | `estrai_promessa(fondamenta_path: str) -> str` | la grande promessa approvata |
| `verifica_derivazione` | `verifica_derivazione(script_path: str, promessa: str, soglia: float = 0.7) -> dict` | per blocco (titolo/apertura/segreto1-3/pitch): derivato sì/no + similarità; exit 1 se <4/4 |
| `verifica_segreti_obiezioni` | `verifica_segreti_obiezioni(script_path: str, obiezioni_path: str) -> list[str]` | segreti senza macro-obiezione dichiarata |

### `assembla_copy.py`
| Funzione | Firma | Ritorna |
|---|---|---|
| `verifica_completezza` | `verifica_completezza(copy_dir: str, lista_pezzi: list[dict]) -> list[str]` | pezzi mancanti, vuoti, sotto dimensione minima o senza score file |
| `verifica_copertura_obiezioni` | `verifica_copertura_obiezioni(copy_dir: str) -> dict` | mappa obiezione → pezzo; `{"copertura": "10/10"}` o i buchi |
| `manifest` | `manifest(copy_dir: str, ok_umano: dict) -> int` | scrive `manifest.json` solo se completezza e copertura passano; exit code |

## 11. La skill e il comando

| Campo | Valore |
|---|---|
| **Skill ufficiale** | `.claude/skills/lancio-copy/SKILL.md` — nome `lancio-copy`, description con trigger ("scrivi il copy del lancio", "materiali marketing del lancio", "sales page del lancio", "/lancio-copy"). La skill **orchestra**; la scrittura resta delegata a `cro-copy-architect` (dichiarato nella description per evitare doppi trigger: `lancio-copy` per il pacchetto-lancio completo, `cro-copy-architect` per il pezzo singolo fuori lancio) |
| **Comando** | `/lancio-copy <lancio_id>` (+ `--rifai`, + `--solo <pezzo-id>` per rigenerare un pezzo singolo dentro un lancio esistente) |
| **Se manca l'input** | Stampa lo schema di `input-copy.json`, i campi mancanti e il proprietario di ciascuno (offerta → LAN-PRICING, ricerca → WF Intelligence, certificato → WF-PROD), esce con codice 2 senza scrivere nulla. Caso speciale già preparato: se manca `offerta.json` il messaggio è *"Il blocco è G4 (prezzo e data). Non è un problema di copy: è la decisione che tiene fermo il lancio."* — perché la storia del Manuale non si ripeta in silenzio |

Registrazione (ADR-008): skill + 10 agenti (`lan-copy-intake`, `lan-copy-stratega`,
`lan-copy-salespage`, `lan-copy-funnelpagine`, `lan-copy-vsl`, `lan-copy-webinar`,
`lan-copy-email`, `lan-copy-ads`, `lan-copy-giudice`, `lan-copy-bibliotecario`) in
`.claude/agents/*.md` con frontmatter minimo valido + anagrafe + wiki. `sentinel-brandvoice` e
`cmo-empire` esistono già e NON si toccano: si invocano.

## 12. Come si misura che ha funzionato

| Metrica | Target | Fonte |
|---|---|---|
| Score medio dei pezzi alla prima presentazione al giudice | ≥80 (se cala sotto per 2 lanci di fila → formazione degli agenti scrittori, non abbassamento soglia) | rubrica |
| Giri di rework medi per pezzo | ≤1,5 — massimo assoluto 2 per pezzo | regola gate |
| Frasi del target per pezzo madre | ≥10 (B1) | rubrica |
| Copertura obiezioni | 10/10 mappate, 5/5 in sales page, 3/3 nei segreti webinar | GC-2/GC-5/C4 |
| Claim indimostrabili trovati DOPO la consegna | **0** (uno solo trovato a valle = fallimento del giudice, voce in REGISTRO-ERRORI) | Mandato Art. 2 |
| Shingle di plagio a consegna | 0 | GC-3 |
| A valle, misurati da LAN-ESECUZIONE ma attribuiti al copy | opt-in bridge >35% (giallo 20-35) · iscrizione webinar da VSL >20% · CR webinar >5% · open rate ≥20% (sotto = subject line) · click ≥1% (sotto = contenuto email) | benchmark funnel + soglie diagnostiche assorbite in L2 |
| Tempo ciclo | ≤8 giorni lavorativi da C0 a manifest | proposta (dichiarata) |

---
---

## OBIEZIONI

### Contro WF-1

**1. "Nove fasi e sei gate per certificare un ebook già pronto: è la burocrazia che il pre-mortem
dice di evitare — Gael lo rifarà a mano."**
Risposta: il percorso E è esattamente la risposta a questa obiezione, ed è **3-5 giorni, non
20**: niente architettura da zero (retro-mappa), niente produzione, solo collaudo + beta +
certificato. Il confronto onesto non è "5 giorni vs 0 giorni": è **5 giorni vs i 6 mesi
misurati** che il Manuale ha già passato fermo senza processo — con un file che lo dichiarava
"Pronto" e che nessuno aveva mai collaudato (203 pagine di link mai testati in incognito). E il
comando è uno: `/lancio-prodotto manuale-claude-code`. Se dopo il primo giro reale il percorso
E supera i 5 giorni, si taglia il percorso, non il collaudo — la retro (ADR-006) esiste per
questo.

**2. "Il beta test obbligatorio col caso peggiore (prezzo ignoto → beta) ritarda il primo
lancio, che è già in ritardo di sei mesi."**
Risposta: tre cose. (a) Il beta gira **in parallelo** a WF-2: mentre 5 lettori leggono, il copy
si scrive — sul percorso critico del lancio il beta costa quasi zero, perché il collo di
bottiglia vero è la decisione prezzo/data (G4), non i tester. (b) Il caso peggiore non è zelo:
è l'unica politica coerente col Mandato Art. 2 — assumere "meno di €97" su un prezzo che
nessuno ha deciso sarebbe dichiarare verificato un numero che non esiste. (c) La via d'uscita
c'è ed è nominata: Max può firmare una deroga, che resta scritta nel certificato. La macchina
non deroga da sola; l'uomo sì, con firma. Il rischio coperto vale il costo: un refund >10% su
un prodotto mai letto da terzi brucia più dei 7 giorni di beta — e brucia la reputazione, che
non ha percorso E.

### Contro WF-2

**1. "La rubrica a 17 voci è sovra-ingegneria: un buon copywriter non scrive col pallottoliere,
e il punteggio diventerà un rito."**
Risposta: la rubrica non serve al copywriter — serve al **gate**. La legge "chi produce non
approva" impone un giudice diverso dall'autore, e un giudice senza criterio scritto produce
l'unica cosa peggiore della burocrazia: l'arbitrio ("secondo me è da 78"). I pesi rendono il
verdetto **contestabile e riproducibile**: ogni bocciatura arriva con voci nominate e
motivazioni scritte, quindi il rework è mirato invece che "migliorala un po'". E il rito è
sorvegliato dal costo: ~60 punti su 100 li calcola la macchina in secondi, il giudizio umano
ancorato copre il resto in 2-3 ore per pezzo. Se dopo 3 lanci una voce non ha mai
discriminato nulla (sempre punteggio pieno per tutti), la retro la elimina: la rubrica è
versionata (v1) apposta.

**2. "La risoluzione APSOC-L scavalca il CMO: la fonte dice che quella decisione è sua, e qui
si è deciso lo standard di copy dell'Impero in un documento di workflow."**
Risposta: non si è deciso — si è **proposto con motivazione e reso reversibile**, che è
esattamente ciò che le leggi dell'Impero chiedono ("si propone, non si decide da soli" — ma
anche: il briefing vieta di lasciare il conflitto in sospeso). La proposta sta in piedi su tre
gambe verificabili: APSOC è installato e funzionante (ADR-003: si avvolge), ha già owner e
guild (APP-SOC non ha nessuno), e i suoi slot sono gate-abili con numeri. La reversibilità è
progettata: se il CMO ratifica diversamente, cambiano **due voci di rubrica** (A3 e A6), non il
sistema — costo di inversione dichiarato e quasi nullo. L'alternativa reale all'aver proposto
era un workflow bloccato in attesa di una decisione aperta da mesi: la stessa malattia del
prezzo del Manuale, applicata al copy.

---

## SEGNALAZIONI

Cose emerse progettando, che NON faccio perché fuori dalla mia area:

1. **`26-ECOSISTEMA-LANCI.md` scrive "14-LANCI" ovunque** (titolo compreso): va aggiornato a
   15-LANCI da chi possiede il documento L3, nello stesso turno di qualunque suo prossimo
   edit (REGOLA PUNTATORI).
2. **Il file canonico di brand voice per i lanci non esiste**: il CMO deve pubblicare un
   percorso verificabile; fino ad allora `brand_voice_path` resta nullable con fallback
   dichiarato (TOV ricerca + default).
3. **Il corpus competitor per l'anti-plagio** (pagine salvate, non solo URL) va aggiunto alle
   specifiche del WF Intelligence dell'altro progettista: senza corpus, GC-3 può solo
   dichiararsi "parziale".
4. **La blacklist frasi generiche** (`scripts/blacklist-frasi.txt`, seed ~50 frasi) va
   costruita e mantenuta da `guild-copy-apsoc` — qui è solo dichiarata.
5. **I 4 componenti `ObjectionCPB_*` vanno indicizzati da LAN-SITI** (schema props verificato
   sul codice reale in `Leanding Page CCM/`): `obiezioni-cpb.json` è tipizzato su quelle props
   per contratto, ma la verifica del codice spetta a chi possiede la libreria.
6. **Il doppio ruolo del Manuale Claude Code** (Premium vs lead magnet gratuito) resta la
   decisione di Max che sblocca G4: nessuno dei due workflow può prenderla, entrambi la
   nominano.
7. **Ratifica APSOC-L**: proposta pronta per il CMO; andrebbe formalizzata in un ADR breve
   (area governance/L6, non mia).
8. **Le soglie proposte come nuove** (beta: ≥3 tester completano; copertura retro-architettura
   ≥80%; tempo ciclo E ≤5 giorni; primo-passaggio GP-4 ≥70%) sono dichiarate tali nel testo:
   alla prima retro reale vanno confermate o corrette coi numeri misurati.
