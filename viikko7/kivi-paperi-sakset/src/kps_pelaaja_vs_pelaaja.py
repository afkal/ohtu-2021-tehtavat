from KPS import KPS

class KPSPelaajaVsPelaaja(KPS):

    def __init__(self):
        super().__init__()

    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto
