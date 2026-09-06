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

function Invoke-Git {
    # Esegue git catturando DAVVERO stdout+stderr, e l'exit code preso sull'istante.
    #
    # PERCHE' ESISTE (difetto misurato il 2026-09-06). Prima i tre punti che possono
    # fallire (pull, commit, push) facevano cosi':
    #     $out = git commit -m "..." 2>&1
    # In PowerShell 5.1 lo stderr di un comando NATIVO redirezionato con 2>&1 diventa un
    # ErrorRecord; con $ErrorActionPreference = "SilentlyContinue" (riga in cima a questo
    # script) quegli ErrorRecord vengono soppressi invece che finire in $out. Risultato
    # visto sul campo: SYNC-CONFLICT.txt diceva "COMMIT BLOCCATO da un controllo
    # pre-commit" con le righe del motivo VUOTE. Un marker diagnostico che perde la
    # diagnosi costringe chi arriva dopo a rifare l'indagine da zero — e' successo, ed e'
    # costato un'indagine intera.
    #
    # I file temporanei non dipendono da come PowerShell tratta i flussi dei comandi
    # nativi: e' l'unico modo che non torna a rompersi da solo alla prossima versione.
    # NOTA PAGATA CON UNA PROVA (2026-09-06). La prima versione usava
    #     Start-Process -FilePath git -ArgumentList $Args
    # e si e' rotta sul primo collaudo: Start-Process unisce gli argomenti con uno spazio
    # SENZA quotarli, quindi il messaggio "sync(Max): aggiornamento automatico ..." si
    # spezzava e git rispondeva "pathspec 'aggiornamento' did not match any file(s)".
    # Avrebbe rotto OGNI commit automatico del team. L'operatore di chiamata con splatting
    # (`& git @Args`) quota gli argomenti correttamente da solo; la redirezione su file
    # tiene comunque lo stderr fuori dagli ErrorRecord, che era il difetto d'origine.
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Args)

    $fOut = [System.IO.Path]::GetTempFileName()
    $fErr = [System.IO.Path]::GetTempFileName()
    try {
        & git @Args 1> $fOut 2> $fErr
        $code = $LASTEXITCODE   # preso sull'istante: qualunque comando dopo lo sovrascrive
        $testo = ((Get-Content $fOut -Raw -ErrorAction SilentlyContinue),
                  (Get-Content $fErr -Raw -ErrorAction SilentlyContinue)) -join ""
        return [pscustomobject]@{ Code = $code; Output = ("$testo").Trim() }
    } catch {
        # Se perfino l'avvio fallisce, si dichiara invece di fingere un successo (§3).
        return [pscustomobject]@{ Code = 1; Output = "Invoke-Git non ha potuto eseguire git: $_" }
    } finally {
        Remove-Item $fOut, $fErr -Force -ErrorAction SilentlyContinue
    }
}

function Warn-Conflict {
    param([string]$Detail)
    if ([string]::IsNullOrWhiteSpace($Detail)) {
        # Un marker senza motivo e' il difetto che questo blocco esiste per impedire:
        # se il motivo manca, lo si dice, invece di lasciare tre righe vuote.
        $Detail = "(motivo non catturato: nessun output da git. Rilancia a mano il comando fallito per vederlo.)"
    }
    $msg = @"
[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] CONFLITTO DI SYNC
$Detail
Il tuo lavoro e' al sicuro (committato in locale).
Risolvi a mano: git pull --rebase  ->  risolvi i conflitti  ->  git push
Poi cancella questo file.
"@
    # UTF-8 SENZA BOM: Set-Content -Encoding utf8 in PS 5.1 scrive il BOM, e il marker
    # si apriva con un "" davanti alla prima riga.
    [System.IO.File]::WriteAllText(
        (Join-Path $RepoRoot "SYNC-CONFLICT.txt"), $msg, (New-Object System.Text.UTF8Encoding($false)))
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
    $rebase = Invoke-Git pull --rebase --autostash origin main
    if ($rebase.Code -ne 0) {
        git rebase --abort 2>$null | Out-Null
        Warn-Conflict "Pull --rebase fallito:`n`n$($rebase.Output)"
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
        # NIENTE "2>$null | Out-Null" qui: dal 2026-08-27 esistono controlli
        # pre-commit (.githooks/) che possono BLOCCARE il commit di proposito —
        # collisione di ID checkpoint (B-009), CRLF nella memoria (B-028), blob
        # oltre 5 MB (B-008). Con l'output soppresso e l'exit code non guardato,
        # un commit bloccato spariva in silenzio: il sync diceva "ok" e il lavoro
        # restava non committato e non pushato, senza che nessuno lo sapesse.
        # E' esattamente il difetto che quei controlli esistono per impedire.
        $res = Invoke-Git commit -m "sync($who): aggiornamento automatico $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        if ($res.Code -ne 0) {
            Warn-Conflict @"
COMMIT BLOCCATO da un controllo pre-commit. Il lavoro NON e' committato ne' pushato.

$($res.Output)

Cosa fare: leggi il messaggio qui sopra, correggi il problema (spesso basta
  python .githooks/check_memory.py --fix
) e rilancia. Non usare --no-verify: quei controlli fermano guasti che si
scoprirebbero al merge, a ore di distanza.
"@
            return $false
        }
    }
    # Offline? Il commit locale e' fatto (lavoro al sicuro), push al prossimo giro
    if (-not (Test-Online)) { Write-Output "EMPIRE-SYNC: offline, commit locale ok - push rimandato"; return $true }
    # (Qui stava un blocco commit morto: `$dirty = $null` seguito da `if ($dirty)`, quindi
    #  mai eseguito. Rimosso il 2026-09-06 — il commit vero avviene sopra, righe ~95.)

    # C'e' qualcosa da pushare? (commit locali avanti rispetto al remoto)
    git fetch origin 2>$null | Out-Null
    $ahead = git rev-list --count origin/main..HEAD 2>$null
    if ([int]$ahead -eq 0) { return $true }   # nulla da fare

    # Integra prima il lavoro degli altri (Gael), poi pusha
    $rebase = Invoke-Git pull --rebase --autostash origin main
    if ($rebase.Code -ne 0) {
        git rebase --abort 2>$null | Out-Null
        Warn-Conflict "Rebase pre-push fallito:`n`n$($rebase.Output)"
        return $false
    }
    $push = Invoke-Git push origin main
    if ($push.Code -ne 0) {
        Warn-Conflict "Push fallito:`n`n$($push.Output)"
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
