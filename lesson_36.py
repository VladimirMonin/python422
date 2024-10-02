"""
Lesson 36: Инкапсуляция
- Методы класса, статик методы
- Приватные, защищенные и публичные атрибуты класса
- Приватные, заащищенные и публичные методы класса
- Геттеры и сеттеры
- All Any
- Полиморфизм


Практика: pytybefix - библиотека для выгрузки видео с ютуба
"""


class Cat():
    def get_voise(self):
        return 'meow'
    

class Dog():
    def get_voise(self):
        return 'woof'
    

class Hamster():
    def get_voise(self):
        return f"squeak"
    

cats = [Cat() for i in range(10)]
dogs = [Dog() for i in range(5)]
hamsters = [Hamster() for i in range(20)]

all_animals = cats + dogs + hamsters

[print(animal.get_voise()) for animal in all_animals]