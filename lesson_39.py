# Lesson 39: Множественное наследование. MRO. Миксины

"""
Миксин для форматированного вывода: 

Создайте PrintableMixin, который добавляет метод pretty_print() для красивого вывода информации об объекте. Примените его к классу Person с атрибутами name и age.

1. Создать Person с атрибутами name и age.
2. Создать PrintableMixin с методом pretty_print(). который вывыводит информацию о Person в красивом формате.
Взаимодействуя с миксинами name и age, которых в самом миксине нет.
3. Создать класс Student, который наследуется от Person и PrintableMixin.
4. Создать объект класса Student с атрибутами name, age, и вывести его информацию в красивом формате.
"""



class Person:
    type = "Персона"
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PrintableMixin:
    
    def pretty_print(self):
        print(f"{self.__class__.type}: {self.name},\nВозраст: {self.age} лет.")


class Student(Person, PrintableMixin):
    type = "Студент"
    pass


class Employee(Person, PrintableMixin):
    type = "Сотрудник"
    pass

student = Student("Спиридон", 20)
student.pretty_print()

employee = Employee("Никифор", 25)
employee.pretty_print()