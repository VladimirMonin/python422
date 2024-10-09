from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        if len(value) < 2 or len(value) > 50:
            raise ValueError("Длина имени должна быть от 2 до 50 символов")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Возраст должен быть целым числом")
        if value < 0 or value > 150:
            raise ValueError("Возраст должен быть в диапазоне от 0 до 150")
        self._age = value

class SeaAnimalMixin:
    def __init__(self):
        self.can_breathe_underwater = True

    def breathe_underwater(self):
        return f"{self.name} дышит под водой."

    def swim(self):
        return f"{self.name} плавает в воде."

class LandAnimalMixin:
    def __init__(self):
        self.legs = 4

    def walk(self):
        return f"{self.name} ходит на {self.legs} лапах."

    def run(self):
        return f"{self.name} бежит на {self.legs} лапах."

class Cat(Animal, LandAnimalMixin):
    def __init__(self, name: str, age: int, breed: str, color: str):
        Animal.__init__(self, name, age)
        LandAnimalMixin.__init__(self)
        self.breed = breed
        self.color = color

    def make_sound(self):
        return "Мяу!"

class Dog(Animal, LandAnimalMixin):
    def __init__(self, name: str, age: int, breed: str):
        Animal.__init__(self, name, age)
        LandAnimalMixin.__init__(self)
        self.breed = breed

    def make_sound(self):
        return "Гав!"

class Fish(Animal, SeaAnimalMixin):
    def __init__(self, name: str, age: int, species: str):
        Animal.__init__(self, name, age)
        SeaAnimalMixin.__init__(self)
        self.species = species

    def make_sound(self):
        return "Буль-буль!"
    

dog = Dog("Бобик", 5, "Дворняга")
print(dog.walk())
print(dog.run())
print(dog.make_sound())