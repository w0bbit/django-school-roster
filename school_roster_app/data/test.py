import json

with open('staff.json') as json_file:
  data = json.load(json_file)
  for i in data:
    print(i)