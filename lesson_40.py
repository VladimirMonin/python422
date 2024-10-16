"""
Lesson 40
Магическиее методы 
1. __call__
2. __bool__
3. __len__
"""

class Person:
    def __init__(self, name: str, height:int, is_working: bool):
        self.name = name
        self.is_working = is_working
        self.height = height

    def __bool__(self):
        return self.is_working
    
    def __len__(self):
        return self.height
    
    def __str__(self) -> str:
        return f'{self.name} {self.height} {self.is_working}'
    
    def __repr__(self) -> str:
        return self.__str__()
    

p = Person('Евгений', 175, True)

if p:
    print(f'{p.name} работает')
else:
    print(f'{p.name} не работает')

persons_list = [
    Person('Евгений', 175, True),
    Person('Ольга', 166, False),
    Person('Владимир', 182, True),
    Person('Наталия', 171, False),
]

# Фильтр
persons_list_filter = list(filter(bool, persons_list))
# persons_list2 = list(filter(lambda p: p.is_working, persons_list))

# Сортировка по росту
persons_list.sort(key=len)

print(persons_list_filter)
print(persons_list)


