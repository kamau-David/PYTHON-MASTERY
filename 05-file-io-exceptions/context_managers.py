"""Context managers: the `with` statement, and writing your own."""

# open() is the most common context manager - it guarantees the file
# is closed even if an exception happens inside the block.
with open(__file__, "r") as f:
    first_line = f.readline()
print("first line of this file:", first_line.strip())


# Class-based context manager: implement __enter__ and __exit__
class Timer:
    def __enter__(self):
        import time
        self._start = time.perf_counter()
        return self   # this is what gets bound to `as timer`

    def __exit__(self, exc_type, exc_value, traceback):
        import time
        elapsed = time.perf_counter() - self._start
        print(f"block took {elapsed:.6f}s")
        return False  # False = don't suppress exceptions


with Timer():
    total = sum(n * n for n in range(1_000_000))
print("total:", total)


# contextlib.contextmanager - a simpler way using a generator function
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"acquiring {name}")
    try:
        yield name   # this is what gets bound to `as`
    finally:
        print(f"releasing {name}")


with managed_resource("database connection") as res:
    print(f"using {res}")
