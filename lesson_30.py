"""
Конструкция match case - как аналог if elif else

"""

# user_input = 'down'.lower()

# match user_input:
#     case "up":
#         print("up")
#     case "down":
#         print("down")
#     case "left":
#         print("left")
#     case "right":
#         print("right")
#     case _:
#         print("wrong input")

"""
small_dict: Dict[str, Union[None, int]] = { # Dict[str, None|int]
    'Железный человек': 2008,
    'Невероятный Халк': 2008,
    'Железный человек 2': 2010,

1. Спросить у человека год фильма
2. Проверяем что это число, интуем, проверяем что входит в диапазон
3. С помощью фильтра получаем фильмы этого года
"""
from unittest import result
from dataset.marvel import small_dict, full_dict

# import dataset.marvel as ds
from pprint import pprint

# pprint(ds.full_dict)

# years_values = set(small_dict.values())

# user_str_year = input("Введите год: ")
# user_year = None

# if user_str_year.isdigit():
#     user_year = int(user_str_year)
#     if user_year in years_values:
#         print(f"Вы ввели год {user_year}. Он валиден.")
#     else:
#         print(f"Вы ввели год {user_year}. Он не валиден.")
#         input('Введите Enter для выхода')
#         exit()

# else:
#     print(f"Вы ввели чушь.")
#     input('Введите Enter для выхода')
#     exit()


# if user_year:
#     # Делеаем фильтрацию через цикл
#     result = []
#     result_dict = {}
#     # items - вернет Iterable [(key, value), (key, value), (key, value)]
#     for film, year in small_dict.items():
#         if year == user_year:
#             result.append(film)
#             result_dict[film] = year


# print(result)
# print(result_dict)

# # Делаем фильтрацию через фильтр

# # Список фильмов
# result_list = list(filter(lambda item: item[1] == user_year, small_dict.items()))
# result_list_final = [film[0] for film in result_list]
# print(result_list)
# print(result_list_final)

# result_dict = dict(filter(lambda item: item[1] == user_year, small_dict.items()))
# print(result_dict)


"""
1. Сделайте константу 
YEAR_LIMIT = 2020
2. Попробуйте адаптировать этот код так, чтобы получить фильмы вышедшие ПОСЛЕ этого
года
3. Выведите результат в консоль
"""
# from typing import Tuple, Union

# YEAR_LIMIT = 2020
# def year_filter(item: Tuple[str, Union[None, int]], year_limit=YEAR_LIMIT) -> bool:
#     year = item[1]
#     if isinstance(year, int):
#         return year > year_limit
#     return False


# YEAR_LIMIT = 2020

# result_dict = dict(filter(year_filter, small_dict.items()))

# # Вариант с lambda и filter - словарь на выходе
# result_dict = dict(
#     filter(
#         lambda item: item[1] > YEAR_LIMIT if isinstance(item[1], int) else False,
#         small_dict.items(),
#     )
# )
# print(result_dict)


# # Версия Константина (фильтр в фильтре)
# result_dict = dict(
#     filter(
#         lambda item: item[1] > YEAR_LIMIT,
#         filter(
#             lambda x: x[1] != None,
#             small_dict.items()),
#     )
# )

# # Вариант со списковым включением и списков назаний

# result_list = [
#     film
#     for film, year in small_dict.items()
#     if isinstance(year, int) and year > YEAR_LIMIT
# ]

# print(result_list)

# # Вариант с словарным включением и словарем

# result_dict2 = {
#     film: year
#     for film, year in small_dict.items()
#     if isinstance(year, int) and year > YEAR_LIMIT
# }


####

# 1. Перепакуем фулл дикт - соберем значения в список

# full_dict_values = list(full_dict.values())

# pprint(full_dict_values, sort_dicts=False)

# 2. Перепаковка словаря словарей в список словарей
"""
БЫЛО:
    0: {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'

СТАЛО
        [
            {
                'id': 0,
                'title': 'Железный человек',
                'year': 2008,
                'director': 'Джон Фавро',
                'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
                'producer': 'Ави Арад и Кевин Файги',
                'stage': 'Первая фаза'
            },
            {
                'id': 1,
                'title': 'Железный человек 2',
                'year': 2010,
                'director': 'Джон Фавро',
                'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
                'producer': 'Ави Арад и Кевин Файги',
                'stage': 'Первая фаза'
            },
           
"""

