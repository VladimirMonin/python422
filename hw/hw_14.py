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

   
 
### Работа с файлами и путями

```python
# Объединение путей
full_path = os.path.join(OBSIDIAN_DIR, hw_name)

# Получение имени файла из пути
file_name = os.path.basename(file_path)

# Получение имени файла без расширения
name_without_extension = os.path.splitext(file_name)[0]

# Получение пути к директории файла
directory_path = os.path.dirname(file_path)
```

### Обход файлов и папок

```python
# Рекурсивный обход файлов и папок
for root, dirs, files in os.walk(path):
    for file in files:
        # Формирование полного пути к файлу
        file_path = os.path.join(root, file)
        
        # Получение относительного пути к файлу
        relative_path = os.path.relpath(file_path, path)
```

### Формирование Markdown заметки

```python
# Добавление содержимого файла в Markdown-заметку
collected_files_content += (
    f"### Файл: `{relative_path}`\n"
    f"```{file_extension}\n"
    f"{file_content}\n"
    "```\n\n"
)
```

### Распаковка разных типов архивов

```python
# Проверка расширения файла и распаковка в зависимости от типа архива
if file_path.endswith('.zip'):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
elif file_path.endswith('.rar'):
    with rarfile.RarFile(file_path, 'r') as rar_ref:
        rar_ref.extractall(extract_path)
elif file_path.endswith('.7z'):
    with py7zr.SevenZipFile(file_path, 'r') as sz_ref:
        sz_ref.extractall(extract_path)
```

### Создание папки под результат

```python
# Формирование пути для распаковки
extract_path = os.path.join(os.path.dirname(file_path), dir_name)
```

### Удаление архива после распаковки

```python
# Удаление исходного архива после успешной распаковки
os.remove(file_path)
```

### Получение имени текущей папки/файла

```python
# Извлечение имени файла и создание имени директории без расширения
file_name = os.path.basename(file_path)
dir_name = os.path.splitext(file_name)[0]
```

### Создание заголовков разных уровней в Markdown

```python
# Формирование заголовков для Markdown-документа
markdown_content = (
    f"# Заголовок первого уровня\n"
    f"## Заголовок второго уровня\n"
    f"### Заголовок третьего уровня\n"
)
```
  
"""
from  abc import ABC, abstractmethod
import os
# Импорты архиваторов
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
        """Рекурсивный обход файлов и папок."""
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                self.process_directory(os.path.join(root, dir))
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, path)
                self.process_file(file_path, relative_path)

class MarkdownGeneratorMixin:
    """Миксин для генерации Markdown-заметки."""
    def __init__(self):
        self.markdown_content = ""
        self.supported_extensions = ['py', 'sql', 'js', 'css', 'html']

    def process_directory(self, dir_path: str) -> None:
        """Обработка директории."""
        dir_name = os.path.basename(dir_path)
        self.markdown_content += f"## Директория: `{dir_name}`\n\n"

    def process_file(self, file_path: str, relative_path: str) -> None:
        """Обработка файла."""
        file_extension = os.path.splitext(file_path)[1][1:]
        if file_extension in self.supported_extensions:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
            file_name = os.path.basename(file_path)
            self.markdown_content += (
                f"### Файл: `{file_name}`\n"
                f"```{file_extension}\n"
                f"{file_content}\n"
                "```\n\n"
            )

    def get_markdown_content(self) -> str:
        """Получение сформированной Markdown-заметки."""
        return self.markdown_content

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

    def run(self) -> None:
        """Распаковка архива и генерация Markdown-заметки."""
        file_name = os.path.basename(self.file_path)
        dir_name = os.path.splitext(file_name)[0]
        extract_path = os.path.join(os.path.dirname(self.file_path), dir_name)
        self.archive.extract(self.file_path, extract_path)
        self.walk_files_and_dirs(extract_path)
        markdown_content = self.get_markdown_content()
        print(markdown_content)
        os.remove(self.file_path)

# Пример использования

if __name__ == "__main__":
    file_path = input("Введите путь к архиву: ").strip('"').strip("'")
    extractor = ArchiveExtractor(file_path)
    extractor.run()
    input("Нажмите Enter для выхода...")