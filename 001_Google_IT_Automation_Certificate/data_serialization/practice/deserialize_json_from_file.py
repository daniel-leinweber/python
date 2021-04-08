#!/usr/bin/env python3

import json

with open('people.json', 'r') as people_json:
    people = json.load(people_json)

print(people)
