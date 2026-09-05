# EMP-RWKX — Gate del battito: forma sorvegliata da hook Stop

- **Codice di ripresa:** `EMP-RWKX`
- **Aperto:** 2026-09-05 (sera) · **Stato:** APERTO — in osservazione per ordine di Max
- **Chi riprende:** basta dire `EMP-RWKX` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE

Il battito (recap) era uscito fuori forma **quattro volte in un giorno** nonostante la regola
scritta carattere per carattere: costruiti due livelli di controllo, il secondo dei quali
**blocca la consegna del messaggio** se la forma non torna. Max ha fermato qui: *"per ora in
realtà me li stai dando tutti giusti i recap"* — si osserva se tiene.

---

## 2. DOVE SIAMO — cosa è FATTO davvero

| Cosa | Dove | Prova eseguita |
|---|---|---|
| Validatore della forma | `scripts/verifica_recap.py` | caso conforme → exit 0; caso rotto con 4 difetti → tutti trovati, exit 1 |
| **Gate automatico (hook Stop)** | `scripts/gate_battito_hook.py` | `py -3 scripts/test_gate_battito.py` → **6/6** |
| Registrazione hook | `.claude/settings.json` → `Stop` | JSON valido, 2 hook Stop (il mio + `empire-sync.ps1`, intatto) |
| Dottrina | `emperator.md` §6.11, blocchi "IL CONTROLLO MECCANICO" e "IL GATE CHE SCATTA DA SOLO" | — |
| Promemoria per messaggio | `scripts/emperator_hook.py` (SVEGLIA + ANCORAGGI) | entrambi girano dopo le modifiche |
| Registro errori | `ERR-20260905-001` in `company/Ispettorato/registro/REGISTRO-ERRORI.md` | APERTO |
| Checkpoint | `CP-20260905-018` | — |
| Commit | `71a6b100` (livello 1) · `2ca18aa7` (livello 2) | verificati **su origin** |
| `.gitignore` | regola `**/frames-hd/*.png` | verificato: il sync successivo ha 0 PNG |

**Come funziona il gate:** a ogni fine turno legge il messaggio in uscita; se contiene un
battito fuori forma, blocca la consegna e ordina di riscriverlo. Tre protezioni: gli esempi
dentro ``` / `>` / indentati non vengono giudicati (altrimenti scrivere documentazione sul
battito si auto-bloccherebbe), anti-loop su `stop_hook_active`, qualunque errore → exit 0
silenzioso (non fa mai fallire il turno). Lo schema si importa da `verifica_recap.py`: una
sola fonte di verità.

## 3. COSA È RIMASTO A METÀ

- **Niente di tecnico.** Resta solo l'**osservazione** decisa da Max: si guarda se i battiti
  reali continuano a uscire giusti. `ERR-20260905-001` resta APERTO finché non se ne vedono
  abbastanza di conformi.
- **Il gate copre la FORMA, non il CONTENUTO.** Percentuale vera, forze contate davvero,
  potere non inventato, parole semplici: nessuna macchina li verifica, restano §3.
- `SYNC-CONFLICT.txt` alla radice: avviso **superato** (il push successivo è andato a buon
  fine, verificato). Max non ha ancora detto se lo cancello io.

## 4. IL PROSSIMO PASSO ESATTO

1. Se un battito esce storto **e il gate non lo blocca** → il gate ha un buco: riprodurre il
   caso in `scripts/test_gate_battito.py` prima di toccare il codice.
2. Se dopo un numero ragionevole di battiti conformi non ci sono cadute → aggiornare
   `ERR-20260905-001` da APERTO a CHIUSO, con il conteggio.
3. Debito trovato e non chiuso: **`empire mem write` usa ancora codici progressivi** e collide
   fra chat parallele (ha già causato la sovrascrittura di `CP-20260905-017`). `scripts/checkpoint.py`
   è già stato corretto (`fe35ab17`), `mem write` no.

---

## 5. DECISIONI GIÀ PRESE — non ridiscuterle

- **L'enforcement non passa più dalla memoria dell'agente.** Una regola che ha ceduto cinque
  volte non si ripara con una sesta riscrittura più severa: si toglie a se stessi la
  possibilità di saltarla.
- Il gate **non impone** un battito dove non serve: se il messaggio non ne contiene uno, passa.
  Sui lavori corti il battito resta rumore (§6.11).
- Non è stato aperto un ADR per generalizzare il principio ad altre regole di processo: fuori
  scope, segnalato a Max, non costruito di iniziativa.

## 6. TRAPPOLE — errori già fatti, non rifarli

- **Il daemon di sync (`empire-sync.ps1`, Stop hook) fa `git add -A` e committa da solo mentre
  lavori.** Ha già: (a) inglobato i miei file in un suo commit, (b) inglobato **259 PNG** di
  Empire Studio (vietati da ADR-013) — intercettati prima del push, `.gitignore` corretto.
  Prima di ricommittare: **verificare HEAD**, mai `git add -A`, sempre pathspec mirati.
- **Chat parallele attive sullo stesso repo** (LANCI v4). `CP-20260905-017` è stato
  sovrascritto da loro: il contenuto originale vive in `riprese/EMP-YZGE.md`.
- **`scripts/checkpoint.py` può risultare rotto per un istante** se un'altra sessione lo sta
  scrivendo: ricontrollare con `ast.parse` prima di concludere che è un bug.
- **Edit su `emperator.md` / `emperator_hook.py`:** ancorare solo le righe che si vogliono
  davvero, mai assumere dove finisce un blocco `"""`.
- Un `git commit` composito (file miei + file di altri) è stato **bloccato dal classificatore**:
  committare per pathspec, solo i propri file.

---

## 7. COMANDI PER RIPARTIRE

```bash
py -3 scripts/test_gate_battito.py                       # 6/6 = il gate è sano
printf '%s' "<battito>" | py -3 scripts/verifica_recap.py  # controllo singolo
```

## 8. FILE TOCCATI

- `scripts/gate_battito_hook.py` · `scripts/test_gate_battito.py` · `scripts/verifica_recap.py`
- `.claude/agents/emperator.md` (§6.11) · `scripts/emperator_hook.py` · `.claude/settings.json`
- `company/Ispettorato/registro/REGISTRO-ERRORI.md` · `company/Memory/checkpoints/CP-20260905-018.md`
- `company/Memory/STATO-EMPIRE.md` · `.gitignore` · `company/Memory/riprese/EMP-YZGE.md`

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-RWKX`*
