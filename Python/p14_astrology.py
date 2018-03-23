# p14_astrology.py
# Brendan Knapp
# 2018-03-22
# Python 3.6.4
'''
Write a program that asks the user for day and month of a birthday.
The program then tells the Zodiac signs that will be compatible with 
that birthday.
'''
month = int(input("Enter month (as number) of birth: "))
day = int(input("Enter day of birth: "))

# -Aries		The Ram			Mar. 21–Apr. 19
if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("You are a Aries, the Ram, Fire group, compatible with Aries, Leo,"
          " Saggittarius")
# -Taurus		The Bull		Apr. 20–May 20
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("You are a Taurus, the Bull, Earth group, compatible with Taurus, "
          "Virgo, Capricorn")
# -Gemini		The Twins		May 21–June 21
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    print("You are a Gemini, the Twins, Air group, compatible with Gemini, "
          "Libra, Aquarius")
# -Cancer		The Crab		June 22–July 22
elif (month == 6 and day >= 22) or (month == 7 and day <=22):
    print("You are a Cancer, the Crab, Water group, compatible with Cancer, "
          "Scorpio, Pisces")
# -Leo		The Lion		July 23–Aug. 22
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("You are a Leo, the Lion, Fire group, compatible with Aries, "
          "Leo, Sagittarius")
# -Virgo		The Virgin		Aug. 23–Sept. 22
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("You are a Virgo, the Virgin, Earth group, compatible with Taurus, "
          "Virgo, Capricorn")
# -Libra		The Balance	        Sept. 23–Oct. 23
elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
    print("You are a Libra, the Balance, Air group, compatible with Gemini, "
          "Libra, Aquarius")
# -Scorpio	The Scorpion	        Oct. 24–Nov. 21
elif (month == 10 and day >= 24) or (month == 11 and day <= 21):
    print("You are a Scorpio, the Scorpion, Water group, compatible with "
          "Cancer, Scorpio, Pisces")
# -Sagittarius	The Archer		Nov. 22–Dec. 21
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("You are a Sagittaruius, the Archer, Fire group, compatible with"
          " Aries, Leo, Sagittarius")
# -Capricorn	The Goat		Dec. 22–Jan. 19
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("You are a Capricorn, the Goat, Earth group, compatible with "
          "Taurus, Virgo, Capricorn")
# -Aquarius	The Water Bearer        Jan. 20–Feb. 18
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("You are a Aquarius, the Water Bearer, Air group, compatible with "
          "Gemini, Libra, Aquarius")
# -Pisces		The Fishes	        Feb. 19–Mar. 20
elif (month == 2 and day >= 19) or (month == 3 and day <=20):
    print("You are a Pisces, the Fishes, Water group, compatible with Cancer, "
          "Scorpio, Pisces")
          
'''
Enter month (as number) of birth: 3
Enter day of birth: 22
You are a Aries, the Ram, Fire group, compatible with Aries, Leo, Saggittarius

Enter month (as number) of birth: 6
Enter day of birth: 30
You are a Cancer, the Crab, Water group, compatible with Cancer, Scorpio, Pisces

Enter month (as number) of birth: 10
Enter day of birth: 24
You are a Scorpio, the Scorpion, Water group, compatible with Cancer, Scorpio, Pisces
'''

