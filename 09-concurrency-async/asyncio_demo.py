"""asyncio: a single thread that cooperatively switches between tasks
whenever one is waiting on I/O. Great for many concurrent network calls."""

import asyncio
import time

async def fetch_simulated(name, seconds):
    print(f"start fetching {name}")
    await asyncio.sleep(seconds)   # non-blocking "wait" - other tasks run meanwhile
    print(f"finished fetching {name}")
    return f"{name} result"

async def main():
    start = time.perf_counter()

    # asyncio.gather runs all these concurrently on one thread
    results = await asyncio.gather(
        fetch_simulated("endpoint-A", 1),
        fetch_simulated("endpoint-B", 1),
        fetch_simulated("endpoint-C", 1),
    )
    print(results)
    print(f"all fetches done in {time.perf_counter() - start:.2f}s (not 3s!)")

    # as_completed lets you process results as they finish, not all at once
    tasks = [fetch_simulated(f"job-{i}", i * 0.5) for i in range(1, 4)]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print("completed:", result)

asyncio.run(main())
