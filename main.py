
# Euro Conversion Rates as of 9/19/25i
# Written by Chase Dustin


import random
import math


us_dollar_value = 1.17


def convert():
    while True:
        try:
            number = float(input("Enter amount to convert: "))
            print(us_dollar_value * number)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number!") 
convert()