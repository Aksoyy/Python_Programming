import json
from urllib.request import urlopen

# https://randomuser.me/api/?results=5000

with urlopen("https://randomuser.me/api/") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

# usd_rates = dict()

# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price

# print(50 * float(usd_rates['USD/INR']))