"""
Lesson 23: TXT Files
- Кодировка
- Таблица кодировки
- Как добыть индекс символа и символ по индексу
- Чтение и запись в файл
- Контекстный менеджер with
- Методы работы с файлами
- Построчное чтение файла
- Чтение файла целиком
- Запись в файл
- Модуль CSV
- lineterminator, delimiter
- CSV для Excel
"""

"""
ASCII - American Standard Code for Information Interchange
Как будет выглядеть кириллица в ASCII?
A%20%D0%90%20%D0%91%20%D0%92%20%D0%93%20%D0%94%20%D0%95%20%D0%96%20%D0%97%20%D0%98%20%D0%99%20%D0%9A%20%D0%9B%20%D0%9C%20%D0%9D%20%D0%9E%20%D0%9F%20%D0%A0%20%D0%A1%20%D0%A2%20%D0%A3%20%D0%A4%20%D0%A5%20%D0%A6%20%D0%A7%20%D0%A8%20%D0%A9%20%D0%AA%20%D0%AB%20%D0%AC%20%D0%AD%20%D0%AE%20%D0%AF

UTF-8 - Unicode Transformation Format
Это самая популярная кодировка в интернете. По-умолчанию в Python используется именно она.
В Linux и MacOS используется UTF-8, 

в Windows - cp1251 (Windows-1251)


010001010010101001010101010 - как это перевести в символы?
Привет мир!

Таблица кодировки:
https://unicode-table.com/ru/

UTF-16 - расширенная таблица символов. Байт на символ - 2 байта.
UTF-8 - 1 байт на символ, но может быть и 2, 3, 4 байта.
windows-1251 - 1 байт на символ.
ASCII - 1 байт на символ.

"""

# Как открыть файл txt в Python?
try:
    file = open(
        "test.txt", "r", encoding="utf-8"  # имя файла  # "флаг" на чтение
    )  # кодировка файла. По умолчанию - utf-8

except FileNotFoundError:  # FileNotFoundError - ошибка, если файл не найден!
    print("Файл не найден!")

# Флаги:
# r - read, чтение
# w - write, запись (если файла нет - создаст, если есть - перезапишет)
# a - append, добавление в конец файла (если файла нет - создаст, если есть - добавит)
# b - binary, бинарный файл (картинки, видео, музыка)

# Запись в файл

# file = open('test.txt', 'a', encoding='utf-8')
# file.write('Привет, мир!\n')
# file.write('Привет, мир!\n')
# file.write('Привет, мир!\n')
# file.write('Привет, мир!\n')
# file.write('Привет, мир!\n')
# file.write('Привет, мир!\n')
# file.write('Привет, мир!\n')
# file.close()

# file = open('test.txt', 'w', encoding='utf-8')
# for i in range(1, 11):
#    file.write(f'Привет, мир {i}-й раз!\n')

# file.close()

# Чтение файла как списка строк
file = open("test.txt", "r", encoding="utf-8")
# print(file) # <_io.TextIOWrapper name='test.txt' mode='r' encoding='utf-8'>
# print(list(file)) # Список строк, как на readlines()
# print('---------')
# for item in file: # item - строка
#     print(item, end='')

print("---------")
# print(list(file)) # Пустой список, так как файл уже прочитан и мы провели итерацию по нему
# lines = file.readlines() # Прочитать строки файла в список

# print(lines)

# CRUD - Create, Read, Update, Delete

clean_file = [line.strip() for line in file]  # Убрать переносы строк
print(clean_file)
# print(clean_file)


file.close()

# help(str.strip)

# контекстный менеджер with
# with open('test.txt', 'r', encoding='utf-8') as file:

with open("test.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)

# Код вне блока. Файл закрыт!


with open("test.txt", "w", encoding="utf-8") as file:
    for i in range(1, 11):
        file.write(f"Привет, мир {i}-й раз!\n")

# CSV - Comma Separated Values - значения, разделенные запятыми
"""
Стандарнтный разделитель - запятая
Кастомный разделитель для Excel - точка с запятой
"""

import csv

with open("data.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Николай", 30, "Москва"])


"""
1. Файл записан через строку
2. Все данные слиплись в первой ячейке строки
3. Иероглифы вместо кириллицы
"""

"""
lineterminator - символ, который будет вставлен в конце строки
delimiter - разделитель, стандартный для Excel - точка с запятой
windows-1251 - кодировка для Excel
"""

with open("data2.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";", lineterminator="\n")
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Николай", 30, "Москва"])


# Список списков
data = [
    ["Name", "Age", "City"],
    ["Николай", 30, "Москва"],
    ["Иван", 25, "Санкт-Петербург"],
    ["Мария", 35, "Казань"],
    ["Анна", 40, "Самара"],
]

for line in data:
    print(line[1])

# печатаем это в tabulate
# pip install tabulate
from tabulate import tabulate

# print(tabulate(data, tablefmt='grid'))

# Список словарей
dict_data = [
    {"Name": "Николай", "Age": 30, "City": "Москва"},
    {"Name": "Иван", "Age": 25, "City": "Санкт-Петербург"},
    {"Name": "Мария", "Age": 35, "City": "Казань"},
    {"Name": "Анна", "Age": 40, "City": "Самара"},
]


# Запись в CSV списка списков в один заход
# windows-1251 - используйте её!
with open("data3.csv", "w", encoding="utf-16") as file:
    writer = csv.writer(file, delimiter=",", lineterminator="\n")
    writer.writerows(data)

# Чтение из CSV в список списков
with open("data3.csv", "r", encoding="utf-16") as file:
    reader = csv.reader(file, delimiter=",")
    print(reader)
    data = list(reader)


# print(tabulate(data, tablefmt="grid"))

# Запись в CSV списка словарей
with open("data4.csv", "w", encoding="utf-16") as file:
    # columns = ["Name", "Age", "City"] # Заголовки вручную
    columns = dict_data[0].keys() # Заголовки из первого словаря
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=",", lineterminator="\n")
    writer.writeheader() # Записать заголовки
    writer.writerows(dict_data) # Записать данные


# Чтение из CSV в список словарей
with open("data4.csv", "r", encoding="utf-16") as file:
    reader = csv.DictReader(file, delimiter=",")
    data = list(reader)

print(data)