# DIAGNOSI — Workflow pubblicazione automatica (TASK-PUBLISHER-W1)

**Data verifica:** 2026-08-27 · **Metodo:** eseguito, non letto. Ogni riga qui sotto
viene da un comando realmente lanciato su questa macchina, non da un'ipotesi.

> Regola applicata: **niente PASS finti.** Dove non ho una prova, scrivo "non verificato",
> non "funziona".

---

## 1. Cosa funziona DAVVERO oggi

| Pezzo | Stato | Prova |
|---|---|---|
| `Core/browser_manager.py` (Playwright + Chrome reale) | ✅ FUNZIONA | Chrome 151.0.7922.174 avviato, `launch_persistent_context` OK |
| `scripts/ig_carousel_publish.py` — logica carosello | ✅ FUNZIONA | `is_ready()` → `(True, '6 img OK')`, `get_imgs()` → 6, `get_cap()` → 924 char su cartella Arsenale reale |
| Navigazione reale a instagram.com | ✅ FUNZIONA | pagina caricata + screenshot in `_diagnostica/` |
| `Instagram/instagram_publisher.py` — import | ✅ importa | ma vedi §2.1: l'esito è inaffidabile |
| `LinkedIn/linkedin_publisher.py` — import | ✅ importa | mai eseguito end-to-end → **non** lo dichiaro funzionante |
| `pubblica.py` (nuovo, questa task) | ✅ FUNZIONA | vedi §4 |

## 2. Cosa è ROTTO o mai finito (verificato)

### 2.1 🔴 `Instagram/instagram_publisher.py::publish()` non può fallire
Il `try/except` finale cattura **ogni** eccezione, la stampa e ritorna `None`:
la funzione "riesce" sempre, anche se non ha pubblicato niente. Il chiamante non
ha modo di distinguere successo da fallimento. In più **non fa login**: va su
instagram.com e cerca subito "Nuovo post".
→ `pubblica.py` **non usa questo motore**. Usa `scripts/ig_carousel_publish.py`,
che restituisce un `bool` onesto.

### 2.2 🔴 `main_orchestrator.py` non parte proprio
```
IMPORT FAIL  main_orchestrator -> OpenAIError: Missing credentials.
```
Catena: `main_orchestrator` → `Core/copy_generator` → `Core/AI_Team/ai_client` che
istanzia `OpenAI(...)` **a livello di modulo** con `OPENROUTER_API_KEY`/`GROQ_API_KEY`
assenti. Muore all'import, prima di eseguire qualsiasi riga.
In più stampa `FLUSSO COMPLETATO CON SUCCESSO!` **incondizionatamente**, senza mai
guardare l'esito di `publish_ig()` (che comunque per la §2.1 non lo riporta).

