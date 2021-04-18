class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return "k"
        if self._siirto == 1:
            return "p"
        return "s"

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
