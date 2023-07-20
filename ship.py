import requests
from pprint import pprint
import urllib3
from nav import nav

urllib3.disable_warnings()
from responseCatcher import responseCatcher


class Ship:

    def __init__(self, shipId, token) -> None:
        url = f"https://api.spacetraders.io/v2/my/ships/{shipId}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers, verify=False)

        self.shipData = response.json()["data"]
        self.currentFuel = self.shipData["fuel"]["current"]
        self.fuelCapacity = self.shipData["fuel"]["capacity"]
        self.shipSymbol = shipId
        self.token = token

        self.nav = nav(token, shipId=self.shipSymbol)

    def update(self):
        """
        standard update function for updating data and also calling for dependencyUpdates.
        makes sure to manually update to save calls to api.


        """

        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        self.shipData = requests.get(url, headers=headers, verify=False).json()["data"]

        self.nav.update(self.shipData["nav"])

    def jump(self, jumpLocation):
        """

        Args:
            jumpLocation: the waypoint marker for the jump 

        Returns:
            object:
        """
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/jump"

        payload = {"systemSymbol": f"{jumpLocation}"}

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.post(url, json=payload, headers=headers, verify=False)
        return response.status_code

    def orbit(self):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/orbit"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.post(url, headers=headers)
        return response.status_code

    def navigate(self, waypoint):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/navigate"

        payload = {"waypointSymbol": str(waypoint)}
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.status_code

    def warp(self, waypointSymbol):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/warp"

        payload = {"waypointSymbol": waypointSymbol}
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.status_code

    def dock(self):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}/dock"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer undefined"
        }

        response = requests.post(url, headers=headers)
        return response.status_code
