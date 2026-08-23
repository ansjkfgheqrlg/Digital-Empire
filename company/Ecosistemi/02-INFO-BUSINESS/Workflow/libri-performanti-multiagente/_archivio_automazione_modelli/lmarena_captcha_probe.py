"""
FASE 0 — Validazione captcha su profilo browser REALE (2026-08-15, PIANO-KDP libri via
Arena v3). BLOCCA tutto il resto della riscrittura: se questo test fallisce, le fasi 1-5
non vanno costruite intorno a un'ipotesi che ha gia' fallito una volta.

PERCHE' QUESTO SCRIPT ESISTE, non un'ipotesi ottimista: la scrittura via LM Arena e' gia'
stata tentata e archiviata il 2026-08-10 con questa nota lasciata nel codice
(`orchestrator.py`): "il captcha scatta dopo poche richieste e un libro ne richiede 24+".
I log reali delle uniche 3 sessioni mai girate (`sessions/debug_logs/lmarena_2026080[7,8].
jsonl`, `lmarena_20260810.jsonl`) mostrano che anche DOPO aver attivato "chat nuova per ogni
richiesta" (la difesa anti-captcha gia' in produzione), il capitolo 1 e' andato in captcha 4
volte consecutive, ogni volta risolto a mano e ripresentatosi. Il profilo usato in tutti
quei tentativi era pero' sempre un profilo Playwright DEDICATO (vuoto, creato da zero,
storico solo automatizzato) — mai il profilo REALE, gia' usato quotidianamente dalla
persona. Questa e' l'unica variabile mai isolata finora, ed e' esattamente cio' che questo
script misura: NON assume che risolva il problema, lo VERIFICA con un test piccolo e
veloce (6 invii, non un libro intero) prima di costruire altro.

COSA NON FA: non aggira il captcha se compare. Se scatta, si ferma e chiede una soluzione
umana nella finestra visibile, esattamente come il resto del codice — coerente con
`CaptchaRequired` in `lmarena_client.py`.

USO:
    python -m engine.lmarena_captcha_probe                  # Brave, Profile 9 (default)
    python -m engine.lmarena_captcha_probe --browser chrome # Chrome, Profile 8

Va lanciato fisicamente al PC (headless=False sempre: serve la finestra sia per un
eventuale captcha sia per il controllo visivo del modello attivo), come `session_manager.py`.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path

from playwright.sync_api import Page, Playwright, sync_playwright

from . import config, lmarena_client

PROBE_LOG_DIR = config.SESSIONS_DIR / "debug_logs"

# Lunghezza-capitolo reale (non i 150 ridotti del self-test archiviato): la durata/il ritmo
# di generazione potrebbero correlare col rilevamento captcha, quindi il test deve
# assomigliare al carico vero, non a una versione comoda ma non rappresentativa.
PAROLE_RICHIESTE = 1500

# Temi generici e diversi fra loro per ogni invio, cosi' nessun invio e' identico al
# precedente (evita che una eventuale euristica anti-spam scatti sulla ripetizione del
# prompt invece che sul ritmo) — non e' testo di un libro vero, questo probe misura solo
# il comportamento del sito, il contenuto non ha bisogno di avere senso narrativo.
TEMI_PROVA = [
    "a lighthouse keeper discovering an old letter",
    "two rival chefs forced to share a food truck",
    "a small-town librarian who finds a hidden room",
    "a retired detective drawn back for one last case",
    "a family reuniting after twenty years apart",
    "a musician who loses their voice before a big show",
]


class ProfiloBloccato(RuntimeError):
    """Il browser scelto risulta gia' in esecuzione: il lock del profilo e' condiviso fra
    TUTTI i Profile della stessa cartella User Data, non solo quello che si vuole usare."""


@dataclass
class ProbeResult:
    label: str
    force_new_chat: bool
    n_richiesti: int
    n_completati: int = 0
    tipo_primo_fallimento: str | None = None  # "captcha" | "sessione_invalidata" | "timeout_generico" | None
    indice_primo_fallimento: int | None = None
    recidive_captcha: int = 0
    durata_s: float = 0.0
    dettaglio_errore: str | None = None

    @property
    def pulito(self) -> bool:
        return self.tipo_primo_fallimento is None and self.n_completati == self.n_richiesti


def _browser_processes_running(image_name: str) -> list[str]:
    """Controlla via `tasklist` (nessuna dipendenza nuova: gia' disponibile su Windows,
    coerente col fatto che requirements.txt non include psutil per una cosa che il sistema
    operativo sa gia' fare)."""
    try:
        esito = subprocess.run(
            ["tasklist", "/FI", f"IMAGENAME eq {image_name}", "/FO", "CSV", "/NH"],
            capture_output=True, text=True, timeout=10,
        )
    except Exception as exc:
        print(f"[probe] impossibile controllare i processi attivi ({exc}) — procedo comunque, "
              f"un eventuale lock verra' comunque intercettato al lancio")
        return []
    righe = [r for r in esito.stdout.splitlines() if image_name.lower() in r.lower()]
    return righe


def _require_browser_closed(image_name: str, label: str) -> None:
    """Il lock di Chromium e' sull'intera cartella User Data, non sul singolo Profile:
    se il browser e' aperto su QUALSIASI profilo, il lancio sul profilo reale fallisce
    comunque. Meglio fermarsi con una causa chiara che con un timeout Playwright oscuro."""
    attivi = _browser_processes_running(image_name)
    if attivi:
        raise ProfiloBloccato(
            f"{label} risulta gia' in esecuzione ({len(attivi)} processo/i {image_name}). "
            f"Il lock del profilo e' condiviso da TUTTE le finestre/i Profile di {label}, "
            f"non solo da quello che si vuole usare qui — chiudi TUTTE le finestre di "
            f"{label} (anche su altri Profile) e rilancia."
        )


def _launch_real_profile(playwright: Playwright, browser: str) -> tuple:
    """Lancia `launch_persistent_context` DIRETTAMENTE sul profilo reale, senza passare
    dalla copia da 381MB gia' abbandonata per lentezza (CP4 2026-08-06) — non una copia,
    il profilo vivo che la persona usa ogni giorno. Ritorna (context, page)."""
    if browser == "brave":
        _require_browser_closed("brave.exe", "Brave")
        user_data_root = config.BRAVE_USER_DATA_ROOT
        profile_name = config.BRAVE_SOURCE_PROFILE_NAME
        launch_kwargs = dict(executable_path=str(config.BRAVE_EXECUTABLE_PATH))
    elif browser == "chrome":
        _require_browser_closed("chrome.exe", "Chrome")
        user_data_root = config.CHROME_USER_DATA_ROOT
        profile_name = config.CHROME_SOURCE_PROFILE_NAME
        launch_kwargs = dict(channel="chrome")
    else:
        raise ValueError(f"browser sconosciuto: {browser!r}")

    if not user_data_root.exists():
        raise FileNotFoundError(
            f"Cartella profili {browser} non trovata: {user_data_root}"
        )

    print(f"[probe] lancio {browser} sul profilo REALE '{profile_name}' "
          f"({user_data_root}) — NON una copia.")
    try:
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=str(user_data_root),
            headless=False,
            viewport=None,
            args=[*lmarena_client.ARENA_LAUNCH_ARGS, f"--profile-directory={profile_name}"],
            **launch_kwargs,
        )
    except Exception as exc:
        raise ProfiloBloccato(
            f"Impossibile lanciare {browser} sul profilo reale ({exc}). Causa piu' probabile: "
            f"{browser} e' ancora aperto da qualche parte (anche minimizzato/in background) — "
            f"chiudilo del tutto e riprova."
        ) from exc

    page = context.pages[0] if context.pages else context.new_page()
    return context, page


