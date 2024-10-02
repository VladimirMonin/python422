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
    def __init__(self, name: str, age: int):
        self.__name = name
        self._age = age

    def __get_info_sring(self):
        return f'{self.__name} - {self._age}'
    
    def show_info(self):
        info = self.__get_info_sring()
        print(info)


p = Person('Bob', 20)
p._Person__name
# p.__get_info_sring() # AttributeError: 'Person' object has no attribute '_Person__get_info_sring'
# result = p._Person__get_info_sring()
# print(result)
p.show_info()