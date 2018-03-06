# p3_input.py
# Brendan Knapp
# 2018-03-06
# Python 3.6.4
'''
1) Type up the Example input.py program, including the comments (in RED), and get it working.

2) When the program runs, copy/paste the Output (in BLUE) at the bottom of your program as a multi-line comment '''     ''', then save the file

3) Submit input.py 
'''

name = input("Please enter your name: ") # this is a string
weight_lbs = float(input("Please enter your weight in lbs: ")) # a float
age = int(input("Please enter your age (whole number): ")) # an integer
weight_kg = weight_lbs * 0.453592
title = "Human"

print("Hello", title, name, "Your weight is")
print(weight_lbs, "lbs")
print("which equals = %.2f" %weight_kg, end = " ")
print("kilograms")

'''
Output:
Windows@DESKTOP-36QPOJ8  ~/Documents/RversusPython
$ cd Python
Windows@DESKTOP-36QPOJ8  ~/Documents/RversusPython/Python
$ python p3_input.py

Please enter your name: Brendan
Please enter your weight in lbs: 560
Please enter your age (whole number): 12
Hello Human Brendan Your weight is
560.0 lbs
which equals = 254.01 kilograms
'''
