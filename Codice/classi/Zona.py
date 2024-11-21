from enum import Enum
from typing import List

class TipoZona(Enum):
    pizzeria = 1
    principale = 2
    prive = 3
    open_space = 4
    saletta = 5

class Zona:
    def __init__(self, lista_tavoli_zona: List['Tavolo'], tipo_zona: TipoZona):
        # Import differito per evitare ciclo
        from .Tavolo import Tavolo
        self.lista_tavoli_zona = lista_tavoli_zona
        self.tipo_zona = tipo_zona
