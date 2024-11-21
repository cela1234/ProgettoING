
from typing import List

from Ingrediente import Ingrediente


class Piatto:
    def __init__(self, nome: str, prezzo: float, lista_ingredienti: List[Ingrediente]):
        self.nome = nome
        self.prezzo = prezzo
        self.lista_ingredienti = lista_ingredienti
