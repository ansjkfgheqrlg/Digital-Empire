# ============================================================
# EMPIRE OS — empire-sync.ps1
# Sincronizzazione bidirezionale del monorepo Digital Empire.
#
#   -Mode pull   : allinea il PC con GitHub (inizio sessione)
#   -Mode push   : commit + rebase + push (dopo ogni blocco di lavoro)
#   -Mode full   : pull poi push (manuale)
#
# Invocato automaticamente dagli hook Claude Code:
#   SessionStart -> pull   |   Stop -> push
# Identico sul PC di Max e su quello di Gael (viaggia col repo).
#
# Garanzie di sicurezza:
#   - mai distruttivo: niente reset --hard, niente force push
#   - conflitto di rebase -> abort + avviso in SYNC-CONFLICT.txt
#     (il lavoro resta committato in locale, si risolve a mano)
#   - lock file contro esecuzioni sovrapposte
#   - rate-limit push: max 1 ogni 90 secondi
# ============================================================
param(
    [ValidateSet("pull", "push", "full")]
    [string]$Mode = "full"
)

$ErrorActionPreference = "SilentlyContinue"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

# Non e' un repo git -> esci in silenzio (setup non ancora fatto)
if (-not (Test-Path (Join-Path $RepoRoot ".git"))) { exit 0 }

# --- Lock anti-sovrapposizione ---
$LockFile = Join-Path $RepoRoot ".git\empire-sync.lock"
if (Test-Path $LockFile) {
    $age = (Get-Date) - (Get-Item $LockFile).LastWriteTime
    if ($age.TotalMinutes -lt 5) { exit 0 }   # un altro sync e' in corso
    Remove-Item $LockFile -Force              # lock stantio, rimuovi
}
New-Item -ItemType File -Path $LockFile -Force | Out-Null

function Release-Lock { Remove-Item $LockFile -Force -ErrorAction SilentlyContinue }

function Warn-Conflict {
    param([string]$Detail)
    $msg = @"
[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] CONFLITTO DI SYNC
$Detail
Il tuo lavoro e' al sicuro (committato in locale).
Risolvi a mano: git pull --rebase  ->  risolvi i conflitti  ->  git push
Poi cancella questo file.
"@
    Set-Content -Path (Join-Path $RepoRoot "SYNC-CONFLICT.txt") -Value $msg -Encoding utf8
    Write-Output "EMPIRE-SYNC: conflitto rilevato - vedi SYNC-CONFLICT.txt"
}

function Test-Online {
    # GitHub raggiungibile? Se no: niente sync, niente falsi allarmi (si riprova al prossimo giro)
    git ls-remote --exit-code origin HEAD 2>$null | Out-Null
    return ($LASTEXITCODE -eq 0)
}

function Do-Pull {
    if (-not (Test-Online)) { Write-Output "EMPIRE-SYNC: offline, salto (riprovo al prossimo giro)"; return $true }
    git fetch origin 2>$null | Out-Null
    $rebase = git pull --rebase --autostash origin main 2>&1
    if ($LASTEXITCODE -ne 0) {
        git rebase --abort 2>$null | Out-Null
        Warn-Conflict "Pull --rebase fallito: $rebase"
        return $false
    }
    Write-Output "EMPIRE-SYNC: pull OK (allineato con GitHub)"
    return $true
}

function Do-Push {
    # Rate-limit: max un push ogni 90s (lo Stop hook scatta a ogni risposta)
    $StampFile = Join-Path $RepoRoot ".git\empire-sync.last-push"
    if (Test-Path $StampFile) {
        $since = (Get-Date) - (Get-Item $StampFile).LastWriteTime
        if ($since.TotalSeconds -lt 90) { return $true }
    }

    # Commit solo se c'e' qualcosa di nuovo
    $dirty = git status --porcelain 2>$null
    if ($dirty) {
        git add -A 2>$null | Out-Null
        $who = git config user.name
        git commit -m "sync($who): aggiornamento automatico $(Get-Date -Format 'yyyy-MM-dd HH:mm')" 2>$null | Out-Null
    }
    # Offline? Il commit locale e' fatto (lavoro al sicuro), push al prossimo giro
    if (-not (Test-Online)) { Write-Output "EMPIRE-SYNC: offline, commit locale ok - push rimandato"; return $true }
    $dirty = $null
    if ($dirty) {
        git add -A 2>$null | Out-Null
        $who = git config user.name
        git commit -m "sync($who): aggiornamento automatico $(Get-Date -Format 'yyyy-MM-dd HH:mm')" 2>$null | Out-Null
    }

    # C'e' qualcosa da pushare? (commit locali avanti rispetto al remoto)
    git fetch origin 2>$null | Out-Null
    $ahead = git rev-list --count origin/main..HEAD 2>$null
    if (-not $dirty -and ([int]$ahead -eq 0)) { return $true }   # nulla da fare

    # Integra prima il lavoro degli altri (Gael), poi pusha
    $rebase = git pull --rebase --autostash origin main 2>&1
    if ($LASTEXITCODE -ne 0) {
        git rebase --abort 2>$null | Out-Null
        Warn-Conflict "Rebase pre-push fallito: $rebase"
        return $false
    }
    $push = git push origin main 2>&1
    if ($LASTEXITCODE -ne 0) {
        Warn-Conflict "Push fallito: $push"
        return $false
    }
    New-Item -ItemType File -Path $StampFile -Force | Out-Null
    Write-Output "EMPIRE-SYNC: push OK (GitHub aggiornato)"
    return $true
}

try {
    switch ($Mode) {
        "pull" { Do-Pull | Out-Null }
        "push" { Do-Push | Out-Null }
        "full" { if (Do-Pull) { Do-Push | Out-Null } }
    }
} finally {
    Release-Lock
}
exit 0
