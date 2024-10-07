"""
Lesson 37: Наследование
Все классы в Python наследуются от базового класса object.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Это {self.__class__.__name__} с именем {self.name}'

class Cat(Animal):
    
    def voise(self):
        print(f'{self.name} мяукает')

animal = Animal("Животное")
cat = Cat("Беляш")
print(cat)
cat.voise()