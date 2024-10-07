"""
Lesson 37: Наследование
Все классы в Python наследуются от базового класса object.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Это {self.__class__.__name__} с именем {self.name}'
    
    def voise(self):
        print(f'{self.name} издает звук')


class Cat(Animal):
    def __init__ (self, name, color):
        self.color = color
        super().__init__(name)
    def voise(self):
        # Вызовем метод родителя через super()
        super().voise()
        # Это можно сделать и напрямую
        # Animal.voise(self)
        print(f'{self.name} мяукает')

animal = Animal("Животное")
cat = Cat("Беляш", "Рыжий")
print(cat)
cat.voise()