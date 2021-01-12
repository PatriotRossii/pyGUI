class Object:
    def __init__(self, parent=None):
        self._parent = parent
        self._children = []

        if self._parent:
            self._parent.add_child(self)

    def add_child(self, child):
        self._children.append(child)

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent
