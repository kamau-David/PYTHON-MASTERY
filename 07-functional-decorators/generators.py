"""Generator functions: yield produces values lazily, one at a time,
instead of building an entire list in memory."""

def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1


for n in count_up_to(5):
    print("counting:", n)

gen = count_up_to(3)
print(next(gen), next(gen), next(gen))
try:
    next(gen)
except StopIteration:
    print("generator exhausted")


def fibonacci():
    """An infinite generator - only safe because we consume it lazily."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
first_ten = [next(fib) for _ in range(10)]
print(first_ten)


# Lazy pipelines: chaining generators processes one item at a time through
# the whole pipeline, rather than materializing intermediate lists.
def read_lines(lines):
    for line in lines:
        yield line.strip()

def non_empty(lines):
    for line in lines:
        if line:
            yield line

def upper(lines):
    for line in lines:
        yield line.upper()

raw = ["  hello  ", "", "world", "   "]
pipeline = upper(non_empty(read_lines(raw)))
print(list(pipeline))
