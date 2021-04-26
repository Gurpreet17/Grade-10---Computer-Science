""""
Filename:Gurpreet_cond03.py
Author:Gurpreet Singh
Date:2019-05-04
Description:This program asks the user for the login password and student number in order to login.
"""
LOGIN=("897163")
PASSWORD=("06172003")
login=int(input("Login:\n"))
password=int(input("Password:\n"))
if LOGIN==login and PASSWORD==password:
    print ("Login Successful")
a=1
while LOGIN!=login or PASSWORD!=password:
    print ("Login Unsuccessful. Try Again")
    a=a+1
    login=int(input("Login:\n"))
    password=int(input("Password:\n"))
    if a==3:
        break

    
    
    



    
