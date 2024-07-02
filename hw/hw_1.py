# Разбор домашнего задания №1 (Секретное послание)


"""  
Вам пришло секретное послание. Оно содержит много странных символов, которые вы не можете понять.  
Но вы знаете, что в этом послании используются только маленькие русские буквы. Используйте знание языка Python  
а так же знание for i чтобы расшифровать его.  
"""

# Секретное послание
from unittest import result


secret_letter = [
    ["DFВsjl24sfFFяВАДОd24fssflj234", "sfsf", "sfsfd"],
    ["asdfFп234рFFdо24с$#afdFFтasfо"],
    ["оafбasdf%^о^FFжа$#af243ю"],
    ["afпFsfайFтFsfо13н"],
    ["fн13Fа1234де123юsdсsfь"],
    ["чFFтF#Fsfsdf$$о"],
    ["и$##sfF"],
    ["вSFSDам"],
    ["пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя"],
    ["FFэasdfтDFsfоasdfFт"],
    ["FяDSFзFFsыSfкFFf"],
]

# Список с маленькими русскими буквами
small_rus = [
    "а",
    "б",
    "в",
    "г",
    "д",
    "е",
    "ё",
    "ж",
    "з",
    "и",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ъ",
    "ы",
    "ь",
    "э",
    "ю",
    "я",
]

# result  = ''

# # Перебор списков на 3х циклах, самое наглядное
# for data in secret_letter:
#     # Перебор строк
#     for string in data:
#         result += ' '
#         for letter in string:
#             if letter in small_rus:
#                 result += letter


# result = result.strip().capitalize()
# print(result)


result = ""
# На двух циклах самое оптимальное

for data in secret_letter:
    result += " "
    for letter in data[0]:
        if letter in small_rus:
            result += letter

result = result.strip().capitalize()

print(result)

# List comprehension (без добавления пробелов)
result_list = [word for data in secret_letter for word in data[0] if word in small_rus]

result = "".join(result_list).strip().capitalize()

print(result)
