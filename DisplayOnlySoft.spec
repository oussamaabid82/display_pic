# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['display.py'],
    pathex=[],
    binaries=[],
    datas=[
        (
            'D:/PROJETS/display_pic/tk',
            'tk/'
        ),
        (
            'D:/PROJETS/display_pic/tk/logo',
            'logo/'
        ),
        (
            'D:/PROJETS/display_pic/tk/icon',
            'icon/'
        ),
        (
            'D:/PROJETS/display_pic/tk/splash',
            'splash/'
        ),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
splash = Splash(
    'D:/PROJETS/display_pic/tk/splash/splashonly.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=None,
    text_color=None,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='Display_Only_Soft',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:/PROJETS/display_pic/tk/icon/icon.ico'],
)
