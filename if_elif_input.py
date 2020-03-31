#!/usr/bin/python
num=raw_input("Guess your number:")
if int(num) > 5:
   print ("Number is bigger than 5", num)
   if int(num) >=15:
    print ("Number is greater than 15 ", num)
   elif int(num) < 15:
    print ("Number is smaller than 15 and the number is:", num)
elif int(num) < 5:
    print ("Number is less than 5", num)

   

