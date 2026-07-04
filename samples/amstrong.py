n=int(input())
x=n
f=n
rev = 0
count = 0
sum=0
while n > 0:
    rev=n%10
    count+=1
    n=n//10
while f > 0:
    rev=f%10
    sum+=rev**count
    f=f//10
print(sum)
print(x==sum)

