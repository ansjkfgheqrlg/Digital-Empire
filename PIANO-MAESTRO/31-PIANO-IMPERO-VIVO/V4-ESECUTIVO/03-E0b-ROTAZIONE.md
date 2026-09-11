# 03 — E0b: LA ROTAZIONE DELLE TRE CREDENZIALI ESPOSTE

> Chi: **Max** (pannelli esterni) + EMPERATOR (i tre `.env`, il gate) · Ore V3: 0,5-1 · Tetto:
> 1,5 · Dipende da: **E0.5 passo 2.8** (`scripts/gate_rotazione.py` deve esistere) · Percorsi in
> scrittura: `Outreach/Outreach Workflow/.env`, `SKILL & Agenti/Workflow pubblicazione
> automatica/.env`, `.claude/skills/workflow-pubblicazione-auto/.env` (tutti gitignorati —
> verificato), le variabili d'ambiente su Netlify (esterno), i pannelli Brevo/OpenRouter/
> Instagram/Arena (esterno) · Politica di guasto: **fail-closed per servizio** (non si passa al
> successivo finché il gate del precedente non è verde), **rollback = la chiave vecchia resta
> valida finché il gate non passa** (V2 §24 R6)
> STATO: COMPLETO (EMPERATOR, 2026-09-11)

**Cosa fa:** revoca e rigenera le tre credenziali che stanno in chiaro nella storia git di un
repository **pubblico** (`gh repo view` → PUBLIC, BACKLOG B-020): B-020 Brevo, B-021
Arena+OpenRouter, B-023 Instagram. **Toglierle dal codice non basta** — la storia resta
indicizzabile — vanno **revocate sui servizi**. Sono aperte dal 27/08 (B-021, B-023) e da prima
(B-020): ogni giorno in più è un giorno in cui chiunque legga il repo entra nell'account
Instagram dell'agenzia.

**Perché è DOPO E0.5 e non nel giorno uno (V3 §2, rilievo A-4):** V2 metteva la rotazione in E0
con un gate che «si verifica a mano e lo si dichiara» — la frase che L5/L9 vietano. Il gate
vero (`gate_rotazione.py`, il 401 sulla chiave vecchia) nasce in E0.5 2.8: mezza giornata di
attesa sulla sicurezza, zero sull'euro (E0a non aspetta E0b).

**Stato di partenza reale, misurato il 2026-09-11 — il disco è avanti rispetto a V2:**
- **B-020 è a metà, e la metà giusta.** Commit `aa20b8e6` (10/09): *«la chiave Brevo non
  raggiunge più il browser, la chiamata passa lato server»* — `netlify/functions/iscrizione.mjs`
  (102 righe + 124 di test) in `Landing Page/ccm-empire/` e in `Lancio corso skill beast/Sale
  pag/Siti CCM/icro-empire/`, `optin-form.tsx` e `page.tsx` che chiamano `/api/iscrizione`.
  **La chiave nuova non finirà più in un bundle**: va in una variabile d'ambiente su Netlify. Ciò
  che resta di B-020 è solo il gesto: revocare la vecchia, generare la nuova, metterla su Netlify.
- **B-061 (nuova, BACKLOG riga circa 405):** `ccm-webinar/index.html` chiama `api.brevo.com` dal
  browser con il segnaposto `TUA_API_KEY_BREVO` — non è una falla (nessuna chiave vera), è un
  form che non ha mai funzionato. **Non si tocca in E0b** (non è una credenziale esposta); si
  punta a `/api/iscrizione` «prima di mandare traffico a quella pagina» — riga in E0.9/E8.
- **I tre `.env` esistono e sono gitignorati** (`ls -la` + `git check-ignore`): `Outreach/Outreach
  Workflow/.env` porta 9 variabili (fra cui `OPENROUTER_API_KEY`, `GROQ_API_KEY`, `FB_ACCESS_TOKEN`,
  `GMAIL_APP_PASSWORD`), gli altri due portano `OPENROUTER_API_KEY` e `GROQ_API_KEY`. **19 file
  Python** consumano `OPENROUTER_API_KEY` (`grep -rl`, 2026-09-11) — V2 diceva «20+»: il numero
  vero è 19.
