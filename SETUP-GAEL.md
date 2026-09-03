# 🤝 SETUP-GAEL — Lavorare sul monorepo Digital Empire, con Emperator

> Repo su GitHub. Una volta fatto questo setup,
> NON devi più ricordare comandi git: la sincronizzazione è AUTOMATICA
> (ci pensa Claude Code via hook — pull a inizio sessione, push dopo ogni blocco).

---

## 0. EMPERATOR — leggi questo per primo *(aggiunto 2026-09-03)*

**Ce l'hai già.** È arrivato con un `git pull`, non c'è niente da installare.
Fino a oggi questa guida non te lo diceva: è per quello che non l'hai mai usato, e la
colpa è della guida, non tua.

### Cos'è, senza giri di parole

Emperator non è un programma separato né un'altra AI. È **la dottrina di Digital Empire
che si accende dentro la tua sessione di Claude Code** quando pronunci il nome: la mappa
dei 14 ecosistemi, la Memory, gli ADR, il backlog, i comandi di misura, le regole di
lavoro. Stessa testa, stessa sessione — ma che sa dove sta ogni cosa invece di doverlo
riscoprire.

### Come si accende

Scrivi **«Emperator»** dentro la frase, in Claude Code, dentro la cartella `Digital Empire`:

```
Emperator, chiudi L2 del reparto Lanci
```

invece di «chiudi L2 del reparto Lanci». Tutto qui. Nessun comando, nessuno slash.

### Una verifica, una volta sola

```powershell
py -3 --version
```

Se **non** risponde un numero di versione, l'hook non parte — e non te ne accorgi, perché
fallisce in silenzio. In quel caso installa Python da python.org spuntando *«Add python.exe
to PATH»*, e riprova.

### Perché conviene a te, in concreto

Il 2026-09-02 hai chiuso la ricognizione L1 dei Lanci e hai scritto: *«0 agenti ufficiali
su 9, violazione ADR-008, stessa forma del difetto dei 120 file del 2026-08-31»*.
Diagnosi giusta e misurata. Ma la regola che chiude quel buco e gli strumenti per farlo
(`empire forge scan`, `registry orphans`, il formato di frontmatter che rende un agente
davvero invocabile) erano già dentro Emperator: quei 9 agenti si ufficializzavano in una
passata invece di finire in una nota.

**Non è un obbligo burocratico: è che il lavoro passa da lì.** Decisione di Max, 2026-09-03.
Tu continui a decidere come si fa il tuo lavoro — Emperator è il capo dei sistemi, non delle
persone.

### Se ti risponde «sono Claude, Emperator è solo una voce»

Era vero fino al 2026-09-02: la dottrina era scritta **solo per Max** («il primo e unico
interlocutore di Max»), quindi con te davanti si contraddiceva e la cosa onesta era
romperla. **Corretto il 2026-09-03:** ora si rivolge a chi la chiama, per nome. Se lo vedi
ancora, fai `git pull` — sei indietro.

---

## 1. Prerequisiti (una volta sola)
1. Installa: [Git](https://git-scm.com/download/win), [GitHub CLI](https://cli.github.com/), Claude Code.
2. Login GitHub CLI **con l'account di Max (ansjkfgheqrlg)** — decisione condivisa: si usa
   un solo account GitHub. Fai il login insieme a Max (lui autorizza il codice device):
   ```powershell
   gh auth login -h github.com    # account: ansjkfgheqrlg → codice device → Max autorizza
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
git pull --rebase                 # git ti mostra i file in conflitto
# apri i file, scegli le righe giuste, salva
git add <solo i file che hai risolto>   # NON `git add -A` — vedi sotto
git rebase --continue; git push
```
Poi cancella `SYNC-CONFLICT.txt`. In dubbio: **«Emperator, risolvi il conflitto di sync»**.

> ⚠️ **Mai `git add -A` durante un conflitto.** Il 2026-09-02 uno `stash pop` aveva lasciato
> **13.778 file — 13,4 GB** di frame video di Empire Studio in stage: un `add -A` li avrebbe
> spediti su GitHub. Prima di ogni push, il controllo che ti salva:
> ```powershell
> git status --porcelain | Measure-Object -Line
> ```
> Se il numero è assurdo — migliaia di file che non hai creato tu — **non pushare**: guarda
> cosa sono e scrivi a Max. ADR-013 vieta i blob pesanti nella storia, e B-008 documenta un
> push già morto a 899 MB.

## 6. Cosa NON viaggia su GitHub (per design — vedi .gitignore)
- Segreti (`.env`, sessioni browser, cookie) — ognuno tiene i propri in locale
- Video `.mp4` e archivi `.zip` (troppo grandi) — passarseli via Drive
- `node_modules/`, build `.next/` — si rigenerano con `npm install`
- Repo annidati indipendenti (es. `Clienti/EXPONIUM` → ha già il suo repo `exponium-client`)

## Regole d'oro
1. **Lavora sempre dentro Claude Code** nella cartella del repo: il sync è garantito.
2. **Mai `git push --force`.**
3. I file grandi nuovi (>100MB) vanno su Drive, non nel repo.
