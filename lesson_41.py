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

# Импорт total ordering
from functools import total_ordering

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __eq__(self, other: 'Employee') -> bool:
            if not isinstance(other, Employee):
                raise TypeError('Класс Employee можно сравнивать только с экземплярами класса Employee')
            return self.salary == other.salary
    
    def __lt__(self, other: 'Employee') -> bool:
            if not isinstance(other, Employee):
                raise TypeError('Класс Employee можно сравнивать только с экземплярами класса Employee')
            return self.salary < other.salary
    
    def __le__(self, other: 'Employee') -> bool:
            if not isinstance(other, Employee):
                raise TypeError('Класс Employee можно сравнивать только с экземплярами класса Employee')
            return self.salary <= other.salary

    def __repr__(self):
        return f'{self.name} - {self.salary}'


employers = [
    {
        'name': 'Николаич',
        'salary': 200000
    },
    {
        'name': 'Иваныч',
        'salary': 200000
    }
]

employers_objs = [Employee(e['name'], e['salary']) for e in employers]
employee1, employee2 = employers_objs

print(employee1 == employee2) # == __eq__ вызывается под капотом

print(employee1 is employee2) # is сравнивает адреса в памяти

print(employee1 != employee2) # == __eq__ вызывается под капотом

print(employee1 >= employee2) 

"""
Практика!
Попробуйте создать класс Product принмающий аргументы name, price, catagory 
и реализовать магические методы сравнения для этого класса на основе цены
"""

products = [
    {"name": "Ноутбук Lenovo ThinkPad", "price": 89999.99, "category": "Ноутбуки"},
    {"name": "Смартфон Samsung Galaxy S21", "price": 69999.50, "category": "Телефоны"},
    {"name": "Холодильник LG", "price": 54999.00, "category": "Бытовая электроника"},
    {"name": "Ноутбук Apple MacBook Air", "price": 99999.99, "category": "Ноутбуки"},
    {"name": "Смартфон iPhone 13", "price": 79999.99, "category": "Телефоны"},
    {"name": "Стиральная машина Bosch", "price": 39999.50, "category": "Бытовая электроника"},
    {"name": "Ноутбук ASUS ROG", "price": 129999.00, "category": "Ноутбуки"},
    {"name": "Смартфон Xiaomi Redmi Note 10", "price": 19999.99, "category": "Телефоны"},
    {"name": "Микроволновая печь Samsung", "price": 9999.50, "category": "Бытовая электроника"},
    {"name": "Ноутбук HP Pavilion", "price": 59999.00, "category": "Ноутбуки"}
]

class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __eq__(self, other: 'Product') -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other: 'Product') -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other: 'Product') -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price <= other.price
    

# Десериализация - процесс преобразования данных из внешнего представления в рабочий формат.
products = [Product(p['name'], p['price'], p['category']) for p in products]


# это позволит сделать сортировку объектов Product.
# Давайте проверим:

sorted_products = sorted(products)

print("Отсортированные продукты по цене:")
for product in sorted_products:
    print(f"{product.name}: {product.price}")

print("Отсортированные продукты по названию:")
# Давайте сортиртировать это по алфавиту (через лямбду)
sorted_products = sorted(products, key=lambda product: product.name) # .split()[0] - чтобы сделать это по первому слову
[print(product.name) for product in sorted_products]


print('Сортируем по 2 признакам, категория, и цена')

sorted_products = sorted(products, key=lambda product: (product.category, product.price))
[print(product.name, product.category, product.price) for product in sorted_products]