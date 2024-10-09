"""
Lesson 38 - Наследование
- Варианты наследования (Иерархическое, множественное)
- Абстрактный класс и абстрактные методы
- Конфликты
- MRO
- Миксины
"""

class BigMatryoshka:
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


class MediumMatryoshka(BigMatryoshka):
    count = 0
    def __init__(self, medium_size: int, big_size: int):
        self.size = medium_size
        self.__class__.count += 1
        self.id = self.__class__.count
        self.big_matryoshka = BigMatryoshka(big_size)
        print(f"Создана средняя матрёшка с ID {self.id}")


class SmallMatryoshka(MediumMatryoshka):
    count = 0
    def __init__(self, small_size: int, medium_size: int, big_size: int):
        self.size = small_size
        self.__class__.count += 1
        self.id = self.__class__.count
        self.medium_matryoshka = MediumMatryoshka(medium_size=medium_size, big_size=big_size)
        print(f"Создана маленькая матрёшка. ID {self.id}")


"""
ЗАДАЧА
Добавить уникальные ID для каждой категории матрешек (атрибут экземпляра)
Добавить счетчик созданных матрешек (атрибут класса)

На инициализации каждой матрешки:
1. Мы увеличиваем счетчик созданных матрешек (в атрибуте класса)
2. На основе него, устанавливаем уникальный ID для каждой матрешки (атрибут экземпляра)
"""

# Создадим по несколько разных комплектов и проверим счетчики и ID

sm = SmallMatryoshka(10, 20, 30)
print(sm.get_count())
print(sm)

sm2 = SmallMatryoshka(15, 25, 35)
print(sm.get_count())
print(sm2)
sm3 = SmallMatryoshka(9, 12, 15)
print(sm.get_count())
print(sm3)
print(f'{"---" * 10}')

smed = MediumMatryoshka(20, 30)
print(smed.get_count())



smed2 = MediumMatryoshka(25, 35)
print(smed.get_count())

print(f'{"---" * 10}')

sb = BigMatryoshka(50)
print(sb.get_count())