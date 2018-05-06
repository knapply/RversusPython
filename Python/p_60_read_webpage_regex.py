# p_60_read_webpage_regex.py
# Brendan Knapp
# 2018-05-06
'''
# readAWebPage.py
# Write a Python program which:
# Connects to a URL "http://www.gavilan.edu/dir/" (see examplesPageRead.py)
# WRITES all the html into a text file (dataFile.txt) as a string, 
# Searches the text file and makes a listOfEmails, (see regexExamples.py)
# Makes a nonRepeatListOfEmails
# Writes those emails to a text file (emails.txt), one per line "Email # : someone@gavilan.edu"
# Close the above file
# Reopen the above file to READ and search it for 'stoykov' (see examplesPageRead.py)
# Print the line where you found that email
# NOTE: see examplesPageRead.py for file Input and Output
'''

# readAWebPage.py
# Write a Python program which:

import urllib.request
import re
# Connects to a URL "http://www.gavilan.edu/dir/"
url = urllib.request.urlopen("http://www.gavilan.edu/dir/")
html_str = str(url.read())
# WRITES all the html into a text file (data_file.txt) as a string
my_file = open("data_file.txt", "w")
my_file.write(html_str)
my_file.close()
my_file = open("data_file.txt", "r")
## read data_file.txt, fix an invalid email (srmcginnis@gavilan.ed@gavilan.edu)
contents = re.sub("rmcginnis@gavilan\.ed@gavilan\.edu", "rmcginnis@gavilan.edu", 
                   str(my_file.read()))
## email regex
email_regex = "[A-z0-9_.+-]+@[A-z0-9-]+\.[A-z]{3}"
## email_regex = "(?<=mailto:)([A-z0-9_.+-]+@[A-z0-9-]+\.[A-z]{3})"
'''
"(?<=mailto:)([A-z0-9_.+-]+@[A-z0-9-]+\.[A-z]{3})" may be better based on the task,
but the example included webmaster@gavilan.edu from the page's author metadata
'''
# Searches the text file and makes a listOfEmails
list_of_emails = []
listOfEmails = re.findall(email_regex, contents)
for match in listOfEmails:
  if match not in list_of_emails:
    list_of_emails.append(match)

# close data_file.txt
my_file.close()

# Writes those emails to a text file (emails.txt), one per line 
## open emails.txt
my_file = open("emails.txt", "w")
## write contents
count = 0
for i in list_of_emails:
  i = "Email #{:3}: {}\n".format(count, i)
  my_file.write(i)
  count += 1
# Close the above file
my_file.close()

# Reopen the above file to READ and search it for 'stoykov'
## read emails.txt, coerce list elements to strings
emails = list(map(str, open("emails.txt").readlines()))
stoykov_line = [email for email in emails if re.search("stoykov", email)][0]
stoykov_index = int(re.search("\d+", stoykov_line)[0])

# Print the line where you found that email
print("Line where email found: {}".format(emails[stoykov_index]))

'''
Line where email found: Email #424: astoykov@gavilan.edu

================
Double check:
- R's index starts at 1, but webmaster@gavilan.edu is skipped as only the table is read:
```
library(tidyverse)                      # data carpentry suite
library(rvest)                          # essentially R's version of BeautifulSoup

target_url <- "http://www.gavilan.edu/dir/"

emails_df <- target_url %>% 
  read_html() %>%                       # read page's html
  html_nodes("#perDir") %>%             # grab table nodes with css
  html_table(fill = TRUE) %>%           # parse table
  as.data.frame() %>%                   # convert to data.frame
  select(-X1) %>%                       # drop first "column" (faculty pages)
  set_names(slice(., 1)) %>%            # first row as column headers
  slice(2:nrow(.)) %>%                  # drop first row, convert to modern tibble data frame
  mutate(Email = na_if(Email, "")) %>%  # empty Email strings as NA
  drop_na() %>%                         # drop NA Emails
  distinct(Email)                       # keep only unique Emails

emails_df                               # resulting 1 column data frame

# # A tibble: 486 x 1                   # correct number of rows
#    Email                 
#    <chr>                 
#  1 mabbass@gavilan.edu   
#  2 dachterman@gavilan.edu
#  3 sadams@gavilan.edu    
#  4 aadamson@gavilan.edu  
#  5 nadham@gavilan.edu    
#  6 jadkins@gavilan.edu   
#  7 pagaliotis@gavilan.edu
#  8 tahlin@gavilan.edu    
#  9 makrop@gavilan.edu    
# 10 jalamdari@gavilan.edu 
# # ... with 476 more rows

emails_df %>% 
  mutate(index = row_number()) %>%       # add index column 
  filter(str_detect(Email, "stoykov"))   # regex match "stoykov" in Email column
  
# # A tibble: 1 x 2                      # result 1 row data frame
#   Email                index
#   <chr>                <int>
# 1 astoykov@gavilan.edu   424           # correct index
```
'''








