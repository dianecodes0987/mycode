#!/usr/bin/python3
round = 0
answer = " "

while round < 3 and answer.lower() != "Brian".lower():
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer.lower()  == "Brian".lower(): # logic to check if user gave correct answer
        print("Correct!")
    elif answer.lower() == "shrubbery":
        print("you gave the super secret answer!")
        round = 4
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

