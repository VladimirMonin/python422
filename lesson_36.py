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
    
    def get_passport_data(self):
        # Логирование, или другая логика
        return f"{self.__passport_number}"
    
    def set_passport_data(self, passport_number: str):
        is_all_digit= all(char.isdigit() for char in passport_number.replace(' ', ''))
        if is_all_digit:
            self.__passport_number = passport_number
        else:
            raise ValueError("Неверный формат паспорта")
    
    
p = Person('Bob', 'Bobov', 20, '123456789')
print(p)
print(p.get_passport_data())
p.set_passport_data('9876543231')

# p.passport_number = 'sdfsdf'