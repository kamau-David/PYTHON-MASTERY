"""Lists (mutable, ordered) vs tuples (immutable, ordered)."""

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(1, "blueberry")
fruits.remove("banana")
print(fruits)

# Slicing: [start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])     # [2, 3, 4]
print(numbers[:3])      # from start
print(numbers[-3:])     # last 3
print(numbers[::2])     # every 2nd
print(numbers[::-1])    # reversed

# Tuples: immutable, often used for fixed-size records
point = (3, 4)
x, y = point            # unpacking
print(f"x={x}, y={y}")

try:
    point[0] = 99
except TypeError as e:
    print("can't mutate a tuple:", e)

# Lists are mutable and passed by reference
def add_item(lst):
    lst.append("mutated!")

original = ["a", "b"]
add_item(original)
print(original)   # the caller sees the mutation
