from PyQt5.QtCore import QObject


class IngredienteProdotto(QObject):
    def __init__(self, ID, ID_nome_elemento, ID_prodotto, quantita, parent=None):
        super().__init__(parent)
        self._ID = ID
        self._ID_nome_elemento = ID_nome_elemento
        self._ID_prodotto = ID_prodotto
        self._quantita = quantita

    @property
    def ID(self):
        return self._ID


    @property
    def ID_nome_elemento(self):
        return self._ID_nome_elemento

    @ID_nome_elemento.setter
    def ID_nome_elemento(self, value):
        self._ID_nome_elemento = value

    @property
    def ID_prodotto(self):
        return self._ID_prodotto

    @ID_prodotto.setter
    def ID_prodotto(self, value):
        self._ID_prodotto = value

    @property
    def quantita(self):
        return self._quantita

    @quantita.setter
    def quantita(self, value):
        self._quantita = value