"""
Lesson 35. Знакомство с ООП
- Правила нейминга. UpperCamelCase  (похоже на переменные)
- Class - ключевое слово для создания класса
"""

"""
Атрибут класса - это переменная, которая определяется внутри класса, но вне любого метода. Она общая для всех экземпляров класса.

Когда мы меняем значение атрибута класса (например, Cat.name = 'Безымянный барсик'), это изменение отражается на всех экземплярах класса, которые не имеют собственного атрибута с таким же именем.

Т.е. кличка может быть одна на всех, или у каждого своя.

Однако, если мы присваиваем значение атрибуту конкретного экземпляра (например, cat1.name = 'Барсик'), мы создаем атрибут экземпляра. Этот атрибут экземпляра имеет приоритет над атрибутом класса с тем же именем.

Таким образом, когда мы обращаемся к атрибуту экземпляра, Python сначала ищет его в самом экземпляре. Если атрибут не найден, поиск продолжается в классе. Поэтому изменение атрибута класса не влияет на экземпляры, у которых уже есть собственный атрибут с таким именем.

Это позволяет иметь общие значения для всех экземпляров класса, но при необходимости переопределять их для конкретных экземпляров.
"""


class Cat:
    # Атрибут класса
    clinic = 'Котоклиника'
    def __init__(self, name: str):
        # Атрибут экземпляра - данные, которые будут принадлежать конкретному экземпляру класса. И только ему.
        self.name =name

cat1 = Cat('Мурзик') # TypeError: Cat.__init__() missing 1 required positional argument: 'name'
cat2 = Cat('Барсик')

cats = [cat1, cat2]

[print(cat.name) for cat in cats]
[print(cat.clinic) for cat in cats]

[print(f'Кличка кота: {cat.name}, Клиника: {cat.clinic}') for cat in cats]