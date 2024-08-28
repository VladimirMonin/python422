"""
Lesson 28 - Тема: Функции Ч4. Анонимные функции. Знакомство. Typing. Mypy. Урок: 28

- Завершаем разбор HW с Городами (функции)
- Анонимные функции
- Ключевое слово "lambda"
- Map
- Filter
- Sorted ???
- Альтернатива однострочников?
- Typing 
- Mypy # pip install mypy
"""
from typing import List, Dict, Callable, Union, Any, Optional, Tuple, Set

# a = lambda x: x + 1

# print(a(1))
# print(a(2))

# get_sum = lambda x, y: x + y

# def get_sum2(x, y):
#     return x + y


# num_list = [1, 2, 3, 4, 5]

# print([num + 1 for num in num_list])

# map - функция высшего порядка.
# Функция которая принемает другую функцию.

# Напишем собственный map

# def get_str_upper(string: str)-> str:
#     return string.upper()

# func = get_str_upper
# func('S')

# def my_map(func, iter_obj):
#     result = []
#     for item in iter_obj:
#         result.append(func(item))
#     return result


# shop_list = ["apple", "banana", "orange"]

# upper_shop_list = my_map(get_str_upper, shop_list)

# print(upper_shop_list)

# Map - функция высшего порядка.
# Принимает другую функцию.
# Применяет её к каждому элементу итерируемого объекта.
# Возвращает итератор.

# Применим get_str_upper к каждому элементу списка

# result = list(map(get_str_upper, shop_list))
# print(result)

# result = list(map(lambda x: x.upper(), shop_list))
# print(result)

# result = list(map(str.upper, shop_list))
# print(result)

# result = [item.upper() for item in shop_list]

# TODO: Практика
"""
Пользователь должен ввести список чисел через input
Делим его на список по пробелу
Ваша задача обойти его map и lambda для получения списка чисел
"""

# user_nums = input("Введите числа через пробел: ").split()
# result = list(map(lambda x: int(x), user_nums))
# print(result)
# result = list(map(int, input("Введите числа через пробел: ").split()))
# print(result)

# result = [int(num) for num in input("Введите числа через пробел: ").split()]


# list_list_nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# sum_list_nums = list(map(sum, list_list_nums))

# print(sum_list_nums)


# Filter
# Принимает функцию и итерируемый объект
# Возвращает итератор
# Фильтрует по условию. Условие - функция, которая возвращает bool

str_num_list = ["1", "2", "3", "4", "5", "a", "7", "b", "9"]
def is_digit(string: str) -> bool:
    return string.isdigit()

result = list(filter(is_digit, str_num_list))
result = list(filter(lambda x: x.isdigit(), str_num_list))
result = [num for num in str_num_list if num.isdigit()]
print(result)

# Вложим filter в map
result = list(map(int, filter(lambda x: x.isdigit(), str_num_list)))
result = [int(num) for num in str_num_list if num.isdigit()]
print(result)


########## Typing - более точная аннотация типов для коллекций

"""
Список строк: List[str]   (В обычном варианте list[str])
Словарь строк: Dict[str, str]
Словарь где ключ строка, а значение или строка или None: Dict[str, Optional[str]]
Сет состоящий из строк или чисел Set[Union[str, int]]
Список словарей, где ключ строка а значения или строка или список чисел: List[Dict[str, Union[str, List[int]]]]

list[int] List[int]
"""

list_nums = [1, 2, 3, 4, "5"]

def sum_nums(nums: List[int]) -> int:
    return sum(nums)


result = sum_nums(list_nums)

