# venv & pip Cheatsheet

## Virtual environments
```bash
python3 -m venv venv              # create a venv in ./venv
source venv/bin/activate          # activate it (Linux/Mac)
venv\Scripts\activate              # activate it (Windows)
deactivate                         # leave the venv
```
Why: keeps each project's dependencies isolated so installing one
project's packages doesn't break another's.

## pip
```bash
pip install requests               # install a package
pip install requests==2.31.0       # pin an exact version
pip install -r requirements.txt    # install everything listed in a file
pip freeze > requirements.txt      # snapshot installed packages + versions
pip uninstall requests
pip list                           # show installed packages
```

## Project layout convention
```
my_project/
├── pyproject.toml       # project metadata + build config (modern standard)
├── README.md
├── requirements.txt      # for apps (pin exact versions)
├── src/ or mypkg/         # your actual package code
│   └── __init__.py
└── tests/
    └── test_something.py
```
