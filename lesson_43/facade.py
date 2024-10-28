# Паттерн проектирования Facade

"""
Простой пример реализации паттерна Facade на примере умного дома
AbstractSystem - абстракция над системами (включить - выключить и т.д.)
MediaSystem
SecuritySystem
LightingSystem 

SmartHomeFacade
"""
from abc import ABC, abstractmethod

class AbstractSystem(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

class LigthingSystem(AbstractSystem):

    def on(self):
        print("Свет включен")

    def off(self):
        print("Свет выключен")

    def dimmer(self, value):
        print(f"Яркость: {value}")

class SecuritySystem(AbstractSystem):

    def on(self):
        print("Охранная система включена")

    def off(self):
        print("Охранная система отключена")


class MediaSystem(AbstractSystem):

    def on(self):
        print("Медиасистема включена")

    def off(self):
        print("Медиасистема отключена")

    def mute(self):
        print("Медиасистема режим: без звука")


class SmartHomeFacade:
    def __init__(self):
        self.lighting = LigthingSystem()
        self.security = SecuritySystem()
        self.media = MediaSystem()

    def go_out(self):
        """
        Ухожу из дома
        """
        self.media.off()
        self.lighting.off()
        self.security.on()
        print("Ушел")

    def come_home(self):
        """
        Пришел домой
        """
        self.security.off()
        self.lighting.on()
        

    def watch_tv(self):
        """
        Смотрю телевизор
        """
        self.media.on()
        self.lighting.dimmer(0.5)


smart_home = SmartHomeFacade()
smart_home.go_out()
smart_home.come_home()
smart_home.watch_tv()