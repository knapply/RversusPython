# p24_longest_shortest_words.py
# Brendan Knapp
# 2018-03-23
# Python 3.6.4
'''
Ask the user to enter a sentence, your program reads the sentence, and then show
the user the longest and shortest words, like so:

Sample Program Run:
Please enter a sentence: One three do ten
Longest word is: "three" , it has 5 letters.
The shortest word is: "do", it has 2 letters.
'''

words = input("Please enter a sentence: ").split()

def get_max(words):
  max_char_count = 0
  for word in words:
    word_length = len(word)
    if word_length > max_char_count:
      max_char_count = word_length
  return(max_char_count)
      
def get_min(words):
  min_char_count = len(words[0])
  for word in words:
    word_length = len(word)
    if word_length < min_char_count:
      min_char_count = word_length
  return(min_char_count)

longest = [word for word in words if len(word) == get_max(words)][0]
shortest = [word for word in words if len(word) == get_min(words)][0]

print("Longest word is: \"{}\". It has {} letters.".format(longest, len(longest)))
print("Shortest word is: \"{}\". It has {} letters.".format(shortest, len(shortest)))

'''
Please enter a sentence: One three do ten
Longest word is: "three". It has 5 letters.
Shortest word is: "do". It has 2 letters.

Please enter a sentence: changing languages is like having your wings clipped
Longest word is: "languages". It has 9 letters.
Shortest word is: "is". It has 2 letters.
'''
