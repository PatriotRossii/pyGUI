from enum import Enum


class EventType(Enum):
    NONE = 0,
    MAX_USER = 255,


class EventState(Enum):
    NONE = 0,
    ACCEPTED = 1,
    IGNORED = 2,


class Event:
    def __init__(self, type_: EventType):
        self.state = EventState.NONE
        self._type = type_

    def is_accepted(self) -> bool:
        return self.state == EventState.ACCEPTED

    def set_accepted(self, state):
        self.state = EventState.ACCEPTED if state else EventState.IGNORED

    def accept(self):
        if self.state == EventState.NONE:
            self.state = EventState.ACCEPTED

    def ignore(self):
        if self.state == EventState.NONE:
            self.state = EventState.IGNORED

    @property
    def type(self) -> EventType:
        return self._type
