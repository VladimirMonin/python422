# Lesson 39: Множественное наследование. MRO. Миксины
# __init__ и __new__ как две половины конструктора классов в Pythyon

class Plate():
    
    def __init__(self, size):
        self.size = size

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


p = Plate(10)

# Паттерн проектирования "Одиночка"

class SingleTonePlate():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, color):
        # Тут мы можем добавить такое же условие, и не выполнять
        # инициализацию, если объект уже создан
        # if not hasattr(self, 'color'):
        self.color = color

plate1 = SingleTonePlate('red')
plate2 = SingleTonePlate('blue')
plate3 = SingleTonePlate('green')

print(plate1 is plate2)
print(plate1 is plate3)
print(plate2 is plate3)

print(plate1)
print(plate2)
print(plate3)

print(plate1.color)
print(plate2.color)
print(plate3.color)

"""
# Заметка о работе оператора 'is' в Python:
# Оператор 'is' в Python проверяет идентичность объектов, а не их значения.
# Он сравнивает идентификаторы объектов (их адреса в памяти).
# Два объекта считаются идентичными, если они ссылаются на одну и ту же область памяти.
# В случае с SingleTonePlate, все экземпляры класса ссылаются на один и тот же объект в памяти,
# поэтому 'is' возвращает True при их сравнении.
# Важно отметить, что 'is' отличается от '==', который сравнивает значения объектов.
"""