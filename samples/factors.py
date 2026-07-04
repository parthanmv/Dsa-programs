#factors counting
def divisor(n):
    i=1
    for i in range(i,n+1):
        if n%i==0:
           print(i)
def factors(n):
      count=0
      i=1
      while i*i <= n:
          if n%i==0:
              if i==n//i:
                 count+=1
              else:
                  count+=2
          i+=1
      return count
n=int(input("enter the number"))
k=int(input("1.count factors 2.print all divisors"))
if k==1:
  print(factors(n)) 
elif k==2:
  divisor(n)
else:
    print("fault")