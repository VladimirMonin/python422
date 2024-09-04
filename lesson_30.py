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

years_values = set(small_dict.values())

user_str_year = input("Введите год: ")
user_year = None

if user_str_year.isdigit():
    user_year = int(user_str_year)
    if user_year in years_values:
        print(f"Вы ввели год {user_year}. Он валиден.")
    else:
        print(f"Вы ввели год {user_year}. Он не валиден.")
        input('Введите Enter для выхода')
        exit()

else:
    print(f"Вы ввели чушь.")
    input('Введите Enter для выхода')
    exit()


if user_year:
    # Делеаем фильтрацию через цикл
    result = []
    result_dict = {}
    # items - вернет Iterable [(key, value), (key, value), (key, value)]
    for film, year in small_dict.items():
        if year == user_year:
            result.append(film)
            result_dict[film] = year


print(result)
print(result_dict)

# Делаем фильтрацию через фильтр

# Список фильмов
result_list = list(filter(lambda item: item[1] == user_year, small_dict.items()))
result_list_final = [film[0] for film in result_list]
print(result_list)
print(result_list_final)

result_dict = dict(filter(lambda item: item[1] == user_year, small_dict.items()))
print(result_dict)
