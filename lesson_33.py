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
# def some_func(main_data=MAIN_DATA):
#     # Директива global a определит что а - глобальная
#     global a, b
#     a = 5
#     b = 22
#     с = 'c'
#     print(f'Привет из функции, а = {a}')
#     print(f'Доступ к константе MAIN_DATA: {MAIN_DATA}')

# some_func()
# print(a) # Попрежнему 10 (Глобальная область видимости)
# print(b) # 22 (Глобальная область видимости)
# print(c) # Переменная не определена, так как находится в локальной области видимости функции

# 4. Non-local: область видимости внутри функций

a = 5 # Global

# def a_one():
#     a = 1 # Local для функции a_one
#     print(f'Внутри функции a_one = {a}')

#     def a_two():
#         nonlocal a # Даю возможность изменить переменную во внешней функции
#         a = 2 # local для функции a_two
#         print(f'Внутри функции a_two = {a}')

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



def say_name2(name: str) -> Callable[[], None]:
    # Олег будет жить тут, пока не вызовется функция say_goodbye(), которая ссылается на него!
    def say_goodbye():
        print(f"Пока {name}!")

    return say_goodbye

sn: Callable = say_name2("Олег Тиньков")
sn2: Callable = say_name2("Валера")
sn()
sn2()