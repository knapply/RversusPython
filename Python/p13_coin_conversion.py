# p13_coin_conversion.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4
'''
Write a program to convert any given number of total cents (under 100)
into the correct number of: quarters, dimes, nickels, pennies.
'''

cents = int(input("Please enter total cents: "))

quarters = int(cents / 25)
if quarters > 0:
  print("# of quarters: %i quarters x 25c = %i cents total" %(quarters, quarters * 25))
  cents = cents - (quarters * 25)

dimes = int(cents / 10)
if dimes > 0:
  print("# of dimes: %i dimes x 10c = %i cents total" %(dimes, dimes * 10))
  cents = cents - (dimes * 10)

nickels = int(cents / 5)
if nickels > 0:
  print("# of nickels: %i nickels x 5c = %i cents total" %(nickels, nickels * 5))
  cents = cents - (nickels * 5)
  
pennies = int(cents)
if pennies > 0:
  print("# of pennies: %i pennies x 1c = %i cents total" %(pennies, pennies))
  
'''
Please enter total cents: 66
# of quarters: 2 quarters x 25c = 50 cents total
# of dimes: 1 dimes x 10c = 10 cents total
# of nickels: 1 nickels x 5c = 5 cents total
# of pennies: 1 pennies x 1c = 1 cents total

Please enter total cents: 16
# of dimes: 1 dimes x 10c = 10 cents total
# of nickels: 1 nickels x 5c = 5 cents total
# of pennies: 1 pennies x 1c = 1 cents total

Please enter total cents: 6
# of nickels: 1 nickels x 5c = 5 cents total
# of pennies: 1 pennies x 1c = 1 cents total

Please enter total cents: 4
# of pennies: 4 pennies x 1c = 4 cents total
'''

