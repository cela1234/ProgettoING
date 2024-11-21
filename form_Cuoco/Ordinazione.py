from PyQt5.QtCore import QObject


class Ordinazione(QObject):
    def __init__(self, ID, ID_tavolo, completato, sequenzaCorrente, parent=None):
        super().__init__(parent)
        self._ID = ID
        self._ID_tavolo = ID_tavolo
        self.completato = completato  # tinyint, quindi 0 o 1
        self.sequenzaCorrente = sequenzaCorrente  # int

    @property
    def ID(self):
        return self._ID


    @property
    def ID_tavolo(self):
        return self._ID_tavolo

    @ID_tavolo.setter
    def ID_tavolo(self, value):
        self._ID_tavolo = value