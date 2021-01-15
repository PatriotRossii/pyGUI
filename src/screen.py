import pygame
from pygame import Surface

from src.widget import Widget


class Screen(Widget):
    def draw(self, surface: Surface):
        pass

    def __init__(self, size):
        super().__init__(None)

        if not pygame.get_init():
            pygame.init()

        self.__screen = pygame.display.set_mode(size)
        self.__rect = pygame.Rect(0, 0, *size)

    @property
    def surface(self):
        return self.__screen

    @property
    def rect(self):
        return self.__rect
