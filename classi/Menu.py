
from typing import List
from Bevanda import Bevanda
from Piatto import Piatto

class Menu:
    def __init__(self, lista_bevande: List[Bevanda], lista_piatti: List[Piatto]):
        self.lista_bevande = lista_bevande
        self.lista_piatti = lista_piatti
