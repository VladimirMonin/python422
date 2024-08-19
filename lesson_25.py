"""
Урок: 25
Тема: Функции. Типы аргументов. Документация. DRY. SRP. 

DRY - Don't Repeat Yourself - Не повторяйся.
Принцип DRY гласит, что каждая часть кода должна быть написана только один раз.

SRP - Single Responsibility Principle - Принцип единственной ответственности.
Принцип SRP гласит, что каждый класс или функция должны быть ответственны только за одну вещь.

Функции - это блоки кода, которые выполняют определенную задачу.
Функции могут принимать аргументы и возвращать значения.
Функции позволяют избежать повторения кода.
Функция, или же подпрограмма, - это некоторый фрагмент программы, который можно вызвать из другого места программы.
"""

# def - ключевое слово для создания функции (define - определить)

# Пример функции без аргументов и без возвращаемого значения с print
# def hello():
#     print("Привет, Мир!")

# Вызов функции
# hello()

# Ссылку на функцию можно присвоить переменной
# hello2 = hello

# Переменная стала вызываемой функцией
# print(hello2) # Получим служебную информацию о том что это объект функции
# hello2()

# Пробуем получить результат выполнения функции в переменную
# result = hello()
# print(result) # None - это специальное значение, которое возвращает функция, если не указано return

# return - ключевое слово, которое прекращает выполнение функции и возвращает значение указанное после return
# Функция которая возвращает значение "Привет, Мир!"


# def hello():
#     return "Привет, Мир!"


# Наберите это. 
# Вызовите фунуцию hello() просто так.
# Поместите результат выполнения функции в переменную result
# Выведите переменную result на экран

# hello()
# result = hello()
# print(result)

# Параметры функции - это переменные, которые передаются в функцию при ее вызове

# Пример функции с параметром
from unittest import result


def hello(name):
    return f"Привет, {name}!"

# Вызов функции с параметром
result = hello("Мир")
result2 = hello([])

# Проверка типов данных

def hello(name):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    return f"Привет, {name}!"

result = hello('')

"""
1. Объявите функцию get_sum которая принимает два аргумента a и b и возвращает их сумму
2. Объявите функцию main которая использует input() для получения двух чисел от пользователя. 
3. После этого вызовите функцию get_sum и передайте в нее полученные числа. Результат выполнения функции get_sum выведите на экран
"""

def get_sum(a, b):
    return a + b


def main():
    user_input = input("Введите два числа через пробел: ").split()
    try:
        a, b = [int(i) for i in user_input]
    except ValueError:
        print("Введите числа")
        return
    
    result = get_sum(a, b)
    print(result)


# Делаем так, чтобы это выполнялось только если файл запущен напрямую
# Если код импортирован в другой файл, то код ниже выполнен не будет
# Потому что запуская его в другом месте, мы получим __name__ = lesson_25
name_25 = __name__
print(name_25)

num_list = [1, 2, 3, 4, 5]

def get_sum_by_list(num_list):
    result = 0
    for num in num_list:
        if not isinstance(num, int):
            raise TypeError("Список должен содержать только числа")
        result += num

    return result

# Функция с множественными параметрами *args
print(1)
print(1, 2)
# print(1, 2, n...)

def get_many_sum(*nums):
    print(nums)# tuple (1, 2, 3, 4, 5)
    print(type(nums)) # <class 'tuple'>
    print(*nums) # 1 2 3 4 5
    print(nums[0], nums[1], nums[2], nums[3], nums[4])
    

get_many_sum(1, 2, 3, 4, 5)
get_many_sum('П', 'р', 'и', 'в', 'е', 'т')
num_list = [1, 2, 3, 4, 5]
get_many_sum(*num_list)
get_many_sum(num_list[0], num_list[1], num_list[2], num_list[3], num_list[4])
print(*num_list)

a, b, c, d, e = num_list
a, b, c, *other = num_list

print(other)

"""
1.
Напишите функцию которая принимает *args слов
и возвращает их количество
2.
Напишите функцию которая принимает *args слов
проверяет их на палиндромы и возвращает список палиндромов
word.lower() == word.lower()[::-1]
3.
Напишите функцию которая принимает *args слов
проверяет их на палиндромы и возвращает словарь формата {слово: True/False}
"""

# 1. Напишите функцию которая принимает *args слов
def count_words(*args):
    return len(args)

words = ['дед', 'казак', 'шалаш', 'репа']

print(count_words(*words))
print(count_words(words[0], words[1], words[2], words[3]))
print(count_words('дед', 'казак', 'шалаш', 'репа'))

#2. Напишите функцию которая принимает *args слов и проверяет их на палиндромы и возвращает список палиндромов

def get_list_palindromes(*words):
    palindromes = []
    for word in words:
        if word.lower() == word.lower()[::-1]:
            palindromes.append(word)
    return palindromes

print(get_list_palindromes(*words))

# 3. Функция которая принимает *args слов и проверяет их на палиндромы и возвращает словарь формата {слово: True/False}

def get_dict_palindromes(*words):
    palindromes = {}
    words = {word.lower() for word in words}
    
    # 3. Dict comprehension
    result = {word: word.lower() == word.lower()[::-1] for word in words}

    # 1. Работа со словарями в цикле
    for word in words:
        palindromes[word] = word.lower() == word.lower()[::-1]
        # 2. Работа со словарями в цикле
        # if word.lower() == word.lower()[::-1]:
        #     palindromes[word] = True
        # else:
        #     palindromes[word] = False
    return palindromes

print(get_dict_palindromes(*words))