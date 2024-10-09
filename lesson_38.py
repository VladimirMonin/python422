"""
Этот модуль содержит пример реализации абстрактного базового класса Animal и примеси SeaAnimalMixin.

Классы:
- Animal: Абстрактный базовый класс для представления животных.
  - Атрибуты:
    - name (str): Имя животного (от 2 до 50 символов).
    - age (int): Возраст животного (от 0 до 150 лет).
  - Методы:
    - make_sound(): Абстрактный метод для издания звука животным.

- SeaAnimalMixin: Примесь для добавления функциональности морских животных.

Этот модуль демонстрирует:
1. Использование абстрактных классов и методов (ABC, abstractmethod).
2. Применение свойств (property) для контроля доступа к атрибутам.
3. Валидацию данных при установке значений атрибутов.
4. Использование аннотаций типов.
5. Применение примесей (mixins) для расширения функциональности классов.

Пример используется в образовательных целях для изучения объектно-ориентированного 
программирования в Python, в частности, для демонстрации концепций наследования, 
инкапсуляции и полиморфизма.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    
    """
    Абстрактный базовый класс для представления животных.

    Атрибуты:
    - name (str): Имя животного. Должно быть строкой длиной от 2 до 50 символов.
    - age (int): Возраст животного. Должно быть целым числом от 0 до 150.

    Методы:
    - make_sound(): Абстрактный метод для издания звука животным.
    """
    
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
    """
    Миксин для морских животных.

    Атрибуты:
    - can_breathe_underwater (bool): Способность дышать под водой.

    Методы:
    - breathe_underwater(): Метод, описывающий дыхание под водой.
    - swim(): Метод, описывающий плавание в воде.
    """
    
    def __init__(self):
        self.can_breathe_underwater = True

    def breathe_underwater(self):
        return f"{self.name} дышит под водой."

    def swim(self):
        return f"{self.name} плавает в воде."

class LandAnimalMixin:
    """
        Миксин для наземных животных.
    
        Атрибуты:
        - legs (int): Количество лап у животного.
    
        Методы:
        - walk(): Метод, описывающий ходьбу животного.
        - run(): Метод, описывающий бег животного.
        """
    
    def __init__(self):
        self.legs = 4

    def walk(self):
        return f"{self.name} ходит на {self.legs} лапах."

    def run(self):
        return f"{self.name} бежит на {self.legs} лапах."

class Cat(Animal, LandAnimalMixin):
    """
        Класс, представляющий кошку.
    
        Наследует от классов Animal и LandAnimalMixin.
    
        Атрибуты:
        - name (str): Имя кошки.
        - age (int): Возраст кошки.
        - breed (str): Порода кошки.
        - color (str): Цвет кошки.
        - legs (int): Количество лап (наследуется от LandAnimalMixin).
    
        Методы:
        - make_sound(): Возвращает звук, издаваемый кошкой.
        - walk(): Наследуется от LandAnimalMixin, описывает ходьбу кошки.
        - run(): Наследуется от LandAnimalMixin, описывает бег кошки.
        """
    
    def __init__(self, name: str, age: int, breed: str, color: str):
        Animal.__init__(self, name, age)
        LandAnimalMixin.__init__(self)
        self.breed = breed
        self.color = color

    def make_sound(self):
        return "Мяу!"

class Dog(Animal, LandAnimalMixin):
    """
        Класс, представляющий собаку.
    
        Наследует от классов Animal и LandAnimalMixin.
    
        Атрибуты:
        - name (str): Имя собаки.
        - age (int): Возраст собаки.
        - breed (str): Порода собаки.
        - legs (int): Количество лап (наследуется от LandAnimalMixin).
    
        Методы:
        - make_sound(): Возвращает звук, издаваемый собакой.
        - walk(): Наследуется от LandAnimalMixin, описывает ходьбу собаки.
        - run(): Наследуется от LandAnimalMixin, описывает бег собаки.
        """
    
    def __init__(self, name: str, age: int, breed: str):
        Animal.__init__(self, name, age)
        LandAnimalMixin.__init__(self)
        self.breed = breed

    def make_sound(self):
        return "Гав!"

class Fish(Animal, SeaAnimalMixin):
    """
        Класс, представляющий рыбу.
    
        Наследует от классов Animal и SeaAnimalMixin.
    
        Атрибуты:
        - name (str): Имя рыбы.
        - age (int): Возраст рыбы.
        - species (str): Вид рыбы.
        - fins (int): Количество плавников (наследуется от SeaAnimalMixin).
    
        Методы:
        - make_sound(): Возвращает звук, издаваемый рыбой.
        - swim(): Наследуется от SeaAnimalMixin, описывает плавание рыбы.
        """
    
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