class Player:
    def __init__(self, name, nationality, assists, goals, team):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
        self.points = self.assists + self.goals


    def get_points(self):
        return self.points

    def __str__(self):
        player_info = f"{self.name:20}" + self.team + " " + f"{str(self.goals):>2}" + " + " + f"{str(self.assists):>2}" + " = " + f"{str(self.points):>2}"
        return player_info
