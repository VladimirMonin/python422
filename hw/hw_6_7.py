"""
Какие тут могут быть функции?
1. Чтение данных из JSON
2. Подготовка set Городов
3. Проверка есть ли город в сете
4. Проверка выполнения правил игры
5. Опционально: работа с сетом плохих букв
6. Опционально: создания функций "Ход человека и ход компьютера"
7. Main
8. Запуск всего
"""


import json
import time
from random import randint

MIN_TIME_LIMIT = 2
MAX_TIME_LIMIT = 8
JSON_FILE = "cities.json"
MESSAGES_DICT = {
    "input_prompt": "Введите город: ",
    "city_in_dataset": "Такой город есть в датасете",
    "city_not_in_dataset": "Такого города нет в датасете",
    "human_lose": "Человек проиграл",
    "computer_lose": "Компьютер проиграл",
    "computer_step": "Ход компьютера",
    "computer_choice": "Компьютер выбрал город",
    "wrong_letter": "Неверная буква. Ваш город должен начинаться на другую букву",

}
# Сохраняем в JSON файл
# with open("cities.json", "w", encoding="utf-8") as file:
#     json.dump(cities_list, file, ensure_ascii=False, indent=4)

# Чтение городов из JSON файла
with open(JSON_FILE, "r", encoding="utf-8") as file:
    cities_list = json.load(file)


def read_json(file_name: str) -> list:
    """
    Чтение данных из JSON файла
    """
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def get_cities_data(json_data: list[dict]) -> set:
    """
    Подготовка set Городов
    """
    return {city["name"] for city in json_data}

def is_city_in_set(city: str, cities_set: set) -> bool:
    """
    Проверка есть ли город в сете
    """
    return city.lower() in {city.lower() for city in cities_set}

def check_city_rules(old_city: str, new_city: str) -> bool:
    """
    Проверка выполнения правил игры
    """
    return old_city[-1].lower() == new_city[0].lower()


def get_random_sleep(
    min_time: int = MIN_TIME_LIMIT, max_time: int = MAX_TIME_LIMIT
) -> None:
    """
    Получение случайного времени
    """
    time.sleep(randint(min_time, max_time))

def main():
    computer_city = ''

    cities_list = read_json(JSON_FILE)
    cities_set = get_cities_data(cities_list)

    while True:
        # ХОД ЧЕЛОВЕКА

        # Ввод города
        human_city = input(MESSAGES_DICT["input_prompt"])
        
        # Проверка города. Есть ли он в датасете?
        if is_city_in_set(human_city, cities_set):
            print(MESSAGES_DICT["city_in_dataset"])
        
        else:
            print(MESSAGES_DICT["city_not_in_dataset"], MESSAGES_DICT["human_lose"])
        
            break

        # Проверка а был ли ход компьютера?
        if computer_city:
            # Ход был. Надо проверять условия игры
            if check_city_rules(computer_city, human_city):
                    print(MESSAGES_DICT["computer_step"])

            else:
                    print(f"{MESSAGES_DICT['wrong_letter']} {computer_city[-1].upper()}")
                    break

        # ХОД КОМПЬЮТЕРА

        # 1. Перебор сета с городами, с поиском подходящего под правила игры города
        get_random_sleep()
        

        for city in cities_set:
            if check_city_rules(human_city, city):
                computer_city = city
                print(f"{MESSAGES_DICT['computer_choice']} {computer_city}")
                break
        else:
            # Eсли в цикле не отработал break мы попадем сюда
            print(MESSAGES_DICT["computer_lose"])
            break

        
if __name__ == "__main__":
    main()