# p10_letter_grade.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4
'''
Write a program which asks the user for a student's grade as a percent, 
and then returns their letter grade.

NOTE: You must VALIDATE the INPUT (so make sure the number is between 
0 - 100 ... for any other number, say "ERROR" and ask for another number)
'''

percent = float(input("Please enter your grade percent: "))

if percent < 0 or percent > 100:
  print("ERROR")
  print("invalid percent entered, must be b/w 0-100")
  percent = float(input("Please enter your grade percent: "))
elif(percent >= 90 and percent <= 100):
  print("The letter grade is an 'A'")
elif(percent >= 80 and percent < 90):
  print("The letter grade is an 'B'")
elif(percent >= 70 and percent < 80):
  print("The letter grade is an 'C'")
elif(percent >= 60 and percent < 70):
  print("The letter grade is an 'D'")
elif(percent < 60):
  print("The letter grade is an 'F'")
  
'''
$ python p10_letter_grade.py
Please enter your grade percent: 102
ERROR
invalid percent entered, must be b/w 0-100
Please enter your grade percent: 90

$ python p10_letter_grade.py
Please enter your grade percent: 20
The letter grade is an 'F'

$ python p10_letter_grade.py
Please enter your grade percent: 65
The letter grade is an 'D'

$ python p10_letter_grade.py
Please enter your grade percent: 73
The letter grade is an 'C'

$ python p10_letter_grade.py
Please enter your grade percent: 87
The letter grade is an 'B'

$ python p10_letter_grade.py
Please enter your grade percent: 92
The letter grade is an 'A'
'''
