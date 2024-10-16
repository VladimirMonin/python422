"""
Lesson 40
Магическиее методы 
1. __call__
2. __bool__
3. __len__
4. __repr__

5. Математика и сравнение
6. Dataclass
Сериализация и десериализация через eval()
"""

# Пицца, ПиццаСоздатель __call__


class Pizza:
    
    names = ['Маргарита', 'Пепперони', 'Гавайская']
    def __init__(self, name: str, price: float, size: int):
        self.name = name
        self.price = price
        self.size = size
        self.done = False

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return self.done
    

# Создатель пиццы. Call - создает пиццу принимая название, цену и размер

class PizzaCreator:
    def __call__(self) -> Pizza|None:
        self.print_menu()
        name = input('Введите название пиццы: ')
        price = float(input('Введите цену пиццы: '))
        size = int(input('Введите размер пиццы: '))

        if self.validate_name(name):
            return Pizza(name, price, size)

    
    def print_menu(self):
        for pizza in Pizza.names:
            print(pizza)

    def validate_name(self,  name: str) -> bool:
        if not name:
            raise ValueError('Название пиццы не может быть пустым')
        if not name.isalpha():
            raise ValueError('Название пиццы должно содержать только буквы')
        if name not in Pizza.names:
            raise ValueError('Такой пиццы нет в меню')
        
        return True


pc = PizzaCreator()
pizza = pc()


p1 = Pizza('Маргарита', 100, 30)
p2 = Pizza('Пепперони', 150, 30)
p3 = Pizza('Гавайская', 120, 30)

"Pizza('Маргарита', 100, 30), Pizza('Пепперони', 150, 30), Pizza('Гавайская', 120, 30)"
repr