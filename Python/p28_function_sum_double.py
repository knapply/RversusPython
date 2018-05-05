# p28_function_sum_double.py
# Brendan Knapp
# 2018-04-05
# Python 3.6.4
'''
Write a function sum_double(a,b) which given two integer parameters 
RETURNS  their sum.

Unless the two values are the same, then the function SHOWS their 
doubled sum.
'''

def sum_double(a, b):
  if a == b:
    print("Doubled sum of {} and {} is: {} (SHOW)".format(a, b, (a + b) * 2))
  else:
    return("Doubled sum of {} and {} is: {} (RETURN)".format(a, b, ((a + b) * 2)))
    
sum_double(1, 1)
sum_double(2, 2)

print(sum_double(1, 2))
print(sum_double(3, 4))

'''
Doubled sum of 1 and 1 is: 4 (SHOW)
Doubled sum of 2 and 2 is: 8 (SHOW)
Doubled sum of 1 and 2 is: 6 (RETURN)
Doubled sum of 3 and 4 is: 14 (RETURN)
'''

    
