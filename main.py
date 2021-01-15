import pygame
from pygame import Rect

from src.event_loop import EventLoop
from src.screen import Screen
from src.widgets.button import Button

loop = EventLoop()
screen = Screen((500, 500))

button = Button(Rect(0, 0, 50, 50), screen)
clock = pygame.time.Clock()

while True:
    screen.update(screen.surface)

    event = loop.get()
    if event.type == pygame.QUIT:
        break

    pygame.display.flip()
    clock.tick(60)
