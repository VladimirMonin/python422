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
from abc import ABC, abstractmethod
import os
import shutil
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
    def walk_files_and_dirs(self, path: str) -> None:
        # Рекурсивный обход директорий и файлов
        for root, dirs, files in os.walk(path):
            # Обработка каждой поддиректории
            for dir in dirs:
                self.process_directory(os.path.join(root, dir))
            # Обработка каждого файла
            for file in files:
                # Формирование полного пути к файлу
                file_path = os.path.join(root, file)
                # Вычисление относительного пути файла
                relative_path = os.path.relpath(file_path, path)
                # Обработка файла с учетом его полного и относительного пути
                self.process_file(file_path, relative_path)


class MarkdownGeneratorMixin:
    """Миксин для генерации Markdown-заметки."""
    def __init__(self):
        self.markdown_content = ""
        self.supported_extensions = ['py', 'sql', 'js', 'css', 'html']

    def process_directory(self, dir_path: str) -> None:
        """Обработка директории."""
        # Удаляем обработку директорий, если она не нужна
        pass

    def process_file(self, file_path: str, relative_path: str) -> None:
        """Обработка файла."""
        file_extension = os.path.splitext(file_path)[1][1:]
        if file_extension in self.supported_extensions:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
            file_name = os.path.basename(file_path)
            # Формируем заголовок согласно вашему требованию
            self.markdown_content += (
                f"## {relative_path} \\ {file_name}\n"
                f"```{file_extension}\n"
                f"{file_content}\n"
                "```\n\n"
            )

    def save_markdown_file(self, file_path: str) -> None:
        """Сохранение сформированной Markdown-заметки в файл."""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.markdown_content)


class ArchiveExtractor(FileSystemWalkerMixin, MarkdownGeneratorMixin):
    """Главный класс для распаковки архивов и генерации Markdown-заметки."""
    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path
        self.archive = self._create_archive_extractor()

    def _create_archive_extractor(self) -> AbstractArchive:
        """Создание объекта-распаковщика на основе типа архива."""
        if self.file_path.endswith('.zip'):
            return ZipArchive()
        elif self.file_path.endswith('.rar'):
            return RarArchive()
        elif self.file_path.endswith('.7z'):
            return SevenZipArchive()
        else:
            raise ValueError("Неподдерживаемый формат архива")

    def __call__(self) -> None:
        """Распаковка архива и генерация Markdown-заметки."""
        file_name = os.path.basename(self.file_path)
        dir_name = os.path.splitext(file_name)[0]
        extract_path = os.path.join(os.path.dirname(self.file_path), dir_name)
        self.archive.extract(self.file_path, extract_path)
        self.walk_files_and_dirs(extract_path)
        # Сохраняем заметку РЯДОМ с разархивированной папкой
        markdown_file_path = os.path.join(os.path.dirname(self.file_path), f"{dir_name}_note.md")
        self.save_markdown_file(markdown_file_path)
        # Удаляем папку с распакованными файлами
        shutil.rmtree(extract_path)
        # Удаляем исходный архив
        os.remove(self.file_path)

# Пример использования

if __name__ == "__main__":
    file_path = input("Введите путь к архиву: ").strip('"').strip("'")
    extractor = ArchiveExtractor(file_path)
    extractor()
    input("Нажмите Enter для выхода...")