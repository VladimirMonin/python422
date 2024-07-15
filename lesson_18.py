# Lesson 18
# Словари

from data.marvel import small_dict, full_dict
from data.cities import cities_list
from pprint import pprint

# TODO: 1. Найдем фильмы по диапазону годов

# YEAR_START = 2008
# YEAR_END = 2012

# reusult = {}

# for title, year in small_dict.items():
#     if year is not None:
#         if YEAR_START <= year <= YEAR_END:
#             reusult[title] = year

# print(reusult)


##### C проверкой типов данных
# type(1) == int
# isinstance(1, int)

# for title, year in small_dict.items():
#     if isinstance(year, int) or isinstance(year, float):
#         if YEAR_START <= year <= YEAR_END:
#             reusult[title] = year


# С проверкой на строку и возможность её преобразования в число

# for title, year in small_dict.items():
#     if isinstance(year, int) or isinstance(year, float):
#         if YEAR_START <= year <= YEAR_END:
#             reusult[title] = year
#     elif isinstance(year, str):
#         if year.isdigit():
#             year = int(year)
#             if YEAR_START <= year <= YEAR_END:
#                 reusult[title] = year

# reusult = {}

# for title, year in small_dict.items():
#     try:
#         YEAR_START <= year <= YEAR_END
#         reusult[title] = year

#     except TypeError as e:
#         print(f"Ошибка в данных: {e}\nВероятно, фильм {title} c {year} год является числом")
#         continue

# print(reusult)

# TODO: 2. Full_dict - поиск фильмов по заданному году.

"""
1. Пользовательский ввод. Пользователь вводит год
2. Проверка на тип данных
3. Поиск фильмов по году
4. Учет ошибок (год может быть None)
"""

# year = input("Введите год: ")

# try:
#     year = int(year)
# except ValueError:
#     print("Год должен быть числом")
#     exit()

# result_dict = {}

# for film in full_dict.values():
#     film_year = film["year"]
#     if film_year == year:
#         film_title = film["title"]
#         result_dict[film_title] = film_year


# print(result_dict)

# Это же в одной строке

# result_dict = {film["title"]: film["year"] for film in full_dict.values() if film["year"] == year}

# print(result_dict)

# pprint(cities_list)


# TODO 3. Поиск городов где население выше пользовательского ввода

"""
1. Пользовательский ввод
2. Проверка на тип данных
3. Поиск городов
4. Учет ошибок?
"""

# Строка
# min_population = input("Введите минимальное количество населения: ")

# # type или isinstance = строка
# try:
#     min_population = int(min_population)
#     if min_population < 0:
#         print("Население не может быть отрицательным числом")
#         exit()
# except ValueError:
#     print("Население должно быть числом")
#     exit()


# result_cities = []

# city - словарь
# for city in cities_list:
#     if city["population"] >= min_population:
#         result_dict = {}
#         result_cities.append(city)


# List comprehension
# result_cities = [city for city in cities_list if city["population"] > min_population]


# for city in cities_list:
#     if city["population"] >= min_population:
#         result_dict = {
#             "name": city["name"],
#             "population": city["population"],
#             "subject": city["subject"],
#             "latitude": city["coords"]["lat"],
#             "longitude": city["coords"]["lon"],
#             "district": city["district"]
#         }
#         result_cities.append(city)


# Comprihension (возьмем только название и население)

# result_cities = [
#     {
#         "name": city["name"],
#         "population": city["population"]
#     }

#     for city in cities_list if city["population"] >= min_population
# ]


# pprint(result_cities)

# Найдем города на й через startswith
result = [city for city in cities_list if city["name"].lower().endswith("й")]

pprint(len(result))

# Пробуем собрать сет плохих букв
# Буквы на которые НЕТ городов в наборе.

cities_set = {city["name"].lower() for city in cities_list}

# Вариант 1
# Цикл в цикле
iter_count = 0
bad_letters = set()
for city in cities_set:
    last_letter = city[-1]
    for city_2 in cities_set:
        first_letter = city_2[0]
        iter_count += 1
        if last_letter == first_letter:
            break
    else:
        bad_letters.add(last_letter)


print(bad_letters)
print(iter_count)
