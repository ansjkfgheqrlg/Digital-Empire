$content = Get-Content -Path "porco-dio-empire.html" -Raw
$lines = $content -split "`r`n"
if ($lines.Length -eq 1) { $lines = $content -split "`n" }
$newLines = @()
$skip = $false

foreach ($line in $lines) {
    if ($line.Contains("<!-- ===================== STATS (bg-ink) ===================== -->")) {
        $skip = $true
    }
    if ($line.Contains("<!-- ===================== CTA FINALE + FORM (bg-ink-2) ===================== -->")) {
        $skip = $false
    }
    
    if (-not $skip) {
        $l = $line.Replace("Scopri i Framework", "Scegli un Percorso")
        if ($l.Contains('id="form-section"') -and $l.Contains('class="bg-ink-2')) {
            $l = $l.Replace('class="bg-ink-2', 'class="bg-ink-2 hidden')
        }
        $newLines += $l
        if ($l.Contains("const target = document.getElementById('form-section');")) {
            $newLines += "      target.classList.remove('hidden');"
        }
    }
}
$newLines -join "`r`n" | Set-Content -Path "porco-dio-empire.html" -Encoding utf8
Write-Host "Done"
