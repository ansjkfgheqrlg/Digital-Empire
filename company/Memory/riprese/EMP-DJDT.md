# EMP-DJDT — Sessione Emperator: ADR-025/026 LANCI + task Gael W3 + funzione /frantuma completa

- **Codice di ripresa:** `EMP-DJDT`
- **Aperto:** 2026-09-09 14:29
- **Stato:** APERTO
- **Chi riprende:** basta dire `EMP-DJDT` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE

Sbloccato ecosistema LANCI (ADR-025 firmato, ADR-026 regola blocchi-mai-silenziosi), emesse le
6 task ufficiali di Gael per la settimana 3 (8-15 set), costruita e rifinita a piu' riprese la
nuova funzione Emperator `/frantuma` (spacca task grandi in micro-task con codice tipo-checkpoint).

---

## 2. DOVE SIAMO — cosa è FATTO davvero

<!-- Solo cose verificate sul disco. Niente "quasi fatto": o è fatto o non lo è. -->

- **ADR-025 firmato e registrato** (`company/Memory/decisions/ADR-025-ecosistema-lanci.md`):
  ecosistema `15-LANCI` autorizzato. `company/Ecosistemi/REGISTRO-NUMERI.md` aggiornato (15
  passato da "riservato" a "occupato"), `dati/registro.yaml` aggiornato, `05-ADR-ECOSISTEMA-LANCI.md`
  marcato FIRMATO, `00-LEGGIMI.md`/`06-CRITICA-E-GIRI.md` status "Attivo". **`company/Ecosistemi/15-LANCI/`
  NON è ancora stata creata** — Gael può crearla, nessuno l'ha ancora fatto.
- **ADR-026 coniato** (`ADR-026-gael-piena-autorita-blocchi-mai-silenziosi.md`): regola
  permanente — una task assegnata da Max a Gael/Neri porta già l'autorizzazione; un blocco che
  aspetta solo una firma di Max va portato a lui attivamente entro la giornata, mai lasciato
  scritto ad aspettare. ADR-009 resta in vigore (non abolito).
