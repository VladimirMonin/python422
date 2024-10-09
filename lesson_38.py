"""
Lesson 38 - Наследование
- Варианты наследования (Иерархическое, множественное)
- Абстрактный класс и абстрактные методы
- Конфликты
- MRO
- Миксины
"""

class BigMatryoshka:
    def __init__(self):
        print("Создана большая матрёшка")


class MediumMatryoshka(BigMatryoshka):
    def __init__(self):
        print("Создана средняя матрёшка")
        super().__init__()


class SmallMatryoshka(MediumMatryoshka):
    def __init__(self):
        print("Создана маленькая матрёшка")
        super().__init__()


small_matryoshka = SmallMatryoshka()