- **B-021, la chiave Groq è già morta** (401, verificato in CP-20260825-003) — resta da ruotare
  **OpenRouter** (viva) e la **password Arena**.

---

## 0. Cosa NON è bloccato da questo scaglione (ADR-028)

**Tutto**, tranne una cosa. E0a, E0.5, E0.6, E0.7, E1, E2, F3, E3.0, E3, E4 non dipendono da
E0b. Anche **E0.9** procede: il decreto del prezzo, il Payment Link, il link nei video non
toccano Brevo.

**L'unica cosa che aspetta E0b:** collegare a Brevo un form d'opt-in **vivo** (la newsletter, il
funnel di LANCI 4️⃣, B-061) — non si collega un form a una chiave che si sta per revocare.
Chi costruisce un form nel frattempo lo collega a `/api/iscrizione` (già costruito) e lo prova
con una chiave di test **dopo** E0b.

**Cosa NON fa E0b:** non ruota `GMAIL_APP_PASSWORD`, `FB_ACCESS_TOKEN` (scaduto da tempo, memoria
`project_outreach_system`), `APIFY_*`, `GOOGLE_PLACES_API_KEY` — non sono in chiaro nel repo, non
sono B-020/021/023. Se Max vuole ruotarle lo stesso, è un giro a parte con lo stesso gate.

---

## 1. Prerequisiti — verificati con un comando, non dichiarati

| # | Prerequisito | Comando | Atteso | Exit |
|---|---|---|---|---|
| P1 | Il gate esiste (E0.5 2.8) | `python scripts/gate_rotazione.py --help` | usage con `--vecchie <path>` e i tre servizi | 0 |
| P2 | I tre `.env` sono fuori da git | `git check-ignore -v "Outreach/Outreach Workflow/.env" "SKILL & Agenti/Workflow pubblicazione automatica/.env" ".claude/skills/workflow-pubblicazione-auto/.env"` | tre righe con la regola di `.gitignore` che li esclude | 0 |
| P3 | Nessuna delle tre chiavi è ancora nel codice tracciato (solo nella storia) | `git grep -c "xkeysib-" HEAD -- . ':!*.md'` · `git grep -n "IG_PASSWORD *= *\"" HEAD -- "*.py"` · `git grep -n "OPENROUTER_API_KEY *= *\"sk-" HEAD -- "*.py"` | **0** occorrenze nel codice a HEAD (la chiave Brevo vive nella funzione Netlify via `process.env`, i `config.py` leggono dall'ambiente da CP-20260909-HV8Q). Se un grep trova qualcosa, **quel file è un passo in più prima di ruotare** | 0/1 |
| P4 | La funzione Netlify legge la chiave dall'ambiente, non da un file | `grep -n "process.env" "Landing Page/ccm-empire/netlify/functions/iscrizione.mjs"` | una riga tipo `process.env.BREVO_API_KEY` — **il nome esatto della variabile si legge qui**, non si indovina | 0 |
| P5 | Il dry-run dell'outreach esiste | `grep -ln "DRY_RUN\|dry_run" "Outreach/Outreach Workflow/"*.py` | `send_ready.py`, `send_outreach_ready.py`, `send_real_b6.py` (2026-09-11) — **il flag esatto si legge in `send_ready.py` prima di lanciare** (`grep -n "DRY_RUN" send_ready.py`) | 0 |
| P6 | Max ha accesso ai quattro pannelli | gesto umano | Brevo, OpenRouter, Instagram, Arena (per B-021 password) | — |
| P7 | Le chiavi vecchie sono salvate FUORI dal repo per il gate | `test -f "$HOME/.digital-empire/vecchie-chiavi.env"` (percorso proposto, fuori da qualunque cartella git) | esiste, permessi solo utente, **mai committato, mai incollato in chat** | 0 |

---

## 2. I passi — numerati, ognuno con il comando esatto

**Ordine dei servizi — motivato dal numero di consumatori (meno consumatori = meno danno se il
passo va storto):** (A) Instagram (1 consumatore: `Instagram/config.py`) → (B) Brevo (1 consumatore
vivo: la funzione Netlify) → (C) Arena (1 consumatore: `caroselli - agency/config.py` +
`config_preventa.py` che lo importa) → (D) OpenRouter (**19 consumatori**, e uno dei 2 workflow su
6 che oggi partono, V2 §21-E0 ⚠️: si fa per ultimo, quando i tre precedenti hanno provato il
metodo).

### 2.0 — Prima di tutto: copiare le chiavi vecchie fuori dal repo (EMPERATOR, 2 min)

```
mkdir -p "$HOME/.digital-empire" && chmod 700 "$HOME/.digital-empire"
# Max incolla qui le tre/quattro chiavi VECCHIE, una per riga, nel formato KEY=valore:
#   BREVO_API_KEY_VECCHIA=..., OPENROUTER_API_KEY_VECCHIA=..., IG_PASSWORD_VECCHIA=..., ARENA_PASSWORD_VECCHIA=...
# Servono SOLO a gate_rotazione.py per verificare il 401. Si cancella il file a fine E0b (passo 2.6).
```

### 2.A — Instagram (B-023): password (Max, 5 min)

1. **Prima** del cambio: `ls "SKILL & Agenti/Workflow pubblicazione automatica/Instagram/session_data/"`
   — se c'è una sessione salvata, **cambiare la password la invalida** (BACKLOG B-023, nota
   esplicita): il login una tantum si rifà **dopo**, non prima.
