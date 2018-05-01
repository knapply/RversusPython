# p_38_find_longest_word.py
# Brendan Knapp
# 2018-04-05
'''
Write a program that asks the user to enter a sentence.

The program then finds the longest word in the sentence, and shows it.
'''

def get_max(nums):
  le_max = 0
  for num in nums:
    if num > le_max:
      le_max = num
  return(le_max)
  
def get_len(some_vars):
  le_len = 0
  for each_var in some_vars:
    le_len = le_len + 1
  return(le_len)
  
def get_word_lens(words):
  les_lens = []
  for word in words:
    les_lens.append(get_len(word))
  return(les_lens)

words = input("Enter a sentence: ").split()
longest = [word for word in words if get_len(word) == get_max(get_word_lens(words))][0]

print("The longest word is: {}".format(longest))
print("It is {} characters long.".format(get_len(longest)))

'''
Enter a sentence: which of these words is the longest
The longest word is: longest
It is 7 characters long.
'''
