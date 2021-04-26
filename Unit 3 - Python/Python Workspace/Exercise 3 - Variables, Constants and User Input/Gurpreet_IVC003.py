"""
Filename:Gurpreet_IVC003.py
Author:Gurpreet Singh
Date:2019-05-28
Description:This program will tell the user the final cost of an item including all taxes.
"""
itemDescription=str(input("What is the description of your item?\n"))
priceItem=float(input("What is the price ($)of your item?\n"))
quantityItem=int(input("What is the quantity of the item?\n"))
GST=0.13
costItem=float(priceItem*quantityItem)
tax=float(costItem*GST)
totalCost=float(costItem+tax)
print("The total cost of the items is "+str(totalCost))
