from statistics import Statistics
from player_reader import PlayerReader
from matchers import Not, And, Or, HasAtLeast, HasFewerThan, PlaysIn

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    '''
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )
    '''

    matcher = And(
        HasAtLeast(50, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
