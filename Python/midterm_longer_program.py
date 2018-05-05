# midterm_longer_program.py
# Brendan Knapp
# 2018-05-08
'''
Write a program that lets the user enter 4 sides and 4 angles.
The program checks if the type of quadrilateral is either: 
- Rhombus
- Square
- Rectangle
'''

# utils
def get_length(a_list):
  length = 0
  for i in a_list:
    length += 1
  return(length)
  
def is_positive(value):
  result = True if value > 0 else False
  return(result)
  
def all_are(values):
  false_list = []
  for i in values:
    if not i:
      false_list.append(i)
  result = True if get_length(false_list) == 0 else False
  return(result)
    
def all_equal(values):
  vals = []
  for val in values:
    if not val in vals:
      vals.append(val)
  if get_length(vals) > 1:
    return(False)
  else:
    return(True)

def is_rhombus(sides, angles):
  all_sides_are_equal = all_equal(sides)
  is_90_degrees = []
  for angle in angles:
    if angle == 90:
      is_90_degrees.append(angle)
  no_90_degree_angles = True if get_length(is_90_degrees) == 0 else False
  angle1_equals_angle3 = True if angles[0] == angles[2] else False
  angle2_equals_angle4 = True if angles[1] == angles[3] else False
  return(all_are([all_sides_are_equal, no_90_degree_angles,
                 angle1_equals_angle3, angle2_equals_angle4]))
  
def is_square(sides, angles):
  all_sides_are_equal = all_equal(sides)
  all_angles_are_equal = all_equal(angles)
  return(all_are([all_sides_are_equal, all_angles_are_equal]))
  
def is_rectangle(sides, angles):
  side1_equals_side3 = True if sides[0] == sides[2] else False
  side2_equals_side4 = True if sides[1] == sides[3] else False
  all_angles_are_equal = all_equal(angles)
  return(all_are([side1_equals_side3, side2_equals_side4, all_angles_are_equal]))
  
def get_val(i, which):
  inputted = float(input("Please enter {} #{}: ".format(which[:-1], i + 1)))
  if not is_positive(inputted):
      print("Value must be positive!", end = " ")
      get_val(i, which)
  return(inputted)
    
def get_4_values(which):
  print("=== Please enter {} ===".format(which.upper()))
  vals = []
  for i in range(0, 4, 1):
    inputted = get_val(i, which)
    vals.append(inputted)
  print()
  return(vals)

# def get_input(which):
#   values = get_4_values(which)
#   return(values)
  # raw = get_4_values(which)
  # if not length_is_valid(raw):
  #   print("You inputted {} value(s) instead of 4.".format(get_length(raw)))
  #   retry = input("Would you like to try again? (y/n) ")
  #   if retry == "y":
  #     return(get_input(which))
  #   else:
  #     quit()
  # else:
  #   try:
  #     values = list(map(float, raw))
  #   except:
  #     print("Your {} aren't numbers.".format(which))
  #     retry = input("Would you like to try again? (y/n) ")
  #     if retry == "y":
  #       return(get_input(which))
  #     else:
  #       quit()
  # 
  # if not all_positive(values):
  #   neg = [val for val in values if not is_positive(val)][0]
  #   print("{} is not a positive value...".format(neg))
  #   retry = input("Would you like to try again? (y/n) ")
  #   if retry == "y":
  #     get_input(which = which)
  #   else:
  #     quit()
  # else:
  #   return(values)

# main
def get_shape():
  sides = get_4_values("sides")
  angles = get_4_values("angles")
  
  if is_square(sides, angles):
    print("This is a SQUARE!")
  
  elif is_rectangle(sides, angles):
    print("This is a RECTANGLE!")
  
  elif is_rhombus(sides, angles):
    print("This is a RHOMBUS!")
    
  repeat = int(input("Would you like to repeat? (1-Yes, 2-No): "))
  if repeat == 1:
    get_shape()

# run
get_shape()


    

