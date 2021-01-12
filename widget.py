from object import Object


class Widget(Object):
    def __init__(self, parent):
        super().__init__(parent)

    def event(self, event):
        return True

    def event_filter(self, obj, ev) -> bool:
        pass
