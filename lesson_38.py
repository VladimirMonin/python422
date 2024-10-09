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
        self.big_matryoshka = BigMatryoshka()
        print("Создана средняя матрёшка")


class SmallMatryoshka(MediumMatryoshka):
    def __init__(self):
        self.medium_matryoshka = MediumMatryoshka()
        print("Создана маленькая матрёшка")


# Создали маленькую - создали среднюю - создали большую автоматически
small_matryoshka = SmallMatryoshka()
small_matryoshka2 = SmallMatryoshka()

# Распечатаем маленькие матрёшки
print(small_matryoshka)
print(small_matryoshka2)

# Распечатаем средние матрёшки
print(small_matryoshka.medium_matryoshka)
print(small_matryoshka2.medium_matryoshka)

# Распечатаем большие матрёшки
print(small_matryoshka.medium_matryoshka.big_matryoshka)
print(small_matryoshka2.medium_matryoshka.big_matryoshka)

"""
ЗАДАЧА
Добавить уникальные ID для каждой категории матрешек (атрибут экземпляра)
Добавить счетчик созданных матрешек (атрибут класса)

На инициализации каждой матрешки:
1. Мы увеличиваем счетчик созданных матрешек (в атрибуте класса)
2. На основе него, устанавливаем уникальный ID для каждой матрешки (атрибут экземпляра)
"""