"""Variables, dynamic typing, and type conversion."""

# Python is dynamically typed - a variable's type is inferred at assignment,
# and can change if you reassign it to a different kind of value.
name = "Davian"
age = 25
height_m = 1.75
is_student = True

print(f"{name} is {age} years old, {height_m}m tall, student={is_student}")
print(type(name), type(age), type(height_m), type(is_student))

# Reassignment can change the type - this is legal but usually a code smell.
value = 10
value = "now a string"
print(value, type(value))

# Explicit type conversion (casting)
age_str = "30"
age_int = int(age_str)
pi_str = str(3.14159)
flag = bool(0)      # falsy: 0, 0.0, "", None, [], {}, set()
flag2 = bool(1)      # truthy: anything else

print(age_int + 5, pi_str, flag, flag2)

# None represents "no value" - Python's null
missing = None
print(missing is None)
