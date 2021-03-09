#!/usr/bin/env python3

print("determine your Fairy Tale name")

first_name = input("Enter the first letter of your first name? ").lower()

last_name = input("What is your favorite food? ").lower()

#determine first name
if first_name in ["a","z"]: #== "a" or first_name == "z":
    code_fname = "Anastasia"
elif first_name in ["b","y"]: # == "b" or first_name == "y":
    code_fname = "Sleeping"
elif first_name in ["c","x"]: # == "c" or first_name == "x":
    code_fname = "Belle"
elif first_name in ["d","w"]: #== "d" or first_name == "w":
    code_fname = "Prince"
elif first_name in ["e","v"]: # == "e" or first_name == "v":
    code_fname = "Aladdin"
elif first_name in ["f","n"]: #== "f" or first_name == "n":
    code_fname = "Gulliver"
elif first_name in ["g","o"]: # == "g" or first_name == "o":
    code_fname = "Romeo"
elif first_name in ["h","p"]: # == "h" or first_name == "p":
    code_fname = "Merlin"
elif first_name in ["i","q"]: # == "i" or first_name == "q":
    code_fname = "Wendy"
elif first_name in ["j","r"]: # == "j" or first_name == "r":
    code_fname = "Esmerelda"
elif first_name in ["k","s"]: # == "k" or first_name == "s":
    code_fname = "Jasmine"
elif first_name in ["l","t"]: # == "l" or first_name == "t":
    code_fname = "Briar"
elif first_name in ["m","u"]: # == "m" or first_name == "u":
    code_fname = "Gretel"
else:
    code_fname = "Doesn't listen"

if last_name:
    last_name1 = []
    last_name1.extend(last_name)

    number = len(last_name1)

    if number < 3:
        code_lname = "Slipper"
    elif number < 5:
        code_lname = "Meadow"
    elif number == 5:
        code_lname = "Hickory"
    elif number == 6:
        code_lname = "Applerose"
    elif number == 7:
        code_lname = "Hubbard"
    elif number == 8:
        code_lname = "Wolf"
    elif number == 9:
        code_lname = "Rooster"
    else:
        code_lname = "Cherry"

else:
    code_lname = "Mulberry"

print(f"Your Fairy Tale name is: {code_fname} {code_lname}")


# I really like this, it is very cool!

# As a challenge to try to improve your python skills, I think it would be neat if you would try using the syntax for "if ... in []"

# For example:
#if "a" in ["a", "b", "c"]:
 #   print("fairytale name")

#if "x" in ["a", "b", "c"]:
   # print("no name")

