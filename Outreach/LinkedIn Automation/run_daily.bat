@echo off
cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"

REM Step 1: Commenta post di professionisti target (warming — 30 commenti)
"C:\Users\Utente\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe" comment_posts.py >> run_today_log.txt 2>&1

REM Step 2: Connection requests + messaggi + follow-up (20 connessioni)
"C:\Users\Utente\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe" run_today.py >> run_today_log.txt 2>&1
