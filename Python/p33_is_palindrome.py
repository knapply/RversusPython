# p33_is_palindrome.py
# Brendan Knapp
# 2018-04-05
# Python 3.6.4
'''
Write a function named isPalindrome that takes a word W and returns 
true if W is a palindrom.
'''

def is_palindrome(W):
  if W == W[::-1]:
    return True
  else:
    return False
    
print ("civic is a palindrome: ", is_palindrome("civic"))
print ("car is a palindrome: ", is_palindrome("car"))
print ("racecar is a palindrome: ", is_palindrome("racecar"))
print ("firetruck is a palindrome: ", is_palindrome("firetruck"))

'''
civic is a palindrome:  True
car is a palindrome:  False
racecar is a palindrome:  True
firetruck is a palindrome:  False
'''
