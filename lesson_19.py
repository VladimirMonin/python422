from lesson_19_1 import * # Буквально копирование!
from dataset.cities import cities_list
# get_message()

# Отлично)

################ Продлолжаем тему "Плохих букв" из lesson_18


# Пробуем собрать сет плохих букв
# Буквы на которые НЕТ городов в наборе.

# Собираем set всех городов в нижнем регистре
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


# Вариант 2
# Собрать сет всех букв из всех городов

all_letters = set(str(cities_set))
print(all_letters)



# Цикл в цикле
iter_count = 0
bad_letters = set()
# Перебираем все уникальные символы в наборе городов
for letter in all_letters:
    # Перебираем все города в наборе
    for city in cities_set:
        iter_count += 1
        first_letter = city[0].lower()
        if letter == first_letter:
            # Проверка конкретной буквы останавливается. Город на эту букву найден.
            break
    # Else - отработает если цикл не завершился break. Т.е. город на эту букву не найден.
    else:
        bad_letters.add(letter)

print(bad_letters)
print(iter_count)