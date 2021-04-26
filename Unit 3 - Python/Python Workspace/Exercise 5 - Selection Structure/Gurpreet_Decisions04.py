"""
Filename:Gurpreet_Decisions04.py
Author:Gurpreet Singh.
Date:2019-06-03
Description: This program will prompt the user for price of the meal and calculate the total rpice including HST.
"""
price=int(input("Enter the price of your meal:\n"))
print ("Subtotal: $"+str(price))
HST=0.13
tax=(price*HST)
print ("Total taxes: $"+str(tax))
total=(price+tax)
print ("Total: $"+str (total))

          

