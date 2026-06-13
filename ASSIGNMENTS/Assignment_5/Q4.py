# Create a Python dictionary of 3 cities and their populations.
# Save it to "cities.json"
# 1. Then load the JSON and print each city and its population.
# 2. Ask the user for a new city & its population - update this info in the json file

import json

with  open("ASSIGNMENTS/Assignment_5/cities.json", "r") as f:
    print(cities.json)

    py_obj = json.loads(cities.json)

print(py_obj)
