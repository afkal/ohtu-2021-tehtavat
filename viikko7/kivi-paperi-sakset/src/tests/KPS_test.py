import unittest
from KPS import KPS


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestKPS(unittest.TestCase):

    def setUp(self):
        self.kps = KPS(StubIO(["k", "s", "p", "k", "q", "x"]))

    def test_pelaa(self):
        self.kps.pelaa()
