# p9_user_height_message.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4
'''
You will write a program to compute a person's height and print out a message.

The user will input their height in feet and inches.

The program will convert the feet and inches into total_inches, 
and then print a message.
'''

print("Please enter your height: ")
feet = int(input("feet:"))
inches = int(input("inches: "))

total_inches = feet * 12 + inches

if total_inches > 72:
  print("You are tall.")
elif total_inches > 60:
  print("You are average.")
else:
  print("You are vertically challenged.")

'''
$ python p9_user_height_message.py
Please enter your height:
feet:6
inches: 5
You are tall.

$ python p9_user_height_message.py
Please enter your height:
feet:5
inches: 10
You are average.

$ python p9_user_height_message.py
Please enter your height:
feet:4
inches: 11
You are vertically challenged.
'''
