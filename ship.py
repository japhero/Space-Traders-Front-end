import json
import requests
from pprint import pprint
import urllib3
import nav
urllib3.disable_warnings()
from responseCatcher import responseCatcher

class ship():

    def __init__(self,shipId,token) -> None:
        
        
        url = "https://api.spacetraders.io/v2/my/ships/shipSymbol"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
            }

        response = requests.get(url, headers=headers,verify=False)
        
        self.id = shipId

        self.token = token
        self.nav = nav(token,shipId = self.id)
    
    
    
    def jump(self,jumpLocation):
        
        
        
        
        url = "https://api.spacetraders.io/v2/my/ships/shipSymbol/jump"

        payload = { "systemSymbol": f"{jumpLocation}" }
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.post(url, json=payload, headers=headers,verify=False)       
        responseCatcher(response.status_code())
        
        
        
