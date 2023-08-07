import requests


class Reactor:
    """
    Its a fucking container it ain't that special lol

    """

    def __init__(self, token, shipSymbol, innitData=None):
        self.token = token
        self.shipSymbol = shipSymbol

        self.getHeaders = {
            "Accept": "application/json",
            "Authorization": "Bearer undefined"
        }

        if innitData:
            self.data = innitData
        else:
            url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}"
            self.data = requests.get(url, headers=self.getHeaders).json()["data"]["reactor"]

        self.symbol = self.data["symbol"]
        self.name = self.data["name"]
        self.powerOutput = self.data["powerOutput"]
        self.condition = self.data["condition"]
        self.requirements = self.data["requirements"]

    def update(self, manual=None):
        url = f"https://api.spacetraders.io/v2/my/ships/{self.shipSymbol}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        self.data = manual if manual else self.data = \
            requests.get(url, headers=headers, verify=False).json()["data"]["reactor"]

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_powerOutput(self):
        return self.powerOutput

    def get_condition(self):
        return self.condition

    def get_requirements(self):
        return self.requirements
