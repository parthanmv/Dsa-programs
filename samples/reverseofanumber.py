def reverse(x):
       sign= -1 if x < 0 else 1
       rev=0
       n=abs(x)
       while  n > 0 :
           rev = rev*10 + n % 10 
           n = n // 10 
       if -2**31 <= rev <= 2**31-1:
            return sign*rev
       else:
            return 0
         
n=int(input())
print(reverse(n))

    
   