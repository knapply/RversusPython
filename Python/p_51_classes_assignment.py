# p_51_classes_assignment.py
# Brendan Knapp
# 2018-04-30
# 
'''
1) Create a Date class.

1a) The class should have 3 properties (instance variables):

month
day
year
1b) The class should have 2 action (functions) :

setDate()  - allows the user to enter a date in 12/31/02 format 
showDate() - displays the date. 
2) Create an instance of the Date class.

3) Test the object's setDate() and showDate() methods.
'''

def get_length(some_vars):
  length = 0
  for each_var in some_vars:
    length += 1
  return(length)

class date:
  def __init__(self, date = "2018-05-05"):
    date = date.split("-")
    self.year = date[0]
    self.month = date[1]
    self.day = date[2]
    
  def set_date(self, new_date):
    new_date = new_date.split("/")
    self.month = new_date[0]
    self.day = new_date[1]
    self.year = new_date[2]
    
  def show_date(self, which = "all", **kwargs):
    if which == "all":
      val = "/".join([self.month, self.day, self.year])
    elif which == "month-year":
      val = "/".join([self.month, self.year])
    elif which == "month-day":
      val = "/".join([self.month, self.day])
    elif(which == "year"):
      val = self.year
    elif(which == "month"):
      val = self.month
    elif(which == "day"):
      val = self.day
    else:
      val = "invalid `which=` argument..."
    print(val, **kwargs)
    

my_date = date()
print("`my_date.show_date()` ->", end = " ")
my_date.show_date()

print('`my_date.set_date("12/31/02")` -> my_date.show_date()` ->', end = " ")
my_date.set_date("12/31/02")
my_date.show_date(end = "\n\n")

print("`date.show_date()` method using different `which=` arguments:")
print('my_date.show_date("month-year") ->', end = " ")
my_date.show_date("month-year")
print('my_date.show_date("month-day") ->', end = " ")
my_date.show_date("month-day")
print('my_date.show_date("year") ->', end = " ")
my_date.show_date("year")
print('my_date.show_date("month") ->', end = " ")
my_date.show_date("month")
print('my_date.show_date("day") ->', end = " ")
my_date.show_date("day")

'''
`my_date.show_date()` -> 05/05/2018
`my_date.set_date("12/31/02")` -> my_date.show_date()` -> 12/31/02

`date.show_date()` method using different `which=` arguments:
my_date.show_date("month-year") -> 12/02
my_date.show_date("month-day") -> 12/31
my_date.show_date("year") -> 02
my_date.show_date("month") -> 12
my_date.show_date("day") -> 31
'''
