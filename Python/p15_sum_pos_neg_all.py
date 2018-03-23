# p15_sum_pos_neg_all.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4
'''
Write a program that asks the user to enter 4 numbers (positive or negative).
The program shows:
the sum of all numbers (sumAll)
the sum of positive numbers (sumPos),
the sum of negative numbers (sumNeg)
'''

inputs = list()
positives = list()
negatives = list()

sum_neg = 0
sum_pos = 0
sum_all = 0

def is_neg_or_pos(number):
  if number > 0:
    positives.append(number)
  elif number < 0:
    negatives.append(number)

for i in range(0, 4, 1):
  input_value = float(input("enter a number: "))
  
  if input_value == 0:
    print("that's not positive or negative...")
    input_value = float(input("try again, enter a number: "))
  
  inputs.append(input_value)

for i in inputs:
  is_neg_or_pos(i)
  sum_all += i

for i in negatives:
  sum_neg += i
  
for i in positives:
  sum_pos += i

print("The sum of all numbers = %.1f" %sum_all)
print("The sum of all positives = %.1f" %sum_pos)
print("The sum of all negatives = %.1f" %sum_neg)

'''
enter a number: 1
enter a number: 2
enter a number: 3
enter a number: 4
The sum of all numbers = 10.0
The sum of all positives = 10.0
The sum of all negatives = 0.0

enter a number: 1
enter a number: -2
enter a number: 3
enter a number: -4
The sum of all numbers = -2.0
The sum of all positives = 4.0
The sum of all negatives = -6.0
'''
