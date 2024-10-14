# Lesson 39: Множественное наследование. MRO. Миксины

class A:
    def greet(self):
        print('Привет из класса A')

class B:
    def greet(self):
        print('Привет из класса B')
        # Это обозначается как ошибка, но когда B попадает в C там
        # Есть вышестоящий метод greet() из класса A
        # super().greet()


class C(B, A):
    
    def greet(self):
        print('Привет из класса C')
        # Вызываем метод greet() из класса B
        # super().greet()
        # A.greet(self)
        # B.greet(self)
        
        # Еще один способ вызвать метод вышестоящего класса
        super(C, self).greet()
        super(B, self).greet()
        

    pass

c = C()
c.greet()

# MRO - Method Resolution Order - Метод разрешения порядка
# self.__class__.__mro__[1].greet(self) - как один из способов вызвать метод из класса B
print(C.mro())
print(C.__mro__[2].__name__)