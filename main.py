import json
import random
groupings = None

with open('groupings.json') as jsonFile:
  groupings = json.load(jsonFile)

while True: 
  userInput = input("")
  
  for group in groupings['groupings']:
    for element in groupings['groupings']['keywords']:
      if userInput.contains(element):
        print(random.choice(groupings['groupings']['keywords']))