'''num=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,4,5,6,7,8,9,8,7,6]
m=[9,8,7,6,5,4,3,2,1,10]

hash=[0]*11
for i in num:
    hash[i]+=1

for i in m:
    if i < 1 or i > 10:
        print(i,":",0)
    else:
        print(i,":",hash[i])'''
        
        #using dictionary
'''num=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,4,5,6,7,8,9,8,7,6]
hash={}


for i in  range(len(num)):
    hash[num[i]]=hash.get(num[i],0)+1 
print(hash)

for i in m:
    if  0 <i<10 :
        print(i,  hash.get(i,0))
    else:
        print(i, 0)
'''

s="azyuyyzaaaa"
q=["d","a","y","u"]
ls=[]
ls=s
hash={}
for i in range(len(ls)):
   hash[ls[i]]=hash.get(ls[i],0)+1
print(hash)

for i in q:
    print(i,  hash.get(i,0))

     
     