### 2.3 🔴 `push_social.py` — il publisher "ufficiale" — è una simulazione
`CLAUDE.md` di questa cartella lo dichiara obbligatorio ("esegui lo script
`push_social.py`"). Eseguito davvero:
```
Pubblicazione completata con successo (SIMULATA)!
EXIT=0
```
La chiamata HTTP è **commentata** (`# response = requests.post(...)`) e il payload
non contiene nemmeno i media (`# "mediaUrls"`). Esce **0** dicendo "successo" senza
pubblicare nulla. È il PASS finto peggiore del folder: chi si fida dell'exit code
crede di aver pubblicato.

### 2.4 🔴 `TikTok/tiktok_publisher.py` non importa
`import config` (riga 10) invece di `from TikTok import config` →
`ModuleNotFoundError: No module named 'config'`. Il canale TikTok è inutilizzabile.
(Stesso pattern in `*/setup_session.py`, ma lì è innocuo: lanciati come script,
la loro cartella finisce in `sys.path[0]`.)

### 2.5 🔴 `scripts/ig_carousel_publish.py` puntava a una macchina che non esiste
```python
CAROSELLI_DIR = Path(r"C:\Users\Utente\Desktop\qui tutto\...\Nuovi")   # esiste? False
```
Il motore è buono, l'**ingresso** era morto: utente `Utente`, qui l'utente è `gdiar`.
Nessun `--auto`/`--folder`/`--list` poteva funzionare. Non l'ho toccato (ADR-003):
`pubblica.py` gli passa un path assoluto e lo bypassa.

### 2.6 🟠 `do_login()` cerca un campo che Instagram non ha più
`do_login()` riempie `input[name="username"]`. Verificato dal vivo oggi, la home
loggata-fuori espone `input[name="email"]` e `input[name="pass"]`:
```
name='email' type='text'
name='pass'  type='password'
```
Il login automatico **non è verificato** su IG 2026. Per questo `pubblica.py` non ci
si appoggia: pretende una sessione già autenticata e in mancanza **rifiuta il live**.

### 2.7 🔴 Nessuna sessione salvata, su nessun canale
`session_data/` **assente** per Instagram, TikTok, LinkedIn, Instagram_Mentalita,
Google_Drive. Nessun canale è loggato su questa macchina: è il vero blocco al live,
non il codice.

### 2.8 🔴 Password Instagram in chiaro nel repo
`Instagram/config.py` contiene `IG_PASSWORD` in chiaro, versionata in un monorepo
sincronizzato su GitHub. Stessa classe del problema chiave Brevo (B-020).
→ **B-023**, va ruotata e spostata in `.env`.

## 3. Cosa NON è stato verificato (lo dico, non lo nascondo)

- Pubblicazione **live** reale su Instagram: mai eseguita — manca la sessione e
  manca l'ok esplicito di Max. Il gate è chiuso con dry-run verificato.
- LinkedIn, TikTok, Instagram Mentalità: **zero** run end-to-end.
- Catena Google Drive (`drive_downloader.py`): non testata.
- Le catene 2-5 di `REGOLE.md` (Mentalità Brutale, Codice dei Potenti, cross-post
  LinkedIn): non implementate nel comando, dichiarate NON pronte a runtime.

---

## 4. Il comando (deliverable della task)

```bash
cd "SKILL & Agenti/Workflow pubblicazione automatica"
python pubblica.py "<cartella>"          # dry-run VERIFICATO (default, sicuro)
python pubblica.py "<cartella>" --live   # pubblica davvero
```

Prende **una cartella di output già pronta** (`slide_*.png` + `caption.txt`), deduce
il canale dal percorso, e in 4 passi dice la verità:

1. **Contenuto** — legge gli header reali dei PNG: dimensioni, aspect ratio nel range
   IG 0.80–1.91, peso ≤8MB, ≤10 slide, caption ≤2200 char, ≤30 hashtag, dedup su
   `published.json`.
2. **Canale** — pubblica solo su canali con un motore reale; gli altri li **blocca**
   dicendo perché.
3. **Sessione** — apre il **browser vero**, va su Instagram, fa uno screenshot in
   `_diagnostica/` e riporta lo stato di login. Non è una stampa: è una verifica.
4. **Esito** — exit code onesto: `0` PASS · `1` FAIL · `2` PASS PARZIALE
   (contenuto pronto, sessione mancante).

Il `--live` si **auto-rifiuta** se la sessione non è autenticata, invece di andare a
sbattere sul login.

Non riscrive nessun motore: li wrappa (ADR-003), e resta dentro questa cartella
come impone il `REGOLE.md` locale.

## 5. Per arrivare al live (unico passo mancante)

```bash
python Instagram/setup_session.py        # login manuale una tantum, salva session_data/
python pubblica.py "<cartella>"          # deve dare VERDETTO: PASS
python pubblica.py "<cartella>" --live   # solo con ok esplicito di Max
```

## 6. Aperti → BACKLOG

- **B-023** password IG in chiaro (§2.8) — ruotare + `.env`
- **B-024** `push_social.py` simulato ma dichiarato obbligatorio in `CLAUDE.md` (§2.3)
- **B-025** `main_orchestrator.py` morto all'import + successo incondizionato (§2.2)
- **B-026** `tiktok_publisher.py` import rotto (§2.4)
- **B-027** `do_login()` selettori IG obsoleti (§2.6)
