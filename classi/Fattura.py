from PyQt5.QtCore import QObject


class Fattura(QObject):
    def __init__(self, data_ora_fattura, ID, ID_cameriere, ID_ordinazione, ricavo, parent=None):
        super().__init__(parent)
        self._data_ora_fattura = data_ora_fattura
        self._ID = ID
        self._ID_cameriere = ID_cameriere
        self._ID_ordinazione = ID_ordinazione
        self._ricavo = ricavo

    @property
    def data_ora_fattura(self):
        return self._data_ora_fattura

    @data_ora_fattura.setter
    def data_ora_fattura(self, value):
        self._data_ora_fattura = value

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def ID_cameriere(self):
        return self._ID_cameriere

    @ID_cameriere.setter
    def ID_cameriere(self, value):
        self._ID_cameriere = value

    @property
    def ID_ordinazione(self):
        return self._ID_ordinazione

    @ID_ordinazione.setter
    def ID_ordinazione(self, value):
        self._ID_ordinazione = value

    @property
    def ricavo(self):
        return self._ricavo

    @ricavo.setter
    def ricavo(self, value):
        self._ricavo = value