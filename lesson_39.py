# Lesson 39: Множественное наследование. MRO. Миксины

class A:
    def greet(self):
        print('Привет из класса A')

class B:
    def greet(self):
        print('Привет из класса B')


class C(B, A):
    
    def greet(self):
        print('Привет из класса C')
    pass

c = C()
c.greet()

# MRO - Method Resolution Order - Метод разрешения порядка
print(C.mro())