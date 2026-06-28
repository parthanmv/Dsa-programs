n=int(input())
rev=0
c=0
sum=0
m=n
x=n
while n > 0:
    c=c+1
    n=n//10
while m > 0:
    k=m%10
    sum=sum+k**c
    m=m//10
if sum == x :
  print ("amstrong ")
else:
    print("not") 
    

