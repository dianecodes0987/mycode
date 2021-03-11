#!/usr/bin/env python3

def addition(a,b):
    result = a + b
    return result

def subtraction(a,b):
    result = a - b
    return result

def multiply(a,b):
    result = a * b
    return result

def divide(a,b):
    result = a/b
    return result

while True:
    try:
        a = float(input("Enter 1st number: "))
        break
    except:
        print("An invalid number was entered")
        
while True:
    try:
        b = float(input("Enter 2nd number: "))
        break
    except:
        print("An invalid number was entered")

while True:
    action = input("Enter operation (+, -, *, /: ").lower()
    if action in ["+","-","*","/"]:
        break
    else:
        print("invalid operation")

if action == "+":
    print(f"Result = {addition(a,b)}")
elif action == "-":
    print(f"Result = {subtraction(a,b)}")
elif action == "*":
    print(f"Result = {multiply(a,b)}")
elif action == "/":
    print(f"Result = {divide(a,b)}")
