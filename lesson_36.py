"""
Lesson 36: Инкапсуляция
- Методы класса, статик методы
- Приватные, защищенные и публичные атрибуты класса
- Приватные, заащищенные и публичные методы класса
- Геттеры и сеттеры
- All Any
- Полиморфизм (концепция)


Практика: pytybefix - библиотека для выгрузки видео с ютуба
"""

from pytubefix import YouTube
from pytubefix.cli import on_progress
from typing import Any, Callable, Tuple
 
url = "https://youtu.be/oBU83uojltE?si=GrOHSF8uBtsc5B4I"
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
 
def get_best_streams(yt: YouTube) -> Tuple[str, str]:
    """
    Получает лучшие видео и аудио потоки.

    :param yt: Объект YouTube
    :return: Кортеж с информацией о лучших видео и аудио потоках
    """
    video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    return video_stream, audio_stream


# Получим лучшие видео и аудио потоки
video_url, audio_url = get_best_streams(yt)

# Загружаем видео
print("Загрузка видео...")
video_url.download()
audio_url.download()
