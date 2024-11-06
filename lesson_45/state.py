from abc import ABC, abstractmethod

class PlayerState(ABC):
    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass


class PlayingState(PlayerState):
    def play(self, player):
        print("Уже играет")
    
    def pause(self, player):
        print("Ставим на паузу")
        player.set_state(PausedState())
    
    def stop(self, player):
        print("Останавливаем воспроизведение")
        player.set_state(StoppedState())


class PausedState(PlayerState):
    def play(self, player):
        print("Возобновляем воспроизведение")
        player.set_state(PlayingState())
    
    def pause(self, player):
        print("Уже на паузе")
    
    def stop(self, player):
        print("Останавливаем воспроизведение")
        player.set_state(StoppedState())


class StoppedState(PlayerState):
    def play(self, player):
        print("Начинаем воспроизведение")
        player.set_state(PlayingState())
    
    def pause(self, player):
        print("Невозможно поставить на паузу остановленный плеер")
    
    def stop(self, player):
        print("Уже остановлено")


class MusicPlayer:
    def __init__(self):
        self._state = StoppedState()
        self.current_track = None
    
    def set_state(self, state: PlayerState):
        self._state = state
    
    def get_state(self):
        return self._state
    
    def play(self):
        self._state.play(self)
    
    def pause(self):
        self._state.pause(self)
    
    def stop(self):
        self._state.stop(self)


def test_player():
    player = MusicPlayer()
    
    # Тестируем из состояния STOP
    print("Состояние STOP:")
    player.play()  # -> PLAYING
    player.stop()  # -> STOP
    player.pause() # Ошибка
    
    print("\nСостояние PLAYING:")
    player.play()  # -> PLAYING
    player.play()  # Уже играет
    player.pause() # -> PAUSE
    
    print("\nСостояние PAUSE:")
    player.pause() # Уже на паузе
    player.play()  # -> PLAYING
    player.stop()  # -> STOP

if __name__ == "__main__":
    test_player()
