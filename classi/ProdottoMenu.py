from PyQt5.QtCore import QObject


class ProdottoMenu(QObject):
    def __init__(self, categoria, descrizione, ID, nome, prezzo, parent=None):
        super().__init__(parent)
        self._categoria = categoria
        self._descrizione = descrizione
        self._ID = ID
        self._nome = nome
        self._prezzo = prezzo

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def descrizione(self):
        return self._descrizione

    @descrizione.setter
    def descrizione(self, value):
        self._descrizione = value

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, value):
        self._prezzo = value