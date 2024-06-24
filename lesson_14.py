# Lesson 14
# 19.06.2024
# Virtual Environments
# Конспекты - https://github.com/VladimirMonin/conspects
# Конспект по VSCode - https://github.com/VladimirMonin/conspects/blob/main/VS%20Studio%20Code%20for%20Python%2C%20Django%2C%20Markdown%2C%20PlantUML.md

# Slice - срез
# SSS
# [start:stop:step]
# [0:-1:1] - Значения по умолчанию

# message = 'мама мыла раму'
# print(message[1:6]) # Не включая 4-й символ
# print(message[:6])
# print(message[:6:2])
# print(message[::2])

# Отзеркаливание строки

# print(message[::-1])

# Палиндром - слово, которое читается одинаково в обоих направлениях
"""
казак
довод
шалаш
топот
Аргентина манит негра
А роза упала на лапу Азора
"""

# Практика!
"""
1. Input: строка (проверяем один палиндром)
2. lower - приводит строку к нижнему регистру
3. slice - отзеркаливаем строку и сравниваем с оригиналом
"""

# word = input("Введите слово: ")

# word_raw = word.lower().replace(" ", "")

# if word_raw == word_raw[::-1]:
#     print("Палиндром")


# Проверка списка

"""
1. input.split(",") - разбиваем строку на список
2. Обвернуть в цикл for 43 и 44 строки
"""

# words = input("Введите слова через запятую: ").split(",")

# for word in words:
#     word_raw = word.lower().replace(" ", "")
#     if word_raw == word_raw[::-1]:
#         print(f"{word} - палиндром")
#     else:
#         print(f"{word} - не палиндром")


# message_2 = 'Пока, группа Python331!'
# new_message = message_2.replace("Python331", "Python422").replace("Пока", "Привет").upper() + '!!'


# names = ["иван иванович иванов", "мария степановна петрова",
#                     "петр николаевич давыдов", "илья сегизмундович перевозчиков",]

# new_names = []

# capitalize - первая буква в слове с большой буквы
# title - каждое слово с большой буквы

# for name in names:
#     new_name = name.title()
#     if "сегизмунд" not in new_name.lower():
#         new_names.append(new_name)

# print(new_names)


# Comprihension. Списковые включения. Списковые выражения. Генераторы списков
# List Comprehension

# Простой перебор списка
# 1. name - из чего состоит новый список
# 2. for name in names - откуда берем значения
# new_names_2 = [name for name in names]

# Преобразуем все элементы списка в верхний регистр title()
# new_names_3 = [name.title() for name in names]

# Плюс к этому отфильтруем Сегизмундов
# new_names_4 = [name.title() for name in names if "сегизмунд" not in name.lower()]

# Тернарнрый if в левой половине выражения
# Если есть мария, сделаем upper, иначе title
# new_names_5 = [name.upper() if "мария" in name.lower() else name.title() for name in names]
# print(new_names_5)

# Добавим условие в правой половине - исключим Сегизмундов
# new_names_6 = [name.upper() if "мария" in name.lower() else name.title() for name in names if "сегизмунд" not in name.lower()]

# Как бы это выглядело в цикле
new_names_7 = []

# for name in names:
#     if "сегизмунд" not in name.lower():
#         if "мария" in name.lower():
#             new_names_7.append(name.upper())
#         else:
#             new_names_7.append(name.title())


# Мы сидим на диете, и нам запрещено покупать определенные продукты питания

bad_products = ["конфеты", "пироженое", "чипсы", "кола", "пицца", "бургер"]
product_list = ["конфеты", "пироженое", "чипсы", "молоко", "хлеб", "пельмени", "масло"]

final_product_list = []

for product in product_list:
    if product not in bad_products:
        final_product_list.append(product)

print(final_product_list)

final_product_list_2 = [
    product for product in product_list if product not in bad_products
]
print(final_product_list_2)

final_product_list_3 = [
    product
    for product in product_list
    if product.lower() not in " ".join(bad_products).lower()
]
print(final_product_list_3)
# Это же с вложенным comprhension
final_product_list_4 = [
    product
    for product in product_list
    if product.lower() not in [bad_product.lower() for bad_product in bad_products]
]
print(final_product_list_4)

# Напишем это в цикле (с проверкой на вхождение в комприхеншен)

final_product_list_5 = []

for product in product_list:
    # Можно и так not in ' '.join(bad_products).lower()
    if product.lower() not in [bad_product.lower() for bad_product in bad_products]:
        final_product_list_5.append(product)


# Нужно обойти список продуктов, и проверить, есть ли продукт в списке запрещенных продуктов
# if not in - если продукта нет в списке запрещенных продуктов, добавляем его в список покупок
# если нет - не добавляем в список покупок

"""
В JS есть нечто похожее
массив.forEach((item, index, array) => {
"""


# List Comprehension - спиковые включения []
# Set Comprehension - множественные включения {value}
# Dict Comprehension - словарные включения {key: value}


group_table_list = [
    ["Фамилия", "Имя", "Отчество"],
    ["Моннин", "Владимир", "Александрович"],
    ["Габбасов", "Азамат", "Ахметович"],
    ["Григорьев", "Денис", "Сергеевич"],
    ["Добровольский", "Спартак", "Витальевич"],
    ["Зенин", "Константин", "Сергеевич"],
    ["Прокопович", "Александр", None],
    ["Савкина", "Наталия", "Павловна"],
    ["Шимкус", "Артур", "Станиславович"],
]

for last_name, first_name, middle_name in group_table_list[1:]:
    print(f"{last_name} {first_name[0]}. {middle_name[0]}.")
