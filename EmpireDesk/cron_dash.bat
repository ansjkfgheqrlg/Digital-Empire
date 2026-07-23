@echo off
:: ============================================================================
:: cron_dash.bat — Script di aggiornamento automatico orario per la Dashboard.
::
:: Owner: Max · Controllore: Claude · Origine: FORGE (GEM-05)
:: Governo: MANDATO Art.8 pilastro 2 (Automazioni & Scripts)
:: ============================================================================

:: Determina la cartella radice del monorepo (una cartella sopra a EmpireDesk)
set "REPO_ROOT=%~dp0.."
cd /d "%REPO_ROOT%"

:: Esegue la rigenerazione della dashboard in isolamento
python -m empire dash build

if %ERRORLEVEL% neq 0 (
    echo [ERRORE] Rigenerazione della dashboard fallita con exit code %ERRORLEVEL%.
    exit /b %ERRORLEVEL%
)

echo [OK] Dashboard aggiornata con successo.
