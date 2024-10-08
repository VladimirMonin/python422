# Lesosn 13
# Списки и методы списков
# copilot 3 месяца бесплатно, 10 уе в месяц , tabnine есть бесплатный тариф на одну строку, codium, cody

# Переменные - ссылки на объекты в оперативной памяти

# id() - возвращает уникальный идентификатор объекта

a = 10
b = 10
print(id(a))
print(id(b))


# Списки
# Список - это упорядоченная именяемая коллекция объектов, которая может содержать объекты любого типа.

# Методы списков
# append() - добавляет элемент в конец списка
# sort() - сортирует список
# pop() - возвращает и удаляет объект из списка по индексу
# count() - возвращает количество элементов с указанным значением
# clear() - удаляет все элементы из списка
# copy() - возвращает копию списка
# extend() - добавляет элементы другого списка в конец списка
# index() - возвращает индекс первого элемента с указанным значением
# insert(index, value) - добавляет элемент в указанное место списка
# remove() - удаляет элемент с указанным значением
# reverse() - разворачивает список

# product_list = ["молоко", "хлеб", "яйца", "сыр", "масло"]

# new_product = "коньяк"
# product_list.append(new_product)

# print(product_list)

# Добавим через insert0 колбасу в начало списка
# product_list.insert(0, "колбаса")

# print(product_list)

# Удалим колбасу
# product_list.remove("колбаса")

# Удалим элемент по индексу
# product_list.pop(0)

# Сортировка списка sort(key=None, reverse=False) key - функция для сортировки, reverse - сортировка в обратном порядке
# product_list.sort()
# print(product_list)

# product_list.sort(key=len)
# print(product_list)

# TODO как именно будет происходить эта сортировка? Лексикографический порядок?
# product_list.sort(key=min)
# print(product_list)

# product_list = [
#     "молоко",
#     "хлеб",
#     "яйца",
#     "сыр",
#     "масло",
#     "сыр",
#     "молоко",
#     "яйца",
#     "бананы",
# ]

# Сколько раз попросили купить молока?
# milk_count = product_list.count("молоко")
# print(milk_count)

# Если в списке нет конфет более 2 раз в магазин я не пойду
# if product_list.count("конфеты") < 2:
#     print("НЕ пойду  в магазин")


# Итерация for по списку
# for product in product_list:
#     print(product)

# Почистим от дубликатов список продуктов
# clear_product_list = []
# for product in product_list:
#     if product not in clear_product_list:
#         clear_product_list.append(product)

# print(clear_product_list)

# Практика!
# Картавая задача
# Список слов принимается из Input. Напишите программу, которая возвращает список слов, в которых меньше двух букв 'р'.

# split - метод строки, который разбивает строку на список по указанному разделителю (по умолчанию пробел)
# BAD_LETTER = "р"
# BAD_LETTER_THRESHOLD = 2

# words = input("Введите список слов через запятую: ").split(",")

# Вариант №1. Цикл в цикле

# банан, бронетранспортер, репа

# filtered_words = []
# for word in words:
#     count = 0
#     for letter in word:
#         if letter == BAD_LETTER:
#             count += 1
#     if count < BAD_LETTER_THRESHOLD:
#         filtered_words.append(word)


# Вариант №2. Цикл с использованием метода count()

# filtered_words = []
# for word in words:
#     if word.count(BAD_LETTER) < BAD_LETTER_THRESHOLD:
#         filtered_words.append(word)
#

# Список внутри списка


# Вот список участников:

# 1. Моннин Владимир Александрович
# 2. Габбасов Азамат Ахметович
# 3. Григорьев Денис Сергеевич
# 4. Добровольский Спартак Витальевич
# 5. Зенин Константин Сергеевич
# 6. Прокопович Александр
# 7. Савкина Наталия Павловна
# 8. Шимкус Артур Станиславович

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

# Печатаю 0 элемент
print(group_table_list[0])

# Печатаю 0 элемент 0го элемента
print(group_table_list[0][0])

# Печатаю 0 элемент 0го элемента 0го элемента
print(group_table_list[0][0][0])

# pip install tabulate - установка библиотеки для красивого вывода таблиц
from tabulate import tabulate

print(tabulate(group_table_list, headers="firstrow", tablefmt="html"))