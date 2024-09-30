"""
Lesson 35. Знакомство с ООП
- Правила нейминга. UpperCamelCase  (похоже на переменные)
- Class - ключевое слово для создания класса
- Атрибуты класса и работа с ними
- __init__ как метод дающий уникальные свойства объекту
- Атрибуты экземпляра класса
- Метод __str__ как метод дающий возможность принтить объект
- Методы экземпляра класса, в т.ч. принимающие аргументы
- Класс TxtFile для работы с текстовыми файлами
"""

class TxtFile:
    def __init__(self, path:str):
        self.path = path
        self.text: str = ''

    def read(self, enconding: str ='utf-8') -> str:
        """
        Метод для чтения текстового файла
        :param path: путь к файлу
        :return: текст файла
        """
        with open(self.path, 'r', encoding=enconding) as f:
             self.text = f.read()
             return self.text
        
    def write(self, text:str, encoding: str = 'utf-8') -> None:
        """
        Метод для записи строки в текстовый файл
        Автоматически добавляет перенос строки
        :param path: путь к файлу
        """
        with open(self.path, 'w', encoding=encoding) as f:
            f.write(text + '\n')


    def append(self, text:str, encoding: str ='utf-8') -> None:
        """
        Метод для дозаписи строки в текстовый файл
        Автоматически добавляет перенос строки
        :param path: путь к файлу
        """
        with open(self.path, 'a', encoding=encoding) as f:
             f.write(text + '\n')

TXT_FILE = 'lesson_35_text.txt'
file1 = TxtFile(TXT_FILE)
file1.write('Hello world!')