2. Su instagram.com → Impostazioni → Password: nuova password. (Gesto umano.)
3. In `SKILL & Agenti/Workflow pubblicazione automatica/Instagram/.env` (o dove `config.py` la
   legge oggi — `grep -n "IG_PASSWORD" Instagram/config.py` dice il nome della variabile): il
   valore nuovo. **Mai in `config.py`.**
4. Rifare il login una tantum: `python "SKILL & Agenti/Workflow pubblicazione
   automatica/Instagram/refresh_session.py"` (il comando che `empire controllo` stesso indica:
   *«MAX: rifare login IG una volta (1 min) via refresh_session.py»* — la sessione ha **98 giorni**).
5. Gate parziale: `python scripts/gate_rotazione.py --solo instagram --vecchie
   "$HOME/.digital-empire/vecchie-chiavi.env"` → `instagram: vecchia RIFIUTATA, nuova OK` (per
   Instagram il «401» è il login che fallisce con la vecchia — la specifica di 2.8 in E0.5 lo
   gestisce come tentativo di login Playwright, non come HTTP).
   Checklist: `[ ] password cambiata` `[ ] .env aggiornato` `[ ] refresh_session ok` `[ ] gate verde`

### 2.B — Brevo (B-020): chiave API (Max, 5 min)

1. Su `app.brevo.com` → SMTP & API → **API Keys** → la chiave `xkeysib-1b440a32…` → **Delete**
   (revoca, non disattiva). Poi **Generate a new API key**, nome `netlify-iscrizione-2026-09`.
2. La chiave nuova **non va in nessun file del repo**: va su Netlify → Site → Environment
   variables → la variabile che `iscrizione.mjs` legge (P4: il nome esatto da `process.env.…`),
   per **entrambi** i siti (ccm-empire e icro-empire hanno ciascuno la propria funzione —
   `git show --stat aa20b8e6` lo mostra). Poi **Redeploy** dei due siti.
3. Gate parziale: `python scripts/gate_rotazione.py --solo brevo --vecchie …` → `brevo: vecchia
   401, nuova 200` **e** una prova reale del form: `curl -s -X POST https://<sito>/api/iscrizione
   -H "Content-Type: application/json" -d '{"email":"prova+e0b@<dominio>","nome":"gate E0b"}'`
   → risposta 200 e il contatto compare nella lista Brevo (poi si cancella a mano).
   Checklist: `[ ] vecchia revocata` `[ ] nuova su Netlify x2` `[ ] redeploy x2` `[ ] gate verde` `[ ] form provato`

### 2.C — Arena (B-021, prima metà): password (Max, 5 min)

1. Su `arena.ai` (o `lmarena`): cambio password dell'account `maxinfoproducer@gmail.com`
   (CP-20260805-007). **Attenzione:** cambiare la password invalida la sessione Playwright
   persistente usata dai caroselli (CP-20260805-013) — il login manuale si rifà dopo, con il
   processo OS indipendente (mai con Playwright collegato: è il segnale che Google rileva,
   CP-20260805-007).
