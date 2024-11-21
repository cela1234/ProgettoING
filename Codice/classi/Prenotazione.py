
from typing import List
from datetime import datetime

class Prenotazione:
    def __init__(self, cliente: 'Cliente', data_orario: datetime, lista_ordini: List['Ordine']):
        self.cliente = cliente
        self.data_orario = data_orario
        self.lista_ordini = lista_ordini
