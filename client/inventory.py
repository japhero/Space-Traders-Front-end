import requests
from pprint import pprint
import urllib3
from navigation import Navigation

urllib3.disable_warnings()
from responseCatcher import responseCatcher


class Cargo:

    def __init__(self, token, shipId, innitData=None):
        self.shipSymbol = shipId
        self.token = token

        self.url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/cargo"

        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        self.data = requests.get(self.url, headers=self.headers).json()[
            "data"] if not innitData else self.data = innitData

        self.capacity = self.data["capacity"]
        self.units = self.data["units"]
        self.inventory = self.data["Inventory"]

    def update(self, manual=None):
        self.data = requests.get(self.url, headers=self.headers).json()["data"] if not manual else self.data = manual

    def have(self, target, returnUnits=True, updateFlag=False):
        self.data = requests.get(self.url, headers=self.headers).json()["data"] if updateFlag else self.data

        for item in self.data["inventory"]:
            if item["symbol"] == target:
                return item["units"] if returnUnits else True
        return False

    def sellCargo(self, units, symbol):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/sell"

        payload = {
            "symbol": symbol,
            "units": units
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.status_code

    def transferCargo(self, itemSymbol, units, transferShipSymbol):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/transfer"

        payload = {
            "tradeSymbol": itemSymbol,
            "units": units,
            "shipSymbol": transferShipSymbol
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.status_code
