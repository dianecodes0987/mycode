#!/usr/bin/env python3

import netifaces

def printip(name):
    print("IP: ", end='')
    
print(netifaces.ifaddresses("io"))

#print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')

    try:
        print("MAC: ", end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print("IP: ", end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:
        print ("Could not collect adapter info") #error message



