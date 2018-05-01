# p30_is_letter.py
# Brendan Knapp
# 2018-04-05
# Python 3.6.4
'''
Write a function named isLetter that has a parameter C. 
isLetter returns true if the argument is an upper or lower case letter.
'''

def is_letter(C):
  if ord(C) in range(65, 91) or ord(C) in range(97, 123):
    return True
  else:
    return False

print("A is a letter: ", is_letter("A"))
print("Z is a letter: ", is_letter("Z"))
print("@ is a letter: ", is_letter("@"))
print("[ is a letter: ", is_letter("["))

'''
A is a letter:  True
Z is a letter:  True
@ is a letter:  False
[ is a letter:  False
'''
