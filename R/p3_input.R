# p3_input.R
# Brendan Knapp
# 2018-03-06
# R 3.4.3

name <- readline("Please enter your name: ")
weight_lbs <- as.numeric(readline("Please enter your weight in lbs: "))
age <- as.integer(readline("Please enter your age (whole number): "))
weight_kg <- weight_lbs * 0.453592
title <- "Human"

cat(paste("Hello", title, name, "Your weight is\n"))
cat(paste(weight_lbs), "lbs\n")
cat(paste("which equals =", weight_kg))
cat(" kilograms")

# Output:
# > source('~/RversusPython/R/p3_input.R')
# Please enter your name: Brendan
# Please enter your weight in lbs: 560
# Please enter your age (whole number): 12
# Hello Human Brendan Your weight is
# 560 lbs
# which equals = 254.01152 kilograms