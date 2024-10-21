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

class AbstractProduct(ABC):
    def __init__(self, name: str, category: str, height: float, width: float, depth: float, weight: float, availability: bool, price: float):
        self.name = name
        self.category = category
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.availability = availability
        self.price = price

    def __bool__(self) -> bool:
        """
        Возвращает наличие товара в продаже.
        """
        return self.availability

    def __len__(self) -> float:
        """
        Возвращает суммарные габаритные характеристики (например, объем).
        """
        return self.weight / (self.height + self.width + self.depth)

    def __eq__(self, other: 'AbstractProduct') -> bool:
        if not isinstance(other, AbstractProduct):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other: 'AbstractProduct') -> bool:
        if not isinstance(other, AbstractProduct):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other: 'AbstractProduct') -> bool:
        if not isinstance(other, AbstractProduct):
            return NotImplemented
        return self.price <= other.price

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Electronics(AbstractProduct):
    def __init__(self, name: str, category: str, height: float, width: float, depth: float, weight: float, availability: bool, price: float, warranty_period: int):
        super().__init__(name, category, height, width, depth, weight, availability, price)
        self.warranty_period = warranty_period  # Гарантийный срок в месяцах

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price} руб., Гарантия: {self.warranty_period} месяцев"
    
    def __repr__(self):
        return f"Electronics(name='{self.name}', category='{self.category}', height={self.height}, width={self.width}, depth={self.depth}, weight={self.weight}, availability={self.availability}, price={self.price}, warranty_period={self.warranty_period})"



class Furniture(AbstractProduct):
    def __init__(self, name: str, category: str, height: float, width: float, depth: float, weight: float, availability: bool, price: float, material: str):
        super().__init__(name, category, height, width, depth, weight, availability, price)
        self.material = material  # Материал изготовления

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price} руб., Материал: {self.material}"
    
    def __repr__(self):
        return f"Furniture(name='{self.name}', category='{self.category}', height={self.height}, width={self.width}, depth={self.depth}, weight={self.weight}, availability={self.availability}, price={self.price}, material='{self.material}')"

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


electronics_products = [Electronics(**data) for data in electronics_data]
furniture_products = [Furniture(**data) for data in furniture_data]

# правльный репр будет возвращать "Furniture(name=Левитирующий диван, category=Мягкая мебель, height=1.0, width=2.5, depth=1.0, weight=50.0, availability=True, price=300000.0, material=Антигравитационный текстиль)"

quantum_computer  = electronics_products[0]
levitating_sofa = furniture_products[0]

# Сериализация объектов в строку с помощью repr()
quantum_computer_str = repr(quantum_computer)
levitating_sofa_str = repr(levitating_sofa)

print(quantum_computer_str)
print(levitating_sofa_str)

# Десериализация объектов из строки с помощью eval()
quantum_computer_obj = eval(quantum_computer_str)
levitating_sofa_obj = eval(levitating_sofa_str)
eval("print('Привет из eval!')")

print(quantum_computer_obj)
print(levitating_sofa_obj)