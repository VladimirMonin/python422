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
    file = open('test.txt',  # имя файла
                'r', # "флаг" на чтение
                encoding='utf-8') # кодировка файла. По умолчанию - utf-8

except FileNotFoundError: # FileNotFoundError - ошибка, если файл не найден!
    print('Файл не найден!')

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
file = open('test.txt', 'r', encoding='utf-8')
lines = file.readlines() # Прочитать строки файла в список
file.close()
print(lines)

