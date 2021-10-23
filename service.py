import requests
import json


class Service:
    def __init__(self):
        self.header = {
        }

    def obterPokemons(self):
        response = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=1&limit=4000', headers=self.header)

        return response.json()