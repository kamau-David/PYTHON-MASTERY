"""Threading: best for I/O-bound tasks (waiting on network/disk), since
Python's GIL means threads don't give a speedup for CPU-bound work."""

import threading
import time

def download_simulated(name, seconds):
    print(f"start downloading {name}")
    time.sleep(seconds)   # simulates waiting on I/O, not CPU work
    print(f"finished downloading {name}")

start = time.perf_counter()

threads = [
    threading.Thread(target=download_simulated, args=(f"file{i}", 1))
    for i in range(4)
]
for t in threads:
    t.start()
for t in threads:
    t.join()   # wait for all threads to finish

print(f"all downloads done in {time.perf_counter() - start:.2f}s (not 4s!)")

# Locks prevent race conditions when threads share mutable state
counter = 0
lock = threading.Lock()

def increment_safely():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment_safely) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("counter (should be exactly 400000):", counter)
