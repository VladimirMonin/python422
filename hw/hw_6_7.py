import json
import time
from random import randint

MIN_TIME_LIMIT = 2
MAX_TIME_LIMIT = 8
JSON_FILE = "cities.json"
# Сохраняем в JSON файл
# with open("cities.json", "w", encoding="utf-8") as file:
#     json.dump(cities_list, file, ensure_ascii=False, indent=4)

# Чтение городов из JSON файла
with open(JSON_FILE, "r", encoding="utf-8") as file:
    cities_list = json.load(file)

cities_set = {city['name'] for city in cities_list}
# print(cities_set)

computer_city = ''
while True:
    # ХОД ЧЕЛОВЕКА

    # Ввод города
    human_city = input("Введите город: ")
    
    # Проверка города. Есть ли он в датасете?
    if human_city.lower() in {city.lower() for city in cities_set}:
        print("Такой город есть в датасете")
    
    else:
        print("Человек проиграл! Такого города нет в датасете")
        break

    # Проверка а был ли ход компьютера?
    if computer_city:
        # Ход был. Надо проверять условия игры
        if human_city[0].lower() == computer_city[-1].lower():
            print("Условия выполнены. Ход переходит к компьютеру")

        else:
            print(f"Условия не выполнены. Город должен был начинатся с {computer_city[-1].upper()}")
            break

    # ХОД КОМПЬЮТЕРА

    # 1. Перебор сета с городами, с поиском подходящего под правила игры города
    random_time_sleep = randint(MIN_TIME_LIMIT, MAX_TIME_LIMIT)
    print(f"Я буду думать {random_time_sleep} секунд...")
    time.sleep(random_time_sleep)
    for city in cities_set:
        if human_city[-1].lower() == city[0].lower():
            computer_city = city
            print(f"Компьютер выбрал город {computer_city}")
            break
    else:
        # Eсли в цикле не отработал break мы попадем сюда
        print("Компьютер проиграл! Нет подходящего города")
        break

    
