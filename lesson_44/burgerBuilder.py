"""
Практика!

Структура классов

1. Класс Burger (Продукт)
Атрибуты:
булочка (str)
котлета (str)
сыр (str)
соус (str)
Метод:
str для вывода состава бургера

2. Класс CheeseburgerBuilder
Методы:
build() - создаёт и возвращает готовый чизбургер
add_ingredients() - добавляет все ингредиенты

3. Класс FishburgerBuilder
Методы:
build() - создаёт и возвращает готовый фишбургер
add_ingredients() - добавляет все ингредиенты

4. Main (точка входа)
Создание и вывод обоих видов бургеров
Требования
Каждый строитель должен создавать уникальный состав бургера
Логика создания должна быть инкапсулирована в строителях
Минимальное количество методов для демонстрации работы паттерна
Ожидаемый результат
При запуске программы должны создаваться и выводиться на экран составы двух разных бургеров.
"""

class Burger():
    """
    Продукт - бургер
    """
    def __init__(self) -> None:
        self.bun: str = "" # булочка
        self.patty: str = "" # котлета
        self.cheese: str = "" # сыр
        self.sauce: str = "" # соус

    def __str__(self) -> str:
        return f"Булочка: {self.bun}, котлета: {self.patty}, сыр: {self.cheese}, соус: {self.sauce}"
    

class CheeseburgerBuilder():
    """
    Строитель чизбургера
    """
    def __init__(self) -> None:
        self.burger: Burger = Burger()

    def add_bun(self) -> None:
            self.burger.bun = "Булочка для чизбургера"

    def add_patty(self) -> None:
            self.burger.patty = "Говяжья котлета"

    def add_cheese(self) -> None:
            self.burger.cheese = "Сыр Чеддер"
    
    def add_sauce(self) -> None:
            self.burger.sauce = "Соус бургер"

    def add_cheese_pull(self):
        def cheese_pull():
            print("Сыр тянется золотистыми ароматными нитями...")
        
        self.burger.cheese_pull = cheese_pull

    def add_ingredients(self) -> None:
        self.add_bun()
        self.add_patty()
        self.add_cheese()
        self.add_sauce()
        self.add_cheese_pull() # Добавляем секретный метод

    def build(self) -> Burger:
        self.add_ingredients()
        return self.burger
    
class FishburgerBuilder():
    """
    Строитель фишбургера
    """
    def __init__(self) -> None:
        self.burger: Burger = Burger()
    
    def add_bun(self) -> None:
            self.burger.bun = "Булочка для фишбургера"

    def add_patty(self) -> None:
            self.burger.patty = "Рыбная котлета"

    def add_cheese(self) -> None:
            self.burger.cheese = "Сыр Чеддер"
    
    def add_sauce(self) -> None:
            self.burger.sauce = "Соус фишбургер"

    def add_ingredients(self) -> None:
        self.add_bun()
        self.add_patty()
        self.add_cheese()
        self.add_sauce()

    def build(self) -> Burger:
        self.add_ingredients()
        return self.burger
    


# Работа с классами

ch_burger = CheeseburgerBuilder().build()
fish_burger = FishburgerBuilder().build()

print(ch_burger)
print(fish_burger)

ch_burger.cheese_pull()