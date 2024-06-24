# Lesson_15
# 24.06.2024
# Множества (set)
# Концепция упорядоченности
# Список как коллекция ссылок на объекты
# Сет как неупорядоченная коллекция уникальных элементов
# Хешируемость элементов

# Упорядоченность
# В строке
message = "Hello, World!"
print(message[0:5])

# В списке
product_list = ["молоко", "хлеб", "масло"]
print(product_list[0])

# НЕ упорядоченность
# пустой сет
empty_set = {}  # ПУСТОЙ СЛОВАРЬ!

# пустой сет
empty_set = set()

# сет с элементами
product_set = {"молоко", "хлеб", "масло"}

print(product_set)

# Сет - это неупорядоченная коллекция уникальных элементов
product_list = ["молоко", "хлеб", "масло", "молоко", "хлеб", "масло", "кефир"]
print(product_list)

product_set = set(product_list)
print(product_set)

some_message = "HelLo, WOrld!"
some_set = set(some_message.lower())
print(some_set)
print(len(some_set))

some_int = 222.22
# print(len(some_int))
print(len(str(some_int)))


# Отличия списка и сета. Хешируемость элементов
# Список - коллекция ссылок на объекты
product_list = ["молоко", "хлеб", "масло", "молоко", "хлеб", "масло", "кефир"]
product_list_1 = product_list
product_list_2 = product_list_1.copy()
# Id - идентификатор объекта или адрес объекта в памяти
print(id(product_list[0]))
print(id(product_list[3]))

print(id(product_list_1[0]))
print(id(product_list_1[3]))

print(id(product_list_2[0]))
print(id(product_list_2[3]))

product_list_1[0] = "йогурт"
product_list_2[0] = "ростишка"

print(product_list)
print(product_list_1)
print(product_list_2)

some_set = {1102380, 13091890, 1232424}

num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
product_set = {"молоко", "Молоко"}
print(product_set)
# TODO - Почему послдние ID все те же? Глубокая копия списка?

# Хешируемость элементов - это преобразование объекта в число
# Одинаковых элементов в сете быть не может быть потому что они хешируются, и в коллекции чисел не может быть одинаковых

# TODO Практика с множествами и рандомным значением
"""
Программа, какой фильм сегодня посмотреть?
1. Пользовательский ввод - список фильмов через запятую
2. split - разбиваем строку на список
3. set - преобразуем список в множество
4. my_films_set.pop() - извлекаем случайный элемент из множества
5. Выводим на экран

"""
# Получили список фильмов
# крепкий орешек,крепкий орешек 2,крепкий орешек 3,крепкий орешек 4
# my_films = input("Введите список фильмов через запятую: ").split(",")

# Преобразовали список в множество
# my_films_set = set(my_films)

# Извлекли случайный элемент из множества
# random_film = my_films_set.pop()

# Вывели на экран
# print(random_film)


# Вариант 2 set_comprehension
# fimls_set = {film for film in
#              input("Введите список фильмов через запятую: ").split(",")}

# Тут я попросил у пользователя фильмы через запятую, потом разбил на список, потом преобразовал в множество, потом извлек случайный элемент и вывел на экран
# print({film for film in input("Введите список фильмов через запятую: ").split(",")}.pop())


product_list = ["Молоко", "Хлеб", "масло", "молОко", "хлеб", "масло", "кефир"]

# Преобразуем список в множество
product_set = set(product_list)

# Мы хотим сет, но без продуктов == молоко
product_set = set()

for product in product_list:
    if product.lower() != "молоко":
        product_set.add(product.lower())

# Set comprehension - выражение множества

# product_set = {product for product in product_list}
product_set = {
    product.lower() for product in product_list if product.lower() != "молоко"
}

print(product_set)

# Сет продуктов где меньше двух букв "о"

product_set = {
    product.lower() for product in product_list if product.lower().count("о") < 2
}

# В виде цикла
product_set = set()

for product in product_list:
    if product.lower().count("о") < 2:
        product_set.add(product.lower())

# МЕТОДЫ МНОЖЕСТВ
# len - длина множества (функция)
# add - добавить элемент в множество
# pop - извлечь случайный элемент из множества
# update - добавить несколько элементов в множество
# remove - удалить элемент из множества, если его нет, то ошибка
# discard - удалить элемент из множества, если его нет, то ничего не произойдет
# clear - очистить множество
# copy - скопировать множество

# Методы для сопоставления множеств

# union - объединение множеств (оператор |)
# intersection - пересечение множеств (оператор &)
# difference - разность множеств (оператор -)
# symmetric_difference - симметричная разность множеств (оператор ^)
# isdisjoint - проверка на не пересечение множеств
# issubset - проверка на подмножество
# issuperset - проверка на надмножество

# Множество с названиями фильмов

my_films = {"Крепкий орешек", "Гарри Поттер", "Такси", "Пила", "Титаник"}

# While коллеция. Пока коллекция не пуста
while my_films:
    # Извлекаем случайный фильм
    random_film = my_films.pop()
    # Выводим на экран
    print(random_film)

# for
for film in my_films:
    print(film)

# РАНДОМ
# Перемешиваем список фильмов - прогнали через set и обратно в список
my_films = ["Крепкий орешек", "Гарри Поттер", "Такси", "Пила", "Титаник"]
my_random_films = list(set(my_films))

print(my_random_films)

# shuffle - перемешивает список
from random import shuffle

# shuffle перемешивает список на месте (существующий список), не возвращает новый список
shuffle(my_random_films)
print(my_random_films)

# Попробуем перемешать буквы в слове
some_word = "трактор"
some_word_list = list(some_word)
shuffle(some_word_list)
new_word = "".join(some_word_list)
print(new_word)

# Попробуем перемешать буквы в слове, так, чтобы первая и последняя буквы остались на месте
some_word = "банан"
some_word_list = list(some_word)
list_for_shuffle = some_word_list[1:-1]
shuffle(list_for_shuffle)
new_word = some_word_list[0] + "".join(list_for_shuffle) + some_word_list[-1]
print(new_word)

# Choice - случайный элемент из коллекции
from random import choice

# Выбираем случайный элемент из списка
random_film = choice(my_random_films)
print(random_film)

# Randint - случайное целое число в диапазоне
from random import randint

# Случайное число от 1 до 10
# random_number = randint(1, 10)
# print(random_number)
# print(my_random_films[random_number])


my_films = ["Крепкий орешек", "Гарри Поттер", "Такси", "Пила", "Титаник"]
# Как быть чтобы не выходить за пределы списка?

list_length = len(my_films)
random_min_number = 0
random_max_number = list_length - 1

random_number = randint(random_min_number, random_max_number)

random_film = my_films[random_number]

print(random_film)

# В одну строку
random_film = my_films[randint(0, len(my_films) - 1)]

# Тут можно исопльзовать pop если вы хотите опустошить список
# random_film = my_films.pop(randint(0, len(my_films) - 1))

while my_films:
    random_index = randint(0, len(my_films) - 1)
    random_film = my_films.pop(random_index)
    print(random_film)


# Сопоставление множеств
my_films = {"Крепкий орешек", "Гарри Поттер", "Такси", "Пила", "Титаник"}
friend_films = {"Гарри Поттер", "Такси", "Пила", "Титаник", "Матрица", "Терминатор"}

# Множество фильмов, которые смотрел я, но не смотрел друг (или мы оба)
my_films_not_friend = my_films.difference(friend_films)
my_films_not_friend = my_films - friend_films
print(my_films_not_friend)
# Пересечение множеств (операотр &) - фильмы, которые смотрели оба
my_films_and_friend = my_films.intersection(friend_films)
my_films_and_friend = my_films & friend_films
print(my_films_and_friend)
# Симметричная разность множеств (оператор ^) - фильмы, которые смотрел только я или только друг
my_films_xor_friend = my_films.symmetric_difference(friend_films)
my_films_xor_friend = my_films ^ friend_films
print(my_films_xor_friend)
# Union - объединение множеств (оператор |) - фильмы, которые смотрел я или друг
my_films_or_friend = my_films.union(friend_films)
my_films_or_friend = my_films | friend_films
print(my_films_or_friend)

# Как еще мы можем получить симметричную разность множеств?
# 1. Сложить две разницы
# 2. Вычесть пересечение из объединения

# 1. Сложить две разницы через операторы
my_films_xor_friend = (my_films - friend_films) | (friend_films - my_films)
print(my_films_xor_friend)
# 2. Вычесть пересечение из объединения
my_films_xor_friend = (my_films | friend_films) - (my_films & friend_films)
print(my_films_xor_friend)

# TODO Практика Список гостей и множества
"""
1. Введите ваш список гостей через запятую
2. Введите список гостей супруги/супруга через запятую
3. Разбейте строки на списки
4. Преобразуйте списки в множества
5. Получите гостей, которые вы не пригласите со стороны супруга/супруги
6. Получите гостей, которые вы не пригласите с вашей стороны
7. Получите гостей итоговый (люди которые есть и там и там)
"""

my_guests = set(input("Введите список ваших гостей через запятую: ").split(","))
spouse_guests = set(
    input("Введите список гостей супруги/супруга через запятую: ").split(",")
)

# Гости, которых не пригласите со стороны супруга/супруги
my_guests_not_spouse = my_guests - spouse_guests
print(my_guests_not_spouse)

# Гости, которых не пригласите с вашей стороны
spouse_guests_not_my = spouse_guests - my_guests
print(spouse_guests_not_my)

# Гости итоговый
all_guests = my_guests & spouse_guests
print(all_guests)
