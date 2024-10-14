# Lesson 39: Множественное наследование. MRO. Миксины

# Порядок  разрешения методов в иерахическом наследовании

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def hello(self):
        print('Hello from A')

    def __str__(self):
        return f'Это __str__ класса: {self.__class__.__name__} а так же от Object {super().__str__()}'


class X(A):
    def hello(self):
        print('Hello from X')


class Y(X):
    def hello(self):
        print('Hello from Y')

class Z(Y):
    def hello(self):
        print('Hello from Z')


z = Z()
# MRO
print(Z.mro())
print(z.__class__.__mro__)
print(z)