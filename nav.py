import json
import requests
from pprint import pprint
import urllib3
urllib3.disable_warnings()


class nav():

    def __init__(self,NavObject = None,shipId = None) -> None:
        
        if NavObject:
            self.navInfo = NavObject
        elif shipId:

            self.url = F"https://api.spacetraders.io/v2/my/ships/{shipId}"


            self.headers = {
                "Accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiVVNSMzM0MjEiLCJ2ZXJzaW9uIjoidjIiLCJyZXNldF9kYXRlIjoiMjAyMy0wNy0wOCIsImlhdCI6MTY4OTI0MzE5OSwic3ViIjoiYWdlbnQtdG9rZW4ifQ.oBemSbEv7bTjj0vlKSBvZwWQ2abOWh_5FLDZpxBPGRj6p4aO9wwRfBWaU3EmMjY57QIk-gJ6ycVT6zbRm13-qVTdF6_My-iqIsgbEGork6l3MHPPGykr3nS9m3swUlGsvHB7HeTxFUI0xacOudam3MooZaC1uLErSiclShaSag2gQEecSKqNr-G21fx5tYMQP58JY6g1WTWnvE450d_yWCC4MRZGH9_0DxcvHmQXUaa66xMDk4cRxceMk0z9BR6o5zTvP2lQULeZwhEIPhx3o8PEIPjB8iNcRNJnxYR9umYdYcYJetpOYczF7-LflG5O3jRbDFtyBxs2NoegileLLw"
            }

            response = requests.get(self.url, headers= self.headers, verify= False)

            self.navInfo = response.json()['data']['nav']
        else:
            raise Exception('need NavObject or ship id to get Data pass one')


        self.systemSymbol =  self.navInfo['systemSymbol']
        self.waypointSymbol   = self.navInfo['waypointSymbol']
        


    def get_systemSymbol(self,flag = False):
        self.navInfo = requests.get(self.url, headers=self.headers, verify= False).json() if flag else self.navInfo
        self.systemSymbol =  self.navInfo['systemSymbol']
        return self.systemSymbol

    def  get_systemSymbol(self,flag = False):
        self.navInfo = requests.get(self.url, headers=self.headers, verify= False).json() if flag else self.navInfo
        self.waypointSymbol   = self.navInfo['waypointSymbol']
        return self.waypointSymbol   
    
