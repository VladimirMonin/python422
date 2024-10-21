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
Давайте сделаем два класса которые представляют разные категории продукции в инт. магазине
Electronics - электроника
Furniture - мебель

Опишем логику сравнения 
"""

class Electronics:
    def __init__(self, name: str, price: float, warranty_period: int):
        self.name = name
        self.price = price
        self.warranty_period = warranty_period  # Гарантийный срок в месяцах


class Furniture:
    # атрибукт класса содержащий классы, с кем мы можем делать сравнение
    

    def __init__(self, name: str, price: float, material: str):
        self.name = name
        self.price = price
        self.material = material  # Материал изготовления
        self.comparison_classes = (Electronics, Furniture)


    def __eq__(self, other) -> bool:
        """
        тут может быть более сложная логика сравния, и она может быть разной для разных классов
        """
        if not any(isinstance(other, class_name) for class_name in self.comparison_classes):
            return NotImplemented
        
        if not hasattr(other, 'price'):
            return NotImplemented
        return self.price == other.price
    

f1 = Furniture('Стол', 1000, 'Дерево')
f2 = Furniture('Стул', 1000, 'Дерево')

e1 = Electronics('Телефон', 1000, 12)
print(f1==f2)
print(f1==e1)

print(e1==f1)