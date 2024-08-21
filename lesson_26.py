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

