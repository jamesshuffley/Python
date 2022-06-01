import requests
import json
from pprint import pprint

# pc_req = requests.get("https://api.postcodes.io/postcodes/S8 9EG")
#
# # print(pc_req, type(pc_req))
#
# if pc_req.status_code == 200:
#     # pprint(dict(pc_req.headers), sort_dicts=False)
#     # print(type(pc_req.content))
#     # print(pc_req.content)
#     postcode = json.loads(pc_req.content)
#     pprint(postcode, sort_dicts=False)
#     print(postcode["result"]['admin_district'])
#     print(postcode["result"]['eastings'])
#     print(postcode["result"]['northings'])
#     print(postcode["result"]['codes']['nuts'])

headers = {'Content-Type': 'application/json'}
body = {'postcodes': ['S8 9EG', 'HG4 2RY', 'EH9 1NX']}

pc_req = requests.post(
    "https://api.postcodes.io/postcodes/",
    headers=headers,
    data=json.dumps(body)
)

# print(pc_req)
pcs = pc_req.json()['result']
print(pcs)

# admin_ward, easting and northings and nuts code

for pc_data in pcs:
    result = pc_data['result']
    print('----', result['postcode'], '----')
    print(result['admin_ward'])
    print(result['eastings'], result['northings'])
    print(result['codes']['nuts'])




