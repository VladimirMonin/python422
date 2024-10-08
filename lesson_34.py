"""
Декораторы
Декораторы с параметрами
"""
from calendar import c
import re
from typing import Callable


# def print_decorator(func: Callable[[], None]) -> Callable[[], None]:
#     # func - хранится тут
#     def wrapper():
#         # Что-то делаем до вызова функции
#         print("Перед вызовом функции")
#         func()
#         print("После вызова функции")
    
#     return wrapper


# @print_decorator # Указание пайтон, что декоратор нужно применить к функции some_func2
# def some_func2() -> None:
#     print("Вызов функции some_func2")

# @print_decorator
# def some_func3() -> None:
#     print("Вызов функции some_func3")


# some_func2()
# some_func3()

# @print_decorator
# def some_func4(name: str) ->None:
#     print(f'Привет {name} из функции some_func4') #TypeError:

# # some_func4('Сергей Сергеич')

# def print_decorator2(func: Callable) -> Callable:
#     # func - хранится тут
#     def wrapper(name: str):
#         # Что-то делаем до вызова функции
#         print("Перед вызовом функции")
#         func(name)
#         print("После вызова функции")
    
#     return wrapper

# def some_func5(name: str) ->None:
#     print(f'Привет {name} из функции some_func5') 

# f: Callable[[str], None] = print_decorator2(some_func5)
# f('Сергей Сергеич')
# f('Иван Иванович')

# # С использованием декоратора. Чтобы не взрывать мозг)

# @print_decorator2
# def some_func6(name: str) ->None:
#     print(f'Привет {name} из функции some_func6')


# @print_decorator2
# def some_func7(name: str, age: int) ->None:
#     print(f'Привет {name}, тебе {age} лет')


# # some_func7('Cергей Сергеич', 30) # TypeError: print_decorator2.<locals>.wrapper() takes 1 positional argument but 2 were given


# def print_decorator3(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         # Что-то делаем до вызова функции
#         print("Перед вызовом функции")
#         func(*args, **kwargs)
#         print("После вызова функции")

#     return wrapper


# @print_decorator3
# def some_func8(name: str, age: int, **kwargs) ->None:
#     print(f'Привет {name}, тебе {age} лет')
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')


# some_func8('Cергей Сергеич', 30, city='Москва', country='Россия', hoobies=['футбол', 'киберспорт'])


# # ВОЗВРАТ ЗНАЧЕНИЯ

# def print_decorator4(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         # Что-то делаем до вызова функции
#         print(f'Вызов функции {func.__name__}')
#         result =  func(*args, **kwargs)
#         print(f'Принт после вызова функции {func.__name__}')
#         return result

#     return wrapper


# @print_decorator4
# def some_func9(name: str, age: int) -> str:
#     return f'Привет {name}, тебе {age} лет'

# result_some_func9 = some_func9('Cергей Сергеич', 30)
# # Отладочная строка
# print(f'{result_some_func9=}')


# def logger_decorator(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         log = ''
#         # Попытка что-то сделать
#         try:
#             result = func(*args, **kwargs)
#         # Поймали ошибку
#         except Exception as e:
#             log = f'Ошибка при выполнении функции {func.__name__}: {e}'
#             log += f'\n, Аргументы функции: {args if args else ""}, {kwargs if kwargs else ""}'
#         # Ошибка не случилась
#         else:
#             log = f'Функция {func.__name__} успешно выполнена.'
#             return result
#         # Отработает в обоих случаях
#         finally:
#             print(log)
#             # Запись в лог файл

#     return wrapper
            

# @logger_decorator
# def delimetr(a: int, b: int) -> float:
#     return a / b

# delimetr(10, 5)
# delimetr(10, 0)

"""
time.perf_counter() — это функция из модуля time в стандартной библиотеке Python, которая предоставляет доступ к 
монотонному счётчику времени с наивысшим доступным разрешением для измерения коротких промежутков времени. 
Вот несколько ключевых моментов об time.perf_counter():

Монотонность: Этот счетчик является монотонным, что означает, что его значения никогда не уменьшаются. 
Это важно для измерения временных интервалов, так как это гарантирует, что разница между концом и началом 
интервала всегда будет положительной или нулевой, даже если системные часы изменяются.

Высокое разрешение: Функция предоставляет время с высокой точностью, что делает ее идеальной для замера 
времени выполнения операций, особенно когда требуется измерить очень короткие промежутки времени.

Независимость от системного времени: Значение, возвращаемое time.perf_counter(), не зависит от системного 
времени и не подвержено изменениям из-за корректировки часов или перехода на летнее/зимнее время.

Использование: Эта функция часто используется для бенчмаркинга и профилирования кода, поскольку 
она предоставляет более точные измерения времени, чем time.time() или time.clock().

Платформонезависимость: time.perf_counter() работает на различных платформах, 
предоставляя стабильный интерфейс для замера времени.

Возвращаемое значение: Функция возвращает время в секундах как число с 
плавающей точкой. С момента запуска Python (или от момента первого вызова time.perf_counter(), 
точное определение зависит от реализации) до момента вызова функции.


start_time = time.perf_counter()
finish_time = time.perf_counter()
"""

