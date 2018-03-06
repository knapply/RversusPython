# p1_output.py
# Brendan Knapp
# 2018-03-06
# Python 3.6.4
# Description: Program to show output in Python

# 1) Type up the Example output.py program, including the comments (in RED), and get it working.
# 2) When the program runs, copy/paste the Output (in BLUE) at the bottom of your program as a multi-line comment '''     ''', then save the file

print('hello world') # single quote
print("hello world") # double quote
print("he\nllo") # \n insert a new line (same as pressing Enter)

# VARIABLES are named storage locations for numbers, strings, lists
# STRING is anything enclosed in quotes "Hello World", that's a string
# NUMBER can be either a float (Ex: 9.3) or an INTEGER (Ex: 9.0)
# LISTS are things like [1,2,3] or ["Brendan", "Knapp"]
my_name = "Brendan"    # declare/initialize string variable `my_name`
weight = 250.34152     # declare/initialize float variable `weight`
age = 30               # declare/initialize int variable `age`
grades = [90, 77, 88]
nameZ = ["Brendan", "Knapp"]

print("Hello ", my_name)
print("Your weight is ", weight, " and your age is ", age)
print("Your weight is %.2f and your age is %i" %(weight, age))
print("Lists: grades =", grades, "nameZ =", nameZ)
print("This is how your print", end = " ")
print("on the same line")

'''
Run:
$ python Python/p1_output.py
hello world
hello world
he
llo
Hello  Brendan
Your weight is  250.34152  and your age is  30
Your weight is 250.34 and your age is 30
Lists: grades = [90, 77, 88] nameZ = ['Brendan', 'Knapp']
This is how your print on the same line
'''

