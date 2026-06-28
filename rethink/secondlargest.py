nums=[1,2,9,7,6,5,4,3,7,10,100,99,1,4,5,7,6]
sl=float('-inf')
l=float('-inf')

for i in range(0,len(nums)):
    if nums[i]> l:
        sl=l
        l=nums[i]
    elif nums[i]>sl and nums[i] != l:
        sl=nums[i]
print("sl:",sl,"l:",l)