# import time
# import json

# def check_time_decorator(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         func(*args, **kwargs)
#         finish_time = time.perf_counter()
#         result_time = finish_time - start_time
#         print(f'Функция {func.__name__} отработала за {result_time:.10f} сек.')

#     return wrapper


# DATASET = "cities.json"

# with open(DATASET, 'r', encoding='utf-8') as file:
#     cities = json.load(file)


# import time
# import json
# import traceback
# from functools import wraps
# from typing import Callable

# def logger_decorator2(func: Callable) -> Callable:
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Entering {func.__name__} (logger_decorator)")
#         print("Stack trace:")
#         print(''.join(traceback.format_stack()[:-1]))
#         log = ''
#         try:
#             result = func(*args, **kwargs)
#         except Exception as e:
#             log = f'Ошибка при выполнении функции {func.__name__}: {e}'
#             log += f'\n, Аргументы функции: {args if args else ""}, {kwargs if kwargs else ""}'
#         else:
#             log = f'Функция {func.__name__} успешно выполнена.'
#             return result
#         finally:
#             print(log)
#     return wrapper

# def check_time_decorator2(func: Callable) -> Callable:
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Entering {func.__name__} (check_time_decorator)")
#         print("Stack trace:")
#         print(''.join(traceback.format_stack()[:-1]))
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         finish_time = time.perf_counter()
#         result_time = finish_time - start_time
#         print(f'Функция {func.__name__} отработала за {result_time:.10f} сек.')
#         return result
#     return wrapper



# # 3 функции, которые обойдут cities, циклом, map, comprenhension, заглянут в ключ name и сделают upper
# @logger_decorator2
# @check_time_decorator2
# def get_for_upper_name(cities: list = cities) -> list:
#     result =[]

#     for city in cities:
#         city = {**city, 'name': city['name'].upper()}
#         result.append(city)

#     return result
# @logger_decorator2
# @check_time_decorator2
# def get_map_upper_name(cities: list = cities) -> list:
#     result = list(map(lambda x: {'name': x['name'].upper(), **x}, cities))
#     return result
# @logger_decorator2
# @check_time_decorator2
# def get_comprenhension_upper_name(cities: list = cities) -> list:
#     result = [{'name': city['name'].upper(), **city} for city in cities]
#     return result


# comprenhension_upper_name = get_comprenhension_upper_name()
# for_upper_name = get_for_upper_name()
# map_upper_name = get_map_upper_name()

# # ДЕКОРАТОР С ПАРАМЕТРАМИ!

# # Этот же декоратор, но чтобы он принимал 2 параметра, это префикс и постфикс
# # Первая функция передает параметры декоратора в обвертку

# def print_decorator_param(prefix: str = 'Начало', postfix: str = 'Конец')-> Callable:
#     # Вторая функция - сам декоратор. Передает обворачиваемую функцию в wrapper
#     def decorator(func: Callable) -> Callable:
#         # Третья функция - сама обвертка
#         def wrapper(*args, **kwargs):
#             print(f'Это старт: {prefix=}')
#             result = func(*args, **kwargs)
#             print(f'Это работа: {result=}')
#             print(f'Это финиш: {postfix=}')
#             return result
        
#         return wrapper
    
#     return decorator


# @print_decorator_param(postfix='Кастомный постфикс')
# def message(msg: str):
#     return f'Функция отработала: {msg}'


# msg = 'Басков!'

# result = message(msg)
# print(type(result))




def decorator_param(one: int = 0, two: int = 10)-> Callable:
    """
    Декоратор с параметрами.
    Проверяет входит ли аргумент декарируемой функции в диапазон чисел
    Если нет - raises ValueError
    """
    def decorator(func: Callable) -> Callable:
        # Третья функция - сама обвертка
        def wrapper(num):
            if not isinstance(num, int):
                raise ValueError('Аргумент должен быть целым числом')

            elif not (one <= num <= two):
                raise ValueError(f'Число должно быть в диапазоне от {one} до {two}')

            else:
                result = func(num)
                return result
        
        return wrapper
    
    return decorator

@decorator_param()
def get_number(num: int):
    return num * 2


get_number(5)
get_number(500)
# get_number('банан')