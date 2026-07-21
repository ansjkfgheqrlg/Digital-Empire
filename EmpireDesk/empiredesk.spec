# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec per Empire Desk (app.py) — build onedir.
# Uso:  python -m PyInstaller --noconfirm empiredesk.spec  (PRIMA: build_exe.bat builda platform/)
# Output:  dist/EmpireDesk/EmpireDesk.exe  (deve restare dentro il monorepo Digital Empire:
# lancia le automazioni REALI con path relativi alla radice del repo, vedi _find_repo_root in app.py).
#
# ATTENZIONE (dossier 17 §0-bis, PIVOT AREUS): 'platform/dist' DEVE esistere prima di lanciare
# questo spec (npm install + npm run build dentro platform/, fatto da build_exe.bat) — altrimenti
# PyInstaller.Analysis fallisce (path 'datas' inesistente).
#
# 'modules' e 'state' NON sono bundlati (rimossi qui — erano nel primo tentativo G1, causavano
# selftest FAIL/dati parziali nel frozen: i moduli A1-A3 calcolano il proprio REPO_ROOT da
# `Path(__file__).resolve().parents[2]` assumendo il layout REPO_ROOT/EmpireDesk/modules/<file>.py;
# una copia bundlata sotto `_internal/` rompe quell'assunzione). app.py li carica sempre dal repo
# live (MODULES_DIR = REPO_ROOT/EmpireDesk/modules) — l'exe deve comunque restare dentro il
# monorepo (vedi sopra), quindi la cartella c'e' sempre, nessun bisogno di bundlarla.

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui', 'ui'),
        ('platform/dist', 'platform/dist'),
    ],
    hiddenimports=[
        # GUI premium (pywebview) + backend Windows (Edge WebView2) e fallback Tkinter
        'webview', 'webview.platforms.edgechromium', 'webview.platforms.winforms',
        'clr_loader', 'tkinter',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='EmpireDesk',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # app con finestra, senza console nera
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    # EDE-9: PyInstaller >=6.0 di default sposta TUTTI i 'datas' dentro dist/EmpireDesk/_internal/.
    # Sintomo: l'exe frozen "funziona" (parte, apre una finestra) ma Aureus non si trova (pagina di
    # aiuto invece della piattaforma) e i moduli spariscono in SILENZIO — nessun errore visibile.
    # contents_directory='.' ripristina il layout piatto pre-6.0 (tutto accanto all'exe).
    #
    # NOTA (2 sessioni Gael in parallelo hanno corretto lo stesso bug, entrambe le difese restano —
    # sono complementari, non ridondanti; verificato insieme: selftest 15/15 da .exe):
    #   1. QUESTA riga  -> layout piatto, cosi' i datas stanno accanto all'exe.
    #   2. In app.py    -> `DATA_DIR` (= sys._MEIPASS se frozen) per `platform/`, cosi' Aureus si
    #      trova ANCHE se un domani si torna al layout _internal/; e `MODULES_DIR` ancorata al repo
    #      live (REPO_ROOT/EmpireDesk/modules), perche' i moduli calcolano il proprio repo-root da
    #      `parents[2]` e da una copia bundlata quel calcolo si rompe (metrics dava 1/6 fonti).
    # Vedi REGISTRO-ERRORI.md EDE-9 + company/Memory/checkpoints/CP-20260720-006.md.
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='EmpireDesk',
)
