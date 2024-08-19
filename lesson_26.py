from lesson_25 import *
# Правила наименования функций
# get_item_by_id   get_item_by_slug  get_name_by_id
# check_user_by_id  check_user_by_slug  check_user_by_name
# позиционность!
kwargs_print = {
    "sep": "\n",
    "end": "\n\n"
}

name_dict = {
    "name": "Vladimir",
    "last_name": "Monin",
    "age": 30,
    "city": "Moscow"
}


print(1, sep="\n", end="\n\n")

print(1, **kwargs_print)
