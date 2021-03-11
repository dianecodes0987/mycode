#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # display the methods available to our new object
    #print( dir(r) )

    print(r.json[0]) #random.randrange(0, len(r.json())-1)) #.get("text")
    #print(random.randrange(0,len(r.json())-1))
    #print(len(r.json())-1)
    #for catfact in r.json():
       # print(catfact.get("text"))
     #  print(catfact["text"])
      # print()

main()

