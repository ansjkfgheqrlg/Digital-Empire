# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec per PreventivoForge Desktop (app.py) — build onedir.
# Uso:  python -m PyInstaller --noconfirm preventivo-forge.spec
# Output:  dist/PreventivoForge/PreventivoForge.exe  (cartella portabile).
# Il PC di destinazione deve avere Google Chrome installato (motore cdp).

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['implementation'],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('schema', 'schema'),
        ('concessionarie', 'concessionarie'),
        ('implementation', 'implementation'),
        ('ui', 'ui'),
    ],
    hiddenimports=[
        # moduli pipeline (importati a runtime via sys.path)
        'run', 'common', 'scraper', 'parser', 'pricer', 'dealers', 'cdp',
        'translate_copy', 'render_pdf', 'qa_gate', 'glossary_de_it',
        # dipendenze terze
        'jinja2', 'PIL', 'PIL.Image', 'jsonschema', 'websocket', 'requests',
        'bs4', 'lxml',
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
    name='PreventivoForge',
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
    name='PreventivoForge',
)
