# Runbook operativo MB-OS

## 0. Bonifica e setup una tantum

1. Ruotare le password storicamente presenti nel repository (Instagram, Google/Drive, LinkedIn e ogni account che riusava la stessa password).
2. Attivare 2FA su account social e Meta.
3. Creare/configurare Meta Business app come in `02-AUTHORIZATION-META.md`.
4. Preparare un host/mirror HTTPS pubblico per i media.

## 1. Setup locale

```bash
cd "Page IG - Mentalità Brutale/OPERATING-SYSTEM"
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r runtime/requirements.txt
cp .env.example .env
python runtime/scripts/mbctl.py init
python runtime/scripts/mbctl.py doctor
```

Compilare `.env` sul PC owner. Il file è ignorato da Git.

## 2. Autorizzazione

```bash
python runtime/scripts/mbctl.py auth-url
# aprire l'URL, autorizzare, copiare il parametro code
python runtime/scripts/mbctl.py exchange-code --code "..." --write-dotenv
python runtime/scripts/mbctl.py doctor --online
```

Se si genera un token long-lived direttamente dal Dashboard, inserirlo in `.env` e usare `doctor --online`.

## 3. Preparare contenuto

- Reel: MP4/MOV posseduto o licenziato.
- Carousel: render esistente → PNG; MB-OS lo converte in JPEG durante staging se Pillow è installato.
- Caption ≤2200 caratteri.
- Ogni immagine ha alt text.
- Manifest conforme agli esempi in `examples/`.
- Tutti i 5 gate hanno evidence `PASS`; rights contiene fonte/licenza.

## 4. Shadow e coda

```bash
python runtime/scripts/mbctl.py validate --manifest examples/carousel.example.json
python runtime/scripts/mbctl.py plan --manifest examples/carousel.example.json
python runtime/scripts/mbctl.py enqueue --manifest /path/content-manifest.json
python runtime/scripts/mbctl.py run-due            # dry-run, zero side effect
```

Ripetere almeno 5 volte con contenuti reali e correggere ogni failure.

## 5. Canary supervisionato

Il canary va eseguito solo dopo `doctor --online` verde e staging pubblico:

```bash
python runtime/scripts/mbctl.py set-mode --mode SUPERVISED
# MB_LIVE_PUBLISH_ENABLED=YES in .env
python runtime/scripts/mbctl.py run --manifest /path/canary.json \
  --live --confirm-publish MENTALITA_BRUTALE_LIVE
```

Verificare permalink, visual, caption e media id. Se qualcosa non torna: `pause`.

## 6. Certificazione

Creare evidence JSON:

```json
{
  "dry_runs_passed": 5,
  "token_health_pass": true,
  "sandbox_publish_pass": true,
  "postcheck_pass": true,
  "insights_pass": true,
  "security_scan_pass": true,
  "approved_by": "owner"
}
```

Poi:

```bash
python runtime/scripts/mbctl.py certify --evidence /path/evidence.json
python runtime/scripts/mbctl.py status
```

Solo ora il mode diventa `CERTIFIED_AUTO`.

## 7. Scheduler

Configurare Task Scheduler/cron per:

```bash
python /absolute/path/runtime/scripts/mbctl.py run-due --live
```

Frequenza raccomandata: ogni 5 minuti. Il job è idempotente. Non pianificare due scheduler sullo stesso DB.

## 8. Insights

```bash
python runtime/scripts/mbctl.py collect --media-id "..." --media-type REEL --content-id MB-...
python runtime/scripts/mbctl.py report --days 28
```

Programmare snapshot a +48h e +168h. Un dataset vuoto resta `null/unavailable`, non diventa zero.

## 9. Token refresh

```bash
python runtime/scripts/mbctl.py refresh-token --write-dotenv
python runtime/scripts/mbctl.py doctor --online
```

Eseguire con margine (es. ogni 30 giorni). Se fallisce, PAUSED e nuova autorizzazione.

## 10. Incidenti

```bash
python runtime/scripts/mbctl.py pause --reason "token|quality|platform|security"
python runtime/scripts/mbctl.py status
```

| Incidente | Azione |
|---|---|
| token 401/expired | PAUSED → refresh/reauth → doctor |
| rate limit | nessun retry immediato; ripianificare |
| post duplicato | PAUSED; confrontare content_hash e publication record |
| asset errato live | PAUSED; correzione manuale nell'app; incident log |
| secret committato | revoca/rotazione immediata, poi rimozione file; la sola cancellazione Git non basta |
| insight vuoto | aspettare finestra; non registrare 0 |
| quality drift | sospendere pattern e tornare al brief precedente |

## 11. Test

```bash
python -m unittest discover runtime/tests -v
python runtime/scripts/secret_scan.py
```

Nessun “PASS” live va dichiarato se è stato eseguito solo il dry-run.
