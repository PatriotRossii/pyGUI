from abc import abstractmethod
from pygame.rect import Rect

from src.object import Object
from src.screen import Screen


class Widget(Object):
    def __init__(self, rect: Rect, parent=None):
        super().__init__(parent)

        if self._parent:
            if not parent.rect().contains(rect):
                raise RuntimeError()

        self._rect = rect

    def update(self, screen: Screen):
        self.draw(screen)
        self.__draw_children(screen)

    def __draw_children(self, screen: Screen):
        for children in self.children():
            children.update(screen)

    @abstractmethod
    def draw(self, screen: Screen):
        pass

    @property
    def rect(self):
        return self._rect
