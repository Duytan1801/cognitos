import requests
import json

params = {
    'active': True,
    'closed': False,
}

datas = requests.get('https://gamma-api.polymarket.com/events',params=params).json()
print(json.dumps(datas,indent=4))