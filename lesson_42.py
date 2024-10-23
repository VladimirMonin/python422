"""
Lesson 42.
ООП Python
Магические методы для арифметических операций
Датаклассы
  - Мутабельность 
  - post_init
  - __slots__
  - field свойства
    - factory
    - default
    - repr False
    - compare False
  - frozen=True
Абстрактные датаклассы и наследование в dataclass
  
"""

# Чем in-place мат. операция отличается от обычной?

"""
In-place операции изменяют исходный объект, а обычные операции создают новый объект с результатом.
Например: a += 1 изменяет a, а a + 1 создает новый объект
"""

# Обычные арифметические операции:
# __add__(self, other) -> +  # сложение
# __sub__(self, other) -> -  # вычитание
# __mul__(self, other) -> *  # умножение
# __truediv__(self, other) -> /  # деление
# __floordiv__(self, other) -> //  # целочисленное деление
# __mod__(self, other) -> %  # остаток от деления
# __pow__(self, other) -> **  # возведение в степень


# In-place операции (с присваиванием):
# __iadd__(self, other) -> +=  # сложение с присваиванием
# __isub__(self, other) -> -=  # вычитание с присваиванием
# __imul__(self, other) -> *=  # умножение с присваиванием
# __itruediv__(self, other) -> /=  # деление с присваиванием
# __ifloordiv__(self, other) -> //=  # целочисленное деление с присваиванием
# __imod__(self, other) -> %=  # остаток от деления с присваиванием
# __ipow__(self, other) -> **=  # возведение в степень с присваиванием

# class Pizza:
#     def __init__(self, size):
#         self.size = size

#     def __add__(self, other):
#         """Создает новую пиццу с суммой размеров"""
#         if not isinstance(other, Pizza):
#             raise TypeError("Можно складывать только пиццы между собой")
#         return Pizza(self.size + other.size)

#     def __iadd__(self, other):
#         """Создает новую пиццу с суммой размеров (in-place операция)"""
#         if not isinstance(other, Pizza):
#             raise TypeError("Можно складывать только пиццы между собой")
#         return Pizza(self.size + other.size)
#     def __str__(self):
#         return f"Пицца размера {self.size} см. ID: {id(self)}"


# Пример использования
# pizza1 = Pizza(30)  # пицца диаметром 30 см
# pizza2 = Pizza(25)  # пицца диаметром 25 см

# Обычное сложение
# pizza3 = pizza1 + pizza2
# print(pizza3)  # Пицца размера 55

# print(pizza1)
# In-place сложение
# pizza1 += pizza2
# print(pizza1)  # Пицца размера 55

### Проверим, а что происходит со строками на инплейс операциях


# product = "чебурек"
# print(id(product))
# product += "из кот"
# print(id(product))

# some_num = 1
# print(id(some_num))
# some_num += 1
# print(id(some_num))

"""
Мутабельность коллекций в Python:

1. Мутабельные (изменяемые) коллекции:
   - list (списки)
   - dict (словари)
   - set (множества)
   Особенности:
   - можно изменять содержимое после создания
   - при модификации сохраняют свой id
   - передаются в функции по ссылке

2. Иммутабельные (неизменяемые) коллекции:
   - tuple (кортежи)
   - frozenset (неизменяемые множества)
   - str (строки)
   Особенности:
   - нельзя изменить после создания
   - при любой модификации создается новый объект с новым id
   - передаются в функции по значению

Пример с list (мутабельный):
"""
# some_list = [1, 2, 3]
# print(id(some_list))  # id сохраняется
# some_list += [4, 5]   # изменяем список
# print(id(some_list))  # id остается тем же

# При работе с изменяемыми коллекциями важно помнить о побочных эффектах
# при передаче их в функции или при создании копий


from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

from hw import data


@dataclass
class AbstractProduct(ABC):
    name: str
    category: str
    price: float
    availability: bool
    


@dataclass
class Electronics(AbstractProduct):
    height: float
    width: float
    depth: float
    weight: float
    warranty_period: int
    stores: list = field(default_factory=list)


@dataclass
class Furniture(AbstractProduct):
    height: float
    width: float
    depth: float
    weight: float
    material: str
    stores: list = field(default_factory=list)


class ShoppingCart:
    def __init__(self):
        self.items: List[AbstractProduct] = []
        self.total: float = 0.0

    def __add__(self, other: AbstractProduct) -> "ShoppingCart":
        if not isinstance(other, AbstractProduct):
            raise TypeError("Можно добавлять только товары")
        if other.availability:
            self.items.append(other)
            self.total += other.price
        return self

    def __sub__(self, other: AbstractProduct) -> "ShoppingCart":
        if not isinstance(other, AbstractProduct):
            raise TypeError("Можно удалять только товары")
        if other in self.items:
            self.items.remove(other)
            self.total -= other.price
        return self

    def __str__(self) -> str:
        cart_contents = "\n".join(
            [f"- {item.name}: {item.price}" for item in self.items]
        )
        return f"Корзина:\n{cart_contents}\nИтого: {self.total}"

