# p_36_codingbat_strings.py
# Brendan Knapp
# 2018-05-05
# 
'''
Solutions to some codingbat.com exercises
'''

# Warmup-2 > string_times http://codingbat.com/prob/p193507
def string_times(str, n):
  string = str * n
  return(string)

# String-1 > extra_end http://codingbat.com/prob/p148853
def extra_end(str):
  new_string = str[-2:] * 3
  return(new_string)

# String-1 > make_tags http://codingbat.com/prob/p132290
def make_tags(tag, word):
  new_tag = "".join(["<", tag, ">", word, "</", tag, ">"])
  return(new_tag)

# String-1 > combo_string
def get_length(some_vars):
  length = 0
  for each_var in some_vars:
    length += 1
  return(length)

def combo_string(a, b):
  short = a if get_length(a) < get_length(b) else b
  long = a if get_length(a) > get_length(b) else b
  new_string = "".join([short, long, short])
  return(new_string)
  
# String-2 > count_code http://codingbat.com/prob/p186048
def get_length(some_vars):
  length = 0
  for each_var in some_vars:
    length += 1
  return(length)
  
def count_code(str):
  count = 0
  for i in range(0, get_length(str)-3):
    if str[i:i + 2] == "co" and str[i + 3] == "e":
      count += 1
  return(count)

# String-2 > xyz_there http://codingbat.com/prob/p149391
def get_length(some_vars):
  length = 0
  for each_var in some_vars:
    length += 1
  return(length)
  
def xyz_there(str):
  checks = []
  for i in range(0, get_length(str)-2):
    check = True if str[i:i + 3] == "xyz" and str[i - 1] != "." else False
    checks.append(check)
  result = True if True in checks else False  
  return(result)
