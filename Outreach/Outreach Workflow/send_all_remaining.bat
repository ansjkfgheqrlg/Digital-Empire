@echo off
chcp 65001 >nul
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow"
echo Invio email rimanenti per Batch 5...
python send_ready.py --input emails_b5_ready.json --auto
echo Invio email rimanenti per Batch 6...
python send_ready.py --input emails_b6_ready.json --auto
echo Finito!