def _snapshot_model_label(page: Page, out_dir: Path) -> Path:
    """Screenshot + dump testuale della zona toolbar/modalita', per scoprire EMPIRICAMENTE
    se Direct seleziona davvero 'Max' come modello di default — il commento in
    `lmarena_client.py` ('Direct, oggi Max di default') non e' mai stato verificato dal
    codice, solo scritto a parole. Non si indovina un selettore per il nome modello: si
    guarda cosa c'e' davvero, come per ogni altra scoperta su questo sito."""
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = out_dir / f"captcha_probe_model_{stamp}.png"
    text_path = out_dir / f"captcha_probe_model_{stamp}.txt"
    try:
        page.screenshot(path=str(screenshot_path))
    except Exception as exc:
        print(f"[probe] screenshot fallito (non bloccante): {exc}")
    try:
        testo = page.evaluate("() => document.body.innerText") or ""
        text_path.write_text(testo, encoding="utf-8")
    except Exception as exc:
        print(f"[probe] dump testo fallito (non bloccante): {exc}")
    print(f"[probe] snapshot modello salvato: {screenshot_path.name} / {text_path.name} — "
          f"controllare a mano quale modello risulta selezionato in modalita' Direct")
    return screenshot_path


def _chapter_length_prompt(indice: int) -> str:
    tema = TEMI_PROVA[indice % len(TEMI_PROVA)]
    return (
        f"Write approximately {PAROLE_RICHIESTE} words of original short fiction about: "
        f"{tema}. Prose only, no title, no meta-commentary."
    )


