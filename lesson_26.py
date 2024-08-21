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
def get_hello_message(name, message):
    return f"{name}{message}"

name_data = "Денис."
message_data = "Рад тебя видеть!"

print(get_hello_message(name_data, message_data))
print(get_hello_message(message_data, name_data))