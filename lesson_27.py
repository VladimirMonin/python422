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

{"дед": True, "мама": False}

2. Напишите функцию которая принимает **kwargs
и выводит их в принте:
Слово: {word}, результат: {result}

3. Напишите функцию main, в которой все начинается с пользовательского
ввода, который разбивается на список по запятой, и передается
в функцию №1 и потом результат первой в функцию №2

4. Вызовите функцию main
"""