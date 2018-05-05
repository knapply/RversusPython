# p_47_file_io_reverse_sentence.py
# Brendan Knapp
# 2018-04-30
# 
'''
Write a program that asks the user to enter a sentence,
and then writes that sentence in reverse to a file named reverse.txt. 
Your solution must do the following (1) accept the sentence as a string input (2) 
split the sentence into a list of words (3) use a loop that iterates through the list
in reverse, starting from the last word and ending at the first word,
to write the words in reverse order into a file.
'''

sentence = input("Please enter a sentence: ").split()

rev_file = open("p_47_reverse.txt", "w")
for word in sentence[::-1]:
  rev_file.write(word + " ")

rev_file.close()
