from pygame.event import Event
from abc import abstractmethod, ABC


class Object(ABC):
    def __init__(self, parent=None):
        self._parent = parent
        self._children = []

        self._event_types: list[int, list] = []
        self._connections = dict()

        if self._parent:
            self._parent.add_child(self)

    def add_child(self, child):
        self._children.append(child)

    def connect(self, event_type, callback):
        self._connections[event_type] =\
            self._connections.get(event_type, []) + [callback]

    def _handle_event(self, event: Event):
        for callback in self._connections[event.type]:
            callback(event)

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @property
    def event_types(self):
        return self._event_types
