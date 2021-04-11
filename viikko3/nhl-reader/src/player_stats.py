
class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self._reader.get_players()
        filtered_players = []

        # Filter players by nationality
        for player in all_players:
            if player.nationality == nationality:
                filtered_players.append(player)

        # Sort by points descending
        filtered_players.sort(key=lambda x: x.get_points(), reverse=True)

        return filtered_players
