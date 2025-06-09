from setuptools import setup

APP = ['test_app.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app.icns',  # ← добавь сюда путь к иконке
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
