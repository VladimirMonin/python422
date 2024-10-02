"""
Lesson 36: Инкапсуляция
- Методы класса, статик методы
- Приватные, защищенные и публичные атрибуты класса
- Приватные, заащищенные и публичные методы класса
- Геттеры и сеттеры


Практика: pytybefix - библиотека для выгрузки видео с ютуба
"""

class Cat():
    types = ['дворянин', 'мэйнкун', 'питерская карнавальская']
    def __init__(self, name:str):
        self.name = name
        

    @staticmethod
    def get_human_age(age: int) -> int:
        return age * 7
    
    @classmethod
    def add_new_type(cls, new_type: str):
        # Тут может быть серия проверок!
        cls.types.append(new_type)
        print(cls.__name__)

    

cat = Cat("Мурзик")
print(cat.types)
cat.add_new_type('вислоухий скотиш')
print(cat.types)
cat1 = Cat("Кот")
print(cat1.types)