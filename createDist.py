import PyInstaller.__main__

PyInstaller.__main__.run([
    'executable_dist.py',
    '--onefile',
    '--windowed',
    '--distpath=./dist/windows-dist',
    '--workpath=./dist/windows-build',
    '--splash=splash.png',
    '--name=PersonalizedSearchEngine'
])
