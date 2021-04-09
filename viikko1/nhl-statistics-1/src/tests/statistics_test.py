import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):

    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_returns_rigth_player(self):
        pelaaja = self.statistics.search("Semenko")
        self.assertEqual(pelaaja.name, "Semenko")

    def test_search_with_unexisting_player(self):
        pelaaja = self.statistics.search("Koivu")
        #self.assertEqual(pelaaja.name, "Semenko")
        self.assertIsNone(pelaaja)

    def test_team_has_correct_players(self):
        pelaajat = self.statistics.team("EDM")
        self.assertEqual(pelaajat[0].name, "Semenko")
        self.assertEqual(pelaajat[1].name, "Kurri")
        self.assertEqual(pelaajat[2].name, "Gretzky")

    def test_gretzky_as_top_scorer(self):
        pelaaja = self.statistics.top_scorers(1)
        self.assertEqual(pelaaja[0].name, "Gretzky")
