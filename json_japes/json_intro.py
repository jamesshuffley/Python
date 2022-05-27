import json

# car_data = {
#     "make": "Tesla",
#     "type": "Electric",
#     "faults": 9384,
#     "death_trap": True,
#     "driver": None
# }
#
# print(car_data, type(car_data))
#
#  print(car_data["faults"])
#
# dumps = json.dumps(car_data)
#
# print(dumps, type(dumps))
#
# with open('tesla.json', 'w') as json_file:
#     json.dump(car_data, json_file)

with open("spartan.json") as json_file_2:
    spartan = json.load(json_file_2)

print(spartan)
