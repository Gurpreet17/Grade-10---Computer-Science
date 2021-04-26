"""
Filename: Gurpreet Singh
Author: Gurpreet Singh
Date: 20019-23-05
Description: This program calculates the surface area and the volume of a box
"""
l=int(input("What is the lenght of the box"))
w=int(input("What is the width of the box"))
h=int(input("What is the height of the box"))
a= str (2*(w*l)+2*(l*h)+2*(h*w))
print ("The surface area of the box is",str(a)) 
v=str(l*w*h)
print ("The volume of the box is",str(v))
