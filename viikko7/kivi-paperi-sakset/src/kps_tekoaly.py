from KPS import KPS
from tekoaly import Tekoaly

class KPSTekoaly(KPS):

    def __init__(self):
        self.tekoaly = Tekoaly()
        super().__init__()

    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        #print("--Debug: KPSTekoaly._toisen_siirto: ensimmaisen_siirto=" + ensimmaisen_siirto)
        return self.tekoaly.anna_siirto()
