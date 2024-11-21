from PyQt5.QtCore import QObject


class ElementoOrdine(QObject):
    def __init__(self, ID, ID_ordinazione, ID_prodotto,completato, sequenza, parent=None):
        super().__init__(parent)
        self._completato = completato
        self._ID = ID
        self._ID_ordinazione = ID_ordinazione
        self._ID_prodotto = ID_prodotto
        self._sequenza = sequenza

    @property
    def completato(self):
        return self._completato

    @completato.setter
    def completato(self, value):
        self._completato = value

    @property
    def ID(self):
        return self._ID

    @property
    def ID_ordinazione(self):
        return self._ID_ordinazione

    @ID_ordinazione.setter
    def ID_ordinazione(self, value):
        self._ID_ordinazione = value

    @property
    def ID_prodotto(self):
        return self._ID_prodotto

    @ID_prodotto.setter
    def ID_prodotto(self, value):
        self._ID_prodotto = value

    @property
    def sequenza(self):
        return self._sequenza

    @sequenza.setter
    def sequenza(self, value):
        self._sequenza = value