import json
import requests
from pprint import pprint
import urllib3
urllib3.disable_warnings()


class ship():

    def __init__(self,shipId) -> None:
        self.id = shipId


        self.nav()
        self.fuel 
        