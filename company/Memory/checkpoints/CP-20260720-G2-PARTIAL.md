# CP-20260720-G2 — Empire Desk G2 (build exe) — PARZIALE

**Data:** 2026-07-20  
**Stato:** ⬜ INCOMPLETO — richiede Windows per exe  

---

## Cosa è stato fatto (sandbox Linux)

### G2 — Build exe (PARZIALE)
1. ✅ **platform/dist/ creata** — `npm install` + `npm run build` completati con successo
   - Output: `dist/index.html` (5.72 kB) + `dist/assets/index-*.js` (977 kB)
   - ⚠️ Warning chunk size (normale per app React grande)

2. ✅ **app.py verificato** — syntax + AST OK
   - Nessun errore di parsing

### Cosa MANCA (richiede Windows)

La build exe con PyInstaller **NON può essere eseguita su Linux**. Serve la macchina Windows di Gael:

```batch
cd EmpireDesk
build_exe.bat
```

Il batch file:
1. Fa `npm install && npm run build` in `platform/` (già fatto ✅)
2. Installa dipendenze Python (`requirements.txt` + `pyinstaller`)
3. Lancia `python -m PyInstaller --noconfirm empiredesk.spec`
4. Output: `dist/EmpireDesk/EmpireDesk.exe`

---

## Verifica post-build (su Windows)

Dopo la build exe, testare:

1. **Doppio-click su `dist/EmpireDesk/EmpireDesk.exe`**
   - L'app deve aprirsi con la GUI Aureus
   - Verificare che le 8 tile siano visibili

2. **Test selftest:**
   ```cmd
   dist\EmpireDesk\EmpireDesk.exe --selftest
   ```
   - Atteso: 13/13 PASS

---

## Dipendenze Windows verificate

- ✅ `empiredesk.spec` — configura `platform/dist/` + `modules/` + `state/` nei datas
- ✅ `build_exe.bat` — batch PowerShell-friendly
- ✅ `requirements.txt` — dipendenze Python

---

## Prossimo passo

Eseguire `build_exe.bat` sulla **macchina Windows di Gael**, poi:
1. Testare doppio-click
2. Testare `--selftest`
3. Commit + push + aggiornare STATO-EMPIRE.md
