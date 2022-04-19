l=['@','#','$']
import random
t=int(input())
C=0
for i in range(t):

       
       def rr(l, n):
           r = []
        
           # Will add values from n to the new list
           for i in range(len(l) - n, len(l)):
               r.append(l[i])
        
           # Will add the values before
           # n to the end of new list
           for i in range(0, len(l) - n):
               r.append(l[i])
        
           return r

       for i in range(3):
           n=random.randint(1,3)
           if(i==0):
               a=rr(l,n)
           elif(i==1):
               b=rr(l,n)
           else:
               c=rr(l,n)
       print(a)
       print(b)
       print(c)
       print("\n")
       if(a[1]==b[1] and b[1]==c[1]):
           C=C+1
       
if(C>=1):
    print("JACKPOT!!!")
else:
    print("YOU R BROKE!!!!")



 






    


  
   