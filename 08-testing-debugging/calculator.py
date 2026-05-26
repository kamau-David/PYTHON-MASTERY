"""A small module with deliberately simple, testable functions."""

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
