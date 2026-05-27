"""The same tests, written pytest-style - plain functions and assert,
no class or self.assertX boilerplate needed."""

import pytest
from calculator import add, divide, is_palindrome

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(10, 0)

# Parametrized test - runs once per (input, expected) pair, no loop needed
@pytest.mark.parametrize("text,expected", [
    ("racecar", True),
    ("hello", False),
    ("Was it a car or a cat I saw".replace(" ", ""), True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected
