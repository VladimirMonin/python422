"""
Модуль для сжатия изображений и конвертации их в формат HEIF.

Этот модуль предоставляет класс ImageCompressor для сжатия изображений
с возможностью настройки качества сжатия. Поддерживает форматы JPG, JPEG и PNG.
Хранятся в аттрибуты класса.

Классы:
    ImageCompressor: Класс для сжатия изображений.

Константы:
    QUALITY: Значение качества сжатия по умолчанию (50).

Зависимости:
    - os: Для работы с файловой системой.
    - typing: Для аннотаций типов.
    - PIL: Для обработки изображений.
    - pillow_heif: Для поддержки формата HEIF.

Пример использования:
    compressor = ImageCompressor(quality=75)
    compressor.compress_image('input.jpg', 'output.heif')

Смело можно использовать качество 50.
"""

import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener

QUALITY: int = 50  # Можно настроить качество сжатия


class ImageCompressor:
    """
    Класс для сжатия изображений.
    """
    supported_formats: tuple = ('.jpg', '.jpeg', '.png')
    def __init__(self, quality: int):
        """
        Инициализирует объект ImageCompressor с указанным качеством сжатия.
        :param quality: Качество сжатия (от 1 до 100).
        """
        self.__quality = quality

    
    @property
    def quality(self) -> int:
        """
        Возвращает текущее качество сжатия.
        :return: Качество сжатия.
        """
        return self.__quality
    
    @quality.setter
    def quality(self, quality: int) -> None:
        """
        Устанавливает новое качество сжатия.
        Проверяет на число, на диапазон.
        :param quality: Новое качество сжатия (от 1 до 100).
        """
        if not isinstance(quality, int):
            raise TypeError("Качество сжатия должно быть целым числом")
        
        if not 1 <= quality <= 100:
            raise ValueError("Качество сжатия должно быть в диапазоне от 1 до 100")
        
        self.__quality = quality

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.
        :param input_path: Путь к исходному изображению.
        :param output_path: Путь для сохранения сжатого изображения.
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.__quality)
        print(f"Сжато: {input_path} -> {output_path}")


    def process_directory(self, directory: str) -> None:
        """
        Обрабатывает все изображения в указанной директории и её поддиректориях.
        :param directory: Путь к директории для обработки.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                # Проверяем расширение файла
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)

    def run(self, input_path: str) -> None:
        """
        Основной метод класса. Обрабатывает входной путь и запускает сжатие изображений.
        :param input_path: Путь к файлу или директории для обработки.
        """
        register_heif_opener()
        input_path = input_path.strip('"')  # Удаляем кавычки, если они есть

        if os.path.exists(input_path):
            if os.path.isfile(input_path):
                # Если указан путь к файлу, обрабатываем только этот файл
                print(f"Обрабатываем файл: {input_path}")
                output_path = os.path.splitext(input_path)[0] + '.heic'
                self.compress_image(input_path, output_path)
            elif os.path.isdir(input_path):
                # Если указан путь к директории, обрабатываем все файлы в ней
                print(f"Обрабатываем директорию: {input_path}")
                self.process_directory(input_path)
                # Функция process_directory рекурсивно обойдет все поддиректории
                # и обработает все поддерживаемые изображения
            else:
                print("Указанный путь не существует")


# Тестирование
if __name__ == "__main__":
    # Пример использования
    compressor = ImageCompressor(quality=40)
    compressor.quality = 50
    # compressor.quality = "чебурек"
    user_input = input("Введите путь к файлу или директории для обработки: ")
    compressor.run(user_input)