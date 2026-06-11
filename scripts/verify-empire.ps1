# verify-empire.ps1 - EMPIRE OS Structure + Integrity Check v1
# Uso: powershell -File scripts/verify-empire.ps1 [-Verbose] [-Fix]
# Gate: tutti i check devono essere PASS per considerare l'ecosistema sano.

param(
    [switch]$Verbose,
    [switch]$Fix
)

$ROOT = Split-Path -Parent $PSScriptRoot
$COMPANY = Join-Path $ROOT "company"
$pass = 0
$fail = 0
$warnings = 0

function Check($label, $ok, $detail = "") {
    if ($ok) {
        if ($Verbose) { Write-Host "  [PASS] $label" -ForegroundColor Green }
        $script:pass++
    } else {
        Write-Host "  [FAIL] $label" -ForegroundColor Red
        $script:fail++
    }
}

function Warn($label) {
    Write-Host "  [WARN] $label" -ForegroundColor Yellow
    $script:warnings++
}

Write-Host ""
Write-Host ("=" * 60)
Write-Host "  EMPIRE OS -- verify-empire v1"
Write-Host "  $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Write-Host ("=" * 60)

# --- F1: struttura company/ ---
Write-Host ""
Write-Host "[ F1 - Struttura company/ ]"

$f1_required = @(
    "company\GRUPPO.md",
    "company\Mandato\MANDATO-EMPIRE.md",
    "company\Board-CSuite\README.md",
    "company\Board-CSuite\CEO-Empire-Conductor.md",
    "company\Board-CSuite\COO.md",
    "company\Board-CSuite\CTO.md",
    "company\Board-CSuite\CMO.md",
    "company\Board-CSuite\CRO.md",
    "company\Board-CSuite\CFO.md",
    "company\Board-CSuite\Chief-Forge.md",
    "company\Backbone\README.md",
    "company\Backbone\Bus\README.md",
    "company\Backbone\Brain\README.md",
    "company\Backbone\Governance\README.md",
    "company\Backbone\Identity-HR\README.md",
    "company\Backbone\Coordination\README.md",
    "company\Guilds\README.md",
    "company\Sentinels\README.md",
    "company\Gerarchia\README.md",
    "company\Memory\INDEX.md",
    "company\Memory\STATO-EMPIRE.md"
)

$ecosistemi = @("01-AGENCY","02-INFO-BUSINESS","03-CONTENT-FACTORY","04-MARKETING",
                "05-MULTI-BUSINESS","06-PLATFORM","07-FORGE","08-INTELLIGENCE",
                "09-OPERATIONS","10-MEMORY")

foreach ($f in $f1_required) {
    Check $f (Test-Path (Join-Path $ROOT $f))
}
foreach ($eco in $ecosistemi) {
    Check "Ecosistemi\$eco\ECOSISTEMA.md" (Test-Path (Join-Path $COMPANY "Ecosistemi\$eco\ECOSISTEMA.md"))
    Check "Ecosistemi\$eco\BACKBONE.md"   (Test-Path (Join-Path $COMPANY "Ecosistemi\$eco\BACKBONE.md"))
}

# --- Mandato: parole chiave fondamentali ---
Write-Host ""
Write-Host "[ Mandato - Integrita documento costituzionale ]"

$mandato = Join-Path $COMPANY "Mandato\MANDATO-EMPIRE.md"
if (Test-Path $mandato) {
    $content = Get-Content $mandato -Raw -Encoding UTF8
    Check "Mandato: contiene APSOC"          ($content -match "APSOC")
    Check "Mandato: contiene brand voice"    ($content -match "brand voice|Brand Voice")
    Check "Mandato: contiene prezzi"         ($content -match "4\.000|3\.500|2\.500|8\.000")
    Check "Mandato: contiene non-negoziabile" ($content -match "non.negoziabil")
} else {
    Check "Mandato: file esiste" $false
}

# --- Memory: checkpoint recente ---
Write-Host ""
Write-Host "[ Memory - Stato e checkpoint ]"

$stato = Join-Path $COMPANY "Memory\STATO-EMPIRE.md"
if (Test-Path $stato) {
    $s = Get-Content $stato -Raw -Encoding UTF8
    Check "STATO-EMPIRE esiste"          $true
    Check "STATO-EMPIRE ha RIPRESA DA"   ($s -match "RIPRESA DA")
    Check "STATO-EMPIRE ha fase roadmap" ($s -match "Fase roadmap")
} else {
    Check "STATO-EMPIRE esiste" $false
}

