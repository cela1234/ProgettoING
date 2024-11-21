
class Ingrediente:
    def __init__(self, nome: str, prezzo: float, piccante: bool, vegano: bool, intolleranze: str = ""):
        self.nome = nome
        self.prezzo = prezzo
        self.piccante = piccante
        self.vegano = vegano
        self.intolleranze = intolleranze
