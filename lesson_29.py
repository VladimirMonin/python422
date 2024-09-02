"""
Lesson 29
Анонимные функции. Вспоминаем map
"""

from typing import List, Dict, Callable, Union, Any, Optional, Tuple, Set, Iterable

"""
Callable - как аннотируется входные и выходные данные?
Callable[[int, int], int] - функция с 2 аргументами и возвращает int
"""


def get_sum(x: int, y: int) -> int:
    return x + y


get_sum2: Callable[[int, int], int] = get_sum


def my_map(func: Callable[[str], str], iter_obj: Iterable[str]) -> List:
    result = []
    for item in iter_obj:
        result.append(func(item))
    return result


product_list = ["apple", "banana", "orange", "pineapple"]


def get_upper(string: str) -> str:
    """
    Документация
    """
    return string.upper()


# Список продуктов в UPPER!

upper_product_list = my_map(get_upper, product_list)
upper_product_list: List = list(map(get_upper, product_list))
upper_product_list2: Iterable = map(get_upper, product_list)


# map (func, iter_obj)
"""
Функция высшего порядка.
Принимает другую функцию и итерируемый объект.
Применяет функцию к каждому элементу итерируемого объекта.
"""

data = ((1, 2), (3, 4), (5, 6))

# Цикл с sum
result = []

for item in data:
    result.append(sum(item))

# Получить суммы
result = list(map(sum, data))


# Вариант с циклом
result = []

for item in data:
    num1 = item[0]
    num2 = item[1]
    result.append(num1 + num2)

# Как это сделать через анонимную функцию с 2 аргументами?
result2 = list(map(lambda item: item[0] + item[1], data))


user_input = input("Введите числа через пробел: ").split()

user_input_nums = list(map(int, user_input))
print(user_input_nums)
user_input_nums = list(map(lambda x: int(x), user_input))
print(user_input_nums)
user_input_nums = [int(num) for num in user_input]
print(user_input_nums)

user_input_nums = []
for num in user_input:
    user_input_nums.append(int(num))

print(user_input_nums)

"""
Iterable - итерируемый объект.
- str
- list
- tuple
- dict
- set
- range
- mapobject
- filterobj
- zipobject
- enumerate
- keysobject
- valuesobject
- itemsobject
"""