from PyQt5.QtCore import QObject


class Cameriere(QObject):
    def __init__(self, cognome_nome, ID, parent=None):
        super().__init__(parent)
        self._cognome_nome = cognome_nome
        self._ID = ID

    @property
    def cognome_nome(self):
        return self._cognome_nome

    @cognome_nome.setter
    def cognome_nome(self, value):
        self._cognome_nome = value

    @property
    def ID(self):
        return self._ID