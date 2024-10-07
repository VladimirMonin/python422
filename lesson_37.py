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
        
    def __str__(self):
        """
        Универсальный метод для вывода информации о животном
        Выводит циклом по атрибутам и их значениям все данные
        """
        attrs = [f'{attr}: {getattr(self, attr)}' for attr in self.__dict__.keys()]
        return f'{self.__class__.__name__}: {", ".join(attrs)}'

    

class Cat(Animal):
    def __init__(self, name, color, **kwargs):
        super().__init__(name, **kwargs)
        self.color = color


class Dog(Animal):
    def __init__(self, name, color, dog_type, **kwargs):
        super().__init__(name, **kwargs)
        self.color = color
        self.dog_type = dog_type


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


dog = Dog("Шарик", "Рыжий", "Дворняга", age=2, weight=10.5, favorite_toy="тарелка")
print(dog)