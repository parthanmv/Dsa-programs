
#factorial without recursion
''''n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is",fact)'''


#factorial using recursion5


def facto():
    global fact,i
    if i < n+1:
       fact=fact*i
       i=i+1
       facto()
n=int(input("Enter a number: "))
fact=1
i=1  
facto()

printer=lambda fact:print("factorial:=",fact,end="")
printer(fact)
    