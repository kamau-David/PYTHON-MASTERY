"""A small reusable module - demonstrates organizing code for import."""

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

PI = 3.14159265358979

if __name__ == "__main__":
    # This block only runs when math_utils.py is executed directly,
    # NOT when it's imported by another file.
    print("Running math_utils.py directly - primes under 20:")
    print([n for n in range(20) if is_prime(n)])
