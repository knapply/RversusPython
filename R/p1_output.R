# p1_output.R
# Brendan Knapp
# 2018-03-06
# R 3.4.3
# Description: Program to show output in R

# 1) Convert output.py to an output.R program

# R assumes interactive use, so in order to duplicate Python behavior,
# be sure you `source()` the script
# Since R is often used interactively, we typically don't need to `print()` explicitly,
# but we'll play along. R's `print()` includes quotes for strings by default, but
# we can omit them by just using `print.noquote()`

print.noquote('hello world')        # single quote
print.noquote("hello world")        # double quote
cat("he\nllo")       # \n insert a new line (same as pressing Enter)
                     # R's `cat()` concatenates an object before printing
                       # it performs less conversion than R's `print()`

my_name <- "Brendan"          # declare/initialize character(pronounced string :| variable `my_name`
weight <- 250.34152           # declare/initialize numeric/double variable `weight`
                               # by default, R initializes numbers as doubles/numerics

age <- 30L                    # declare/initialize integer variable `age`
                               # in R, we have to explicitly denote integers by ending
                                # them with `L` 
                                 # we can also use `as.integer()`
grades <- c(90, 77, 88)       # in R, we can `c()`ombine objects of the same type into vectors
                               # but we can also use `list()` to combine all kinds of objects
nameZ <- c("Brendan", "Knapp")

cat("\n")                       # just to skip a line
print.noquote(paste("Hello", my_name))  # `paste()` before `print()`ing multiple objects
print.noquote(paste("Your weight is", weight, "and your age is", age))
print.noquote(paste("Your weight is", weight, "and your age is", age))
print.noquote(paste("Lists: grades =", grades, "nameZ =", nameZ))
cat("This is how your print ")
cat("on the same line")

# Output:
# > source('~/hapPywoRld/R/p1_output.R')
# [1] hello world
# [1] hello world
# he
# llo
# [1] Hello Brendan
# [1] Your weight is 250.34152 and your age is 30
# [1] Your weight is 250.34152 and your age is 30
# [1] Lists: grades = 90 nameZ = Brendan
# [2] Lists: grades = 77 nameZ = Knapp  
# [3] Lists: grades = 88 nameZ = Brendan
# This is how your print on the same line


