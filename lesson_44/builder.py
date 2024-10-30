"""
Паттерн Builder - рассматриваем на пирмере Pizza строителя

1. PizzaDirector - который знает все рецепты и руководит процессом постройки
2. AbstractPizzaBuilder - который содержит в себе минимальный набор абстрактных методов (типа добавить соус, сыр, начинка, раскатать тесто, начать новую пиццу, и вернуть пиццу (готовую))
3. Конкретные пица строители в количестве 2 штук
- PeperoniBuilder 
- CilliChikenBuilder

Они будут строить конкртеные пиццы

4. Сам класс Pizza
- Документация на русском 
- Аннотация типов
"""

from abc import ABC, abstractmethod
from typing import List

class Pizza:
    """Класс пиццы, который содержит все компоненты и методы для работы с пиццей"""
    
    def __init__(self) -> None:
        self.dough: str = ""
        self.sauce: str = ""
        self.cheese: str = ""
        self.toppings: List[str] = []

    def cheese_pull(self) -> None:
        pass
        
    def __str__(self) -> str:
        return f"Пицца: {self.dough}, {self.sauce}, {self.cheese}, {', '.join(self.toppings)}"

class AbstractPizzaBuilder(ABC):
    """Абстрактный класс строителя пиццы"""
    
    def __init__(self) -> None:
        self.pizza: Pizza = Pizza()
        
    @abstractmethod
    def reset(self) -> None:
        """Сброс пиццы для начала нового приготовления"""
        pass
    
    @abstractmethod
    def prepare_dough(self) -> None:
        """Подготовка теста"""
        pass
    
    @abstractmethod
    def add_sauce(self) -> None:
        """Добавление соуса"""
        pass
    
    @abstractmethod
    def add_cheese(self) -> None:
        """Добавление сыра"""
        pass
    
    @abstractmethod
    def add_toppings(self) -> None:
        """Добавление топпингов"""
        pass
    
    def get_pizza(self) -> Pizza:
        """Получение готовой пиццы"""
        return self.pizza

class PeperoniBuilder(AbstractPizzaBuilder):
    """Строитель пиццы Пепперони"""
    
    def reset(self) -> None:
        self.pizza = Pizza()
        
    def prepare_dough(self) -> None:
        self.pizza.dough = "Тонкое тесто"
        
    def add_sauce(self) -> None:
        self.pizza.sauce = "Томатный соус"
        
    def add_cheese(self) -> None:
        self.pizza.cheese = "Моцарелла"
        self.pizza.cheese_pull = lambda: print("Сыр тянется длинными белыми нитями, как настоящая итальянская моцарелла")
        
    def add_toppings(self) -> None:
        self.pizza.toppings = ["Пепперони", "Орегано"]

class ChilliChickenBuilder(AbstractPizzaBuilder):
    """Строитель острой куриной пиццы"""
    
    def reset(self) -> None:
        self.pizza = Pizza()
        
    def prepare_dough(self) -> None:
        self.pizza.dough = "Толстое тесто"
        
    def add_sauce(self) -> None:
        self.pizza.sauce = "Острый соус"
        
        
    def add_cheese(self) -> None:
        self.pizza.cheese = "Чеддер"
        self.pizza.cheese_pull = lambda: print("Сыр тянется плотно и равномерно, образуя золотистые тягучие нити")
        
    def add_toppings(self) -> None:
        self.pizza.toppings = ["Курица", "Перец чили", "Лук"]

class PizzaDirector:
    """Директор, который знает рецепты и руководит процессом приготовления"""
    
    def __init__(self, builder: AbstractPizzaBuilder) -> None:
        self.builder = builder
        
    def change_builder(self, builder: AbstractPizzaBuilder) -> None:
        """Смена строителя"""
        self.builder = builder
        
    def make_pizza(self) -> Pizza:
        """Процесс приготовления пиццы"""
        self.builder.reset()
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_cheese()
        self.builder.add_toppings()
        return self.builder.get_pizza()

def main():
    # Создаем строителей
    peperoni_builder = PeperoniBuilder()
    chilli_chicken_builder = ChilliChickenBuilder()
    
    # Создаем директора
    director = PizzaDirector(peperoni_builder)
    
    # Готовим пепперони
    peperoni = director.make_pizza()
    print(peperoni)
    peperoni.cheese_pull()
    
    # Меняем строителя и готовим острую куриную
    director.change_builder(chilli_chicken_builder)
    chilli_chicken = director.make_pizza()
    print(chilli_chicken)
    chilli_chicken.cheese_pull()

if __name__ == "__main__":
    main()
