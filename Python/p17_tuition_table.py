# p17_tuition_table.py
# Brendan Knapp
# 2018-03-23
# Python 3.6.4
'''
Suppose that the tuition for a university is $10,000 this year 
and increases 5% every year.

Write a program that computes the tuition in ten years and displays
a table of the years and tuition costs.
'''

tuition = 10000
year = 1

for i in range(0, 10, 1):
  print("Year {:2d}    Tuition {:5.0f}".format(year, tuition))
  year += 1
  tuition = tuition + tuition * 0.05
  
'''
Year  1    Tuition 10000
Year  2    Tuition 10500
Year  3    Tuition 11025
Year  4    Tuition 11576
Year  5    Tuition 12155
Year  6    Tuition 12763
Year  7    Tuition 13401
Year  8    Tuition 14071
Year  9    Tuition 14775
Year 10    Tuition 15513
'''
