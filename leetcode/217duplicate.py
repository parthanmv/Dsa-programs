nums=[1,1,1,3,3,4,3,2,4,2]
hash={}
n=len(nums)
for i in range(0,n):
    hash[nums[i]]=hash.get(nums[i],0)+1
for i in range(0,len(nums)-1):
         if hash[nums[i]] > 1:
                 print(True)
                 break
print(False)