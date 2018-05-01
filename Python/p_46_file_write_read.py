# p_46_file_write_read.py
# Brendan Knapp
# 2018-04-30
'''
1) User enters a file name (such as "myMovies.txt").
2) User enters the titles of 4 of their favorite moveis (use a loop!).
3) Program Writes the 4 titles to a file, one per line,
   then closes the file (use a loop!).
4) Program Reads the 4 titles from "myMovies.txt" stores them
   in a list and shows the list
5) The program writes the titles in reverse order into a file "reverseOrder.txt"
6) Submit the 3 files (your "p43.py" program and the two files "myMoveis.txt"
   and "reverseOrder.txt")
'''

my_file = open("p_46_my_movies.txt", "w")

top_4_movies = []

for i in range(1, 5):
  top_4_movies.append(input("What's your {} st/nd/rd favorite movie? ".format(i)))

for j in top_4_movies:
  my_file.write(j + "\n")

my_file.close()

my_file_as_list = open("p_46_my_movies.txt", "r").read().splitlines()

print(my_file_as_list)

reverse_order_file = open("p_46_reverse_order_file.txt", "w")

for i in my_file_as_list[::-1]:
  reverse_order_file.write(i + "\n")
  
'''
What's your 1 st/nd/rd favorite movie?lord of the rings
What's your 2 st/nd/rd favorite movie?the iron giant
What's your 3 st/nd/rd favorite movie?zoolander
What's your 4 st/nd/rd favorite movie?cloud atlas
['lord of the rings', 'the iron giant', 'zoolander', 'cloud atlas']
'''

