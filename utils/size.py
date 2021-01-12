class Size:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_height(self, height):
        self._height = height

    def set_width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def __eq__(self, other):
        return self.width() == other.width()\
               and self.height() == other.height()

    def __ne__(self, other):
        return not self.__eq__(other)