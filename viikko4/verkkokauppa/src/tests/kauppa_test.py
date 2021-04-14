import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    # toteutus varasto saldo-metodille
    # tuote id 1, 10kpl
    # tuote id 2,  5kpl
    # tuote id 3,  0kpl
    def varasto_saldo(self, tuote_id):
        if tuote_id == 1:
            return 10
        if tuote_id == 2:
            return 5
        if tuote_id == 3:
            return 0

    # toteutus hae_tuote-metodille
    # tuote id: 1, nimi: maito, hinta: 5
    # tuote id: 2, nimi: leipä, hinta: 3
    # tuote id: 3, nimi: juusto, hinta: 2
    def varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        if tuote_id == 2:
            return Tuote(2, "leipä", 3)
        if tuote_id == 3:
            return Tuote(3, "juusto", 2)

    def setUp(self):

        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote


        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_yksi_ostos_tilisiirtoa_kutsutaan_oikeilla_tiedoilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kaksi_eri_ostosta_tilisiirtoa_kutsutaan_oikeilla_tiedoilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_kaksi_samaa_ostosta_tilisiirtoa_kutsutaan_oikeilla_tiedoilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_kaksi_eri_ostosta_toinen_loppu_tilisiirtoa_kutsutaan_oikeilla_tiedoilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_hinnan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla hinnalla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)

        # nollataan ostoskori
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu nolla hinnalla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 0)


    def test_aloita_asiointi_nollaa_hinnan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla hinnalla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)


    def test_uusi_viitenumero(self):
        # määritellään että metodi palauttaa ensimmäisellä kutsulla 1, toisella 2 ja kolmannella 3
        self.viitegeneraattori_mock.uusi.side_effect = [12, 25, 37]

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla viitenumerolla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 12, ANY, ANY, ANY)

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla viitenumerolla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 25, ANY, ANY, ANY)

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla viitenumerolla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 37, ANY, ANY, ANY)

    def test_poista_korista_palauttaa_varastoon(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        # varmistetaan, että metodia palauta varastoon on kutsuttu oikealla tuotteella
        self.varasto_mock.palauta_varastoon.assert_called_with(Tuote(1, "maito", 5))
