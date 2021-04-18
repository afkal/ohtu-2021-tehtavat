from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

# Factory
class Peli:
    # def __init__(self):

    def luo_kaksinpeli(self):
        return KPSPelaajaVsPelaaja()

    def luo_yksinpeli(self):
        return KPSTekoaly()

    def luo_haastava_yksinpeli(self):
        return KPSParempiTekoaly()
