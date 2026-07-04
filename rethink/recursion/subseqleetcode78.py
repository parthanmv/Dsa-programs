nums=[1,2,3,4,5,6,7]
ls=[]
ans=[]
def rec(i,ls):
            if i >=len(nums):
                ans.append(ls.copy())
                return 
            ls.append(nums[i])
            rec(i+1,ls)
            ls.pop()
            rec(i+1,ls)
            
i=0  
rec(i,ls)
print(ans)