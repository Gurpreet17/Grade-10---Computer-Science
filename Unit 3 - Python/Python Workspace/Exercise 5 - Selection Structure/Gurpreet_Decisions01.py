"""
Filename:Gurpreet_Decisions01.py
Author:Gurpreet Singh.
Date:2019-05-31
Description: This program will prompt for user's age and tell the user if it is eligible to obtain it's driver license.
"""
age=int(input("How old are you?\n"))
if(age>=16):
    print ("You are eligible to get your license!")
if(age<16):
    print("You are not eligible to get your license wait "+ str(16-age)+" more years")

