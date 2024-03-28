import requests
import json
from pathlib import Path


def getToken():
    endpoint = 'https://api.ebay.com/identity/v1/oauth2/token'

    # Setting up the parameters for the request

    secret_path =  Path(__file__).parent.parent / 'ebaySECRETS.json'
    print("hi")
    with open(secret_path, "r") as f:
        cred = json.load(f)
        encoded_credentials = cred["encoded_credentials"]

    print(encoded_credentials)
    

    headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encoded_credentials}'
    }

    body={
        'grant_type': 'client_credentials',
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    response = requests.post(endpoint, headers=headers, data=body)

    return response.json()['access_token']


def getEbayItemInfo(item:str, access_token:str):
    endpoint = f'https://api.ebay.com/buy/browse/v1/item_summary/search?q={item}&limit=1'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-EBAY-C-MARKETPLACE-ID': 'EBAY_US',
        'X-EBAY-C-ENDUSERCTX':'affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>'
    }

    response = requests.get(endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse and return the response JSON
        return response.json()
    else:
        print('Failed to retrieve data')
        print(response.text)
        return {}

def printReadable(jsonItem:json):
    print(json.dumps(jsonItem, indent=4))


def parser(jsonItem:json) -> json:
    pass