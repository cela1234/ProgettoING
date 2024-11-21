
from typing import List

class Magazzino:
    def __init__(self, lista_bevande: List['Bevanda'], lista_ingredienti: List['Ingrediente']):
        self.lista_bevande = lista_bevande
        self.lista_ingredienti = lista_ingredienti
