@echo off
REM ═══════════════════════════════════════════════════════════════
REM  Digital Empire — Daily Outreach (Parallelo)
REM  USO: doppio click ogni mattina
REM  Avvia run_parallel.py che coordina tutto insieme:
REM    - 40 commenti LinkedIn (warming)
REM    - 20 connection requests con nota Barnum/Rainbow
REM    - 150 email con framework 5-Pillar
REM ═══════════════════════════════════════════════════════════════
cd /d "%~dp0"
python run_parallel.py
pause
