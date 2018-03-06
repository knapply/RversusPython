# p4_print_C_any_letter.py
# Brendan Knapp
# 2018-03-06
# Python 3.6.4
# Description: Write a program that asks for a character INPUT from the 
#              keyboard and then OUTPUTS a large block letter "C" 
#              composed of that character.

x = input("Enter a letter: ")

print("************************************************")
print("")
print("            %s %s %s" %(x, x, x))
print("          %s       %s" %(x, x))
print("         %s" %x)
print("        %s" %x)
print("        %s" %x)
print("        %s" %x)
print("         %s" %x)
print("          %s       %s" %(x, x))
print("            %s %s %s" %(x, x, x))
print("")
print("**************************************************")
print("    Computer Science is Cool Stuff!!")

'''
Run:
$ python Python/p4_print_CS_any_letter.py
Enter a letter: B
************************************************

            B B B
          B       B
         B
        B
        B
        B
         B
          B       B
            B B B

**************************************************
    Computer Science is Cool Stuff!!
'''


