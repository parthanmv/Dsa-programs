arr=[1,2,3,9,55,33,2,77,9,11,00,33,88,1,8,34,3,9,1,22,44,5,99,8] 
k=5
s=sum(arr[:k])
maxi=0
maxi=max(s,maxi)
j=0
for i in range(k,len(arr)):
    s-=arr[j]
    j+=1
    s+=arr[i]
    maxi=max(s,maxi)
print(maxi)