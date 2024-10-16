"""
Разбор домашней работы №14 - "Работа с архивами"

В данной программе будет реализована система классов для работы с архивами, что позволит пользователям легко создавать, извлекать и манипулировать файлами в различных форматах архивов, таких как ZIP, RAR и 7z. Основная архитектура программы будет состоять из абстрактного класса `Archive`, который будет задавать общий интерфейс для всех типов архивов. Классы-наследники будут реализовывать конкретные методы для работы с каждым типом архива.

Структура классов

1. **Абстрактный базовый класс `AbstractArchive`**
   - Определите абстрактные методы для распаковки архивов.

2. **Классы-наследники**
   - **`ZipArchive`**
     - Реализует методы для работы с ZIP-архивами.
   - **`RarArchive`**
     - Реализует методы для работы с RAR-архивами.
   - **`SevenZipArchive`**
     - Реализует методы для работы с 7z-архивами.

3. **Класс-миксин `FileSystemWalker`**
   - Отвечает за рекурсивный обход папок и файлов.

4. **Класс-миксин `MarkdownGenerator`**
   - Хранит список расширений файлов (js, sql, html, css, py).
   - Читает содержимое файлов с указанными расширениями.
   - Накапливает прочитанные данные в формате Markdown.
   - Предоставляет метод для получения итоговой Markdown-заметки.

5. **Главный класс `ArchiveExtractor`**
   - Использует миксины `FileSystemWalker` и `MarkdownGenerator`.
   - **В инициализаторе** определяет тип входного архива.
   - Создает соответствующий объект-распаковщик на основе типа архива **в атрибуте экземпляра.**
   - Выполняет распаковку содержимого в текущую папку, создавая новую директорию с именем архива.
   - Генерирует Markdown-заметку с содержимым распакованных файлов.

"""
# Импорт абстрактного базового класса и декоратора для создания абстрактных методов
from abc import ABC, abstractmethod

# Импорт модуля для работы с операционной системой и файловой структурой
import os
import shutil  

# Импорт модулей для работы с различными форматами архивов
import zipfile
import rarfile
import py7zr

class AbstractArchive(ABC):
    """Абстрактный базовый класс для работы с архивами.
    Обязывает реализовать метод для распаковки архивов.
    """

    @abstractmethod
    def extract(self, file_path: str, extract_path: str) -> None:
        """Распаковка архива."""
        pass


class ZipArchive(AbstractArchive):

    def extract(self, file_path: str, extract_path: str) -> None:
        """Распаковка ZIP-архива."""
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)


class RarArchive(AbstractArchive):
    
    def extract(self, file_path: str, extract_path: str) -> None:
        """Распаковка RAR-архива."""
        with rarfile.RarFile(file_path, 'r') as rar_ref:
            rar_ref.extractall(extract_path)


class SevenZipArchive(AbstractArchive):
    
    def extract(self, file_path: str, extract_path: str) -> None:
        """Распаковка 7z-архива."""
        with py7zr.SevenZipFile(file_path, 'r') as sz_ref:
            sz_ref.extractall(extract_path)

class FileSystemWalkerMixin:
    """Миксин для рекурсивного обхода файлов и папок."""
    def walk_files_and_dirs(self, path: str, base_path: str) -> None:
        
        for root, dirs, files in os.walk(path):
            for file in files:
                # Формирование полного пути к файлу
                file_path = os.path.join(root, file)
                # Получение относительного пути файла
                relative_path = os.path.relpath(file_path, base_path)
                # Обработка файла с использованием полного и относительного путей
                self.process_file(file_path, relative_path)

