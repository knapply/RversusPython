# p_39_first_last_word.py
# Brendan Knapp
# 2018-04-05
'''
Write a program which asks the user to enter a sentence, then shows the
first and last words of the sentence. The sentence can consist of many words, 
and each word can be of different length.
'''

def get_len(some_vars):
  le_len = 0
  for each_var in some_vars:
    le_len = le_len + 1
  return(le_len)

words = input("Enter a sentence: ").split()
first_word = words[0]
last_word = words[get_len(words) - 1]

print("Your sentence has {} words.".format(get_len(words)))
print("First word: '{}'".format(first_word))
print("Last word: '{}'".format(last_word))

'''
Your sentence has 5 words.
First word: 'here's'
Last word: 'sentence'
'''
