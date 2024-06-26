# Lesson 16
# 26.06.2024
# Словари (dict)
# Синтаксис словаря
# Ключ - значение
# Схожесть с мноожеством
# Хешируемость ключей
# Упорядоченность ключей с версии Python 3.7

# Пустой словарь

# empty_dict = {}

# Словарь с элементами
# product_dict = {"молоко": 40, "хлеб": 30, "масло": 100}
# person_dict = {
#                 "name": "Александр", 
#                 "age": 25, 
#                 "is_student": True,
#                 "hobbies": ["плавание", "аниме", "программирование"],
#                 "address": {"city": "Москва", "street": "Ленина", "house": 10}
#                 }

# Ключами словаря как и элементами сета могут быть только неизменяемые объекты такие как:
# - числа
# - строки
# - кортежи
# - None
# - булевые значения

# unhashable type: 'list'
# name_set = {"Александр", "Спартак", "Анна", [1, 2, 3]}
# print(name_set)

# product_dict = {"молоко": 40, "хлеб": 30, "масло": 100}

# Доступ к элементам словаря
# bread_price = product_dict["хлеб"]
# bananas_price = product_dict['бананы'] # KeyError: 'бананы'

# Обновим цену хлеба
# product_dict["хлеб"] = 40
# product_dict["хлеб"] = product_dict["хлеб"] + 5
# print(product_dict)

# # Добавим кефир
# product_dict["кефир"] = 50
# print(product_dict)
# product_dict["кефир"] = 55
# print(product_dict)

# Так как ключи хешируются, как и значения сета, то ключи словаря должны быть уникальными
# Поэтому мы не можем добавить элемент с ключом "кефир" в словарь product_dict дважды
# Значение ключа "кефир" будет перезаписано

# Удаление элементов
# del product_dict["кефир"]
# print(product_dict)

# del - удаляет элемент по ключу
# del работает и в списках

# films_list = ["Побег из Шоушенка", "Зеленая миля", "Форрест Гамп"]
# del films_list[0]

# del работает и в строках
# my_string = "Hello, World!"
# del my_string[0] # строка неизменяемый объект!

# МЕТОДЫ СЛОВАРЕЙ!
# update() - обновляет словарь, добавляя элементы из другого словаря
# keys() - возвращает все ключи словаря
# values() - возвращает все значения словаря
# items() - возвращает пары ключ - значение
# copy() - копирует словарь
# get() - возвращает значение по ключу, если ключа нет, то возвращает None
# pop() - удаляет элемент по ключу и возвращает его значение
# popitem() - удаляет случайный элемент и возвращает его пару ключ - значение
# clear() - очищает словарь
# setdefault() - возвращает значение по ключу, если ключа нет, то добавляет его в словарь
# fromkeys() - создает словарь с ключами из списка и значением None
# dict() - создает словарь из итерируемого объекта
# len() - возвращает количество элементов в словаре
# in - проверяет наличие ключа в словаре
# not in - проверяет отсутствие ключа в словаре


# product_dict = {"молоко": 40, "хлеб": 30, "масло": 100}

# bananas_price = product_dict.get("бананы", 'Такого товара нет в наличии!')
# print(bananas_price)

# updatable_dict = {"масло": 110, "сметана": 60}

# product_dict.update(updatable_dict)
# product_dict.update(
#     {"бананы": 50,
#     "апельсины": 70,
#     "яблоки": 40,
#     }
#                      )
# print(product_dict)

# Длина словаря
# print(len(product_dict))


# [print(product) for product in product_dict]

# for product in product_dict:
#     print(product)

# keys - возвращает все ключи словаря
# for product in product_dict.keys():
#     print(product)

# keys - возвращает объект типа dict_keys
# dict_keys = product_dict.keys()
# print(dict_keys)
# print(type(dict_keys))
# list_dict_keys = list(dict_keys)
# print(list_dict_keys)
# print(type(list_dict_keys))

# values - возвращает все значения словаря
# for price in product_dict.values():
#     print(price)

# dict_values = product_dict.values()
# print(dict_values)
# print(type(dict_values))
# list_dict_values = list(dict_values)
# print(list_dict_values)
# print(type(list_dict_values))

# items - возвращает пары ключ - значение
# На каждой итерации, сюда попадает
# ['молоко', 40]
# for product, price in product_dict.items():
#     print(f'Продукт: {product}, цена: {price}')

# dict_items = product_dict.items()
# print(dict_items)
# print(type(dict_items))
# list_dict_items = list(dict_items)
# print(list_dict_items)

# names = ["Нина", "Анна"]
# name1, name2 = names

# name1 = names[0]
# name2 = names[1]

# names = ["Нина", "Анна", "Спартак", "Мария", "Азамат"]
# name1, name2, *other_names = names
# print(name1)
# print(name2)
# print(other_names)

# names = [
#     ["Нина", "Анна"],
#     ["Спартак", "Мария"],
#     ["Азамат", "Константин"],

#     ]

# for name1, name2 in names:
#     print(f'Имя 1: {name1}, Имя 2: {name2}')



# CRUD - Create, Read, Update, Delete
# Создание, Чтение, Обновление, Удаление

