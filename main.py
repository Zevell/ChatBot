import json
import random
groupings = None

with open('groupings.json') as jsonFile:
  groupings = json.load(jsonFile)

while True: 
  userInput = input("")
  
  for group in groupings['groupings']:
    for keyword in group['keywords']:
      if keyword in userInput:
        print(random.choice(group['responses']))