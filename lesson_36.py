from pytubefix import YouTube
from pytubefix.cli import on_progress
from typing import Any, Callable, Tuple
from moviepy.editor import VideoFileClip, AudioFileClip
import os

url = "https://youtu.be/oBU83uojltE?si=GrOHSF8uBtsc5B4I"

yt = YouTube(url, on_progress_callback=on_progress)
title = yt.title
safe_title = title.replace(' ', '_')

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

video_filename = os.path.join(os.getcwd(), f'video_{safe_title}.mp4')
audio_filename = os.path.join(os.getcwd(), f'audio_{safe_title}.mp4')

# Загружаем видео
print("Загрузка видео...")
video_url.download(filename=video_filename)
audio_url.download(filename=audio_filename)

# Проверяем существование файлов
if not os.path.exists(video_filename) or not os.path.exists(audio_filename):
    raise FileNotFoundError("Видео или аудио файл не найден после загрузки")

# Объединяем видео и аудио
try:
    video = VideoFileClip(video_filename)
    audio = AudioFileClip(audio_filename)
    final_clip = video.set_audio(audio)
    final_clip.write_videofile(f"{safe_title}.mp4")
finally:
    # Закрываем файлы
    if 'video' in locals(): video.close()
    if 'audio' in locals(): audio.close()
    if 'final_clip' in locals(): final_clip.close()

print("Загрузка и объединение завершены.")