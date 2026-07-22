@echo off
echo ==============================================
echo ESECUZIONE CHECKPOINT GIORNALIERO EOD (h19:00)
echo ==============================================
python memory_manager.py checkpoint --task WORKFLOW-ESTATE --note "Aggiornamento serale metriche e gate"
pause
