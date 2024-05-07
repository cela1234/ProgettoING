from PyQt5.QtCore import QObject


class NomeElemento(QObject):
    def __init__(self, ID, nome, intolleranze, piccante, vegano, parent=None):
        super().__init__(parent)
        self._ID = ID
        self._nome = nome
        self._intolleranze = intolleranze
        self._piccante = piccante
        self._vegano = vegano

    @property
    def ID(self):
        return self._ID

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def intolleranze(self):
        return self._intolleranze

    @intolleranze.setter
    def intolleranze(self, value):
        self._intolleranze = value

    @property
    def piccante(self):
        return self._piccante

    @piccante.setter
    def piccante(self, value):
        self._piccante = value

    @property
    def vegano(self):
        return self._vegano

    @vegano.setter
    def vegano(self, value):
        self._vegano = value