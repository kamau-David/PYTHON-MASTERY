"""Inheritance, super(), and method overriding."""

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("subclasses must implement speak()")

    def introduce(self) -> str:
        return f"I am {self.name} and I say {self.speak()}"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


class ServiceDog(Dog):
    def __init__(self, name: str, handler: str):
        super().__init__(name)   # call the parent's __init__
        self.handler = handler

    def introduce(self) -> str:
        # extend the parent behavior rather than fully replacing it
        base = super().introduce()
        return f"{base} (working with handler {self.handler})"


animals = [Dog("Rex"), Cat("Whiskers"), ServiceDog("Buddy", "Davian")]
for animal in animals:
    print(animal.introduce())

# isinstance respects the inheritance chain
print(isinstance(animals[2], Dog))     # True
print(isinstance(animals[2], Animal))  # True
print(isinstance(animals[1], Dog))     # False
