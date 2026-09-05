# EMP-YZGE — Gate meccanico sul battito (verifica_recap.py)

- **Codice di ripresa:** `EMP-YZGE`
- **Aperto:** 2026-09-05 19:02
- **Stato:** CHIUSO il 2026-09-05 19:05
- **Chi riprende:** basta dire `EMP-YZGE` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE

Dopo la 5a caduta sulla forma del recap nello stesso giorno, creato scripts/verifica_recap.py e reso obbligatorio in emperator.md 6.11 + emperator_hook.py; registrato ERR-20260905-001

---

## 2. DOVE SIAMO — cosa e' FATTO davvero

- `scripts/verifica_recap.py` creato e verificato per esecuzione (caso conforme → `OK` exit 0;
  caso rotto con 4 difetti diversi → tutti e 4 trovati con riga esatta, exit 1).
- `.claude/agents/emperator.md` §6.11 — blocco "IL CONTROLLO MECCANICO" innestato.
- `scripts/emperator_hook.py` — pointer al controllo in SVEGLIA (per-messaggio) e in
  ANCORAGGI (apertura sessione, importato da `emperator_boot.py`). Verificato che il file
  parsi (`ast.parse`) e giri (stdin reale, `emperator_boot.py` incluso).
- `company/Ispettorato/registro/REGISTRO-ERRORI.md` — voce `ERR-20260905-001` aggiunta.
- Memoria persistente aggiornata (`feedback_recap_ogni_10_minuti.md` + `MEMORY.md`).
- Checkpoint `CP-20260905-017` scritto con `mem write`.
- Commit `71a6b100`, pushato su `origin/main`.

## 3. COSA E' RIMASTO A META'

- Nulla del lavoro tecnico. **Resta aperta solo l'osservazione**: `ERR-20260905-001` in
  REGISTRO-ERRORI.md è in stato APERTO finché non si vedono N battiti reali passare dal
  controllo senza violazioni — questo non si verifica in un colpo solo, si verifica nel tempo.

## 4. IL PROSSIMO PASSO ESATTO

- Al prossimo battito vero (automatico o su comando `recap`), farlo passare da
  `printf '%s' "<battito>" | py -3 scripts/verifica_recap.py` prima di inviarlo.
- Dopo un numero ragionevole di battiti conformi consecutivi, aggiornare lo stato di
  `ERR-20260905-001` in `company/Ispettorato/registro/REGISTRO-ERRORI.md` da APERTO a CHIUSO,
  con la nota di quanti battiti verificati.

---

## 5. DECISIONI GIA' PRESE — non ridiscuterle

- Il controllo è OBBLIGATORIO per ogni battito, senza eccezioni per l'urgenza: è esattamente
  l'eccezione che ha causato le cadute precedenti.
- Non è stato aperto un ADR nuovo per generalizzare il principio (gate meccanico su regole di
  processo/stile, non solo su errori tecnici) ad altre parti dell'Impero — segnalato a Max come
  possibile passo successivo, non costruito di iniziativa: fuori dallo scope chiesto oggi.
- Non si è dichiarata chiusa la recidiva in REGISTRO-ERRORI: chiuderla subito senza aver
  osservato nemmeno un battito reale sarebbe la stessa finzione vietata da §3.

## 6. TRAPPOLE — errori gia' fatti, non rifarli

- **`ANCORAGGI` in `emperator_hook.py` sembra dead code se si guarda solo `main()`** — non lo è:
  viene importato ed emesso da `emperator_boot.py` (`eh.ANCORAGGI`) a SessionStart. Verificato
  con grep mirato prima di dichiararlo un bug: NON lo è. Non toccarlo pensando sia orfano senza
  aver prima grepp­ato i suoi usi in `scripts/`.
- **Edit su blocchi di testo lunghi in questi due file**: usare come `old_string` solo le righe
  che si vogliono davvero ancorare, mai assumere dove finisce un blocco `"""` — un tentativo di
  edit è fallito proprio per questo (assunto che la stringa SVEGLIA finisse due righe dopo,
  in realtà continuava con altri paragrafi prima della chiusura).
- **Prima di ogni push su questo repo**: `git status --porcelain` può mostrare file untracked
  di un altro lavoro in corso (oggi: `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/*`, non miei) — mai
  `git add -A`, sempre path mirati.

---

## 7. COMANDI PER RIPARTIRE

```bash
printf '%s' "<battito da controllare>" | py -3 scripts/verifica_recap.py
```

## 8. FILE TOCCATI

- `scripts/verifica_recap.py` (nuovo)
- `.claude/agents/emperator.md` (§6.11)
- `scripts/emperator_hook.py` (SVEGLIA + ANCORAGGI)
- `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260905-001)
- `company/Memory/checkpoints/CP-20260905-017.md`
- Memoria persistente: `feedback_recap_ogni_10_minuti.md`, `MEMORY.md`

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-YZGE`*
