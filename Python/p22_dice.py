# p22_dice.py
# Brendan Knapp
# 2018-03-23
# Python 3.6.4
'''
Write a Dice Game program that generates two random numbers between 1 - 6 
that would result in an output like this:

Beat the computer!
You rolled a 2 and a 1 (total =  3)
Do you want to keep those? (y or n)
n

Rolling again....
You rolled a 4 and a 1 (total =  5)
Do you want to keep those? (y or n)
n

Rolling again....
You rolled a 1 and a 1 (total =  2)
Do you want to keep those? (y or n)
y

The computer rolled 6 and 3 (total = 9)

So sorry. You lose.
'''

import random

def sum_score(rolls):
  summed = 0
  for dice in rolls:
    summed += dice
  return(summed)

def roll():
  keep = "n"
  
  while keep == "n":
    rolls = [random.randint(1, 6), random.randint(1, 6)]
    print("You rolled {} and {} (total = {})".format(rolls[0], rolls[1], sum_score(rolls)))
    keep = input("Do you want to keep those? (y or n) ")
    if keep == "n":
      print("Rolling again...")
  
  return(rolls)
  
def play(player_rolls):
  computer_rolls = [random.randint(1, 6), random.randint(1, 6)]
  
  if sum_score(player_rolls) > sum_score(computer_rolls):
    winner = "player"
    result_message = "Beat the computer!"
    scores = [player_rolls[0], player_rolls[1], sum_score(player_rolls)]
  elif sum_score(player_rolls) < sum_score(computer_rolls):
    result_message = "So sorry. You lose."
    winner = "computer"
    scores = [computer_rolls[0], computer_rolls[1], sum_score(computer_rolls)]
  elif sum_score(player_rolls) == sum_score(computer_rolls):
    result_message = "It's a tie."
    winner = "none"
    scores = sum_score(player_rolls)
  
  print()  
  print(result_message)

  if winner == "player":
    print("You rolled a {} and a {} (total = {})".format(scores[0], scores[1], scores[2]))
  elif winner == "computer":
    print("The computer rolled {} and {} (total = {})".format(scores[0], scores[1], scores[2]))
  elif winner == "none":
    print("Both rolled a total of {}".format(scores))

  
play(roll())
  
'''
You rolled 3 and 2 (total = 5)
Do you want to keep those? (y or n) n
Rolling again...
You rolled 6 and 2 (total = 8)
Do you want to keep those? (y or n) n
Rolling again...
You rolled 4 and 6 (total = 10)
Do you want to keep those? (y or n) y

Beat the computer!
You rolled a 4 and a 6 (total = 10)



You rolled 1 and 6 (total = 7)
Do you want to keep those? (y or n) y

So sorry. You lose.
The computer rolled 6 and 4 (total = 10)


You rolled 5 and 4 (total = 9)
Do you want to keep those? (y or n) y

It's a tie.
Both rolled a total of 9
'''





