@echo off
rem Avvia PreventivoForge con l'interfaccia grafica (finestra).
rem Doppio click qui: si apre l'app, incolli il link, esce il PDF.
cd /d "%~dp0"
start "" pythonw app.py
