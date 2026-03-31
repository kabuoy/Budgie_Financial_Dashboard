# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Budgie.py'],
    pathex=['C:\\Users\\harnish\\AppData\\Local\\miniconda3\\envs\\dash_visualizer'],
    binaries=[],
    datas=[('components', '.'), ('assets', 'assets')],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Budgie',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\parakeet.ico'],
)
