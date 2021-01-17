import pygame
from pygame import Rect
from pygame.event import Event

from src.event_loop import EventLoop
from src.widget import Widget


class Button(Widget):
    def _handle_event(self, event: Event):
        event = super()._handle_event(event)
        if event is None:
            return
        if event.type == pygame.MOUSEBUTTONUP:
            print("Clicked button")

    def __init__(self, rect: Rect, parent=None):
        super().__init__(rect, parent)

        self._event_types = [
            pygame.MOUSEBUTTONUP
        ]
        EventLoop().add_subscribers(self, self._event_types)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect, 1)