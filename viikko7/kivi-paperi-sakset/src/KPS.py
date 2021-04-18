from tuomari import Tuomari
from konsoli_io import KonsoliIO

class KPS:

    def __init__(self, io = KonsoliIO()):
        self._io = io
        self._tuomari = Tuomari()

    def pelaa(self):

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            # ...
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._io.kirjoita(self._tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            self._io.kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        self._io.kirjoita("Kiitos!")
        self._io.kirjoita(self._tuomari)

    def _ensimmaisen_siirto(self):
        return self._io.lue("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return self._io.lue("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
