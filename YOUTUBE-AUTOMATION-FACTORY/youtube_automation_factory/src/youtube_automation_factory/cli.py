"""Interfaccia a riga di comando.

Codici di uscita: ``0`` successo, ``1`` errore d'uso o configurazione, ``2`` blocco
regolatorio o workflow non completabile.
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

import typer

from .core.enums import WorkflowState
from .core.repositories import JsonFileWorkflowRepository
from .core.workflow import ALLOWED_TRANSITIONS
from .demo import run_demo_workflow, run_side_analyses

EXIT_OK = 0
EXIT_USAGE = 1
EXIT_BLOCKED = 2

app = typer.Typer(
    add_completion=False,
    help=(
        "YouTube Automation Factory — fabbrica multi-agentica con gerarchia decisionale, "
        "controlli regolatori e report tracciabili."
    ),
)


def _settings():  # noqa: ANN202 - tipo interno di pydantic-settings
    """Carica le impostazioni, aggiungendo ``config/`` al percorso se serve."""
    try:
        from config.settings import get_settings
    except ImportError:  # pragma: no cover - dipende da come e' installato il progetto
        root = Path(__file__).resolve().parents[2]
        sys.path.insert(0, str(root))
        from config.settings import get_settings
    return get_settings()


def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )


@app.command("init-demo")
def init_demo(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Log di dettaglio."),
) -> None:
    """Crea i dati demo locali e le cartelle necessarie."""
    _setup_logging(verbose)
    settings = _settings()
    reports = settings.reports_path
    repo_dir = reports / "workflows"
    repo_dir.mkdir(parents=True, exist_ok=True)
    typer.echo(f"Nicchia primaria: {settings.primary_niche}")
    typer.echo(f"Cartella report:  {reports}")
    typer.echo(f"Cartella stati:   {repo_dir}")
    typer.echo("Dati demo pronti. Prossimo comando: `yaf run-demo`.")
    raise typer.Exit(EXIT_OK)


@app.command("run-demo")
def run_demo(
    stop_before_copy_review: bool = typer.Option(
        False,
        "--stop-before-copy-review",
        help="Si ferma prima della revisione esterna del copy, per mostrare il blocco.",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Esegue un workflow completo simulato, senza servizi esterni."""
    _setup_logging(verbose)
    settings = _settings()
    reports = settings.reports_path

    result = run_demo_workflow(
        primary_niche=settings.primary_niche,
        reports_dir=reports,
        complete=not stop_before_copy_review,
    )
    repo = JsonFileWorkflowRepository(reports / "workflows")
    repo.save(result.run)

    typer.echo(f"Workflow: {result.run.id}")
    typer.echo(f"Stato finale: {result.run.state}")
    typer.echo(f"Report generati: {len(result.reports)} in {reports}")
    for nota in result.notes:
        typer.echo(f"  nota: {nota}")
    if result.run.blocked_reasons:
        for motivo in result.run.blocked_reasons:
            typer.echo(f"  BLOCCO: {motivo}")

    if result.run.state is WorkflowState.COMPLETED:
        raise typer.Exit(EXIT_OK)
    raise typer.Exit(EXIT_BLOCKED)


@app.command("validate-workflow")
def validate_workflow(
    workflow_id: str = typer.Argument(..., help="ID del workflow salvato."),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Valida stato, transizioni e asset di un workflow salvato."""
    _setup_logging(verbose)
    settings = _settings()
    repo = JsonFileWorkflowRepository(settings.reports_path / "workflows")
    run = repo.get(workflow_id)
    if run is None:
        typer.echo(f"Workflow '{workflow_id}' non trovato.", err=True)
        typer.echo(f"Disponibili: {', '.join(repo.list_ids()) or 'nessuno'}", err=True)
        raise typer.Exit(EXIT_USAGE)

    from .agents import RegulatoryAgent

    regolatore = RegulatoryAgent("cli-regulator", settings.primary_niche)
    problemi = regolatore.audit(run)

    typer.echo(f"Workflow {run.id} — stato {run.state}")
    typer.echo(f"Eventi registrati: {len(run.events)}")
    successori = sorted(ALLOWED_TRANSITIONS.get(run.state, frozenset()))
    typer.echo(f"Transizioni ammesse da qui: {', '.join(successori) or 'nessuna'}")

    if problemi:
        typer.echo("\nNon conformita':")
        for p in problemi:
            typer.echo(f"  - {p}")
        raise typer.Exit(EXIT_BLOCKED)
    typer.echo("\nNessuna non conformita' rilevata.")
    raise typer.Exit(EXIT_OK)


@app.command("generate-report")
def generate_report(
    include_side_analyses: bool = typer.Option(
        True, "--side/--no-side", help="Include competitor, canali e proposte di nicchia."
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Genera i report Markdown eseguendo il workflow demo."""
    _setup_logging(verbose)
    settings = _settings()
    reports = settings.reports_path

    result = run_demo_workflow(primary_niche=settings.primary_niche, reports_dir=reports)
    percorsi = list(result.reports)
    if include_side_analyses:
        percorsi.extend(
            run_side_analyses(primary_niche=settings.primary_niche, reports_dir=reports)
        )

    typer.echo(f"{len(percorsi)} report generati in {reports}:")
    for p in percorsi:
        typer.echo(f"  - {p.name}")
    raise typer.Exit(EXIT_OK)


@app.command("list-states")
def list_states() -> None:
    """Mostra gli stati del workflow e le transizioni ammesse."""
    for stato in WorkflowState:
        successori = sorted(ALLOWED_TRANSITIONS.get(stato, frozenset()))
        freccia = " → " + ", ".join(successori) if successori else " (terminale)"
        typer.echo(f"{stato}{freccia}")
    raise typer.Exit(EXIT_OK)


@app.command("check-config")
def check_config() -> None:
    """Verifica la configurazione e dichiara cosa non e' pronto."""
    settings = _settings()
    righe: list[tuple[str, bool, str]] = []

    righe.append(("Nicchia primaria", True, settings.primary_niche))
    righe.append(("Cartella report", True, str(settings.reports_path)))

    try:
        import playwright  # noqa: F401

        playwright_ok, nota_pw = True, "installato"
    except ImportError:
        playwright_ok, nota_pw = False, "non installato — pip install -e '.[browser]'"
    righe.append(("Playwright", playwright_ok, nota_pw))

    righe.append(
        (
            "YouTube",
            settings.youtube_is_configured(),
            "selettori configurati"
            if settings.youtube_is_configured()
            else "selettori assenti: l'automazione si rifiutera' di partire (voluto)",
        )
    )
    righe.append(
        (
            "Arena",
            settings.arena_is_configured(),
            "configurata"
            if settings.arena_is_configured()
            else "non configurata: il brief copertina viene comunque prodotto",
        )
    )
    righe.append(
        (
            "Flik",
            True,
            "adapter mock (nessuna API reale documentata in questo repository)"
            if not settings.flik_is_real()
            else f"adapter '{settings.flik_adapter}'",
        )
    )

    for nome, ok, nota in righe:
        simbolo = "OK  " if ok else "MANCA"
        typer.echo(f"[{simbolo}] {nome}: {nota}")

    typer.echo(
        "\nLa demo funziona senza Playwright, senza rete e senza credenziali. "
        "Le integrazioni reali vanno configurate in `.env` (vedi `.env.example`)."
    )
    raise typer.Exit(EXIT_OK)


@app.command("show-config-json")
def show_config_json() -> None:
    """Stampa la configurazione effettiva in JSON (senza segreti)."""
    settings = _settings()
    dati = {
        "primary_niche": settings.primary_niche,
        "reports_dir": str(settings.reports_path),
        "browser_headless": settings.browser_headless,
        "browser_timeout_ms": settings.browser_timeout_ms,
        "youtube_configured": settings.youtube_is_configured(),
        "arena_configured": settings.arena_is_configured(),
        "flik_adapter": settings.flik_adapter,
    }
    typer.echo(json.dumps(dati, indent=2, ensure_ascii=False))
    raise typer.Exit(EXIT_OK)


if __name__ == "__main__":  # pragma: no cover
    app()
