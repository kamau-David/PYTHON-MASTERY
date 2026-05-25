# 08 — Testing, Debugging & Logging

Writing tests with `unittest` and `pytest`, and using `logging` instead of
scattered `print()` calls.

## Files
- `calculator.py` — a small module to test
- `test_calculator_unittest.py` — tests using the standard library's `unittest`
- `test_calculator_pytest.py` — the same tests, pytest-style (less boilerplate)
- `logging_demo.py` — structured logging with levels and formatting
- `requirements.txt` — pytest

## Run
```bash
python3 -m unittest test_calculator_unittest.py -v
pip install -r requirements.txt
pytest test_calculator_pytest.py -v
python3 logging_demo.py
```
