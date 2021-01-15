import pygame
from pygame import Rect

from src.widget import Widget


class Button(Widget):
    def __init__(self, rect: Rect, parent=None):
        super().__init__(rect, parent)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect, 1)