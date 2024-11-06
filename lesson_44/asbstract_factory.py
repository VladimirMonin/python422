from abc import ABC, abstractmethod
from typing import List

# Абстрактные классы юнитов
class Warrior(ABC):
    """Базовый класс для всех воинов."""
    @abstractmethod
    def attack(self) -> None:
        pass

    @abstractmethod
    def defend(self) -> None:
        pass

class Archer(ABC):
    """Базовый класс для всех лучников."""
    @abstractmethod
    def shoot(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass

class Mage(ABC):
    """Базовый класс для всех магов."""
    @abstractmethod
    def cast_spell(self) -> None:
        pass

    @abstractmethod
    def heal(self) -> None:
        pass

# Конкретные классы человеческих юнитов
class HumanWarrior(Warrior):
    """Воин человеческой расы."""
    def attack(self) -> None:
        print("Человек-воин наносит удар мечом!")

    def defend(self) -> None:
        print("Человек-воин защищается щитом!")

class HumanArcher(Archer):
    """Лучник человеческой расы."""
    def shoot(self) -> None:
        print("Человек-лучник стреляет из длинного лука!")

    def move(self) -> None:
        print("Человек-лучник перемещается на новую позицию!")

class HumanMage(Mage):
    """Маг человеческой расы."""
    def cast_spell(self) -> None:
        print("Человек-маг читает заклинание огненного шара!")

    def heal(self) -> None:
        print("Человек-маг восстанавливает здоровье союзникам!")

# Конкретные классы орочьих юнитов
class OrcWarrior(Warrior):
    """Воин орочьей расы."""
    def attack(self) -> None:
        print("Орк-воин наносит удар боевым топором!")

    def defend(self) -> None:
        print("Орк-воин принимает защитную стойку!")

class OrcArcher(Archer):
    """Лучник орочьей расы."""
    def shoot(self) -> None:
        print("Орк-лучник стреляет из композитного лука!")

    def move(self) -> None:
        print("Орк-лучник совершает тактическое перемещение!")

class OrcShaman(Mage):
    """Шаман орочьей расы."""
    def cast_spell(self) -> None:
        print("Орк-шаман призывает силы природы!")

    def heal(self) -> None:
        print("Орк-шаман исцеляет соратников тотемом!")

# Абстрактная фабрика юнитов
class UnitFactory(ABC):
    """Абстрактная фабрика для создания юнитов."""
    @abstractmethod
    def create_warrior(self) -> Warrior:
        pass

    @abstractmethod
    def create_archer(self) -> Archer:
        pass

    @abstractmethod
    def create_mage(self) -> Mage:
        pass

# Конкретные фабрики
class HumanFactory(UnitFactory):
    """Фабрика для создания человеческих юнитов."""
    def create_warrior(self) -> Warrior:
        return HumanWarrior()

    def create_archer(self) -> Archer:
        return HumanArcher()

    def create_mage(self) -> Mage:
        return HumanMage()

class OrcFactory(UnitFactory):
    """Фабрика для создания орочьих юнитов."""
    def create_warrior(self) -> Warrior:
        return OrcWarrior()

    def create_archer(self) -> Archer:
        return OrcArcher()

    def create_mage(self) -> Mage:
        return OrcShaman()

class GameWorld:
    """
    Игровой мир, который использует фабрику для создания армий разных рас.
    """
    def __init__(self, unit_factory: UnitFactory):
        self.unit_factory = unit_factory

    def create_army(self) -> List[object]:
        """Создает армию определенной расы."""
        army = []
        
        warrior = self.unit_factory.create_warrior()
        archer = self.unit_factory.create_archer()
        mage = self.unit_factory.create_mage()
        
        army.extend([warrior, archer, mage])
        return army

# Пример использования
if __name__ == "__main__":
    print("Создание человеческой армии:")
    human_world = GameWorld(HumanFactory())
    human_army = human_world.create_army()
    
    for unit in human_army:
        if isinstance(unit, Warrior):
            unit.attack()
            unit.defend()
        elif isinstance(unit, Archer):
            unit.shoot()
            unit.move()
        elif isinstance(unit, Mage):
            unit.cast_spell()
            unit.heal()
    
    print("\nСоздание орочьей армии:")
    orc_world = GameWorld(OrcFactory())
    orc_army = orc_world.create_army()
    
    for unit in orc_army:
        if isinstance(unit, Warrior):
            unit.attack()
            unit.defend()
        elif isinstance(unit, Archer):
            unit.shoot()
            unit.move()
        elif isinstance(unit, Mage):
            unit.cast_spell()
            unit.heal()
