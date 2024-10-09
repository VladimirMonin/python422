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
    def __init__(self):
        # BigMatryoshka.count += 1
        self.__class__.count += 1
        self.id = self.__class__.count
        print(f"Создана большая матрёшка с ID {self.id}")

    @classmethod
    def get_count(cls):
        return f'Класс {cls.__name__} создал {cls.count} матрешек'


class MediumMatryoshka(BigMatryoshka):
    count = 0
    def __init__(self):
        self.__class__.count += 1
        self.id = self.__class__.count
        self.big_matryoshka = BigMatryoshka()
        print(f"Создана средняя матрёшка с ID {self.id}")


class SmallMatryoshka(MediumMatryoshka):
    count = 0
    def __init__(self):
        self.__class__.count += 1
        self.id = self.__class__.count
        self.medium_matryoshka = MediumMatryoshka()
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

sm = SmallMatryoshka()
print(sm.get_count())

sm2 = SmallMatryoshka()
print(sm.get_count())

sm3 = SmallMatryoshka()
print(sm.get_count())

print(f'{"---" * 10}')

smed = MediumMatryoshka()
print(smed.get_count())



smed2 = MediumMatryoshka()
print(smed.get_count())

print(f'{"---" * 10}')

sb = BigMatryoshka()
print(sb.get_count())