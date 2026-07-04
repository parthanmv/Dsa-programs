n=int(input())
prev=0
curr=1
def fibo(prev,curr,i):
     if(i > n):
        return prev
     next=prev+curr
     prev=curr
     curr=next
     return fibo(prev,curr,i+1)
return fibo(prev,curr,1)    