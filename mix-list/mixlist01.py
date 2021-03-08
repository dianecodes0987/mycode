#!/usr/bin/env python3

#create a list
my_list = [ "192.168.0.5", 5060, "UP" ]

#print first entry
print("The first item in the list (IP): " + my_list[0] )

#print 2nd
print("The second item in the list (port): " + str(my_list[1]) )

#print 3rd
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#print(f"{my_list[3]} stuff")

print(f"When I ssh into IP addresses {new_list[3]} or {new_list[4]} i am unable to ping ports {str(new_list[0])}, {new_list[1]}, or {str(new_list[2])}")
