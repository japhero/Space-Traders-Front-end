import requests
from pprint import pprint
import urllib3
from nav import nav

urllib3.disable_warnings()
from responseCatcher import responseCatcher


class Cargo:

    def __init__(self, token, shipId, innitData=None):
        self.shipId = shipId
        self.token = token

        self.url = f"https://api.spacetraders.io/v2/my/ships/{self.shipId}/cargo"

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

    def have(self, target, returnUnits=True, upFlag=False):
        self.data = requests.get(self.url, headers=self.headers).json()["data"] if upFlag else self.data

        for item in self.data["inventory"]:
            if item["symbol"] == target:
                return item["units"] if returnUnits else True
        return False
