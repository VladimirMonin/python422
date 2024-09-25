"""
Декораторы
Декораторы с параметрами
"""
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


some_func7('Cергей Сергеич', 30) # TypeError: print_decorator2.<locals>.wrapper() takes 1 positional argument but 2 were given