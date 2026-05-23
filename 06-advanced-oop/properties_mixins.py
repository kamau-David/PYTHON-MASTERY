"""@property for computed/validated attributes, and mixin classes for
sharing behavior across unrelated class hierarchies."""

class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        # computed on access - not stored, always in sync with celsius
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print(t.celsius, t.fahrenheit)
t.celsius = 30           # goes through the setter's validation
print(t.fahrenheit)


class JSONExportMixin:
    """A mixin adds reusable behavior to any class that includes it -
    it's not meant to be instantiated on its own."""
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class LoggingMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")


class User(JSONExportMixin, LoggingMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email


u = User("Davian", "davian@example.com")
u.log("user created")
print(u.to_json())
