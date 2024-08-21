"""
Lesson 26. Функции
- Правила наименования функций
- Типы аргументов:
   - Позиционные
   - Именованные
   - Звездочка
   - Две звезды
"""
# def
"""
Правила наименования функций

- Имя функции должно быть осмысленным
- Имя функции должно быть в нижнем регистре
- snack_case - каждое слово с маленькой буквы разделенное подчеркиванием
- начинается как правило с глагола
- не должно начинаться с цифры
- не должено содержать специальных символов
- не должно содержать пробелов

get_user_by_id
get_user_by_name
get_user_by_email
"""

# Типы аргументов:
# Позиционные аргументы - это аргументы, которые передаются в функцию в определенном порядке
def get_hello_message(name, message):
    """
    Краткое, но ёмкое описание функции
    :param name: Имя пользователя
    :param message: Сообщение
    """
    return f"{name}{message}"

name_data = "Спартак."
message_data = "Рад тебя видеть!"

print(get_hello_message(name_data, message_data))
print(get_hello_message(message_data, name_data))


# get_hello_message(name_data)
# get_hello_message(name_data, name_data, message_data)

# Именованные аргументы - это аргументы, которые передаются в функцию в виде пары ключ: значение
print(get_hello_message(message=message_data, name=name_data))
print(get_hello_message(name=name_data, message=message_data))

"""
Практика!
Напишите функцию, которая принимает два аргумента:
- Имя
- Фамилия
И выводит строку, Имя: {имя}. Фамилия: {фамилия}
Попробуйте вызвать её 4 разаза:
1. Аргументы как положено
2. Поменяйте их иместами
3. Передайте их в виде именованных аргументов (имя=имя, фамилия=фамилия)
4. Передайте именнованные аргументы в ином порядке (фамилия=фамилия, имя=имя)
"""

def get_full_name(name, surname):
    return f"Имя: {name}. Фамилия: {surname}"

name = 'Иван'
surname = 'Иванов'

print(get_full_name(name, surname))
print(get_full_name(surname, name)) # Сбой!)
print(get_full_name(name=name, surname=surname))
print(get_full_name(surname=surname, name=name))


# Аргументы по-умолчанию
def get_hello_message2(name, message="Привет!"):
    return f"{name}{message}"

print(get_hello_message2(name_data))
print(get_hello_message2(name_data, message_data))

PASSWORD = "123456"
LOGIN = "admin"

def get_login(login=LOGIN, password=PASSWORD):
    print(f'Логинимся под пользователем {login} и паролем {password}')
    SECRET = 'secret'

get_login('логин', 'пароль')
get_login(login='логин', password='пароль')
get_login()

# *args - это аргументы, которые передаются в функцию в виде списка
"""
Когда мы описываем функцию, и пишем параметр где перед ним стоит *
Мы предполагаем, что туда может попасть N аргументов
И просим Пайтон упаковать их в список
"""

def print_upper_words(*args):
    for word in args:
        print(word.upper())

print_upper_words('a', 'b', 'c')
letters_list = ['a', 'b', 'c']
print_upper_words(letters_list[0], letters_list[1], letters_list[2])
print_upper_words(*letters_list)

# **kwargs - это аргументы, которые передаются в функцию в виде словаря

person_dict = {
    'name': 'Константин',
    'age': 25,
    'hobbie': 'программирование'
}

def print_person_info(name, age, hobbie):
    print(f'Имя: {name}, Возраст: {age}, Хобби: {hobbie}')


print_person_info(name=person_dict['name'],
                  age= person_dict['age'], 
                  hobbie= person_dict['hobbie'])
"""
Распаковка произойдет следующим образом
**person_dict
name = person_dict['name']
age = person_dict['age']
hobbie = person_dict['hobbie']
"""
print_person_info(**person_dict)
# print(**person_dict) # Ошибка! Он не ждёт именнованных аргументов name,  age, hobbie

print_config = {
    'sep': '|',
    'end': '++'
}

# print('a', 'b', 'c', **print_config)
print(*letters_list,  **print_config)

"""
Используя ниже приведенный датасет
Напишите фунцию которую можно будет применить в цикле к укажанному ниже датасету
Она принемает аргументы:
- Имя
- Фамилию
- Возраст
- Профессию
- Факультет

Ваша задача написать цикл, в котором вы пройдете по списку словарей, и 
И вызовете вашу функцию, передав в неё словарь в виде **словарь

Функция возвращает строку (может и сразу делать принт!)
Пример: 
Студент: Алина Ковалева, 20 лет, Программная инженерия, факультет Информатики
"""

students = [
    {
        "name": "Алина",
        "last_name": "Ковалева",
        "age": 20,
        "profession": "Программная инженерия",
        "fac": "Информатики"
    },
    {
        "name": "Бекжан",
        "last_name": "Жуманов",
        "age": 22,
        "profession": "Экономика и управление",
        "fac": "Экономики"
    },
    {
        "name": "Мария",
        "last_name": "Иванова",
        "age": 21,
        "profession": "Международные отношения",
        "fac": "Политологии"
    },
    {
        "name": "Арсен",
        "last_name": "Мамедов",
        "age": 23,
        "profession": "Гражданское право",
        "fac": "Юридический"
    },
    {
        "name": "София",
        "last_name": "Петренко",
        "age": 19,
        "profession": "Биотехнологии",
        "fac": "Биологический"
    }
]


def get_student_data(name, last_name, age, profession, fac):
    return f"Студент: {name} {last_name}, {age} лет, {profession}, факультет {fac}"

[print(get_student_data(**student)) for student in students]

data = [get_student_data(**student) for student in students]


# Простой пример с функцией **kwargs

def simple_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'ключ: {key}, значение: {value}')

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

simple_kwargs(**simple_dict)

# Порядок указания всех типов аргументов
"""
1. Обязательные аргументы
2. *args
3. Аргументы по-умолчанию
4. **kwargs
"""

# функция со всеми типами аргументов

def example_func(a, b, *args, c=1, d=2, **kwargs):
    print(a, b, args, c, d, kwargs)

example_func(11, 22, 33, name='John', age=25)

########################################
# Type Hints (Аннотации типов)
# Аннотации типов - это способ указать типы данных, которые ожидаются в качестве аргументов и возвращаемых значений функции.

"""
Простой вариант аннотации типов (без импорта модуля typing)
Позволяет указать базовые типы данных и возвращаемые значения

variable: type
str - строка
int - целое число
float - число с плавающей точкой
bool - булево значение (True или False)
list - список
tuple - кортеж
dict - словарь
set - множество

list[int] - список целых чисел
tuple[str, int] - кортеж, состоящий из 2 элементов: строка и целое число
"""

def simple_func(a: int, b: int = 2) -> int:
    return a + b

def simple_func2(a:list) -> None:
    print(a)

a = 2
b = 2
c = simple_func(a, b)

"""
Попробуйте написать фу
"""