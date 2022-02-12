#WAP in python in which user guessed a number and  unil the guessed number is correct 
# program will be keep on asking  for the number

import random

b=random.randint(1,9)
a=int(input("Enter a number between 1-9 :"))

if(a==b):
   print("Guessed Correct") 

else:  
   while(a!=b):
     c=int(input("Enter number again"))
     if(c==b):
          print("Guessed Correct")
          break

