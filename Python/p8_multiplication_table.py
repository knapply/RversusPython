# p8_multiplication_table.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4
'''
Write a program to print a multiplication table for float values  0.1, 0.2 and
0.3. Output should use the placeholder (%) to control column widths.
'''

print("     0.1     0.2     0.3")
print("0.1  %.2f    %.2f    %.2f" %(0.1 * 0.1, 0.1 * 0.2, 0.1 * 0.3))
print("0.2  %.2f    %.2f    %.2f" %(0.2 * 0.1, 0.2 * 0.2, 0.2 * 0.3))
print("0.3  %.2f    %.2f    %.2f" %(0.3 * 0.1, 0.3 * 0.2, 0.3 * 0.3))

'''
$ python p8_multiplication_table.py
     0.1     0.2     0.3
0.1  0.01    0.02    0.03
0.2  0.02    0.04    0.06
0.3  0.03    0.06    0.09
'''
