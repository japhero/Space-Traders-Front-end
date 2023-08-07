import requests
from pprint import pprint


class Navigation:

    def __init__(self, token, shipSymbol, NavObject=None, ) -> None:

        if NavObject:
            self.navInfo = NavObject
        elif shipSymbol:

            self.url = F"https://api.spacetraders.io/v2/my/ships/{shipSymbol}/nav"

            self.headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {token} "
            }

            response = requests.get(self.url, headers=self.headers, verify=False)

            self.navInfo = response.json()['data']
            # pprint(self.navInfo)
        else:
            raise Exception('need NavObject or ship id to get Data pass one')

        self.token = token
        self.shipSymbol = shipSymbol
        self.systemSymbol = self.navInfo['systemSymbol']
        self.waypointSymbol = self.navInfo['waypointSymbol']
        self.status = self.navInfo['status']
        self.flightMode = self.navInfo['flightMode']
        self.updateFlag = False
        self.travelTime = 0

    def update(self, manualData, returnSelf=False):
        """
        updates the nav object by calling for the most recent data or accepting data to pass

        Args:
            manualData: if passed allows the user to pass nav data instead of calling the api
            made to save api calls.
            returnSelf: A flag that if true returns the nav data.

        Returns: nav json string

        """

        self.navInfo = requests.get(self.url, headers=self.headers, verify=False).json()[
            'data'] if not manualData else self.navInfo = manualData
        if returnSelf:
            return self.navInfo

    def get_systemSymbol(self, flag=False):
        self.navInfo = requests.get(self.url, headers=self.headers, verify=False).json()[
            'data'] if flag else self.navInfo
        self.systemSymbol = self.navInfo['systemSymbol']
        return self.systemSymbol

    def get_ship_waypointSymbol(self, flag=False):
        self.navInfo = requests.get(self.url, headers=self.headers, verify=False).json()[
            'data'] if flag else self.navInfo
        self.waypointSymbol = self.navInfo['waypointSymbol']
        return self.waypointSymbol

    def get_status(self, flag=False) -> str:
        self.navInfo = requests.get(self.url, headers=self.headers, verify=False).json()[
            'data'] if flag else self.navInfo
        self.status = self.navInfo["status"]
        return self.status

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

#
# tk = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUExBWUVSMzEzMjU0IiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDctMTUiLCJpYXQiOjE2ODk2NzY2NjgsInN1YiI6ImFnZW50LXRva2VuIn0.tZAdqiJed61JGEqiZkmjX4d6BSjErBqyw-UDkgN74sAdkOi20myKT9-1e1bxZaSEAON38eg145FHTISHrhzqE2SU-CbzU78qWGhcEylmhVpdgBLh-982YLRcUjOe4bCRYb3S2KrT75JYXTDlX3Pl36Q4C0cPyco6rltld1HfIndMm5PQQqoqXA1dFKqoqB8F2dAw4QmVQ_SF7Ez_dm-_e64DtFgrbD8SK_ZF2OWZCgmGocfCHkBZxU2yCeuRvCyFZh5XS-f3k3Zc1FwpS3wM01yMLBckLx7_WEjg1SFXbwVh04SnzkgV5ak15dOzRXLhBAtIQjACTKomflnJ3OyMbg'
# n = nav(tk,shipId=  'PLAYER313254-1')
#
# print(f': {n.get_status(True)}')
