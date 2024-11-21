
from typing import List
from Bevanda import Bevanda
from Piatto import Piatto

class Ordine:
    def __init__(self, lista_bevande_ordinate: List[Bevanda], lista_piatti_ordinati: List[Piatto], sequenza: int):
        self.lista_bevande_ordinate = lista_bevande_ordinate
        self.lista_piatti_ordinati = lista_piatti_ordinati
        self.sequenza = sequenza
