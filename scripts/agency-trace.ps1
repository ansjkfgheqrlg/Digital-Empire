# agency-trace.ps1 - Logger append-only per il project state AGENCY (F4)
# Uso:
#   powershell -File scripts/agency-trace.ps1 -CycleId "CY-20260611-001" -Step "A2.REPLY" `
#     -Event "handoff_sent" -From "A2" -To "A3" -Hc "HC-A2-A3-call" `
#     -Agent "WF-REPLY-FOLLOWUP" -Summary "call prenotata con Azienda X"
#
# Scrive una riga JSON in company/Memory/state/agency/trace.jsonl
# NON tocca il runtime outreach (ADR-003). NON modifica state.json (quello e' manuale/Claude).

param(
    [Parameter(Mandatory=$true)]  [string]$CycleId,
    [Parameter(Mandatory=$true)]  [ValidateSet("A1.SOURCING","A2.OUTREACH","A2.REPLY","A3.PREVENTIVO","A4.DELIVERY","A4.SUPPORTO","A6.UPSELL","INIT","SYSTEM")] [string]$Step,
    [Parameter(Mandatory=$true)]  [ValidateSet("started","completed","failed","gate_passed","gate_failed","handoff_sent","handoff_received","blocker_added","blocker_resolved")] [string]$Event,
    [Parameter(Mandatory=$true)]  [string]$From,
    [Parameter(Mandatory=$false)] [string]$To = $null,
    [Parameter(Mandatory=$false)] [string]$Hc = $null,
    [Parameter(Mandatory=$false)] [string]$Agent = $null,
    [Parameter(Mandatory=$true)]  [string]$Summary,
    [Parameter(Mandatory=$false)] [string]$Notes = ""
)

$ROOT = Split-Path -Parent $PSScriptRoot
$traceFile = Join-Path $ROOT "company\Memory\state\agency\trace.jsonl"

if (-not (Test-Path $traceFile)) {
    Write-Host "[ERRORE] trace.jsonl non trovato: $traceFile" -ForegroundColor Red
    Write-Host "         Verifica di essere nella root del monorepo Digital Empire."
    exit 1
}

$entry = [ordered]@{
    ts              = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    cycle_id        = $CycleId
    step            = $Step
    event           = $Event
    from_reparto    = $From
    to_reparto      = $To
    hc              = $Hc
    agent           = $Agent
    payload_summary = $Summary
    notes           = $Notes
}

$json = ($entry | ConvertTo-Json -Compress)

# Append senza BOM (PS 5.1: WriteAllText/AppendAllText con UTF8 no-BOM esplicito)
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::AppendAllText($traceFile, $json + "`n", $utf8NoBom)

Write-Host "[OK] Evento tracciato in trace.jsonl:" -ForegroundColor Green
Write-Host "     $json"
exit 0
