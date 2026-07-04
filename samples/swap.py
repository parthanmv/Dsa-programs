'''a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print( "a=",a ,end=" " )
print("b= ",b ,end=" ")  '''

a=int(input())
b=int(input())

a,b=b,a
print( "a=",a ,end=" " )
print("b= ",b ,end=" ")  