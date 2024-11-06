from abc import ABC, abstractmethod

# Базовый абстрактный класс состояния
class CatState(ABC):
    @abstractmethod
    def meow(self, cat: "Cat"):
        pass

# Конкретное состояние - Голодный кот
class HungryCatState(CatState):
    def meow(self, cat: "Cat"):
        print(f"😾 Голодный кот (id={id(cat)}) громко мяукает МЯЯЯЯУ!")
        # Покормили кота - он стал счастливым
        cat.set_state(HappyCatState())

# Конкретное состояние - Счастливый кот
class HappyCatState(CatState):
    def meow(self, cat: "Cat"):
        print(f"😺 Счастливый кот (id={id(cat)}) мурлычет мур-мур")

# Главный класс - Кот
class Cat:
    def __init__(self):
        # При создании кот голодный
        self._state = HungryCatState()
        print(f"🐱 Создан новый кот (id={id(self)})")
    
    def set_state(self, state: CatState):
        # Метод для смены состояния
        print(f"🔄 Кот (id={id(self)}) меняет состояние на {state.__class__.__name__}")
        self._state = state
    
    def meow(self):
        # При вызове meow() у кота, он делегирует выполнение 
        # текущему состоянию, передавая ссылку на самого себя
        print(f"➡️ Кот (id={id(self)}) делегирует meow() в {self._state.__class__.__name__}")
        self._state.meow(self)

# Тестируем
if __name__ == "__main__":
    # Создаем кота
    cat = Cat()
    
    # Кот мяукает когда голодный
    cat.meow()
    
    # Кот мяукает когда счастливый
    cat.meow()
