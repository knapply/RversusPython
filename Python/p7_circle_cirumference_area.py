# p7_circle_cirumference_area.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4

pi = 3.1415

radius = float(input("Please enter the radius: "))

area = pi * (radius**2)
circumference = 2 * pi * radius

print("A circle with radius %.1f inches has" %radius)
print("circumference: %.1f inches" %circumference)
print("area: %.1f sq. inches" %area)

'''
$ python p7_circle_cirumference_area.py
Please enter the radius: 12
A circle with radius 12.0 inches has
circumference: 75.4 inches
area: 452.4 sq. inches
'''
