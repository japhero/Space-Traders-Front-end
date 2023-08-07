import requests
from pprint import pprint


class Fuel:

    def __init__(self, token, shipSymbol, innitData=None):

        self.shipSymbol = shipSymbol
        self.token = token

        self.getHeaders = {
            "Accept": "application/json",
            "Authorization": "Bearer undefined"
        }

        self.postHeaders = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        if innitData:
            self.data = innitData
        else:
            url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}"
            self.data = requests.get(url, headers=self.getHeaders).json()["data"]["fuel"]

        self.currentFuel = self.data["current"]
        self.capacity = self.data["capacity"]
        self.consumed = None

    def update(self, manual):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}"
        self.data = manual if manual else self.data = requests.get(url, headers=self.getHeaders).json()["data"]["fuel"]

    def refuel(self, units):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/refuel"

        payload = {"units": units}

        response = requests.post(url, json=payload, headers=self.postHeaders)
        return response.status_code
