# Lesson 31, 32 находятся в другом репозитории (selenium422)
# Lesson 33: Области видимости, замыкания, декораторы

# 1. Области видимости переменных
# 2. Переменные внутри функций
# 3. Функции внутри функций
# 4. Замыкания
# 5. Декораторы

# Области видимости переменных
# 0. Built-in:

# print = 'Чебурек'
# print('Привет')

# # 1. Global: общедоступные переменные, которые можно использовать в любом месте кода
# MAIN_DATA = 'Чебурек'
# a = 10
# print(a)

# # 2. Local: область видимости внутри функции
def some_func(main_data=MAIN_DATA):
    # Директива global a определит что а - глобальная
    global a, b
    a = 5
    b = 22
    с = 'c'
    print(f'Привет из функции, а = {a}')
    print(f'Доступ к константе MAIN_DATA: {MAIN_DATA}')

# some_func()
# print(a) # Попрежнему 10 (Глобальная область видимости)
# print(b) # 22 (Глобальная область видимости)
# print(c) # Переменная не определена, так как находится в локальной области видимости функции

# 4. Non-local: область видимости внутри функций

# a = 5 # Global

def a_one():
    a = 1 # Local для функции a_one
    print(f'Внутри функции a_one = {a}')

    def a_two():
        nonlocal a # Даю возможность изменить переменную во внешней функции
        a = 2 # local для функции a_two
        print(f'Внутри функции a_two = {a}')

#     # Сделаем принт ДО вызова функции а_two
#     print(f'Принт до вывызова функции a_two: {a}')
#     # Вызов функции а_two
#     a_two()
#     # Принт ПОСЛЕ вызова функции
#     print(f'Принт после вызова функции a_two: {a}')

# a_one()
# print(f'Внешний принт = {a}')

from typing import List, Tuple, Callable

# def say_name(name: str):
#     # name - local в пространстве функции say_name
#     def say_goodbye():
#         print(f"Пока {name}!")

#     say_goodbye()

# say_name("Валера")

# # Ссылка на функцию - приравнивание без вызова функции
# my_print: Callable = print
# my_print('Привет из функции А!')



# def say_name2(name: str) -> Callable[[], None]:
#     # Олег будет жить тут, пока не вызовется функция say_goodbye(), которая ссылается на него!
#     # name тут
#     def say_goodbye():
#         print(f"Пока {name}!")

#     return say_goodbye

# sn: Callable = say_name2("Олег Тиньков")
# sn2: Callable = say_name2("Валера")
# sn()
# sn2()



"""
Пока sn ссылается на функцию say_name2, то она не будет удалена из памяти.
Соответственно и Олег останется в переменной name.

Почему замыкание?

Мы держим внутренние окружения и "замыкаем" их по цепочке
Обратившись к sn

sn -> say_name2 -> say_goodbye -> name = "Олег" 
"""

# def sum_a_b(a: int, b: int) -> int:
#     return a + b


# new_name = sum_a_b
# # Callable - что-то вызываемое (функция)- значит она сама вызываема
# # [[аргумент1, аргумент2], возвращаемое значение]
# new_name: Callable[[int, int], int] = sum_a_b

# def counter(start: int = 0) -> Callable[[], int]:
#     # Данные переменной start лежат ТУТ

#     def step():
#         # При вызове мы переписываем start
#         # Это возможно благодаря nonlocal (доступ наружу)
#         nonlocal start
#         start += 1
#         return start
    
#     return step

# c1 : Callable = counter()
# c2 : Callable = counter(10)

# print(c1()) # 1
# print(c1()) # 2
# print(c2()) # 11
# print(c2()) # 12

# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "lemon", "orange", "grape"]

# def sort_fruits(fruits: List[str]) -> Callable[[], List[str]]:
#     """
#     Сортируем список и сохраняем результат в кеш
#     :param fruits: Список фруктов
#     :return: Функция, которая возвращает список фруктов или результат кеша
#     """
#     # fruits - local - Они будут тут
#     cache: list = []

#     def sort() -> List[str]:
#         nonlocal cache # Позволяет перезаписать кеш, хранимый снаружи

#         # Проверка, есть ли кеш, и совпадает ли он по длине 
#         if not cache or len(cache) != len(fruits):
#             # Сортируем фрукты
#             cache = sorted(fruits)
        
#         return cache
    
#     return sort


# # Тестируем функцию с кешем

# sorter: Callable = sort_fruits(fruits)
# print(sorter())

# # Вызываем повторно с этими же данными (сортировка не будет произведена - вернется кеш)
# print(sorter())

# # Добавляем новый фрукт
# fruits.append("apples")

# # Пересортируем
# print(sorter())

# print(fruits)


# def print_decorator(func: Callable[[], None]) -> Callable[[], None]:
#     # func - хранится тут
#     def wrapper():
#         # Что-то делаем до вызова функции
#         print("Перед вызовом функции")
#         func()
#         print("После вызова функции")
    
#     return wrapper

# def some_func():
#     print("Вызов какой-то функции")

# f: Callable = print_decorator(some_func)
# f()

# @print_decorator
# def some_func2() -> None:
#     print("Вызов функции some_func2")


# some_func2()