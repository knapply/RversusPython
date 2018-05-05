# midterm_short_programs.py
# Brendan Knapp
# 2018-04-05
'''
Function 1: Write a function which takes 2 float PARAMETERS distance and time.
The functions computes and SHOWS the speed = distance/ time rounded to 2 values
to the right of the decimal point.

Function 2: Write a function which takes 3 integer PARAMETERS num1, num2, num3.
The function then RETURNS the middle(median) value of the 3 arguments.
Assume 3 different values as parameters.
'''

def show_speed(distance, time, **kwargs):
  speed = distance / time
  print("speed = {:5.2f}".format(speed), **kwargs)

def middle(num1, num2, num3):
  unsorted_list = [num1, num2, num3]
  maximum = 0
  for num in unsorted_list:
    if num > maximum:
      maximum = num
  
  minimum = maximum
  for num in unsorted_list:
    if num < minimum:
      minimum = num
  
  for num in unsorted_list:
    if num not in [minimum, maximum]:
      median = num
  
  return("middle({}, {}, {}) -> returns {}".format(num1, num2, num3, median))
  

show_speed(130.108508, 2.123455)
show_speed(92.851242, 1.291241)
show_speed(32.851242, 12.291241, end = "\n\n")

print(middle(1, 2, 3))
print(middle(5, 4, 6))
print(middle(7, 9, 8))

'''
speed = 61.27
speed = 71.91
speed =  2.67

middle(1, 2, 3) -> returns 2
middle(5, 4, 6) -> returns 5
middle(7, 9, 8) -> returns 8
'''
