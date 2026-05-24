"""Lambda expressions and the map/filter/reduce/sorted functional toolkit."""

from functools import reduce

numbers = [5, 3, 8, 1, 9, 2]

# lambda: a small anonymous function, useful inline
square = lambda x: x ** 2
print(square(4))

# map applies a function to every item
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# filter keeps items where the function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# reduce collapses a sequence into a single value
total = reduce(lambda acc, x: acc + x, numbers, 0)
print(total)

# sorted with a key function - very common real-world use of lambda
people = [{"name": "Amina", "age": 30}, {"name": "Davian", "age": 25}]
by_age = sorted(people, key=lambda p: p["age"])
print(by_age)

# These same things are usually clearer as comprehensions - shown for comparison
squared_comprehension = [x ** 2 for x in numbers]
evens_comprehension = [x for x in numbers if x % 2 == 0]
assert squared == squared_comprehension
assert evens == evens_comprehension
