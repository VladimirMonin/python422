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

