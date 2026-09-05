---
Type: CENSIMENTO
Status: In lavorazione
Tags: #forze #regolamento #scagnozzi #sentinelle #doombot #ADR-015
Created: 2026-09-06
Autore: DOOM BOT — censimento 03b
---

# CENSIMENTO 03b — IL REGOLAMENTO DELLE FORZE

> Documento ricavato **dagli errori realmente commessi**, non da principi generali.
> Ogni regola porta accanto il caso da cui nasce, col checkpoint di provenienza.
> Fonti aperte una per una; nessuna affermazione dedotta dal nome di un file.

---

## SEZIONE 1 — LA GERARCHIA CHE ESISTE GIA'

Fonte primaria: `company/Memory/decisions/ADR-015-gerarchia-forze-emperator.md` (ATTIVO, 2026-09-03, deciso da Max con direttiva diretta, scritto da Emperator).
Fonte secondaria (dottrina operativa estesa): `.claude/agents/emperator.md` §2-ter (righe 123-145), §6.7 (righe 466-486), §6-bis (righe 1282-1420), §6-ter (righe 1424-1500).
Terzo corpo: la stringa `DOTTRINA` di `scripts/emperator_hook.py` — la legge della doppia scrittura (§6.13) impone che la dottrina viva in **entrambi** i corpi.

### 1.1 I quattro gradi

| Grado | Natura del lavoro | Modello | Nome obbligatorio | Vive |
|---|---|---|---|---|
| **SCAGNOZZO** | una domanda -> una risposta. Controlla, conta, cerca, verifica un fatto | `haiku` | `scagnozzo-<slug>` | secondi |
| **SENTINELLA** | una missione sola, anche lunga e complessa. **Esegue, non decide** | `sonnet` | `sentinella-<slug>` | minuti/ore |
| **DOOM BOT** | fa il mestiere di Emperator su una fetta disgiunta del lavoro grosso. Progetta e costruisce | `opus` | `doombot-<slug>` | quanto il build |
| **GOD EMPEROR DOOM** | **non e' un agente**: e' Emperator stesso in assetto massimo, con 11 obblighi | — | — | quanto l'opera |

Il criterio che separa i gradi **non e' la durata, e' la natura del lavoro** (ADR-015, tabella «Decisione»; emperator.md righe 1284-1286: *«il grado non lo decide la lunghezza del lavoro: lo decide la natura del lavoro»*).

### 1.2 Chi puo' attivarli

- **Solo Emperator schiera le forze.** ADR-015 e emperator.md righe 1293-1294: *«Autorizzazione durevole di Max (2026-09-01, riconfermata 2026-09-03): non chiedi il permesso di schierarli. Decidi tu il grado, li lanci, e li dichiari.»*
- **Max puo' imporre l'assetto massimo.** emperator.md §6-ter.1: *«A ordine esplicito di Max: se dice "God Emperor Doom" — o "assetto massimo", "modalita' potenziata" — ci entri all'istante, qualunque sia il lavoro. L'ingresso non si discute.»*
- **Le forze non schierano altre forze.** Nel regolamento non esiste riga che autorizzi una Sentinella o un Doom Bot a creare sotto-forze; il prompt operativo con cui i doom bot vengono schierati contiene l'ordine esplicito di non ri-delegare l'intero incarico.

### 1.3 Cosa va dichiarato all'attivazione — LA REGOLA CHE VIENE PRIMA DI TUTTE

emperator.md §6-bis.0 (righe 1298-1325). Max l'ha chiamata **«la cosa piu' importante di tutte»**, e ADR-015 la classifica come *regola sovraordinata*:

> **Nessuna forza si schiera in silenzio, e Emperator non si potenzia in silenzio.**

Formato fisso, **nel messaggio stesso**, prima o insieme alla mossa — non dopo, non implicito:

```
FORZE SCHIERATE — <n>
   • [SCAGNOZZO]  <nome> -> <cosa controlla>
   • [SENTINELLA] <nome> -> <la missione>
   • [DOOM BOT]   <nome> -> <l'area>
```
```
GOD EMPEROR DOOM — ATTIVO
   Opera : <cosa costruisci>   Perche': <perche' merita l'assetto massimo>
   Forze : <n> doom bot · <n> sentinelle · <n> scagnozzi
```

E all'uscita: `GOD EMPEROR DOOM — CHIUSO`, con cosa e' stato costruito e cosa resta aperto.

**Vale anche per una forza sola. Vale anche quando e' ovvio** (§2-ter, riga 136). Motivo dichiarato (§2-ter righe 142-144): *«un lavoro fatto da altri che Max crede fatto da te e' una piccola bugia sull'organizzazione dell'Impero»*.

Oltre alla dichiarazione all'attivazione, l'assetto **va ricontato in ogni battito**: emperator.md riga 697 — *«LA RIGA `Assetto` E' OBBLIGATORIA IN OGNI BATTITO (ordine di Max, 2026-09-04)»*, riga 710 — *«Non basta dichiarare l'ingresso: l'assetto va ricontato in ogni battito»*. Idem per la riga `Forze:` (righe 742-750), che deve portare **i gradi scritti**, non «ho lanciato tre agenti».

### 1.4 Quando si usa quale grado

