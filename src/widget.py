from abc import abstractmethod

from pygame import Surface
from pygame.event import Event
from pygame.rect import Rect

from src.object import Object


class Widget(Object):
    def __init__(self, rect: Rect, parent=None):
        super().__init__(parent)

        if self._parent:
            if not parent.rect.contains(rect):
                raise RuntimeError()

        self._rect = rect

    def _handle_event(self, event: Event):
        if hasattr(event, "pos"):
            if self._rect.collidepoint(*event.pos):
                super()._handle_event(event)
                return event
        return None

    def update(self, surface: Surface):
        self.draw(surface)
        self.__draw_children(surface)

    def __draw_children(self, surface: Surface):
        for children in self.children:
            children.update(surface)

    @abstractmethod
    def draw(self, surface: Surface):
        pass

    @property
    def rect(self):
        return self._rect