def _sessione_invalidata(page: Page) -> bool:
    """Stesso controllo di `open_session`/`prepare_authenticated_direct_page`: distinto dal
    captcha testuale — e' il fallimento reale documentato in PIANO-KDP-67.md (bottone
    'Log In' ricomparso a meta' sessione), che un probe che guarda solo il captcha
    perderebbe."""
    try:
        return page.get_by_text("Log In", exact=True).count() > 0
    except Exception:
        return False


def _run_probe_batch(page: Page, label: str, n: int, force_new_chat: bool) -> ProbeResult:
    risultato = ProbeResult(label=label, force_new_chat=force_new_chat, n_richiesti=n)
    inizio = time.time()
    print(f"\n=== Sotto-test {label} — {n} invii, force_new_chat={force_new_chat} ===")

    for i in range(n):
        print(f"[probe:{label}] invio {i + 1}/{n}...")
        if _sessione_invalidata(page):
            risultato.tipo_primo_fallimento = "sessione_invalidata"
            risultato.indice_primo_fallimento = i
            risultato.dettaglio_errore = "bottone 'Log In' ricomparso prima dell'invio"
            break
        try:
            lmarena_client.send_text_prompt(
                page, _chapter_length_prompt(i), timeout_s=600, force_new_chat=force_new_chat,
            )
            risultato.n_completati += 1
            print(f"[probe:{label}] invio {i + 1}/{n}: OK")
        except lmarena_client.CaptchaRequired as exc:
            if risultato.tipo_primo_fallimento is None:
                risultato.tipo_primo_fallimento = "captcha"
                risultato.indice_primo_fallimento = i
                risultato.dettaglio_errore = str(exc)
            else:
                risultato.recidive_captcha += 1
            print(f"[probe:{label}] invio {i + 1}/{n}: CAPTCHA non risolto entro il timeout — interrompo il batch")
            break
        except (TimeoutError, RuntimeError) as exc:
            risultato.tipo_primo_fallimento = "timeout_generico"
            risultato.indice_primo_fallimento = i
            risultato.dettaglio_errore = str(exc)
            print(f"[probe:{label}] invio {i + 1}/{n}: fallito ({exc}) — interrompo il batch")
            break

    risultato.durata_s = round(time.time() - inizio, 1)
    return risultato


