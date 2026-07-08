"""List, dict, and set comprehensions, plus generator expressions."""

numbers = range(1, 11)

# List comprehension: [expression for item in iterable if condition]
squares = [n ** 2 for n in numbers]
evens_squared = [n ** 2 for n in numbers if n % 2 == 0]
print(squares)
print(evens_squared)

# Dict comprehension
square_map = {n: n ** 2 for n in numbers}
print(square_map)

# Set comprehension - dedupes automatically
lengths = {len(word) for word in ["hi", "hey", "yo", "sup", "hi"]}
print(lengths)

# Generator expression - lazy, doesn't build the whole list in memory.
# Great for large datasets you only need to iterate once.
gen = (n ** 2 for n in numbers)
print(next(gen), next(gen))       # pulls values one at a time
print(sum(n ** 2 for n in numbers))  # sum never materializes a full list

# Nested comprehension: flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [value for row in matrix for value in row]
print(flat)
