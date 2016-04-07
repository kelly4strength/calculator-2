"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""


from arithmetic import *
"""defining arithmetic to open the arithmetic.py file and
"""
user_input_raw = raw_input()
#user inputs string
#take that string and break it up/ unpack it
user_input_list = user_input_raw.split(" ")
# now identify what each element in the string means
operator = user_input_list[0]
num1 = int(user_input_list[1])
num2 = int(user_input_list[2])

if operator == "+":
    answer = add(num1,num2)
    print answer

