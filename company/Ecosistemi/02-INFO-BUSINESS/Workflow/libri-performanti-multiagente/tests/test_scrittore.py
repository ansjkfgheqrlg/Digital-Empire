"""
Test dello STEP 2 (scrittura con Haiku) — i tre difetti trovati al primo giro end-to-end
del 2026-08-13. Nessuno di questi test chiama un modello: girano sempre, gratis.

Il piu' importante e' `test_mai_il_wrapper_batch`. Il wrapper `claude.CMD` non fallisce mai
in modo visibile: accetta il comando, risponde con successo, e intanto ha buttato via tutto
il prompt dopo la prima riga E l'opzione `--model haiku`. Il primo libro e' uscito sbagliato
proprio cosi', e la spesa e' andata sul modello di default invece che su Haiku. Un test che
guarda solo "il CLI risponde" non lo avrebbe mai visto.

    python -m pytest tests/test_scrittore.py -v
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import scrittore_haiku, workflow  # noqa: E402


# --------------------------------------------------------------------------- #
# 1. L'eseguibile: mai il wrapper batch
# --------------------------------------------------------------------------- #

def test_mai_il_wrapper_batch():
    """L'eseguibile scelto non deve MAI essere un .cmd/.bat: tronca i prompt multiriga."""
    try:
        exe = scrittore_haiku._eseguibile()
    except scrittore_haiku.ClaudeNonDisponibile:
        pytest.skip("CLI di Claude non installato su questa macchina")
    assert Path(exe).suffix.lower() not in (".cmd", ".bat"), (
        f"_eseguibile() ha restituito un wrapper batch ({exe}): troncherebbe i prompt "
        f"multiriga alla prima riga e perderebbe --model haiku"
    )
    assert Path(exe).exists()


def test_il_wrapper_batch_tronca_davvero(tmp_path):
    """La ragione del test sopra, dimostrata invece che dichiarata.

    Riproduce il guasto reale con una sonda su argv: stesso prompt multiriga, una volta
    attraverso un wrapper batch identico a quello di npm e una volta in diretta."""
    if sys.platform != "win32":
        pytest.skip("il guasto e' specifico di cmd.exe su Windows")

    sonda = tmp_path / "sonda.py"
    sonda.write_text(
        "import sys\n"
        "print(len(sys.argv) - 1)\n"
        "print(repr(sys.argv[1:]))\n",
        encoding="utf-8",
    )
    # Stessa struttura del claude.cmd generato da npm: rilancio con %*
    wrapper = tmp_path / "sonda.cmd"
    wrapper.write_text(
        "@ECHO off\n"
        f'python "{sonda}"   %*\n',
        encoding="utf-8",
    )

    prompt = "riga uno del prompt\n\nriga due\nTITLE: <segnaposto>"
    args = ["-p", prompt, "--model", "haiku"]

    via_wrapper = subprocess.run([str(wrapper)] + args, capture_output=True, text=True,
                                 encoding="utf-8", errors="replace")
    diretto = subprocess.run([sys.executable, str(sonda)] + args, capture_output=True,
                             text=True, encoding="utf-8", errors="replace")

    argc_wrapper = int(via_wrapper.stdout.splitlines()[0])
    argc_diretto = int(diretto.stdout.splitlines()[0])

    assert argc_diretto == 4, "in diretta devono arrivare tutti e 4 gli argomenti"
    assert argc_wrapper < argc_diretto, (
        "il wrapper batch dovrebbe perdere argomenti sul prompt multiriga; se questo test "
        "diventa verde su Windows, ricontrolla se si puo' tornare a usare claude.CMD"
    )
    # La conseguenza costosa: --model haiku non arriva affatto.
    assert "haiku" not in via_wrapper.stdout, (
        "attraverso il wrapper --model haiku non deve arrivare: e' il bug che faceva pagare "
        "il modello di default"
    )
    assert "haiku" in diretto.stdout


def test_cartella_di_lavoro_fuori_dal_repo():
    """La cwd delle chiamate non deve stare nell'albero del repo, altrimenti il CLI carica
    i CLAUDE.md risalendo e si comporta da assistente invece che da scrittore."""
    from engine import config

    neutra = scrittore_haiku._cartella_neutra().resolve()
    repo = config.WORKFLOW_DIR.resolve()
    assert not neutra.is_relative_to(repo)
    # e nemmeno dentro Digital Empire, dove vive il CLAUDE.md che ha causato il guasto
    assert not any(p.name == "Digital Empire" for p in neutra.parents)


