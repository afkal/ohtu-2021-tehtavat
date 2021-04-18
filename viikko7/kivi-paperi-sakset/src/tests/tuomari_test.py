import unittest
from tuomari import Tuomari

class TestTuomari(unittest.TestCase):

    def setUp(self):
        self.tuomari = Tuomari()

    def test_pelaaja1_kivi_voittaa_sakset(self):
        self.tuomari.kirjaa_siirto("k", "s")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)
        self.assertEqual(self.tuomari.tasapelit, 0)

    def test_pelaaja1_sakset_voittaa_paperin(self):
        self.tuomari.kirjaa_siirto("s", "p")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)
        self.assertEqual(self.tuomari.tasapelit, 0)

    def test_pelaaja1_paperi_voittaa_kiven(self):
        self.tuomari.kirjaa_siirto("p", "k")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)
        self.assertEqual(self.tuomari.tasapelit, 0)

    def test_pelaaja2_sakset_voittaa_paperin(self):
        self.tuomari.kirjaa_siirto("p", "s")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 1)
        self.assertEqual(self.tuomari.tasapelit, 0)

    def test_paperi_paperi_tuottaa_tasapelin(self):
        self.tuomari.kirjaa_siirto("p", "p")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)
        self.assertEqual(self.tuomari.tasapelit, 1)
