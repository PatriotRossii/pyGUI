import pygame

from object import Object


class Application(Object):
    def __init__(self, argv):
        self._argv = argv

        self._name = None
        self._exit_code = None

        self.__init_pygame()

    def exec(self) -> int:


    def set_application_name(self, name):
        self._name = name

    @property
    def application_name(self):
        return self._name

    def exit(self, return_code=0):
        self._exit_code = return_code

    @property
    def arguments(self):
        return self._argv
