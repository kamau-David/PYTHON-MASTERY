"""Decorators: functions that wrap other functions to add behavior."""

import functools
import time

def timer(func):
    """A decorator that prints how long the wrapped function took to run."""
    @functools.wraps(func)   # preserves the original function's name/docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))


slow_sum(1_000_000)


def retry(times=3):
    """A decorator FACTORY - takes arguments and returns a decorator.
    This is why it needs an extra layer of nesting."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"attempt {attempt} failed: {e}")
            raise last_error
        return wrapper
    return decorator


call_count = 0

@retry(times=3)
def flaky_operation():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ValueError("simulated failure")
    return "success"


print(flaky_operation())


# Stacking multiple decorators - applied bottom-up
@timer
@retry(times=2)
def combined_example():
    return sum(range(500_000))

combined_example()
