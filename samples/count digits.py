def counter(n):
   count=0
   while n > 0:
       n % 10
       count+=1
       n=n//10
   return count     

n=int(input())
c=counter(n)
print("count=",c,end="")  
