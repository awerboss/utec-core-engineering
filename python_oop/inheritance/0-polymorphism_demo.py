
#!/usr/bin/env python3
"""Demonstrate inheritance and polymorphism with animals."""


class Animal:
    """Represent an animal with a basic sound."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog that inherits from Animal."""

    def speak(self):
        """Return the sound of a dog."""
        return "Woof"


class Cat(Animal):
    """Represent a cat that inherits from Animal."""

    def speak(self):
        """Return the sound of a cat."""
        return "Meow"


def main():
    """Demonstrate method overriding and class relationships."""
    dog = Dog()
    cat = Cat()

    print(dog.speak())
    print(cat.speak())

    print("--")

    animals = [Dog(), Cat(), Dog()]

    for animal in animals:
        print(animal.speak())

    print("--")

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))


if __name__ == "__main__":
    main()
