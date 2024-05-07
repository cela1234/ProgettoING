from PyQt5.QtCore import QObject


class Tavolo(QObject):
    def __init__(self, ID, numero, sala, stato, parent=None):
        super().__init__(parent)
        self._ID = ID
        self._numero = numero
        self._sala = sala
        self._stato = stato

    @property
    def ID(self):
        return self._ID


    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def sala(self):
        return self._sala

    @sala.setter
    def sala(self, value):
        self._sala = value

    @property
    def stato(self):
        return self._stato

    @stato.setter
    def stato(self, value):
        self._stato = value