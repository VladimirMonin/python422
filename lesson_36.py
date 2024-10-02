"""
Lesson 36: Инкапсуляция
- Методы класса, статик методы
- Приватные, защищенные и публичные атрибуты класса
- Приватные, заащищенные и публичные методы класса
- Геттеры и сеттеры


Практика: pytybefix - библиотека для выгрузки видео с ютуба
"""

"""
У нас есть возможность спрятать атрибуты или методы класса, чтобы закрыть доступ к ним извне.
Обычные методы и классы = public (открытые)
__ - private (закрытые полностью) доступны только внутри класса
_ - protected (защищенные) доступны внутри класса, а также в наследниках.
"""

# All - возвращает true если все элементы списка True
# Any - возвращает true если хотя бы один элемент списка True

integers = [0, 0, 0, 1]
trus_list = [True, True, False]

is_all_true = all(trus_list)
is_any_true = any(trus_list)


is_all_zeroes = all(x == 0 for x in integers)
is_any_zeroes = any(x == 0 for x in integers)

# Проверка, все ли строки в списке содержат определенную подстроку
strings = ["hello world", "hello python", "hello programming"]
contains_hello = all("hello" in s.lower() for s in strings)

# Проверка, есть ли в списке словарей элемент с определенным значением ключа
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]
has_adult = any(user["age"] >= 18 for user in users)

# Проверка, все ли числа в списке являются простыми
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

numbers = [2, 3, 5, 7, 11, 13]
all_prime = all(is_prime(num) for num in numbers)
