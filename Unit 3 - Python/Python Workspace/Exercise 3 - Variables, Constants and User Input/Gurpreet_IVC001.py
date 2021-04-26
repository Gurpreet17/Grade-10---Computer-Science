"""
Filanme: Gurpreet_IVC001.py
Author: Gurpreet Singh
Date: 2019-05-26
Description: This program ask user for two prices of items and then a discount as a percentage. This program will calculate the overall cost o both items after the HST of 13%
"""
item1=float(input("What is the price of your first item?""\n"))#the price of the first item.
item2=float(input("What is the price of your second item?""\n"))#the price of the second item.
discount=float(input("What is the discount on these two items?""\n"))#the discount (%) on the two items.
HST=float(0.13)#The tax that is put on the items after discount
cost=float(item1+item2)
costafterdiscount=float(cost*discount)
tax=float(costafterdiscount*HST)
totalcost=(float(costafterdiscount+tax))
print("The total cost of the two items is "+str (totalcost))





                
