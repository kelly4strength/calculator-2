"""Calculate various mathematical functions"""
#imports all arithmetic.py (module)
from arithmetic import *

#initiate blank prompt for user input
user_input_raw = raw_input()
#create a list from the raw input
user_input_list = user_input_raw.split(" ")

if len(user_input_list) == 2:
#Assign variables to list elements
    operator = user_input_list[0]
    num1 = int(user_input_list[1])
    if operator == "square": 
        #Create variable for module call
        answer = square(num1)
        print answer

    if operator == "cube": 
        #Create variable for module call
        answer = cube(num1)
        print answer

elif len(user_input_list) > 2:
    operator = user_input_list[0]
    num1 = int(user_input_list[1])
    num2 = int(user_input_list[2])
    #Evaluate operator variable
    if operator == "+": 
        #Create variable for module call
        answer = add(num1,num2)
        print answer

    if operator == "-": 
        #Create variable for module call
        answer = subtract(num1,num2)
        print answer

    if operator == "*": 
        #Create variable for module call
        answer = multiply(num1,num2)
        print answer

    if operator == "/": 
        #Create variable for module call
        answer = divide(num1,num2)
        print answer

    if operator == "**": 
    #Create variable for module call
        answer = power(num1,num2)
        print answer

    if operator == "%": 
    #Create variable for module call
        answer = mod(num1,num2)
        print answer




