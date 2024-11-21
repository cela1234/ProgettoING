from Prenotazione import Prenotazione
from TipoPagamento import TipoPagamento
class Fattura:
    def __init__(self, importo: float, prenotazione: Prenotazione, tipo_pagamento: TipoPagamento):
        self.importo = importo
        self.prenotazione = prenotazione
        self.tipo_pagamento = tipo_pagamento
