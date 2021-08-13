import PyInstaller.__main__

PyInstaller.__main__.run([
    'executable_dist.py',
    '--onefile',
    '--windowed',
    '--distpath=./dist/windows-dist',
    '--workpath=./dist/windows-build',
    '--splash=splash.png',
    '--name=Magni',
    '--icon=icon.ico',
    # '--add-data=./config;./dist/windows-dist/config',
    # '--add-data=./icon.ico;./dist/windows-dist/icon.ico',
    # '--add-data=./splash.png;./dist/windows-dist/splash.png',
    # '--add-data=./LICENSE.md;./dist/windows-dist/LICENSE.md',
    # '--add-data=./README.md;./dist/windows-dist/README.md',
])