$cpDir = Join-Path $COMPANY "Memory\checkpoints"
if (Test-Path $cpDir) {
    $cps = (Get-ChildItem $cpDir -Filter "CP-*.md" | Measure-Object).Count
    Check "Checkpoint presenti ($cps)" ($cps -gt 0)
} else {
    Warn "Cartella checkpoints mancante"
}

# --- Backbone: componenti operativi F2 ---
Write-Host ""
Write-Host "[ Backbone - Componenti F2 ]"

Check "Bus\handoffs esiste"      (Test-Path (Join-Path $COMPANY "Backbone\Bus\handoffs"))
Check "Bus\contracts esiste"     (Test-Path (Join-Path $COMPANY "Backbone\Bus\contracts"))
Check "HC-template.json"         (Test-Path (Join-Path $COMPANY "Backbone\Bus\contracts\HC-template.json"))
Check "registro-agenti.yaml"     (Test-Path (Join-Path $COMPANY "Backbone\Identity-HR\registro-agenti.yaml"))

# --- F3: Migrazione asset ---
Write-Host ""
Write-Host "[ F3 - Migrazione asset ]"

Check "skills-map.yaml"                     (Test-Path (Join-Path $COMPANY "skills-map.yaml"))
Check "org\inventario-asset.yaml"           (Test-Path (Join-Path $COMPANY "org\inventario-asset.yaml"))
Check "01-AGENCY Workflow wrapper"          (Test-Path (Join-Path $COMPANY "Ecosistemi\01-AGENCY\Workflow\outreach-wrapper.md"))
Check "02-INFO-BUSINESS Workflow wrapper"   (Test-Path (Join-Path $COMPANY "Ecosistemi\02-INFO-BUSINESS\Workflow\lancio-wrapper.md"))
Check "03-CONTENT-FACTORY Workflow wrapper" (Test-Path (Join-Path $COMPANY "Ecosistemi\03-CONTENT-FACTORY\Workflow\caroselli-wrapper.md"))
Check "04-MARKETING Workflow wrapper"       (Test-Path (Join-Path $COMPANY "Ecosistemi\04-MARKETING\Workflow\copy-workflow-wrapper.md"))
Check "05-MULTI-BUSINESS Workflow wrapper"  (Test-Path (Join-Path $COMPANY "Ecosistemi\05-MULTI-BUSINESS\Workflow\libri-wrapper.md"))
Check "06-PLATFORM Workflow wrapper"        (Test-Path (Join-Path $COMPANY "Ecosistemi\06-PLATFORM\Workflow\crea-siti-wrapper.md"))
Check "07-FORGE Workflow wrapper"           (Test-Path (Join-Path $COMPANY "Ecosistemi\07-FORGE\Workflow\skill-creator-wrapper.md"))
Check "08-INTELLIGENCE Workflow wrapper"    (Test-Path (Join-Path $COMPANY "Ecosistemi\08-INTELLIGENCE\Workflow\wiki-wrapper.md"))

# Controllo 0 orfani (orfani dichiarati nel inventario devono essere <= 3)
$invFile = Join-Path $COMPANY "org\inventario-asset.yaml"
if (Test-Path $invFile) {
    $inv = Get-Content $invFile -Raw -Encoding UTF8
    $orfaniCount = ([regex]::Matches($inv, "orfano: true")).Count
    Check "Orfani <= 3 (attuale: $orfaniCount)" ($orfaniCount -le 3)
}

# --- F4: AGENCY live ---
Write-Host ""
Write-Host "[ F4 - AGENCY live ]"

$agencyDir = Join-Path $COMPANY "01-agency"
Check "01-agency/ esiste"                         (Test-Path $agencyDir)
Check "01-agency/BACKBONE.md"                     (Test-Path (Join-Path $agencyDir "BACKBONE.md"))

$reparti = @("A1-RICERCA","A2-ACQUISIZIONE","A3-PREVENTIVI","A4-DELIVERY","A5-COPY-INTERNO","A6-MARKETING-INTERNO")
foreach ($r in $reparti) {
    Check "01-agency/$r/BACKBONE.md"              (Test-Path (Join-Path $agencyDir "$r\BACKBONE.md"))
}

