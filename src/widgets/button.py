import pygame
from pygame import Rect

from src.screen import Screen
from src.widget import Widget


class Button(Widget):
    def __init__(self, rect: Rect, parent=None):
        super().__init__(rect, parent)

    def draw(self, screen: Screen):
        pygame.draw.rect(screen.surface(), (0, 0, 0), self.rect, 1)
