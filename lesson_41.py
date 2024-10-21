"""
Lesson 41: Магические методы сравнения и математики
Операторы сравния - магический метод
== - __eq__ от equal (равенство)
!= - __ne__ от not equal (не равенство)
< - __lt__ от less than (меньше чем)
> - __gt__ от greater than (больше чем)
<= - __le__ от less or equal (меньше или равно)
>= - __ge__ от greater or equal (больше или равно)

@functools.total_ordering - декоратор, который автоматически достроит все 
методы на базе __eq__ и __lt__ 
from functools import total_ordering


Нужен для старых версий Ptyhon

__eq__ и __lt__ и __le__ минимальный набор, на базе которого современная версия 
языка допишет остальные методы (Т.е. один метод равно или не равно + больше или меньше + больше равно или меньше равно)
"""

"""

"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

electronics_data = [
    {
        "name": "Квантовый компьютер",
        "category": "Суперкомпьютеры",
        "height": 2.5,
        "width": 3.0,
        "depth": 1.5,
        "weight": 500.0,
        "availability": True,
        "price": 10000000.0,
        "warranty_period": 24
    },
    {
        "name": "Нейроинтерфейс",
        "category": "Устройства ввода",
        "height": 0.1,
        "width": 0.2,
        "depth": 0.05,
        "weight": 0.1,
        "availability": False,
        "price": 500000.0,
        "warranty_period": 12
    },
    {
        "name": "Голографический проектор",
        "category": "Устройства отображения",
        "height": 0.5,
        "width": 0.5,
        "depth": 0.3,
        "weight": 2.0,
        "availability": True,
        "price": 200000.0,
        "warranty_period": 18
    },
    {
        "name": "Антигравитационная платформа",
        "category": "Транспортные средства",
        "height": 0.3,
        "width": 1.5,
        "depth": 1.5,
        "weight": 50.0,
        "availability": True,
        "price": 1000000.0,
        "warranty_period": 36
    },
    {
        "name": "Телепортационная капсула",
        "category": "Транспортные средства",
        "height": 2.2,
        "width": 1.0,
        "depth": 1.0,
        "weight": 300.0,
        "availability": False,
        "price": 5000000.0,
        "warranty_period": 60
    }
]

furniture_data = [
    {
        "name": "Левитирующий диван",
        "category": "Мягкая мебель",
        "height": 1.0,
        "width": 2.5,
        "depth": 1.0,
        "weight": 50.0,
        "availability": True,
        "price": 300000.0,
        "material": "Антигравитационный текстиль"
    },
    {
        "name": "Стол-трансформер",
        "category": "Офисная мебель",
        "height": 0.8,
        "width": 1.5,
        "depth": 0.8,
        "weight": 30.0,
        "availability": True,
        "price": 150000.0,
        "material": "Умный пластик"
    },
    {
        "name": "Шкаф-невидимка",
        "category": "Системы хранения",
        "height": 2.2,
        "width": 1.5,
        "depth": 0.6,
        "weight": 100.0,
        "availability": False,
        "price": 500000.0,
        "material": "Метаматериал"
    },
    {
        "name": "Кровать-симулятор невесомости",
        "category": "Мягкая мебель",
        "height": 0.5,
        "width": 2.0,
        "depth": 2.0,
        "weight": 200.0,
        "availability": True,
        "price": 800000.0,
        "material": "Память формы"
    },
    {
        "name": "Кресло-телепорт",
        "category": "Мягкая мебель",
        "height": 1.2,
        "width": 1.0,
        "depth": 1.0,
        "weight": 80.0,
        "availability": True,
        "price": 1200000.0,
        "material": "Квантовая пена"
    }
]

@dataclass
class Furniture:
    name: str
    category: str
    height: float
    width: float
    depth: float
    weight: float
    availability: bool
    price: float
    material: str
    store: str = "Галактика диванов"

    def __str__(self):
        """
        Возвращает название, цену и магазин
        """
        return f"{self.name} - {self.price} - {self.store}"
    
    def __bool__(self):
        """
        Возвращает доступность товара
        """
        return self.availability


furniture_list = [Furniture(**item) for item in furniture_data]

# Создаем в отдельную переменную Кресло-телепорт
chair = furniture_list[4]

# Проверяем на равенство
print(chair == furniture_list[4])

# Вызовим repr 
string = repr(chair)
print(string)

# Вызовим eval
print(eval(string))