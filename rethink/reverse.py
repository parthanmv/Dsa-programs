n=int(input())
rev=0
while n > 0:
    rev=rev*10+n%10
    print(rev)
    n=n//10
print(rev)


