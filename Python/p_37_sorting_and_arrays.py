# p_37_sorting_and_arrays.py
# Brendan Knapp
# 2018-04-05

# CodingBat centered_average
def get_sum(nums):
  sum = 0
  for num in nums:
    sum += num
  return(sum)
  
def get_max(nums):
  max = 0
  for num in nums:
    if num > max:
      max = num
  return(max)
  
def get_min(nums):
  min = get_max(nums)
  for num in nums:
    if num < min:
      min = num
  return(min)
  
def get_len(nums):
  len = 0
  for num in nums:
    len = len + 1
  return(len)
  
def centered_average(nums):
  return (get_sum(nums) - get_max(nums) - get_min(nums)) / (get_len(nums) - 2)

# CodingBat sum13 ====
def get_length(nums):
  length = 0
  for num in nums:
    length = length + 1
  return(length)
    
def sum13(nums):
    le_sum = 0
    index = 0
    while index < get_length(nums):
        if nums[index] == 13:
            index += 1
        else:
            le_sum += nums[index]
        index += 1
        
    return(le_sum)
    
# CodingBat big_diff

