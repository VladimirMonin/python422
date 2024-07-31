"""
Lesson_24: JSON и YAML
Picle - ?
"""
# JSON - JavaScript Object Notation
"""
Массив - список
Объект - словарь
Массив массивов - список списков
Массив объектов - список словарей
"""
import json

FILE = "./data/lesson_24.json"

# Чтение из JSON

with open(FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print(type(data))

# Методы JSON
# load - загрузка из файла
# dump - запись в файл
# loads - загрузка из строки s - string - строка
# dumps - запись в строку s - string - строка

# JSON строка - список покупок

json_shop_list = '["Шоколадный дед мороз", "Мандарины", "Шампанское", "Огурцы", "Кефир"]'
print(type(json_shop_list))

# Задача - преобразовать это в JSON строку и обратно в список Python