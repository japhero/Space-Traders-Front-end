import json
import requests
from pprint import pprint
import urllib3

urllib3.disable_warnings()


class System:

    def __init__(self, systemId) -> None:

        requestsUrl = f"https://api.spacetraders.io/v2/systems/{systemId}/waypoints"

        mainJsonPath = 'mainPlayer.json'
        f = open(mainJsonPath, 'r')
        rawPlayerData = json.load(f)
        token = rawPlayerData['data']['token']

        requestHeader = {'Authorization': f'Bearer {token}'}

        currRequest = requests.get(requestsUrl, headers=requestHeader, verify=False)
        self.systemsData = currRequest.json()

        self.systemSymbol = systemId
        self.planets = self.systemsData['data']

        # pprint(self.planets)

    def findTraitInSystem(self, target):

        """_Find a given trait in a system for example a scrapyard or shipyard

        Raises:
            Exception: raises when target isn't spelled correctly or no target exists.

        Returns:
            string : Json string of the plannet object with the target trait or returns none if the trait isnt found.
        """

        if not target[0].isupper() and target[-1].isupper():
            raise Exception('check spelling. Is case sensitive!')

        for index, planet in enumerate(self.planets):
            for trait in planet['traits']:
                if target == trait['name'] or target == trait['symbol']:
                    return planet
                    # ITSSSS TOO DEEP
        return None

    def getPlanetLoc(self, index=None, symbol=None):

        """ gets the x,y cords of a planet given the symbol or index
        
        Raises:
            when neither index or symbol is given it throws an error and asks for the index or symbol

        Returns:
            list: returns a list in the form of (x,y) holding the transform of an object
        """
        if not index and not symbol:
            raise Exception('needs a symbol or planet index')

        if symbol:
            for planetIndex, planet in enumerate(self.planets):
                if planet['symbol'] == symbol:
                    index = planetIndex
                    # Stop stacking ifs

        return (self.systemsData['data'][index]['x'], self.systemsData['data'][index]['y'])


'''
testSys = System('X1-ZR18')

ret = testSys.findTraitInSystem('Shipyard')

pprint(ret)
'''
