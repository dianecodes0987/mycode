#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

#print(challenge[2][1])
#print(trial[2]['eyes'])
#print(nightmare[0]['d'])

print(f"My {challenge[2][1]}! The {trial[2]['eyes']} do {nightmare[0]['d']}!")



