"""
Декораторы
Декораторы с параметрами
"""
from calendar import c
import re
from typing import Callable


def print_decorator(func: Callable[[], None]) -> Callable[[], None]:
    # func - хранится тут
    def wrapper():
        # Что-то делаем до вызова функции
        print("Перед вызовом функции")
        func()
        print("После вызова функции")
    
    return wrapper


@print_decorator # Указание пайтон, что декоратор нужно применить к функции some_func2
def some_func2() -> None:
    print("Вызов функции some_func2")

@print_decorator
def some_func3() -> None:
    print("Вызов функции some_func3")


some_func2()
some_func3()

@print_decorator
def some_func4(name: str) ->None:
    print(f'Привет {name} из функции some_func4') #TypeError:

# some_func4('Сергей Сергеич')

def print_decorator2(func: Callable) -> Callable:
    # func - хранится тут
    def wrapper(name: str):
        # Что-то делаем до вызова функции
        print("Перед вызовом функции")
        func(name)
        print("После вызова функции")
    
    return wrapper

def some_func5(name: str) ->None:
    print(f'Привет {name} из функции some_func5') 

f: Callable[[str], None] = print_decorator2(some_func5)
f('Сергей Сергеич')
f('Иван Иванович')

# С использованием декоратора. Чтобы не взрывать мозг)

@print_decorator2
def some_func6(name: str) ->None:
    print(f'Привет {name} из функции some_func6')


@print_decorator2
def some_func7(name: str, age: int) ->None:
    print(f'Привет {name}, тебе {age} лет')


# some_func7('Cергей Сергеич', 30) # TypeError: print_decorator2.<locals>.wrapper() takes 1 positional argument but 2 were given


def print_decorator3(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        # Что-то делаем до вызова функции
        print("Перед вызовом функции")
        func(*args, **kwargs)
        print("После вызова функции")

    return wrapper


@print_decorator3
def some_func8(name: str, age: int, **kwargs) ->None:
    print(f'Привет {name}, тебе {age} лет')
    for key, value in kwargs.items():
        print(f'{key}: {value}')


some_func8('Cергей Сергеич', 30, city='Москва', country='Россия', hoobies=['футбол', 'киберспорт'])


# ВОЗВРАТ ЗНАЧЕНИЯ

def print_decorator4(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        # Что-то делаем до вызова функции
        print(f'Вызов функции {func.__name__}')
        result =  func(*args, **kwargs)
        print(f'Принт после вызова функции {func.__name__}')
        return result

    return wrapper


@print_decorator4
def some_func9(name: str, age: int) -> str:
    return f'Привет {name}, тебе {age} лет'

result_some_func9 = some_func9('Cергей Сергеич', 30)
# Отладочная строка
print(f'{result_some_func9=}')


def logger_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        log = ''
        # Попытка что-то сделать
        try:
            result = func(*args, **kwargs)
        # Поймали ошибку
        except Exception as e:
            log = f'Ошибка при выполнении функции {func.__name__}: {e}'
            log += f'\n, Аргументы функции: {args if args else ""}, {kwargs if kwargs else ""}'
        # Ошибка не случилась
        else:
            log = f'Функция {func.__name__} успешно выполнена.'
            return result
        # Отработает в обоих случаях
        finally:
            print(log)
            # Запись в лог файл

    return wrapper
            

@logger_decorator
def delimetr(a: int, b: int) -> float:
    return a / b

delimetr(10, 5)
delimetr(10, 0)

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

import time
import json

def check_time_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        finish_time = time.perf_counter()
        result_time = finish_time - start_time
        print(f'Функция {func.__name__} отработала за {result_time:.10f} сек.')

    return wrapper


DATASET = "cities.json"

with open(DATASET, 'r', encoding='utf-8') as file:
    cities = json.load(file)


# 3 функции, которые обойдут cities, циклом, map, comprenhension, заглянут в ключ name и сделают upper
@logger_decorator
@check_time_decorator
def get_for_upper_name(cities: list = cities) -> list:
    result =[]

    for city in cities:
        city = {**city, 'name': city['name'].upper()}
        result.append(city)

    return result
@logger_decorator
@check_time_decorator
def get_map_upper_name(cities: list = cities) -> list:
    result = list(map(lambda x: {'name': x['name'].upper(), **x}, cities))
    return result
@logger_decorator
@check_time_decorator
def get_comprenhension_upper_name(cities: list = cities) -> list:
    result = [{'name': city['name'].upper(), **city} for city in cities]
    return result


comprenhension_upper_name = get_comprenhension_upper_name()
for_upper_name = get_for_upper_name()
map_upper_name = get_map_upper_name()

