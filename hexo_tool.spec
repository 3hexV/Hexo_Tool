# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['hexo_tool.py'],
             pathex=['E:\\23_project\\hexo_tool'],
             binaries=[],
             datas=[('.\\\\*.mps1', '.\\\\'),('.\\\\ht_cfg.ini', '.\\\\'),('.\\\\hexo.ico', '.\\\\')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='hexo_tool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='hexo_tool_demo_v_1_1',
	icon='heox.icon')
