import requests
from pprint import pprint
import urllib3

urllib3.disable_warnings()


class Player:

    def __init__(self, Name) -> None:

        self.mainJsonPath = r'mainPlayer.json'

        requestsUrl = "https://api.spacetraders.io/v2/register"
        requestHeader = {'Content-Type': 'application/json', 'Content-Length': '39'}
        payload = {'symbol': Name, 'faction': 'VOID'}
        currRequest = requests.post(requestsUrl, headers=requestHeader, verify=False, json=payload)

        self.rawPlayerData = currRequest.json()
        # f = open(self.mainJsonPath, 'r')

        # self.rawPlayerData = json.load(f) 
        # pprint(self.rawPlayerData)

        # with open('mainPlayer.json', 'w') as f:
        #     json.dump(self.rawPlayerData, f)

        self.token = self.rawPlayerData['data']['token']
        self.agent = self.rawPlayerData['data']['agent']
        self.contract = self.rawPlayerData['data']['contract']
        self.faction = self.rawPlayerData['data']['faction']
        self.ships = self.rawPlayerData['data']['ship']

    def getMyShipIds(self, returnShips=False):
        # Gets all of your ship ids 
        url = "https://api.spacetraders.io/v2/my/ships"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"  #
        }
        response = requests.get(url, headers=headers, verify=False)

        self.ships = response.json()['data']

        idList = []
        for ship in self.ships:
            idList.append(ship['symbol']) if not returnShips else idList.append(ship)
        return idList if idList else None

    def getToken(self):
        return self.token

    def getCredits(self):
        url = "https://api.spacetraders.io/v2/my/agent"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers, verify=False)

        return response.json()['data']['credits']

    def purchase_ship(self, wishedType, amount=1):

        for shipNum in range(1, amount + 1):
            pass

# p = Player('player313254')
# c = p.getCredits()
# print(p.getToken())
# print(c)
