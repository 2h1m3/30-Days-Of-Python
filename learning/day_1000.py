class Animal:
    def __init__(self, name, species):
        self._name = name       # Encapsulation: using a protected attribute
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")  # Abstraction

    def __str__(self):
        return f"{self._name} is a {self.species}"

class Dog(Animal):  # Inheritance
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):  # Polymorphism
        return "Woof!"

class Cat(Animal):  # Inheritance
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):  # Polymorphism
        return "Meow!"

# Creating instances of Dog and Cat
dog = Dog(name="Rex", breed="German Shepherd")
cat = Cat(name="Whiskers", breed="Siamese")

# Printing information and sounds
print(dog)                # Output: Rex is a Dog
print(dog.make_sound())   # Output: Woof!
print(cat)                # Output: Whiskers is a Cat
print(cat.make_sound())   # Output: Meow!
