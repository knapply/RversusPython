# p27_count_random_letters.py
# Brendan Knapp
# 2018-03-23
# Python 3.6.4
'''
Write a program that generates a random list of letters.

# start with an
empty_list = [ ]
# and use
empty_list.append(Letter) # to add letters to the list

The length of the list of letters changes every time you run the program.
There can be a random number of X  letters on the list, where X is a random number 
between 50 to 75.
Each of the letters on the list is a random letter between A to F (uppercase).
Use a loop to generate the list and then Show the generated list of letters to the user.
Count and then show to the user how many times the letter B appears.
'''

from random import randint

letter_list = []
b_count = 0

for i in range(0, randint(50, 75), 1):
  ascii = randint(65, 70)
  letter_list.append(chr(ascii))
  if ascii == 66:
    b_count += 1

print("Made a list of {} letters:".format(len(letter_list)))
print(", ".join(letter_list))
print("The letter \"B\" appears {} times.".format(b_count))

'''
Made a list of 56 letters:
B, F, A, A, D, E, D, E, D, B, C, B, B, D, E, D, B, B, F, E, F, E, B, E,
F, B, D, F, D, A, E, F, C, B, F, F, B, C, D, B, D, A, E, F, B, E, D, C,
C, C, C, F, E, B, F, D
The letter "B" appears 13 times.

Made a list of 70 letters:
B, E, C, F, D, E, B, C, F, C, A, F, D, B, A, D, E, C, C, F, C, E, F, D,
F, A, C, B, E, B, F, A, A, B, E, F, D, C, B, A, B, E, B, F, A, E, B, E,
E, E, C, F, A, B, E, F, E, B, E, C, C, C, B, E, A, B, D, F, B, C
The letter "B" appears 15 times.

Made a list of 57 letters:
C, F, E, D, C, E, A, C, A, F, F, A, F, E, D, E, D, C, E, D, A, B, A, B,
C, B, F, E, A, B, D, A, F, C, F, E, A, D, E, A, A, D, A, A, F, B, C, F,
A, E, B, A, F, E, E, E, E
The letter "B" appears 6 times.
'''