shared_stores = ["Остап и КО", "Рога и Копыта", "Сбермаркет"]
# Пример использования:
def create_sample_products():
    tv = Electronics(
        name="Квантовый компьютер",
        category="Суперкомпьютеры",
        price=10000000.0,
        availability=True,
        stores=shared_stores,
        height=2.5,
        width=3.0,
        depth=1.5,
        weight=500.0,
        warranty_period=24,
    )

    sofa = Furniture(
        name="Левитирующий диван",
        category="Мягкая мебель",
        price=300000.0,
        availability=True,
        stores=["Диваны Галактики", "Фабрика Остапа", "Мебельный ад"],
        height=1.0,
        width=2.5,
        depth=1.0,
        weight=50.0,
        material="Антигравитационный текстиль",
    )

    return tv, sofa


# Использование:
cart = ShoppingCart()
tv, sofa = create_sample_products()

# cart += tv  # добавляем телевизор
# print(cart)
# cart += sofa  # добавляем диван
# print(cart)
# cart -= tv  # удаляем телевизор
# print(cart)
# print(tv.stores)
# print(sofa.stores)


electornics = [
    {
        "name": "Голографический проектор",
        "category": "Устройства отображения",
        "height": 0.5,
        "width": 0.5,
        "depth": 0.3,
        "weight": 2.0,
        "availability": True,
        "stores": shared_stores,
        "price": 200000.0,
        "warranty_period": 18,
    },
    {
        "name": "Нейроинтерфейс",
        "category": "Устройства ввода",
        "height": 0.1,
        "width": 0.2,
        "depth": 0.05,
        "weight": 0.1,
        "availability": False,
        "stores": shared_stores,
        "price": 500000.0,
        "warranty_period": 12,
    },
]

electronics = [Electronics(**item) for item in electornics] + [tv]

# Демонстрация проблемы
print("Исходные списки магазинов:")
[print(f"{item.name}: {item.stores}") for item in electronics]

# Изменяем список магазинов у одного объекта
electronics[0].stores.append("ххххххххххххх")

print("\nСписки магазинов после изменения:")
[print(f"{item.name}: {item.stores}") for item in electronics]

# Проблема: изменение списка магазинов у одного объекта отражается на всех объектах
# ПРИ УСЛОВИИ что изначально мы передали магазины в виде переменной, а не самостоятельных списков

# Решение:
# Решение проблемы с изменяемыми значениями по умолчанию в dataclass:

# 1. Используем default_factory из модуля dataclasses
# При определении поля с изменяемым значением (список, словарь и т.д.)
# вместо default используем default_factory, который будет создавать
# новый объект при каждой инициализации класса

# Пример:
# @dataclass
# class Electronics:
#     stores: list = field(default_factory=list)

# Как это работает:
# - default_factory принимает функцию (не вызов функции)
# - при создании каждого нового экземпляра класса
# - default_factory вызывает переданную функцию
# - получаем новый независимый объект для каждого экземпляра

# Преимущества:
# - Каждый экземпляр получает свою копию изменяемого объекта
# - Изменения в одном экземпляре не влияют на другие
# - Решает проблему разделяемых ссылок на изменяемые объекты

# Важно:
# - Работает не только со списками, но и с любыми изменяемыми типами
# - Можно использовать lambda для создания более сложных значений
# - При наследовании поведение сохраняется
# Теперь изменение списка магазинов у одного объекта не влияет на другие объекты

# Параметры field
# - default_factory - функция, которая будет вызываться для создания значения по умолчанию для мутабельных объектов
# default - значение по умолчанию для неизменяемых объектов
# init - будет ли поле инициализироваться при создании экземпляра класса
# repr - будет ли поле включено в строковое представление объекта
# hash - будет ли поле включено в хэш объекта
# compare - будет ли поле включено в сравнения объектов
# metadata - дополнительная информация о поле

# oreder=True - создаст ВСЕ методы сравнений а не только на равенство
@dataclass(order=True)
class User:
    password: str = field(repr=False, compare=False)
    hobbies: list = field(default_factory=list, compare=False, metadata={"help_text": "Ваши хобби"}, init=False)
    username: str = field(default="anonim")

u1 = User("qwerty", "user1")
u1.hobbies.append("football")

print(repr(u1))

@dataclass(order=True)
class Student:
    name: str = field(compare=False)
    age: int


st1 = Student("Константин", 22)
st2 = Student("Ирина", 20)

print(st1 <= st2)

# 