class MarkdownGeneratorMixin:
    """Миксин для генерации Markdown-заметки."""
    def __init__(self):
        # Инициализация контента для Markdown и поддерживаемых расшир файлов
        self.markdown_content = ""
        self.supported_extensions = ['py', 'sql', 'js', 'css', 'html']

    def process_file(self, file_path: str, relative_path: str) -> None:
        """Обработка файла."""
        # Получение расширения файла
        file_extension = os.path.splitext(file_path)[1][1:]
        # Проверка, поддерживается ли данное расширение
        if file_extension in self.supported_extensions:
            try:
                # Попытка открыть файл с кодировкой UTF-8
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
            except UnicodeDecodeError:
                # Если произошла ошибка декодирования, пробуем открыть с кодировкой CP1251
                try:
                    with open(file_path, 'r', encoding='cp1251') as file:
                        file_content = file.read()
                except Exception as e:
                    # Обработка ошибок чтения файла
                    print(f"Не удалось прочитать файл {file_path}: {e}")
                    return
            # Получение имени файла для заголовка
            file_name = os.path.basename(file_path)
            # Получение относительного пути к директории
            dirname = os.path.dirname(relative_path)
            if dirname == ".":
                dirname = ""
            else:
                # Замена обратных слешей на прямые в относительном пути
                dirname = dirname.replace("\\", "/") 
            # Формирование заголовка для Markdown
            header = f"## {dirname} \\ {file_name}" if dirname else f"## {file_name}"
            # Добавление содержимого файла в Markdown
            self.markdown_content += (
                f"{header}\n"
                f"{file_extension}\n"
                f"{file_content}\n"
                "\n\n"
            )
    def save_markdown_file(self, file_path: str) -> None:
        """Сохранение сформированной Markdown-заметки в файл."""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.markdown_content)


class ArchiveExtractor(FileSystemWalkerMixin, MarkdownGeneratorMixin):
    """Главный класс для распаковки архивов и генерации Markdown-заметки."""
    def __init__(self, file_path: str):
        MarkdownGeneratorMixin.__init__(self)
        # Инициализация пути к архиву и создание экстрактора
        self.file_path = file_path
        self.archive = self._create_archive_extractor()

    def _create_archive_extractor(self) -> AbstractArchive:
        # Определение типа архива и создание соответствующего экстрактора
        if self.file_path.endswith('.zip'):
            return ZipArchive()
        elif self.file_path.endswith('.rar'):
            return RarArchive()
        elif self.file_path.endswith('.7z'):
            return SevenZipArchive()
        else:
            raise ValueError("Неподдерживаемый формат архива")

    def __call__(self) -> None:
        # Извлечение имени файла и директории для распаковки
        file_name = os.path.basename(self.file_path)
        dir_name = os.path.splitext(file_name)[0]
        parent_dir = os.path.dirname(self.file_path)
        extract_path = os.path.join(parent_dir, dir_name)
        
        # Распаковка архива
        self.archive.extract(self.file_path, extract_path)
        
        # Определение базового пути для обхода файлов
        extracted_items = os.listdir(extract_path)
        # Проверка, содержит ли распакованный архив только одну директорию
        if len(extracted_items) == 1 and os.path.isdir(os.path.join(extract_path, extracted_items[0])):
            # Если да, устанавливаем базовый путь на эту директорию
            base_path = os.path.join(extract_path, extracted_items[0])
        else:
            # Иначе, базовый путь - это путь распаковки
            base_path = extract_path

        # Обход файлов и директорий
        self.walk_files_and_dirs(extract_path, base_path)
       
        # Сохранение Markdown-заметки
        markdown_file_path = os.path.join(parent_dir, f"{dir_name}_note.md")
        self.save_markdown_file(markdown_file_path)
        
        # Удаление временной директории с распакованными файлами
        shutil.rmtree(extract_path)
       
        # Удаление исходного архива
        os.remove(self.file_path)

# Пример использования
if __name__ == "__main__":
    # Запрос пути к архиву у пользователя и удаление лишних кавычек
    file_path = input("Введите путь к архиву: ").strip('"').strip("'")
    # Создание экземпляра класса ArchiveExtractor с указанным путем к архиву
    extractor = ArchiveExtractor(file_path)
    # Вызов метода извлечения и обработки архива
    extractor()
    # Ожидание нажатия Enter перед завершением программы
    input("Нажмите Enter для выхода...")