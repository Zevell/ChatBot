import json
groupings = None

with open('groupings.json') as jsonFile:
  groupings = json.load(jsonFile)
