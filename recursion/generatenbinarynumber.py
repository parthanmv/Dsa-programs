n=3
s="0"*n

ls=[]
def gen(i,s,n):
    if i==n:
        ls.append(s)
        return
    gen(i+1,s+"0",n)
    gen(i+1,s+"1",n)
gen(0,"",n)
print(ls)