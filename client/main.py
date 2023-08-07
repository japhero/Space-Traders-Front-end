import json
import requests
import urllib3
from pprint import pprint



urllib3.disable_warnings()



token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiVVNSMzIxIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDctMDgiLCJpYXQiOjE2ODkyMzg1NzYsInN1YiI6ImFnZW50LXRva2VuIn0.w1EN3M2rKwD75gM1CGW446GGhxuVbcqP1euGkVuHtC5Fe2JJpRFWpi8m7i82l_w67rEj65AYaDnVsjHUEXfa4J-zYVz-vA4P2uMzXGnD0ze0fhJROnaEUG1JKQ3JlEE55mO-bhyC43X-kIKlTXYXfRakspiw1A0USXPavgrRUuE0UmRR_hXBXwcsRcNHuB9zyyMqgwlCEOH7t-asFIT8IPLgrJTtT8PR0Vwx3AqHLGWIbaR-ycy9PniiCpY0GmQV1YnSbn0sQ0egXoJpaZbqNwZxcXpmJzdmSWAdn03prXai_a36i2_zgfvp_lCTFR8bSiPoQwdXW7tuo-_rB3k9iA'

certificatePath = r'C:\Users\praktikant\Documents\Visual Studio code\Rest Project\cert\GG-CA.cer'

requestsUrl = "https://api.spacetraders.io/v2/register"
requestHeader = {'Content-Type': 'application/json','Content-Length': '39'}

payload = {'symbol': 'MainPLayer12','faction': 'VOID'}




currRequest = requests.post(requestsUrl,headers=requestHeader,verify= False,json=payload)

with open('../mainPlayer.json', 'w') as f:
    fileContents = currRequest.json()
    json.dump(fileContents, f)

#pprint(currRequest.json())





