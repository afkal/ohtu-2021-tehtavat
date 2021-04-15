class IntJoukko:
    def __init__(self, kapasiteetti=0, kasvatuskoko=0):
        self.joukko = []

    def kuuluu(self, luku):
        return luku in self.joukko

    def lisaa(self, luku):
        if luku not in self.joukko:
            self.joukko.append(luku)

    def poista(self, luku):
        if luku in self.joukko:
            self.joukko.remove(luku)

    def mahtavuus(self):
        return len(self.joukko)

    def to_int_list(self):
        return self.joukko

    @staticmethod
    def yhdiste(joukko_1, joukko_2):
        tulosjoukko = IntJoukko()
        tulosjoukko.joukko = joukko_1.to_int_list()+joukko_2.to_int_list()
        return tulosjoukko

    @staticmethod
    def leikkaus(joukko_1, joukko_2):
        tulosjoukko = IntJoukko()

        for luku in joukko_1.to_int_list():
            if luku in joukko_2.to_int_list():
                tulosjoukko.lisaa(luku)
        return tulosjoukko

    @staticmethod
    def erotus(joukko_1, joukko_2):
        tulosjoukko = IntJoukko()

        for luku in joukko_1.to_int_list():
            if luku not in joukko_2.to_int_list():
                tulosjoukko.lisaa(luku)
        return tulosjoukko

    def __str__(self):
        joukko_string = str(self.joukko)
        joukko_string=joukko_string.replace("[", "{")
        joukko_string=joukko_string.replace("]", "}")
        return joukko_string
