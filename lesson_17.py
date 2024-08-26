# Lesson 17
# Импорт модулей и пакетов

"""
Правила нейминга модулей:
1. Не использовать кириллицу
2. Не использовать пробелы
3. Не использовать спецсимволы
4. Не использовать ключевые слова
5. Не использовать однобуквенные названия
6. Не использовать названия стандартных модулей
"""

"""
Модуль - это файл с расширением .py, который содержит код на языке Python.
Пакет - это каталог, который содержит файлы модулей и файл __init__.py

"""
# Импорт из модуля который лежит рядом. MESSAGE - это переменная
# from lesson_16 import MESSAGE
# MESSAGE = "Привет!"
# import lesson_16
# Выглядит как копирование ВСЕГО ФАЙЛА lesson_16.py
# print(lesson_16.MESSAGE)
from pprint import pprint
# print(msg)

# Самый не безопасный способ импорта
# from lesson_16 import *
# MESSAGE = "Пока!"
# print(MESSAGE)

# Импорт marvel
from dataset.marvel import full_dict

# print(small_dict)

# for key, value in small_dict.items():
#     print(f"{key} -> {value}")


# [print(f"{key} -> {value}") for key, value in small_dict.items()]


# pprint(full_dict, sort_dicts=False, indent=4)

# Параметры pprint
# indent - отступ
# sort_dicts - сортировка словарей

# Поработаем с small_dict
# 1. Попросим пользователя ввести год
# 2. Выведем фильмы этого года из small_dict

# year = input("Введите год: ")

# try:
#     year = int(year)

# except ValueError:
#     print("Год должен быть числом")
#     exit()

# result_dict = {}
# if year in small_dict.values():
#     # pass # Заглушка
#     for key, value in small_dict.items():
#         if value == year:
#             result_dict[key] = value
# if year in small_dict.values():
#     result_dict_ = {film: film_year for film, film_year in small_dict.items() if film_year == year}
#     pprint(result_dict_)

# else:
#     print(f"Фильмов за {year} год нет в базе данных")
#     exit()

"""
На самом деле эта штука состоит из 4 частей:
1. try - блок кода, который мы хотим проверить на ошибки
2. except Exception - блок кода, который выполняется, если в блоке try произошла ошибка
3. else - блок кода, который выполняется, если в блоке try ошибок не произошло
4. finally - блок кода, который выполняется в любом случае
"""

# 2. Сделаем поисковик фильмов. Пользователь вводит название фильма, мы списком по вхождению в ключ (с поправкой на регистр)

# film_name = input("Введите название фильма: ")
# result_dict = {film: film_year for film, film_year in small_dict.items() if film_name.lower() in film.lower()}
# pprint(result_dict)

# # В цикле бы это выглядело так:
# result_dict = {}
# for film, film_year in small_dict.items():
#     if film_name.lower() in film.lower():
#         result_dict[film] = film_year



# 3. Обходим small_dict, заменяем в ключах пробелы на "_" и в результат берем те, где не None в значениях
        
# Вариант с циклом
        
# result_dict = {}

# for film, film_year in small_dict.items():
#     if film_year is not None:
#         new_film_name = film.replace(" ", "_")
#         result_dict[new_film_name] = film_year

# pprint(result_dict, sort_dicts=False)
# # Вариант с comprehension
# result_dict = {film.replace(" ", "_"): film_year for film, film_year in small_dict.items() if film_year is not None}

# pprint(result_dict, sort_dicts=False)

# 4. Получим список словарей из full_dict
# Простая версия, без ключей

# result_list = list(full_dict.values())
# pprint(result_list)

# Сложная версия, Где мы возьмем ключ, и поместим его в словарь в формате 'id': key
# Цикл
result_list = []
for key, value in full_dict.items():
    new_dict = {}
    
    # Равноценно

    # new_dict['id'] = key
    # new_dict.update(value)
    # result_list.append(new_dict)

    # Равноценно (Через распаковку словаря)
    new_dict.update(
        {
            'id': key,
            **value
            
        }
    )

    result_list.append(new_dict)

pprint(result_list, sort_dicts=False)

for film in result_list:
    print(f'ID: {film["id"]} - {film["title"]} ({film["year"]})')


product_list = ['молоко', 'хлеб', 'яйца', 'масло', 'сахар', 'мука']
print(*product_list, sep=', ')
print(product_list[0], product_list[1], product_list[2], sep=', ')