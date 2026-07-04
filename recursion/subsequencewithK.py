nums=[1,2,3,4,5,6,7,8,9,10,2,3,4,5,7,8,9]
k=10
ls=[]
ans=[]
def rec(i,ls):
                if i >=len(nums):
                    return 
                if sum(ls)==k:
                    ans.append(ls.copy())
                ls.append(nums[i])
                rec(i+1,ls)
                ls.pop()
                rec(i+1,ls)
                
i=0  
rec(i,ls)
a=[]
for u in ans:
        if u not in a:
            a.append(u)
print(a)