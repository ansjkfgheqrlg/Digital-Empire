# 🤝 SETUP-GAEL — Lavorare in due sul monorepo Digital Empire

> Repo: **privato** su GitHub (`digital-empire`). Una volta fatto questo setup,
> NON devi più ricordare comandi git: la sincronizzazione è AUTOMATICA
> (ci pensa Claude Code via hook — pull a inizio sessione, push dopo ogni blocco).

## 1. Prerequisiti (una volta sola)
1. Installa: [Git](https://git-scm.com/download/win), [GitHub CLI](https://cli.github.com/), Claude Code.
2. Accetta l'invito al repo (arriva via email/GitHub da Max).
3. Login GitHub CLI:
   ```powershell
   gh auth login -h github.com    # browser → autorizza
   ```

## 2. Clona il workspace (una volta sola)
```powershell
cd $env:USERPROFILE\Desktop
gh repo clone ansjkfgheqrlg/Digital-Empire "Digital Empire"
cd "Digital Empire"
git config user.name  "Gael"
git config user.email "<email-di-gael>"
git config core.longpaths true
git config core.autocrlf false
git config pull.rebase true
```

## 3. Fatto. Da qui in poi è automatico
Apri Claude Code dentro la cartella `Digital Empire`:
- **All'apertura della sessione** → hook `SessionStart` esegue `scripts/empire-sync.ps1 -Mode pull`
  → ricevi automaticamente tutto quello che ha fatto Max.
- **Dopo ogni blocco di lavoro** (ogni volta che Claude finisce di rispondere) → hook `Stop`
  esegue `-Mode push` → commit + push automatico → Max riceve tutto.

Gli hook viaggiano col repo (`.claude/settings.json`): non devi configurare nulla.

## 4. Comandi manuali (solo se serve)
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/empire-sync.ps1 -Mode full   # sync completo ora
git status                                                                                # cosa è cambiato
```

## 5. Se compare `SYNC-CONFLICT.txt` nella root
Tu e Max avete modificato le STESSE righe dello stesso file. Il tuo lavoro è al sicuro
(committato in locale). Risolvi così:
```powershell
git pull --rebase    # git ti mostra i file in conflitto
# apri i file, scegli le righe giuste, salva
git add -A; git rebase --continue; git push
```
Poi cancella `SYNC-CONFLICT.txt`. In dubbio: chiedi a Claude "risolvi il conflitto di sync".

## 6. Cosa NON viaggia su GitHub (per design — vedi .gitignore)
- Segreti (`.env`, sessioni browser, cookie) — ognuno tiene i propri in locale
- Video `.mp4` e archivi `.zip` (troppo grandi) — passarseli via Drive
- `node_modules/`, build `.next/` — si rigenerano con `npm install`
- Repo annidati indipendenti (es. `Clienti/EXPONIUM` → ha già il suo repo `exponium-client`)

## Regole d'oro
1. **Lavora sempre dentro Claude Code** nella cartella del repo: il sync è garantito.
2. **Mai `git push --force`.**
3. I file grandi nuovi (>100MB) vanno su Drive, non nel repo.
