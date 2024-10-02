from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy.editor import VideoFileClip, AudioFileClip
import os

class YouTubeDownloader:
    """
    Класс для скачивания и обработки видео с YouTube.
    """

    def __init__(self, url: str, output_folder: str = "./download"):
        """
        Инициализирует объект YouTubeDownloader.

        :param url: URL видео на YouTube
        :param output_folder: Папка для сохранения видео (по умолчанию "./download")
        """
        self.url = url
        self.output_folder = output_folder
        self.yt = YouTube(url, on_progress_callback=on_progress)
        self.title = self.yt.title
        self.safe_title = self.title.replace(' ', '_')
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def get_best_streams(self):
        """
        Получает лучшие доступные видео и аудио потоки.

        :return: Кортеж с лучшими видео и аудио потоками
        """
        video_stream = self.yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
        audio_stream = self.yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        return video_stream, audio_stream

    def download(self):
        """
        Скачивает видео и аудио, объединяет их и сохраняет результат.

        :return: Путь к итоговому видеофайлу
        """
        video_stream, audio_stream = self.get_best_streams()
        
        video_filename = os.path.join(self.output_folder, f'video_{self.safe_title}.mp4')
        audio_filename = os.path.join(self.output_folder, f'audio_{self.safe_title}.mp4')
        
        print("Загрузка видео...")
        video_stream.download(filename=video_filename)
        audio_stream.download(filename=audio_filename)
        
        if not os.path.exists(video_filename) or not os.path.exists(audio_filename):
            raise FileNotFoundError("Видео или аудио файл не найден после загрузки")
        
        try:
            video = VideoFileClip(video_filename)
            audio = AudioFileClip(audio_filename)
            final_clip = video.set_audio(audio)
            output_filename = os.path.join(self.output_folder, f"{self.safe_title}.mp4")
            final_clip.write_videofile(output_filename)
        finally:
            if 'video' in locals(): video.close()
            if 'audio' in locals(): audio.close()
            if 'final_clip' in locals(): final_clip.close()
        
        print("Загрузка и объединение завершены.")
        return output_filename

# Пример использования:
downloader = YouTubeDownloader("https://youtu.be/oBU83uojltE?si=GrOHSF8uBtsc5B4I")
downloader.download()