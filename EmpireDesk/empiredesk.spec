# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec per Empire Desk (app.py) — build onedir.
# Uso:  python -m PyInstaller --noconfirm empiredesk.spec  (PRIMA: build_exe.bat builda platform/)
# Output:  dist/EmpireDesk/EmpireDesk.exe  (deve restare dentro il monorepo Digital Empire:
# lancia le automazioni REALI con path relativi alla radice del repo, vedi _find_repo_root in app.py).
#
# ATTENZIONE (dossier 17 §0-bis, PIVOT AREUS): 'platform/dist' DEVE esistere prima di lanciare
# questo spec (npm install + npm run build dentro platform/, fatto da build_exe.bat) — altrimenti
# PyInstaller.Analysis fallisce (path 'datas' inesistente). 'modules' e 'state' inclusi così i
# moduli A1-A3/scheduler e i loro dati (es. state/revenue.json) funzionano anche nell'exe frozen.

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui', 'ui'),
        ('platform/dist', 'platform/dist'),
        ('modules', 'modules'),
        ('state', 'state'),
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
