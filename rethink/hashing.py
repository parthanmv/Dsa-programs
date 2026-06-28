s="azyuyyzaaaa"
q="d","a","y","u"
ls=[]
ls=s
hash={}
for i in range(0,len(ls)-1):
    hash[ls[i]]=hash.get(ls[i],0)+1
print(hash)
for i in q:
    print(i,hash.get(i,0))