"""
Filename:Gurpreet_Decisions03.py
Author:Gurpreet Singh.
Date:2019-06-03
Description:This program ask the user for the page count, line count, and page length.and if the variable line count is greater than page length it will add 1 to page.count.
"""
pageCount=int(input("What is the page count?"))
lineCount=int(input("What is the line count?"))
pageLength=int(input("What is the page length?"))
if (lineCount>pageLength):
    print(1+pageCount)
else:
    print (pageCount)


    


               
                
