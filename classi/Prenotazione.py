from PyQt5.QtCore import QObject


class Prenotazione(QObject):
    def __init__(self, data_ora_prenotazione, ID, ID_tavolo, nome, numero_persone, parent=None):
        super().__init__(parent)
        self._data_ora_prenotazione = data_ora_prenotazione
        self._ID = ID
        self._ID_tavolo = ID_tavolo
        self._nome = nome
        self._numero_persone = numero_persone

    @property
    def data_ora_prenotazione(self):
        return self._data_ora_prenotazione

    @data_ora_prenotazione.setter
    def data_ora_prenotazione(self, value):
        self._data_ora_prenotazione = value

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def ID_tavolo(self):
        return self._ID_tavolo

    @ID_tavolo.setter
    def ID_tavolo(self, value):
        self._ID_tavolo = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def numero_persone(self):
        return self._numero_persone

    @numero_persone.setter
    def numero_persone(self, value):
        self._numero_persone = value