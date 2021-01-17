import pygame
from pygame.event import Event

from src.object import Object


class EventLoop:
    _instance = None
    _events = dict()

    def __new__(cls, *args, **kwargs):
        if not EventLoop._instance:
            EventLoop._instance = super(
                EventLoop, cls
            ).__new__(cls, *args, **kwargs)
        return EventLoop._instance

    def __init__(self):
        if not pygame.get_init():
            pygame.init()

    def handle(self):
        event = pygame.event.poll()
        if pygame.NOEVENT == event.type:
            return
        self.notify(event)

    def post(self, event: Event) -> None:
        pygame.event.post(event)

    def add_subscriber(self, widget: Object, event: int):
        EventLoop._events[event] = EventLoop._events.get(event, []) + [widget]

    def add_subscribers(self, widget: Object, events):
        [self.add_subscriber(widget, event) for event in events]

    def notify(self, event: Event):
        subscribers = EventLoop._events.get(event.type, [])
        for subscriber in subscribers:
            subscriber._handle_event(event)