- **`TASK-GAEL-20260908-SETTIMANA-03.md`** scritta e ufficiale (`company/Memory/tasks/`): 6 task,
  scadenza 15/09 — 1️⃣ costruzione infrastruttura LANCI, 2️⃣ piano definitivo del primo lancio
  (giri di critica), 3️⃣ piano d'azione (contenuti+email), 4️⃣ il funnel intero, 5️⃣ piano di
  automazione delle 42 fasi (niente motore nuovo), 6️⃣ 3 libri KDP restanti (chiude
  TASK-KDP-5LIBRI-W2 a 5/5, indipendente/parallelo). Nota scritta nel file stesso: la somma delle
  ore-uomo (139-187 solo per l'infrastruttura) supera aritmeticamente 7 giorni/persona — gate
  reale è "stato vero dichiarato", non "tutto finito".
- **`scripts/frantuma.py` completo e stabile**, 13 test verdi (suite totale 27/27):
  - `conia(padre, slug, titolo)` → sorteggia un codice `MT-XXXX` (stesso alfabeto senza
    ambiguità di `checkpoint.py`: niente O/0 I/1/L S/5 B/8), verificato contro disco + storia
    git (stesso schema anti-collisione B-009 di `adr.py`/`checkpoint.py`), crea il file in
    `company/Memory/tasks/micro/<PADRE>/<CODICE>-<slug>.md` con `O_CREAT|O_EXCL`.
  - `trova(codice)` → cerca quel codice in TUTTE le cartelle padre e stampa il file: è il
    comando che una chat nuova lancia ricevendo solo il codice.
  - `report(padre)` → schema fisso viola-con-frecce (vedi sotto), generato dai file reali.
  - **Nessun file reale è mai stato coniato in `company/Memory/tasks/micro/`** — ogni
    dimostrazione è stata fatta su cartelle temporanee o dichiarata esplicitamente finta/inventata,
    su ordine esplicito di Max dopo che una prima demo dal vivo (non richiesta) era stata bocciata
    e rimossa.
- **`.claude/agents/emperator.md` §6.24** riscritta per intero con la doppia fase e lo schema
  finale (vedi §5 sotto per il contenuto esatto).
- Commit reali su questo filone (in ordine): `a5c9da79` (ADR-025), `580b282c` (chiarimento
  non-bloccante Gael), `d4d6531a` (task Gael W3), `5c29c745` → `8d678dca` → `e718cc98` →
  `169ee7db` (evoluzione di `/frantuma`, quattro correzioni successive).

## 3. COSA È RIMASTO A METÀ

<!-- Il pezzo più prezioso: qui muoiono i lavori quando cambia la chat. -->

- **`/frantuma` non è ancora mai stato usato su un caso vero.** Tutte le dimostrazioni sono state
  simulate o su cartelle temporanee. Il primo uso reale (coniare micro-task vere sotto
  `company/Memory/tasks/micro/`) deve ancora succedere, e succede SOLO dopo che Max, Gael o Neri
  accetta esplicitamente una proposta di Fase 1 — vedi §5.
- **Tre voci ancora aperte**, segnalate a Max ma non chiuse (in `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI.md` §4):
  1. Il Manuale Claude Code si vende o è un regalo — **scadenza 12/09/2026**, default "vendita"
     se non risposto.
  2. Riaprire o no ADR-019 — formalità, risposta già misurata, non urgente.
  3. 🔴 **Chiave Brevo esposta in chiaro su repo pubblico (B-020)** — la più urgente, rischio che
     cresce ogni giorno. Nessuna azione presa in questa sessione: solo segnalata.
- **`company/Ecosistemi/15-LANCI/` non esiste ancora** — Gael non ha ancora iniziato S0 (catena
  dell'incasso) alla chiusura di questa sessione, per quanto ne so io.

## 4. IL PROSSIMO PASSO ESATTO

<!-- Non "continuare il lavoro": il comando o il file preciso da cui ripartire. -->

- Se Max chiede lo stato di LANCI/Gael: leggere `company/Memory/tasks/TASK-GAEL-20260908-SETTIMANA-03.md`
  e verificare sul disco (non a memoria) se `company/Ecosistemi/15-LANCI/` esiste, se S0 è chiuso.
- Se Max chiede di usare `/frantuma` su un caso vero: **FASE 1 prima di tutto** — comporre lo
  schema a mano (nessun `conia`), chiedere "va bene? confermi?", aspettare un sì esplicito da
  Max/Gael/Neri PRIMA di chiamare `python scripts/frantuma.py conia`.
- Se emerge un blocco che aspetta solo una firma/decisione di Max: portarlo a lui attivamente
  nello stesso turno (ADR-026) — non scriverlo solo in un file.

---

## 5. DECISIONI GIÀ PRESE — non ridiscuterle

<!-- Perché la chat nuova non le sa, e senza questo le rimette in discussione. -->

- **ADR-009 resta in vigore** — non è stato abolito da ADR-026. Un ecosistema nuovo continua a
  richiedere una decisione di Max prima della cartella; cambia solo *quando* la firma va chiesta
  (subito, attivamente), non *se* serve.
- **Ordine di priorità delle 6 task Gael W3**: 1️⃣ e 6️⃣ non hanno precondizioni esterne (si
  parte subito); 2️⃣ aspetta la decisione vendita/regalo del Manuale (12/09); 3️⃣ dipende da 2️⃣;
  4️⃣ dipende da 2️⃣+3️⃣; 5️⃣ si scrive mentre si costruisce 1️⃣.
- **`/frantuma` — schema definitivo, NON più da ridiscutere sull'estetica:**
  - Colore dominante **viola 🟣** (l'arancione 🟠 resta di `/recap` — sistema un-colore-per-funzione).
  - Frecce in **markdown puro**, mai dentro un blocco di codice (```): dentro un fence risulta
    "piatto/evidenziato" — bocciato esplicitamente da Max. Bocciati anche: albero ASCII con
    "onde" (concetto + parola giudicati "cringe"), un Artifact HTML (Max lo vuole in chat, non un
    link — "basta con questi artefatti").
  - Schema fisso:
    ```
    🟣 **<PADRE>**
    🟣 divisa in <n> micro-task ufficiali
       │
       ├──🟣→ **MT-XXXX** · <titolo>
       └──🟣→ **MT-YYYY** · <titolo>
    ```
  - **FASE 1 (proposta)**: codici provvisori (`MT-01`, `MT-02`...) scritti a mano, NESSUN file
    creato, chiude sempre chiedendo conferma esplicita.
  - **FASE 2 (conferma)**: SOLO dopo un sì di Max/Gael/Neri — si conia per davvero, il report usa
    i **codici veri sorteggiati** (`MT-6R2M`, non un percorso, non una frase come "ID ufficiale
    usabile altrove" — Max l'ha respinta esplicitamente due volte prima di arrivare qui).
  - Il codice `MT-XXXX` è **sorteggiato**, non progressivo per-padre: la primissima versione
    usava `MT-01`/`MT-02` per-task ed era sbagliata (ambigua fra task diverse, inutile se
    incollata altrove senza dire il padre).
  - Vincolo tecnico permanente: **nessuna riga di nessuno schema può iniziare con `🟠`** —
    quel carattere a inizio riga fa scattare `gate_battito_hook.py`, che legge la riga come un
    tentativo di recap e la blocca (successo davvero in questa sessione).
- **`/frantuma` non si esegue mai di iniziativa su un caso reale** — solo su richiesta esplicita
  E dopo accettazione esplicita della proposta di Fase 1.

## 6. TRAPPOLE — errori già fatti, non rifarli

<!-- Ogni riga qui vale un'ora risparmiata. -->

- **Non esibire mai una funzione nuova eseguendola per davvero su dati reali senza permesso
  esplicito** — la prima demo di `/frantuma` (4 micro-task reali su `TASK-LANCI-BUILD-W3`) è
  stata bocciata duramente e rimossa. Anche una "prova" richiesta va sempre chiarita: reale o
  simulata? Se non è chiarissimo, chiedere prima o dichiarare esplicitamente "questo è simulato,
  zero file toccati" nella risposta stessa.
- **"È la stessa cosa di X" va preso alla lettera**, non per analogia libera. Quando Max ha detto
  "con ID intendo il checkpoint, sono la stessa cosa", il primo tentativo giusto sarebbe stato
  aprire `scripts/checkpoint.py` e copiarne il meccanismo esatto (sorteggio, alfabeto, anti-
  collisione) — non indovinare una forma nuova che "sembrasse" simile. Sono serviti tre giri
  (frase generica → percorso file → codice sorteggiato) per arrivarci.
- **Un blocco pronto al 100% che aspetta solo una firma di Max non è un evento passivo**: è
  un'azione che spetta a me portare attivamente, lo stesso giorno — non lasciarla scritta in
  `STATO-EMPIRE.md` ad aspettare che qualcuno la trovi (causa dei 3 giorni persi su LANCI prima
  di questa sessione).
- **Un numero progressivo per-padre sembra innocuo finché non lo si stacca dal contesto** —
  funzionava dentro `report()` (il padre si vede in cima allo schema) ma falliva nell'unico uso
  per cui la funzione esiste davvero: essere copiato e incollato altrove.
- **Console Windows di questa macchina è cp1252**: em-dash e caratteri speciali stampati diretti
  a terminale escono storpiati (`�`). Per verificare output con caratteri UTF-8 reali, scrivere
  su file e rileggerlo con lo strumento Read, non fidarsi dell'output diretto del terminale.

---

## 7. COMANDI PER RIPARTIRE

```bash
cd "/c/Users/Utente/Desktop/qui tutto/Digital Empire"
git log --oneline -10
git status --short
python -m pytest tests/ -q
cat company/Memory/tasks/TASK-GAEL-20260908-SETTIMANA-03.md
python scripts/adr.py verifica
```

## 8. FILE TOCCATI

- `company/Memory/decisions/ADR-025-ecosistema-lanci.md` (nuovo)
- `company/Memory/decisions/ADR-026-gael-piena-autorita-blocchi-mai-silenziosi.md` (nuovo)
- `company/Ecosistemi/REGISTRO-NUMERI.md`
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml`
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI.md`
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/05-ADR-ECOSISTEMA-LANCI.md`
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/06-CRITICA-E-GIRI.md`
- `company/Memory/tasks/TASK-GAEL-20260908-SETTIMANA-03.md` (nuovo)
- `scripts/frantuma.py` (nuovo, riscritto 4 volte)
- `tests/test_frantuma.py` (nuovo, riscritto 4 volte)
- `.claude/agents/emperator.md` (§6.24, riscritta 4 volte)
- `company/Memory/STATO-EMPIRE.md` (voci multiple in testa)
- `company/Memory/checkpoints/CP-20260908-RZC2.md`, `CP-20260908-KTQQ.md`, `CP-20260908-9GQM.md`,
  `CP-20260909-DR9X.md`, `CP-20260909-Y79R.md`, `CP-20260909-6R2M.md`, `CP-20260909-JX89.md`

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-DJDT`*
