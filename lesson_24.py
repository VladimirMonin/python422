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
from pprint import pprint

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
"""
1. Объявляем переменную, в которую вы делаете json вызов метода loads
- Это преобразует строку в список
2. Выводим эту переменную, проверяем тип данных
3. Объявляем переменную, в которую вы записываете json вызов метода dumps
- Это преобразует список в строку
"""

shop_list = json.loads(json_shop_list)
print(shop_list)
print(type(shop_list))
shop_list.append("фейрверк")

json_shop_list = json.dumps(shop_list, ensure_ascii=False)
print(json_shop_list)

print(json.loads(json_shop_list))

# Список словрей студентов. Фамилия, имя, возраст, группа, хобби

students = [
    {
        "Фамилия": "Мишустин",
        "Имя": "Иван",
        "Возраст": 18,
        "Группа": "ПИ-19-1",
        "Хобби": ["налоги", "приливы", "отливы"],
    },
    {
        "Фамилия": "Басков",
        "Имя": "Петр",
        "Возраст": 19,
        "Группа": "ПИ-19-1",
        "Хобби": ["пение", "шубы"],
    },
    {
        "Фамилия": "Киркоров",
        "Имя": "Сидор",
        "Возраст": 20,
        "Группа": "ПИ-19-1",
        "Хобби": ["не те двери", "короны"],
    },
]


# Запись в JSON файл
with open(FILE, "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)


# Чтение из JSON файла
with open(FILE, "r", encoding="utf-8") as file:
    data = json.load(file)


pprint(data)