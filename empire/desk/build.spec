# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec per Empire Desk (Windows, windowed / no console).
# Build:  pyinstaller build.spec
import os

block_cipher = None

a = Analysis(
    ['empire_desk.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('workflows.json', '.'),
        ('scripts', 'scripts'),
        ('apex7', 'apex7'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='EmpireDesk',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,                # Tray app: nessuna console
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe, a.binaries, a.zipfiles, a.datas,
    name='EmpireDesk',
)
