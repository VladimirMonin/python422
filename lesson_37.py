"""
Lesson 37: Наследование
Все классы в Python наследуются от базового класса object.
"""

class Animal:
    animal_attrs = ['name', 'color', 'age', 'weight', 'favorite_toy']
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            self.validate_attr(key)
            setattr(self, key, value)

    def validate_attr(self, attr_name):
        if attr_name not in self.animal_attrs:
            raise ValueError(f'Атрибут {attr_name} не поддерживается классом {self.__class__.__name__}')

    

class Cat(Animal):
    def __init__(self, name, color, **kwargs):
        super().__init__(name, **kwargs)
        self.color = color

# Пример использования
# cat = Cat("Беляш", "Рыжий", age=3, weight=4.5, favoriteToy="мячик")
# print(cat)

cats_list = [
    {
        "name": "Барсик",
        "color": "Рыжий",
        "age": 3,
        "weight": 4.5,
        "favorite_toy": "мячик"
    },
    {
        "name": "Мурзик",
        "color": "Серый",
        "age": 2,
        "weight": 3.5,
        "favorite_toy": "клубок"
    }, {
        "name": "Мурка",
        "color": "Черный",
        "age": 1,
        "favorite_toy": "Мурзик"
    }
]

cats = [Cat(**cat_data) for cat_data in cats_list]
for cat in cats:
    print(cat)

cats[2].__delattr__("favorite_toy")
print(cats[2].__dir__())
print(cats[2].__dict__) # выводит словарь атрибутов
"""
Методы для работы с атрибутами
__getattr__ - добывает атрибуты
__setattr__ - устанавливает атрибуты
__delattr__ - удаляет атрибуты

__dir__ - возвращает список методов (Все целиком)
__dict__ - возвращает словарь атрибутов

"""