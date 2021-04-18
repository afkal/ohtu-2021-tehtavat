from peli import Peli

def tulosta_valikko():
    print("Valitse pelataanko"
        "\n (a) Ihmistä vastaan"
        "\n (b) Tekoälyä vastaan"
        "\n (c) Parannettua tekoälyä vastaan"
        "\nMuilla valinnoilla lopetetaan"
    )

def kasittele_valinta(valinta):
    kps = Peli() # Luodaan instanssi peli luokasta

    if valinta not in ['a', 'b', 'c']:
        return False

    print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

    pelimoodi = {
        "a" : kps.luo_kaksinpeli(),
        "b" : kps.luo_yksinpeli(),
        "c" : kps.luo_haastava_yksinpeli()
    }

    return pelimoodi[valinta]

def main():

    while True:
        tulosta_valikko()
        vastaus = input()
        valinta = kasittele_valinta(vastaus)
        if valinta == False:
            break
        valinta.pelaa()

if __name__ == "__main__":
    main()