2. Il valore nuovo nel `.env` accanto a `SKILL & Agenti/Workflow agency creative/caroselli -
   agency/config.py` (che dal 09/09 legge `ARENA_PASSWORD` dall'ambiente, CP-20260909-HV8Q).
3. Gate parziale: `gate_rotazione.py --solo arena` → login con la vecchia rifiutato.
   Checklist: `[ ] password cambiata` `[ ] .env aggiornato` `[ ] login manuale rifatto` `[ ] gate verde`

### 2.D — OpenRouter (B-021, seconda metà): la chiave dei 19 consumatori (Max + EMPERATOR, 10 min)

1. Su `openrouter.ai/keys`: **Delete** la chiave esposta, **Create** una nuova (nome
   `digital-empire-2026-09`, con limite di spesa mensile: è il momento giusto per metterlo).
2. EMPERATOR incolla la nuova in **tutti e tre** i `.env` (P2), riga `OPENROUTER_API_KEY=`:
   - `Outreach/Outreach Workflow/.env`
   - `SKILL & Agenti/Workflow pubblicazione automatica/.env`
   - `.claude/skills/workflow-pubblicazione-auto/.env`
   Checklist a tre caselle, una per file: `[ ] outreach` `[ ] pubblicazione` `[ ] skill pubblicazione`.
   **È il passo che V1 non aveva** (V2 §21-E0: *«e il passo "incolla la nuova in tutti e tre",
   che in V1 non c'era»*).
3. Il gate positivo, quello che mancava: il dry-run dell'outreach **dopo** la rotazione.
   ```
   cd "Outreach/Outreach Workflow"
   grep -n "DRY_RUN" send_ready.py          # come si accende il dry-run: variabile o flag
   DRY_RUN=1 python send_ready.py            # (o il flag che il grep mostra) → exit 0, zero invii
   ```
   Se il dry-run **fallisce con 401/403 su OpenRouter**, la chiave nuova non è arrivata al file
   giusto: si torna al punto 2, non si tocca la vecchia (che è già revocata al punto 1 — **per
   questo l'ordine è: nuova nei file, dry-run, POI revoca**; il punto 1 va letto così: creare
   la nuova PRIMA, revocare la vecchia DOPO il dry-run verde. Corretto qui rispetto a V2 §24 R6,
   che diceva «la vecchia resta valida finché il dry-run non passa»: è la stessa regola, scritta
   nell'ordine eseguibile).
4. Gate parziale: `gate_rotazione.py --solo openrouter` → `vecchia 401, nuova 200`.
5. **Ora anche 2.1 di E0.5 può chiudersi:** `cd "SKILL & Agenti/Workflow pubblicazione
   automatica" && python -c "import main_orchestrator"` → exit 0, e `python pubblica.py
   <flag dry-run>` → exit 0.

### 2.6 — Chiusura (EMPERATOR, 2 min)

```
python scripts/gate_rotazione.py --vecchie "$HOME/.digital-empire/vecchie-chiavi.env"   # tutti e quattro, exit 0
rm "$HOME/.digital-empire/vecchie-chiavi.env"                                          # le vecchie non servono piu'
python -m empire controllo                                                             # 5/6 atteso (V2 §21-E0)
```
In `company/Memory/BACKLOG.md`: B-020, B-021, B-023 → `✅` con la data e il codice del checkpoint.
B-061 resta ⬜ (non è E0b).

---

## 3. Il gate — comando, condizione di fallimento, exit code (L9)

```
python scripts/gate_rotazione.py --vecchie "$HOME/.digital-empire/vecchie-chiavi.env"
#   PASSA: 4 righe "vecchia RIFIUTATA / nuova OK" (instagram, brevo, arena, openrouter), exit 0
#   FALLISCE: qualunque riga "vecchia ANCORA VALIDA" (revoca non fatta) o "nuova RIFIUTATA" (chiave nel file sbagliato), exit 1

cd "Outreach/Outreach Workflow" && DRY_RUN=1 python send_ready.py        # (flag esatto da P5) exit 0, "0 invii"
cd "SKILL & Agenti/Workflow pubblicazione automatica" && python -c "import main_orchestrator"   # exit 0
python -m empire controllo | grep -c "pronti a partire"                  # la riga finale dice 5/6 (era 2/6)
git grep -c "xkeysib-\|sk-or-v1-" HEAD -- . ':!*.md'                     # 0 (nessuna chiave nuova finita nel codice per sbaglio)
```
**Condizione di chiusura:** `gate_rotazione.py` 4/4 **e** dry-run outreach exit 0 **e** import
del publisher exit 0 **e** `git grep` a zero. `controllo 5/6` è atteso ma non blocca (IG e
LinkedIn dipendono anche dal login, che è E0b per IG e un gesto separato per LinkedIn — 116 gg).

---

## 4. Politica di guasto e piano di rientro

| Guasto | Politica | Cosa si fa |
|---|---|---|
| La chiave nuova non arriva a un consumatore (dry-run 401) | **fail-closed sul servizio**: non si revoca la vecchia | si trova il file (`grep -rl OPENROUTER_API_KEY`), si incolla, si rilancia il dry-run; la vecchia resta viva fino al verde (R6) |
| La vecchia è già revocata e il dry-run fallisce | **fail-closed, danno dichiarato**: l'outreach email è fermo | riga ⚠️ in cima a STATO-EMPIRE con l'ora; si ripara il `.env` entro la giornata — è l'unico caso in cui E0b spegne un motore vivo, ed è esattamente il rischio che l'ordine «nuova prima, revoca dopo» esiste per evitare |
| Cambio password IG invalida la sessione e `refresh_session.py` fallisce | fail-open sul resto di E0b | Instagram DM resta rosso in `controllo` (lo era già: 98 gg); si riprova il login il giorno dopo; B-023 è comunque chiuso (la password esposta non vale più) |
| Netlify non ha la variabile e il form risponde 500 | fail-closed sul form | si aggiunge la variabile, redeploy, si riprova il `curl`; nel frattempo la landing mostra il form ma non iscrive — **come oggi** (B-061 dice che il webinar non ha mai iscritto nessuno) |
| Una chiave finisce per sbaglio in un file tracciato | **fail-closed**: `git grep` del gate lo becca prima del commit; H11 (E0.7) lo beccherà al pre-commit | si toglie, si ruota di nuovo quella chiave (una chiave committata anche per un minuto è bruciata) |

**Rientro globale:** nessun `git checkout` serve — E0b non tocca file tracciati (i `.env` sono
ignorati, Netlify è esterno). Il rientro è **ruotare di nuovo**.

---

## 5. Le forze — chi fa cosa, e il prompt d'ingaggio già scritto

**Nessuna forza.** Quattro gesti sui pannelli sono di Max; i tre `.env` e i comandi del gate li
lancia EMPERATOR in chat, con Max che incolla le chiavi **nella chat privata, mai in un file del
repo**. Nessuno scagnozzo tocca una chiave — è la regola 4 della memoria `credential-keeper`
applicata al contrario: solo la persona e l'agente supremo.

---

## 6. Cosa si scrive in Memory alla chiusura

- **Checkpoint:** `python scripts/checkpoint.py cp --titolo "E0b chiusa: B-020/B-021/B-023 ruotate sui servizi, gate 4/4, outreach dry-run verde" --costi "0 token, 0 EUR, <min>"` — con dentro: i quattro servizi con ora di revoca, i tre `.env` aggiornati (nomi, mai valori), l'esito del dry-run, la riga di `controllo` prima/dopo, e **B-061 lasciata aperta con la ragione**.
- **Riga per `STATO-EMPIRE.md`** in cima: `## ✅ <data> — E0b: le tre credenziali esposte non valgono più — CP-…` + «da oggi H11 (E0.7) protegge dal quarto caso».
- **BACKLOG:** B-020, B-021, B-023 → ✅.
- **ADR:** nessuna. (Decisione 3 di V2 §26 — repo resta pubblico + scanner H11 — è già un default; E0b non la riapre.)
- **I sei numeri del cruscotto, prima → dopo:** `controllo` 2/6 → **5/6** atteso · OPERATIVO invariato · tracce invariate · entrate invariate · pezzi fermi invariati · vivo% invariato — **E0b non muove nessun numero del piano: chiude un rischio**, ed è giusto che il cruscotto lo dica.
