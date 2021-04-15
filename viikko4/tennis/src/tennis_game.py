class Player:

    def __init__(self, id, name, points = 0):
        self.id = id
        self.name = name
        self.points = points

    def add_point(self):
        self.points += 1

    def get_points(self):
        return self.points

class TennisGame:
    def __init__(self, player1_name, player2_name):

        # Alustetaan pelaajat
        self.player1 = Player(1, player1_name)
        self.player2 = Player(2, player2_name)

        # Pelaajalista
        self.players = {
            player1_name : self.player1,
            player2_name : self.player2
        }

    def won_point(self, player_name):
        self.players[player_name].add_point()

    def _score_when_less_than_four_points(self, player1_points, player2_points):

            # Pisteitä vastaavat termit
            score_terms_for_points = ["Love", "Fifteen", "Thirty", "Forty"]

            # Tasatilanne esim. "Thirty-All"
            if player1_points == player2_points:
                score = score_terms_for_points[player1_points] + "-All"
                return score

            # Jompi kumpi johtaa esim. "Fifteen-Forty"
            else:
                score = score_terms_for_points[player1_points] + "-" + score_terms_for_points[player2_points]
                return score

    def _score_when_at_least_four_points(self, player1_points, player2_points):
            # Piste-eroa vastaavat termit
            score_terms_for_point_difference = {
                -2 : "Win for player2",
                -1 : "Advantage player2",
                 0 : "Deuce",
                 1 : "Advantage player1",
                 2 : "Win for player1"
            }

            # Lasketaan piste-ero
            point_difference = player1_points - player2_points

            # Jommalla kummalla etu tai tasatilanne
            if abs(point_difference) < 2:
                return score_terms_for_point_difference[point_difference]

            # Pelaajalla 1 riittävä ero voittoon
            if point_difference >= 2:
                return score_terms_for_point_difference[2]

            # Pelaajalla 2 riittävä ero voittoon
            if point_difference <= -2:
                return score_terms_for_point_difference[-2]

    def get_score(self):

        # Käsitellään tapaukset, joissa kummallakin on alle heljä pistettä
        if self.player1.get_points() < 4 and self.player2.get_points() < 4:
            return self._score_when_less_than_four_points(self.player1.get_points(), self.player2.get_points())

        # Käsitellään tapaukset, joissa jommalla kummalla pelaajalla on vähintään 4 pistettä
        else:
            return self._score_when_at_least_four_points(self.player1.get_points(), self.player2.get_points())
