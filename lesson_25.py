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
def hello():
    print("Привет, Мир!")

# Вызов функции
hello()

# Ссылку на функцию можно присвоить переменной
hello2 = hello

# Переменная стала вызываемой функцией
print(hello2) # Получим служебную информацию о том что это объект функции
hello2()

# Пробуем получить результат выполнения функции в переменную
result = hello()
print(result) # None - это специальное значение, которое возвращает функция, если не указано 