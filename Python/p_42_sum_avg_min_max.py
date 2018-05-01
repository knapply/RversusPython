# p_42_sum_avg_min_max.py
# Brendan Knapp
# 2018-04-05
'''
Write the definitions for the following 4 functions:

sum (list_parameter) : returns the sum of numbers inside a list
average (list_parameter) : returns the average of numbers inside a list
min (list_parameter) : returns the smallest of all numbers inside a list
max (list_parameter) : returns the largest of all numbers inside a list
main () : calls all the other functions
'''

def get_len(nums):
  len = 0
  for num in nums:
    len += 1
  return(len)

def sum(nums):
  sum = 0
  for num in nums:
    sum += num
  return(sum)

def average(nums):
  average = sum(nums) / get_len(nums)
  return(average)

def min(nums):
  min = max(nums)
  for num in nums:
    if num < min:
      min = num
  return(min)

def max(nums):
  max = 0
  for num in nums:
    if num > max:
      max = num
  return(max)
  
def main():
  a_list = [1, 2, 3, 4, 5]
  print("The numbers are: {}.".format(", ".join(str(num) for num in a_list)))
  print("Their sum is {}.".format(sum(a_list)))
  print("Their average is {}.".format(average(a_list)))
  print("The minimum is {}.".format(min(a_list)))
  print("The maximum is {}.".format(max(a_list)))

main()
  
'''
The numbers are: 1, 2, 3, 4, 5.
Their sum is 15.
Their average is 3.0.
The minimum is 1.
The maximum is 5.
'''
