import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    # Return players as json
    def get_players_json(self):
        response = requests.get(self._url).json()
        return response

    # Return players as dict of Player objects
    def get_players(self):
        response = requests.get(self._url).json()
        players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['team']
            )

            players.append(player)

        return players
