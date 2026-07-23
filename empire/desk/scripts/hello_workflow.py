#!/usr/bin/env python3
"""Script dimostrativo: stampa CWD e args, poi termina con successo."""
import time
import sys
import os

print("CWD:", os.getcwd())
print("ARGS:", sys.argv[1:])
print("Avvio del workflow di esempio...")
time.sleep(2)
print("Lavoro completato con successo! ✅")
sys.exit(0)
