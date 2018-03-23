# p11_rock_paper_scissors.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4
'''
Write a program to simulate rock-paper-scissors game.

Each players enters 'R', 'P', 'S' or 1, 2, 3 for Rock, Paper, Scissors.

The program then shows the winner on the basis of:
- Paper covers Rock
- Rock breack Scissors
- Scissors cut Paper
- Tie
'''

import random

p1 = random.randint(1,3)
p2 = random.randint(1,3)

rock = 1
paper = 2
scissors = 3

if p1 == rock and p2 == scissors:
  print("p1 wins, rock beats scissors")
elif p1 == scissors and p2 == paper:
  print("p1 wins, scissors beats paper")
elif p1 == paper and p2 == rock:
  print("p1 wins, paper beats rock")
if p2 == rock and p1 == scissors:
  print("p2 wins, rock beats scissors")
elif p2 == scissors and p1 == paper:
  print("p2 wins, scissors beats paper")
elif p2 == paper and p1 == rock:
  print("p2 wins, paper beats rock")
elif p1 == p2 and p1 == rock:
  print("tie, both have rock")
elif p1 == p2 and p1 == paper:
  print("tie, both have paper")
elif p1 == p2 and p1 == scissors:
  print("tie, both have scissors")

'''
just executing .py script from R
> purrr::walk(1:20, ~ system("python Python/p11_rock_paper_scissors.py"))

tie, both have rock
tie, both have scissors
p2 wins, paper beats rock
p2 wins, scissors beats paper
p2 wins, rock beats scissors
p1 wins, rock beats scissors
p1 wins, paper beats rock
tie, both have rock
tie, both have rock
p1 wins, scissors beats paper
p1 wins, rock beats scissors
tie, both have scissors
p1 wins, scissors beats paper
p1 wins, rock beats scissors
p1 wins, scissors beats paper
p2 wins, rock beats scissors
p2 wins, paper beats rock
p2 wins, paper beats rock
p1 wins, rock beats scissors
p1 wins, paper beats rock
'''



  