Check "A1 handoffs/HC-A1-A2-leads.json"           (Test-Path (Join-Path $agencyDir "A1-RICERCA\handoffs\HC-A1-A2-leads.json"))
Check "A2 handoffs/HC-A2-A3-call.json"            (Test-Path (Join-Path $agencyDir "A2-ACQUISIZIONE\handoffs\HC-A2-A3-call.json"))
Check "A3 handoffs/HC-A3-A4-contratto.json"       (Test-Path (Join-Path $agencyDir "A3-PREVENTIVI\handoffs\HC-A3-A4-contratto.json"))
Check "A4 handoffs/HC-A4-A6-testimonianza.json"   (Test-Path (Join-Path $agencyDir "A4-DELIVERY\handoffs\HC-A4-A6-testimonianza.json"))

Check "Memory/state/agency/README.md"             (Test-Path (Join-Path $COMPANY "Memory\state\agency\README.md"))
Check "Memory/state/agency/state.json"            (Test-Path (Join-Path $COMPANY "Memory\state\agency\state.json"))
Check "Memory/state/agency/trace.jsonl"           (Test-Path (Join-Path $COMPANY "Memory\state\agency\trace.jsonl"))

$stateFile = Join-Path $COMPANY "Memory\state\agency\state.json"
if (Test-Path $stateFile) {
    $st = Get-Content $stateFile -Raw -Encoding UTF8
    Check "state.json: schema agency-state-v1"    ($st -match "agency-state-v1")
    Check "state.json: kpi presenti"              ($st -match '"kpi"')
}

$traceFile = Join-Path $COMPANY "Memory\state\agency\trace.jsonl"
if (Test-Path $traceFile) {
    $traceLines = (Get-Content $traceFile -Encoding UTF8 | Measure-Object -Line).Lines
    Check "trace.jsonl: almeno 1 evento ($traceLines righe)" ($traceLines -ge 1)
}

# Skills F4 (9 nuove)
$skillsF4 = @(
    ".claude\skills\discovery-call-brief\SKILL.md",
    ".claude\skills\proposal-gate\SKILL.md",
    ".claude\skills\delivery-playbook\SKILL.md",
    ".claude\skills\client-handover\SKILL.md",
    ".claude\skills\support-90\SKILL.md",
    ".claude\skills\outreach-reply-triage\SKILL.md",
    ".claude\skills\icp-radar\SKILL.md",
    ".claude\skills\case-study-forge\SKILL.md",
    ".claude\skills\upsell-mapper\SKILL.md"
)
foreach ($sk in $skillsF4) {
    Check "Skill $sk" (Test-Path (Join-Path $ROOT $sk))
}

# --- Scripts ---
Write-Host ""
Write-Host "[ Scripts ]"

Check "gen-empire.py esiste"     (Test-Path (Join-Path $ROOT "scripts\gen-empire.py"))
Check "empire-sync.ps1 esiste"   (Test-Path (Join-Path $ROOT "scripts\empire-sync.ps1"))
Check "verify-empire.ps1 esiste" (Test-Path (Join-Path $ROOT "scripts\verify-empire.ps1"))

# --- .gitignore: segreti esclusi ---
Write-Host ""
Write-Host "[ Sicurezza - .gitignore ]"

$gi = Join-Path $ROOT ".gitignore"
if (Test-Path $gi) {
    $g = Get-Content $gi -Raw -Encoding UTF8
    Check "gitignore: esclude .env"         ($g -match "\.env")
    Check "gitignore: esclude session_data" ($g -match "session_data")
    Check "gitignore: esclude node_modules" ($g -match "node_modules")
} else {
    Warn ".gitignore non trovato"
}

# --- RIEPILOGO ---
$total = $pass + $fail
Write-Host ""
Write-Host ("=" * 60)
Write-Host "  PASS: $pass / $total   |   FAIL: $fail   |   WARN: $warnings"
if ($fail -eq 0) {
    Write-Host "  [OK] Tutti i gate VERDE - EMPIRE OS integro" -ForegroundColor Green
} else {
    Write-Host "  [!!] $fail gate ROSSI - verificare i FAIL sopra" -ForegroundColor Red
    Write-Host "       Riesegui con: python scripts/gen-empire.py (crea mancanti)"
}
Write-Host ("=" * 60)
Write-Host ""

exit $fail
