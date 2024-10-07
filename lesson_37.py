"""
Lesson 37: Наследование
Все классы в Python наследуются от базового класса object.
"""
class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    pass

animal = Animal("Животное")
cat = Cat("Кот")