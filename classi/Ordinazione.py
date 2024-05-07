from PyQt5.QtCore import QObject


class Ordinazione(QObject):
    def __init__(self, ID, ID_tavolo, parent=None):
        super().__init__(parent)
        self._ID = ID
        self._ID_tavolo = ID_tavolo

    @property
    def ID(self):
        return self._ID


    @property
    def ID_tavolo(self):
        return self._ID_tavolo

    @ID_tavolo.setter
    def ID_tavolo(self, value):
        self._ID_tavolo = value