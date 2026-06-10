"""
Auto-login helper: apre Chromium con il profilo persistente,
aspetta 25 secondi (abbastanza per caricare NotebookLM),
poi invia ENTER automaticamente per salvare storage_state.json
"""
import subprocess
import time
import sys

print("Avvio notebooklm login...")
print("Chromium si aprirà. Assicurati di essere su NotebookLM, poi aspetta.")
print()

proc = subprocess.Popen(
    [sys.executable, '-m', 'notebooklm', 'login'],
    stdin=subprocess.PIPE,
    stdout=sys.stdout,
    stderr=sys.stderr,
    text=True
)

# Aspetta che il browser si apra e carichi NotebookLM
for i in range(25, 0, -1):
    print(f"\r  Salvataggio sessione in {i}s...  ", end='', flush=True)
    time.sleep(1)

print("\r  Invio ENTER per salvare la sessione...   ", flush=True)
proc.stdin.write('\n')
proc.stdin.flush()
proc.wait()
print("\nFatto! Sessione salvata.")
