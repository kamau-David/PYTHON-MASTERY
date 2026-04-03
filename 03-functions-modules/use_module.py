"""Demonstrates importing a locally-defined module."""

import math_utils
from math_utils import factorial, PI

print(math_utils.is_prime(17))
print(factorial(5))
print(PI)

# Importing the standard library the same way
import math
print(math.sqrt(2))
