"""
Lesson 28 - Тема: Функции Ч4. Анонимные функции. Знакомство. Typing. Mypy. Урок: 28

- Завершаем разбор HW с Городами (функции)
- Анонимные функции
- Ключевое слово "lambda"
- Map
- Filter
- Sorted
- Альтернатива однострочников?
- Typing 
- Mypy
"""

a = lambda x: x + 1

print(a(1))
print(a(2))

get_sum = lambda x, y: x + y

def get_sum2(x, y):
    return x + y


num_list = [1, 2, 3, 4, 5]

print([num + 1 for num in num_list])

# map - функция высшего порядка.
# Функция которая принемает другую функцию.

# Напишем собственный map

def get_str_upper(string: str)-> str:
    return string.upper()

func = get_str_upper
func('S')

def my_map(func, iter_obj):
    result = []
    for item in iter_obj:
        result.append(func(item))
    return result


shop_list = ["apple", "banana", "orange"]

upper_shop_list = my_map(get_str_upper, shop_list)

print(upper_shop_list)
