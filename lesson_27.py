"""
Lesson 27
Typing - модуль для сложной, детальной аннотации типов ????
"""
a = 5
print(f'{a=}') # Отладочная строка. Выведет a=5

# Функция со всеми типами аргументов

def example_func(a, b, *args, c=1, d=2, **kwargs):
    print(a, b, args, c, d, kwargs)


def get_four_arg(a, b, c, d):
    print(f"{a=} {b=} {c=} {d=}")


a = 1
b = 2
c = 3
d = 4

get_four_arg(a, b, c, d)
get_four_arg(a, b, c=c, d=d)
# get_four_arg(c, d, a=a, b=b)
get_four_arg(d, d=a, b=c, c=b)
get_four_arg(d=a, b=c,a=d, c=b)

arg = [a, b, c, d]
kwarg = {"d": d, "c": c, "b": b, "a": a}

get_four_arg(*arg) # 1, 2, 3, 4,
get_four_arg(**kwarg) # 4, 3, 2, 1

def get_four_arg2(**kwargs):
    print(f"{kwargs=}")


get_four_arg2(a=a, b=b, c=c, d=d)
get_four_arg2(**kwarg)

# TODO: Практика *args, **kwargs
"""
1. Напишите функцию, которая принимает *args строк
и проверяет их на палиндромность word.lower() == word[::-1].lower()
Возвращает список словарей с результатом формата

{"дEд": True, "мама": False}

2. Напишите функцию которая принимает **kwargs
и выводит их в принте:
Слово: {word}, результат: {result}

3. Напишите функцию main, в которой все начинается с пользовательского
ввода, который разбивается на список по запятой, и передается
в функцию №1 и потом результат первой в функцию №2

4. Вызовите функцию main

Дополнительный тестовый датасет
"""

words = [
    "Дед",        # Палиндром
    "Анна",       # Палиндром
    "КазАк",      # Палиндром
    "Топот",      # Палиндром
    "Яблоко",     # Не палиндром
    "Привет",     # Не палиндром
    "довод",      # Палиндром
    "Шалаш",      # Палиндром
    "коМок",      # Палиндром
    "Стол"        # Не палиндром
]


# 1 функция принмает *args строк и возвращает словарь
def is_palindrome(*words: str) -> dict:
    """
    Функция принимает *args строк и возвращает словарь с результатом проверки каждого слова
    на палиндромность.
    :param words: *args строк
    :return: словарь с результатом проверки каждого слова на палиндромность
    """
    result = {}
    for word in words:
        # result[word] = word.lower() == word[::-1].lower()
        if word.lower().replace(" ", "") == word.lower().replace(" ", "")[::-1]:
            result[word] = True
        else:
            result[word] = False
    return result


#  2 функция принмает **kwargs и выводит их в принте
def print_result(**words: dict) -> None:
    """
    Функция принимает **kwargs результатов анализа на палиндром
    и выводит их в принте
    :param words: **kwargs
    :return: None
    """
    for word, result in words.items():
        print(f"Cлово: {word}, результат: {result}")


def main() -> None:
    """
    Функция main, в которой все начинается с пользовательского
    ввода, который разбивается на список по запятой, и передается
    в функцию №1 и потом результат первой в функцию №2
    :return: None
    """
    user_input = input("Введите слова через запятую: ")
    words = user_input.split(",")
    result = is_palindrome(*words)
    print_result(**result)


if __name__ == "__main__":
    main()
