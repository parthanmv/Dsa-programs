
nums=[0,0,1,1,1,2,2,3,3,4]
hash={}
for i in range(len(nums)):
  hash[nums[i]]=hash.get(nums[i],0)+1
a=[]*len(hash)  
for i in hash:
    a.append(i)
print(a)    