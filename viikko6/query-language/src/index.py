from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder
from matchers import All, Not, And, Or, HasAtLeast, HasFewerThan, PlaysIn

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

    #matcher = All()


    query = QueryBuilder()
    #matcher = query.build()
    #matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals").build()

    matcher = (
      query
        .playsIn("NYR")
        .hasAtLeast(5, "goals")
        .hasFewerThan(10, "goals")
        .build()
    )


    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
