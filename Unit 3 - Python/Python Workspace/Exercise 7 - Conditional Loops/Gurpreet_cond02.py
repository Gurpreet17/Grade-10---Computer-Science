"""
Filename:Gurpreet_cond02.py
Author:Gurpreet Singh
Date:2019-05-05
Description: Thus program prints the statement "I am so samrt!" and prompts the user weather they want to continue seeing that statement.
"""
print ("I am so smart!")
x=input(str("Do you wish to continue?"))
while x==("no"):
    break
y=1
while x==("yes"):
    y=y+1
    print (y)
    print ("I am so smart!")
    x=input(str("Do you wish to continue?"))
