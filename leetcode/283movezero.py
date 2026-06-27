
nums=[4,2,4,0,0,3,0,5,1,0]
i=0
j=i+1

while i < j and i<len(nums) and j<len(nums):
            if nums[i]==0 and nums[j]!=0 :
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i]!=0 and nums[j]==0 : 
                i+=1
                j+=1
            else :
               j+=1
print(nums)