import requests, urllib3
from pprint import pprint
from responseCatcher import responseCatcher
from inventory import Cargo
from navigation import Navigation
from engine import Engine
from reactor import Reactor

urllib3.disable_warnings()


class Ship:

    def __init__(self, shipId, token) -> None:
        url = f"https://api.spacetraders.io/v2/my/ships/{shipId}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers, verify=False)

        self.shipData = response.json()["data"]
        self.shipSymbol = shipId
        self.token = token

        self.nav = Navigation(token, self.shipSymbol, self.shipData["nav"])
        self.cargo = Cargo(token, self.shipSymbol, self.shipData["cargo"])
        self.engine = Engine(token, self.shipSymbol, self.shipData["engine"])
        self.reactor = Reactor(token, self.shipSymbol, self.shipData["reactor"])

    def update(self, manual=None):
        """
        standard update function for updating data and also calling for dependencyUpdates.
        makes sure to manually update to save calls to api.
        """

        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        self.shipData = manual if manual else self.shipData = requests.get(url, headers=headers, verify=False).json()[
            "data"]

        self.nav.update(self.shipData["nav"])
        self.cargo.update(self.shipData["cargo"])
        self.engine.update(self.shipData["engine"])
        self.reactor.update(self.shipData["reactor"])
