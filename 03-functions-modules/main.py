"""Entry point tying functions and modules together."""

from math_utils import is_prime, factorial

def primes_up_to(limit):
    return [n for n in range(2, limit) if is_prime(n)]

def main():
    print("Primes up to 30:", primes_up_to(30))
    print("5! =", factorial(5))

if __name__ == "__main__":
    main()
