"""
Lesson 38 - Наследование
- Варианты наследования (Иерархическое, множественное)
- Абстрактный класс и абстрактные методы
- Конфликты
- MRO
- Миксины
"""
# Импорт ABC
from abc import ABC, abstractmethod

class AbstractMatroyshka(ABC):

    @abstractmethod
    def open(self):
        pass



class BigMatryoshka(AbstractMatroyshka):
    count = 0
    def __init__(self, big_size: int):
        # BigMatryoshka.count += 1
        self.size = big_size
        self.__class__.count += 1
        self.id = self.__class__.count
        print(f"Создана большая матрёшка с ID {self.id}")

    @classmethod
    def get_count(cls):
        return f'Класс {cls.__name__} создал {cls.count} матрешек'
    
    def __str__(self):
        """
        Универсальный str который вернет все атрибуты этого экземпляра
        """
        attrs = [f'{attr}: {getattr(self, attr)}' for attr in self.__dict__.keys()]
        return f'{self.__class__.__name__}: {", ".join(attrs)}'
    
    def open(self):
        print(f"Открываю матрёшку {self.__class__.__name__} с ID {self.id}")


class MediumMatryoshka(BigMatryoshka):
    count = 0
    def __init__(self, medium_size: int, big_size: int):
        self.size = medium_size
        self.__class__.count += 1
        self.id = self.__class__.count
        self.big_matryoshka = BigMatryoshka(big_size)
        print(f"Создана средняя матрёшка с ID {self.id}")

    def open(self):
        self.big_matryoshka.open()
        print(f"Открываю матрёшку {self.__class__.__name__} с ID {self.id}")
        


class SmallMatryoshka(MediumMatryoshka):
    count = 0
    def __init__(self, small_size: int, medium_size: int, big_size: int):
        self.size = small_size
        self.__class__.count += 1
        self.id = self.__class__.count
        self.medium_matryoshka = MediumMatryoshka(medium_size=medium_size, big_size=big_size)
        print(f"Создана маленькая матрёшка. ID {self.id}")

    def open(self):
        self.medium_matryoshka.open()
        print(f"Открываю матрёшку {self.__class__.__name__} с ID {self.id}")



sm = SmallMatryoshka(10, 20, 30)
smed = MediumMatryoshka(20, 30)
sb = BigMatryoshka(50)

sm.open()
# smed.open()
# sb.open()