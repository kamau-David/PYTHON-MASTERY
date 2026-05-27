# 09 — Concurrency: Threading, Multiprocessing, Asyncio

Three different ways Python handles "doing more than one thing" - and when
to use each.

## Files
- `threading_demo.py` — threads, good for I/O-bound work (network, disk)
- `multiprocessing_demo.py` — processes, good for CPU-bound work (bypasses the GIL)
- `asyncio_demo.py` — async/await, good for many concurrent I/O-bound tasks

## Run
```bash
python3 threading_demo.py
python3 multiprocessing_demo.py
python3 asyncio_demo.py
```
