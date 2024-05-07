from PyQt5.QtCore import QObject


class ElementoMagazzino(QObject):
    def __init__(self, ID, fornitore, id_nome_elemento, prezzo, quantita, scadenza, parent=None):
        super().__init__(parent)
        self._ID = ID
        self._fornitore = fornitore
        self._id_nome_elemento = id_nome_elemento
        self._prezzo = prezzo
        self._quantita = quantita
        self._scadenza = scadenza

    @property
    def ID(self):
        return self._ID


    @property
    def fornitore(self):
        return self._fornitore

    @fornitore.setter
    def fornitore(self, value):
        self._fornitore = value

    @property
    def id_nome_elemento(self):
        return self._id_nome_elemento

    @id_nome_elemento.setter
    def id_nome_elemento(self, value):
        self._id_nome_elemento = value

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, value):
        self._prezzo = value

    @property
    def quantita(self):
        return self._quantita

    @quantita.setter
    def quantita(self, value):
        self._quantita = value

    @property
    def scadenza(self):
        return self._scadenza

    @scadenza.setter
    def scadenza(self, value):
        self._scadenza = value