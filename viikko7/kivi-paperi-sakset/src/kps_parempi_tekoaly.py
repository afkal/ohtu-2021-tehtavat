from KPS import KPS
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPS):

    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
        super().__init__()

    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        #print("--Debug: KPSTekoaly._toisen_siirto: ensimmaisen_siirto=" + ensimmaisen_siirto)
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return self.tekoaly.anna_siirto()
