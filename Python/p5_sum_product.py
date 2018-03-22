# p5_sum_product.py
# Brendan Knapp
# 2018-03-06
# Python 3.6.4
# Description: Write a program which computes the sum and 
#              product of two numbers entered by the user.

num_1 = int(input("Enter the first number: "))

num_2 = int(input("Enter the second number: "))

sum = num_1 + num_2

product = num_1 * num_2

print("The sum of %i and %i is %i." %(num_1, num_2, sum))
print("The product of %i and %i is %i." %(num_1, num_2, product))

'''
Run:
$ python Python/p5_sum_product.py
Enter the first number: 5
Enter the second number: 6
The sum of 5 and 6 is 11.
The product of 5 and 6 is 30.
'''