def _verdetto(risultati: list[ProbeResult]) -> str:
    totale_richiesti = sum(r.n_richiesti for r in risultati)
    totale_completati = sum(r.n_completati for r in risultati)
    primo_fallimento_precoce = any(
        r.tipo_primo_fallimento is not None and (r.indice_primo_fallimento or 0) < 2
        for r in risultati
    )
    recidive = sum(r.recidive_captcha for r in risultati)

    if primo_fallimento_precoce or recidive > 0:
        return (
            "FALLIMENTO — captcha/sessione invalidata entro le prime 2 richieste, o recidiva "
            "dopo soluzione manuale: uguale o peggiore dei run gia' falliti in passato. Il "
            "profilo reale non e' la causa del problema — NON costruire il resto della "
            "pipeline su questa ipotesi."
        )
    if totale_completati < totale_richiesti:
        return (
            f"PARZIALE — {totale_completati}/{totale_richiesti} completati, ma non tutti: "
            "segnale incoraggiante, non definitivo. Ripetere con un batch piu' ampio "
            "(~12 invii) prima di impegnarsi nella build completa."
        )
    return (
        f"PIENO — {totale_completati}/{totale_richiesti} completati, zero captcha. "
        "Procedere con le fasi 1-5, sapendo che 6 richieste non provano ancora la tenuta "
        "su un libro intero da 24+ capitoli (vedi il piano di verifica end-to-end)."
    )


def esegui_validazione(browser: str = "brave") -> dict:
    risultati: list[ProbeResult] = []
    with sync_playwright() as p:
        context, page = _launch_real_profile(p, browser)
        try:
            print("[probe] verifico login + captcha in apertura + modalita' Direct...")
            lmarena_client.prepare_authenticated_direct_page(page, "captcha_probe")
            _snapshot_model_label(page, PROBE_LOG_DIR)

            risultato_a = _run_probe_batch(page, "A (chat nuova a ogni invio)", 3, force_new_chat=True)
            risultati.append(risultato_a)

            if risultato_a.pulito:
                risultato_b = _run_probe_batch(page, "B (stessa chat riusata)", 3, force_new_chat=False)
                risultati.append(risultato_b)
            else:
                print("\n[probe] sotto-test A NON pulito — salto B: se il profilo reale non "
                      "aiuta nemmeno con chat isolate, non ha senso bruciare altra pazienza "
                      "umana su un pattern piu' rischioso.")
        finally:
            context.close()

    verdetto = _verdetto(risultati)
    report = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "browser": browser,
        "risultati": [asdict(r) for r in risultati],
        "verdetto": verdetto,
    }
    PROBE_LOG_DIR.mkdir(parents=True, exist_ok=True)
    report_path = PROBE_LOG_DIR / f"captcha_probe_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n" + "=" * 78)
    print("VERDETTO FASE 0")
    print("=" * 78)
    for r in risultati:
        print(f"  {r.label}: {r.n_completati}/{r.n_richiesti} completati"
              f"{', fallimento=' + r.tipo_primo_fallimento if r.tipo_primo_fallimento else ''}"
              f" ({r.durata_s:.0f}s)")
    print(f"\n{verdetto}")
    print(f"\nReport completo: {report_path}")
    print("=" * 78)

    report["report_path"] = str(report_path)
    return report


if __name__ == "__main__":
    cli = argparse.ArgumentParser(
        description="FASE 0 — valida se un profilo browser REALE evita il captcha di LM "
                     "Arena su invii sequenziali, prima di costruire il resto della "
                     "pipeline di scrittura. Va lanciato fisicamente al PC.",
    )
    cli.add_argument("--browser", choices=["brave", "chrome"], default="brave",
                     help="quale profilo reale usare (default: brave, Profile 9)")
    args = cli.parse_args()

    try:
        report = esegui_validazione(args.browser)
    except ProfiloBloccato as e:
        print(f"\n[probe] BLOCCATO: {e}")
        sys.exit(2)
    except (lmarena_client.CaptchaRequired, RuntimeError) as e:
        print(f"\n[probe] Errore prima di poter completare la validazione: {e}")
        sys.exit(1)

    sys.exit(0 if "PIENO" in report["verdetto"] else 1)
