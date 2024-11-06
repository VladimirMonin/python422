from abc import ABC, abstractmethod

class PlayerState(ABC):
    @abstractmethod
    def play(self, player: "MusicPlayer": "MusicPlayer"):
        pass

    @abstractmethod
    def pause(self, player: "MusicPlayer": "MusicPlayer"):
        pass

    @abstractmethod
    def stop(self, player: "MusicPlayer": "MusicPlayer"):
        pass


class PlayingState(PlayerState):
    def play(self, player: "MusicPlayer"):
        print("Уже играет")
    
    # Переход в состояние паузы
    def pause(self, player: "MusicPlayer"):
        print("Ставим на паузу")
        player.set_state(PausedState())
    
    # Переход в состояние остановки
    def stop(self, player: "MusicPlayer"):
        print("Останавливаем воспроизведение")
        player.set_state(StoppedState())


class PausedState(PlayerState):
    # Возобновление проигрывания из состояния паузы
    def play(self, player: "MusicPlayer"):
        print("Возобновляем воспроизведение")
        player.set_state(PlayingState())
    
    def pause(self, player: "MusicPlayer"):
        print("Уже на паузе")
    
    # Переход в состояние остановки из паузы
    def stop(self, player: "MusicPlayer"):
        print("Останавливаем воспроизведение")
        player.set_state(StoppedState())


class StoppedState(PlayerState):
    # Начало воспроизведения из остановленного состояния
    def play(self, player: "MusicPlayer"):
        print("Начинаем воспроизведение")
        player.set_state(PlayingState())
    
    def pause(self, player: "MusicPlayer"):
        print("Невозможно поставить на паузу остановленный плеер")
    
    def stop(self, player: "MusicPlayer"):
        print("Уже остановлено")


class MusicPlayer:
    # Инициализация плеера в состоянии остановки
    def __init__(self):
        self._state = StoppedState()
        self.current_track = None
    
    # Метод для изменения текущего состояния плеера
    def set_state(self, state: PlayerState):
        self._state = state
    
    def get_state(self):
        return self._state
    
    # Делегирование выполнения команды текущему состоянию
    def play(self):
        self._state.play(self)
    
    def pause(self):
        self._state.pause(self)
    
    def stop(self):
        self._state.stop(self)


def test_player():
    # Создаем экземпляр плеера в начальном состоянии STOP
    player = MusicPlayer()
    
    # Тестируем из состояния STOP
    print("Состояние STOP:")
    # Запускаем воспроизведение из состояния STOP
    player.play()  # -> PLAYING
    # Останавливаем воспроизведение, возвращаемся в STOP
    player.stop()  # -> STOP
    # Проверяем невозможность постановки на паузу в состоянии STOP
    player.pause() # Ошибка
    
    print("\nСостояние PLAYING:")
    # Переходим в состояние воспроизведения
    player.play()  # -> PLAYING
    # Проверяем повторный вызов play в состоянии воспроизведения
    player.play()  # Уже играет
    # Ставим на паузу из состояния воспроизведения
    player.pause() # -> PAUSE
    
    print("\nСостояние PAUSE:")
    # Проверяем повторную постановку на паузу
    player.pause() # Уже на паузе
    # Возобновляем воспроизведение из состояния паузы
    player.play()  # -> PLAYING
    # Останавливаем воспроизведение полностью
    player.stop()  # -> STOP

if __name__ == "__main__":

    test_player()