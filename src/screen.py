import pygame

from src.object import Object


class Screen(Object):
    def __init__(self, size, caption=None):
        super().__init__(None)

        if not pygame.get_init():
            pygame.init()

        self.__screen = pygame.display.set_mode(size)
        if caption:
            pygame.display.set_caption(caption)

    @property
    def surface(self):
        return self.__screen
