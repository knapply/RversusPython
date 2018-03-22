# p4_print_C_any_letter.R
# Brendan Knapp
# 2018-03-06
# R 3.4.3
# Description: Write a program that asks for a character INPUT from the 
#              keyboard and then OUTPUTS a large block letter "C" 
#              composed of that character.

x <- readline("Enter a letter: ")

print("************************************************")
print("")
print(sprintf("            %s %s %s", x, x, x))
print(sprintf("          %s       %s", x, x))
print(sprintf("         %s", x))
print(sprintf("        %s", x))
print(sprintf("        %s", x))
print(sprintf("        %s", x))
print(sprintf("         %s", x))
print(sprintf("          %s       %s", x, x))
print(sprintf("            %s %s %s", x, x, x))
print("")
print("**************************************************")
print("    Computer Science is Cool Stuff!!")

# Run:
# > source('~/RversusPython/R/p4_print_CS_any_letter.R')
# Enter a letter: B
# [1] "************************************************"
# [1] ""
# [1] "            B B B"
# [1] "          B       B"
# [1] "         B"
# [1] "        B"
# [1] "        B"
# [1] "        B"
# [1] "         B"
# [1] "          B       B"
# [1] "            B B B"
# [1] ""
# [1] "**************************************************"
# [1] "    Computer Science is Cool Stuff!!"
