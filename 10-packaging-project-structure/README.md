# 10 — Packaging & Project Structure

Virtual environments, `pip`, and structuring a real installable Python
package.

## Files
- `venv_and_pip_cheatsheet.md` — the commands you actually need
- `mypkg_project/` — a minimal installable package with `pyproject.toml`

## Try it
```bash
python3 -m venv venv
source venv/bin/activate
cd mypkg_project
pip install -e .          # editable install
python3 -c "from mypkg import greet; print(greet('Davian'))"
```
