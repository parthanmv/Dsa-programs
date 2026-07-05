nums=[1,2,3,4,5,6,7,8,9,10,2,3,4,5,7,8,9]
k=1000
ls=[]
ans=[]
def rec(i,ls):
                if i >=len(nums):
                    return False
                if sum(ls)==k:
                    return True
                ls.append(nums[i])
                if rec(i+1,ls):
                    return True
                ls.pop()
                if  rec(i+1,ls):
                    return True
                return False
                
i=0  

print(rec(i,ls))