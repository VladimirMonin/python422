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
from dataset.marvel import small_dict

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
from typing import Tuple, Union

YEAR_LIMIT = 2020
def year_filter(item: Tuple[str, Union[None, int]], year_limit=YEAR_LIMIT) -> bool:
    year = item[1]
    if isinstance(year, int):
        return year > year_limit
    return False
    

YEAR_LIMIT = 2020

result_dict = dict(filter(year_filter, small_dict.items()))

# Вариант с lambda и filter - словарь на выходе
result_dict = dict(
    filter(
        lambda item: item[1] > YEAR_LIMIT if isinstance(item[1], int) else False,
        small_dict.items(),
    )
)
print(result_dict)


# Версия Константина (фильтр в фильтре)
result_dict = dict(
    filter(
        lambda item: item[1] > YEAR_LIMIT,
        filter(
            lambda x: x[1] != None, 
            small_dict.items()),
    )
)

# Вариант со списковым включением и списков назаний

result_list = [
    film
    for film, year in small_dict.items()
    if isinstance(year, int) and year > YEAR_LIMIT
]

print(result_list)

# Вариант с словарным включением и словарем

result_dict2 = {
    film: year
    for film, year in small_dict.items()
    if isinstance(year, int) and year > YEAR_LIMIT
}
