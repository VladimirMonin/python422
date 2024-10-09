"""
Lesson 38 - Наследование
- Варианты наследования (Иерархическое, множественное)
- Абстрактный класс и абстрактные методы
- Конфликты
- MRO
- Миксины
"""
# Импорт ABC
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    # Абстрактный метод
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
    

class Cat(Animal):
    def __init__(self, name: str, age: int, breed: str, color: str):
        super().__init__(name, age)
        self.breed = breed
        self.color = color

    def make_sound(self):
        return "Мяу!"

