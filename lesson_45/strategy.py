from typing import Optional, Protocol


class RangedAttackStrategy(Protocol):
    """Интерфейс для стратегий дальних атак"""
    
    def execute_attack(self, distance: float) -> int:
        """Выполнить атаку на указанной дистанции"""
        pass
    

    def get_max_range(self) -> float:
        """Получить максимальную дальность атаки"""
        pass


class Character:
    """Базовый класс игрового персонажа"""
    
    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self._attack_strategy: Optional[RangedAttackStrategy] = None
        
    def attack(self, target_distance: float) -> None:
        """Атаковать цель на указанной дистанции"""
        if not self._attack_strategy:
            print(f"{self.name} не может атаковать - не выбрана стратегия!")
            return
            
        if target_distance > self._attack_strategy.get_max_range():
            print(f"{self.name} не может атаковать - цель слишком далеко!")
            return
            
        damage = self._attack_strategy.execute_attack(target_distance)
        print(f"{self.name} наносит {damage} урона на дистанции {target_distance}")
        
    def set_attack_strategy(self, strategy: RangedAttackStrategy) -> None:
        """Установить стратегию атаки"""
        self._attack_strategy = strategy
        print(f"{self.name} меняет стратегию атаки")


class BowAttackStrategy:
    """Стратегия атаки луком"""
    
    def __init__(self, bow_damage: int = 20):
        self.bow_damage = bow_damage
        self._max_range = 40.0
        
    def execute_attack(self, distance: float) -> int:
        # Урон уменьшается с расстоянием
        damage_multiplier = 1 - (distance / self._max_range) * 0.5
        return int(self.bow_damage * damage_multiplier)
        
    def get_max_range(self) -> float:
        return self._max_range


class MagicAttackStrategy:
    """Стратегия атаки магией"""
    
    def __init__(self, spell_power: int = 30, mana_cost: int = 10):
        self.spell_power = spell_power
        self.mana_cost = mana_cost
        self._max_range = 50.0
        
    def execute_attack(self, distance: float) -> int:
        # Магия не теряет силу с расстоянием
        return self.spell_power
        
    def get_max_range(self) -> float:
        return self._max_range


class CrossbowAttackStrategy:
    """Стратегия атаки арбалетом"""
    
    def __init__(self, crossbow_damage: int = 35, reload_time: float = 2.0):
        self.crossbow_damage = crossbow_damage
        self.reload_time = reload_time
        self._max_range = 60.0
        
    def execute_attack(self, distance: float) -> int:
        # Арбалет наносит фиксированный урон до определенной дистанции
        if distance <= self._max_range * 0.7:
            return self.crossbow_damage
        # После теряет урон быстрее лука
        damage_multiplier = 1 - (distance / self._max_range) * 0.8
        return int(self.crossbow_damage * damage_multiplier)
        
    def get_max_range(self) -> float:
        return self._max_range


# Пример использования
if __name__ == "__main__":
    # Создаем персонажа
    archer = Character("Лучник")
    
    # Создаем разные стратегии
    bow = BowAttackStrategy()
    magic = MagicAttackStrategy()
    crossbow = CrossbowAttackStrategy()
    
    # Тестируем разные стратегии
    archer.attack(30)  # Без стратегии
    
    archer.set_attack_strategy(bow)
    archer.attack(20)  # Ближняя дистанция
    archer.attack(35)  # Дальняя дистанция
    archer.attack(45)  # Слишком далеко
    
    archer.set_attack_strategy(magic)
    archer.attack(40)  # Магическая атака
    
    archer.set_attack_strategy(crossbow)
    archer.attack(30)  # Арбалет ближняя дистанция
    archer.attack(50)  # Арбалет дальняя дистанция
