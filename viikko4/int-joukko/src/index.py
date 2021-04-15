import unittest
from int_joukko import IntJoukko

def tee_joukko(*luvut):
    joukko = IntJoukko()

    for luku in luvut:
        joukko.lisaa(luku)

    return joukko


def main():
    '''
    joukko = IntJoukko()
    joukko.lisaa(57)
    joukko.lisaa(-32)
    joukko.lisaa(12)
    joukko.lisaa(12)
    joukko.lisaa(4)
    joukko.lisaa(2)
    joukko.poista(4)
    '''

    '''
    # test_toimii_kasvatuksen_jalkeen
    joukko = IntJoukko()
    lisattavat = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for luku in lisattavat:
        joukko.lisaa(luku)

    print(joukko)

    print(joukko.joukko)
    '''

    eka = tee_joukko(1, 2)
    toka = tee_joukko(3, 4)

    tulos = IntJoukko.yhdiste(eka, toka)
    vastauksen_luvut = tulos.to_int_list()

    print(vastauksen_luvut)
    #print(joukko.to_int_list())

if __name__ == "__main__":
    main()
