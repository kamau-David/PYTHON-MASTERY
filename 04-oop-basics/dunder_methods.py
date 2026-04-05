"""Dunder (double underscore) / magic methods - how Python objects hook into
built-in behavior like printing, equality, and operators."""

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        """Called by print() and str() - human-readable representation."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Called in the REPL/debugger - should be unambiguous."""
        return f"Vector(x={self.x!r}, y={self.y!r})"

    def __eq__(self, other):
        """Called by ==."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """Called by +. Lets us write v1 + v2."""
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        """Called by len(). Here we define it as the magnitude, rounded."""
        return round((self.x ** 2 + self.y ** 2) ** 0.5)


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)                  # uses __str__
print(v1 == Vector(1, 2))  # uses __eq__
print(v1 + v2)             # uses __add__
print(len(v2))             # uses __len__
