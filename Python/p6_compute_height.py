# p6_compute_height.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4

'''
Write a program to compute a person's height.

INPUT: User will enter two whole numbers: feet and inches.

OUTPUT: Values input & total in inches.
'''

print("please enter your height")
feet = float(input("feet: "))
inches = float(input("inches: "))

total_inches = feet * 12 + inches

print("%.0f feet %.0f inch(es) = %.0f inches" %(feet, inches, total_inches))

'''
$ python p6_compute_height.py
please enter your height
feet: 6
inches: 5
6 feet 5 inch(es) = 77 inches
'''
