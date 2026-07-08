"""Operators: arithmetic, comparison, logical, and the walrus operator."""

a, b = 17, 5

# Arithmetic
print(a + b, a - b, a * b, a / b)   # / always returns float
print(a // b, a % b, a ** b)        # floor division, modulo, exponent

# Comparison returns bool
print(a > b, a == b, a != b)

# Logical operators short-circuit
print(True and False, True or False, not True)

# Walrus operator (:=) - assign and use a value in one expression
# Useful to avoid computing something twice.
data = [1, 2, 3, 4, 5, 6]
if (n := len(data)) > 3:
    print(f"list has {n} items, which is more than 3")
