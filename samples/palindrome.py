x=int(input())
rev=0
n = x
while  x > 0 :
  rev = rev*10 + x % 10 
  x = x // 10 
print( n == rev)