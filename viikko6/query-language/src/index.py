from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder
#from matchers import All, Not, And, Or, HasAtLeast, HasFewerThan, PlaysIn

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    #matcher = query.build()
    #matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals").build()

    matcher = (
      query
        .oneOf(
          query.playsIn("PHI")
              .hasAtLeast(10, "assists")
              .hasFewerThan(5, "goals")
              .build(),
          query.playsIn("EDM")
              .hasAtLeast(40, "points")
              .build()
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
