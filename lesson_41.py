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

__eq__ и __lt__ минимальный набор, на базе которого современная версия 
языка допишет остальные методы
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

