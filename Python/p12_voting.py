# p12_voting.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4
'''
Write a program to determine if the user can vote. 
The program will ask the user a series of questions - age,
citizenship and registration. The user will receive a message
as to whether or not s/he may vote -- yes, no (with a reason -
too young, not a citizen, hasn't registered to vote).
'''

age = int(input("How old are you? "))
citizen = input("Are you a citizen? (y/n) ")
registered = input("Are you registred? (y/n) ")

if age >= 18 and citizen == "y" and registered == "y":
  print("Congratulations, you can vote!")
else:
  print("Sorry, you cannot vote")
  if age < 18:
    print("-You are not old enough.")
  if citizen != "y":
    print("-You must be a citizen.")
  if registered != "y":
    print("-You must be registered")

'''
How old are you? 18
Are you a citizen? (y/n) y
Are you registred? (y/n) y
Congratulations, you can vote!

How old are you? 17
Are you a citizen? (y/n) y
Are you registred? (y/n) y
Sorry, you cannot vote
-You are not old enough.

How old are you? 16
Are you a citizen? (y/n) n
Are you registred? (y/n) y
Sorry, you cannot vote
-You are not old enough.
-You must be a citizen.

How old are you? 12
Are you a citizen? (y/n) n
Are you registred? (y/n) n
Sorry, you cannot vote
-You are not old enough.
-You must be a citizen.
-You must be registered
'''
