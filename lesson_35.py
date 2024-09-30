"""
Lesson 35. Знакомство с ООП
- Правила нейминга. UpperCamelCase  (похоже на переменные)
- Class - ключевое слово для создания класса
"""

class Cat:
    pass

cat1 = Cat()
cat2 = Cat()

print(cat1) # <__main__.Cat object at 0x00000209DA4D1F10>
print(cat2) # <__main__.Cat object at 0x00000209DA4D1E80>
print(type(cat1)) # <class '__main__.Cat'>
print(type(cat2)) # <class '__main__.Cat'>
print(id(cat1)) # 2241340448528
print(id(cat2)) # 2241340448384

##### Мы можем добавить данных котам

cat1.name = 'Барсик'
print(cat1.name) # Барсик
cat2.name = 'Мурка'
print(cat2.name) # Мурка
