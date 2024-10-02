"""
Lesson 36: Инкапсуляция
- Методы класса, статик методы
- Приватные, защищенные и публичные атрибуты класса
- Приватные, заащищенные и публичные методы класса
- Геттеры и сеттеры


Практика: pytybefix - библиотека для выгрузки видео с ютуба
"""

"""
У нас есть возможность спрятать атрибуты или методы класса, чтобы закрыть доступ к ним извне.
Обычные методы и классы = public (открытые)
__ - private (закрытые полностью) доступны только внутри класса
_ - protected (защищенные) доступны внутри класса, а также в наследниках.
"""

class Person():
    def __init__(self, first_name: str, last_name: str, age: int, passport_number: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__passport_number = passport_number

    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def passport_number(self):
        # Логирование, или другая логика
        return f"{self.__passport_number}"
    
    @passport_number.setter
    def passport_number(self, passport_number: str):
        is_all_digit= all(char.isdigit() for char in passport_number.replace(' ', ''))
        if is_all_digit:
            self.__passport_number = passport_number
        else:
            raise ValueError("Неверный формат паспорта")
    
    
p = Person('Bob', 'Bobov', 20, '123456789')
print(p)
print(p.passport_number)
p.passport_number = '98765  43231'
print(p.passport_number)

