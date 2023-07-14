import json
import requests
from pprint import pprint
import urllib3
urllib3.disable_warnings()




class System():

    def __init__(self,systemId) -> None:
        
        requestsUrl = f"https://api.spacetraders.io/v2/systems/{systemId}/waypoints"
        
        mainJsonPath = 'mainPlayer.json'
        f = open (mainJsonPath,'r')
        rawPlayerData = json.load(f) 
        token = rawPlayerData['data']['token']

        requestHeader = {'Authorization': f'Bearer {token}'}
        
        

        currRequest = requests.get(requestsUrl,headers=requestHeader,verify= False)
        self.systemsData = currRequest.json()

        self.systemSymbol = systemId
        self.planets = self.systemsData['data']
        
        # pprint(self.planets)
        
       


    def findTraitInSystem(self,target):
        
        if not target[0].isupper() and target[-1].isupper() :
            raise Exception('check spelling. Is case sensative!')

        for index,planet  in enumerate(self.planets):
            for trait in planet['traits']:
                if target == trait['name'] or target == trait['symbol']:
                    return planet
                    # ITSSSS TOO DEEEP

        return None 
    
    
    def getPlanetLoc(self,index, symbol = None):


        if symbol:
            for Cindex,planet  in enumerate(self.planets):
                if planet['symbol'] == symbol:
                    index = Cindex
                    #Stop stacking ifs 

        return  (self.systemsData['data'][index]['x'],self.systemsData['data'][index]['y'])

testSys = System('X1-ZR18')



ret = testSys.findTraitInSystem('Shipyard')

pprint(ret)