a=int(input("enter the number "))
sums=0
for i in range(1,a):
    if a % i == 0:
       print(i)
       sums+=i
if sums == a:
    print(a,"is a perfect number",end=" ")
else:
    print("not perfect number")          
        