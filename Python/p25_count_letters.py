# p25_count_letters.py
# Brendan Knapp
# 2018-03-23
# Python 3.6.4
'''
Write a program that asks the user to input a sentence.
The program will ask the user what two letters are to be counted.
You must use a “for” loop to go through the sentence & count how many times 
the chosen letter appears in the sentence.
You are not allowed to use python built-in function "count()" or you'll get a Zero!
Output will show the sentence, the letter, and the number of times the letter
appears in the sentence.
'''

sentence = input("Please enter a sentence: ")
letter_1 = input("Please enter letter 1: ")
letter_2 = input("Please enter letter 2: ")

def letter_to_list(sentence, desired_letter):
  letters_found = list()
  for letter in sentence:
    if letter == desired_letter:
      letters_found.append(desired_letter)
  return(letters_found)
  
print("The letter \"{}\" occurs {} time(s)".format(letter_1, 
                                                   len(letter_to_list(sentence, 
                                                                      letter_1))))
print("The letter \"{}\" occurs {} time(s)".format(letter_2, 
                                                   len(letter_to_list(sentence,  
                                                                      letter_2))))
                                                                      
'''
Please enter a sentence: HELLO WORLD
Please enter letter 1: O
Please enter letter 2: L
The letter "O" occurs 2 time(s)
The letter "L" occurs 3 time(s)

Please enter a sentence: You are not allowed to use python built-in function "count()" or
you'll get a Zero!
Please enter letter 1: Z
Please enter letter 2: a
The letter "Z" occurs 1 time(s)
The letter "a" occurs 3 time(s)
'''