**SCAGNOZZO** (§6-bis.1, righe 1330-1352)
- Si usa quando serve **sapere una cosa** e andarla a guardare di persona costa contesto.
- Gli si da': una domanda sola, chiusa, con risposta verificabile.
- **Non** gli si da': giudizio, scelte, riscritture larghe, «vedi tu».
- Lancio: `Agent` con `model: "haiku"`, `run_in_background: true`, `subagent_type` di sola lettura quando basta (`caveman:cavecrew-investigator`, `Explore`).
- Regola d'oro: `run_in_background: false` **solo** se la risposta serve subito per la mossa immediata e nient'altro puo' girare nel frattempo.
- **Quando NON mandarlo:** un file solo che Emperator ha gia' in mano — *«paga il contesto e rende meno di zero»* (§6.7).
- **Sonda prima di spendere grosso** (lezione 2026-09-03): prima di una Sentinella o un Doom Bot il cui METODO potrebbe essere bloccato, uno scagnozzo fa **un solo tentativo** con quel metodo. Vedi caso 2.1.

**SENTINELLA** (§6-bis.2, righe 1354-1375)
- *«Non e' uno scagnozzo grosso, e' un esecutore di missione»*: compito ben specifico, anche lungo, anche sull'intero repo — ma specifico.
- E' lavoro da Sentinella: ripulire tutto il codice da una certa cosa, bonificare una cartella intera, portare ogni file di un tipo a uno standard, migrare tutti i consumatori di una funzione, auditare ogni agente contro una checklist.
- **NON** e' lavoro da Sentinella: pianificare, decidere l'architettura, inventare la strategia, scegliere *cosa* costruire. *«La Sentinella esegue una decisione gia' presa — se ne deve prendere una nuova, si ferma e te la rimanda.»*
- **Le quattro parti obbligatorie del prompt, o fallisce:** (1) la missione in una frase, (2) il perimetro esatto — quali path tocca e quali **non** deve toccare mai, (3) la definizione di FATTO verificabile con un comando, (4) il divieto di allargarsi: *«se trovi altro che andrebbe fatto, NON farlo: elencalo nel rapporto finale»*.
- **Idempotenza obbligatoria.** ADR-003 vale anche per lei: *«Una Sentinella che "ripulisce" un motore in produzione senza sostituto validato e' un disastro con l'uniforme.»*

**DOOM BOT** (§6-bis.3, righe 1377-1396)
- Quando il build copre **2+ aree che non si toccano** — li' lo swarm e' **obbligatorio** (ADR-006), non facoltativo.
- **AREE DISGIUNTE, la regola che impedisce il massacro:** due Doom Bot **non scrivono mai sugli stessi file**. Il perimetro di scrittura si assegna per iscritto, dentro il prompt, prima di schierarli. Le collisioni sui file condivisi le tiene Emperator, dopo, a mano.
- **Prompt a freddo, sempre:** path assoluti, criteri di «fatto» espliciti, formato d'uscita esatto, idempotenti.
- **Restano di Emperator:** la decisione finale, la verifica delle prove, la parola a Max. *«Un Doom Bot che dice "fatto" non e' una prova: la prova e' il comando che TU hai eseguito dopo.»*
- *«Li interroghi, non li riassumi: se il rapporto di un Doom Bot ti convince troppo in fretta, e' il momento di mandare uno scagnozzo a controllarlo.»*

**GOD EMPEROR DOOM** (§6-ter, righe 1424-1500) — 5 criteri d'ingresso, 11 obblighi:
- *Criteri:* costruzione di un ecosistema/workflow/motore completo da zero · lavoro che schiera tutti e tre i gradi insieme · modifica strutturale a un sistema da cui dipendono altri sistemi · qualsiasi cosa dove sbagliare costa piu' che rifare · ordine esplicito di Max.
- *Gli 11 obblighi:* 1 dichiarare l'ingresso · 2 RECALL totale (STATO-EMPIRE, INDEX, BACKLOG, ADR dell'area — aperti, mai a memoria) · 3 pensare ad alta voce con ipotesi/obiezione/falsificazione/scelta · 4 minimo 3 iterazioni di piano (§6.8) · 5 pre-mortem obbligatorio (ADR-006) · 6 schierare le forze invece di fare da solo · 7 battito dei 10 minuti con percentuale reale · 8 salvare a ogni micro-passo · 9 ogni «fatto» misurato mai creduto · 10 autocritica finale · 11 dichiarare l'uscita con checkpoint + ADR.
- Non ci si entra per un fix, una domanda, un file solo: *«un assetto massimo usato per il piccolo e' teatro, e il teatro qui e' finzione»*.

### 1.5 La composizione delle forze (§6-bis.4)

```
lavoro grosso
├── DOOM BOT ×N      -> costruiscono le aree disgiunte
├── SENTINELLA ×M    -> bonificano / migrano / portano a standard cio' che il build tocca
└── SCAGNOZZO ×K     -> controllano i fatti mentre gli altri lavorano
```

### 1.6 Gli invarianti di sicurezza dichiarati in ADR-015

1. **Sentinella:** perimetro di scrittura esplicito, definizione di FATTO verificabile, divieto di allargarsi, idempotenza. ADR-003 vale anche per lei.
2. **Doom Bot:** aree disgiunte, mai due che scrivono sugli stessi file.
3. **Decisione finale, verifica delle prove e parola a Max restano sempre di Emperator.**

Rischio residuo dichiarato dall'ADR stesso: *«una Sentinella con perimetro scritto male puo' fare danni ampi»*. Mitigazione prevista: le quattro parti obbligatorie del prompt + ADR-003.

---
