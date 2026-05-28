"""Multiprocessing: separate processes, each with its own Python interpreter
and memory - this bypasses the GIL, so it DOES speed up CPU-bound work."""

import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

def run_sequentially(tasks):
    return [cpu_heavy(n) for n in tasks]

def run_in_parallel(tasks):
    with multiprocessing.Pool(processes=4) as pool:
        return pool.map(cpu_heavy, tasks)

if __name__ == "__main__":
    print(f"CPU cores available: {multiprocessing.cpu_count()}")
    print("(if this is 1, parallel won't beat sequential - there's no second")
    print(" core to run on, and you're just paying process-spawn overhead.")
    print(" Run this on a multi-core machine to see the real speedup.)\n")

    tasks = [5_000_000] * 4

    start = time.perf_counter()
    run_sequentially(tasks)
    print(f"sequential: {time.perf_counter() - start:.2f}s")

    start = time.perf_counter()
    run_in_parallel(tasks)
    print(f"parallel:   {time.perf_counter() - start:.2f}s")
