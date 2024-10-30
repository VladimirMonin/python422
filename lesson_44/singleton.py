"""
Singleton - Одиночка.
"""

class DBConnection:
    """
    Класс для подключения к базе данных, реализующий паттерн Singleton.
    Гарантирует, что будет создан только один экземпляр подключения к БД.
    """
    _instance = None  # Приватное поле для хранения единственного экземпляра

    def __new__(cls):
        """
        Переопределяем метод создания нового объекта.
        Если экземпляр еще не создан - создаем его.
        Если уже существует - возвращаем существующий.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print(f"Создание нового подключения к БД: {id(cls._instance)}")
        return cls._instance

    def __init__(self):
        """
        Инициализация подключения к БД.
        Выполняется только при первом создании экземпляра.
        """
        if not hasattr(self, 'initialized'):
            print("Инициализация подключения к БД...")
            self.host = 'localhost'
            self.port = 5432
            self.db_name = 'test_db'
            self.initialized = True

    def get_connection_info(self):
        """Получение информации о подключении"""
        return f"Подключение к {self.db_name} на {self.host}:{self.port}"


# Демонстрация работы синглтона
if __name__ == "__main__":
    # Создаем первый экземпляр
    db1 = DBConnection()
    print(f"ID первого экземпляра: {id(db1)}")
    print(db1.get_connection_info())

    # Создаем второй экземпляр
    db2 = DBConnection()
    print(f"ID второго экземпляра: {id(db2)}")
    print(db2.get_connection_info())

    # Проверяем, что это один и тот же объект
    print(f"db1 и db2 - один и тот же объект: {db1 is db2}")


