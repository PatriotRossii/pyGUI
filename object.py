from abc import ABC, abstractmethod
from enum import Enum

from event import Event


class FindChildOption(Enum):
    FindDirectOnly = 1,
    FindRecursively = 2,


class Object(ABC):
    def __init__(self, parent=None):
        self._parent = parent
        self._object_name: str = None
        self._children = []

        self._signals = dict()
        self._event_filter = None

        if self.parent:
            self.parent.__add_child(self)

    def connect(self, signal, receiver, method):
        self._signals[signal] = (receiver, method)

    def disconnect(self, signal, receiver, method):
        if signal in self._signals:
            del self._signals[signal][self._signals(signal).find((receiver, method))]

    def find_child(self, name: str, option: FindChildOption):
        for obj in self._children:
            if obj.object_name() == name:
                return object
            if option == FindChildOption.FindRecursively:
                return obj.find_child(name, option)

    @abstractmethod
    def event_filter(self, obj, ev) -> bool:
        pass

    def install_event_filter(self, event_filter):
        self._event_filter = event_filter

    def set_parent(self, parent):
        self._parent = parent

    def set_object_name(self, object_name: str):
        self.object_name = object_name

    def __handle_event(self, event: Event):
        if self._event_filter:
            process = self._event_filter.event_filter(self, event)
            if not process:
                return
        self.event(event)

    def __add_child(self, child):
        self._children.append(child)

    def __set_signals(self, signals):
        self.signals = signals

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    @property
    def object_name(self):
        return self._object_name

    @abstractmethod
    def event(self, event: Event) -> bool:
        pass
