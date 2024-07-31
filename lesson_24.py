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
from weather_api import API_KEY
import requests

FILE = "./data/lesson_24.json"

# Чтение из JSON

# with open(FILE, "r", encoding="utf-8") as file:
#     data = json.load(file)

# print(data)
# print(type(data))

# Методы JSON
# load - загрузка из файла
# dump - запись в файл
# loads - загрузка из строки s - string - строка
# dumps - запись в строку s - string - строка

# JSON строка - список покупок

# json_shop_list = '["Шоколадный дед мороз", "Мандарины", "Шампанское", "Огурцы", "Кефир"]'
# print(type(json_shop_list))

# Задача - преобразовать это в JSON строку и обратно в список Python
"""
1. Объявляем переменную, в которую вы делаете json вызов метода loads
- Это преобразует строку в список
2. Выводим эту переменную, проверяем тип данных
3. Объявляем переменную, в которую вы записываете json вызов метода dumps
- Это преобразует список в строку
"""

# shop_list = json.loads(json_shop_list)
# print(shop_list)
# print(type(shop_list))
# shop_list.append("фейрверк")

# json_shop_list = json.dumps(shop_list, ensure_ascii=False)
# print(json_shop_list)

# print(json.loads(json_shop_list))

# Список словрей студентов. Фамилия, имя, возраст, группа, хобби

# students = [
#     {
#         "Фамилия": "Мишустин",
#         "Имя": "Иван",
#         "Возраст": 18,
#         "Группа": "ПИ-19-1",
#         "Хобби": ["налоги", "приливы", "отливы"],
#     },
#     {
#         "Фамилия": "Басков",
#         "Имя": "Петр",
#         "Возраст": 19,
#         "Группа": "ПИ-19-1",
#         "Хобби": ["пение", "шубы"],
#     },
#     {
#         "Фамилия": "Киркоров",
#         "Имя": "Сидор",
#         "Возраст": 20,
#         "Группа": "ПИ-19-1",
#         "Хобби": ["не те двери", "короны"],
#     },
# ]


# Запись в JSON файл
# with open(FILE, "w", encoding="utf-8") as file:
#     json.dump(students, file, ensure_ascii=False, indent=4)


# # Чтение из JSON файла
# with open(FILE, "r", encoding="utf-8") as file:
#     data = json.load(file)


# pprint(data)

# Команда обнволения pip - pip install --upgrade pip

############################ OPEN WEATHER API и JSON ############################
# https://openweathermap.org/current

city = input("Введите город: ")
units = "metric"
lang = "ru"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}&lang={lang}"

print(url)

response = requests.get(url)

print(response)

"""
Что есть в объекте response:
.status_code - статус код
    200 - все ок
    404 - страница не найдена
    403 - доступ запрещен
.text - текст ответа
.json() - преобразование в JSON
.headers - заголовки
.cookies - куки
.url - URL
"""

# print(f'Статус код: {response.status_code}')
# print(f'Текст ответа: {response.text}')
# print(f'Применение .json: {response.json()}')
# print(f'Заголовки: {response.headers}')
# print(f'Куки: {response.cookies}')
# print(f'URL: {response.url}')

weather_data = response.json()
# pprint(weather_data)
# Разбираем данные, которые нам понадобятся
"""
["name"] - название города
["weather"][0]["description"] - описание погоды
["main"]["temp"] - температура
["main"]["feels_like"] - ощущается как
["main"]["humidity"] - влажность
["wind"]["speed"] - скорость ветра
"""
# Дата время - импорт
from datetime import datetime

final_weather_data = {
    "дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "город": weather_data["name"],
    "погода": weather_data["weather"][0]["description"],
    "температура": weather_data["main"]["temp"],
    "ощущается как": weather_data["main"]["feels_like"],
    "влажность": weather_data["main"]["humidity"],
    "скорость ветра": weather_data["wind"]["speed"],
}


# Запись данных в CSV файл, windows-1251, lineterminator="\n", dictwriter
import csv

# CSV_FILE = "./data/lesson_24.csv"

# with open(CSV_FILE, "a", encoding="windows-1251") as file:
#     writer = csv.DictWriter(file, fieldnames=final_weather_data.keys(), lineterminator="\n",)
#     writer.writeheader()
#     writer.writerow(final_weather_data)

# all_weather = []
# all_weather.append(final_weather_data)

# print(json.dumps(all_weather, ensure_ascii=False, indent=4))

# 1. Читаю JSON - список словарей и ложу в переменную all_weather

with open(FILE, "r", encoding="utf-8") as file:
    all_weather = json.load(file)

# 2. Добавляю в список словарей новую погоду
all_weather.append(final_weather_data)

# 3. Записываю в файл
with open(FILE, "w", encoding="utf-8") as file:
    json.dump(all_weather, file, ensure_ascii=False, indent=4)
