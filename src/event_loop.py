import pygame
from pygame.event import Event


class EventLoop:
    def __init__(self):
        if not pygame.get_init():
            pygame.init()

    def get(self) -> Event:
        return pygame.event.poll()

    def post(self, event: Event) -> None:
        pygame.event.post(event)
