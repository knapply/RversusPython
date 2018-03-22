# p5_sum_product.R
# Brendan Knapp
# 2018-03-06
# R 3.4.3
# Description: Write a program which computes the sum and 
#              product of two numbers entered by the user.

num_1 <- as.numeric(readline("Enter the first number: "))

num_2 <- as.numeric(readline("Enter the second number: "))

sum <- num_1 + num_2

product <- num_1 * num_2

print(sprintf("The sum of %i and %i is %i.", num_1, num_2, sum))
print(sprintf("The product of %i and %i is %i.", num_1, num_2, product))

# > source('~/RversusPython/R/p5_sum_product.R')
# Enter the first number: 5
# Enter the second number: 6
# [1] "The sum of 5 and 6 is 11."
# [1] "The product of 5 and 6 is 30."