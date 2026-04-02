"""Function definitions: defaults, *args, **kwargs, and scope."""

def greet(name, greeting="Hello"):
    """Default argument - greeting is optional."""
    return f"{greeting}, {name}!"

print(greet("Davian"))
print(greet("Davian", greeting="Karibu"))

def sum_all(*args):
    """*args collects any number of positional arguments into a tuple."""
    return sum(args)

print(sum_all(1, 2, 3, 4))

def build_profile(**kwargs):
    """**kwargs collects keyword arguments into a dict."""
    return kwargs

print(build_profile(name="Davian", role="student", years=3))

def combined(required, *args, default="x", **kwargs):
    """You can mix all of these - order matters: positional, *args, keyword
    defaults, **kwargs."""
    return required, args, default, kwargs

print(combined(1, 2, 3, default="y", extra="z"))

# Scope: local vs global
counter = 0

def increment():
    global counter   # without this, Python would create a new local variable
    counter += 1

increment()
increment()
print("counter:", counter)

# Functions are first-class objects - can be passed around, returned, stored
def apply_twice(fn, value):
    return fn(fn(value))

print(apply_twice(lambda x: x * 2, 3))   # (3*2)*2 = 12
