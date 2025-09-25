
# Euro Conversion Rates as of 9/19/25
# Written by Chase Dustin


import random
import math



def welcome_message():
    print("Welcome to the CurrencyConverter!\n"
          "Please choose a currency to convert: ")
    print("1. $ U.S. Dollar(USD) $")
    print("2. € EU Euro(EUR) €")
    print("3. ¥ Japanese Yen(JPY) ¥")
    print("4. £ British Pound Sterling(GBP) £")
    print("5. $ Australian Dollar(AUD) $")
    print("6. ")
    


def convert():
    while True:
        try:
            number = float(input("Enter amount to convert: "))
            print(us_dollar_value * number)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number!") 
convert()