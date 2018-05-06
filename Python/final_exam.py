# final_exam.py
# Brendan Knapp
# 2018-05-06
# Python 3.6.4
'''
A) Use a for loop to make 10 random numbers between 20 and 30 and store them in a 
variable numList .
B) Sort the list. You may not use the sort(), sorted() or any other built-in 
python function!
C) Show the sorted list and the unsorted list
D) Find the sum, and average of the numbers in numList. You main not use sum() or
average() python functions!
E) Find the median of the list.
F) Show how many numbers are evenly divisible by 2
'''

from random import randint
# import statistics # ONLY USED TO CHECK THE RESULTS!
                    # uncomment here and "Passes" print() lines
                    # if you'd like to do same

# utils
def get_len(nums):
  len = 0
  for num in nums:
    len += 1
  return(len)

def get_sum(nums):
  sum = 0
  for num in nums:
    sum += num
  return(sum)

def get_mean(nums):
  mean = get_sum(nums) / get_len(nums)
  return(mean)

def get_median(nums):
  if get_len(nums) % 2 == 0:
    median = get_mean([nums[get_len(nums) // 2 - 1], nums[get_len(nums) // 2]])
  else:
    median = nums[get_len(nums)//2]
  return(median)
  
def which_divisible_by2(nums):
  divisible_by2 = []
  for num in nums:
    if num % 2 == 0 and num not in divisible_by2:
      divisible_by2.append(num)
  return(divisible_by2)

# A) =====================================================================================
## create list of random numbers
num_list = []
for i in range(0, 10, 1):
  num_list.append(randint(20, 31))

# keep a copy in the original order
unsorted_list = num_list.copy()

# B) Sort the list =======================================================================
for i in range(0, get_len(num_list)):
  for j in range(0, get_len(num_list) - 1, 1):
    if num_list[j] > num_list[j + 1]:
      temp = num_list[j]
      num_list[j] = num_list[j + 1]
      num_list[j + 1] = temp
      
# C) Show the sorted list and the unsorted list ==========================================
print("C) {}".format("=" * 60))
# print("Passes `sorted()` check? -> {}".format(num_list == sorted(unsorted_list)))
print("Sorted List -> {}".format(num_list))
print("Unsorted List -> {}".format(unsorted_list), end = "\n\n")

# D) Find the sum, and average of the numbers ============================================
the_sum = get_sum(num_list)
the_mean = get_mean(num_list)
# E) Find the median =====================================================================
the_median = get_median(num_list)
# F) Show how many numbers are evenly divisible by 2 =====================================
divisible_by_2 = which_divisible_by2(num_list)


print("D) {}".format("=" * 60))
# print("Passes `sum()` check? -> {}".format(sum(num_list) == the_sum)) ###
print("Sum -> {}".format(the_sum))
# print("Passes `mean()` check? -> {}".format(statistics.mean(num_list) == the_mean)) ###
print("Average -> {}".format(the_mean), end = "\n\n")

print("E) {}".format("=" * 60))
# print("Passes `median()` check? -> {}".format(statistics.median(num_list) == the_median)) ###
print("Median -> {}".format(the_median), end = "\n\n")

print("F) {}".format("=" * 60))
print("How many numbers are divisible by 2? -> {}".format(get_len(divisible_by_2)))
print("   ... and they are -> {}".format(", ".join(list(map(str, divisible_by_2)))))

# G) Submit the Output of your program (A-F) as a multiline comment at ===================
# the bottom of your program .
'''
C) ============================================================
Sorted List -> [20, 20, 21, 21, 23, 23, 24, 24, 24, 28]
Unsorted List -> [28, 21, 23, 20, 24, 21, 23, 20, 24, 24]

D) ============================================================
Sum -> 228
Average -> 22.8

E) ============================================================
Median -> 23.0

F) ============================================================
How many numbers are divisible by 2? -> 3
   ... and they are -> 20, 24, 28
'''




