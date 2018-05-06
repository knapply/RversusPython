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
  if ord(letter) in range(65, 91):
    return(letter)
  elif ord(letter) in range(97, 123):
    return(chr(ord(letter) - 32))
  else:
    return("Not a Letter")
    
print(to_upper("a"))
print(to_upper("A"))
print(to_upper("z"))
print(to_upper("Z"))
print(to_upper("5"))
print(to_upper(")"))
print(to_upper("`"))

'''
A
A
Z
Z
Not a Letter
Not a Letter
Not a Letter
'''
