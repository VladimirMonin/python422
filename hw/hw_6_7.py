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

# Сделаем 2 функции. Ход человека и ход компьютера.
# Они будут инкапсулировать логику каждого хода и возвращать bool
# Функция main подготовит данные и будет вызвать их по очереди.


def human_step(
    cities_set: set, computer_city: str = "", messages_dict: dict = MESSAGES_DICT) -> str:
    """
    Ход человека
    """
    human_city = input(MESSAGES_DICT["input_prompt"])
    
    # Проверка что город в датасете
    if is_city_in_set(human_city, cities_set):
        print(MESSAGES_DICT["city_in_dataset"])
    
    # Прогирыш. Город не в датасете
    else:
        print(MESSAGES_DICT["city_not_in_dataset"], MESSAGES_DICT["human_lose"])
        
        return human_city
    
    # Был ли ход компьютера?
    if computer_city:
        # Проверка правил игры
        if check_city_rules(computer_city, human_city):
            print(MESSAGES_DICT["computer_choice"])
            return human_city
        
        # Первая буква НЕ правильная
        else:
            print(MESSAGES_DICT["wrong_letter"], MESSAGES_DICT["human_lose"])
            return ''
        
    # Первый ход - хода еще не было
    return human_city



def computer_step(
    cities_set: set, human_city: str = "", messages_dict: dict = MESSAGES_DICT
) -> str:
    """
    Ход компьютера
    """
    print(MESSAGES_DICT["computer_step"])
    get_random_sleep()
    
    computer_city = ''
    for city in cities_set:
            if check_city_rules(human_city, city):
                computer_city = city
                print(f"{MESSAGES_DICT['computer_choice']} {computer_city}")
                return computer_city
    else:
        # Eсли в цикле не отработал break мы попадем сюда
        print(MESSAGES_DICT["computer_lose"])
        return ''

  
def main():
    computer_city = ''

    cities_list = read_json(JSON_FILE)
    cities_set = get_cities_data(cities_list)

    while True:
        # ХОД ЧЕЛОВЕКА
        human_city = human_step(cities_set, computer_city)

        # Если человек не проиграл
        if human_city:
            cities_set.remove(human_city)
            computer_city = computer_step(cities_set, human_city)
            
            # Если компьютер не проиграл
            if computer_city:
                cities_set.remove(computer_city)
            
            # Если компьютер проиграл
            else:
                break
        # Если человек проиграл
        else:
            break



    
        
if __name__ == "__main__":
    main()