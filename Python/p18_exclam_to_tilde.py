# p18_exclam_to_tilde.py
# Brendan Knapp
# 2018-03-23
# Python 3.6.4
'''
Write a program that displays the characters in the ASCII character
table from ! to ~.

Display ten characters per line.

The characters are separated by exactly one space.

! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
'''

col_position = 0
ascii_dec_val = 33

while ascii_dec_val <= 126:
  print(chr(ascii_dec_val), end = " ")
  
  ascii_dec_val += 1
  col_position += 1
  
  if col_position % 10 == 0:
    print()

'''
! " # $ % & ' ( ) *
+ , - . / 0 1 2 3 4
5 6 7 8 9 : ; < = >
? @ A B C D E F G H
I J K L M N O P Q R
S T U V W X Y Z [ \
] ^ _ ` a b c d e f
g h i j k l m n o p
q r s t u v w x y z
{ | } ~
'''
  
  
