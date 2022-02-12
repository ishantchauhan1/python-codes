#*
#**
#***
#**
#*

a=int(input("Enter number of rows"))
    
for i in range(a+1):
    for j in range(i):
        print("*", end =' ')
    print()    


    
for i in range(a+1,0,-1):
    for j in range(0,i):
      print("*",end=' ')
    print()
    