def test_il_modello_resta_haiku():
    """Scelta vincolante di Gael: il volume regge solo col modello economico."""
    assert scrittore_haiku.MODELLO == "haiku"


# --------------------------------------------------------------------------- #
# 2. Il titolo: mai un placeholder in copertina
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("outline, atteso", [
    ("TITLE: The Quiet Hours\nACT1: ...", "The Quiet Hours"),
    ("**TITLE:** The Quiet Hours", "The Quiet Hours"),          # decorazione markdown reale
    ("# TITLE: The Quiet Hours", "The Quiet Hours"),
    ('TITLE: "The Quiet Hours"', "The Quiet Hours"),
    ("titolo del libro\ntitle: the quiet hours", "the quiet hours"),  # minuscolo
    ("  TITLE:   The Quiet Hours  ", "The Quiet Hours"),
])
def test_estrae_il_titolo_anche_se_decorato(outline, atteso):
    assert workflow.estrai_titolo(outline) == atteso


@pytest.mark.parametrize("outline", [
    "",
    "CHARACTERS: Anna, 34\nACT1: qualcosa",   # nessuna riga TITLE
    "TITLE:",                                  # riga presente ma vuota
    "TITLE senza due punti",
])
def test_nessun_titolo_e_None_non_un_placeholder(outline):
    """Deve dire 'non l'ho trovato', non restituire qualcosa di plausibile."""
    assert workflow.estrai_titolo(outline) is None


def test_libro_senza_titolo_non_viene_creato(monkeypatch, tmp_path):
    """Il caso che ha prodotto 'Untitled Small Town Romance Suspense 202608131759'.

    Se l'impianto non ha un titolo leggibile il libro NON deve nascere: meglio zero libri
    che un titolo placeholder pubblicato, che mette a rischio l'intero account KDP."""
    chiamate = []

    def finto_genera(prompt, timeout_s=None):
        chiamate.append(prompt)
        return "CHARACTERS: Anna, 34, libraia\nACT1: succede qualcosa."   # nessun TITLE

    monkeypatch.setattr(scrittore_haiku, "genera", finto_genera)

    with pytest.raises(RuntimeError, match="titolo leggibile"):
        workflow.step2_scrivi("small town romance suspense", "Untitled X", ["Un competitor"],
                              capitoli=2, parole_per_capitolo=100, tentativi_outline=2)

    assert len(chiamate) == 2, "deve riprovare prima di arrendersi"


def test_titolo_valido_al_secondo_tentativo(monkeypatch, tmp_path):
    """Un impianto malformato non deve bruciare il libro: si rigenera e si prosegue."""
    from engine import book_project

    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)

    risposte = iter([
        "CHARACTERS: Anna\nACT1: niente titolo qui",
        "**TITLE:** Silence in Cedar Hollow\nACT1: c'e' il titolo",
    ])
    monkeypatch.setattr(scrittore_haiku, "genera", lambda p, timeout_s=None: next(risposte))
    monkeypatch.setattr(
        scrittore_haiku, "scrivi_capitolo",
        lambda *a, **k: ("# Capitolo\n\n" + "parola " * 900, "riassunto del capitolo"),
    )

    progetto = workflow.step2_scrivi("small town romance suspense", "Untitled X", [],
                                     capitoli=1, parole_per_capitolo=100,
                                     tentativi_outline=3)

    assert progetto._config()["titolo"] == "Silence in Cedar Hollow"
    assert not progetto.slug.startswith("untitled")


# --------------------------------------------------------------------------- #
# 3. Il limite di spesa: un messaggio chiaro, non 24 oscuri
# --------------------------------------------------------------------------- #

def test_limite_di_spesa_riconosciuto(monkeypatch):
    """Il CLI comunica il limite come testo normale, non come errore di autenticazione."""
    class EsitoFinto:
        returncode = 1
        stdout = ("You've hit your monthly spend limit · raise it at "
                  "claude.ai/settings/usage?from=cc_cli_limit_message")
        stderr = ""

    monkeypatch.setattr(scrittore_haiku, "_eseguibile", lambda: "claude.exe")
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: EsitoFinto())

    with pytest.raises(scrittore_haiku.LimiteSpesaRaggiunto, match="limite di spesa"):
        scrittore_haiku.genera("qualsiasi prompt")
