import json
import requests
import uuid
import time

response = requests.get("https://data.kcmo.org/resource/c46m-hv6s.json")
contracts = json.loads(response.text)
for x in contracts:
    x['effective_date'] = x.pop('contract_date')
    x['supplier'] = x.pop('vendor')
    x.update({
        'id' : str(uuid.uuid4()),
        'type' : 'add',
        'fields' : {
            'buyer_lead_agency' : 'City of Kansas City, Missouri',
            'states' : 'MO',
                'contract_amount' : x['contract_amount'],
                'contract_number' : x['contract_number'],
                'department' : x['department'],
                'description' : x['description'],
                'effective_date' : x['effective_date'][0:10],
                'supplier' : x['supplier'],
        }
        })
    del x['contract_amount'], x['contract_number'], x['department'], x['description'], x['effective_date'], x['supplier']

with open('contracts.json', 'w') as outfile:
        json.dump(contracts, outfile)

for x in contracts:
    filename = x['id']+'.json'
    with open(filename, 'w') as outfile:
        json.dump(contracts, outfile)
