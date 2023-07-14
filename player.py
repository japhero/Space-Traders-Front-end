import json
import requests
from pprint import pprint
import urllib3
urllib3.disable_warnings()


class player():

    def __init__(self,Name) -> None:

        
        
        self.mainJsonPath = r'mainPlayer.json'


        requestsUrl = "https://api.spacetraders.io/v2/register"
        requestHeader = {'Content-Type': 'application/json','Content-Length': '39'}
        payload = {'symbol': Name,'faction': 'VOID'}
        currRequest = requests.post(requestsUrl,headers=requestHeader,verify= False,json=payload)

        # self.rawPlayerData = currRequest.json()
        f = open (self.mainJsonPath,'r')
        
        self.rawPlayerData = json.load(f) 
        # pprint(self.rawPlayerData)



        with open('mainPlayer.json', 'w') as f:
            json.dump(self.rawPlayerData, f)


        self.token = self.rawPlayerData['data']['token']
        self.agent = self.rawPlayerData['data']['agent']
        self.contract = self.rawPlayerData['data']['contract']
        self.faction = self.rawPlayerData['data']['faction']
        self.ships = self.rawPlayerData['data']['ship']
        
        
    def getMyShipIds(self):
        # Gets all of your ship ids 
        url = "https://api.spacetraders.io/v2/my/ships"
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiVVNSMzM0MjEiLCJ2ZXJzaW9uIjoidjIiLCJyZXNldF9kYXRlIjoiMjAyMy0wNy0wOCIsImlhdCI6MTY4OTI0MzE5OSwic3ViIjoiYWdlbnQtdG9rZW4ifQ.oBemSbEv7bTjj0vlKSBvZwWQ2abOWh_5FLDZpxBPGRj6p4aO9wwRfBWaU3EmMjY57QIk-gJ6ycVT6zbRm13-qVTdF6_My-iqIsgbEGork6l3MHPPGykr3nS9m3swUlGsvHB7HeTxFUI0xacOudam3MooZaC1uLErSiclShaSag2gQEecSKqNr-G21fx5tYMQP58JY6g1WTWnvE450d_yWCC4MRZGH9_0DxcvHmQXUaa66xMDk4cRxceMk0z9BR6o5zTvP2lQULeZwhEIPhx3o8PEIPjB8iNcRNJnxYR9umYdYcYJetpOYczF7-LflG5O3jRbDFtyBxs2NoegileLLw"
        }
        response = requests.get(url, headers=headers,verify= False)

        self.ships = response.json()['data']

        idList = []
        for ship in self.ships:
           idList.append(ship['symbol']) 
        return idList if idList else None
    
    def getToken(self):
        return self.token



    def getCredits(self):
        url = "https://api.spacetraders.io/v2/my/agent"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers,verify=False)

        return response.json()['data']['credits']



p = player('player37134')
c = p.getCredits()
print(c)

