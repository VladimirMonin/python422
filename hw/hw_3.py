# Разбор HW_3 Привет из ветки hw_3_1

print('Привет из ветки main')
import sys
import os
print('Привет из ветки hw_3_1')

# .. - это родительский каталог на уровень выше
# ../.. - это родительский каталог на два уровня выше

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
Костыль для VSCode который не смог найти пакет.


import sys: Это импортирует модуль sys, который предоставляет доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором Python. В данном случае, он используется для доступа к sys.path.

import os: Это импортирует модуль os, который предоставляет функции для взаимодействия с операционной системой, включая работу с файловой системой.

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))):

os.path.dirname(__file__): Это возвращает каталог, в котором находится текущий файл (__file__ - это специальная переменная, которая содержит путь к текущему файлу).

os.path.join(os.path.dirname(__file__), '..'): Это объединяет путь к каталогу текущего файла и '..', что означает "родительский каталог". Результатом будет путь к родительскому каталогу текущего файла.

os.path.abspath(...): Это преобразует относительный путь к абсолютному. Это значит, что все символические ссылки (например, '..' для родительского каталога) будут разрешены.

sys.path.insert(0, ...): sys.path - это список, который содержит пути, где Python ищет модули при импорте. Этот код вставляет путь к родительскому каталогу текущего файла в начало этого списка. Это означает, что Python будет сначала искать модули в этом каталоге.

В общем, этот код добавляет родительский каталог текущего файла в пути поиска модулей Python. Это может быть полезно, если вы хотите импортировать модули, которые находятся в родительском каталоге.

"""

"""В данном задании вы будете работать с данными фильмов Марвелл, представленными в формате словаря словарей. Ваша задача - преобразовать этот словарь в список словарей, добавить идентификатор для каждого фильма, а затем предоставить пользователю возможность выбрать фазу Марвелл и получить список фильмов, соответствующих этой фазе."""

# from data.marvel import full_dict # Работает в Pycharm но не в VSCode
from data.marvel import full_dict # Пересоздание venv не помогло (VSCode увидеть пакет data)

from pprint import pprint

marvel_phases = {
    1: "Первая фаза",
    2: "Вторая фаза",
    3: "Третья фаза",
    4: "Четвертая фаза",
    5: "Пятая фаза",
    6: "Шестая фаза",
}

new_fdm = []

for key, value in full_dict.items():
    result = {
        "id": key,
        **value,  # равноценно коду ниже
        # 'title': value['title'],
        # 'year': value['year'],
        # 'director': value['director'],
        # 'screenwriter': value['screenwriter'],
        # 'producer': value['producer'],
        # 'stage': value['stage']
    }
    # result = {
    #     'id': key,
    # }
    result.update(value)
    new_fdm.append(result)

# new_fdm = []
# # Вариант от Константина
# for key, dict_value in full_dict.items():

#     dict_value["id"] = key
#     new_fdm.append(dict_value)

pprint(marvel_phases, sort_dicts=False)


user_choise = input("Введите номер фазы: ")

if not user_choise.isdigit():
    raise ValueError(f'Фаза должна быть числом, а не "{user_choise}"')

user_choise = int(user_choise)

marvel_keys = list(marvel_phases.keys())
marvel_keys_str = [str(key) for key in marvel_keys]
marvel_keys_str = ', '.join(marvel_keys_str)

# Одна строка через map
# marvel_keys_str = ', '.join(map(str, marvel_keys))

# Одна строка через генератор списка
# marvel_keys_str = ', '.join([str(key) for key in marvel_keys])


# if user_choise not in marvel_phases: # Равноценно варианту ниже
if user_choise not in marvel_phases.keys():
    raise ValueError(f'Фазы "{user_choise}" не существует\nВыберите одну из предложенных фаз: {marvel_keys_str}')


# result = [film for film in new_fdm if film["stage"].lower() == marvel_phases[user_choise].lower()]

# Это в цикле for

result = []
stage_str = marvel_phases[user_choise].lower()
for film in new_fdm:
    if film["stage"].lower() == stage_str:
        result.append(film)
    

pprint(result, sort_dicts=False)