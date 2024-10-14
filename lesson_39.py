# Lesson 39: Множественное наследование. MRO. Миксины
import time
class A:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.time = time.time()
        
    def greet(self):
        print(f'Привет из A. Name: {self.name}, age: {self.age}')

    def bye(self):
        print(f'Пока из A. Name: {self.name}, age: {self.age}, time: {self.time}')

class B:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def greet(self):
        print(f'Привет из B. Name: {self.name}, age: {self.age}')



class C(B, A):
    def __init__(self, name, age) -> None:
        # "Оттолкнись от B в MRO и вызови A __init__"
        super(B, self).__init__(name, age)
    
    def greet(self):
        print(f'Привет из C. Name: {self.name}, age: {self.age}')
        super(C, self).greet() # super().greet() Вызывается метод greet класса B
        super(B, self).greet() # Вызывается метод greet класса А
        

c = C('Alex', 25)
c.greet()
c.bye()