# # Сделаем перепаковку через цикл
# result_list = []

# for id, film_data in full_dict.items():
#     # Вариант где новый ключ id - последний
#     # film_data["id"] = id
#     # result_list.append(film_data)
#     # Вариант где новый ключ id - первый
#     new_dict = {"id": id, **film_data}
#     result_list.append(new_dict)


# # Сделаем перепаковку через списковое включение
# result_list = [{"id": id, **film_data} for id, film_data in full_dict.items()]
# pprint(result_list, sort_dicts=False)

#####
# names_list = [
#     "Азамат",
#     "Игорь",
#     "Денис",
#     "Спартак",
#     "Константин",
#     "Дмитрий",
#     "Наталия",
#     "Мария",
#     "Артур",
#     "Владимир",
# ]
# names_list.sort()
# print(names_list)

# # Реверс
# names_list.sort(reverse=True)
# print(names_list)

# # Сортировка по длине имени
# names_list.sort(key=len)
# print(names_list)

# # Сортировка по 2м признакам, длина имени и алфавит
# names_list.sort(key=lambda name: (len(name), name))
# print(names_list)

# # Сортировка по последней букве имени
# names_list.sort(key=lambda name: (name[-1], len(name)))
# print(names_list)

# # Sorted - функция высшего порядка, sorted(iterable, key=None, reverse=False)
# # Возвращает отсортированную коллекцию типа list
# print(sorted(names_list))

# # По длине имени
# print(sorted(names_list, key=len))


# # Сортировка словаря по ключам small_dict.items()
# pprint(dict(sorted(small_dict.items())), sort_dicts=False)


# Явно зададим функцию сортировки
# Сортировка словаря по ключам small_dict.items()
# pprint(dict(sorted(small_dict.items(), key=lambda item: item[0])), sort_dicts=False)

# # Сортировка словаря по значениям small_dict.items()
# pprint(
#     dict(
#         sorted(
#             small_dict.items(),
#             key=lambda item: item[1] if isinstance(item[1], int) else 3000,
#         )
#     ),
#     sort_dicts=False,
# )


result_list = [{"id": id, **film_data} for id, film_data in full_dict.items()]

# Сортировка списка словарей по ключу title
# pprint(
#     sorted(
#         result_list,
#         key=lambda item: item["title"] if isinstance(item["title"], str) else "",
#     ),
#     sort_dicts=False,
# )

# Функция для сортировки по ключу stage


def sort_by_stage(item):
    if item.get('stage'):
        if isinstance(item["stage"], str):
            match item["stage"]:
                case "Первая фаза":
                    return 1
                case "Вторая фаза":
                    return 2
                case "Третья фаза":
                    return 3
                case "Четвёртая фаза":
                    return 4
                case "Пятая фаза":
                    return 5
                case "Шестая фаза":
                    return 6
                case _:
                    return 99
        else:
            return 99
    else:
        return 99
    

# pprint(
#     sorted(
#         result_list,
#         key=sort_by_stage,
#     ),
#     sort_dicts=False,
# )

stage_dict = {
    "Первая фаза": 1,
    "Вторая фаза": 2,
    "Третья фаза": 3,
    "Четвёртая фаза": 4,
    "Пятая фаза": 5,
    "Шестая фаза": 6,
}

# 
phase_list = [
    "Нулевая фаза",
    "Первая фаза",
    "Вторая фаза",
    "Третья фаза",
    "Четвёртая фаза",
    "Пятая фаза",
    "Шестая фаза",
]

# Перепакуем! Подставим в значение фазы индекс из списка
new_result_list = [
    {**item, "stage": phase_list.index(item.get("stage"))} for item in result_list
]

pprint(new_result_list, sort_dicts=False)


# Сориторовка с лямбдой опираясь на словарь
# pprint(
#     sorted(
#         result_list,
#         key=lambda item: stage_dict.get(item.get("stage")) if item.get("stage") else 99,
#     ),
#     sort_dicts=False,
# )

# Резу