# TODO Практика. Внести запись, прочитать запись, удалить запись из словаря.
"""
Напишите программу, которая предложит пользователю:
1. Внести запись в словарь
2. Прочитать запись из словаря
3. Обновить запись в словаре

В зависимости от выбора пользователя, программа должна совершить нужную операцию.
Внести запись - спросить ключ и значение и добавить их в словарь
Прочитать запись - спросить ключ и вывести значение из словаря
Обновить запись - спросить ключ и значение и обновить значение в словаре
"""

# product_dict = {
#     'молоко': 40, 'хлеб': 30, 
#     'масло': 110, 'сметана': 60, 
#     'бананы': 50, 'апельсины': 70, 
#     'яблоки': 40}

# user_choise = input("Выберите действие: 0 - получить все данные, 1 - внести запись, 2 - прочитать запись, 3 - удаленить запись: ")
# user_choise = int(user_choise)

# # Получить все данные из словаря
# if user_choise == 0:
#     for product, price in product_dict.items():
#         print(f'Продукт: {product}, цена: {price}')

# # Операция внесения записи
# if user_choise == 1:
#     key = input("Введите название продукта: ")
#     value = input("Введите цену продукта: ")
#     product_dict[key] = int(value)
#     print(product_dict)

# # Операция чтения записи
# elif user_choise == 2:
#     key = input("Введите название продукта: ")
#     value = product_dict[key]
#     print(value)

# # Операция удаления записи
# elif user_choise == 3:
#     key = input("Введите название продукта: ")
#     del product_dict[key]
#     print(product_dict)


############################################

product_dict = {
    'молоко': 40, 'хлеб': 30, 
    'масло': 110, 'сметана': 60, 
    'бананы': 50, 'апельсины': 70, 
    'яблоки': 40}

choises_dict = {
    0: "Получить все данные",
    1: "Внести запись",
    2: "Прочитать запись",
    3: "Удалить запись",
    100: "Выход"
}

while True:
    for key, value in choises_dict.items():
        print(f"{str(key)} - {value}")

    print("Выберите действие:")

    user_choise = input()

    if user_choise.isdigit():
        if int(user_choise) in choises_dict:
            user_choise = int(user_choise)
        else:
            print("Такого действия нет!")
            break

    # Получить все данные из словаря
    if user_choise == 0:
        import tabulate
        print(tabulate.tabulate(product_dict.items(), headers=["Продукт", "Цена"], tablefmt="grid"))

    # Операция внесения записи
    if user_choise == 1:
        user_input = input("Введите название продукта и цену через двоеточие без пробелов: ").split(":")
        if len(user_input) == 2:
            product = user_input[0]
            price = user_input[1]
            if product.isalpha() and price.isdigit():
                product_dict.update({product.lower(): int(price)})
        

    # Операция чтения записи
    elif user_choise == 2:
        key = input("Введите название продукта: ").lower()
        value = product_dict.get(key, f'Продукта {key} нет в базе')

    # Операция удаления записи
    elif user_choise == 3:
        key = input("Введите название продукта: ").lower()
        if key in product_dict:
            # Удалит по ключу, и вернет значение в переменную price
            price = product_dict.pop(key)
            print(f'Продукт {key} с ценой {price} удален из базы')

    elif user_choise == 100:
        print("До свидания!")
        break

    else:
        print(f'Действия {user_choise} нет в списке!')

# pop - удаляет элемент по ключу и возвращает его значение
# popitem - удаляет случайный элемент и возвращает его пару ключ - значение
# setdefault - возвращает значение по ключу, если ключа нет, то добавляет его в словарь
# fromkeys - 

milk = product_dict.setdefault("молоко", 100500)
print(milk)
print(product_dict)

steam_games = ["CS:GO", "Dota 2", "GTA 5", "Cyberpunk 2077"]
steam_games_dict = dict.fromkeys(steam_games, 0)

print(steam_games_dict)

steam_prices = [100, 200, 500, 3000]

steam_games_zip = zip(steam_games, steam_prices) # Объект типа zip - итериратор
print(steam_games_zip)
# print(list(steam_games_zip))
print(dict(steam_games_zip))

# Словарные выражения
product_dict = {
    'молоко': 40, 'хлеб': 30, 
    'масло': 110, 'сметана': 60, 
    'бананы': 50, 'апельсины': 70, 
    'яблоки': 40}


# Обходим делаем дубль
product_dict_double = {key:value for key, value in product_dict.items()}

# Равноценный цикл
product_dict_double = {}

for key, value in product_dict.items():
    product_dict_double[key] = value

# Увеличим цены на 10%
product_dict_double = {key: value * 1.1 for key, value in product_dict.items()}

# Равноценный цикл
product_dict_double = {}

for key, value in product_dict.items():
    product_dict_double[key] = value * 1.1

# Тернарный if в левой половине. Уменьшим цены на 10% если цена больше 50 и сделаем реплейс о на а если в продукте больше 1 буквы о

product_dict_double = {key.replace("о", "а") if key.count('о') > 1 else key: value * 0.9 if value > 50 else value for key, value in product_dict.items()}

# Равноценный цикл
product_dict_double = {}

for key, value in product_dict.items():
    if key.count('о') > 1:
        key = key.replace("о", "а")
    if value > 50:
        value *= 0.9
    product_dict_double[key] = value


# Тернарный if справа. Фильтруем продукты если есть буквы ы

product_dict_double = {key: value for key, value in product_dict.items() if 'ы' not in key.lower()}


