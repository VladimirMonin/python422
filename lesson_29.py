"""
Lesson 29
Анонимные функции. Вспоминаем map
"""

from typing import List, Dict, Callable, Union, Any, Optional, Tuple, Set, Iterable

"""
Callable - как аннотируется входные и выходные данные?
Callable[[int, int], int] - функция с 2 аргументами и возвращает int
"""


# def get_sum(x: int, y: int) -> int:
#     return x + y


# get_sum2: Callable[[int, int], int] = get_sum


# def my_map(func: Callable[[str], str], iter_obj: Iterable[str]) -> List:
#     result = []
#     for item in iter_obj:
#         result.append(func(item))
#     return result


# product_list = ["apple", "banana", "orange", "pineapple"]


# def get_upper(string: str) -> str:
#     """
#     Документация
#     """
#     return string.upper()


# # Список продуктов в UPPER!

# upper_product_list = my_map(get_upper, product_list)
# upper_product_list: List = list(map(get_upper, product_list))
# upper_product_list2: Iterable = map(get_upper, product_list)


# # map (func, iter_obj)
# """
# Функция высшего порядка.
# Принимает другую функцию и итерируемый объект.
# Применяет функцию к каждому элементу итерируемого объекта.
# """

# data = ((1, 2), (3, 4), (5, 6))

# # Цикл с sum
# result = []

# for item in data:
#     result.append(sum(item))

# # Получить суммы
# result = list(map(sum, data))


# # Вариант с циклом
# result = []

# for item in data:
#     num1 = item[0]
#     num2 = item[1]
#     result.append(num1 + num2)

# # Как это сделать через анонимную функцию с 2 аргументами?
# result2 = list(map(lambda item: item[0] + item[1], data))


# user_input = input("Введите числа через пробел: ").split()

# user_input_nums = list(map(int, user_input))
# print(user_input_nums)
# user_input_nums = list(map(lambda x: int(x), user_input))
# print(user_input_nums)
# user_input_nums = [int(num) for num in user_input]
# print(user_input_nums)

# user_input_nums = []
# for num in user_input:
#     user_input_nums.append(int(num))

# print(user_input_nums)

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
# type - вернет строку с классом объекта
# if type(string) == str:
# isinstance - вернет bool
# if isinstance(string, str):

nums_product_list = ["хлеб", "молоко", "яйца", "масло", "сыр", "колбаса", 2, 4, 55, None]

# Как это отсортировать?

# Цикл!

result = []
for item in nums_product_list:
    if isinstance(item, str):
        if len(item) > 4:
            result.append(item)


def string_filter(item: Any) -> bool:
    """
    Функция фильтрации, которая отбирает строки длиннее 4 символов
    """
    if isinstance(item, str):
        if len(item) >= 4:
            return True
    return False


#### Цикл с фильтрацией

result = []

for item in nums_product_list:
    if string_filter(item):
        result.append(item)

#### Собственная функция высшего порядка, фильтр
"""
Она на вход берет функцию, и коллекцию
Применяет функцию фильтр к каждому элементу коллекции
Возвращает коллекцию, состоящую из элементов, которые прошли фильтр
"""

nums_product_list = ["хлеб", "молоко", "яйца", "масло", "сыр", "колбаса", 4, 55, None]

def my_filter(func: Callable, iter_obj: Iterable) -> Iterable:
    result = []
    for item in iter_obj:
        if func(item):
            result.append(item)
    return result


print(my_filter(string_filter, nums_product_list))
print(type(None))


# Используем встроенную функцию filter
result = list(filter(string_filter, nums_product_list))
print(result)


"""
Обработаем пользовательский ввод
Предположим, что пользователь вводит числа через пробел
Нам надо отфильтровать их, чтобы оставить только числа
Потом применить к ним int через map и полчить список чисел

1. Ввод пользователя
2. Превращаем в список
3. Фильтруем с помощью filter и is_digit
4. Применяем map с int
5. Получаем список чисел и выводим на экран

* Попробуйте сделать и фильтр и map в одной строке

** Попробуйте вообще все сделать в одной строке
"""

user_input = input("Введите числа через пробел: ").split()
# filtered_user_input = filter(lambda x: x.isdigit(), user_input)
# nums_list = list(map(int, filtered_user_input))
# print(nums_list)

# Вариант с map и filter в одной строке
filtered_nums = list(map(int, filter(lambda x: x.isdigit(), user_input)))
# Списковое выражение
filtered_nums = [int(item) for item in user_input if item.isdigit()]
print(feltered_nums)

# Вообще всё в одной строке
print(list(map(int, filter(lambda x: x.isdigit(), input("Введите числа ерез пробел".split())))))

# А теперь через list comprehension
print([int(item) for item in input("Введите числа через пробел: ").split() if item.isdigit()])
