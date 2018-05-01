# p29_to_upper.py
# Brendan Knapp
# 2018-04-05
# Python 3.6.4
'''
Write the definition of, and test the function toUpper which has a parameter
letter: toUpper(letter)

The function returns the upper case of a given letter if possible, and returns
"Not a Letter" if the argument is not a letter.
'''

def to_upper(letter):
  if ord(letter) not in range(97, 123):
    return("Not a Letter")
  else:
    letter = chr(ord(letter) - 32)
    return(letter)
    
print(to_upper("a"))
print(to_upper("z"))
print(to_upper("`"))
print(to_upper("!"))

'''
A
Z
Not a Letter
Not a Letter
'''
