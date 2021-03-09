#!/usr/bin/env python3
ipchk = input("Apply an IP address: ")

# a string tests as True
if ipchk == "192.168.70.1":
    print("this is the ip of the gateway, it's not available")
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)
else: #if nothing is set by the user
    print("you didn't enter an input")

