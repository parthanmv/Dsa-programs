s=["j","k","t","o"]
n=[]*len(s)
i=0
n=len(s)//2
j=len(s)-1
while i < n and  j >n :
    s[i],s[j]=s[j],s[i]
    i+=1 
    j-=1
print(s)