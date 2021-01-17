import sys

import pygame
from pygame import Surface
from pygame.event import Event

from src.event_loop import EventLoop
from src.widget import Widget


class Application(Widget):
    def draw(self, surface: Surface):
        pass

    def __init__(self, name, fps):
        self._loop = EventLoop()

        self._name = None
        self._screen = None
        self._fps = None

        self._event_types = [
            pygame.QUIT
        ]
        self._loop.add_subscribers(self, self._event_types)

        self._clock = pygame.time.Clock()
        self.set_fps(fps)

        self.set_name(name)

    def _handle_event(self, event: Event):
        if event.type == pygame.QUIT:
            sys.exit(0)

    def set_screen(self, screen):
        self._screen = screen

    def run(self):
        if not self._screen:
            raise RuntimeError()

        is_running = True
        while is_running:
            self._screen.update(self._screen.surface)

            self._loop.handle()

            pygame.display.flip()
            self._clock.tick(self._fps)

    def set_name(self, name):
        self._name = name
        pygame.display.set_caption(name)

    @property
    def name(self):
        return self._name

    def set_fps(self, fps):
        self._fps = fps

    @property
    def fps(self):
        return self._fps

    def set_icon(self, filepath):
        pygame.display.set_icon(pygame.image.load(filepath))
