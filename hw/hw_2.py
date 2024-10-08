# Разбор HW2

from random import choice

proverbs = [
    "Ум хорошо, а два лучше.",
    "Ум — горячая штука.",
    "Ум всё голова.",
    "Умом Россию не понять.",
    "Ум бережет, а глупость губит.",
    "Ум в голову приходит.",
    "Ум от ума не горит.",
    "Умом нагружен, а волосы развеваются.",
    "Умом обдумал, а ногами пошел.",
    "Ум — сокровище, не пропадет без него и копье на ветру.",
    "Ум — грех, а бес — мера.",
    "Ум есть богатство.",
    "Ум роднит народы.",
    "Ум краток, да забот — бездна.",
    "Ум не камень, взял и положил.",
    "Ум не велит, а наставляет.",
    "Ум с мерой, а глупость без меры.",
    "Ум — сокол, глаз его — телескоп.",
    "Ум — не конская морда, не разобьешь.",
    "Ум — семь пядей во лбу.",
    "Ум — не барсук, в нору не залезет.",
    "Ум в голове, а не на ветру.",
    "Ум греет душу, а глупость терпение.",
    "Ум служит человеку, а глупость — хозяином.",
    "Ум мил, да безумству хозяин.",
    "Ум в труде, да наслаждение в праздности.",
    "Ум глаза исправляет.",
    "Ум человека не обманешь.",
    "Ум на подобии огня — без сна не останешься.",
    "Ум к уму приходит.",
    "Ум с пользой тратит время.",
    "Ум желание творит.",
    "Ум общего дела дело.",
    "Ум — друг, а воля — враг.",
    "Ум — бесценное сокровище.",
    "Ум тонок, да разум невелик.",
    "Ум — враг бедности.",
    "Ум — теремок, да не на прокол.",
    "Ум силен, да не камень.",
    "Ум рассудит, что сердце не посоветует.",
    "Ум — подкова, а топор — ось.",
    "Ум легче камня, да весомей золота.",
    "Ум не вешать на гроздья.",
    "Ум — не мешок, на плечи не вешай.",
    "Ум — лучшая победа.",
    "Ум — в суде велик, а в деле своем мал.",
    "Ум голове краса.",
    "Ум — сокровище, а глупость — нищета.",
    "Ум человека — огонь, а глаза — масло.",
    "Ум — путь, а дорога — конец.",
    "Ум стоит денег.",
    "Ум от смеха бьет в ладоши.",
    "Ум — коза, к барскому плечу привыкает.",
    "Ум — лезвие, а лень — ржавчина.",
    "Ум на вершине — мир в руках.",
]

variants = [
    "кот",
    "шеф",
    "мозг",
    "лес",
    "фолк",
    "код",
    "рот",
    "мёд",
    "лук",
    "лес",
    "год",
    "час",
    "друг",
    "жена",
    "муж",
    "айфон",
    "работа",
]


# input_num_prowerbs = int(input('Введите количество пословиц: '))
# result_proverbs = []

# proverbs_set = set(proverbs)
# variants_set = set(variants)

# while (proverbs_set and variants_set) and len(result_proverbs) < input_num_prowerbs:
#     proverbs_item = proverbs_set.pop()
#     variants_item = variants_set.pop()
#     new_proverb = proverbs_item.lower().replace('ум', variants_item).capitalize()
#     result_proverbs.append(new_proverb)


# [print(proverb) for proverb in result_proverbs]


# Вариант №2
# proverbs_set = set(proverbs)
# variants_set = set(variants)

# result_set = set()
# max_result = len(proverbs) * len(variants)

# print(f"Возможный максимум пословиц: {max_result}")
# input_num_prowerbs = int(input("Введите количество пословиц: "))

# if input_num_prowerbs > max_result:
#     raise ValueError("Слишком большое количество пословиц")

# count = 0
# while len(result_set) < input_num_prowerbs:
#     random_proverb = choice(proverbs)
#     random_variant = choice(variants)
#     new_proverb = random_proverb.lower().replace("ум", random_variant).capitalize()
#     result_set.add(new_proverb)
#     count += 1
#     print(f"Итераций: {count}")

# Вариант от Константина
"""
Создать копию списков, и внутри цикла идти по ним,
чтобы не было холостых итераций.

Как только одна из коллекций закончится, обновлять копию.

TODO: Где появляется 935 пословиц, если 880 - максимум?
"""
